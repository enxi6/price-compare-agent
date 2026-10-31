"""Tests for identifier matching (DECISIONS 002)."""

from price_agent.catalog import EvalProduct
from price_agent.identity import match_offers, normalize_identifier
from price_agent.models import Offer


def _offer(identifier):
    return Offer(merchant="M", title="T", identifier=identifier, price=10.0)


def _product(identifiers):
    return EvalProduct(key="k", brand="B", model="M", variant="V",
                       category="c", identifiers=identifiers, status="verified")


def test_gtin14_matches_upc12():
    matched, suspected = match_offers(
        [_offer("00045496883386")], _product({"UPC": "045496883386"}))
    assert len(matched) == 1 and not suspected


def test_different_variant_upc_is_suspected():
    # Silver XM5 UPC must not match the Black entry.
    matched, suspected = match_offers(
        [_offer("027242923249")], _product({"UPC": "027242923232"}))
    assert not matched and len(suspected) == 1


def test_no_verified_identifier_means_nothing_matched():
    matched, suspected = match_offers(
        [_offer("027242923232")], _product({}))
    assert not matched and len(suspected) == 1


def test_normalize_strips_punctuation_and_case():
    assert normalize_identifier(" 910-006557 ") == "910006557"
    # Punctuation is stripped on both sides, so MPNs still match each other.
    assert normalize_identifier("mqd83am/a") == "MQD83AMA"
