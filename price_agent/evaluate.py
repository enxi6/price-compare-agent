"""Evaluation harness: run the whole eval set through one data source.

Reports, per model and in total: verified identifiers, snapshot
coverage, matched offers (identifier match) and suspected offers
(title match only). A low matched rate on snapshot data is expected
until a source returns real identifiers -- the harness measures the
gap instead of hiding it behind title similarity.
"""

from __future__ import annotations

from .catalog import EVAL_SET
from .identity import match_offers
from .snapshots import SnapshotAdapter


def evaluate(snapshot_path: str) -> dict:
    rows = []
    total_offers = 0
    total_matched = 0
    total_suspected = 0
    for product in EVAL_SET:
        offers = SnapshotAdapter(snapshot_path, product.key).search("")
        matched, suspected = match_offers(offers, product)
        total_offers += len(offers)
        total_matched += len(matched)
        total_suspected += len(suspected)
        rows.append(
            {
                "key": product.key,
                "identifier_status": product.status,
                "offers": len(offers),
                "matched": len(matched),
                "suspected": len(suspected),
            }
        )
    return {
        "models": len(EVAL_SET),
        "verified_identifiers": sum(1 for p in EVAL_SET if p.status == "verified"),
        "with_snapshot_offers": sum(1 for r in rows if r["offers"] > 0),
        "total_offers": total_offers,
        "matched": total_matched,
        "suspected": total_suspected,
        "rows": rows,
    }
