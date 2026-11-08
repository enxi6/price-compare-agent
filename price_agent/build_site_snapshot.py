"""Build the consolidated site snapshot from all eval snapshots.

Reads every ``data/eval_snapshots*.json`` file (Meta Catalog stream,
no identifiers) and every ``data/eval_snapshots_identified_*.json``
file (identifier-bearing quotes, e.g. Shopify public product JSON)
and, for each of the 200 catalog models, merges the two streams into
one offer list. Snapshot keys that are not in the current catalog
(retired entries, e.g. ``keychron-k8-pro``) are ignored, never added:
the output is exactly the 200 catalog models.

Merge rules (DECISIONS 002/021/059/066):
- Meta stream: latest ``meta.collected_at`` per model wins (each Meta
  snapshot is a full refresh).
- Identified stream: UNION across files per model (each identified
  file is an incremental collection covering different merchants —
  Shopify pins, retries, hand-verified rows). Latest-per-model on
  this stream was a bug: it silently dropped hand rows whenever a
  newer collector file mentioned the same model (it dropped the
  Switch 2 Micro Center row in favour of a BrandsMart row).
- The two streams union; an identified file never wholesale-replaces
  a model's Meta rows.
- An identified row supersedes a Meta row only when it is MATCHED
  (its identifier equals a catalog verified identifier) and shares
  the Meta row's merchant and price. A mismatched identified row is a
  different variant: it joins the suspected table and supersedes
  nothing.
- The verified ranking is decided only by ``identity.match_offers``:
  matched -> ``suspected: False``; everything else -> suspected.
  Pending models (no verified identifier) can never have a matched
  offer; the build fails rather than publishing one.
- Identifiers come only from identified files (recorded exactly as
  the source stated them), prices only from snapshots, and nothing
  is invented: a model whose latest snapshots have no offers keeps
  an empty offers list.

Usage:
    python3 -m price_agent.build_site_snapshot
    python3 -m price_agent.build_site_snapshot --out data/site_snapshot_2026-11-06.json
"""

from __future__ import annotations

import argparse
import glob
import json
import os
from datetime import datetime, timezone

from .catalog import EVAL_SET
from .identity import match_offers, normalize_identifier
from .models import Offer
from .ranking import rank_offers

SNAPSHOT_GLOB = "data/eval_snapshots*.json"
IDENTIFIED_GLOB = "data/eval_snapshots_identified_*.json"
DEFAULT_OUT = "data/site_snapshot_2026-11-06.json"


