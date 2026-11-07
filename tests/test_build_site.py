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


def _snapshot_matched(tmp_path):
    """Like _snapshot(), but the XM5 model has one identifier-matched
    offer (Dell, UPC) plus a mismatched identified offer and a Meta
    suspected offer, and DualSense has a suspected identified row.
    """
    path = _snapshot(tmp_path)
    data = json.loads(open(path, encoding="utf-8").read())
    data["meta"].update({
        "verified_ranking_models": 1,
        "matched_offers": 1,
        "suspected_offers": 3,
        "identified_source_files": 1,
        "total_offers": 4,
        "models_with_offers": 2,
    })
    by_key = {m["key"]: m for m in data["models"]}
    xm5 = by_key["sony-wh1000xm5-black"]
    xm5["offers"] = [
        {"merchant": "Dell", "price": 379.99,
         "title": "Sony WH-1000XM5 Wireless Noise Canceling Headphones - Black",
         "url": "https://www.dell.com/en-us/shop/xm5/pd",
         "collected_at": "2026-11-07T10:00:00Z",
         "identifier": "027242923232", "identifier_kind": "UPC",
         "source_tier": 1, "source": "shopify:test-store",
         "suspected": False},
        {"merchant": "Adorama", "price": 389.99,
         "title": "Sony WH-1000XM5 Wireless Headphones - Silver",
         "url": "https://www.adorama.com/soxm5s.html",
         "collected_at": "2026-11-07T10:00:00Z",
         "identifier": "027242923249", "identifier_kind": "UPC",
         "source_tier": 1, "source": "shopify:test-store",
         "suspected": True},
        {"merchant": "Best Buy", "price": 399.99,
         "title": "Sony WH-1000XM5 Wireless Noise Canceling Headphones - Black",
         "url": "https://www.bestbuy.com/xm5",
         "collected_at": "2026-11-06T10:00:00Z",
         "identifier": None, "identifier_kind": None,
         "source_tier": 2, "source": "meta-catalog",
         "suspected": True},
    ]
    xm5["identified_source_file"] = "eval_snapshots_identified_2026-11-07.json"
    xm5["identified_collected_at"] = "2026-11-07T10:00:00Z"
    ds = by_key["sony-dualsense-white"]
    ds["offers"] = [
        {"merchant": "Sony", "price": 69.99,
         "title": "DualSense Wireless Controller - White",
         "url": "https://www.playstation.com/en-us/ps5/accessories/dualsense/",
         "collected_at": "2026-11-07T10:00:00Z",
         "identifier": "711719541080", "identifier_kind": "UPC",
         "source_tier": 1, "source": "shopify:test-store",
         "suspected": True},
    ]
    ds["identified_source_file"] = "eval_snapshots_identified_2026-11-07.json"
    ds["identified_collected_at"] = "2026-11-07T10:00:00Z"
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(data, handle)
    return path


def test_product_page_renders_verified_ranking_when_matched(tmp_path):
    data = _snapshot_matched(tmp_path)
    build_site(data, tmp_path / "site")
    page = ((tmp_path / "site") / "products" / "sony-wh1000xm5-black.html").read_text()
    assert "Verified ranking (identifier-matched)" in page
    assert "UPC 027242923232" in page
    assert "Verified ranking: empty" not in page
    assert "<td>1</td>" in page  # rank column
    assert "shopify:test-store" in page


def test_product_page_pending_model_shows_empty_warning(tmp_path):
    data = _snapshot_matched(tmp_path)
    build_site(data, tmp_path / "site")
    page = ((tmp_path / "site") / "products" / "sony-dualsense-white.html").read_text()
    assert "Verified ranking: empty" in page
    assert "Verified ranking (identifier-matched)" not in page
    assert "Identifier pending" in page


def test_suspected_table_still_present_when_matched(tmp_path):
    data = _snapshot_matched(tmp_path)
    build_site(data, tmp_path / "site")
    page = ((tmp_path / "site") / "products" / "sony-wh1000xm5-black.html").read_text()
    assert "Title-matched offers (suspected same product)" in page
    assert "Adorama" in page  # mismatched identified row stays
    assert "Best Buy" in page  # Meta suspected row stays
    assert "not in the verified ranking above" in page


def test_home_shows_verified_counts(tmp_path):
    data = _snapshot_matched(tmp_path)
    build_site(data, tmp_path / "site")
    home = ((tmp_path / "site") / "index.html").read_text()
    assert "models with a verified ranking" in home
    assert "now have a verified ranking" in home
    assert "no offer on this site is in the verified ranking yet" not in home


def test_coverage_shows_verified_counts(tmp_path):
    data = _snapshot_matched(tmp_path)
    build_site(data, tmp_path / "site")
    coverage = ((tmp_path / "site") / "coverage.html").read_text()
    assert "<th>Matched</th>" in coverage
    assert "<th>With verified ranking</th>" in coverage
    assert "Verified ranking populated for 1 of 200 models" in coverage
    assert "The verified ranking is empty everywhere" not in coverage


def test_method_page_mentions_identified_sources(tmp_path):
    data = _snapshot_matched(tmp_path)
    build_site(data, tmp_path / "site")
    method = ((tmp_path / "site") / "method.html").read_text()
    assert "identifier-matched and appear in verified rankings" in method
    assert "Shopify public product JSON (tier 1)" in method
