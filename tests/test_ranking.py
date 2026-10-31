"""Tests for the comparison core: totals, ranking, identifier split."""

import unittest

from price_agent.adapters import ALL_MOCK_ADAPTERS, MOCK_IDENTIFIER
from price_agent.models import Offer
from price_agent.ranking import rank_offers, split_by_identifier


class TestTotal(unittest.TestCase):
    def test_total_arithmetic(self):
        offer = Offer(
            merchant="T",
            title="T",
            identifier="X",
            price=100.0,
            shipping=10.0,
            tax_estimate=8.0,
            coupon=5.0,
        )
        self.assertAlmostEqual(offer.total, 113.0)

    def test_unknown_shipping_is_not_zero(self):
        offer = Offer(
            merchant="T", title="T", identifier="X", price=100.0, shipping=None
        )
        self.assertFalse(offer.shipping_known)
        self.assertIn("运费未知", offer.breakdown())


class TestRanking(unittest.TestCase):
    def test_cheapest_total_wins(self):
        cheap = Offer(
            merchant="Cheap", title="T", identifier="X", price=90.0, shipping=0.0
        )
        dear = Offer(
            merchant="Dear", title="T", identifier="X", price=100.0, shipping=0.0
        )
        self.assertEqual(rank_offers([dear, cheap])[0].merchant, "Cheap")

    def test_unknown_shipping_ranks_behind_at_same_total(self):
        known = Offer(
            merchant="Known",
            title="T",
            identifier="X",
            price=100.0,
            shipping=0.0,
        )
        unknown = Offer(
            merchant="Unknown",
            title="T",
            identifier="X",
            price=100.0,
            shipping=None,
        )
        self.assertEqual(rank_offers([unknown, known])[0].merchant, "Known")

    def test_unknown_shipping_ranks_behind_even_when_partial_total_lower(self):
        # The unknown-shipping total is a lower bound, not a delivered
        # price, so it must not win just because its partial sum is lower.
        known = Offer(
            merchant="Known",
            title="T",
            identifier="X",
            price=110.0,
            shipping=0.0,
        )
        unknown = Offer(
            merchant="Unknown",
            title="T",
            identifier="X",
            price=90.0,
            shipping=None,
        )
        self.assertEqual(rank_offers([unknown, known])[0].merchant, "Known")

    def test_out_of_stock_last(self):
        available = Offer(
            merchant="A", title="T", identifier="X", price=100.0, shipping=0.0
        )
        oos = Offer(
            merchant="B",
            title="T",
            identifier="X",
            price=50.0,
            shipping=0.0,
            in_stock=False,
        )
        self.assertEqual(rank_offers([oos, available])[0].merchant, "A")


class TestIdentifierSplit(unittest.TestCase):
    def test_mismatched_identifier_goes_to_suspected(self):
        offers = [
            Offer(merchant="A", title="T", identifier="X", price=10.0),
            Offer(merchant="B", title="T", identifier="Y", price=9.0),
        ]
        matched, suspected = split_by_identifier(offers, "X")
        self.assertEqual([o.merchant for o in matched], ["A"])
        self.assertEqual([o.merchant for o in suspected], ["B"])

    def test_mock_adapters_all_match_demo_identifier(self):
        offers = []
        for adapter in ALL_MOCK_ADAPTERS:
            offers.extend(adapter.search("Sony WH-1000XM5"))
        matched, suspected = split_by_identifier(offers, MOCK_IDENTIFIER)
        self.assertEqual(len(matched), 3)
        self.assertEqual(len(suspected), 0)


if __name__ == "__main__":
    unittest.main()
