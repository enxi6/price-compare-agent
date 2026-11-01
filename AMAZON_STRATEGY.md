# Amazon Strategy: Access Routes, Tier Design, and Sequencing

Status: strategy decision, 2026-11-01 (DECISIONS 018). Amazon data is a
Phase 2 layer, not a Phase 1 scope change. No Amazon spend is approved
by this document; provider choice and Pro pricing are deferred to
Phase 2 evaluation (see "Still open").

## 1. The problem, stated precisely

Amazon blocks automated access (Conditions of Use wall). This is not
a temporary scrape failure; it is a permanent property of the
retailer. It affects the whole plan because Amazon is, for many
electronics models, the price setter or the cheapest offer. A ranking
that silently omits Amazon is incomplete, and an incomplete ranking
that claims to be "the best price" damages trust — trust is the
product.

## 2. Access routes (legitimate channels only)

Direct self-operated scraping that defeats the wall (rotating proxies,
headless browsers, session spoofing) is REJECTED. It violates the
project's compliance red line (DECISIONS 004: blocked means stop, do
not bypass), exposes the project to Amazon enforcement, and would be
the first thing a future partner's diligence kills. The wall is a
signal to buy data through legitimate channels, not a moat to climb.

### Route A — Amazon's own API (official, but gated by sales)

Amazon's affiliate product API (PA-API 5.0) has reportedly been
deprecated in favor of the Creators API (third-party reports put the
PA-API 5.0 deprecation at 2026-04-30 and endpoint retirement at
2026-05-15; verify against Associates Central before building).
Access to the successor requires an Amazon Associates account in
final-accepted status AND a rolling threshold of qualifying referred
sales in the trailing 30 days (third-party reports consistently cite
10; the window is rolling, so a quiet month loses access).
Consequence: a new site with zero Amazon referral traffic cannot get
official API access on day one. The free site must first earn
Associates traffic through tagged links, then qualify. This is a
sequencing constraint, not a reason to scrape.

### Route B — Licensed data providers (the industry-standard route)

Buy Amazon data from a provider that assumes the collection burden:

- Keepa API: token-metered, from about EUR 49/month (20 tokens/min;
  one token buys the full data set for one ASIN, price history
  included). Strength: Amazon price history, Buy Box history, offer
  counts — the depth layer. Lookups accept ASIN, UPC, EAN, ISBN-13,
  which makes it the ASIN-to-UPC bridge (see section 4).
- Rainforest API (Traject Data): credit-based, from $23/month
  (Hobbyist, 500 credits) to $375/month (Production, 250,000
  credits), with per-credit overage. Strength: real-time current
  product/offer/search data by ASIN — the current-price layer.
- Cheaper scraping intermediaries exist (per-request rates far below
  Rainforest's entry tier), but price is not the selection criterion:
  provider terms, data freshness guarantees, and Amazon's position
  toward the provider matter more than the unit rate. Evaluate on
  the 28-product catalog first, not on traffic scale.

### Route C — User-side reads (fallback, not infrastructure)

Prices the user sees in their own browser (e.g., a future browser
extension that reads pages the user opens) are not blocked the way
server-side access is. This is a legitimate fallback for individual
verification, in the same spirit as the Kindle retailer corroboration
pattern, but it is not a data pipeline: it cannot refresh a catalog
on schedule and cannot be the ranking's source of truth.

### Interim pattern (Phase 1, already in use)

Where Amazon is the only missing leg, corroborate through other
retailers (Best Buy, Target) and label the result honestly: price
confirmed, Amazon-official status not confirmed. Never present a
retailer price as an Amazon price.

## 3. Tier design: what Pro pays for (and what it must not buy)

The naive design — "Amazon rows are Pro-only" — is REJECTED, for a
reason that outranks revenue: it breaks the ranking-parity rule
(ROADMAP: free and Pro rankings must be identical) and, worse, it
makes the free ranking misleading by design. If Amazon is cheapest
and free users never see it, the free ranking is not "the best
price", it is "the best price except Amazon". A deliberately
incomplete free ranking undermines the trust that converts free
users to Pro.

Adopted principle: **the ranking is identical across tiers; Pro pays
for depth, freshness, and tools — never for a different answer.**

- Free: full ranking including the Amazon snapshot price (cached,
  timestamped, labeled "as of HH:MM"); 3 active price alerts;
  30-day price history for non-Amazon retailers; standard refresh
  cadence.
- Pro: everything in Free, plus live Amazon refresh on demand; full
  Amazon price history (Keepa layer); Amazon coupon and Lightning
  Deal detection; unlimited alerts with shorter check intervals;
  all-variant coverage for Amazon listings; export and API access
  (later).
- Honest monetization story: "Your subscription pays the Amazon data
  providers." The cost center is real (provider fees scale with
  refresh frequency, not with ranking), so the subscription funds
  freshness, which is exactly what Pro delivers.