def _parse_collected_at(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _is_identified_path(path: str) -> bool:
    return os.path.basename(path).startswith("eval_snapshots_identified_")


def load_snapshot_files(pattern: str = SNAPSHOT_GLOB) -> list[dict]:
    """Load every snapshot file, sorted by path for determinism."""
    files = []
    for path in sorted(glob.glob(pattern)):
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
        files.append({"path": path, "data": data})
    return files


def load_meta_files() -> list[dict]:
    """Meta stream: every eval snapshot except identified files."""
    return [
        entry
        for entry in load_snapshot_files()
        if not _is_identified_path(entry["path"])
    ]


def _latest_per_model(files: list[dict]) -> dict[str, tuple[datetime, str, list[dict]]]:
    """Latest observation per model key: (collected_at, source_path, offers)."""
    latest: dict[str, tuple[datetime, str, list[dict]]] = {}
    for entry in files:
        path = entry["path"]
        data = entry["data"]
        collected_at = _parse_collected_at(data["meta"]["collected_at"])
        for key, model_data in data.get("models", {}).items():
            offers = model_data.get("offers", [])
            if key not in latest or collected_at > latest[key][0]:
                latest[key] = (collected_at, path, offers)
    return latest


def _union_identified(files: list[dict]) -> dict[str, tuple[datetime, str, list[dict]]]:
    """Union of identified rows per model key across files.

    Returns the same (collected_at, source_path, offers) shape as
    ``_latest_per_model``: collected_at / source_path are the newest
    contributing file's, offers are the concatenation of every file's
    rows (deduped downstream by ``_identified_dedupe``).

    Identified files are incremental collections covering different
    merchants, so they complement each other — unioning is the only
    correct semantic. Latest-per-model here was a bug (DECISIONS
    066): the hand file's ``meta.collected_at`` is stale (from its
    creation), so a newer collector file mentioning the same model
    silently discarded its hand-verified rows.
    """
    union: dict[str, tuple[datetime, str, list[dict]]] = {}
    for entry in files:
        path = entry["path"]
        data = entry["data"]
        collected_at = _parse_collected_at(data["meta"]["collected_at"])
        for key, model_data in data.get("models", {}).items():
            offers = list(model_data.get("offers", []))
            if key not in union:
                union[key] = (collected_at, path, offers)
            else:
                prev_at, prev_path, prev_offers = union[key]
                if collected_at > prev_at:
                    union[key] = (
                        collected_at, path, prev_offers + offers,
                    )
                else:
                    union[key] = (
                        prev_at, prev_path, prev_offers + offers,
                    )
    return union


def _exact_dedupe(rows: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for row in rows:
        key = (
            row["merchant"],
            float(row["price"]),
            row.get("title", ""),
            row.get("url", ""),
        )
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def _identified_dedupe(rows: list[dict]) -> list[dict]:
    """Collapse identified rows on (merchant, normalized identifier, price).

    Keeps the lowest source_tier, then earliest collected_at, then
    shortest url — the same merchant selling the same identified
    product at the same price is one offer, however often collected.
    """
    best: dict[tuple, dict] = {}
    for row in rows:
        key = (
            row["merchant"].strip().casefold(),
            normalize_identifier(row["identifier"]),
            round(float(row["price"]), 2),
        )
        current = best.get(key)
        if current is None:
            best[key] = row
            continue
        candidate_rank = (
            row.get("source_tier") or 99,
            row.get("collected_at") or "",
            len(row.get("url") or ""),
        )
        current_rank = (
            current.get("source_tier") or 99,
            current.get("collected_at") or "",
            len(current.get("url") or ""),
        )
        if candidate_rank < current_rank:
            best[key] = row
    return list(best.values())


def _to_offer(row: dict, collected_at: str) -> Offer:
    return Offer(
        merchant=row["merchant"],
        title=row.get("title", ""),
        identifier=row.get("identifier"),
        price=float(row["price"]),
        shipping=None,
        tax_estimate=0.0,
        url=row.get("url", ""),
        in_stock=row.get("in_stock", True),
        fetched_at=row.get("collected_at") or collected_at,
    )


def build_site_snapshot(snapshot_files: list[dict] | None = None,
                        identified_files: list[dict] | None = None) -> dict:
    """Merge snapshots into one per-model record for the whole catalog.

    Returns a dict with ``meta`` (counts, source files, generation time)
    and ``models`` (one entry per catalog model, in catalog order).
    When ``snapshot_files`` is passed explicitly (tests), the identified
    stream defaults to empty so fixtures stay hermetic; the real run
    loads both globs.
    """
    if snapshot_files is None:
        snapshot_files = load_meta_files()
        if identified_files is None:
            identified_files = load_snapshot_files(IDENTIFIED_GLOB)
    elif identified_files is None:
        identified_files = []

    for entry in snapshot_files:
        if entry["data"].get("meta", {}).get("identified"):
            raise ValueError(
                f"Meta stream file {entry['path']} carries "
                "meta.identified=true; move it to the identified stream"
            )
    for entry in identified_files:
        if not entry["data"].get("meta", {}).get("identified"):
            raise ValueError(
                f"Identified stream file {entry['path']} lacks "
                "meta.identified=true; the filename prefix and the meta "
                "flag must agree"
            )

    meta_latest = _latest_per_model(snapshot_files)
    identified_latest = _union_identified(identified_files)

    all_dates = [
        _parse_collected_at(entry["data"]["meta"]["collected_at"])
        for entry in snapshot_files + identified_files
    ]
    snapshot_date = (
        max(all_dates).date().isoformat() if all_dates
        else datetime.now(timezone.utc).date().isoformat()
    )

    models_out = []
    total_offers = 0
    matched_offers = 0
    verified_ranking_models = 0
    for product in EVAL_SET:
        collected_at, source_path, meta_offers = meta_latest.get(
            product.key, (None, None, [])
        )
        id_collected_at, id_source_path, id_offers = identified_latest.get(
            product.key, (None, None, [])
        )

        meta_rows = [
            {
                "merchant": offer["merchant"],
                "price": float(offer["price"]),
                "title": offer.get("title", ""),
                "url": offer.get("url", ""),
                "collected_at": (
                    collected_at.isoformat() if collected_at else None
                ),
                "identifier": None,
                "identifier_kind": None,
                "source_tier": None,
                "source": "meta-catalog",
                "in_stock": offer.get("in_stock", True),
            }
            for offer in _exact_dedupe(meta_offers)
        ]
        identified_rows = [
            {
                "merchant": offer["merchant"],
                "price": float(offer["price"]),
                "title": offer.get("title", ""),
                "url": offer.get("url", ""),
                "collected_at": offer.get("collected_at"),
                "identifier": offer["identifier"],
                "identifier_kind": offer.get("identifier_kind"),
                "source_tier": offer.get("source_tier"),
                "source": offer.get("source"),
                "in_stock": offer.get("in_stock", True),
            }
            for offer in _identified_dedupe(_exact_dedupe(id_offers))
            if offer.get("identifier")
        ]

        # Match gate: only identity.match_offers decides the ranking.
        merged = meta_rows + identified_rows
        offers = [
            _to_offer(
                row,
                (collected_at.isoformat() if collected_at else ""),
            )
            for row in merged
        ]
        matched, _suspected = match_offers(offers, product)
        if not product.identifiers:
            # Pending models can never have a verified ranking. The
            # matcher already returns ([], all) for them; this guard
            # fails the build rather than publishing a contradiction.
            assert not matched, (
                f"pending model {product.key} has matched offers"
            )
        matched_ids = {id(o) for o in matched}

        # Supersede: a MATCHED identified row replaces the Meta row
        # with the same merchant and price (it carries the identifier
        # the Meta row lacks). Mismatched rows supersede nothing.
        matched_rows = [
            row for row, offer in zip(merged, offers)
            if id(offer) in matched_ids
        ]
        meta_keep = []
        for row in meta_rows:
            dropped = any(
                mrow["merchant"].strip().casefold()
                == row["merchant"].strip().casefold()
                and round(mrow["price"], 2) == round(row["price"], 2)
                for mrow in matched_rows
                if mrow.get("identifier") is not None
            )
            if not dropped:
                meta_keep.append(row)
        identified_keep = [
            row for row in identified_rows
        ]
        kept = meta_keep + identified_keep
        kept_offers = [
            _to_offer(
                row,
                (collected_at.isoformat() if collected_at else ""),
            )
            for row in kept
        ]
        kept_matched, _kept_suspected = match_offers(kept_offers, product)
        if not product.identifiers:
            assert not kept_matched, (
                f"pending model {product.key} has matched offers"
            )
        kept_matched_ids = {id(o) for o in kept_matched}
        ranked = rank_offers(kept_matched)
        suspected_rows = [
            dict(row)
            for row, offer in zip(kept, kept_offers)
            if id(offer) not in kept_matched_ids
        ]
        suspected_rows.sort(key=lambda o: (o["price"], o["merchant"]))
        # Re-emit rows in ranked-then-suspected order, flags from the
        # split. Paired by position, never by value: two rows may
        # share merchant/price/title and still be different offers.
        # split. Paired by position, never by value: two rows may
        # share merchant/price/title and still be different offers.
        ordered = []
        for offer in ranked:
            # rank_offers returns the same Offer objects in sorted
            # order; locate them by identity.
            row = None
            for idx, candidate in enumerate(kept_offers):
                if candidate is offer:
                    row = dict(kept[idx])
                    break
            assert row is not None
            row["suspected"] = False
            ordered.append(row)
        for out_row in suspected_rows:
            out_row["suspected"] = True
            ordered.append(out_row)

        total_offers += len(ordered)
        matched_offers += len(ranked)
        if ranked:
            verified_ranking_models += 1
        models_out.append(
            {
                "key": product.key,
                "brand": product.brand,
                "model": product.model,
                "variant": product.variant,
                "category": product.category,
                "status": product.status,
                "identifiers": dict(product.identifiers),
                "offers": ordered,
                "source_file": (
                    os.path.basename(source_path) if source_path else None
                ),
                "source_collected_at": (
                    collected_at.isoformat() if collected_at else None
                ),
                "identified_source_file": (
                    os.path.basename(id_source_path)
                    if id_source_path else None
                ),
                "identified_collected_at": (
                    id_collected_at.isoformat()
                    if id_collected_at else None
                ),
            }
        )

    verified = sum(1 for p in EVAL_SET if p.status == "verified")
    return {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "snapshot_date": snapshot_date,
            "source_files": len(snapshot_files),
            "identified_source_files": len(identified_files),
            "models": len(models_out),
            "verified_identifiers": verified,
            "pending_identifiers": len(models_out) - verified,
            "total_offers": total_offers,
            "matched_offers": matched_offers,
            "suspected_offers": total_offers - matched_offers,
            "verified_ranking_models": verified_ranking_models,
            "models_with_offers": sum(
                1 for m in models_out if m["offers"]
            ),
            "note": (
                "Latest snapshot per model (by collected_at) from the "
                "Meta Catalog stream, unioned with identifier-bearing "
                "quotes (Shopify public product JSON and "
                "browser-verified retailer spec pages). An offer enters "
                "the verified ranking only when its identifier matches "
                "the catalog's verified identifier for that exact "
                "variant; everything else is title-matched (suspected). "
                "Prices are as of their snapshot date; anything older "
                "than 24h needs re-check."
            ),
        },
        "models": models_out,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merge eval snapshots into the site snapshot."
    )
    parser.add_argument("--out", default=DEFAULT_OUT)
    parser.add_argument("--glob", default=SNAPSHOT_GLOB)
    args = parser.parse_args()

    files = load_meta_files()
    identified = load_snapshot_files(IDENTIFIED_GLOB)
    result = build_site_snapshot(files, identified)
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, ensure_ascii=False)
    meta = result["meta"]
    print(
        f"wrote {args.out}: {meta['models']} models, "
        f"{meta['verified_identifiers']} verified / "
        f"{meta['pending_identifiers']} pending, "
        f"{meta['total_offers']} offers "
        f"({meta['matched_offers']} matched, "
        f"{meta['verified_ranking_models']} models with a verified "
        f"ranking) from {meta['source_files']} files + "
        f"{meta['identified_source_files']} identified files, "
        f"{meta['models_with_offers']} models with offers"
    )


if __name__ == "__main__":
    main()
