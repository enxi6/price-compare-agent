"""CLI entry point.

Usage:
    python3 -m price_agent.cli compare "Sony WH-1000XM5"

Current version uses mock adapters (see adapters.py) to demonstrate the
comparison core. Real merchant adapters land in Phase 1 (see PLAN.md).
"""

from __future__ import annotations

import argparse
import sys

from .adapters import ALL_MOCK_ADAPTERS, MOCK_IDENTIFIER
from .models import Offer
from .ranking import rank_offers, split_by_identifier


def compare(query: str, adapters=ALL_MOCK_ADAPTERS) -> None:
    offers: list[Offer] = []
    for adapter in adapters:
        offers.extend(adapter.search(query))
    matched, suspected = split_by_identifier(offers, MOCK_IDENTIFIER)
    ranked = rank_offers(matched)

    print(f"商品：{query}（模拟商家数据，非真实价格）")
    print(f"同款标识：{MOCK_IDENTIFIER}，命中 {len(ranked)} 家\n")
    print("到手总价排名：")
    for i, offer in enumerate(ranked, 1):
        stock = "有货" if offer.in_stock else "缺货"
        delivery = f"{offer.delivery_days} 天" if offer.delivery_days else "未知"
        rating = f"{offer.seller_rating:.1f}" if offer.seller_rating else "未知"
        print(f"{i}. {offer.merchant}｜{stock}｜到货约 {delivery}｜商家评分 {rating}")
        print(f"   {offer.breakdown()}")
        print(f"   来源：{offer.url}｜抓取于 {offer.fetched_at}")
    if suspected:
        print(f"\n疑似同款（标识对不上，未进排名）：{len(suspected)} 家")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="price_agent")
    sub = parser.add_subparsers(dest="command", required=True)
    cmp_parser = sub.add_parser("compare", help="比较一款商品的到手总价")
    cmp_parser.add_argument("query", help="商品名或型号，例如 Sony WH-1000XM5")
    args = parser.parse_args(argv)
    if args.command == "compare":
        compare(args.query)
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
