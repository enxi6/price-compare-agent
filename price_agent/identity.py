"""Same-product matching on identifiers only (DECISIONS 002).

A merchant offer counts as the same product only when its identifier
matches one of the eval product's verified identifiers. Title similarity
is evidence for the "suspected" table, never for the main ranking.

Identifier normalization: strip punctuation/spaces, uppercase, and for
pure-digit codes strip leading zeros, so a GTIN-14 (``00`` + UPC-12)
matches its UPC-12 form. MPNs/SKUs keep their characters (uppercased).
"""

from __future__ import annotations

import re

from .catalog import EvalProduct
from .models import Offer


def normalize_identifier(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9]", "", value).upper()
    if cleaned.isdigit():
        cleaned = cleaned.lstrip("0") or "0"
    return cleaned


def match_offers(
    offers: list[Offer], product: EvalProduct
) -> tuple[list[Offer], list[Offer]]:
    """Return (matched, suspected) offers for one eval product."""
    references = {normalize_identifier(v) for v in product.identifiers.values()}
    if not references:
        return [], list(offers)
    matched: list[Offer] = []
    suspected: list[Offer] = []
    for offer in offers:
        if offer.identifier and normalize_identifier(offer.identifier) in references:
            matched.append(offer)
        else:
            suspected.append(offer)
    return matched, suspected
