# Long-Term Roadmap (ROADMAP)

> Positioning: this file is the **product and business timeline**, answering "how the website
> launches, how the app launches, and how money is charged". `PLAN.md` is the build phases
> (Phase 0–4); this file is the timeline (near-term – mid-term – long-term). They align via
> the mapping table below and do not replace each other.
>
> Non-negotiable bottom lines (from `DECISIONS.md`; if any line in this file conflicts with
> them, the bottom lines prevail):
> 1. Rank for the buyer only; ranking is decoupled from revenue;
> 2. Same products align by identifier (UPC / EAN / MPN / official SKU); title similarity only
>    enters the suspected table;
> 3. Compare first, do not order yet; ordering needs a separate approval;
> 4. Compliant data sourcing: stop when blocked; no bypassing verification, no fake identity.
>
> This file contains no revenue figures, partner merchants, or user private information;
> anything undecided is written as "to be confirmed" — never dress up a placeholder number
> as decided.

## 0. Status snapshot (2026-10-31)

| Item | Status |
|---|---|
| Phase 0 | Complete; public repository https://github.com/enxi6/price-compare-agent |
| Phase 1 | In progress: eval set of 28 models, 27 verified identifiers (only DualSense White pending on a UPC conflict); Shopify public JSON adapter verified against a live store; Meta Catalog snapshot of 12 quotes (covering 5 models) |
| Phase 2 | Not started: quality signals + price-tracking alerts |
| Phase 3 | Not started, needs the user's separate approval: constrained order placement |
| Phase 4 | Not started: category expansion and monthly public eval |
| Known gaps | Snapshot quotes carry no UPC, so all land in the suspected table and the main ranking is 0; the Apple cluster (8 models) has identifiers but no quote source — Apple's own site, Amazon, and Best Buy are not Shopify and need new adapters |

## 1. Timeline and PLAN mapping

| Period | This file's section | Corresponding PLAN phase | Core output |
|---|---|---|---|
| Near-term, 1–2 months | §3 Website launch | Phase 1 wrap-up + Phase 2 start | A publicly accessible price-compare website |
| Mid-term, 3–6 months | §4 App Store launch | Phase 2 complete + Phase 3 preparation | iOS app (TestFlight → full launch) |
| Long-term, 6–12 months and beyond | §5 Monetization | Phase 3 (separate approval needed) + Phase 4 | Freemium subscription, optional order-placement service fee |

