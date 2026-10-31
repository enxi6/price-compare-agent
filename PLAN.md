# Detailed Steps and Plan

Goal: build a **price-compare agent that serves the buyer only**, starting from a "minimal
comparison that runs" and step by step reaching "trusted enough to compare for you, and even
order for you". Fully open source, with the process public.

Inspiration anchor: Patrick Collison's 2026-10-09 long post — personal agents make consumers
more rational and reward good products rather than big advertising; the agent's loyalty must
belong to the buyer.

## Phase 0: Project setup and open-source infrastructure (this week, started)

- [x] Repository skeleton: README / PLAN / ARCHITECTURE / DECISIONS / BUILD_LOG / LICENSE / CONTRIBUTING
- [x] Minimal compare core + mock merchants + tests (`python3 -m price_agent.cli compare` runs)
- [x] Public repository created on GitHub and pushed (created 2026-10-31 at https://github.com/enxi6/price-compare-agent;
  from Phase 1 on, local commits and the remote upload history are out of sync — the history
  difference must be handled before pushing)
- [x] First category set: standardized electronics models (user said "start" on 2026-10-31 without changing the default)
- [x] Eval set set: 20 specific models (`price_agent/catalog.py`), 6 identifiers verified, 14 pending

Acceptance: someone else can clone and run the demo within 5 minutes; the repository homepage
explains clearly "whom it serves and what it ranks by".

## Phase 1: Same-product compare core (weeks 1–2)

1. **Identifier normalization**: UPC / EAN / MPN / official SKU as the primary key; titles and
   images are supporting evidence only. Title-similar items that do not match go to the
   "suspected same product" branch, never into the main ranking.
   (2026-10-31 progress: matching module and 20-model eval set landed, 6 identifiers verified.)
2. **Landed total price**: `total = item price + shipping + estimated tax − discount`, showing
   source and time per component; shipping is estimated by delivery location (default: United
   States); merchants without shipping data are labeled "shipping unknown", never counted as 0.
3. **Data-source tiers** (in priority order; move down only when a tier is unavailable):
   1. Official APIs / product feeds (brand official sites, Shopify stores' public product
      endpoints, eBay API, etc.)
   2. Affiliate product catalogs (aggregated catalogs such as Meta Catalog)
   3. Merchant structured data (product-page JSON-LD / Open Graph)
   4. Browser manual verification (read-only, rate-limited, respecting robots and ToS;
      stop if blocked)
   Never use: fake identities, CAPTCHA bypasses, brute-force scraping.
   (2026-10-31 progress: catalog snapshot connected with 12 real quotes; Shopify adapter code
   implemented; real stores to be connected after their domains and handles are verified.)
4. **Transparent bill**: every quote carries merchant, link, fetch time, and price composition;
   prices older than 24h are labeled "needs re-check", never presented directly as current prices.
5. **CLI → simple web page**: CLI first, then a read-only results page (enter product →
   ranking table). No account system.

Acceptance: across the 20 eval models, same-product identification accuracy ≥ 90%, and landed
total prices fall within an explainable shipping/tax range of merchant checkout pages; every
quote is traceable to its source.

## Phase 2: Quality signals and price tracking (weeks 3–4)

1. **Quality signals**: alongside total price, show merchant rating, review count, return policy,
   and estimated delivery; ranking still leads with total price, and quality signals act as the
   second sort key for "same price, pick whom" — no black-box composite score.
2. **Price tracking**: re-check products the user watches on a schedule and alert when the price
   drops to the target (alerts only at first, never auto-buy); alert records are publicly auditable.
3. **Coupon verification**: only publicly available merchant coupon codes; no "internal coupons",
   no invented discounts; expired coupons must be detectable and labeled.
4. **Anti-gaming**: detect and label tricks such as "low sticker price but high shipping",
   "clickbait variants", and "refurbished sold as new"; each finding goes into the eval set.

Acceptance: tracking alerts on time with explainable false positives; quality signals have
sources, not model-invented.

## Phase 3: Constrained order placement (weeks 5–8, starts only with separate approval)

This is the most sensitive step, where "whom the agent is loyal to" from Collison's post lands:

1. **Constraints first**: allowlisted merchants, per-order cap, total budget cap, category limits,
   written as a machine-checkable constraints file; orders exceeding constraints are rejected at
   the payment step (following Stripe's SPT-style constraint thinking: allowed_merchant /
   amount / budget — over the limit means declined).
2. **Confirm before ordering**: before every order, present "what, which merchant, total price,
   delivery date" to the user at once; execute only on the user's approval; never "buy first,
   report later" by default.
3. **Payment isolation**: payment credentials go through a wallet / trusted payment channel, never
   handed to agent code; start with paper / small real orders before scaling.
4. **Auditable**: every order leaves a trail: decision basis (why this merchant), price snapshot,
   constraint-check results. Users can review anytime and cancel unshipped orders.

Acceptance: all constraint tests pass (including three rejection scenarios: over budget,
non-allowlisted merchant, price change); 10 consecutive small real orders with zero "wrong item,
overpaid, over budget" incidents.

## Phase 4: Category expansion and public eval (ongoing)

1. For each new category, first add that category's same-product identifier rules and eval set,
   then connect merchants.
2. Publish a public eval report monthly: same-product accuracy, total-price error, merchant
   coverage, blocked channels; publish ugly numbers as they are — that is where an open-source
   project's credibility comes from.
3. Accept external PRs for merchant adapters, but each adapter must include: a data-source
   legitimacy statement + eval cases. Missing either means no merge.

## Risks and countermeasures

| Risk | Countermeasure |
|---|---|
| Merchants block the agent (Amazon and others are not friendly to outside agents) | Start from open channels; stop when blocked, never fight back; write "not covered" into the report |
| Same-product misidentification (variants, refurbished, regional versions) | Identifier primary key + suspected branch + eval-set regression |
| Stale prices / inaccurate shipping and tax estimates | Per-item source + timestamp + "needs re-check" label; never present estimates as current prices |
| Loyalty conflict (commissions, ads) | Ranking decoupled from revenue; commissions disclosed truthfully, never affecting ranking |
| Runaway automatic ordering | Constraints file + prior confirmation + payment isolation + auditability; missing any one means no launch |

## Decisions pending from you this week

1. GitHub publishing method (choose one of two, see the options in the reply): I log in via
   browser as you to create the public repository and push, or keep working locally and push later?
2. First category: default is "standardized electronics models". If you want to switch (e.g. books,
   specific sneaker models), one sentence will do.
3. Target market: default is the United States (merchant, shipping, and tax conventions all US).
   Say so first if another market is needed, because tax and merchant lists would all differ.
