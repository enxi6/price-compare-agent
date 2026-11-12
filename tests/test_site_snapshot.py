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
    assert len(result["models"]) == 250
    assert {m["key"] for m in result["models"]} == {
        p.key for p in EVAL_SET
    }
    # Retired snapshot keys never enter the output.
    assert "keychron-k8-pro" not in {m["key"] for m in result["models"]}
    assert result["meta"]["verified_identifiers"] == 124
    assert result["meta"]["pending_identifiers"] == 126


def test_merge_invents_nothing_meta_only(tmp_path):
    """Meta stream only: identifiers are copied from the catalog, never
    invented. (Identified-stream assertions live in the identified
    tests below; this test is scoped to the Meta stream, not loosened.)
    """
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


def _id_offer(merchant, price, identifier, kind="UPC",
              url="https://example.com/id",
              collected_at="2026-11-07T10:00:00Z"):
    return {
        "merchant": merchant, "price": price,
        "title": "Sony WH-1000XM5 Black", "url": url,
        "collected_at": collected_at, "identifier": identifier,
        "identifier_kind": kind, "source_tier": 1,
        "source": "shopify:test-store",
    }


def _identified(tmp_path, models, name="identified.json",
                collected_at="2026-11-07T10:00:00Z"):
    data = {
        "meta": {"collected_at": collected_at, "source": "test",
                 "source_tier": 1, "identified": True,
                 "generated_by": "test"},
        "models": models,
    }
    path = tmp_path / name
    path.write_text(json.dumps(data), encoding="utf-8")
    return [{"path": str(path), "data": data}]


def _xm5(result):
    return {m["key"]: m for m in result["models"]}["sony-wh1000xm5-black"]


def test_identified_offer_matching(tmp_path):
    identified = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Best Buy", 389.99, "027242923232",
                      url="https://example.com/bb-id"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    xm5 = _xm5(result)
    matched = [o for o in xm5["offers"] if not o["suspected"]]
    assert len(matched) == 1
    assert matched[0]["merchant"] == "Best Buy"
    assert matched[0]["identifier"] == "027242923232"
    assert matched[0]["identifier_kind"] == "UPC"
    assert matched[0]["source"] == "shopify:test-store"
    assert result["meta"]["matched_offers"] == 1
    assert result["meta"]["verified_ranking_models"] == 1
    assert result["meta"]["identified_source_files"] == 1


def test_identified_offer_mismatch_stays_suspected(tmp_path):
    # 027242923249 is the Silver variant's UPC (catalog.py): a real
    # wrong-variant trap — it must never enter the Black ranking.
    identified = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 379.99, "027242923249",
                      url="https://example.com/dell-id"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    xm5 = _xm5(result)
    assert all(o["suspected"] is True for o in xm5["offers"])
    assert result["meta"]["matched_offers"] == 0
    assert result["meta"]["verified_ranking_models"] == 0
    # The mismatched row is preserved with its identifier (it may
    # match later if the catalog ever gains that variant), and the
    # Meta Dell row survives: matched-only supersede (§2.2).
    dell_rows = [o for o in xm5["offers"] if o["merchant"] == "Dell"]
    assert len(dell_rows) == 2
    assert {o["identifier"] for o in dell_rows} == {
        None, "027242923249"}


def test_identified_supersedes_meta_same_merchant_price(tmp_path):
    identified = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 379.99, "027242923232",
                      url="https://example.com/dell-id"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    xm5 = _xm5(result)
    dell_rows = [o for o in xm5["offers"] if o["merchant"] == "Dell"]
    assert len(dell_rows) == 1  # Meta row replaced, not duplicated
    assert dell_rows[0]["identifier"] == "027242923232"
    assert dell_rows[0]["source"] == "shopify:test-store"
    assert dell_rows[0]["suspected"] is False
    assert len(xm5["offers"]) == 2  # Dell matched + Best Buy suspected


def test_identified_does_not_replace_meta_for_other_merchants(tmp_path):
    identified = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 379.99, "027242923232",
                      url="https://example.com/dell-id"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    xm5 = _xm5(result)
    bb_rows = [o for o in xm5["offers"] if o["merchant"] == "Best Buy"]
    assert len(bb_rows) == 1
    assert bb_rows[0]["identifier"] is None
    assert bb_rows[0]["suspected"] is True


