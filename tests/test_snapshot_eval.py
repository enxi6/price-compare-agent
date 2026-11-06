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
    assert len(EVAL_SET) == 190
    verified = [p for p in EVAL_SET if p.status == "verified"]
    assert len(verified) == 94
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
        "keychron-b39-deep-black",
        "anker-maggo-2-pro-phantom-gray",
        "anker-prime-power-bank-26k-300w-black",
        "anker-desktop-usb-c-hub-10-in-1",
        "anker-prime-wireless-car-charger",
        "anker-nano-charger-70w-3-ports-black-stone",
        "jbl-tour-one-m3-smart-tx-black",
        "jbl-tour-pro-3-black",
        "jbl-bar-1300xmk2-black",
        "jbl-partybox-stage-320-black",
        "razer-viper-v4-pro-black",
        "razer-blackwidow-v4-pro-green-black",
        "razer-blackshark-v3-pro-black",
        "razer-wolverine-v3-pro-black",
        "razer-kraken-v4-pro-black",
        "corsair-m65-rgb-ultra-black",
        "corsair-k65-plus-wireless-midnight-grey",
        "corsair-virtuoso-max-wireless-carbon",
        "corsair-frame-4000d-rs-argb-black",
        "corsair-titan-ii-360-rx-rgb-black",
        "alienware-27-qd-oled-aw2726dm",
        "alienware-pro-wireless-gaming-keyboard-dark-side-of-the-moon",
        "alienware-pro-wireless-gaming-headset-dark-side-of-the-moon",
        "hp-omen-27s-black",
        "hyperx-cloud-iii-black-red",
        "hp-omen-27q-g2-black",
        "hyperx-alloy-rise-75-black",
        "hp-omen-27k-black",
        "hyperx-omen-oled-27q-black",
        "hyperx-pulsefire-haste-2-pro-slate-grey",
        "hyperx-quadcast-2-s-black",
        "asus-rog-swift-oled-pg27ucwm-black",
        "asus-rog-delta-ii-black",
        "asus-rog-gladius-iv-ace-black",
        "asus-rog-azoth-96-he-black",
        "asus-rog-cetra-open-wireless-black",
        "dell-27-plus-4k-monitor-s2725qs",
        "alienware-32-curved-gaming-monitor-aw3225dm",
        "alienware-tri-mode-wireless-gaming-keyboard-aw920k-dark-side-of-the-moon",
        "dell-pro-7-webcam-4k-wb726",
        "asus-rog-swift-oled-pg32ucwm-black",
        "asus-rog-swift-oled-pg27aqdpr-black",
        "asus-rog-delta-usb-c-black",
        "asus-rog-harpe-mini-core-black",
        "asus-rog-pelta-black",
        "lenovo-legion-tab-gen-3-eclipse-black",
        "lenovo-tab-plus-gen-2-celestial-white",
        "lenovo-idea-tab-pro-gen-2-cloud-grey",
        "lenovo-tab-one-luna-grey",
        "lenovo-yoga-tab-plus-gen-2-cosmic-blue",
        "xbox-series-s-512gb-robot-white",
        "xbox-wireless-headset-2024-black",
        "microsoft-surface-laptop-13-8-8th-edition-platinum",
        "garmin-fenix-9-47mm-titanium-pebble-gray",
        "lenovo-yoga-tab-gen-2-cosmic-blue",
        "lenovo-idea-tab-luna-grey",
        "lenovo-idea-tab-plus-cloud-grey",
        "asus-rog-swift-oled-pg27ucdm-black",
        "samsung-galaxy-watch9-40mm-graphite",
        "samsung-galaxy-tab-s11-128gb-gray",
        "samsung-galaxy-tab-s11-ultra-256gb-gray",
        "keychron-k2-he-special-black",
        "dell-ultrasharp-27-4k-thunderbolt-hub-monitor-u2725qe",
        "keychron-k2-max-black-rgb-aluminum-banana",
        "hyperx-cloud-iii-black"}


def test_evaluate_counts_fixture_snapshot(tmp_path):
    result = evaluate(_snapshot(tmp_path))
    assert result["models"] == 190
    assert result["total_offers"] == 1
    # No UPC in snapshots -> everything lands in "suspected", by design.
    assert result["matched"] == 0 and result["suspected"] == 1
