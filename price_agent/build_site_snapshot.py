"""Build the consolidated site snapshot from all eval snapshots.

Reads every ``data/eval_snapshots*.json`` file and, for each of the 200
catalog models, keeps the offers from the snapshot with the latest
``meta.collected_at`` that contains that model. Snapshot keys that are
not in the current catalog (retired entries, e.g. ``keychron-k8-pro``)
are ignored, never added: the output is exactly the 200 catalog models.

Snapshot offers carry no identifier (the catalog source returns none),
so every offer in the output is flagged ``suspected: true`` with
``identifier: None`` -- title-matched only, never the verified ranking.
Nothing is invented here: identifiers come only from the catalog,
prices only from snapshots, and a model whose latest snapshot has no
offers keeps an empty offers list.

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

SNAPSHOT_GLOB = "data/eval_snapshots*.json"
DEFAULT_OUT = "data/site_snapshot_2026-11-06.json"


def _parse_collected_at(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def load_snapshot_files(pattern: str = SNAPSHOT_GLOB) -> list[dict]:
    """Load every snapshot file, sorted by path for determinism."""
    files = []
    for path in sorted(glob.glob(pattern)):
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
        files.append({"path": path, "data": data})
    return files


def build_site_snapshot(snapshot_files: list[dict] | None = None) -> dict:
    """Merge snapshots into one per-model record for the whole catalog.

    Returns a dict with ``meta`` (counts, source files, generation time)
    and ``models`` (one entry per catalog model, in catalog order).
    """
    if snapshot_files is None:
        snapshot_files = load_snapshot_files()

    # Latest observation per model key: (collected_at, source_path, offers).
    latest: dict[str, tuple[datetime, str, list[dict]]] = {}
    for entry in snapshot_files:
        path = entry["path"]
        data = entry["data"]
        collected_at = _parse_collected_at(data["meta"]["collected_at"])
        for key, model_data in data.get("models", {}).items():
            offers = model_data.get("offers", [])
            if key not in latest or collected_at > latest[key][0]:
                latest[key] = (collected_at, path, offers)

    models_out = []
    total_offers = 0
    for product in EVAL_SET:
        collected_at, source_path, offers = latest.get(
            product.key, (None, None, [])
        )
        clean_offers = []
        seen_rows = set()
        for offer in offers:
            row = (
                offer["merchant"],
                float(offer["price"]),
                offer.get("title", ""),
                offer.get("url", ""),
            )
            if row in seen_rows:
                continue
            seen_rows.add(row)
            clean_offers.append(
                {
                    "merchant": offer["merchant"],
                    "price": float(offer["price"]),
                    "title": offer.get("title", ""),
                    "url": offer.get("url", ""),
                    "collected_at": (
                        collected_at.isoformat() if collected_at else None
                    ),
                    "identifier": None,
                    "suspected": True,
                }
            )
        clean_offers.sort(key=lambda o: (o["price"], o["merchant"]))
        total_offers += len(clean_offers)
        models_out.append(
            {
                "key": product.key,
                "brand": product.brand,
                "model": product.model,
                "variant": product.variant,
                "category": product.category,
                "status": product.status,
                "identifiers": dict(product.identifiers),
                "offers": clean_offers,
                "source_file": (
                    os.path.basename(source_path) if source_path else None
                ),
                "source_collected_at": (
                    collected_at.isoformat() if collected_at else None
                ),
            }
        )

    verified = sum(1 for p in EVAL_SET if p.status == "verified")
    return {
        "meta": {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "snapshot_date": "2026-11-06",
            "source_files": len(snapshot_files),
            "models": len(models_out),
            "verified_identifiers": verified,
            "pending_identifiers": len(models_out) - verified,
            "total_offers": total_offers,
            "models_with_offers": sum(
                1 for m in models_out if m["offers"]
            ),
            "note": (
                "Latest snapshot per model (by collected_at). Offers carry "
                "no identifier: the catalog source returns none, so every "
                "offer is title-matched (suspected), never the verified "
                "ranking. Prices are as of their snapshot date; anything "
                "older than 24h needs re-check."
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

    files = load_snapshot_files(args.glob)
    result = build_site_snapshot(files)
    with open(args.out, "w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, ensure_ascii=False)
    meta = result["meta"]
    print(
        f"wrote {args.out}: {meta['models']} models, "
        f"{meta['verified_identifiers']} verified / "
        f"{meta['pending_identifiers']} pending, "
        f"{meta['total_offers']} offers from {meta['source_files']} files, "
        f"{meta['models_with_offers']} models with offers"
    )


if __name__ == "__main__":
    main()
