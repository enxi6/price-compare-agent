"""Collect identifier-bearing quotes from Shopify public product JSON.

Reads ``data/shopify_handles.json`` (one pinned variant per entry) and,
for each entry, fetches the store's public product JSON
(``/products/<handle>.js``, falling back to ``.json``) and writes the
pinned variant's price + barcode/SKU into
``data/eval_snapshots_identified_YYYY-MM-DD.json`` in the identified
snapshot schema (see IDENTIFIED_SOURCE_DESIGN_DRAFT.md §1 / DECISIONS
059).

This is a tier-1 source (DECISIONS 004): Shopify's public product JSON
is an official public product interface, not scraping. One request per
configured product, paced (default 12 s between requests) with retry on
rate-limit responses; any block or non-200 response stops that entry
with a logged warning instead of retrying around it (DECISIONS 004).

Safety rules enforced here, not downstream:
- Only the pinned variant (by ``variant_id``, or the single variant
  when a product has exactly one) is ever written. A multi-variant
  product with no pinned id is skipped, never guessed.
- Variants whose title or handle contains "bundle" are skipped:
  a bundle's barcode must never be recorded against the standalone
  model (DECISIONS 021).
- The identifier is recorded exactly as the store states it
  (``barcode`` preferred, else ``sku``); normalization happens at
  merge time. Whether it matches the catalog is decided by the merge
  (``identity.match_offers``), never here.

Usage:
    python3 -m price_agent.collect_identified
    python3 -m price_agent.collect_identified --merchants Keychron,HyperX
    python3 -m price_agent.collect_identified --products keychron-k8-ultra-8k
    python3 -m price_agent.collect_identified --out data/eval_snapshots_identified_2026-11-07.json
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

from .adapters_shopify import USER_AGENT
from .catalog import EVAL_SET

DEFAULT_CONFIG = "data/shopify_handles.json"
BUNDLE_WORDS = ("bundle",)


class CollectError(Exception):
    pass


def _price_from_payload(value, endpoint: str) -> float:
    """Shopify ``.js`` prices are integer cents; ``.json`` prices are
    dollar strings. The endpoint decides the unit; never guess."""
    if endpoint == ".js":
        if isinstance(value, bool) or not isinstance(value, int):
            raise CollectError(f".js price is not integer cents: {value!r}")
        return value / 100.0
    return float(value)


def _identifier_from_variant(variant: dict) -> tuple[str, str] | None:
    """Return (identifier, kind) or None when the variant states none.

    ``barcode`` preferred: 12 digits -> UPC, 13/14 digits -> EAN,
    anything else non-empty -> SKU (a store may put an MPN in barcode).
    Fall back to ``sku`` -> SKU. Kind is provenance only; matching is
    value-based at merge time.
    """
    barcode = (variant.get("barcode") or "").strip()
    if barcode:
        if barcode.isdigit() and len(barcode) == 12:
            return barcode, "UPC"
        if barcode.isdigit() and len(barcode) in (13, 14):
            return barcode, "EAN"
        return barcode, "SKU"
    sku = (variant.get("sku") or "").strip()
    if sku:
        return sku, "SKU"
    return None


def _pick_variant(product: dict, entry: dict) -> tuple[dict, str]:
    """Return (variant, how) or raise CollectError when unresolvable."""
    variants = product.get("variants", [])
    if not variants:
        raise CollectError("product JSON has no variants")
    variant_id = entry.get("variant_id")
    if variant_id is not None:
        for variant in variants:
            if variant.get("id") == variant_id:
                return variant, "pinned variant_id"
        raise CollectError(
            f"variant_id {variant_id} not in product JSON "
            f"({len(variants)} variants)"
        )
    if len(variants) == 1:
        return variants[0], "single variant"
    raise CollectError(
        f"{len(variants)} variants and no variant_id pinned; "
        "refusing to guess — hand-pin variant_id in the config"
    )


def _fetch_product_json(store: str, handle: str, opener) -> tuple[dict, str]:
    """Fetch ``.js`` then ``.json``; return (payload, endpoint used)."""
    for endpoint in (".js", ".json"):
        url = f"https://{store}/products/{handle}{endpoint}"
        request = urllib.request.Request(
            url, headers={"User-Agent": USER_AGENT}
        )
        try:
            with opener(request, timeout=15) as response:
                return json.load(response), endpoint
        except urllib.error.HTTPError as exc:
            if exc.code in (429, 500, 502, 503):
                raise CollectError(
                    f"{url} returned HTTP {exc.code} (rate-limit/server)"
                ) from exc
            if endpoint == ".js":
                continue  # try .json before giving up
            raise CollectError(f"{url} returned HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise CollectError(f"{url} fetch failed: {exc}") from exc
    raise CollectError(f"no usable product JSON for {store}/{handle}")


def collect_entry(entry: dict, opener, now: datetime) -> dict:
    """Collect one configured entry into an identified offer row."""
    for field in ("product_key", "merchant", "store", "handle"):
        if not entry.get(field):
            raise CollectError(f"config entry missing {field!r}: {entry!r}")
    store = entry["store"]
    handle = entry["handle"]
    title_lower = handle.lower()
    if any(word in title_lower for word in BUNDLE_WORDS):
        raise CollectError(f"handle looks like a bundle: {handle}")
    payload, endpoint = _fetch_product_json(store, handle, opener)
    # ``.js`` returns the product object at the top level; ``.json``
    # wraps it in a ``product`` key. Normalize to the product dict.
    product = payload.get("product") or payload
    variant, how = _pick_variant(product, entry)
    variant_title = (variant.get("title") or "").strip()
    if any(word in variant_title.lower() for word in BUNDLE_WORDS):
        raise CollectError(
            f"variant title looks like a bundle: {variant_title!r}"
        )
    identified = _identifier_from_variant(variant)
    if identified is None:
        raise CollectError("variant states neither barcode nor sku")
    identifier, kind = identified
    try:
        price = _price_from_payload(variant["price"], endpoint)
    except (KeyError, TypeError, ValueError) as exc:
        raise CollectError(f"variant price unreadable: {exc}") from exc
    title = product.get("title", handle)
    full_title = title if variant_title in ("", "Default Title") else (
        f"{title} - {variant_title}"
    )
    variant_id = variant.get("id")
    url = f"https://{store}/products/{handle}"
    if variant_id is not None:
        url += f"?variant={variant_id}"
    available = variant.get("available")
    return {
        "merchant": entry["merchant"],
        "price": price,
        "title": full_title,
        "url": url,
        "collected_at": now.isoformat(),
        "identifier": identifier,
        "identifier_kind": kind,
        "source_tier": 1,
        "source": f"shopify:{store}",
        "in_stock": True if available is None else bool(available),
        "_debug": {"endpoint": endpoint, "variant_match": how},
    }


def collect(config_path: str, opener=None, merchants=None, products=None,
            pace_seconds: float = 12.0, sleep=time.sleep,
            now: datetime | None = None) -> dict:
    """Run the sweep; return the identified snapshot dict.

    Failures are per-entry warnings, never fatal: a blocked store must
    not kill the whole sweep. ``now`` is injectable for tests.
    """
    if opener is None:
        opener = urllib.request.urlopen
    now = now or datetime.now(timezone.utc)
    with open(config_path, encoding="utf-8") as handle:
        config = json.load(handle)
    known_keys = {p.key for p in EVAL_SET}
    models: dict[str, list[dict]] = {}
    collected = skipped = 0
    first_fetch = True
    for entry in config["entries"]:
        if merchants and entry["merchant"] not in merchants:
            continue
        if products and entry["product_key"] not in products:
            continue
        if entry["product_key"] not in known_keys:
            print(f"SKIP unknown catalog key: {entry['product_key']}")
            skipped += 1
            continue
        if not first_fetch:
            sleep(pace_seconds)
        first_fetch = False
        try:
            row = collect_entry(entry, opener, now)
        except CollectError as exc:
            print(
                f"SKIP {entry['product_key']} @ {entry['merchant']}: {exc}"
            )
            skipped += 1
            continue
        debug = row.pop("_debug")
        models.setdefault(entry["product_key"], []).append(row)
        collected += 1
        print(
            f"OK {entry['product_key']} @ {entry['merchant']}: "
            f"${row['price']:.2f} {row['identifier_kind']} "
            f"{row['identifier']} ({debug['endpoint']}, "
            f"{debug['variant_match']})"
        )
    return {
        "meta": {
            "collected_at": now.isoformat().replace("+00:00", "Z"),
            "source": "shopify public product JSON sweep",
            "source_tier": 1,
            "identified": True,
            "generated_by": "price_agent/collect_identified.py",
        },
        "models": {
            key: {"offers": offers} for key, offers in sorted(models.items())
        },
        "_counts": {"collected": collected, "skipped": skipped},
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Collect identifier-bearing Shopify quotes."
    )
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--out", default=None)
    parser.add_argument("--merchants", default=None,
                        help="comma-separated merchant names to include")
    parser.add_argument("--products", default=None,
                        help="comma-separated catalog keys to include")
    parser.add_argument("--pace", type=float, default=12.0,
                        help="seconds between requests (default 12)")
    args = parser.parse_args()

    merchants = (
        {m.strip() for m in args.merchants.split(",")} if args.merchants
        else None
    )
    products = (
        {p.strip() for p in args.products.split(",")} if args.products
        else None
    )
    result = collect(
        args.config, merchants=merchants, products=products,
        pace_seconds=args.pace,
    )
    counts = result.pop("_counts")
    out = args.out or (
        "data/eval_snapshots_identified_"
        f"{datetime.now(timezone.utc).date().isoformat()}.json"
    )
    with open(out, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, ensure_ascii=False)
    print(
        f"wrote {out}: {len(result['models'])} models, "
        f"{counts['collected']} offers collected, "
        f"{counts['skipped']} skipped"
    )


if __name__ == "__main__":
    main()