Dependency chain (each later link requires the earlier link's acceptance; no skipping):

```
Identifier system and snapshot format finalized (§2)
  → Website static pages + read-only API (§3)
    → Price tracking and alerts (Phase 2, validated on the website first)
      → iOS app reusing the same API (§4)
        → Subscription monetization (§5 Stage 1)
          → Order-placement service fee (§5 Stage 2, needs Phase 3 acceptance + user's separate approval)
```

## 2. Architecture decisions to lock in now (or pay for major rework later)

These 8 items are the most important part of this file. Changing them now costs "a few lines";
changing them after the website and app are both live costs "data migration + dual-client
releases + user-data compatibility". Each item states "what to lock in now" and "what it costs
not to".

### 2.1 Identifier system: `identifier` is the global primary key, never redefined

- Lock in now:
  - Eval-set entries (`catalog.py`) are the seeds of the future product database: every entry
    must have a stable `product_key` (e.g. `apple-macbook-air-13-m4`), decoupled from merchant
    SKUs, variants, colors, and configurations; once published, a `product_key` is never reused
    and never repointed.
  - The identifier normalization rules (`identity.py`: strip leading zeros, strip punctuation,
    unify case) are the single normalization standard across GTIN-14 / UPC-12 / EAN-13; the
    website and app must not each write their own.
  - One entry = one "comparable configuration" (chip + memory + storage + color + network
    type). The Apple cluster already proved it: a different color is a different part number,
    a different configuration is a different SKU.
- Cost of not locking in: changing the primary key after the website launches = all site links
  dead + price history broken; changing it after the app launches = forced upgrade + user
  tracking lists invalidated.

### 2.2 Quote snapshot format: append-only, versioned, sourced

- Lock in now (fill these in before the `Offer` model lands, or website v1 needs rework):
  - Snapshots gain a `schema_version` field (starting at 1); format evolution only adds fields
    and never redefines old ones; old snapshots are never edited in place — a price change is a
    new snapshot row.
  - Every quote must carry: `product_key`, `merchant`, `price`, `shipping` (unknown = null,
    never 0), `tax_estimate` with its tax-rate basis, `coupon`, `url`, `fetched_at`,
    `source_tier` (official API / catalog / structured data / browser verification), `condition`
    (new / refurbished / used), `bundle` (whether a bundle), `region` (default US).
    The current `Offer` lacks `source_tier`, `condition`, `bundle`, and `region` — these four
    must be added before the website launches, because Phase 2 anti-gaming (refurbished sold as
    new, bundles posing as single items) depends entirely on them.
  - The price-history table is designed now as "(product, merchant, fetch time) → price
    composition"; tracking alerts read the history table directly — no second scraping pipeline
    just for tracking.
- Cost of not locking in: without `condition` / `bundle`, when the first wave of website users
  complains "the comparison showed me a refurbished unit", there is no fix without changing the
  schema.

### 2.3 API boundary: the core engine is a pure library; website and app are its callers

- Lock in now:
  - The `price_agent/` core (identifier → adapter → total price → ranking) stays a **pure
    library with no CLI, web, or app dependencies**; the website and iOS app call it only through
    a thin API layer and must not each implement their own ranking.
  - API contracts are versioned (`/api/v1/compare`, `/api/v1/track`, etc.); once v1 ships,
    breaking changes require a version bump — never silently change a field.
  - The ranking function must be deterministic and side-effect-free: the same input produces the
    same ranking on every client. This is the only code-level verifiable form of "ranking is
    decoupled from revenue".
- Cost of not locking in: one ranking on the website, another in the app, and sooner or later
  "the same product ranks differently on the two clients" — trust collapses outright, and it is
  unexplainable during App Store review.

### 2.4 Ranking/revenue code isolation: enforced by tests, not by verbal promise

- Lock in now:
  - All revenue code (affiliate commissions, ads, subscriptions, service fees) lives in a
    separate module that **`ranking.py` is forbidden to import**; an automated test asserts this
    dependency ban, and a CI failure blocks merging.
  - Commission disclosure is a presentation-layer duty: quote cards state "this link may earn a
    commission; the commission does not affect ranking". The disclosure copy is in §5.4; the
    presentation layer may change it, the ranking layer may not touch it.
- Cost of not locking in: once revenue logic seeps into ranking, no later claim of "we do not
  sell rankings" can be substantiated, and an open-source project's credit foundation is gone.

### 2.5 Currency and region: the US convention is a pluggable module, not hardcoded

- Lock in now: shipping estimation and tax estimation (state tax-rate conventions) are each
  standalone modules taking (product, merchant, delivery state) and returning an estimate +
  basis note; a market beyond the US = a new set of modules and merchant lists, not a core change.
- Cost of not locking in: tax rates hardcoded into ranking code mean expanding markets is a rewrite.

### 2.6 Adapter contract: every adapter declares its own compliance status

- Lock in now: beyond fetching prices, the adapter interface must declare `tier` (data-source
  tier), `rate_limit`, and `blocked` status; a blocked adapter fails closed (raises an error,
  recorded in the coverage report), and callers must not silently degrade to adversarial scraping.
- Cost of not locking in: after the website launches, a blocked channel gets quietly replaced by
  a rule-breaking method, and the whole project carries the legal risk.

### 2.7 User and alert identity: the website's v1 choice decides the app's account migration cost

- Lock in now (choose at website v1, see §3.4):
  - Website v1 has no password accounts: price-drop alerts use email subscription + token
    unsubscribe links; no passwords stored, no payment information stored.
  - User records are keyed by email; when the app phase introduces Apple ID sign-in, the same
    email merges into the same user, and the website subscription's tracking list carries into
    the app automatically.
  - If accounts are introduced later, the App Store requires an in-app account-deletion entry —
    the data model reserves the semantics "user deletion = tracking list and alerts cleared
    together" from now.
- Cost of not locking in: the website uses one anonymous ID scheme and the app another account
  scheme, tracking lists cannot merge, and users end up with one list on each client — losing on
  both experience and data.

### 2.8 Data freshness and expiry semantics: an expired price is not a price

- Lock in now: the snapshot expiry threshold (currently: >24h labeled "needs re-check") is
  written into the API contract, and the website and app show the same copy; on refresh failure,
  keep the previous snapshot labeled "expired" — never present an estimated or stale price as
  current.
- Cost of not locking in: inconsistent expiry copy across clients means users see a price in the
  app that is not on the website and mistake it for a live price when ordering.

---

## 3. Near-term (1–2 months): Website launch

### 3.1 Shape: static-first + thin API; no full dynamic web app

| Option | Approach | Pros | Cons | Verdict |
|---|---|---|---|---|
| A. Pure static site | Render snapshots to HTML on a schedule, deploy to static hosting | Lowest cost, search-engine indexable, no user-data liability, lowest blocking risk | No results for models not yet indexed | **v1 main shape** |
| B. Static site + read-only API | A + one read-only API: any model a user enters is priced live via adapters | Covers any model, still no accounts, no writes | Needs one always-on service or serverless, slightly higher cost and ops | **Build alongside v1, API read-only** |
| C. Full dynamic web app | Accounts, tracking management, and back office all on the website | Fullest features | Cost, compliance, ops, and security responsibility all maxed at once; v1 does not need it | Rejected, deferred to long-term |

Reasoning: v1's goal is "let people verify this comparison is trustworthy", not "build a complete
product". Static pages are naturally auditable (each compare page is a timestamped public
snapshot), consistent with an open-source project's credibility logic; accounts and write
operations are all deferred until real demand exists.

