"""CLI entry point.

Usage:
    python3 -m price_agent.cli compare "Sony WH-1000XM5"   # mock demo
    python3 -m price_agent.cli compare --model sony-wh1000xm5-black --snapshot data/eval_snapshots.json
    python3 -m price_agent.cli compare --model keychron-k8-pro --shopify www.keychron.com/keychron-k8-pro-qmk-via-wireless-mechanical-keyboard
    python3 -m price_agent.cli eval --snapshot data/eval_snapshots.json

Mock mode demonstrates the ranking core. Snapshot mode uses checked-in
catalog data: offers there are title-matched only (no UPC from the
source) and stay out of the matched ranking by design.
"""

from __future__ import annotations

import argparse
import os
import sys

from .adapters import ALL_MOCK_ADAPTERS, MOCK_IDENTIFIER
from .adapters_shopify import AdapterError, ShopifyAdapter
from .catalog import get_product
from .evaluate import evaluate
from .identity import match_offers
from .models import Offer
from .ranking import rank_offers, split_by_identifier
from .snapshots import STALE_AFTER_HOURS, SnapshotAdapter, load_snapshot, snapshot_age_hours

DEFAULT_SNAPSHOT = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "data", "eval_snapshots.json")
)


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


def compare_model(model_key: str, snapshot_path: str) -> None:
    product = get_product(model_key)
    snapshot = load_snapshot(snapshot_path)
    age = snapshot_age_hours(snapshot)
    offers = SnapshotAdapter(snapshot_path, model_key).search("")
    matched, suspected = match_offers(offers, product)
    ranked = rank_offers(matched)

    print(f"商品：{product.brand} {product.model}（{product.variant}）")
    print(f"同款标识：{product.identifiers or '未核实（不得凭标题进主排名）'}")
    if age > STALE_AFTER_HOURS:
        print(f"注意：快照已 {age:.0f} 小时，超过 {STALE_AFTER_HOURS:.0f} 小时，价格需复核，不当现价用。")
    print(f"快照来源：{snapshot['meta']['source']}，采集于 {snapshot['meta']['collected_at']}")
    print(f"\n主排名（标识匹配）：{len(ranked)} 家")
    for i, offer in enumerate(ranked, 1):
        print(f"{i}. {offer.merchant}｜{offer.breakdown()}")
        print(f"   来源：{offer.url}")
    print(f"\n疑似同款价格一览（标题匹配、未验证标识，不进主排名，仅作线索）：{len(suspected)} 家")
    for offer in sorted(suspected, key=lambda o: o.price):
        print(f"- {offer.merchant}｜商品 ${offer.price:.2f}（运费未知、税费未计）｜{offer.url}")
    if suspected:
        print("下单前须在商家页核实型号、颜色、库存与结算总价。")


def compare_shopify(model_key: str, spec: str) -> None:
    """Compare one eval model against one live Shopify store product.

    spec format: ``store/handle`` (e.g. www.keychron.com/keychron-k8-pro-...).
    The store's public product JSON is the source; a block or error stops
    the adapter with a plain message, never a workaround.
    """
    product = get_product(model_key)
    try:
        store, handle = spec.split("/", 1)
    except ValueError:
        print("请用 store/handle 格式，例如 www.keychron.com/keychron-k8-pro-...")
        return
    adapter = ShopifyAdapter(store, handle, merchant=store)
    try:
        offers = adapter.search("")
    except AdapterError as exc:
        print(f"店铺接口未返回可用数据，已停住：{exc}")
        return
    matched, suspected = match_offers(offers, product)
    ranked = rank_offers(matched)
    print(f"商品：{product.brand} {product.model}（{product.variant}）")
    print(f"店铺：{adapter.url}（公开商品 JSON，只读）")
    print(f"同款标识：{product.identifiers or '未核实（不得凭标题进主排名）'}")
    print(f"\n主排名（标识匹配）：{len(ranked)} 家")
    for i, offer in enumerate(ranked, 1):
        stock = "有货" if offer.in_stock else "缺货"
        print(f"{i}. {offer.merchant}｜{stock}｜{offer.title}")
        print(f"   {offer.breakdown()}")
        print(f"   来源：{offer.url}｜抓取于 {offer.fetched_at}")
    print(f"\n疑似（标识对不上，未进排名）：{len(suspected)} 个变体")
    for offer in suspected:
        print(f"- {offer.title}｜商品 ${offer.price:.2f}｜标识 {offer.identifier}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="price_agent")
    sub = parser.add_subparsers(dest="command", required=True)
    cmp_parser = sub.add_parser("compare", help="比较一款商品的到手总价")
    cmp_parser.add_argument("query", nargs="?", help="商品名或型号，例如 Sony WH-1000XM5")
    cmp_parser.add_argument("--model", help="评测集型号 key，例如 sony-wh1000xm5-black")
    cmp_parser.add_argument("--snapshot", default=DEFAULT_SNAPSHOT,
                            help="快照文件路径（默认 data/eval_snapshots.json）")
    cmp_parser.add_argument("--shopify", help="实店：store/handle，例如 www.keychron.com/keychron-k8-pro-...")
    eval_parser = sub.add_parser("eval", help="跑一遍 20 型号评测集并汇总覆盖率")
    eval_parser.add_argument("--snapshot", default=DEFAULT_SNAPSHOT)
    args = parser.parse_args(argv)
    if args.command == "compare":
        if args.model and args.shopify:
            compare_shopify(args.model, args.shopify)
            return 0
        if args.model:
            compare_model(args.model, args.snapshot)
            return 0
        if not args.query:
            cmp_parser.error("compare 需要 query，或用 --model 指定评测集型号")
        compare(args.query)
        return 0
    if args.command == "eval":
        result = evaluate(args.snapshot)
        print(f"评测集：{result['models']} 个型号，已核实标识 {result['verified_identifiers']} 个，"
              f"有快照报价 {result['with_snapshot_offers']} 个")
        print(f"报价总数 {result['total_offers']}，标识匹配 {result['matched']}，"
              f"标题匹配（疑似）{result['suspected']}")
        for row in result["rows"]:
            print(f"- {row['key']}：标识 {row['identifier_status']}，报价 {row['offers']}，"
                  f"匹配 {row['matched']}，疑似 {row['suspected']}")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
