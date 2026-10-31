# Architecture

## Architecture in one line

```
User query → identifier normalization (UPC/MPN/SKU) → merchant adapters fetch prices in parallel
        → landed total price calculation → ranking (total price → delivery → reputation) → transparent bill output
```

## Modules

| Module | Responsibility | Current status |
|---|---|---|
| `price_agent/models.py` | Offer / Product data models, total-price calculation | Implemented |
| `price_agent/adapters.py` | Merchant adapter interface + mock merchants | Implemented (mock) |
| `price_agent/ranking.py` | Ranking: total price → delivery days → merchant rating | Implemented |
| `price_agent/cli.py` | Command-line entry point | Implemented |
| Real merchant adapters | Official API / feed / catalog integrations | Phase 1 |
| Price tracker | Scheduled re-checks + price-drop alerts | Phase 2 |
| Constraint validator | Allowlist / caps / budget cap, enforced before ordering | Phase 3 |

## Data model (core fields)

```python
Offer(
    merchant: str,          # merchant name
    title: str,             # merchant product title
    identifier: str | None, # UPC / EAN / MPN / official SKU, the same-product key
    price: float,           # item price
    shipping: float | None, # shipping; unknown = None, never treated as 0
    tax_estimate: float,    # estimated tax (tax-rate basis must be stated)
    coupon: float,          # available public discount (none = 0)
    delivery_days: int | None,
    seller_rating: float | None,  # 0–5
    url: str,               # product page link
    in_stock: bool,
    fetched_at: str,        # ISO time, basis for price-expiry judgment
)
total = price + (shipping or 0) + tax_estimate - coupon
# But when shipping is unknown, the total must be labeled "shipping unknown, not included";
# it must never be presented as an all-in price
```

## Ranking formula (Phase 1, no black-box score)

1. Primary key: offers with known shipping rank by landed total price, low to high; offers with
   unknown shipping rank after all known-shipping offers (their total is only a lower bound and
   not comparable), labeled "shipping unknown, not included".
2. Price tie (difference < $1): shorter delivery wins.
3. Further tie: higher merchant rating wins.
4. Items whose identifiers do not match never enter the main ranking; they go to the
   "suspected same product" appendix table.

From Phase 2 on, quality signals are for display and same-price tie-breaks only, never merged
into a weighted total score — once a weighted score is opaque, the buyer can no longer audit
whom the agent really serves.

## Data-source tiers (restating README's compliance line)

Official API / feed > affiliate catalog > merchant structured data > browser read-only verification.
If any tier is blocked, requires login to see prices, or is explicitly prohibited by ToS, stop at
that tier, record it in the public report, and never work around it.

## Ordering constraints (Phase 3 reserved, interface fixed in advance)

```yaml
constraints:
  allowed_merchants: []   # empty = no automatic ordering allowed
  max_per_order: 0         # per-order cap, 0 = disabled
  total_budget: 0          # total budget cap
  require_confirmation: true  # user approval required before every order
```

Constraint validation happens before payment and independently of ranking logic: ranking says
"this merchant is cheapest", constraints say "whether this order may be paid" — two separate locks.