### 3.2 Page and feature list (v1)

| Page | Content | Acceptance criteria |
|---|---|---|
| Home + search | Enter a product name or UPC/MPN to reach a compare page; popular-model entries (starting from the 28-model eval set) | All 28 eval models have result pages; unknown models clearly say "not indexed", never invent results |
| Product compare page (core) | Main ranking (identifier matches), landed-total-price itemization, source and fetch time per item, expiry labels (>24h shows "needs re-check"), suspected-same-product appendix, refurbished/bundle labels | Every quote traceable to a source link and time; unknown-shipping offers rank after known-shipping ones and are labeled "shipping unknown, not included" |
| Method and principles page | Ranking rules, identifier rules, data-source tiers, commission disclosure, handling of blocked channels | Copy consistent with `DECISIONS.md`; no black-box phrasing like "composite score" anywhere |
| Coverage and gaps page | Merchant coverage per model, gaps (e.g. Buds2 Pro white has no clean quote), blocked channels | Gaps written truthfully; numbers consistent with the monthly eval report |
| Price history page (Phase 2 linked) | Price trend for a chosen model (reads the §2.2 history table) | Every trend point comes from a real snapshot; no interpolation, no smoothing |
| Price-drop alert subscription | Email subscription + target price, token unsubscribe (§2.7) | Subscription confirmed on success; one-click unsubscribe works; no marketing mail beyond subscriptions |
| Apple showcase page (optional, Phase 4 precursor) | Collection page for the 8 Apple models, reusing the same compare-page template with no separate logic | Same data source and same ranking as ordinary compare pages; the page is only a filtered view |

Explicitly excluded from v1: account registration and login, on-site payment, user reviews,
merchant onboarding entries, and any "recommended for you" feature — once a recommendation
algorithm appears, ranking neutrality becomes indefensible.

### 3.3 Data refresh mechanism

- Scheduled refresh (cron / scheduled jobs), with frequency by data-source tier:
  - Tier-1 (official APIs / feeds / Shopify public JSON): at least once daily, more often for
    popular models;
  - Tier-2 (affiliate catalogs): once daily;
  - Tier-3/4 (structured data / browser read-only verification): once weekly or manually
    triggered, rate-limited, respecting robots and ToS.
  - Exact frequencies follow each channel's compliance ceiling; to be confirmed.
- Refresh failure policy: keep the previous snapshot + label it "expired" and record it in the
  coverage report; when consecutive failures reach a threshold (threshold to be confirmed), the
  channel is marked "temporarily unavailable" on the coverage page — never silently disappearing.
- Blocking policy: immediately disable the channel, record it in the public report, no identity
  switching, no verification bypass (§2.6).
- Static page generation: re-render affected model pages after each successful refresh; a failed
  render never publishes a half-finished page.
- Quote-source priority: the Apple cluster currently has no quote source — before the website
  launches, at least one identifier-returning tier must be connected, or the Apple showcase page
  may only show "no verifiable quotes yet" and must not pass off the suspected table as a ranking.

