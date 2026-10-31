"""Merchant adapters.

Real adapters (Phase 1) must implement ``MerchantAdapter.search(query)``
against a lawful source (official API / feed / catalog) and return Offers
with identifier, price breakdown, source URL and fetch time.

This module ships only mock adapters so the ranking core can be exercised
without any merchant integration. Mock data is clearly labelled and must
never be presented as real prices.
"""

from __future__ import annotations

from .models import Offer


class MerchantAdapter:
    name = "base"

    def search(self, query: str) -> list[Offer]:
        raise NotImplementedError


# Demo identifier shared by all mock offers for the same query, so the
# demo exercises the matched (same-product) path.
MOCK_IDENTIFIER = "DEMO-UPC-0001"


class MockMerchantA(MerchantAdapter):
    name = "Mock 商家 A"

    def search(self, query: str) -> list[Offer]:
        return [
            Offer(
                merchant=self.name,
                title=query,
                identifier=MOCK_IDENTIFIER,
                price=349.00,
                shipping=0.0,
                tax_estimate=27.92,
                coupon=20.00,
                delivery_days=3,
                seller_rating=4.8,
                url="https://example.com/mock-a",
            )
        ]


class MockMerchantB(MerchantAdapter):
    name = "Mock 商家 B"

    def search(self, query: str) -> list[Offer]:
        return [
            Offer(
                merchant=self.name,
                title=query,
                identifier=MOCK_IDENTIFIER,
                price=329.99,
                shipping=12.99,
                tax_estimate=26.40,
                coupon=0.0,
                delivery_days=5,
                seller_rating=4.6,
                url="https://example.com/mock-b",
            )
        ]


class MockMerchantC(MerchantAdapter):
    name = "Mock 商家 C"

    def search(self, query: str) -> list[Offer]:
        # Lowest sticker price, but shipping unknown: must NOT win silently.
        return [
            Offer(
                merchant=self.name,
                title=query,
                identifier=MOCK_IDENTIFIER,
                price=319.00,
                shipping=None,
                tax_estimate=25.52,
                coupon=0.0,
                delivery_days=7,
                seller_rating=4.2,
                url="https://example.com/mock-c",
            )
        ]


ALL_MOCK_ADAPTERS: list[MerchantAdapter] = [
    MockMerchantA(),
    MockMerchantB(),
    MockMerchantC(),
]
