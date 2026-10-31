"""Data models for the price comparison core."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Offer:
    """One merchant's offer for one product.

    ``shipping=None`` means shipping is unknown -- it must be surfaced as
    unknown, never silently counted as zero.
    """

    merchant: str
    title: str
    identifier: str | None  # UPC / EAN / MPN / official SKU; same-product key
    price: float
    shipping: float | None = None
    tax_estimate: float = 0.0
    coupon: float = 0.0
    delivery_days: int | None = None
    seller_rating: float | None = None  # 0-5
    url: str = ""
    in_stock: bool = True
    fetched_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    @property
    def total(self) -> float:
        """Delivered total, excluding unknown shipping (flagged separately)."""
        return self.price + (self.shipping or 0.0) + self.tax_estimate - self.coupon

    @property
    def shipping_known(self) -> bool:
        return self.shipping is not None

    def breakdown(self) -> str:
        ship = f"${self.shipping:.2f}" if self.shipping_known else "运费未知"
        return (
            f"商品 ${self.price:.2f} + 运费 {ship} "
            f"+ 预估税 ${self.tax_estimate:.2f} - 优惠 ${self.coupon:.2f} "
            f"= 到手 ${self.total:.2f}"
            + ("" if self.shipping_known else "（不含未知运费）")
        )