### 3.4 Lowest-cost hosting plan

- Static site: static-hosting free tier (one of Cloudflare Pages / GitHub Pages / Netlify,
  to be confirmed); 1 domain, cost per the registrar's price at the time, to be confirmed.
- Read-only API and scheduled refresh: one minimal always-on service, or serverless functions +
  scheduled triggers; selection principle is "use the free tier while it covers usage" and only
  evaluate scaling after exceeding it — never buy a large instance in advance.
- Alert email: reuse an existing email-sending channel (provider to be confirmed); email volume
  = subscriptions × triggers, with free-tier limits per the provider's price at the time, to be
  confirmed.
- Not purchased in v1: paid database instances (snapshots start as versioned JSON files + object
  storage), paid CDN tiers, paid monitoring services (free tiers and logs first).
- Cost review point: review actual usage at the end of the first month after website launch;
  decide on scaling only if free tiers are exceeded, never expand early.

### 3.5 Near-term milestones

| Milestone | Depends on | Acceptance criteria |
|---|---|---|
| M1.1 Snapshot format finalized | §2.2 | `Offer` contains all §2.2 fields; old snapshots identifiable by `schema_version`; test coverage |
| M1.2 Ranking/revenue isolation test | §2.4 | Dependency-ban test in CI and passing; disclosure copy finalized (see §5.4) |
| M1.3 Static site live | M1.1, M1.2, at least one identifier-returning quote source | All 28 models have compare pages; every quote has source and time; expiry labels active |
| M1.4 Read-only API + alert subscription | M1.3, §2.7 | Any-model queries run through the same ranking engine; subscribe and unsubscribe work end to end; refresh-failure policy tested live |

---

## 4. Mid-term (3–6 months): App Store launch

### 4.1 App shape: native shell + shared API; no pure wrapper

- Conclusion: **a SwiftUI native app calling the same read-only API from §3; static content
  pages may be shown in a WebView inside the native shell, but the app's main features must be
  native.**
- Why pure wrappers are rejected (wrapping the whole website in a WebView for launch): Apple
  has minimum-functionality requirements for "website-wrapper-only" apps, so a pure wrapper
  carries high rejection risk; and a wrapper cannot deliver the genuinely native capabilities
  (push notifications, barcode scanning, home-screen widgets) — launching it would be pointless.
