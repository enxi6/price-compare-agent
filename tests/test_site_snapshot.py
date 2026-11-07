"""Tests for the site-snapshot merge (offline fixtures only)."""

import json

from price_agent.build_site_snapshot import build_site_snapshot
from price_agent.catalog import EVAL_SET


def _files(tmp_path):
    """Two snapshot files: an older one and a newer one sharing a model."""
    older = {
        "meta": {"collected_at": "2026-11-05T10:00:00Z", "source": "test"},
        "models": {
            "sony-wh1000xm5-black": {
                "offers": [
                    {"merchant": "Dell", "title": "Sony WH-1000XM5 Black",
                     "price": 399.99, "url": "https://example.com/dell"},
                    {"merchant": "Dell", "title": "Sony WH-1000XM5 Black",
                     "price": 399.99, "url": "https://example.com/dell"},
                ]
            },
            "keychron-k8-pro": {  # retired key: must not appear in output
                "offers": [
                    {"merchant": "Keychron", "title": "K8 Pro",
                     "price": 49.99, "url": "https://example.com/k8"},
                ]
            },
        },
    }
    newer = {
        "meta": {"collected_at": "2026-11-06T10:00:00Z", "source": "test"},
        "models": {
            "sony-wh1000xm5-black": {
                "offers": [
                    {"merchant": "Dell", "title": "Sony WH-1000XM5 Black",
                     "price": 379.99, "url": "https://example.com/dell"},
                    {"merchant": "Best Buy",
                     "title": "Sony WH-1000XM5 Black",
                     "price": 399.99, "url": "https://example.com/bb"},
                ]
            },
        },
    }
    paths = []
    for name, data in (("old.json", older), ("new.json", newer)):
        path = tmp_path / name
        path.write_text(json.dumps(data), encoding="utf-8")
        paths.append({"path": str(path), "data": data})
    return paths


def test_merge_takes_latest_per_model(tmp_path):
    result = build_site_snapshot(_files(tmp_path))
    by_key = {m["key"]: m for m in result["models"]}
    xm5 = by_key["sony-wh1000xm5-black"]
    # Latest file wins: Dell $379.99, not the older $399.99 row.
    assert [o["price"] for o in xm5["offers"]] == [379.99, 399.99]
    assert xm5["source_collected_at"].startswith("2026-11-06")
    assert xm5["source_file"] == "new.json"


def test_merge_output_is_exactly_the_catalog(tmp_path):
    result = build_site_snapshot(_files(tmp_path))
    assert len(result["models"]) == 200
    assert {m["key"] for m in result["models"]} == {
        p.key for p in EVAL_SET
    }
    # Retired snapshot keys never enter the output.
    assert "keychron-k8-pro" not in {m["key"] for m in result["models"]}
    assert result["meta"]["verified_identifiers"] == 98
    assert result["meta"]["pending_identifiers"] == 102


def test_merge_invents_nothing(tmp_path):
    result = build_site_snapshot(_files(tmp_path))
    catalog = {p.key: p for p in EVAL_SET}
    for model in result["models"]:
        product = catalog[model["key"]]
        # Identifiers are copied from the catalog, never invented.
        assert model["identifiers"] == dict(product.identifiers)
        assert model["status"] == product.status
        for offer in model["offers"]:
            assert offer["identifier"] is None
            assert offer["suspected"] is True


def test_merge_dedupes_exact_duplicate_rows(tmp_path):
    result = build_site_snapshot(_files(tmp_path))
    # The older file's duplicated Dell row is gone (latest wins), and
    # no model carries two identical merchant/price/url rows.
    for model in result["models"]:
        rows = [
            (o["merchant"], o["price"], o["url"]) for o in model["offers"]
        ]
        assert len(rows) == len(set(rows))
