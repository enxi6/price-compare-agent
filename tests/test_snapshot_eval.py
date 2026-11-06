"""Tests for snapshots and the eval harness (offline fixtures only)."""

import json
from datetime import datetime, timezone

from price_agent.catalog import EVAL_SET
from price_agent.evaluate import evaluate
from price_agent.snapshots import SnapshotAdapter, snapshot_age_hours


def _snapshot(tmp_path):
    data = {
        "meta": {"collected_at": "2026-10-31T22:42:00Z", "source": "test"},
        "models": {
            "sony-wh1000xm5-black": {
                "offers": [
                    {"merchant": "Dell", "title": "Sony WH-1000XM5 Black",
                     "price": 399.99, "url": "https://example.com/dell"},
                ]
            }
        },
    }
    path = tmp_path / "snap.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return str(path)


def test_snapshot_offers_carry_no_identifier(tmp_path):
    offers = SnapshotAdapter(_snapshot(tmp_path),
                             "sony-wh1000xm5-black").search("")
    assert len(offers) == 1
    assert offers[0].identifier is None  # title match only, by design
    assert offers[0].shipping is None


def test_snapshot_staleness(tmp_path):
    snapshot = {"meta": {"collected_at": "2026-10-31T22:42:00Z"}}
    now = datetime(2026, 11, 1, 23, 42, tzinfo=timezone.utc)
    assert snapshot_age_hours(snapshot, now) == 25.0


def test_eval_set_shape():
    assert len(EVAL_SET) == 100
    verified = [p for p in EVAL_SET if p.status == "verified"]
    assert len(verified) == 68
    assert all(p.identifiers for p in verified)
    pending = [p for p in EVAL_SET if p.status == "pending"]
    assert all(not p.identifiers for p in pending)
    assert {p.key for p in pending} == {
        "sony-dualsense-white", "apple-macbook-pro-14-m6",
        "apple-watch-series-12-42mm-gps-black",
        "apple-watch-ultra-4-49mm-gps-cellular-natural",
        "sony-dualsense-edge-black-white",
        "logitech-g-pro-x-superlight-2-dex-black",
        "apple-macbook-neo-13-256gb-blush",
        "sony-wh1000xm4c-black",
        "sony-pulse-elite-midnight-black",
        "sony-pulse-explore-midnight-black",
        "logitech-wave-keys-graphite",
        "bose-sport-open-earbuds-black",
        "sony-access-controller-white",
        "logitech-pop-keys-cosmos",
        "xbox-elite-series-2-core-white",
        "xbox-adaptive-controller",
        "apple-magic-keyboard-touch-id-numeric-keypad-white",
        "logitech-pro-x-tkl-lightspeed-tactile-black",
        "keychron-q1-knob-navy-blue-red",
        "apple-macbook-pro-14-proled-xdr",
        "sony-wf-c510-black",
        "sony-inzone-h5-black",
        "logitech-pro-x2-superstrike-lunar-eclipse",
        "keychron-b40-deep-black",
        "sony-mdr-7506",
        "sony-pulse-headset-white",
        "sony-linkbuds-clip-black",
        "nintendo-n64-controller",
        "apple-studio-display-xdr-standard-tilt-height",
        "sony-mdr-m1",
        "sony-mdr-mv1",
        "keychron-b39-deep-black"}


def test_evaluate_counts_fixture_snapshot(tmp_path):
    result = evaluate(_snapshot(tmp_path))
    assert result["models"] == 100
    assert result["total_offers"] == 1
    # No UPC in snapshots -> everything lands in "suspected", by design.
    assert result["matched"] == 0 and result["suspected"] == 1