- Features that must be native (the app's legitimacy rests on them):
  1. **Price-drop push alerts**: push when a tracked model drops to its target price — something
     the website cannot do, and the core reason a user would install the app; also the mobile
     landing point for Phase 2 tracking alerts.
  2. **Barcode scanning for comparison**: scan a barcode in-store → UPC/EAN → straight to
     compare results. The identifier system (§2.1) exists for this feature; without an identifier
     primary key, scanning has nothing to start from.
  3. **Tracking-list management**: view, add, and delete tracked models; edit target prices.
  4. **Home-screen widget (optional, v1.1)**: a tracked model's current lowest price; tap into
     the app for details.
- Website/app division of labor (avoid building everything twice):
  - Ranking, identifier matching, price history: implemented once, server-side; both clients
    only render.
  - Alert subscriptions: website uses email; app uses push + email (same user record, §2.7).
  - Payments (long-term subscriptions): each client uses its own compliant channel (§4.3);
    no shared payment code.

### 4.2 Data-reuse architecture with the website (reserved now, unchanged later)

```
iOS App (SwiftUI)
   │  HTTPS, API v1 (versioned contract, §2.3)
   ▼
Read-only API (same service as the website)
   │  calls
   ▼
Core engine price_agent (identifier → adapter → total price → ranking, pure library)
   │  reads
   ▼
Versioned snapshots + price history table (§2.2)
```

- Hard constraints (locked in now):
  - The app must not embed its own ranking logic, identifier-normalization logic, or price
    estimation logic; every ranking comes from server responses. The client only renders,
    switches sort fields (total price / delivery, with rules consistent with the server),
    and shows expiry labels.
  - Once API v1 fields ship, no breaking changes during the app's release cycle; to change,
    ship v2 and keep v1 for a while (parallel-run length to be confirmed).
  - Push-trigger logic lives server-side (price refresh → compare against target price → push),
    not client polling; client polling wastes battery, is unreliable, and cannot stay consistent
    with website alerts.

### 4.3 Launch compliance checklist (verify item by item against Apple's review guidelines at submission time)

| Item | Approach | Notes |
|---|---|---|
| Consistent feature disclosure | Release notes, screenshots, and preview videos for the submitted build must match the binary's actual features; test features and unlaunched features must not be hidden in the bundle | One of the most frequent rejection causes; build a "disclosure vs binary" checklist before release |
| No hidden features | No feature switches or remote-config backdoors that activate only outside the review period | Remote config may change copy and thresholds only, never feature visibility |
| Subscriptions and in-app purchase | Digital subscription features must go through StoreKit in-app purchase; offer restore purchases; show subscription terms, price, and renewal terms in full before purchase; never steer users inside the app to external payment for digital features | Exact rules per the guidelines at submission time, to be confirmed; website payments and app payments comply separately, never mixed |
| Privacy policy and labels | Provide the privacy policy link both in-app and in App Store Connect; fill in privacy labels truthfully (email for alerts, push tokens, whether scan records are uploaded); no cross-app tracking without user consent | If claiming "no data collected", scan and search records must not be uploaded to the server — decide now, see below |
| Data-collection decision (decide now) | Recommended: search and scan records are not uploaded by default and no user profiles are built; only when a user actively subscribes to alerts are email and tracking lists saved | This decision shapes the privacy-label wording; changing it before submission means refilling labels + re-review — the earlier it is set, the better |
| Accounts and deletion | If accounts are introduced, in-app account deletion must be provided, and deletion clears tracking lists and alerts (§2.7) | Website v1 email subscription does not count as an "account", but this rule takes effect immediately once the app introduces sign-in |
| Trademark and source statements | App description and in-app copy state that prices come from public channels and merchant pages, with affiliate commission disclosure consistent with the website (§5.4) | Never imply an official partnership with Apple, Amazon, Best Buy, etc., unless a written partnership exists (to be confirmed; if none, do not write it) |
| Price authenticity | Prices in screenshots and previews must come from real snapshots — never use invented "sample low prices" | When making screenshots, use that day's snapshots and label the fetch time |

### 4.4 Mid-term milestones

| Milestone | Depends on | Acceptance criteria |
|---|---|---|
| M2.1 API v1 frozen | §2.3, M1.4 | Contract documentation finalized; regression test that website and API use the same ranking engine passes |
| M2.2 TestFlight internal testing | M2.1, push channel | Barcode comparison, tracking lists, and price-drop push work in TestFlight; crash rate and push delivery rate have measured records |
| M2.3 Privacy and compliance self-check | §4.3 checklist | Privacy labels, privacy policy, subscription terms, and disclosure copy checked item by item; no hidden features |
| M2.4 Full launch | M2.2, M2.3 | Target: pass review on the first attempt; on rejection, fix item by item per reviewer feedback — never bypass review or resubmit under a new bundle name |

---

## 5. Long-term (6–12 months and beyond): Monetization

Evolution principle: **each step starts only after the previous step is verified; any step that
harms "ranking decoupled from revenue" is rolled back immediately, no clinging.** Trigger
conditions, pricing thinking, and compatibility notes for each step follow; all specific price
tiers and threshold numbers are to be confirmed and must not be hardcoded before verification.

### 5.1 Stage 0: Free + affiliate commission disclosure (starts at website launch)

- Model: users use all compare features free; when a user completes a purchase via a link from
  this site, the merchant's affiliate program may pay a commission (whether one arises, and at
  what rate, per each affiliate program's terms at the time, to be confirmed).
- Compatibility notes (proof of compatibility with DECISIONS 001):
  - Ranking inputs contain no commission field (§2.4's dependency-ban test is the evidence);
  - Every quote card carrying an affiliate link is labeled "this link may earn a commission;
    the commission does not affect ranking";
  - The method page publicly explains the commission mechanism and isolation measures.
- Conditions for the next stage: the website's real usage over a sustained period (period to be
  confirmed) — compare request counts, alert subscription counts — reaches pre-written thresholds,
  and ranking accuracy and coverage acceptance keep passing. Threshold numbers to be confirmed,
  not guessed.
- Signal not to start subscriptions: if user feedback concentrates on "coverage too thin, prices
  inaccurate", fix coverage and accuracy first, not monetization; charging for inaccurate
  rankings only accelerates trust loss.

### 5.2 Stage 1: Freemium subscription

- Tiers (feature boundaries set now; prices to be confirmed):

| Tier | Includes | Excludes |
|---|---|---|
| Free | Full comparison, suspected table, basic tracking (tracked-model count capped, cap to be confirmed), daily price refresh | Instant push, high-frequency refresh, full price history curves |
| Pro (subscription) | Uncapped tracked models, instant price-drop push, high-frequency refresh, full price history and price-drop statistics, priority coverage of the Apple showcase and new categories | Order placement (that is Stage 2, separately charged and separately confirmed) |

- Pricing thinking (method, no hardcoded numbers):
  - Anchor: the order of magnitude a successful comparison saves the user — the subscription
    price should be well below that, so that "subscribe for a month, save on one order" holds
    intuitively; specific tiers to be confirmed.
  - Structure: monthly + annual (annualized below monthly × 12); iOS via StoreKit, website via a
    compliant payment channel; price conventions per each channel's rules, to be confirmed.
  - Trial: whether a trial period is offered and its length, to be confirmed; before a trial ends
    there must be a clear reminder — no "silent conversion".
- Compatibility notes: free users and Pro users see **exactly the same rankings**; Pro buys
  alert speed, tracking capacity, and history data — not better rankings, not priority display.
  Any design where paying users see different rankings is rejected outright.
- Trigger conditions: Stage 0 trigger conditions met + alert subscription volume proving users
  genuinely need "price watching" (not one-off comparison); otherwise there is nothing to sell
  a subscription on.

### 5.3 Stage 2: Optional order-placement service fee (needs Phase 3 acceptance + user's separate approval)

- Preconditions (all required, all from PLAN Phase 3):
  1. Constraints file first: allowlisted merchants, per-order cap, total budget cap, category
     limits, machine-checkable;
  2. Per-order user confirmation before every order (what, which merchant, total price, delivery
     date); never "buy first, report later" by default;
  3. Payment isolation: payment credentials go through a wallet / trusted payment channel, never
     handed to agent code;
  4. Acceptance: all constraint tests pass (including the three rejection scenarios: over budget,
     non-allowlisted merchant, price change), and 10 consecutive small real orders have zero
     "wrong item, overpaid, over budget" incidents;
  5. The user's separate approval of the order-placement feature itself (already agreed in PLAN
     and restated here — a Pro subscription must never be read as implied consent to ordering).
