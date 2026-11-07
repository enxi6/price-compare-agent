"""Tests for the Shopify identified-quote collector (offline fixtures)."""

import json
from urllib.error import HTTPError

import pytest

from datetime import datetime, timezone

from price_agent.collect_identified import (
    CollectError,
    collect,
    collect_entry,
)
from price_agent.catalog import EVAL_SET


def _product_json(variants):
    return {"product": {"title": "Test", "handle": "test",
                        "variants": variants}}


def _variant(variant_id, price, barcode=None, sku=None, title="Default Title"):
    return {"id": variant_id, "title": title, "price": price,
            "barcode": barcode, "sku": sku}


class _Response:
    def __init__(self, payload):
        self._payload = json.dumps(payload).encode("utf-8")

    def read(self):
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def _opener(responses):
    """responses: url -> payload dict, or HTTPError to raise."""
    def open_(request, timeout=15):
        url = request.full_url
        value = responses.get(url)
        if isinstance(value, HTTPError):
            raise value
        if value is None:
            raise HTTPError(url, 404, "Not Found", None, None)
        return _Response(value)
    return open_


NOW = datetime(2026, 11, 7, 10, 0, tzinfo=timezone.utc)


def _config(tmp_path, entries):
    path = tmp_path / "handles.json"
    path.write_text(json.dumps({"entries": entries}), encoding="utf-8")
    return str(path)


def _entry(key, store, handle, variant_id=None):
    return {"product_key": key, "merchant": store,
            "store": store, "handle": handle, "variant_id": variant_id}


XM5 = "sony-wh1000xm5-black"
K8U = "keychron-k8-ultra-8k"


def test_collects_pinned_variant_js_cents(tmp_path):
    responses = {
        "https://test-store.com/products/xm5.js": _product_json([
            _variant(111, 37999, barcode="027242923232",
                     sku="WH1000XM5/B", title="Black"),
            _variant(222, 37999, barcode="027242923249",
                     sku="WH1000XM5/S", title="Silver"),
        ]),
    }
    entry = _entry(XM5, "test-store.com", "xm5", variant_id=111)
    result = collect_entry(entry, opener=_opener(responses), now=NOW)
    assert result is not None
    assert result["merchant"] == "test-store.com"
    assert result["price"] == 379.99
    assert result["identifier"] == "027242923232"
    assert result["identifier_kind"] == "UPC"
    assert result["source_tier"] == 1


def test_single_variant_fallback(tmp_path):
    responses = {
        "https://test-store.com/products/k8u.js": _product_json([
            _variant(999, 11999, barcode="4894979057969",
                     sku="K8U-J1"),
        ]),
    }
    entry = _entry(K8U, "test-store.com", "k8u")
    result = collect_entry(entry, opener=_opener(responses), now=NOW)
    assert result is not None
    assert result["price"] == 119.99
    assert result["identifier"] == "4894979057969"
    assert result["identifier_kind"] == "EAN"


def test_multi_variant_without_pin_skipped(tmp_path):
    responses = {
        "https://test-store.com/products/xm5.js": _product_json([
            _variant(111, 37999, barcode="027242923232"),
            _variant(222, 37999, barcode="027242923249"),
        ]),
    }
    entry = _entry(XM5, "test-store.com", "xm5")
    with pytest.raises(CollectError, match="no variant_id pinned"):
        collect_entry(entry, opener=_opener(responses), now=NOW)


def test_bundle_variant_skipped(tmp_path):
    responses = {
        "https://test-store.com/products/xm5.js": _product_json([
            _variant(111, 39999, barcode="196271645177",
                     title="XM5 + Case Bundle"),
        ]),
    }
    entry = _entry(XM5, "test-store.com", "xm5", variant_id=111)
    with pytest.raises(CollectError, match="bundle"):
        collect_entry(entry, opener=_opener(responses), now=NOW)


def test_sku_fallback_when_no_barcode(tmp_path):
    responses = {
        "https://test-store.com/products/xm5.js": _product_json([
            _variant(111, 37999, barcode=None, sku="WH1000XM5/B"),
        ]),
    }
    entry = _entry(XM5, "test-store.com", "xm5", variant_id=111)
    result = collect_entry(entry, opener=_opener(responses), now=NOW)
    assert result is not None
    assert result["identifier"] == "WH1000XM5/B"
    assert result["identifier_kind"] == "SKU"


def test_no_identifier_raises(tmp_path):
    responses = {
        "https://test-store.com/products/xm5.js": _product_json([
            _variant(111, 37999, barcode=None, sku=None),
        ]),
    }
    entry = _entry(XM5, "test-store.com", "xm5", variant_id=111)
    with pytest.raises(CollectError, match="neither barcode nor sku"):
        collect_entry(entry, opener=_opener(responses), now=NOW)


def test_json_endpoint_fallback_when_js_404s(tmp_path):
    responses = {
        "https://test-store.com/products/xm5.js": HTTPError(
            "https://test-store.com/products/xm5.js", 404,
            "Not Found", None, None),
        "https://test-store.com/products/xm5.json": _product_json([
            _variant(111, "379.99", barcode="027242923232"),
        ]),
    }
    entry = _entry(XM5, "test-store.com", "xm5", variant_id=111)
    result = collect_entry(entry, opener=_opener(responses), now=NOW)
    assert result is not None
    assert result["price"] == 379.99
    assert result["identifier"] == "027242923232"


def test_rate_limit_error_skips_entry_but_not_run(tmp_path):
    responses = {
        "https://test-store.com/products/xm5.js": HTTPError(
            "https://test-store.com/products/xm5.js", 429,
            "Too Many Requests", None, None),
        "https://test-store.com/products/k8u.js": _product_json([
            _variant(999, 11999, barcode="4894979057969"),
        ]),
    }
    config = _config(tmp_path, [
        _entry(XM5, "test-store.com", "xm5", variant_id=111),
        _entry(K8U, "test-store.com", "k8u"),
    ])
    data = collect(config, opener=_opener(responses),
                   sleep=lambda s: None, pace_seconds=0, now=NOW)
    assert XM5 not in data["models"]
    assert K8U in data["models"]
    assert data["models"][K8U]["offers"][0]["identifier"] == "4894979057969"
    assert data["meta"]["identified"] is True
    assert data["_counts"]["collected"] == 1
    assert data["_counts"]["skipped"] == 1


def test_unknown_catalog_key_skipped(tmp_path):
    responses = {}
    config = _config(tmp_path, [
        _entry("no-such-key", "test-store.com", "x"),
    ])
    out = tmp_path / "identified.json"
    data = collect(config, opener=_opener(responses),
                   sleep=lambda s: None, pace_seconds=0, now=NOW)
    assert data["models"] == {}
    assert data["_counts"]["collected"] == 0
    assert data["_counts"]["skipped"] == 1


def test_collect_skips_missing_handle(tmp_path):
    config = _config(tmp_path, [
        {"product_key": XM5, "merchant": "test-store.com",
         "store": "test-store.com"},
    ])
    data = collect(config, opener=_opener({}),
                   sleep=lambda s: None, pace_seconds=0, now=NOW)
    assert data["models"] == {}
    assert data["_counts"]["skipped"] == 1