def test_identified_dedupe_same_merchant_identifier_price(tmp_path):
    # Same merchant + identifier + price twice in one file, once as
    # GTIN-14 and once as UPC-12, different titles/URLs: one row.
    identified = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 379.99, "00027242923232",
                      url="https://example.com/dell-a"),
            dict(_id_offer("Dell", 379.99, "027242923232",
                           url="https://example.com/dell-b"),
                 title="Sony WH-1000XM5 Black (other listing)"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    xm5 = _xm5(result)
    dell_rows = [o for o in xm5["offers"] if o["merchant"] == "Dell"]
    assert len(dell_rows) == 1
    assert result["meta"]["matched_offers"] == 1


def test_identified_price_change_supersedes_stale_row(tmp_path):
    # Regression: the same merchant + identifier at a new price in a
    # newer file must supersede the stale price, not list both as
    # matched offers (Beach Camera QC Ultra 2 $399 -> $449,
    # 2026-11-10 — the ranking showed a price that no longer exists).
    older = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 379.99, "027242923232",
                      url="https://example.com/dell-id",
                      collected_at="2026-11-07T10:00:00Z"),
        ]},
    }, name="identified-older.json",
        collected_at="2026-11-07T10:00:00Z")
    newer = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 399.99, "027242923232",
                      url="https://example.com/dell-id",
                      collected_at="2026-11-08T10:00:00Z"),
        ]},
    }, name="identified-newer.json",
        collected_at="2026-11-08T10:00:00Z")
    result = build_site_snapshot(_files(tmp_path), older + newer)
    xm5 = _xm5(result)
    dell_rows = [o for o in xm5["offers"] if o["merchant"] == "Dell"]
    # The stale identified $379.99 row is gone. The Meta $379.99 row
    # survives as suspected: supersede only replaces a Meta row at
    # the SAME price as the matched row, and the matched row is now
    # $399.99.
    assert len(dell_rows) == 2
    identified_dell = [o for o in dell_rows
                       if o["source"] != "meta-catalog"]
    assert len(identified_dell) == 1
    assert identified_dell[0]["price"] == 399.99
    assert identified_dell[0]["suspected"] is False
    assert result["meta"]["matched_offers"] == 1


def test_identified_price_reverts_to_earlier_value(tmp_path):
    # QuadCast 2 S pattern: $149.99 (old) -> $159.99 (mid) -> $149.99
    # (new). The newest read wins even though its price equals the
    # oldest read's: the duplicate $149.99 rows must keep the newest
    # collected_at, or the stale $159.99 row wins the dedupe.
    old = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 149.99, "027242923232",
                      url="https://example.com/dell-id",
                      collected_at="2026-11-07T10:00:00Z"),
        ]},
    }, name="identified-old.json",
        collected_at="2026-11-07T10:00:00Z")
    mid = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 159.99, "027242923232",
                      url="https://example.com/dell-id",
                      collected_at="2026-11-08T10:00:00Z"),
        ]},
    }, name="identified-mid.json",
        collected_at="2026-11-08T10:00:00Z")
    new = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 149.99, "027242923232",
                      url="https://example.com/dell-id",
                      collected_at="2026-11-09T10:00:00Z"),
        ]},
    }, name="identified-new.json",
        collected_at="2026-11-09T10:00:00Z")
    result = build_site_snapshot(_files(tmp_path), old + mid + new)
    xm5 = _xm5(result)
    identified_dell = [o for o in xm5["offers"]
                       if o["merchant"] == "Dell"
                       and o["source"] != "meta-catalog"]
    assert len(identified_dell) == 1
    assert identified_dell[0]["price"] == 149.99
    assert identified_dell[0]["suspected"] is False
    assert result["meta"]["matched_offers"] == 1


