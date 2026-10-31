"""Snapshot adapter: checked-in price snapshots as traceable data.

A snapshot file (see data/eval_snapshots.json) records real catalog
listings with merchant, price, URL and collection time. The catalog
source does not return UPCs, so snapshot offers carry identifier=None:
identity matching therefore puts them in the "suspected" (title-matched)
table, never in the matched ranking, until a source returns a real
identifier. That is the rule working as designed, not a bug.

Snapshots do not assert stock and do not carry shipping/tax: shipping
stays unknown, tax stays 0, and the CLI must say stock needs checking
at the merchant page. Prices older than 24h are stale (PLAN.md) and the
CLI flags them for re-check instead of presenting them as live.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone

from .adapters import MerchantAdapter
from .models import Offer

STALE_AFTER_HOURS = 24.0


def load_snapshot(path: str) -> dict:
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def snapshot_age_hours(snapshot: dict, now: datetime | None = None) -> float:
    collected = datetime.fromisoformat(
        snapshot["meta"]["collected_at"].replace("Z", "+00:00")
    )
    now = now or datetime.now(timezone.utc)
    return (now - collected).total_seconds() / 3600.0


class SnapshotAdapter(MerchantAdapter):
    """Offers for one eval model key from a snapshot file."""

    def __init__(self, path: str, model_key: str):
        self.snapshot = load_snapshot(path)
        self.model_key = model_key
        self.name = f"snapshot:{model_key}"

    def search(self, query: str) -> list[Offer]:
        collected_at = self.snapshot["meta"]["collected_at"]
        offers: list[Offer] = []
        for entry in self.snapshot["models"].get(self.model_key, {}).get(
            "offers", []
        ):
            offers.append(
                Offer(
                    merchant=entry["merchant"],
                    title=entry["title"],
                    identifier=None,  # catalog source gives no UPC
                    price=float(entry["price"]),
                    shipping=None,
                    tax_estimate=0.0,
                    url=entry["url"],
                    in_stock=True,  # snapshot does not assert stock; see note
                    fetched_at=collected_at,
                )
            )
        return offers
