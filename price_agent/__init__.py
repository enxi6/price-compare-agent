"""Price Compare Agent: buyer-side price comparison core.

Principles (see DECISIONS.md):
- Rank only on buyer interests: delivered total, delivery time, seller reputation.
- Same product = same UPC/EAN/MPN/official SKU. Title look-alikes go to a
  separate "suspected same product" list, never into the main ranking.
- Unknown shipping is never treated as zero.
"""

from .models import Offer
from .ranking import rank_offers

__all__ = ["Offer", "rank_offers"]
