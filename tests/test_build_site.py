"""Tests for the static-site generator (offline fixtures only)."""

import json

from price_agent.build_site import build_site


def _snapshot(tmp_path):
    data = {
        "meta": {
            "generated_at": "2026-11-06T20:00:00Z",
            "snapshot_date": "2026-11-06",
            "source_files": 1,
            "models": 200,
            "verified_identifiers": 98,
            "pending_identifiers": 102,
            "total_offers": 2,
            "models_with_offers": 1,
            "note": "test fixture",
        },
        "models": [
            {
                "key": "sony-wh1000xm5-black",
                "brand": "Sony",
                "model": "WH-1000XM5",
                "variant": "Black (WH1000XM5/B)",
                "category": "headphones",
                "status": "verified",
                "identifiers": {"UPC": "027242923232"},
                "offers": [
                    {
                        "merchant": "Dell",
                        "price": 379.99,
                        "title": "Sony WH-1000XM5 Black",
                        "url": "https://example.com/dell",
                        "collected_at": "2026-11-06T20:00:00Z",
                        "identifier": None,
                        "suspected": True,
                    }
                ],
                "source_file": "eval_snapshots_2026-11-06.json",
                "source_collected_at": "2026-11-06T20:00:00Z",
            },
            {
                "key": "sony-dualsense-white",
                "brand": "Sony",
                "model": "DualSense",
                "variant": "White",
                "category": "controllers",
                "status": "pending",
                "identifiers": {},
                "offers": [],
                "source_file": "eval_snapshots_2026-11-06.json",
                "source_collected_at": "2026-11-06T20:00:00Z",
            },
        ],
    }
    path = tmp_path / "site_snapshot.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return str(path)


def test_build_site_renders_all_pages(tmp_path):
    result = build_site(_snapshot(tmp_path), str(tmp_path / "site"))
    assert result["pages"] == 5  # index, method, coverage + 2 products
    assert result["models"] == 2
    assert (tmp_path / "site" / "index.html").exists()
    assert (tmp_path / "site" / "method.html").exists()
    assert (tmp_path / "site" / "coverage.html").exists()
    assert (tmp_path / "site" / "products" / "sony-wh1000xm5-black.html").exists()
    assert (tmp_path / "site" / "products" / "sony-dualsense-white.html").exists()


def test_product_page_never_fakes_a_verified_ranking(tmp_path):
    build_site(_snapshot(tmp_path), str(tmp_path / "site"))
    page = (tmp_path / "site" / "products" / "sony-wh1000xm5-black.html").read_text()
    assert "Verified ranking: empty" in page
    assert "Title-matched offers" in page
    assert "shipping unknown" in page
    assert "Needs re-check" in page or "Current" in page


def test_product_page_with_no_quotes_says_so(tmp_path):
    build_site(_snapshot(tmp_path), str(tmp_path / "site"))
    page = (tmp_path / "site" / "products" / "sony-dualsense-white.html").read_text()
    assert "No quotes in the latest snapshot" in page
    assert "Identifier pending" in page


def test_home_search_says_not_indexed_for_unknown_models(tmp_path):
    build_site(_snapshot(tmp_path), str(tmp_path / "site"))
    page = (tmp_path / "site" / "index.html").read_text()
    assert "Not indexed" in page
    assert "never invent results" in page
