"""Ranking: transparent, buyer-side, no black-box score.

Order: delivered total ascending; unknown-shipping offers rank behind
known-shipping offers at (nearly) the same total; ties broken by delivery
days, then seller rating. Offers whose identifier does not match the
reference product never enter the main ranking.
"""

from __future__ import annotations

from .models import Offer


def split_by_identifier(
    offers: list[Offer], reference_identifier: str | None
) -> tuple[list[Offer], list[Offer]]:
    """Return (matched, suspected) offers.

    When no reference identifier is known, everything is 'suspected' --
    the caller must not present it as verified same-product ranking.
    """
    if reference_identifier is None:
        return [], list(offers)
    matched = [o for o in offers if o.identifier == reference_identifier]
    suspected = [o for o in offers if o.identifier != reference_identifier]
    return matched, suspected


def rank_offers(offers: list[Offer]) -> list[Offer]:
    """Rank matched offers.

    Unknown shipping makes a total incomparable (it is a lower bound, not
    a delivered price), so unknown-shipping offers always rank behind
    known-shipping ones, regardless of their partial total. Out-of-stock
    offers rank last within each group.
    """
    known = [o for o in offers if o.in_stock and o.shipping_known]
    unknown = [o for o in offers if o.in_stock and not o.shipping_known]
    out_of_stock = [o for o in offers if not o.in_stock]
    key = lambda o: (
        round(o.total, 2),
        o.delivery_days if o.delivery_days is not None else 999,
        -(o.seller_rating or 0.0),
    )
    return (
        sorted(known, key=key)
        + sorted(unknown, key=key)
        + sorted(out_of_stock, key=key)
    )
