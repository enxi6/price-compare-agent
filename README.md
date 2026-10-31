# Price Compare Agent

A price-compare agent that stands on the buyer's side: give it a product, and it compares the **landed total price** across merchants, breaking down every cent for you.

## Inspiration

Stripe CEO Patrick Collison's 2026-10-09 long post on X, 《Assorted things I've been mulling over
regarding agents in the economy》: companies are "primitive superintelligences" that can use
diluted cognitive surplus against consumers with limited attention and incomplete information;
personal agents shrink that gap — searching for alternatives, comparing terms, finding discounts,
watching subscriptions — and thereby become "a structural subsidy for product quality".
This project builds the "price comparison" piece of that post, hands-on: **the agent serves the buyer only**.

## Buyer-side stance (non-negotiable principles)

1. **Rank for the buyer only**: rankings consider only buyer-favorable factors (landed total price,
   delivery time, merchant reputation). No paid rankings, ad placements, or commission bias, ever.
   If affiliate commission revenue exists in the future, it must be disclosed in the results
   and must not affect ranking.
2. **Total cost first**: compare not the sticker price but the landed total price = item price +
   shipping + estimated tax − available discounts, listing every component with its source and
   fetch time.
3. **Same product only**: only items with matching UPC / EAN / MPN / official SKU count as the
   "same product". Items with similar titles but mismatched identifiers are labeled separately
   as "suspected same product, unconfirmed" and never mixed into the ranking.
4. **Never spend your money recklessly**: automatic ordering (if ever built) must simultaneously
   satisfy: your prior approval + a per-order cap + a merchant allowlist + a total budget cap,
   all required. By default, compare only — never order.
5. **Compliant data sourcing**: prefer official APIs / product feeds / affiliate catalogs; respect
   robots.txt and merchant ToS. If blocked, stop and switch to a legitimate channel — never bypass
   verification or fake an identity.

## Quick start (minimal skeleton, mock merchant data)

```bash
cd price-compare-agent
python3 -m price_agent.cli compare "Sony WH-1000XM5"
python3 -m unittest discover -s tests -v
```

Sample output: landed-total-price rankings per merchant, each cost component, delivery days,
merchant ratings. The current version is a skeleton: merchants are mock data used to validate the
compare core and ranking logic; real merchant integrations proceed in the phases of `PLAN.md`.

## Directory structure

```
README.md          This file: vision and principles
PLAN.md            Detailed steps and plan (phases, milestones, acceptance criteria)
ARCHITECTURE.md    Architecture, data models, ranking formula, data-source tiers
DECISIONS.md       Decision log (the reasoning behind each key trade-off)
BUILD_LOG.md       Public build log (build in public)
CONTRIBUTING.md    Contributing guide
LICENSE            MIT
price_agent/       Source: models, ranking, merchant adapters, CLI
tests/             Tests
```

## Roadmap (summary; see PLAN.md for details)

- Phase 0: Project setup and open-source infrastructure (this repository) — started
- Phase 1: Same-product compare core (identifier normalization + landed total price + transparent bill)
- Phase 2: Quality signals (reviews, returns, merchant reputation) and price-tracking alerts
- Phase 3: Constrained order placement (allowlist + caps + prior approval)
- Phase 4: Category expansion and public eval set (regression-test ranking quality on real products regularly)

## Status

Early skeleton; issues and PRs are welcome. The roadmap and trade-offs are governed by `DECISIONS.md`.
