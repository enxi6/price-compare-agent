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

    print(f"Product: {query} (mock merchant data, not real prices)")
    print(f"Same-product identifier: {MOCK_IDENTIFIER}, {len(ranked)} matched\n")
    print("Landed total price ranking:")
    for i, offer in enumerate(ranked, 1):
        stock = "In stock" if offer.in_stock else "Out of stock"
        delivery = f"{offer.delivery_days} days" if offer.delivery_days else "Unknown"
        rating = f"{offer.seller_rating:.1f}" if offer.seller_rating else "Unknown"
        print(f"{i}. {offer.merchant} | {stock} | Delivery ~{delivery} | Merchant rating {rating}")
        print(f"   {offer.breakdown()}")
        print(f"   Source: {offer.url} | Fetched at {offer.fetched_at}")
    if suspected:
        print(f"\nSuspected same product (identifier mismatch, not ranked): {len(suspected)}")


def compare_model(model_key: str, snapshot_path: str) -> None:
    product = get_product(model_key)
    snapshot = load_snapshot(snapshot_path)
    age = snapshot_age_hours(snapshot)
    offers = SnapshotAdapter(snapshot_path, model_key).search("")
    matched, suspected = match_offers(offers, product)
    ranked = rank_offers(matched)

    print(f"Product: {product.brand} {product.model} ({product.variant})")
    print(f"Same-product identifier: {product.identifiers or 'Unverified (title matches must not enter the main ranking)'}")
    if age > STALE_AFTER_HOURS:
        print(f"Note: snapshot is {age:.0f} hours old, over {STALE_AFTER_HOURS:.0f} hours; prices need re-check, do not use as current prices.")
    print(f"Snapshot source: {snapshot['meta']['source']}, collected at {snapshot['meta']['collected_at']}")
    print(f"\nMain ranking (identifier matches): {len(ranked)}")
    for i, offer in enumerate(ranked, 1):
        print(f"{i}. {offer.merchant} | {offer.breakdown()}")
        print(f"   Source: {offer.url}")
    print(f"\nSuspected same-product prices (title matches, unverified identifiers, not ranked, leads only): {len(suspected)}")
    for offer in sorted(suspected, key=lambda o: o.price):
        print(f"- {offer.merchant} | Item ${offer.price:.2f} (shipping unknown, tax not included) | {offer.url}")
    if suspected:
        print("Before ordering, verify model, color, stock, and checkout total on the merchant page.")


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
        print("Use the store/handle format, e.g. www.keychron.com/keychron-k8-pro-...")
        return
    adapter = ShopifyAdapter(store, handle, merchant=store)
    try:
        offers = adapter.search("")
    except AdapterError as exc:
        print(f"Store endpoint returned no usable data, stopped: {exc}")
        return
    matched, suspected = match_offers(offers, product)
    ranked = rank_offers(matched)
    print(f"Product: {product.brand} {product.model} ({product.variant})")
    print(f"Store: {adapter.url} (public product JSON, read-only)")
    if not adapter.stock_field_present:
        print("Stock note: this store's public product JSON has no stock field; 'in stock' only means listed — verify stock on the product page before purchase.")
    print(f"Same-product identifier: {product.identifiers or 'Unverified (title matches must not enter the main ranking)'}")
    print(f"\nMain ranking (identifier matches): {len(ranked)}")
    for i, offer in enumerate(ranked, 1):
        stock = "In stock" if offer.in_stock else "Out of stock"
        print(f"{i}. {offer.merchant} | {stock} | {offer.title}")
        print(f"   {offer.breakdown()}")
        print(f"   Source: {offer.url} | Fetched at {offer.fetched_at}")
    print(f"\nSuspected (identifier mismatch, not ranked): {len(suspected)} variants")
    for offer in suspected:
        print(f"- {offer.title} | Item ${offer.price:.2f} | Identifier {offer.identifier}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="price_agent")
    sub = parser.add_subparsers(dest="command", required=True)
    cmp_parser = sub.add_parser("compare", help="Compare the landed total price of a product")
    cmp_parser.add_argument("query", nargs="?", help="Product name or model, e.g. Sony WH-1000XM5")
    cmp_parser.add_argument("--model", help="Eval-set model key, e.g. sony-wh1000xm5-black")
    cmp_parser.add_argument("--snapshot", default=DEFAULT_SNAPSHOT,
                            help="Snapshot file path (default data/eval_snapshots.json)")
    cmp_parser.add_argument("--shopify", help="Live store: store/handle, e.g. www.keychron.com/keychron-k8-pro-...")
    eval_parser = sub.add_parser("eval", help="Run the full eval set and summarize coverage")
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
            cmp_parser.error("compare needs a query, or use --model to specify an eval-set model")
        compare(args.query)
        return 0
    if args.command == "eval":
        result = evaluate(args.snapshot)
        print(f"Eval set: {result['models']} models, {result['verified_identifiers']} verified identifiers, "
              f"{result['with_snapshot_offers']} with snapshot quotes")
        print(f"Total quotes {result['total_offers']}, identifier matches {result['matched']}, "
              f"title matches (suspected) {result['suspected']}")
        for row in result["rows"]:
            print(f"- {row['key']}: identifier {row['identifier_status']}, quotes {row['offers']}, "
                  f"matched {row['matched']}, suspected {row['suspected']}")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
