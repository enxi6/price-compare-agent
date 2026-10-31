"""Tier-1 adapter: a merchant's public Shopify product JSON endpoint.

Many independent stores publish ``https://<store>/products/<handle>.json``
without login. That is an official public product interface (data tier 1
in PLAN.md), not scraping: one request per configured product, with an
identifying User-Agent, and any block or non-200 response stops the
adapter with AdapterError instead of retrying around it.

Shopify product JSON does not carry shipping or tax, so those stay
unknown/zero and the ranking rules flag them; the adapter never invents
them. A variant's ``barcode`` is the identifier when present, else its
``sku`` (often the MPN), else None (title-only -> suspected table).
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request

from .adapters import MerchantAdapter
from .models import Offer

USER_AGENT = "price-compare-agent/0.1 (open-source buyer-side agent)"


class AdapterError(Exception):
    pass


class ShopifyAdapter(MerchantAdapter):
    """One configured product on one Shopify store."""

    def __init__(self, store: str, handle: str, merchant: str):
        self.store = store
        self.handle = handle
        self.name = merchant
        self.url = f"https://{store}/products/{handle}"

    def search(self, query: str) -> list[Offer]:
        # Product-specific adapter: the configured product is the query.
        # Matching against an eval product happens in identity.py.
        request = urllib.request.Request(
            self.url + ".json", headers={"User-Agent": USER_AGENT}
        )
        try:
            with urlopen(request, timeout=15) as response:
                payload = json.load(response)
        except urllib.error.HTTPError as exc:
            raise AdapterError(f"Shopify store returned HTTP {exc.code}") from exc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            raise AdapterError(f"Shopify fetch failed: {exc}") from exc

        product = payload.get("product") or {}
        title = product.get("title", self.handle)
        offers: list[Offer] = []
        for variant in product.get("variants", []):
            try:
                price = float(variant["price"])
            except (KeyError, TypeError, ValueError):
                continue
            compare_at = variant.get("compare_at_price")
            coupon = 0.0
            if compare_at:
                try:
                    coupon = max(0.0, float(compare_at) - price)
                except (TypeError, ValueError):
                    coupon = 0.0
            variant_title = variant.get("title") or ""
            full_title = title if variant_title in ("", "Default Title") else (
                f"{title} - {variant_title}"
            )
            offers.append(
                Offer(
                    merchant=self.name,
                    title=full_title,
                    identifier=variant.get("barcode") or variant.get("sku") or None,
                    price=price,
                    shipping=None,  # not in product JSON; never invent it
                    tax_estimate=0.0,
                    coupon=coupon,
                    url=self.url,
                    in_stock=bool(variant.get("available")),
                )
            )
        return offers


# Patch point for tests (they stub urlopen, never hit the network).
urlopen = urllib.request.urlopen
