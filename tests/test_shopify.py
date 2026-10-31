"""Tests for the Shopify adapter, using a stubbed HTTP response.

No test hits the network: urlopen is monkeypatched with a fixture
Shopify product JSON payload.
"""

import io
import json

import pytest

import price_agent.adapters_shopify as shopify_module
from price_agent.adapters_shopify import AdapterError, ShopifyAdapter

FIXTURE = {
    "product": {
        "title": "Test Headphones",
        "variants": [
            {"price": "99.99", "compare_at_price": "129.99",
             "sku": "TEST-001", "barcode": "012345678905", "available": True},
            {"price": "89.99", "compare_at_price": None,
             "sku": "TEST-002", "barcode": "", "available": False},
        ],
    }
}


class _Response(io.StringIO):
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def _stub_urlopen(request, timeout=15):
    assert request.full_url.endswith(".json")
    assert "price-compare-agent" in request.headers["User-agent"]
    return _Response(json.dumps(FIXTURE))


def test_shopify_parses_variants_and_coupon(monkeypatch):
    monkeypatch.setattr(shopify_module, "urlopen", _stub_urlopen)
    offers = ShopifyAdapter("example.myshopify.com", "test-headphones",
                            "Example Store").search("")
    assert len(offers) == 2
    first, second = offers
    assert first.identifier == "012345678905"  # barcode wins over sku
    assert first.price == 99.99 and first.coupon == pytest.approx(30.0)
    assert first.shipping is None  # never invented from product JSON
    assert first.in_stock is True
    assert second.identifier == "TEST-002"  # empty barcode falls back to sku
    assert second.in_stock is False


def test_shopify_http_error_becomes_adapter_error(monkeypatch):
    import urllib.error

    def _failing(request, timeout=15):
        raise urllib.error.HTTPError(request.full_url, 404, "Not Found",
                                     None, None)

    monkeypatch.setattr(shopify_module, "urlopen", _failing)
    with pytest.raises(AdapterError):
        ShopifyAdapter("example.myshopify.com", "missing",
                       "Example Store").search("")