## 4. Architecture decisions (design now, build in Phase 2)

- Adapter contract: the Amazon adapter must carry `source_tier` and
  `license` fields (which provider, under which terms), extending
  the adapter compliance-status decision in ROADMAP section 2.
- Identity mapping: Amazon's key is ASIN; ours is UPC/MPN. Map once
  (Keepa accepts UPC/EAN lookups), store the mapping, re-verify on
  a schedule. An unmapped ASIN is never guessed into a ranking.
- Cost control: scheduled refresh (catalog on a fixed cadence, Pro
  on demand), NEVER per-query live calls. Per-query calls would blow
  the token/credit budget at traffic scale; caching is a cost
  decision, not just a performance one.
- Freshness display: every Amazon row carries an `as_of` timestamp
  and the provider name. A cached Amazon price is never presented
  as live. Display rule: "Amazon price as of HH:MM — verify at
  checkout."
- Graceful degradation: if a provider is down or quota-exhausted,
  the Amazon row shows its stale timestamp (or is hidden with an
  explicit note). Amazon is never silently dropped from a ranking.
- Disclosure and ranking integrity: Associates disclosure is
  required when linking to Amazon with a tag ("As an Amazon
  Associate we earn from qualifying purchases"). Amazon commission
  must not affect rank, under the same rule as every retailer
  (DECISIONS 001).
- Legal review: provider terms and the Associates Operating
  Agreement must be reviewed before any Amazon row ships. This
  fills one item of ROADMAP section 7 (legal-review channel), which
  is currently empty.

## 5. Sequencing

- Phase 1 (now): Amazon-free. Finish the open-retailer ranking and
  prove ranking trust. No Amazon spend.
- Phase 2 (with the website): join Amazon Associates; place tagged
  links on free pages; build toward the referred-sales threshold
  for official API eligibility. In parallel, trial Keepa API vs
  Rainforest API on the 28-product catalog and pick on freshness
  per dollar, not on headline rate.
- Phase 3 (only after subscriptions exist): Amazon depth features
  (live refresh, history, deal detection) ship as the Pro
  differentiator, funded by the subscriptions they justify.

## 6. Still open (decided during Phase 2, not on launch day)

- Pro subscription price (no number is set by this document).
- Refresh cadence for the Amazon snapshot layer.
- Provider choice (Keepa vs Rainforest vs official API once
  eligible), and whether to run two providers for redundancy.
- Whether a delayed Amazon price (e.g., 24h snapshot) for free
  users is ever needed for cost reasons; the default is the same
  snapshot for all tiers.
- Legal-review channel (who reviews provider terms and the
  Associates agreement).

## 7. Why this is not a moat (honest framing)

Other comparison sites face the same wall, but the established ones
already solved it through exactly these channels (official API,
Keepa, Rainforest). Access is therefore not the moat. The moat is
cost efficiency (refresh cadence per dollar), freshness discipline
(timestamped, never stale-presented-as-live), and ranking integrity
(commission-blind, identical across tiers). Those are the things a
competitor cannot copy by buying the same API key.