def test_identified_union_across_files_same_model(tmp_path):
    # Regression test for DECISIONS 066: identified files union per
    # model. A matched hand row in the OLDER file and a mismatched
    # collector row in the NEWER file must BOTH survive — latest-
    # per-model on this stream silently dropped the hand row (it
    # dropped the Switch 2 Micro Center row in favour of a
    # BrandsMart row).
    older = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Dell", 379.99, "027242923232",
                      url="https://example.com/dell-id"),
        ]},
    }, name="identified-hand.json",
        collected_at="2026-11-07T10:00:00Z")
    newer = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("BrandsMart", 379.99, "027242923249",
                      url="https://example.com/bm-id"),
        ]},
    }, name="identified-retry.json",
        collected_at="2026-11-07T12:00:00Z")
    result = build_site_snapshot(_files(tmp_path), older + newer)
    xm5 = _xm5(result)
    matched = [o for o in xm5["offers"] if not o["suspected"]]
    assert len(matched) == 1
    assert matched[0]["merchant"] == "Dell"
    assert matched[0]["identifier"] == "027242923232"
    # The mismatched newer row survives as suspected and supersedes
    # nothing (no Meta BrandsMart row exists in the fixture).
    bm_rows = [o for o in xm5["offers"]
               if o["merchant"] == "BrandsMart"]
    assert len(bm_rows) == 1
    assert bm_rows[0]["suspected"] is True
    assert bm_rows[0]["identifier"] == "027242923249"
    assert len(xm5["offers"]) == 3  # Dell matched + Best Buy + BrandsMart
    assert result["meta"]["matched_offers"] == 1
    assert result["meta"]["verified_ranking_models"] == 1
    assert result["meta"]["identified_source_files"] == 2
    assert xm5["identified_source_file"] == "identified-retry.json"
    assert xm5["identified_collected_at"] == "2026-11-07T12:00:00+00:00"


def test_pending_model_never_has_verified_ranking(tmp_path):
    identified = _identified(tmp_path, {
        "sony-dualsense-white": {"offers": [
            _id_offer("Sony", 69.99, "711719541080",
                      url="https://example.com/ds"),
        ]},
        "sony-dualsense-edge-black-white": {"offers": [
            _id_offer("Sony", 69.99, "711719999999",
                      url="https://example.com/dse"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    by_key = {m["key"]: m for m in result["models"]}
    for key in ("sony-dualsense-white", "sony-dualsense-edge-black-white"):
        assert all(
            o["suspected"] is True for o in by_key[key]["offers"]
        )
    assert result["meta"]["matched_offers"] == 0
    assert result["meta"]["verified_ranking_models"] == 0


def test_meta_counts_include_verified_ranking(tmp_path):
    identified = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Best Buy", 389.99, "027242923232",
                      url="https://example.com/bb-id"),
        ]},
        "sony-dualsense-white": {"offers": [
            _id_offer("Sony", 69.99, "711719541080",
                      url="https://example.com/ds"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    meta = result["meta"]
    assert meta["verified_ranking_models"] == 1
    assert meta["matched_offers"] == 1
    assert meta["suspected_offers"] == meta["total_offers"] - 1
    assert meta["identified_source_files"] == 1


def test_identified_unknown_key_ignored(tmp_path):
    identified = _identified(tmp_path, {
        "keychron-k8-pro": {"offers": [  # retired key
            _id_offer("Keychron", 49.99, "4895248870609",
                      url="https://example.com/k8"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    assert len(result["models"]) == 250
    assert "keychron-k8-pro" not in {m["key"] for m in result["models"]}


def test_identifier_normalization_gtin14_matches_upc12(tmp_path):
    identified = _identified(tmp_path, {
        "sony-wh1000xm5-black": {"offers": [
            _id_offer("Best Buy", 389.99, "00027242923232",
                      url="https://example.com/bb-id"),
        ]},
    })
    result = build_site_snapshot(_files(tmp_path), identified)
    xm5 = _xm5(result)
    matched = [o for o in xm5["offers"] if not o["suspected"]]
    assert len(matched) == 1
    assert matched[0]["identifier"] == "00027242923232"


def test_merge_dedupes_exact_duplicate_rows(tmp_path):
    result = build_site_snapshot(_files(tmp_path))
    # The older file's duplicated Dell row is gone (latest wins), and
    # no model carries two identical merchant/price/url rows.
    for model in result["models"]:
        rows = [
            (o["merchant"], o["price"], o["url"]) for o in model["offers"]
        ]
        assert len(rows) == len(set(rows))