- Fee structure:
  - A per-order execution service fee (flat fee or capped percentage fee, specifics to be
    confirmed), **disclosed in advance** on the user's per-order confirmation page; confirmed
    price = item total + service fee, with no fees added after confirmation.
  - The service fee charges for the "order execution" service, not for "ranking"; users who do
    not pay the service fee still see the same ranking and can order from merchants themselves.
- Exit conditions: any real order with a wrong item, over-budget charge, or constraint failure
  immediately suspends order placement with a public explanation; it resumes only after fixes and
  re-acceptance. Never run while broken.

### 5.4 Disclosure copy (final-draft wording; user confirms before launch)

> The copy below is a draft, not legal advice; formal legal review through a legal channel is
> recommended before launch (to be confirmed).

- Affiliate commission (quote cards):
  > "This link may earn an affiliate commission. The commission is paid by the merchant, does not
  > increase your purchase cost, and does not affect this page's ranking — ranking considers
  > only factors in your favor."
- Subscription (before purchase):
  > "A Pro subscription provides faster price-drop alerts, more tracked models, and full price
  > history. Free users and Pro users see exactly the same rankings."
- Order placement (per-order confirmation page):
  > "You are authorizing this service to place an order for you: [product], [merchant], landed
  > total [amount], including service fee [amount], estimated delivery [date]. Orders not yet
  > shipped can be canceled after confirmation."

### 5.5 Models explicitly not pursued (written down so a future "just this once" cannot talk us into them)

| Model not pursued | Reason for rejection |
|---|---|
| Selling rankings / paid top placement / paid merchant inclusion | Directly violates DECISIONS 001; once money changes rankings, the project turns from a buyer tool into an ad slot |
| Hidden commissions (taken but undisclosed, or buried in fine print) | Incomplete disclosure = no disclosure; trust loss is irreversible |
| Paid inclusion lists / paid removal of bad reviews / paid suppression of competitors | Same as above, and it destroys eval-set neutrality |
| Selling user data (search records, tracking lists, emails) | Conflicts with the §4.3 data-collection decision; once users find out, they leave permanently |
| Selling price data to merchants for dynamic price increases | Turns the agent's intelligence against buyers; loyalty flips outright |
| Fake discounts, internal coupons, invented coupon codes | PLAN Phase 2 already sets: only public coupon codes; expired coupons must be detectable and labeled |
| Charging merchants a "ranking optimization consulting fee" | Isomorphic to selling rankings; a different name does not change it |

### 5.6 Long-term milestones

| Milestone | Depends on | Acceptance criteria |
|---|---|---|
| M3.1 Stage 0 disclosure live | M1.3 | All affiliate links disclosed; dependency-ban test keeps passing in CI |
| M3.2 Pro subscription live | M3.1, Stage 1 trigger conditions met | Free-vs-Pro ranking-consistency regression test passes; subscription, restore purchases, cancellation, and trial reminders tested end to end |
| M3.3 Order-placement pilot | M3.2, Phase 3 acceptance, user's separate approval | 10 small real orders with zero incidents; per-order confirmation page shows the service fee; any incident triggers the suspension mechanism, tested live |
| M3.4 Monthly public eval normalized | Phase 4 | Monthly reports include same-product accuracy, total-price error, merchant coverage, blocked channels, and revenue-source disclosure (disclosure wording to be confirmed); ugly numbers published as they are |

---

## 6. Risk table (across all three periods)

| Risk | Response | Period |
|---|---|---|
| Major channels block the agent (Amazon and others unfriendly) | Start from open channels; stop when blocked and disclose; write coverage gaps into reports | Near-term – long-term |
| Same-product misidentification (variants, refurbished, regional versions) | Identifier primary key + suspected branch + eval-set regression; §2.2 condition/bundle fields | Near-term |
| Stale prices / inaccurate shipping and tax estimates | Source + timestamp + "needs re-check" labels; estimates never pose as current prices | Near-term |
| Loyalty conflict (commissions, ads, paid merchants) | §2.4 code isolation + §5.4 disclosure + §5.5 rejection list | Throughout |
| App review rejection | §4.3 item-by-item self-check; feature disclosure consistent with the binary; no hidden switches | Mid-term |
| Subscription rule changes (Apple, payment channels) | Follow the rules at submission and launch time; comply first when rules change, never race ahead | Mid-term – long-term |
| Runaway order placement | Constraints file + per-order confirmation + payment isolation + auditability + incident suspension | Long-term |
| Cost overrun (hosting, push, email beyond free tiers) | Start on free tiers, review usage monthly, decide only after exceeding a tier (§3.4) | Near-term – long-term |

## 7. Open items (deliberately left unfilled in this file)

- [ ] Domain and static-hosting provider choice, one of three (§3.4)
- [ ] Per-channel refresh frequencies and failure thresholds (§3.3)
- [ ] Apple Developer account ownership and annual-fee bearer (§4)
- [ ] App privacy-label wording: whether search/scan records are uploaded (§4.3; recommended default: not uploaded)
- [ ] Stage 0 → Stage 1 usage thresholds and measurement period (§5.1)
- [ ] Pro subscription tiers, trial period, free-tier tracking cap (§5.2)
- [ ] Order-placement service-fee structure (flat fee or capped percentage fee) (§5.3)
- [ ] Legal review channel for disclosure copy (§5.4)
- [ ] Affiliate program partners and terms (§5.1)
- [ ] API v1/v2 parallel-run length (§4.2)

## 8. Document relationships

- `README.md`: vision and five principles (unchanged).
- `PLAN.md`: build phases and acceptance criteria (Phase 0–4).
- `ARCHITECTURE.md`: modules, data model, ranking formula — once the §2 decisions land,
  the `Offer` new-field and API contract sections should be backfilled.
- `DECISIONS.md`: if this file ever drives a decision change (e.g. a new revenue model), append
  records per the rule "new decisions appended, old decisions never quietly changed".
- `BUILD_LOG.md`: one entry per milestone completed (M1.x / M2.x / M3.x), recording ugly
  numbers truthfully.
- This file (`ROADMAP.md`): product and business timeline; time estimates in "months",
  no specific dates promised; a stage begins only after the previous milestone's acceptance passes.
