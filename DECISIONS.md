# Decision Log

One line per key trade-off: what was decided, why, and why the alternative was not chosen.
New decisions are appended at the top; old decisions are never quietly changed — a change is
written as "superseded by" with the original text kept.

## 001 (2026-10-31): Serve the buyer only; ranking is decoupled from revenue

- Decision: Ranking factors contain buyer interests only (total price, delivery, reputation);
  affiliate commissions and ad revenue are disclosed truthfully and never enter ranking.
- Why: The core of Collison's post is "which side the agent is on". Once ranking can be
  influenced by payment, this project turns from a buyer tool into just another ad slot.
- Alternative (not chosen): A composite value score — opaque, unauditable by users. Rejected.

## 002 (2026-10-31): The same-product key is the identifier, not title similarity

- Decision: Only matching UPC / EAN / MPN / official SKU counts as the same product;
  similar titles go to the "suspected same product" appendix table.
- Why: Title similarity will inevitably fail on variants, refurbished units, and regional
  versions; one failure can make someone buy the wrong thing.
- Alternative (not chosen): Pure title / image matching — high recall but uncontrollable
  precision. Rejected.

## 003 (2026-10-31): Compare first, do not order yet; ordering needs a separate approval round

- Decision: Phases 1–2 compare prices and send alerts only; Phase 3 ordering requires a
  separate approval, with the constraints file written first.
- Why: Spending money is irreversible; get comparison right and earn trust first, then
  talk about ordering.
- Alternative (not chosen): Building ordering from day one — too much risk and compliance
  cost. Rejected.

## 004 (2026-10-31): Data sources follow the tier "official API > catalog > structured data > browser verification"

- Decision: A channel that is blocked or prohibited by ToS stops there — no bypassing
  verification, no fake identity.
- Why: Adversarial scraping would kill the project on legal and ban risk; an open-source
  project must above all withstand scrutiny.
- Alternative (not chosen): Scraping everything — higher short-term coverage, unsustainable
  long-term. Rejected.

## 005 (2026-10-31): Default market is the United States; first category is standardized electronics models

- Decision: Shipping, tax, and merchant lists follow US conventions first; the first category
  is model-based products whose identifiers are easiest to align.
- Why: A narrower scope is the only way to get same-product accuracy up; spread too thin and
  the first version compares nothing accurately.
- Status: Pending user confirmation — changing market or category takes one sentence.
- 2026-10-31 note: The user said "start" without changing the defaults, so Phase 1 has
  proceeded on these defaults (US market, standardized electronics models).

## 006 (2026-10-31): Phase 1 covers currently-selling mainstream new products only; no secondhand tracking for now

- Decision: The Phase 1 eval set is limited to mainstream new products
  currently on sale. Used, refurbished, and open-box markets are
  explicitly out of scope for Phase 1; they may be revisited later as
  a separate decision, not silently added.
- Why: Secondhand pricing is far more complex (condition grading,
  seller variance, no stable SKU identity), and mixing it into new-unit
  rankings would corrupt the "same product" guarantee before it is proven.
- Consequence: Entries that stop being sold new at major retailers
  (e.g. MacBook Air 13 M4, confirmed discontinued-new at Best Buy and
  B&H on 2026-10-31) are flagged for review against this criterion;
  whether they are replaced by current-generation successors is a
  separate user decision, not an automatic substitution.

## 007 (2026-10-31): Repository language is English only; market is the United States

- Decision: All repository content (docs, code comments, CLI output,
  snapshot metadata) is written in English, targeting US consumers.
  This confirms and closes the open item in decision 005: the market
  is the United States and the language is English.
- Why: The product and its future service target US consumers; a
  single-language public repository avoids mixed-language drift and
  keeps every claim auditable by its audience.
- Consequence: Existing Chinese text in docs and code is translated
  to English in one pass; new content must be written in English.

## 008 (2026-10-31): Discontinued Apple entries are replaced by current-generation successors, user-confirmed

- Decision: The open item left by decision 006 is closed: discontinued
  Apple entries are replaced by their current-generation successors
  (9 replaced, 3 kept; see BUILD_LOG 011 for the full list), rather than
  tracked as clearance items.
- Why: The eval set's purpose is comparing what a buyer can buy new
  today; carrying retired generations would measure clearance pricing,
  not the mainstream new-unit market the project claims to cover.
- Nuance, user-confirmed: the MacBook Pro 14 M6 base (MHWT4LL/A) counts
  as the current model even though it is pre-order until its 2026-11-06
  release, because the M5 base it replaces is already discontinued; its
  entry stays pending (no UPC yet) and cannot enter the matched ranking
  until a retailer listing states the UPC.

## 009 (2026-10-31): Discontinued Galaxy Buds2 Pro replaced by Galaxy Buds4 Pro White, user-confirmed

- Decision: The Galaxy Buds2 Pro entry (samsung-buds2-pro-white) is retired
  and replaced by Galaxy Buds4 Pro White, US version (SM-R640NZWAXAR),
  under the new key samsung-buds4-pro-white. The old key is retired, never
  reused, and no Buds2 Pro quote is carried over.
- Why: The Buds2 Pro US white model is discontinued as new (B&H: "no
  longer available"; no current US listing found 2026-10-31). The user
  chose Buds4 Pro over Buds3 Pro and over dropping the entry. Buds4 Pro
  (released 2026-03-11, MSRP $249.99) is the current generation.
- Identifier: UPC 198957273582 for SM-R640NZWAXAR, agreed by Best Buy
  spec, a distributor catalog (GTIN 0198957273582), and T-Mobile's URL
  sku. The Amazon SM-R640NZWFXAR / 198957273568 listing is a different
  variant and was excluded, as were MEA and Latino Americana suffixes.

## 010 (2026-10-31): Superlight 2 US identifier corrected from 910-006630 to 910-006628

- Correction, not a new model: the eval entry for the G Pro X Superlight 2
  Black changes MPN from 910-006630 to 910-006628 and identifier from EAN
  5099206104525 to UPC 097855177797. The key
  (logitech-g-pro-x-superlight-2-black) does not change, and the two
  $159.99 quotes already collected (Logitech G direct, Sweetwater) stand:
  the Logitech G direct URL already showed 910-006628, so the correction
  makes the entry agree with its own quote instead of contradicting it.
- Why: the 910-006630 pinning came from European retailer listings. Four
  further sources agree 910-006628 is the North American black unit: Abt
  (US) lists Model 910-006628 with UPC 097855177797 and Color Black;
  DirectDial agrees on MFG part and UPC (0097855177797, the same code in
  GTIN-13 form); Best Buy Canada lists Model 910-006628, Black; the
  Logitech G US store URL carries 910-006628. The old 910-006630 / EAN
  5099206104525 reference is recorded here as superseded, not erased:
  it remains a valid European reference for the same mouse.
- Rule applied: an eval set for the US market pins the US identifier;
  a regional identifier is not silently kept once US sources disagree.

## 011 (2026-10-31): Electronics selection references brands' official current-sale catalogs; old-model and secondhand hunting deferred

- Decision: for electronics, the main product selection is built from
  each brand's official current-sale catalog. Hunting old models and
  secondhand units is a later-phase goal, not current work.
- Why: the official catalog is ground truth for what is actually
  current, and it is the most efficient source — the 737, Buds2 Pro,
  and M4-Apple rounds all burned effort on models that had already
  left the official catalog. Old-model and secondhand sourcing needs
  different machinery (marketplace condition grading, regional
  variants, refurbished-vs-new disambiguation) and belongs in its own
  phase, not mixed into the in-sale-new comparison.
- Scope: this confirms and extends DECISIONS 006 (in-sale new only,
  no secondhand/refurbished). It also retroactively justifies
  excluding the 736 Nano II 100W as a 737 successor: it is the 737's
  own generation (2022), not a current-catalog model. Current
  entries that remain in a brand's official catalog (e.g. DualSense
  White, still sold by PlayStation Direct) are unaffected.

## 012 (2026-10-31): Anker 737 replaced by Anker Prime Charger 100W, user-confirmed

- Decision: the Anker 737 entry (anker-737-120w) is retired and replaced
  by the Anker Prime Charger 100W, 3-port (A2688), under the new key
  anker-prime-100w. The old key is retired, never reused, and no 737
  quote is carried over (there was none to carry: the entry held
  0 qualifying quotes).
- Why: the 737 has no qualifying US new-unit offer as of 2026-10-31
  (BUILD_LOG 016: Ayoub Lebanon/A2148311 and Newegg marketplace
  TECHVAULT rows both excluded on browser verification; ShopAbunda
  out of stock). The user chose replacement over keeping the gap or
  dropping the entry, then chose the Prime 100W over the 140W 4-port.
- Why Prime 100W: it is the like-for-like current-catalog successor —
  same 3-port travel-charger role (2 USB-C + 1 USB-A), GaN, foldable
  plug — from Anker's current official catalog, consistent with
  DECISIONS 011. The 140W 4-port (A2697) was the step-up alternative;
  its UPC was not yet pinned to a single code (two codes on the main
  ASIN), and the 736 Nano II 100W (A2145) was rejected as the 737's
  own generation, not a current model.
- Identifier: UPC 194644040635 for A2688, agreed by Ubuy, Desertcart
  (multiple regions), and CamelCamelCamel (ASIN B0CZ6LXL8R, Model
  A2688); Anker US official spec confirms Model A2688, 100W,
  2 USB-C + 1 USB-A. A2688341 (UPC 194644041021) is a different
  variant and was excluded; B&H US listing code A2688J41.

## 013 (2026-10-31): Complete the eval set brand by brand from official catalogs, Apple first

- Decision: the eval set is completed one brand at a time, each brand
  checked against its own official current-sale catalog, starting
  with Apple. Proceed gradually; do not try to sweep every brand at
  once.
- Why Apple first: it is the largest cluster in the set (12 of 28
  models) and the fastest-churning (M-series generations), so a
  catalog check there pays the most. Apple's US catalog is also the
  cleanest single source (one store, explicit part numbers, no
  marketplace noise), making it the most efficient first sweep. It
  also folds in the pending MacBook Pro 14 M6 UPC check (launch
  2026-11-06, re-check already scheduled 2026-11-07).
- Method per brand: (1) verify existing entries are still current
  (currency, identifiers, quotes); (2) list current-catalog lines
  NOT in the eval set as candidates — additions need user approval,
  never auto-add, so the set does not balloon; (3) retire entries
  that left the official catalog only with user confirmation (the
  DECISIONS 006 / 009 / 012 pattern); (4) record everything in
  DECISIONS, BUILD_LOG, and CHANGELOG.
- Guardrails: iPhones stay excluded (DECISIONS 006) unless the user
  revisits that scope; no old-model or secondhand hunting inside
  this sweep (DECISIONS 011 — that is a later phase).

## 014 (2026-10-31): AirPods 4 replaced by AirPods 5 (USB-C case), user-confirmed

- Decision: the AirPods 4 entry (apple-airpods-4-usbc) is retired and
  replaced by AirPods 5 with the USB-C charging case, under the new
  key apple-airpods-5-usbc. The old key is retired, never reused,
  and no AirPods 4 quote is carried over.
- Why: the 2026-10-31 apple.com sweep (BUILD_LOG 020) found AirPods
  4 no longer available on apple.com — its buy page redirects to
  AirPods 5 and its product page states it is no longer available.
  The user chose replacement over keeping the gap or dropping the
  entry.
- Why the USB-C case, not the wireless case: the old entry was the
  base USB-C-case model, and the $129 USB-C-case AirPods 5 is its
  like-for-like successor. The wireless charging case (MKFT4LL/A,
  $149) is the step-up variant and was excluded, as was the AU
  variant MKFT4X/A.
- Identifier: UPC 195951378978 for MKFW4LL/A, agreed by B&H Photo
  spec and eBay US product identifiers (GTIN 0195951378978, the
  same code). Best Buy US confirms Model MKFW4LL/A, SKU 6376553,
  $129.

## 015 (2026-10-31): Pin one retailer-sold configuration per model; never track brand-direct-only configurations

- Decision: when a model ships in multiple configurations, pin exactly
  one — the configuration that major US retailers sell. Do not track
  all configurations, and never pin a configuration that only the
  brand itself sells.
- Why: comparison needs at least two independent sellers. A
  configuration sold only by the brand (for example an Apple
  configure-to-order config that exists only on apple.com, such as
  the Mac Studio example) has a single price, so there is nothing to
  compare — tracking it is price monitoring, not price comparison,
  and it dilutes the eval set with uncomparable rows.
- Scope: this governs every new entry and every candidate (if Mac
  Studio is added later, pin its base retailer-sold config, never a
  CTO-only config). Audit 2026-10-31: the existing set already
  complies — all 28 pinned configurations hold retailer quotes and
  no entry's identifiers rest on apple.com alone — so no existing
  entry changes. Corollary: if a pinned configuration later becomes
  brand-direct-only (retailers drop it), that triggers a re-pin or
  retirement decision, on the same pattern as discontinuation.

## 016 (2026-10-31): Close existing categories first; new categories are a later phase

- Decision: new product categories (TVs, home theater, cameras,
  lenses, and the like) are deferred to the category-expansion
  phase. Current work closes out the categories already in the
  eval set: same-family candidates for brands already present,
  decided batch by batch.
- Why: opening new categories mid-Phase-1 would keep Phase 1 from
  ever closing, and each new category carries its own
  configuration traps (camera body-only vs kit, TV size variants)
  that deserve their own pinning rules, not a sweep-by-sweep
  add-on. TVs and cameras are good comparison categories in
  principle (strong US retailer coverage), which is why they are
  deferred, not rejected.
- Scope: this explicitly leaves Sony's TV, home-theater, camera,
  and lens families out of the Sony sweep's candidacy (BUILD_LOG
  022 covered audio + PlayStation only). It does not remove any
  existing entry or candidate.

## 017 (2026-11-01): MX Master 3S replaced by MX Master 4 (Graphite), user-confirmed

- Decision: the MX Master 3S entry (logitech-mx-master-3s-graphite)
  is retired and replaced by the MX Master 4, Graphite standard
  edition, under the new key logitech-mx-master-4-graphite. The old
  key is retired, never reused, and no 3S quote is carried over.
- Why: the 2026-10-31 Logitech sweep (BUILD_LOG 024) found no plain
  consumer MX Master 3S in the 65-product Mice catalog; the line's
  current flagship is MX Master 4. The user chose replacement with
  Master 4 over the 3S Bluetooth Edition, keeping the gap, or
  dropping the entry.
- Why Master 4 over the 3S Bluetooth Edition: the Bluetooth Edition
  (910-007499) is a variant of the previous generation, not the
  current-catalog flagship; picking it would keep an old-generation
  model as the entry, against the current-catalog principle
  (DECISIONS 008 / 011 / 012 / 014). The for Business variant is a
  business-channel listing, outside the mainstream consumer scope.
- Identifier: UPC 097855207623 for 910-007558, agreed by
  CamelCamelCamel (ASIN B0FC5SJNQX, Model 910-007558) and WantItAll
  spec (ItemPartNumber 910-007558, Graphite). Part map confirmed:
  Graphite 910-007558, Pale Gray 910-007559, Black 910-007560;
  Logitech US direct URL pins Graphite to 910-007558. 910-007562
  and 910-007565 are different codes and were excluded.

## 018 (2026-11-01): Amazon access strategy — legitimate channels only, Amazon layer in Phase 2, ranking identical across tiers

- Amazon's Conditions of Use wall is treated as a permanent
  property of the retailer, not a temporary scrape failure. Direct
  self-operated scraping that defeats the wall (rotating proxies,
  headless browsers, session spoofing) is REJECTED under the
  compliance red line (DECISIONS 004).
- Legitimate routes, in order: (a) Amazon's own affiliate API —
  PA-API 5.0 reportedly deprecated 2026-04-30 in favor of the
  Creators API, with access gated by a rolling referred-sales
  threshold (third-party reports cite 10 qualifying sales in the
  trailing 30 days; verify against Associates Central before
  building); (b) licensed data providers — Keepa API (token-metered,
  from ~EUR 49/month; price history + Buy Box depth) and Rainforest
  API (credit-based, from $23/month; real-time current prices);
  (c) user-side reads as a verification fallback, never as the
  ranking's source of truth. Phase 1 interim pattern: retailer
  corroboration (Kindle pattern), honestly labeled.
- Tier principle: the ranking is IDENTICAL across tiers. Amazon
  rows are NOT Pro-only — a Pro-only Amazon row would make the
  free ranking misleading by design and break the ranking-parity
  rule. Pro pays for depth, freshness, and tools (live refresh,
  full Amazon price history, coupon/deal detection, unlimited
  alerts), never for a different answer. Full design in
  AMAZON_STRATEGY.md.
- Sequencing: Phase 1 stays Amazon-free; Phase 2 (with the website)
  joins Associates, builds referral traffic toward API eligibility,
  and trials Keepa vs Rainforest on the catalog. No Amazon spend
  is approved by this decision.

## 019 (2026-11-01): K8 Pro replaced by K8 Ultra 8K (Black, Apex Red), user-confirmed

- Decision: the K8 Pro entry (keychron-k8-pro) is retired and
  replaced by the K8 Ultra 8K under the new key
  keychron-k8-ultra-8k. The old key is retired, never reused, and
  the old $49.99 quote is NOT carried over (different product).
- Why: the 2026-10-31 small-brands sweep (BUILD_LOG 025) found the
  K8 Pro listed on keychron.com but sold out (0 stock), with the
  page pointing to K8 HE and K8 Ultra 8K as successors. The user
  chose the Ultra 8K over the K8 HE and over keeping the sold-out
  entry.
- Why Ultra 8K over K8 HE: the Ultra 8K is the direct 8K-polling
  successor line named on the K8 Pro page, at the same $119.99
  price point as the K8 HE's successor positioning; the user
  chose it. (No technical claim is made for one over the other
  beyond the page's successor pointer and the user's choice.)
- Identifier: SKU K8U-J1 from Keychron's official product page
  (page's default variant). The entry pins the Apex Red variant,
  mirroring the old entry's Red pinning; Brown and Banana share
  the $119.99 price on the same page. Per-variant barcodes are
  pending verification via Keychron's public product JSON (the
  K8 Pro precedent); old-K8 barcodes (753610396260, 617748997846)
  belong to the original K8 and were excluded.

## 020 (2026-11-01): Selection methodology — deal sites are NOT the selection source; brand catalogs stay the backbone, demand signals prioritize

- Decision: deal-aggregation sites (DealMoon and equivalents) are
  NOT adopted as the selection source for non-Apple brands. The
  selection backbone stays the brand official catalog
  (DECISIONS 011): it is the only stable, verifiable,
  non-commercial source of "what is currently sold".
- Why DealMoon fails as a selector, in three parts:
  (a) Audience skew: DealMoon is a Chinese-language deals site
  for Chinese consumers in North America. Its attention map
  reflects that audience (deal-sensitive categories, diaspora
  shopping patterns), not the US mainstream market this project
  serves in English. Seeding selection from it would import a
  catalog whose demand story does not match the stated market.
  (b) Deal-ephemerality: deal sites show temporary price drops,
  coupons, and promos, not the stable catalog. A product appears
  because it is discounted today and vanishes tomorrow; products
  that rarely discount would never appear even if they are top
  sellers. Selection built on deal posts inherits churn and
  promo-bias.
  (c) Commercial bias: deal posts partly reflect affiliate and
  merchant relationships. Importing selection from a
  commission-driven source conflicts with the buyer-side,
  commission-blind principle (DECISIONS 001).
- The real bottleneck is not discovery but prioritization: brand
  catalogs already give the full list (65 mice, 339 keyboards);
  the question is which items to track first. That is solved by
  demand signals, in priority order:
  (1) Retailer bestseller lists (public best-seller pages) and
  review volume on retailer pages — the closest public proxy for
  installed base and mainstream demand.
  (2) Search demand (trends, keyword volume) for category
  prioritization.
  (3) Deal sites as a SECONDARY signal only: repeated appearance
  over time (not single posts) marks a product as a gap-check
  candidate (user-approved per DECISIONS 013) and, in Phase 2,
  as an alert-priority input. For US-mainstream deal-heat,
  Slickdeals is a better proxy than DealMoon; DealMoon becomes
  relevant only if the project ever targets Chinese-American
  shoppers or a Chinese-language version — a segment decision,
  not a Phase 1 selection rule.
- The user's underlying point is kept: selection does need a
  demand filter ("pre-screened for attention and traffic"), and
  that filter is adopted — but as prioritization over the brand
  catalog, not as replacement of it.

## 021 (2026-11-06): Quote eligibility — no third-party sellers, no non-US-market goods; selection stays mainstream-or-new

- Decision (user, 2026-11-06): three rules, effective immediately for
  all snapshots and browser rechecks.
  (a) Third-party sellers: NOT touched for now. A quote only counts
  when the seller is the merchant itself (first-party sale: brand
  direct, or a named retailer selling directly). Marketplace /
  third-party seller rows are excluded from snapshots entirely —
  not flagged, excluded — even when cheaper. Rationale: today's
  Newegg $117 case (BUILD_LOG 036) — the price looked like a deal
  but was Astonlink shipping from China, 2-week delivery,
  quantity 1; a buyer-side ranking that surfaces it as
  "Newegg $117" misleads the buyer. Earlier precedent: the
  TECHVAULT third-party Anker row, excluded on five independent
  grounds (2026-10-31).
  (b) Non-US-market goods: NOT touched. Only US-market versions
  count — US MPN/UPC, sold by US retailers / US stores.
  Excluded: parallel imports, international variants (non-US
  ASINs, MEA/LatAm suffixes, overseas sellers, non-US listings).
  This formalizes what prior rounds already practiced (e.g.
  Ayoub Lebanon, iCuracao, Australian ASIN rows excluded).
  (c) Selection: each brand's mainstream or new products first;
  expand gradually later. Phase 1 keeps tracking the current 28
  (each brand's core/bestseller lineup or new release); no
  long-tail, niche, or legacy models added now. Expansion stays
  batch-by-batch with user approval (DECISIONS 013); candidate
  lists stay list-only.
- What changes in practice: the 2026-11-06 snapshot's Newegg $117
  Astonlink row is excluded from future snapshots (it was already
  marked not-confirmed in BUILD_LOG 036; from the next daily run
  it is out of the feed-derived quote set, not carried as a
  quote). No catalog entry changes: no current eval model is
  itself a third-party or non-US product — the rule bites on
  quote eligibility only.
- What does NOT change: DECISIONS 011/013/020 stand; this narrows
  quote eligibility and selection pace, it does not replace the
  brand-catalog backbone or the demand-prioritization layer.
- Revisit: when the user says expand, third-party sellers and
  non-US goods are separate expansion decisions, each needing its
  own user approval; do not bundle them into a general "expand"
  step.

## 022 (2026-11-06): Expansion batch 1 — eval set 28 → 33, one model per brand

- Decision (user, 2026-11-06, "按这 5 款加"): add the first expansion
  batch, five models, each brand's current mainstream/new product,
  drawn from the brand-catalog candidate lists (BUILD_LOG 020/022/
  023/024/025). No other model is added; the remaining candidates stay
  list-only for later batches, each needing its own user approval
  (DECISIONS 013/021).
  (a) Nintendo Switch 2, base system only — `nintendo-switch-2`,
  pinned variant base system 256GB (BEE-001). The $549.99 Mario Kart
  bundle and $529.99 Sports bundle are different SKUs, excluded.
  (b) Sony WH-1000XM6, Black — `sony-wh1000xm6-black`, pinned
  variant Black (WH1000XM6/B). Bare unit only; accessory bundles
  excluded.
  (c) Apple Watch Series 12, GPS 42mm — `apple-watch-series-12-42mm-
  gps-black`, pinned variant GPS 42mm Black Aluminum, Black Sport
  Band S/M (MJEA4LS/A). The entry-price GPS configuration (from
  $399); GPS + Cellular and 46mm are different SKUs.
  (d) Logitech MX Anywhere 3S, Graphite — `logitech-mx-anywhere-3s-
  graphite`, pinned variant Graphite, standard edition
  (910-006928). The current compact flagship mouse; for-Mac and
  for-Business are different products.
  (e) Samsung Galaxy Buds4, Black — `samsung-buds4-black`, pinned
  variant Black (SM-R540NZKAXAR). White is a different SKU;
  Buds4 Pro is a different model.
- Identifier outcome: 4 of 5 verified (Switch 2, XM6, Anywhere 3S,
  Buds4), 1 pending (Watch Series 12 — US UPC not yet found; MPN
  MJEA4LS/A is confirmed but identifiers stay empty per the MacBook
  Pro 14 M6 precedent, DECISIONS 008/BUILD_LOG 035). Eval set is now
  33 models, 30 verified identifiers, 3 pending (DualSense White,
  MacBook Pro 14 M6, Watch Series 12). `tests/test_snapshot_eval.py`
  counts updated 28 → 33 / 26 → 30 to match; this is a coverage
  change, not a loosened assertion.
- Regional-code traps avoided, same discipline as the Kindle pin:
  Anywhere 3S US Graphite is 910-006928 / UPC 097855184030
  (Logitech spec sheet + B&H + Staples); the NZ graphite
  910-006932 / UPC 097855184047 is a different regional SKU and was
  NOT used. Watch Series 12 NZ MJEA4X/A UPC 195951225470 and UK EAN
  195951225395 are regional; neither was used. XM6 carries one
  conflicting code, 094148746326, from the Sony manual hosted on
  manuals.plus (single source); the retailer-agreed 027242930698
  was used instead.
- Correction to BUILD_LOG 024: the $69.99 Anywhere 3S candidate price
  was the Pale Grey sale price (Newegg), not Graphite. Graphite
  street price is $89.99 (B&H, Sweetwater, Lenovo, 2026-11-06).
- What changes in practice: new snapshot
  `data/eval_snapshots_batch1_2026-11-06.json` holds 16 quotes
  across the 5 models (Switch 2: 5, XM6: 3, Watch 12: 2, Anywhere
  3S: 3, Buds4: 3). DECISIONS 021 applied to every quote: no
  marketplace/third-party rows, no non-US rows, no Amazon.
- What does NOT change: the existing 28 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense identifiers
  untouched, MacBook Pro 14 M6 untouched). No other snapshot file
  is rewritten. No Amazon touch.
- Revisit: batch 2 candidates stay list-only until the user approves
  the next batch; the daily refresh cron still says "28 models" in
  its body and needs a count update to 33 on the next edit.

## 024 (2026-11-06): Expansion batch 3 — eval set 38 → 42, one model per brand

- Decision (user, 2026-11-06, "按这 5 款加"): add the third expansion
  batch, each brand's current mainstream/new product, drawn from the
  brand-catalog candidate lists (BUILD_LOG 020/022/023/024/025). One
  of the five was already in the set, so the batch adds FOUR new
  models, 38 → 42 — no duplicate key was created (see (e)).
  (a) Sony PlayStation 5 Pro, 2TB — `sony-ps5-pro`, pinned variant
  2TB, White, all-digital (1000046529 / CFI-7019B01X). Bare console
  only; the disc drive is sold separately. UPC 711719595946
  verified (Best Buy + Amazon US + Desertcart + SeekMonkey agree);
  the unverified guess 711719581124 was NOT used. PlayStation's
  current PDP lists model CFI-7021 and Best Buy's current listing
  shows 1000046529/1000050805 — the UPC is verified for the launch
  revision; a separate CFI-7021 UPC was not found and is flagged
  in the entry notes, not assumed.
  (b) Nintendo Switch - OLED Model, Neon Blue/Neon Red set —
  `nintendo-switch-oled-neon`, pinned variant Neon set (HEGSKABAA;
  SKU 115464). The White set is already in the set and is a
  different SKU; Splatoon 3, Mario Red and Zelda editions are
  different SKUs.
  (c) Logitech Lift, Graphite — `logitech-lift-graphite`, pinned
  variant Graphite, standard right-handed (910-006466). The
  left-handed Lift, for-Business and for-Mac are different SKUs;
  Rose and Off-White are different colors.
  (d) Meta Quest 3, 512GB — `meta-quest-3-512gb`, pinned variant
  512GB (899-00583-01). The 128GB Quest 3 was phased out in 2024,
  so 512GB is the only current Quest 3 storage tier; Quest 3S is
  a different model and is already in the set. Amazon's "Model
  Number 899-00585-01" is a different code (bundle/box) and was
  NOT used.
  (e) Apple AirPods 5 — NOT added: already in the set since
  2026-10-31 as `apple-airpods-5-usbc`, USB-C case (MKFW4LL/A),
  UPC 195951378978, verified. DECISIONS 015 (one configuration
  per model) forbids adding the $149 wireless-charging-case
  variant (MKFT4LL/A) as a second entry. The batch was approved
  as five and delivered as four new models plus one
  already-present; nothing was forced in to make it five.
- What changes in practice: new snapshot
  `data/eval_snapshots_batch3_2026-11-06.json` holds 13 quotes
  across the 4 models (PS5 Pro: 4, OLED Neon: 2, Lift: 3,
  Quest 3: 4). DECISIONS 021 applied to every quote: no
  marketplace/third-party rows, no non-US rows, no Amazon. One
  direct price is price-only (stock not confirmed): PlayStation
  Direct PS5 Pro $899.00 — the console is broadly out of stock in
  the US since mid-September 2026 (Best Buy sold out, GameStop
  new unavailable, 2026-11-06). Eval: 42 models, 38 verified
  identifiers, 13 quotes, 0 identifier-matched, 13 suspected.
- What does NOT change: the existing 38 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense identifiers
  untouched, MacBook Pro 14 M6 untouched, batch 1 and 2 entries
  untouched). No other snapshot file is rewritten. No Amazon
  touch. The daily refresh cron still says "38 models" in its
  body and needs a count update to 42 on the next edit (parent
  owns the cron; not touched here).
- Revisit: PS5 Pro CFI-7021 revision UPC (if it differs from the
  launch revision's 711719595946); Watch Ultra 4 UPC still needs
  a second independent US source.

## 023 (2026-11-06): Expansion batch 2 — eval set 33 → 38, one model per brand

- Decision (user, 2026-11-06, "按这 5 款加"): add the second expansion
  batch, five models, each brand's current mainstream/new product,
  drawn from the brand-catalog candidate lists (BUILD_LOG 020/022/
  023/024/025). No other model is added; the remaining candidates stay
  list-only for later batches, each needing its own user approval
  (DECISIONS 013/021).
  (a) Sony WF-1000XM6, Black — `sony-wf1000xm6-black`, pinned
  variant Black (WF1000XM6/B). Bare unit only; care-program and
  accessory bundles excluded; Platinum Silver is a different SKU.
  (b) Apple Watch Ultra 4, GPS + Cellular 49mm — `apple-watch-ultra-
  4-49mm-gps-cellular-natural`, pinned variant GPS + Cellular 49mm
  Natural Titanium, Sand Trail Loop M/L (MJAQ4LS/A). There is no
  GPS-only Ultra 4 tier; Black Titanium, Desert Alpine Loop
  (MJAE4LS/A), Milanese Loop and Ocean Band are different SKUs.
  (c) Nintendo Switch 2 Pro Controller — `nintendo-switch-2-pro-
  controller`, pinned variant Black, standard edition (BEE-008).
  The Zelda 40th Anniversary and Resident Evil Requiem editions
  are different SKUs.
  (d) Logitech MX Keys Mini, Black — `logitech-mx-keys-mini-black`,
  pinned variant Black, standard edition (920-010475). Graphite
  (920-010388) is a different SKU; for-Mac and for-Business are
  different products; Pale Grey and Rose are different colors.
  (e) Samsung Galaxy Buds3 FE, Black — `samsung-buds3-fe-black`,
  pinned variant Black (SM-R420NZKAXAR). Gray (SM-R420NZAAXAR)
  is a different SKU; the older Galaxy Buds FE is a different
  model.
- Identifier outcome: 4 of 5 verified (WF-1000XM6, Switch 2 Pro
  Controller, MX Keys Mini, Buds3 FE), 1 pending (Watch Ultra 4 —
  the only US UPC found, 195951394480 for Natural M/L Sand Trail
  Loop, appears in a single source (Adorama's spec table); MPN
  MJAQ4LS/A is confirmed but identifiers stay empty per the
  MacBook Pro 14 M6 precedent, DECISIONS 008/BUILD_LOG 035). Eval
  set is now 38 models, 34 verified identifiers, 4 pending
  (DualSense White, MacBook Pro 14 M6, Watch Series 12, Watch
  Ultra 4). `tests/test_snapshot_eval.py` counts updated 33 → 38
  / 30 → 34 to match; this is a coverage change, not a loosened
  assertion.
- Regional-code traps avoided, same discipline as the Kindle pin:
  Switch 2 Pro Controller US UPC is 045496885861 (Nintendo's own
  US store page); the Japan JAN 4902370552843 and the single
  uncorroborated eBay code 0219341384384 were NOT used. Buds3 FE
  US Black is SM-R420NZKAXAR / UPC 0198957213090; the AU
  SM-R420NZKAASA and other regional suffixes (NZKAXSE, ZNAXNU,
  NZAFXAR) were NOT used. MX Keys Mini US Black is 920-010475 /
  UPC 097855169617; Graphite 920-010388 is a different SKU, not a
  different name for the same board.
- What changes in practice: new snapshot
  `data/eval_snapshots_batch2_2026-11-06.json` holds 19 quotes
  across the 5 models (WF-1000XM6: 4, Ultra 4: 2, Pro Controller:
  5, MX Keys Mini: 3, Buds3 FE: 5). DECISIONS 021 applied to every
  quote: no marketplace/third-party rows, no non-US rows, no
  Amazon. Two direct prices are price-only (stock not confirmed
  in the page text): Sony direct WF-1000XM6 $298.00 (Sony page
  403'd on direct fetch; price from Sony's own page via search
  index) and Apple direct Ultra 4 $799.00.
- What does NOT change: the existing 33 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense identifiers
  untouched, MacBook Pro 14 M6 untouched, batch 1 entries
  untouched). No other snapshot file is rewritten. No Amazon
  touch. The daily refresh cron still says "33 models" in its
  body and needs a count update to 38 on the next edit (parent
  owns the cron; not touched here).
- Revisit: batch 3 candidates stay list-only until the user approves
  the next batch; Watch Ultra 4 UPC needs a second independent US
  source (a US retailer spec page or a physical box barcode).

## 025 (2026-11-06): Expansion batch 4 — eval set 42 → 47, one model per brand

- Decision (user, 2026-11-06, "按这 5 款加"): add the fourth expansion
  batch, each brand's current mainstream/new product, drawn from the
  brand-catalog candidate lists (BUILD_LOG 020/022/023/024/025). All
  five were verified and added, 42 → 47, verified identifiers 38 → 43.
  (a) Apple iPad mini (A20 Pro), Wi-Fi 128GB Standard Glass, Starlight
  — `apple-ipad-mini-a20-128gb-wifi-starlight`, MPN MJ6J4LL/A, UPC
  195951205595 (B&H spec page + Adorama spec table agree). Released
  2026-11-06, $699. (b) Sony PlayStation 5 Slim Digital Edition 825GB,
  White — `sony-ps5-digital-825gb`, MPN CFI-2015, UPC 711719541035
  (PayMore US spec table + eBay GTIN agree). $599.99. (c) Nintendo
  Joy-Con 2 (L)/(R) Light Blue / Light Red pair —
  `nintendo-joy-con-2-pair-light-blue-light-red`, MPN BEEAJAAAA, UPC
  045496885892 (Nintendo US official page + Snapklik agree). $99.99.
  (d) Logitech G502 X PLUS Black, HERO 25K —
  `logitech-g502-x-plus-black`, MPN 910-006160, UPC 097855166951
  (ErgoDirect + Desertcart + Amazon US + DirectDial + eBay agree).
  $159.99. (e) Google Pixel Buds 2a, Hazel —
  `google-pixel-buds-2a-hazel`, MPN GA06155-US, UPC 840353930506
  (eBay product catalog + Poshmark US seller + Snapklik/ImportItAll/
  WantItAll agree; OnBuy UK's conflicting 840353930520 not used).
  $129.
- Membership check (skill, re-done by the batch worker, BUILD_LOG 041):
  the 42-model key list was read before adding anything; none of the
  five candidates matched an existing model by name, MPN, or UPC
  (no ipad-mini, ps5-digital, joy-con-2, g502, or pixel-buds-2a key
  existed; the set's only Pixel Buds entry is Pixel Buds Pro 2
  Porcelain, a different model). No candidate was dropped.
- Variant corrections vs the 2026-10-31 candidate prices: PS5 Digital
  $599 → $599.99 (Best Buy); G502 X PLUS $149.99 → $159.99 (Logitech
  direct list, Best Buy, Adorama all $159.99 — the $149.99 was stale).
  iPad mini A20 Pro launched 2026-11-06 at $699 (Wi-Fi 128GB) as the
  candidate list anticipated. The G502 X PLUS HERO 44K refresh (fall
  2026, new colorways Black/Purple, White/Mint, Dark Lilac) was NOT
  pinned: its part numbers conflict across retailers (910-007808 on
  Logitech's US page and Best Buy's Dark Lilac listing vs 910-007812
  on PBTech NZ / Scorptec AU for Black/Purple) and no UPC was found
  for any 44K part number — the 44K UPC is an open item, and the
  HERO 25K UPC 097855166951 was NOT carried over to it. The pinned
  HERO 25K Black is still in stock at Logitech direct (list),
  Best Buy, Adorama, and Staples.
- What changes in practice: new snapshot
  `data/eval_snapshots_batch4_2026-11-06.json` holds 15 quotes
  across the 5 models (iPad mini A20: 3, PS5 Digital: 2, Joy-Con 2: 2,
  G502 X PLUS: 4, Pixel Buds 2a: 4). DECISIONS 021 applied to every
  quote: no marketplace/third-party rows, no non-US rows, no Amazon.
  Three direct prices are price-only (stock not confirmed in the page
  text): Apple direct iPad mini $699.00, Logitech direct G502 X PLUS
  $159.99 (current PDP defaults to the 44K variant), Google Store
  Pixel Buds 2a $129. Best Buy PS5 Digital stock signals were mixed
  across crawls (Add to cart + JSON-LD InStock on the direct page
  read, one earlier crawl Unavailable for shipping).
- What does NOT change: the existing 42 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense identifiers untouched,
  MacBook Pro 14 M6 untouched, batches 1–3 entries untouched). No
  other snapshot file is rewritten. No Amazon touch. The daily refresh
  cron still says "42 models" in its body and needs a count update to
  47 on the next edit (parent owns the cron; not touched here).
- Revisit: batch 5 candidates stay list-only until the user approves
  the next batch; G502 X PLUS HERO 44K UPC needs a second independent
  US source once the part-number conflict settles; PS5 Digital UPC
  rests on PayMore + eBay (Best Buy's page states no UPC) — a US
  retailer spec page would strengthen it.

## 026 (2026-11-06): Expansion batch 5 — eval set 47 → 52, one model per brand

- Decision (user, 2026-11-06, "按这 5 款加"): add the fifth expansion
  batch, each brand's current mainstream/new product, drawn from the
  brand-catalog candidate lists (BUILD_LOG 020/022/023/024/025). Four
  were verified and added, one added with identifiers pending, 47 →
  52, verified identifiers 43 → 47. (a) Apple iPad Air 13-inch (M4),
  128GB Wi-Fi, Space Gray — `apple-ipad-air-m4-13`, MPN MH5N4LL/A,
  UPC 195950797817 (Abt US + iGiftcardz agree; Best Buy US SKU
  6586913 confirms the MPN). $949. (b) Sony DualSense Edge, Black &
  White — `sony-dualsense-edge-black-white`, MPN CFI-ZCP1 confirmed,
  UPC PENDING (see below). $199.99. (c) Nintendo Joy-Con (L)/(R)
  Neon Red/Neon Blue pair — `nintendo-joy-con-pair-neon-red-neon-blue`,
  MPN HACAJAEAA, UPC 045496590130 (Nintendo US official store page,
  SKU 104882, UPC 00045496590130 + eBay + PayMore agree). $89.99.
  (d) Logitech MX Vertical, Graphite — `logitech-mx-vertical-graphite`,
  MPN 910-005447, UPC 097855144461 (Govets + Compsource + Desertcart
  GTIN + CamelCamelCamel agree). $99.99 sale (was $119.99). (e) Bose
  QuietComfort Earbuds (2024), Black — `bose-qc-earbuds-black`, MPN
  888507-0100, UPC 017817853460 (Abt US + Adorama spec table + Ubuy
  GTIN + Desertcart + eBay agree). $119.00 sale (was $179.00).
- Membership check (skill, re-done by the batch worker, BUILD_LOG 042):
  the 47-model key list was read before adding anything; none of the
  five candidates matched an existing model by name, MPN, or UPC
  (no ipad-air-13, dualsense-edge, joy-con-pair, mx-vertical, or
  qc-earbuds key existed; the set's only iPad Air is the 11-inch M4,
  the only DualSense is the standard White, the only Joy-Con is the
  Switch 2 pair, the only Logitech vertical mice are Lift, and the
  only Bose earbuds entry is QC Ultra 2). No candidate was dropped.
- DualSense Edge UPC is the batch's open item: MPN CFI-ZCP1 is
  confirmed, but three UPCs circulate for the Black & White version —
  711719444190 (Desertcart GTIN 00711719444190 + Albagame barcode +
  itworkup EAN + startech24 datasheet), 711719585552 (eBay product
  catalog, ePID 10058650690, Glacier White), 711719586555 (PBTech NZ,
  regional) — and no two independent US sources agree, so identifiers
  stay empty per the DualSense White precedent (DECISIONS 002). The
  Midnight Black variant (MPN 1000046706, UPC 711719596554) is
  consistent across Desertcart/Ubuy but both are Amazon-derived, so
  it was not pinned as a substitute. The Edge UPC needs a US retailer
  spec page or a physical box barcode.
- Variant corrections vs the 2026-10-31 candidate prices: Bose QC
  Earbuds $129 → list $179.00 (Bose direct sale $119.00 to
  2026-11-08, P.C. Richard sale $129.00); MX Vertical $99.99 is the
  current sale price, list $119.99 (Logitech direct, Staples, Dell
  all $99.99 sale / $119.99 list). iPad Air 13 $949, DualSense Edge
  $199.99, Joy-Con pair $89.99 confirmed as listed.
- What changes in practice: new snapshot
  `data/eval_snapshots_batch5_2026-11-06.json` holds 15 quotes
  across the 5 models (iPad Air 13: 2, DualSense Edge: 4, Joy-Con
  pair: 2, MX Vertical: 3, QC Earbuds: 4). DECISIONS 021 applied to
  every quote: no marketplace/third-party rows, no non-US rows, no
  Amazon. Three direct prices are price-only (stock not confirmed in
  the page text): Apple direct iPad Air 13 $949.00, Bose direct QC
  Earbuds $119.00 (sale). PlayStation Direct US Edge page not
  reached; the feed's direct.playstation.com $30 row is not a real
  price and was excluded.
- What does NOT change: the existing 47 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense identifiers untouched,
  MacBook Pro 14 M6 untouched, batches 1–4 entries untouched). No
  other snapshot file is rewritten. No Amazon touch. The daily refresh
  cron still says "47 models" in its body and needs a count update to
  52 on the next edit (parent owns the cron; not touched here).
- Revisit: the user has authorized continuous expansion to 200 models
  without per-batch approval (2026-11-06, recorded in MEMORY.md), so
  further batches proceed under the same skill + DECISIONS 021 rules
  from 52 models up; DualSense Edge UPC stays pending until a US
  retailer spec page or box barcode settles it.

## 027 (2026-11-06): Continuous expansion authorized — eval set 52 → 200, no per-batch approval

- Decision (user, 2026-11-06, "这个不需要我每5款确定一次，效率太低，
  目前就按照这个流程，一直加到200款"): expand the eval set
  continuously from 52 to 200 models without per-batch user approval.
  Batches of 5 are for documentation only. This replaces the
  batch-by-batch approval rule (DECISIONS 013) for this run.
- What stays the same: the expansion skill
  (`~/workspace/custom-skills/price_compare_expansion/SKILL.md`) and
  DECISIONS 021 apply to every batch — membership-check each batch
  against the current set by name, MPN and UPC (record in BUILD_LOG);
  pin exactly one variant per model (DECISIONS 015); verify identifiers
  from at least two independent sources where possible, else leave
  empty and mark pending — never invent an identifier, never carry one
  across variants/revisions/regions; first-party/retailer-direct
  quotes only; US-market goods only; mainstream or new products only.
  No Amazon in any way; no purchases, sign-ins, spending,
  registrations. Existing catalog entries are not modified; pending
  identifiers (DualSense White, MacBook Pro 14 M6, Watch Series 12,
  Watch Ultra 4, PS5 Pro CFI-7021) stay pending until genuinely new
  evidence appears — dead ends are not re-searched daily.
- Order of work: first exhaust the remaining candidates from the five
  brand sweeps (BUILD_LOG 020/022/023/024/025), skipping bundles,
  second colors of models already in the set, refurbished and
  discontinued lines (DECISIONS 006/015); then sweep new mainstream US
  electronics brands one at a time (Anker, JBL, Razer, Corsair, Dell,
  HP, Lenovo, ASUS, Microsoft, Garmin, and others as needed), staying
  in standardized consumer electronics. A new category (e.g. TVs,
  appliances) is opened only if the existing categories cannot reach
  200, and only with a category decision recorded in DECISIONS first.
- Reporting: progress reports after every 25 models added (75, 100,
  125, 150, 175) and at 200. Stop and report immediately (do not force
  it) if no more models meet the rules, a site blocks repeatedly, a
  rate limit hits, or tests fail and cannot be fixed cleanly. The
  daily refresh cron (10:52 PT) also edits the repo — on a push
  conflict, pull/rebase cleanly and retry once; if it still conflicts,
  stop and report rather than force-pushing.
- The daily refresh cron is parent-owned; the coordinator does not
  touch it (the parent updates its model count).

## 028 (2026-11-06): Expansion batch 6 — 52 → 57 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/023/024/025), no per-batch user approval needed
  (DECISIONS 027): iPad Pro 13-inch M5 (256GB Wi-Fi, Space Black,
  MDYJ4LL/A), PlayStation Portal Remote Player (White, 1000041319),
  Nintendo Switch Neon Blue/Neon Red set (HADSKABAA, SKU 117972),
  Logitech G Pro X Superlight 2 DEX (Black, 910-007328 — identifiers
  pending), Bose Ultra Open Earbuds 2nd Gen (Black, 897806-0010).
  One variant pinned per model (DECISIONS 015); 4 of 5 identifiers
  verified, DEX stays pending (UPC not found in any US retailer spec
  page — DualSense Edge precedent, not a reason to hold the batch).
- Why these 5: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (13-inch vs the
  11-inch Pro; Portal vs DualSense controllers; non-OLED Switch vs
  the two OLED sets; DEX ergonomic vs the symmetrical Superlight 2;
  Ultra Open vs QC Earbuds / QC Ultra 2). All five are in stock new
  in the US on 2026-11-06 (brand-direct pages or InStock JSON-LD).
- What was corrected along the way: the candidate price $1,499 for
  the iPad Pro 13 is the 256GB list price (Apple direct page-verified;
  PhoneArena's $1,299 MSRP figure is wrong/stale); the Switch Neon's
  current UPC is 045496883775 per Nintendo's own store page, not the
  older 045496882174 from the 2019 red-box listing; the Portal's US
  UPC is 711719579779, not the regional 711719580782.
- What does NOT change: the existing 52 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–5 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "52 models" in
  its body and needs a count update to 57 on the next edit (parent
  owns the cron; not touched here).
- Revisit: DEX Black UPC stays pending until a US retailer spec page
  or box barcode settles it; the Switch HADSKABAA vs HADSKABAH
  spelling variant is recorded in the entry notes.

## 029 (2026-11-06): Expansion batch 7 — 57 → 62 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/023/024/025), no per-batch user approval needed
  (DECISIONS 027): MacBook Neo 13-inch 256GB Blush (MHFH4LL/A, UPC
  pending), PlayStation 5 Slim Console 1TB disc (CFI-2100 model
  group, retail MPN 1000049888, UPC 711719021452), Nintendo Switch
  Pro Controller Black (HAC-013; retail MPN HACAFSSKA, UPC
  045496590161), Logitech MX Mechanical full-size Tactile Quiet
  Graphite (920-010547, UPC 097855174659), Xbox Elite Wireless
  Controller Series 2 Black (FST-00001, UPC 889842196344). One
  variant pinned per model (DECISIONS 015); 4 of 5 identifiers
  verified, MacBook Neo stays pending (UPC not found for the Blush
  variant in any US source — DualSense Edge / DEX precedent, not a
  reason to hold the batch).
- Why these 5: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (Neo vs MacBook Pro
  14 M6 / MacBook Air M5; disc 1TB vs the digital 825GB and the Pro;
  original Pro Controller vs the Switch 2 Pro Controller; MX
  Mechanical vs MX Keys Mini / MX Keys S; Elite Series 2 vs the
  standard Xbox Wireless Controller). All five are in stock new in
  the US on 2026-11-06 (brand-direct pages or InStock JSON-LD).
- What was corrected along the way: the PS5 disc model is NOT
  CFI-2016 — that is the EU disc code (15 = US, 16 = EU); the
  current US disc console is the CFI-2100 model group (CFI-2115 per
  JNLGame), retail MPN 1000049888, and the older CFI-2015 disc (UPC
  711719573364) is superseded. The MX Mechanical candidate price
  $149.99 was the Oct 31 LogiWork Deal Days sale price; the current
  full-size list is $179.99 (Logitech direct, Best Buy, Target all
  $179.99; Dell $169.99) and the $149.99 rows today are the Mini, a
  different model. The MX Mechanical MPN mapping is 920-010547 =
  Tactile Quiet, 920-010548 = Linear (not the other way round). The
  MacBook Neo 256GB price is $699, not EveryMac's $599 figure
  (stale/wrong against live Apple + Best Buy $699). The only Neo UPC
  found, 195950852745, is Indigo MHFF4LL/A's, not Blush MHFH4LL/A's,
  and was not copied across colors.
- What does NOT change: the existing 57 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–6 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 62 on the next edit (parent
  owns the cron; not touched here).
- Revisit: MacBook Neo Blush UPC stays pending until a US retailer
  spec page or box barcode settles it (the Indigo UPC 195950852745
  is recorded in the entry notes as a pointer, not a pin); the
  PlayStation Direct PS5 $649.00 and Microsoft direct Elite Series 2
  $167.99 prices are price-only (stock not confirmed in the page
  text); the Elite Series 2's Amazon "discontinued by manufacturer"
  flag is contradicted by live Microsoft/Target/Best Buy listings
  and is recorded, not acted on.

## 030 (2026-11-06): Expansion batch 8 — 62 → 67 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/023/024/025), no per-batch user approval needed
  (DECISIONS 027): iMac 24-inch M6 10-core Blue (MH094LL/A, UPC
  195950838091), Sony WH-1000XM4C Black (WH1000XM4C/B, UPC pending),
  Sony PULSE Elite Midnight Black (retail MPN 1000044173, UPC
  pending), Logitech ERGO K860 Graphite (920-009166, UPC
  097855151667), Keychron K8 HE Special Edition Black (K8H-F1, EAN
  4894979028990). One variant pinned per model (DECISIONS 015); 3 of
  5 identifiers verified, XM4C and PULSE Elite stay pending (UPC not
  verified from a non-Amazon US source for either — DualSense Edge /
  DEX / Neo precedent, not a reason to hold the batch).
- Why these 5: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (first iMac in the
  set; XM4C is the 2026 M4 refresh, not the XM5/XM6 flagships;
  PULSE Elite is the first PlayStation headset; K860 is the first
  split ergonomic keyboard; K8 HE is the Hall Effect line vs the K8
  Ultra 8K). All five are in stock new in the US on 2026-11-06
  (brand-direct pages or InStock JSON-LD), except the two
  price-only direct rows noted below.
- What was corrected along the way: the new iMac is M6, not M5 — it
  skips M5 entirely (announced 2026-10-27, on sale 2026-11-06);
  the K860 candidate price $119.99 was an Amazon-only sale price,
  the current first-party list is $149.99 and no Amazon price is
  used; the K8 HE candidate price $139.99 is the Special Edition
  (the Standard is $129.99 and currently out of stock at Keychron),
  and the feed's $139.99 keychron.com row is the Japan JIS Layout
  product, a different layout; the feed's B&H $159.99 K860 row is
  the K860 for Business (920-010175), not the standard 920-009166;
  the feed's Dell K860 $129.99 row is stale (page text $149.99);
  the Meta Catalog feed returned no M6 iMac rows at all, so the
  iMac quotes are page-verified. The PULSE Elite is NOT CFI-ZWH1
  (that is the PULSE 3D headset); its US retail MPN is 1000044173.
- What does NOT change: the existing 62 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–7 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 67 on the next edit (parent
  owns the cron; not touched here).
- Revisit: XM4C Black UPC stays pending until a US retailer spec page
  or box barcode settles it (the only XM4C barcode found,
  4548736181861, is the Silver EAN and must not be copied to Black;
  the original XM4 Black UPC 027242919419 belongs to WH1000XM4/B,
  not the XM4C); PULSE Elite Midnight Black UPC stays pending (the
  only UPC seen, 711719588009, appears on a single Amazon listing
  and has no second source); iMac Blue UPC 195950838091 currently
  rests on B&H alone (launch day) and should be re-confirmed on the
  next refresh; the Apple direct iMac $1,499.00 and PlayStation
  Direct PULSE Elite $149.00 prices are price-only (stock not
  confirmed in the page text); the K8 HE has a single quote
  (Keychron direct — the line is sold only through Keychron's own
  store).

## 031 (2026-11-06): Expansion batch 9 — 67 → 72 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/023/024/025), no per-batch user approval needed
  (DECISIONS 027): Mac Studio M5 Max 18-core/32-core 36GB/512GB
  Silver (MHL64LL/A, UPC 195951078564), Sony ULT WEAR Black
  (WHULT900N/B, UPC 027242928688), Sony PULSE Explore Midnight Black
  (retail MPN 1000044170, UPC pending), Logitech Wave Keys Graphite
  (920-011898, UPC pending), Bose Sport Open Earbuds Black
  (901149-0010, UPC pending). One variant pinned per model
  (DECISIONS 015); 2 of 5 identifiers verified, PULSE Explore,
  Wave Keys and Sport Open stay pending (UPC not verified from a
  non-Amazon US source for any of the three — DualSense Edge / DEX
  / Neo / PULSE Elite precedent, not a reason to hold the batch).
- Why these 5: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (first Mac Studio in
  the set, and the current M5 Max generation; ULT WEAR is Sony's
  bass-first ULT line, not a 1000X flagship; PULSE Explore is the
  first PlayStation earbuds line, the Elite's sibling; Wave Keys is
  the first wavy-keyframe ergonomic keyboard vs the K860 split
  keyboard; Sport Open is Bose's new 2026 clip-on sport line, not
  the QC Earbuds or the Ultra Open 2nd Gen). All five are in stock
  new in the US on 2026-11-06 (brand-direct pages or InStock
  JSON-LD), except the Apple direct Mac Studio price row (price-only,
  stock not stated in the page text) and the Bose direct price,
  which was not shown in the bose.com page text this batch.
- What was corrected along the way: the current Mac Studio is the
  M5 Max generation (announced 2026-08-25, available 2026-09-22),
  not the 2025 M4 Max — the M4 Max MU963LL/A launched at $1,999
  and is discontinued, and the feed's Apple row pairing MU963LL/A
  with $2,499 mixes the old MPN with the new price and was
  excluded; the ULT WEAR candidate price $249.99 is the list price,
  the current street price is $148.00 at three retailers (Black
  Friday deal, Best Buy deal ends Nov 8); the PULSE Explore
  candidate price $149 is $149.99, a sale price off the $199.99
  list; the Wave Keys candidate price $69.99 is confirmed current
  (the 2023 launch price was $59.99); the Bose Sport Open Earbuds
  are a NEW 2026 product, not the 2021 original — the 2021 Sport
  Open Earbuds 857628-0010 (UPC 017817826211) are a different
  in-ear product and were excluded. The Wave Keys 920-012059 is
  the MK670 keyboard+mouse combo, not the standalone keyboard;
  the B&H $69.99 Wave Keys row is the 2026 Sand refresh
  920-013925, a different colorway from the pinned Graphite.
  The PULSE Explore is NOT the PULSE Elite (1000044173, over-ear
  headset) and is NOT CFI-ZWH1 (the PULSE 3D headset); its
  hardware model is CFI-ZWE1.
- What does NOT change: the existing 67 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–8 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 72 on the next edit (parent
  owns the cron; not touched here).
- Revisit: PULSE Explore Midnight Black UPC stays pending until a US
  retailer spec page or box barcode settles it (the only US UPC
  seen, 711719587972, is Amazon-only; the UK/AU barcode
  711719590231 is a different regional code and must not be copied);
  Wave Keys Graphite UPC stays pending (the only UPC found,
  097855191533, is Amazon-only; the US International layout
  920-012304 is a different layout and was not added); Sport Open
  Black UPC stays pending (B&H publishes only the Eucalyptus Green
  UPC 017817865449, which must not be copied across colors); the
  Bose direct price should be re-checked on the next refresh
  (bose.com page text showed no price this batch); the ULT WEAR
  $148.00 street price is a Black Friday deal and should be
  re-checked after Nov 8.

## 032 (2026-11-06): Expansion batch 10 — 72 → 77 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/023/024/025), no per-batch user approval needed
  (DECISIONS 027): Apple Studio Display (2026) Standard glass,
  Tilt-adjustable stand (MFEX4LL/A, UPC 195950529173), Sony LinkBuds
  Fit Black (WFLS910N/B, UPC 027242929289), Sony Access Controller
  White (retail MPN 1000037579, CFI-ZAC1, UPC pending), Logitech POP
  Keys Cosmos (920-011233, UPC pending), Xbox Elite Wireless
  Controller Series 2 – Core White (4IK-00001, UPC pending). One
  variant pinned per model (DECISIONS 015); 2 of 5 identifiers
  verified, Access Controller, POP Keys and Elite Core stay pending
  (UPC not verified from a US source for any of the three —
  DualSense Edge / DEX / Neo / PULSE Elite precedent, not a reason
  to hold the batch).
- Why these 5: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (first monitor in
  the set, and the current March 2026 Studio Display generation;
  LinkBuds Fit is Sony's open-fit Air Fitting Supporters line, not
  a 1000X flagship; Access Controller is the first PlayStation
  accessibility controller; POP Keys is the typewriter-style
  emoji-key line vs the MX/Wave ergonomic keyboards; Elite Core is
  the cheaper Elite line vs the full Elite Series 2 already in the
  set). All five are in stock new in the US on 2026-11-06
  (brand-direct pages or InStock JSON-LD), except the B&H LinkBuds
  Fit (Special Order, 2-4 weeks) and the two price-only direct
  rows noted below.
- What was corrected along the way: the current Studio Display is
  the March 2026 refresh (A19 chip, Thunderbolt 5, 12MP Center
  Stage camera with Desk View), NOT the 2022 model (A13,
  Thunderbolt 3, MK0U3LL/A, UPC 0194253030447) — the base price is
  coincidentally the same $1,599, and the pinned config is the
  Standard glass tilt-stand MFEX4LL/A; the Studio Display XDR
  (mini-LED, 120Hz, from $3,299) is a separate line; the LinkBuds
  Fit candidate price $229.99 is the list price, the current street
  price is $198.00–$199.99; the Access Controller candidate price
  $89 is $89.00 direct / $89.99 list, and Best Buy's live $79.95
  offer is a marketplace seller (A2Z Games Inc) and was excluded;
  the POP Keys candidate price $99.99 is confirmed current (the
  feed's Best Buy Blast Yellow $69.99 and Heartbreaker Rose
  $117.22 rows are different colorways); the Elite Core candidate
  range $111.74–$139.99 resolves to $111.74 at Microsoft Store
  (current sale price) and $149.99 retailer list, and the $139.99
  ShopCGX feed row is titled "Series 2", not Core. The POP Keys
  920-010817 feed row is not Cosmos (Cosmos is 920-011233 per
  Dell, Colamco, BuyDig, iFixit and logitech.com); the feed's
  Apple rows pairing the Studio Display with $5,499 is the Mac
  Studio, not a display.
- What does NOT change: the existing 72 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–9 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 77 on the next edit (parent
  owns the cron; not touched here).
- Revisit: Access Controller White UPC stays pending until a US
  retailer spec page or box barcode settles it (the only barcode
  seen, 711719567929, is a UK EAN with no US source); POP Keys
  Cosmos UPC stays pending (the only UPC found, 097855179401, is
  Amazon-only; the AU Cosmos Lavender 920-011227 GTIN 097855179340
  is a different regional variant and was not copied); Elite Core
  White UPC stays pending (the only barcodes seen, AU 889842717082
  vs LV 889842717075, conflict and are both non-US); the Studio
  Display UPC 195950529173 rests on B&H (two B&H pages agree) and
  should be re-confirmed on the next refresh (iMac precedent); the
  Microsoft direct Elite Core $111.74 and PlayStation Direct Access
  $89.00 prices are price-only (stock not confirmed in the page
  text); the B&H LinkBuds Fit $198.00 is Special Order (2-4 weeks),
  not in stock; the ULT WEAR $148.00 Black Friday street price
  should be re-checked after Nov 8 (batch 9 revisit, still open).

## 034 (2026-11-06): Expansion batch 12 — 82 → 87 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/024/025), no per-batch user approval needed
  (DECISIONS 027): Apple Magic Keyboard with Touch ID and Numeric
  Keypad USB-C, US English, White Keys (MJM64LL/A, UPC pending),
  Sony WF-C710N Black (WFC710N/B, UPC 027242931770), Sony LinkBuds
  Open Black (WFL910/B, UPC 027242928695), Logitech PRO X TKL
  LIGHTSPEED GX Brown Tactile Black (920-012127, UPC pending),
  Keychron Q1 Version 2 Fully Assembled Knob, Navy Blue - B, Gateron
  G Pro Red (Q1-O1Z, EAN pending). One variant pinned per model
  (DECISIONS 015); 2 of 5 identifiers verified, 3 stay pending on
  single-source-only UPC/EAN codes (Apple page only, eBay only,
  Keychron JSON only — Adaptive Controller / DualSense precedent,
  not a reason to hold the batch).
- Why these 5: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (first Magic Keyboard
  in the set, and the distinct typing line vs the Magic Mouse and
  Magic Trackpad; C710N is Sony's everyday mid-range
  noise-cancelling earbud line, not a 1000X flagship; LinkBuds Open
  is Sony's open-ring open-ear line, not the noise-cancelling
  LinkBuds Fit; PRO X TKL is Logitech G's standard tenkeyless
  wireless gaming keyboard, not the low-profile G915 X; base Q1 is
  the original 75% full-aluminum Q-series line vs the K8 lines and
  the Q1 Pro/Max/HE/Ultra 8K successors). All five are in stock new
  in the US on 2026-11-06 (brand-direct pages or InStock JSON-LD),
  except the Lenovo PRO X TKL price-only row and the Sony direct
  WF-C710N Black price, which was not freshly confirmed at all (see
  below).
- What was corrected along the way: the Magic Keyboard candidate
  range $99–$199 spans three different models — $99 is the plain
  Magic Keyboard, $129 the Numeric-Keypad-only Lightning model; the
  pinned Touch ID + Numeric Keypad USB-C White is $179 ($199 Black
  Keys MJM74LL/A, a different colorway), and the 2026 MJM64LL/A
  supersedes the older MXK73LL/A (Adorama, on backorder to 01/2027);
  the WF-C710N candidate price $129.99 is the list price (Sony US
  store) while the current street/sale price is $98 at Best Buy,
  Abt, Crutchfield and Beach Camera; the LinkBuds Open candidate
  price $229.99 is confirmed current at Sony direct and Dell; the
  PRO X TKL candidate price $219.99 is confirmed as the current list
  (launch SRP was $199) while the Logitech G direct US price was not
  confirmed in page text; the Keychron Q1 candidate range
  $229.99–$254.99 was the Q-line range (the Q1 Max is $229.99), not
  the base Q1 — the base Q1 V2 fully assembled knob lists $189.99
  and is currently $89.99 on sale at Keychron direct.
- Variant pinning, recorded explicitly: Magic Keyboard pins the
  Touch ID + Numeric Keypad USB-C, US English, White Keys
  (MJM64LL/A) — the full-size keyboard line, not the plain or
  numeric-only models; PRO X TKL pins LIGHTSPEED, GX Brown Tactile,
  Black (920-012127) — the standard US variant, per Best Buy Model
  920-012127 / SKU 10111534 (White 920-012143 and Magenta 920-012154
  are different colorways, Linear Black 920-012122 a different
  switch); Q1 pins the page-default in-stock variant, Fully
  Assembled Knob / Navy Blue - B / Gateron G Pro Red (Q1-O1Z) — the
  Carbon Black knob Red Q1-M1Z and all Carbon Black / Silver Grey
  knob variants are out of stock in this read, while Navy Blue - B
  Red/Blue/Brown and the Barebone Knob variants are in stock.
- What does NOT change: the existing 82 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–11 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 87 on the next edit (parent
  owns the cron; not touched here).
- Revisit: Magic Keyboard UPC 195951258324 (Apple page only), PRO X
  TKL UPC 097855188984 (eBay product identifiers only) and Q1-O1Z
  EAN 4895248817345 (Keychron JSON only) stay pending until a second
  source confirms each; Sony direct WF-C710N Black price was not
  freshly confirmed (stale page at the $119.99 launch price; White
  page shows a $99.99 sale) — re-check next refresh; LinkBuds Open
  Sony direct stock is low ("Only 3 left") — re-check next refresh;
  Lenovo US PRO X TKL Black $219.99 is price-only ("Available Soon")
  — re-check stock next refresh; the Keychron Q1 $89.99 is a sale
  price (was $189.99) — re-check after the sale ends; the ULT WEAR
  $148.00 Black Friday street price should be re-checked after
  Nov 8 (batch 9 revisit, still open); the Sony direct CH720N
  $89.99 is a sale price and should be re-checked after the sale
  ends.

## 035 (2026-11-06): Expansion batch 13 — 87 → 92 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/024/025), no per-batch user approval needed
  (DECISIONS 027): Apple MacBook Pro 14-inch with PROLED XDR
  Display, M5 Pro 15-core/16-core, 24GB/1TB, Space Black, Standard
  display (MJ2K4LL/A, UPC pending), Sony WF-C510 Black (WFC510/B,
  UPC pending), Sony INZONE H5 Black (WHG500/B, UPC pending),
  Logitech PRO X2 SUPERSTRIKE LIGHTSPEED, Lunar Eclipse (910-007700,
  UPC pending), Keychron B40 75% Alice, Deep Black (B40-K9, no
  UPC/EAN found). One variant pinned per model (DECISIONS 015); 0 of
  5 identifiers verified — all 5 stay pending on single-source-only
  UPC/EAN codes (Adorama spec table only, B&H spec page only, Sony
  spec sheet via manuals.plus only, Keychron store page only —
  Adaptive Controller / DualSense / PULSE Elite precedent, not a
  reason to hold the batch). Verified-identifier count stays 68.
- Why these 5: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (PROLED XDR is the
  first touchscreen tandem-OLED MacBook Pro, a distinct display line
  vs the M6 and the Liquid Retina M5 Pro; C510 is Sony's compact
  everyday budget earbud line, not a 1000X flagship or the C710N;
  INZONE H5 is the first INZONE headset in the set, Sony's mid-range
  wireless gaming headset vs the PULSE headsets; Superstrike is
  Logitech G's haptic-trigger PRO mouse line, not a Superlight and
  not a keyboard — the candidate note mislabelled it; B40 is
  Keychron's budget Alice-layout scissor-switch line, not a K8 or
  Q-series board). All five are in stock new in the US on 2026-11-06
  (brand-direct pages or InStock JSON-LD), except the two price-only
  direct rows and the Abt INZONE PreOrder row noted below.
- What was corrected along the way: the PROLED XDR candidate note
  "from $2,899 (pre-order 11.6)" is confirmed current — the base
  14-inch is $2,899 at Apple direct and Best Buy, on sale from
  2026-11-06, and it runs M5 Pro (not M6); the WF-C510 candidate
  price $69.99 is the list price while the current street price is
  $58 at B&H, Abt, Electronic Express and Focus Camera ($59.99 at
  Best Buy); the INZONE H5 candidate price ~$249.99 matches no
  current US price — the current street price is $128 at Focus
  Camera, Datavision and Abt (comp. value $178), with Sony direct
  listing the White at $159.99 sale / $179.99 original; the
  "Superstrike" candidate was a gaming keyboard in the notes but is
  in fact a wireless gaming mouse ($179.99), and the $199.99 Best
  Buy row is the newer PRO X3 SUPERSTRIKE, a different model; the
  B40 candidate price $49.99 is confirmed current at Keychron
  direct (Deep Black, the only variant).
- Variant pinning, recorded explicitly: PROLED XDR pins the base
  14-inch M5 Pro 15-core CPU / 16-core GPU, 24GB, 1TB, Space Black,
  Standard display (MJ2K4LL/A) — the 16-inch, M5 Max, 48GB and
  Nano-texture configurations are different configurations; WF-C510
  pins Black (WFC510/B) — White, Blue and Yellow are different
  colorways; INZONE H5 pins Black (WHG500/B) — White is a different
  colorway; Superstrike pins Lunar Eclipse (910-007700), the only US
  colorway (white casing, black buttons) — the EU/Asia 910-007777 /
  910-007778 are different regional part numbers; B40 pins Deep
  Black (B40-K9), the only colorway sold — the B39 (96% Alice,
  $54.99) is the larger sibling, a different model.
- What does NOT change: the existing 87 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–12 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 92 on the next edit (parent
  owns the cron; not touched here).
- Revisit: all five UPC/EAN codes stay pending until a second
  non-Amazon US source confirms each (PROLED 195951196749, WF-C510
  027242930339, INZONE H5 027242927919, Superstrike 097855211309,
  B40 none found); the Apple direct PROLED price was not shown in
  the buy-page text ($2,899 per the Apple announcement and Best
  Buy) — re-check next refresh; the Abt INZONE H5 $128 is price-only
  (PreOrder, "Notify me when this item is available") — re-check
  stock next refresh; the Sony direct INZONE H5 Black price was not
  confirmed (only the White, $159.99 sale / $179.99 original, on a
  stale category crawl) — re-check next refresh; the Logitech G
  direct Superstrike US price was not confirmed in page text —
  re-check; the ULT WEAR $148.00 Black Friday street price should
  be re-checked after Nov 8 (batch 9 revisit, still open); the Sony
  direct CH720N $89.99 is a sale price and should be re-checked
  after the sale ends.

## 036 (2026-11-06): Expansion batch 14 — 92 → 96 models (continuous expansion, DECISIONS 027)

- Decision: add 4 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/023/025), no per-batch user approval needed
  (DECISIONS 027): Sony MDR-7506, Black (MDR7506, UPC pending),
  Sony PlayStation Pulse Wireless Headset, White ($99.99, pre-order,
  no identifiers published yet), Sony LinkBuds Clip, Black
  (WF-LC900/B, UPC pending), Nintendo 64 Controller, Gray (HAC-043,
  Nintendo SKU 128577, UPC pending). One variant pinned per model
  (DECISIONS 015); 0 of 4 identifiers verified — all 4 stay pending
  on single-source-only or no-source codes (Adaptive Controller /
  DualSense / PULSE Elite precedent, not a reason to hold the batch).
  Verified-identifier count stays 68. The fifth candidate, Apple Pro
  Display XDR, was NOT added: discontinued March 3, 2026 and
  replaced by the Studio Display XDR (see below) — the batch was
  split rather than forcing it in (batch 3 AirPods 5 precedent).
- Why these 4: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (MDR-7506 is Sony's
  pro studio monitor line — the set has no MDR model at all; the new
  PlayStation Pulse is the base planar-magnetic headset below the
  Elite, distinct from the Elite, the Explore and the older PULSE 3D;
  LinkBuds Clip is the distinct 2026 clip-on open-ear line vs the
  Fit and the Open; the N64 controller is the distinct retro NSO
  controller line vs the Joy-Con and Pro Controller lines). Three of
  the four are in stock new in the US on 2026-11-06 (brand-direct
  pages or InStock JSON-LD); the Pulse is pre-order only until its
  November 19 launch, which is recorded explicitly rather than
  presented as in-stock.
- What was corrected along the way: the Pro Display XDR candidate
  price $3,299 is NOT a Pro Display XDR configuration — the Pro
  Display XDR was $4,999 standard glass / $5,999 nano-texture, and
  it was discontinued March 3, 2026 (EveryMac); Apple's
  /shop/buy-mac/pro-display-xdr URL now serves the "Buy Studio
  Display XDR" page, and the Meta Catalog feed returns Studio
  Display XDR rows for the query. $3,299 is the Studio Display XDR
  launch price (standard glass, tilt-and-height stand — Sweetwater
  $3,299, Sam's Club $3,299; Apple direct nano-texture tilt-height
  $3,599, nano VESA $3,199). The Studio Display XDR itself (27-inch
  5K mini-LED, 120Hz, from $3,299) is a distinct new line and was
  NOT substituted in — it is a different model from the named
  candidate and needs its own batch; the set's Studio Display 2026
  (MFEX4LL/A, $1,599) is the separate non-XDR line. The PULSE $99
  (pre-order) candidate figure is the NEW PlayStation Pulse headset
  (2026), not the PULSE 3D (CFI-ZWH1, 2020, $99.99) — the PULSE 3D
  is the older base line and was not added. The LinkBuds Clip
  candidate price $229.99 is the launch SRP while the current US
  street price is $198 at Best Buy, Sweetwater, BuyDig and Abt
  (comp. value $228). The N64 controller candidate price $49.99 was
  the 2021 launch price — the current Nintendo direct price is
  $54.99. The MDR-7506 candidate price $114.99 is confirmed current
  at Sony direct (street $113 at Abt and Sweetwater).
- Variant pinning, recorded explicitly: MDR-7506 pins Black
  (MDR7506), the only colorway sold; Pulse pins White, the
  first-listed launch colorway in Sony's announcement — Midnight
  Black is the other launch colorway; LinkBuds Clip pins Black
  (WFLC900/B) — Greige, Green and Lavender are different colorways;
  N64 controller pins Gray (HAC-043; Nintendo SKU 128577), the only
  colorway sold — the revised HAC-043(-01) with a replaceable
  battery (Europe, early 2027) is a different hardware revision.
- What does NOT change: the existing 92 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–13 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 96 on the next edit (parent
  owns the cron; not touched here).
- Revisit: all four identifier sets stay pending until a second
  non-Amazon US source confirms each (MDR-7506: no UPC surfaced on
  any US spec page; Pulse: no identifiers published yet — re-check
  after the Nov 19 launch; LinkBuds Clip Black 027242934054, BuyDig
  spec table only; N64 00045496894948, Nintendo US page only); the
  Pulse has a single quote (PlayStation Direct $99.99 pre-order) —
  add a Best Buy pre-order quote once a verbatim Best Buy product
  URL surfaces; the Sony direct LinkBuds Clip price rests on a
  270-day-old crawl ($229.99 SRP) — re-confirm; the MusicArts
  MDR-7506 $89.99 feed row is the low outlier vs $113–$114.99
  elsewhere and was not page-verified — re-check; the Studio
  Display XDR (from $3,299) is a candidate for a future batch, not
  added here; the ULT WEAR $148.00 Black Friday street price should
  be re-checked after Nov 8 (batch 9 revisit, still open); the Sony
  direct CH720N $89.99 is a sale price and should be re-checked
  after the sale ends.

## 037 (2026-11-06): Expansion batch 15 — 96 → 100 models (continuous expansion, DECISIONS 027)

- Decision: add 4 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/023/025), no per-batch user approval needed
  (DECISIONS 027): Apple Studio Display XDR, Standard glass,
  Tilt- and height-adjustable stand (MFEL4LL/A, UPC pending), Sony
  MDR-M1, Black (MDRM1, UPC pending), Sony MDR-MV1, Black (MDRMV1,
  UPC pending), Keychron B39, 96% Alice, Deep Black (B39-K9, UPC
  pending). One variant pinned per model (DECISIONS 015); 0 of 4
  identifiers verified — all 4 stay pending on single-source-only
  or no-source codes (Adaptive Controller / DualSense / PULSE Elite
  precedent, not a reason to hold the batch). Verified-identifier
  count stays 68. The fifth candidate, Sony INZONE H7, was NOT
  added: discontinued by Sony (Audio46 lists it "Discontinued";
  Headphone Zone: "permanently discontinued by the manufacturer"),
  the Meta Catalog feed returns no Sony-direct or Best Buy H7 row,
  and only ListenUp still lists it ($228.00) — the batch was split
  rather than forcing it in (batch 3 AirPods 5 precedent; batch 14
  Pro Display XDR precedent).
- Why these 4: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (the Studio Display
  XDR is the separate mini-LED 120Hz XDR monitor line vs the
  non-XDR Studio Display 2026; the MDR-M1 is Sony's modern pro
  reference closed monitor line vs the 1991 MDR-7506; the MDR-MV1
  is the open-back reference monitor sibling of the M1, not a
  closed-back variant of it; the B39 is the larger 96% Alice
  sibling of the 75% B40). All four are in stock new in the US on
  2026-11-06 (brand-direct pages or InStock JSON-LD), except the
  Sony direct MDR-M1 price, which rests on a stale 2024 crawl (see
  below).
- What was corrected along the way: the Studio Display XDR
  candidate price $3,299 is confirmed current and is the
  standard-glass tilt-and-height config (MFEL4LL/A) — $2,899 is
  the standard-glass VESA config (MFEN4LL/A), $3,599 / $3,199 are
  the nano-texture tilt-height / VESA configs; the B&H UPC
  195950527650 belongs to the VESA config and was not copied to
  the MFEL entry. The MDR-M1 candidate price $269.99 is confirmed
  current-ish ($268 at B&H and Sweetwater, $269.99 at Vintage
  King) while $249.99 is the launch MSRP, not the current street
  price. The MDR-MV1 candidate price $339.99 matches no US price —
  the MSRP is $419.99 and the current US street price is
  $418–$419.99. The B39 candidate price $54.99 is confirmed
  current at Keychron direct (Deep Black, Available). The INZONE
  H7 candidate "~$349.99 launch price" was wrong: the H7 launched
  in 2022 at $229.99 US.
- Variant pinning, recorded explicitly: Studio Display XDR pins
  Standard glass, Tilt- and height-adjustable stand (MFEL4LL/A) —
  the VESA (MFEN4LL/A, $2,899) and nano-texture (MFEP4LL/A,
  $3,599; MFEQ4LL/A, $3,199) configs are different configurations;
  MDR-M1 pins Black (MDRM1), the only colorway sold; MDR-MV1 pins
  Black (MDRMV1), the only colorway sold; B39 pins 96% Alice, Deep
  Black (B39-K9) — Deep Black is the only colorway sold, mirroring
  the B40 pinning.
- What does NOT change: the existing 96 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–14 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 100 on the next edit (parent
  owns the cron; not touched here).
- Revisit: all four identifier sets stay pending until a second
  non-Amazon US source confirms each (XDR MFEL4LL/A: no UPC on any
  US retailer spec page; MDR-M1 027242930612, B&H spec page only —
  manuals.plus mirrors the Amazon ASIN listing and does not count
  as the second source; MDR-MV1 027242926585, eBay listing only;
  B39: SKU B39-K9 on the Keychron page only, no UPC anywhere);
  the Sony direct MDR-M1 $249.99 rests on a page crawled
  2024-10-22 — re-confirm the direct price; the Sony direct MDR-MV1
  US page returned 403 on 2026-11-06 — re-check; the INZONE H7
  stays out while discontinued (ListenUp $228 is the sole remaining
  US listing); the ULT WEAR $148.00 Black Friday street price should
  be re-checked after Nov 8 (batch 9 revisit, still open); the Sony
  direct CH720N $89.99 is a sale price and should be re-checked
  after the sale ends.

## 033 (2026-11-06): Expansion batch 11 — 77 → 82 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the remaining brand-sweep candidates
  (BUILD_LOG 020/022/023/024/025), no per-batch user approval needed
  (DECISIONS 027): Apple Magic Trackpad USB-C White (MXK93AM/A, UPC
  195949654305), Sony WH-CH720N Black (WHCH720N/B, UPC 027242925397),
  Logitech G915 X LIGHTSPEED full-size Tactile Black (920-012670, UPC
  097855195005), Microsoft Xbox Adaptive Controller White (JMU-00003,
  UPC pending), Keychron K8 hot-swappable Red (K8-G1, UPC
  617748997921). One variant pinned per model (DECISIONS 015); 4 of
  5 identifiers verified, Adaptive Controller stays pending (UPC
  conflict, no US retailer spec page — DualSense Edge / DEX / Neo /
  PULSE Elite precedent, not a reason to hold the batch).
- Why these 5: they are the next un-added mainstream lines from the
  five brand sweeps, each distinct from the set (first trackpad in
  the set, and the distinct glass-trackpad line vs the Magic Mouse;
  CH720N is Sony's lightweight mid-range noise-cancelling line, not
  a 1000X flagship; G915 X is Logitech G's low-profile wireless
  gaming keyboard, not an MX keyboard; Adaptive Controller is the
  first Xbox accessibility controller; base K8 is the original
  tenkeyless line vs the K8 HE and K8 Ultra 8K successors). All five
  are in stock new in the US on 2026-11-06 (brand-direct pages or
  InStock JSON-LD), except the two price-only direct rows noted
  below and the K8-G1 stock flip (see below).
- What was corrected along the way: the Trackpad candidate price
  $129 is the White price — the Black trackpad (MXKA3AM/A) is $149
  and is a different colorway; the CH720N candidate price $89.99 is
  the current Sony direct sale price (was $179.99) while retailer
  street price is $178–$180, and the launch MSRP was $149.99
  (Sony's own page now lists MSRP $179.99); the G915 X candidate
  price $129.99 was an Amazon Clicky-switch deal price, not the
  standard US Tactile price — the LIGHTSPEED full-size Tactile
  Black is $259.99 (Logitech G, Best Buy, Quill; B&H $219.99
  sale); the Adaptive Controller's current retail MPN is JMU-00003
  (Best Buy SKU 6455394, InStock) — the older JMU-00001 listing
  (SKU 6381218) is no longer available new; the K8 candidate price
  $59.99+ is the base price (K8-A1, soldered, $59.99) while the
  pinned hot-swappable Red K8-G1 is $69.99.
- Variant pinning, recorded explicitly: G915 X pins full-size
  LIGHTSPEED, GL Tactile (Brown), Black — logitechg.com defaults
  to the full-size LIGHTSPEED line at $259.99 with per-switch URLs
  (.920-012670 Tactile, .920-012696 Linear, .920-012704 Clicky);
  TKL ($229.99) and the wired Linear (920-012950, $199.99) are
  different configurations. K8 pins White Backlight, Keychron
  Super Switch (Hot-Swappable), Red (K8-G1) — mirroring the K8 Pro
  precedent (hot-swappable, White Backlight, Red); the
  page-default K8-A1 (Gateron G Pro Mechanical, Red, $59.99) is
  the soldered version, not hot-swappable, and was not pinned.
- What does NOT change: the existing 77 catalog entries are untouched
  (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro untouched,
  batches 1–10 entries untouched). No other snapshot file is rewritten.
  No Amazon touch. The daily refresh cron still says "57 models" in
  its body and needs a count update to 82 on the next edit (parent
  owns the cron; not touched here).
- Revisit: Adaptive Controller White UPC stays pending until a US
  retailer spec page or box barcode settles it (889842295368 vs
  889842439038, both tied to JMU-00003 in eBay listings); K8-G1
  stock flips between reads (out of stock in the 2026-11-06 product
  JSON, Available 2 days earlier) and should be re-checked on the
  next refresh; the Microsoft direct Adaptive $99.99 and Keychron
  direct K8-G1 $69.99 prices are price-only (stock not confirmed in
  the page text); the B&H CH720N $178.00 price rests on a page
  crawled 2026-09-12 and should be re-confirmed; the ULT WEAR
  $148.00 Black Friday street price should be re-checked after
  Nov 8 (batch 9 revisit, still open); the Sony direct CH720N
  $89.99 is a sale price and should be re-checked after the sale
  ends.

## 038 (2026-11-06): Expansion batch 16 — 100 → 105 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Anker models from the anker.com US homepage sweep
  (BUILD_LOG 054), no per-batch user approval needed (DECISIONS
  027): Anker MagGo 2 Pro Magnetic Power Bank (10K, Qi2 25W, Active
  Cooling), Phantom Gray (A110R, UPC pending), Anker Prime Power
  Bank (26K, 300W), Black (A110A, UPC pending), Anker Desktop USB-C
  Hub, 10-in-1 Dual 4K (A210C, UPC pending), Anker Prime Wireless
  Car Charger (MagGo, AirCool, Pad), (A2933, UPC pending), Anker
  Nano Charger (70W, 3 Ports), Black Stone (B121A, UPC pending).
  One variant pinned per model (DECISIONS 015); 0 of 5 identifiers
  verified — all 5 stay pending on single-source-only or no-source
  codes (Adaptive Controller / DualSense / PULSE Elite precedent,
  not a reason to hold the batch). Verified-identifier count stays
  68. The Anker Nano Charger (45W, Smart Display, 180° Foldable,
  A121D) was NOT added: two different US product pages ($34.99
  PreOrder on the dual-foldable page vs $39.99 InStock on the
  foldable-plug-compact page) and the page text never states which
  Shopify variant is which color, so no color can be pinned cleanly
  — the Nano 70W replaces it as this batch's charger pick (batch 14
  Pro Display XDR / batch 15 INZONE H7 precedent: split the batch
  rather than forcing a model in).
- Why these 5: they are the first Anker-brand sweep (the set's only
  prior Anker entry is the Prime Charger 100W, A2688), one per
  product family where the official US catalog has a current model
  — flagship magnetic power bank, flagship laptop power bank, USB-C
  hub/dock, car charger, compact wall charger. Soundcore
  earbuds/speakers were not picked: they are not listed on anker.com
  (separate soundcore.com store), and the task rule is "only what
  the official US catalog actually lists as current". All five are
  in stock new in the US on 2026-11-06 (Anker direct JSON-LD
  InStock, page-verified).
- What was corrected along the way: the A110A direct price is
  $199.99 on sale, not $229.99 — $229.99 is the list price (product
  JSON-LD and the Meta feed both show it; the homepage shelf and
  the "$30 OFF" banner show $199.99); the A210C direct price is
  $79.99 on sale, not $99.99 — $99.99 is the list price (JSON-LD
  and the feed both show it; the homepage shelf and the Anker blog
  "$20 OFF, $79.99, Code: WSPDV2ONVYED" show $79.99); the anker.com
  feed row for the A2933 car charger says $135, but the live page
  JSON-LD and the us.anker.com feed row both say $89.99 — the $135
  row is stale and was excluded; the A121D two-page / PreOrder
  problem above; the B121A model number is B121A on Anker's own
  page while Notebookcheck and Amazon listings call the same
  charger A121A — the Anker page takes precedence and A121A was not
  recorded as a separate identifier.
- Variant pinning, recorded explicitly: MagGo 2 Pro pins Phantom
  Gray (A110R) — one of four colors (Starlight Silver, Polar Night
  Blue, Phantom Gray, Burgundy Red), price color-independent at
  $109.99, but the page does not state which Shopify variant is
  Phantom Gray, so the color-to-variant mapping is recorded as
  unverified; Prime 26K pins Black (A110A) — Heavins IE lists
  A110AH11 Black, but its EAN 0194644239299 is the EU/IE regional
  code and was not copied (MDR-MV1 EAN precedent); Desktop Hub pins
  10-in-1, Dual 4K (A210C) with no color claimed — the Anker page
  names no colorway and the Amazon-derived "Iron Gray" was not
  corroborated; the VALORANT Limited Edition ($109.99, same A210C
  base) is a different edition and was not pinned; Car Charger pins
  MagGo, AirCool, Pad (A2933), the only configuration sold; Nano
  70W pins Black Stone (B121A) — one of four colors (green, pink,
  black, white) on the Anker page, with "Black Stone" named by
  Impulse Cameras; Best Buy White is $34.99, cheaper than Black at
  $39.99, and was not pinned.
- What does NOT change: the existing 100 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–15 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 105 on
  the next edit (parent owns the cron; not touched here).
- Revisit: all five identifier sets stay pending until a second
  non-Amazon US source confirms each (A110R: no UPC anywhere;
  A110A: no US UPC on any retailer spec page; A210C: UPC
  194644340506 only on pickoryx, which mirrors the Amazon ASIN
  listing; A2933: no UPC anywhere; B121A: UPC 194644241247 for
  Black on Amazon listings only); the A121D stays out until Anker
  consolidates its two US pages or a retailer spec page settles
  the color-to-variant mapping (bundle slug 'bundle-b121a111-
  a1638011' hints the B121A black variant MPN may be B121A111,
  mirroring A121D121 = White confirmed by Best Buy Canada —
  unverified, check next refresh); the Anker direct A110A $199.99
  and A210C $79.99 are sale prices and should be re-checked after
  the sale ends; the ULT WEAR $148.00 Black Friday street price
  should be re-checked after Nov 8 (batch 9 revisit, still open);
  the Sony direct CH720N $89.99 is a sale price and should be
  re-checked after the sale ends.

## 039 (2026-11-06): Expansion batch 17 — 105 → 110 models (continuous expansion, DECISIONS 027)

- Decision: add 5 JBL models from the jbl.com US storefront sweep
  (BUILD_LOG 055), no per-batch user approval needed (DECISIONS
  027): JBL Flip 7, Black (JBLFLIP7BLKAM, UPC 050036407342
  VERIFIED), JBL Tour One M3 Smart Tx, Black (JBLTOM3AVIBLKAM,
  UPC pending), JBL Tour Pro 3, Black (JBLTOURPRO3BLKAM, UPC
  pending), JBL Bar 1300XMK2, Black (JBLBAR1300XM2BLKAM, UPC
  pending), JBL PartyBox Stage 320, Black (JBLPBSTAGE320AM, UPC
  pending). One variant pinned per model (DECISIONS 015); 1 of 5
  identifiers verified — the other 4 stay pending on
  single-source-only or no-source codes (Adaptive Controller /
  DualSense / PULSE Elite precedent, not a reason to hold the
  batch). Verified-identifier count rises 68 → 69. The PartyBox
  330 (new 2026 successor to the Stage 320) was NOT added: its US
  price is conflicting ($499.95 on the JBL US page per one source
  vs $630 per another), so no price can be pinned cleanly —
  revisit next sweep (batch 14 Pro Display XDR / batch 15 INZONE
  H7 precedent: split the batch rather than forcing a model in).
- Why these 5: they are the first JBL-brand sweep (the set had no
  JBL entry at all), one per product family where the official US
  catalog has a current model — flagship portable speaker,
  flagship over-ear ANC headphones, flagship true-wireless
  earbuds, flagship soundbar, wheeled party speaker. They are also
  the set's first speakers, first soundbar and first party
  speaker (new categories "speakers" and "soundbars"; category
  strings are free-form, no validation to update). All five are
  in stock new in the US on 2026-11-06 (JBL direct JSON-LD
  InStock / feed brand_direct rows, page-verified).
- What was corrected along the way: the Tour One M3 Smart Tx
  $199.95 sale (audiowords, checked 2026-11-01; Slickdeals/Best
  Buy ~8 days ago) has ended — the Best Buy page now shows
  $449.95 and the JBL feed row shows $449.95, so $449.95 is the
  current price at JBL direct, Abt, Best Buy, PC Richard and
  Sweetwater; the Meta feed's Abt $229.95 Tour Pro 3 Black row
  conflicts with the live Abt page ($329.95) and was excluded as
  stale (A2933 $135 precedent); the Flip 7 $149.95 is the April
  2025 launch price, $129.95 is the current JBL direct sale price;
  the US soundbar is the Bar 1300XMK2 (12-inch sub, 1570W max) —
  the non-US Bar 1300MK2 (dual 8-inch sub, 2470W) is a different
  regional variant and was not added, even though Best Buy lists
  the US bar under the BAR1300MK2 name with model
  JBLBAR1300XM2BLKAM; the non-Tx Tour One M3 (JBLTOURONEM3BLKAM,
  headphones-only) is a different product from the US Smart Tx
  bundle and was not added.
- Variant pinning, recorded explicitly: Flip 7 pins Black
  (JBLFLIP7BLKAM) — one of several colorways (Black, Blue, White,
  Red, Purple, Squad, Camo), price color-independent at $129.95;
  the JBL US page crawl shows Item# JBLFLIP7TBLUAM (an
  unexplained page artifact — the global.jbl.com Black page shows
  JBLFLIP7BLKAM and Best Buy's Blue model is JBLFLIP7BLUAM, so
  the Black AM code stands); Tour One M3 pins Smart Tx, Black
  (JBLTOM3AVIBLKAM) — the US sells the Smart Tx bundle (the
  headphones-only JBLTOURONEM3BLKAM is sold outside the US);
  Tour Pro 3 pins Black (JBLTOURPRO3BLKAM); Bar 1300XMK2 pins
  Black (JBLBAR1300XM2BLKAM), the only colorway sold; PartyBox
  Stage 320 pins Black (JBLPBSTAGE320AM) — the JBL US page
  Item# is JBLPBSTAGE320AM and Sharaf DG lists PARTYBOXSTAGE320AM
  as Black; the White code is JBLPBSTAGE320SWAM and was not
  pinned.
- What does NOT change: the existing 105 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–16 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 110 on
  the next edit (parent owns the cron; not touched here).
- Revisit: the four pending identifier sets stay pending until a
  second non-Amazon US source confirms each (Tour One M3: UPC
  050036414029 on snapklik + tanotis aggregators only; Tour Pro 3:
  UPC 050036402392 on Amazon listings only; Bar 1300XMK2: UPC
  050036414869 on Amazon + an eBay refurbished listing + Target
  Plus partner data only; PartyBox Stage 320: no UPC surfaced
  anywhere); the PartyBox 330 stays out until its US price is
  settled; the Flip 7 $129.95 and Tour One M3 $449.95 are
  current-price observations that should be re-checked after the
  sale ends; the ULT WEAR $148.00 Black Friday street price
  should be re-checked after Nov 8 (batch 9 revisit, still open);
  the Sony direct CH720N $89.99 is a sale price and should be
  re-checked after the sale ends.

## 040 (2026-11-06): Expansion batch 18 — 110 → 115 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Razer models from the razer.com US store sweep
  (BUILD_LOG 056), no per-batch user approval needed (DECISIONS
  027): Razer Viper V4 Pro, Black (RZ01-05630100-R3U1, UPC
  pending), Razer BlackWidow V4 Pro, Green switches, Black
  (RZ03-04680200-R3U1, UPC pending), Razer BlackShark V3 Pro, PC
  version, Black (RZ04-05400100-R3U1, UPC pending), Razer
  Wolverine V3 Pro, Black (RZ06-05200100-R3U1, UPC pending),
  Razer Kraken V4 Pro, Black (RZ04-05160100-R3U1, UPC pending).
  One variant pinned per model (DECISIONS 015); 0 of 5 identifiers
  verified — all 5 stay pending on single-source-only or no-source
  codes (Anker batch 16 precedent: 0 of 5 verified is not a reason
  to hold the batch). Verified-identifier count stays 69. No model
  was split out of this batch.
- Why these 5: they are the first Razer-brand sweep (the set had no
  Razer entry at all), one per product family where the official US
  catalog has a current model — flagship symmetrical esports mouse,
  flagship full-size keyboard, flagship esports headset, flagship
  Xbox/PC controller, flagship haptic lifestyle headset. The two
  headsets are different lines (BlackShark = esports, Kraken =
  lifestyle/haptic), not a duplicate family. All five are in stock
  new in the US on 2026-11-06 (Razer direct listings + Best Buy
  InStock JSON-LD / Add to cart, page-verified).
- What was corrected along the way: Razer's US models all carry
  the R3U1 suffix — the R3G1 (EU) and R3M1 (global) codes are
  different regional variants and were not used as US identifiers
  (Viper V4 Pro EU EAN 8887910085134, Kraken V4 Pro EU EAN
  8887910060094, PBTech's Kraken UPC 840272909980 listed against
  the R3M1); the BlackShark V3 Pro UPC 840272919484 appears on
  Amazon listings only and was not recorded; the BlackWidow V4 Pro
  Green UPC 840272903315 is stated on the B&H page only and stays
  pending for lack of a second source; the Yellow-switch UPC
  840272903339 is a different switch variant and was not copied;
  the BlackShark platform variants (PlayStation RZ04-05400500-R3G1,
  Xbox RZ04-05400300-R3U1) are different products at the same
  $249.99 and were not pinned; the Wolverine V3 Pro 8K PC
  (RZ06-05540100-R3U1, PC-only) is a different model from the
  Xbox/PC Wolverine V3 Pro and was not pinned; the Razer direct
  Viper V4 Pro price is $159.99 (the March 24, 2026 launch release
  and Windows Central agree) — there is no Razer direct row for it
  in the Meta feed, so the quote rests on the release + the
  resolving US product URL, marked price-only.
- Variant pinning, recorded explicitly: Viper V4 Pro pins Black
  (RZ01-05630100-R3U1) — White (RZ01-05630200-R3U1) is a different
  SKU, 50 g vs 49 g; BlackWidow V4 Pro pins Green switches, Black
  (RZ03-04680200-R3U1) — Yellow (RZ03-04681900-R3U1) and Orange
  (RZ03-04683500-R3M1) are different switch variants, White
  (RZ03-04683600-R3U1) a different colorway; BlackShark V3 Pro
  pins the PC version, Black (RZ04-05400100-R3U1) — the platform
  variants above are different products; Wolverine V3 Pro pins
  Black (RZ06-05200100-R3U1) — White (RZ06-05200200-R3U1) is a
  different SKU; Kraken V4 Pro pins Black (RZ04-05160100-R3U1),
  the only colorway sold.
- What does NOT change: the existing 110 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–17 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 115 on
  the next edit (parent owns the cron; not touched here).
- Revisit: all five identifier sets stay pending until a second
  non-Amazon US source confirms each (Viper V4 Pro: no US UPC
  anywhere; BlackWidow Green: UPC 840272903315 on B&H only;
  BlackShark V3 Pro: UPC 840272919484 on Amazon only; Wolverine
  V3 Pro: no UPC anywhere; Kraken V4 Pro: UPC 840272909980 listed
  against the R3M1 only); the DeathAdder V4 Pro Black
  (RZ01-05330100-R3U1, $169.99) and Basilisk V4 Pro Black
  (RZ01-05670100-R3U1, $169.99) stay list-only for later batches;
  Blade laptops stay out — Razer rotates configurations and no
  single retailer-pinned base config was found (DECISIONS 015);
  the ULT WEAR $148.00 Black Friday street price should be
  re-checked after Nov 8 (batch 9 revisit, still open); the Sony
  direct CH720N $89.99 is a sale price and should be re-checked
  after the sale ends.

## 041 (2026-11-06): Expansion batch 19 — 115 → 120 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Corsair models from the corsair.com US store sweep
  (BUILD_LOG 057), no per-batch user approval needed (DECISIONS
  027): Corsair M65 RGB Ultra, Black, wired (CH-9309411-NA2, UPC
  pending), Corsair K65 Plus Wireless, Midnight Grey, MLX Red
  linear (CH-91D401L-NA, UPC pending), Corsair Virtuoso Max
  Wireless, Carbon (CA-9011372-WW, UPC pending), Corsair FRAME
  4000D RS ARGB, Black (CC-9011296-WW, UPC pending), Corsair iCUE
  LINK Titan II 360 RX RGB, Black (CW-9061037-WW, UPC pending).
  One variant pinned per model (DECISIONS 015); 0 of 5 identifiers
  verified — all 5 stay pending on single-source-only or no-source
  codes (Anker batch 16 precedent: 0 of 5 verified is not a reason
  to hold the batch). Verified-identifier count stays 69. No model
  was split out of this batch. Two new categories enter the set:
  pc-cases (FRAME 4000D RS ARGB) and cpu-coolers (Titan II 360 RX
  RGB); category is free-form and unused by the eval.
- Why these 5: they are the first Corsair-brand sweep (the set had
  no Corsair entry at all — grep finds zero), one per product family
  where the official US catalog has a current in-stock model —
  flagship wired FPS mouse, current 75% wireless keyboard, flagship
  wireless headset, current modular mid-tower case, current flagship
  360 mm AIO cooler. Corsair sells no first-party controller on
  corsair.com US (SCUF is a separate store), so there is no
  controller pick this batch. All five are in stock new in the US on
  2026-11-06 (Corsair direct pages, page-verified, plus Best Buy /
  Micro Center / Newegg feed rows).
- What was corrected along the way: Corsair SKUs carry regional
  suffixes — the NA/NA2 US codes were pinned and the EU/EU2 codes
  were not used (M65 RGB Ultra Wireless White EU CH-9319511-EU2 at
  129.99 EUR; K65 Plus Wireless EU at 159.99 EUR); the M65's
  original CH-9309411-NA SKU shows $69.99 Discontinued on
  corsair.com — the current revision is CH-9309411-NA2 at $59.99;
  the K65 Plus Wireless base colorway is Corsair's 'Original
  (Midnight Grey)', not Black (Best Buy lists it as Black/Gray);
  the Virtuoso Max $249.99 is a holiday sale price against the
  $299.99 list (stale checkout.corsair.com feed row still shows
  $299.99), not a price cut; the K65's $129.99 is a lapsed sale
  from a 4-day-old crawl — the live page read today says $159.99
  and Best Buy agrees; the Newegg FRAME 4000D RS ARGB $114.99 feed
  row is titled 'Non-LED' and may belong to the non-ARGB RS case,
  so it stays suspected; the Best Buy Titan II page's 'About this
  product' block wrongly describes the Titan II Ultra 360 LX LCD
  (a Best Buy copy error — Model/SKU/color/price are for this
  cooler); the Virtuoso Max UPC 840440484615 (manuals.plus spec
  table + eBay + Amazon) and the FRAME UPC 840440487715 (Amazon.in
  only) were not recorded — neither has a retailer or manufacturer
  listing stating it, and Amazon is never a corroborating source.
- Variant pinning, recorded explicitly: M65 RGB Ultra pins the
  wired Black (CH-9309411-NA2) — the Wireless (CH-9319511, $129.99)
  is a different connectivity variant; K65 Plus Wireless pins
  Midnight Grey, MLX Red linear (CH-91D401L-NA) — the Tactile
  (CH-91D441F-NA, $129.99) and all licensed editions (Call of Duty,
  Witcher 3, Cyberpunk) are different SKUs; Virtuoso Max pins
  Carbon (CA-9011372-WW) — Silver (CA-9011373-WW) is a different
  colorway and the Xbox version (CA-9011374-WW) a different platform
  variant, both at the same $249.99; FRAME 4000D RS ARGB pins Black
  (CC-9011296-WW) — White (CC-9011297-WW, $124.99) is a different
  colorway and the fanless FRAME 4000D ($104.99) a different model;
  Titan II 360 RX RGB pins Black (CW-9061037-WW) — White
  (CW-9061038-WW, GTIN 840440419471) is a different colorway and
  the LCD version ($239.99) a different model.
- What does NOT change: the existing 115 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–18 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 120 on
  the next edit (parent owns the cron; not touched here).
- Revisit: all five identifier sets stay pending until a second
  non-Amazon US source confirms each (M65: UPC 840006657613 on the
  Micro Center feed row only; K65: no UPC anywhere; Virtuoso Max:
  UPC 840440484615 on manuals.plus + eBay only; FRAME: UPC
  840440487715 on Amazon.in only; Titan II: GTIN 840440419464 on
  Scan UK only); the Virtuoso Max $249.99 and K65 $159.99 prices
  should be re-checked after the Early Black Friday event ends Nov
  8 (the Virtuoso Max is a $50-off holiday deal; the K65's $129.99
  crawl may return); the M65 RGB Ultra Wireless ($129.99), Sabre
  RGB Pro Wireless, HS80 Max Wireless ($119.99), Virtuoso RGB
  Wireless XT ($199.99), K70 CORE SE ($89.99–$109.99), Vengeance
  RGB DDR5 32GB 6000 CL30 (volatile $599.99–$657.99, conflicting
  stock) and WARTHOG case ($179.99, pre-order only) stay list-only
  for later batches; the ULT WEAR $148.00 Black Friday street price
  should be re-checked after Nov 8 (batch 9 revisit, still open);
  the Sony direct CH720N $89.99 is a sale price and should be
  re-checked after the sale ends.

## 042 (2026-11-06): Expansion batch 20 — 120 → 125 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Dell/Alienware models from the dell.com US store
  sweep (BUILD_LOG 058), no per-batch user approval needed (DECISIONS
  027): Dell 32 Plus 4K Monitor S3225QS, Ash White (F06FR, UPC
  884116485131 verified), Alienware 27 240Hz QD-OLED Gaming Monitor
  AW2726DM, Black (JW05F, UPC pending), Alienware Pro Wireless Gaming
  Mouse, Dark Side of the Moon (PRO-MS-G-DEAM, UPC 884116464914
  verified), Alienware Pro Wireless Gaming Keyboard, Dark Side of the
  Moon (WR47C, UPC pending), Alienware Pro Wireless Gaming Headset,
  Dark Side of the Moon (UPC pending). One variant pinned per model
  (DECISIONS 015); 2 of 5 identifiers verified, 3 stay pending on
  single-source-only or no-source codes (Corsair batch 19 precedent:
  0 of 5 verified is not a reason to hold the batch). Verified-
  identifier count rises 69 → 71. No model was split out of this
  batch. This batch completes the 125-model milestone (progress
  report point per DECISIONS 027). Two new brands enter the set:
  Dell and Alienware; two new categories enter the set: monitors
  (S3225QS, AW2726DM — the set's first monitors) — category is
  free-form and unused by the eval.
- Why these 5: they are the first Dell-brand sweep (the set had no
  Dell or Alienware entry at all), one per product family where the
  official US catalog has a current fixed-configuration in-stock
  model — mainstream 32-inch 4K productivity monitor, budget QD-OLED
  gaming monitor, flagship pro wireless mouse, flagship pro wireless
  keyboard, flagship pro wireless headset. No laptop or desktop pick:
  Dell laptops and desktops are configurable with no retailer-pinned
  base configuration (DECISIONS 015) — the Alienware 16 Aurora
  featured config is Sold Out and the XPS 14 (2026) has no fixed
  base config, so both families were left out rather than forced.
  All five are in stock new in the US on 2026-11-06 (Dell direct
  pages, page-verified or search-index read, plus Best Buy / Micro
  Center / Newegg feed rows).
- What was corrected along the way: Dell monitor MPNs are regional
  — the US codes were pinned and the regional codes were not used
  (S3225QS US F06FR vs Ireland MX17X; AW2726DM US JW05F vs UK
  N0XJ0); the S3225QS UPC 884116485131 is verified on Icecat +
  eBay, not on the Amazon listing that also states it (Amazon is
  never a corroborating source); the Pro Mouse UPC 884116464914
  belongs to the Black PRO-MS-G-DEAM, while the White PRO-MS-W-DEAM
  carries 884116464945 and was not used; the keyboard UPC
  884116464853 belongs to the White/Lunar Light board (Icecat
  PRO-KB-W-WW + Ubuy X3V4D) and was not carried across colorways
  to the pinned Dark Side board; the headset has two candidate
  UPCs (884116469728 manuals.plus, 884116469759 Amazon Lunar
  Light) and neither is corroborated, so both stay unrecorded; the
  keyboard MPN WR47C is Dark Side by elimination (X3V4D is Lunar
  Light); the headset's Dell feed rows ($229.99 / $199.99) lag the
  $174.99 sale shown on Dell's own search page and techaeris, so
  the page reads win per the Quill precedent; the AW2726DM's only
  code is the EU EAN 5397321030553 (single Icecat datasheet), not
  a US UPC.
- Variant pinning, recorded explicitly: S3225QS pins Ash White
  (F06FR) — the only colorway; AW2726DM pins Black (JW05F) — the
  only colorway; Pro Mouse pins Dark Side of the Moon
  (PRO-MS-G-DEAM) — Lunar Light (PRO-MS-W-DEAM) is a different
  colorway at the same $149.99 list; Pro Keyboard pins Dark Side
  of the Moon (WR47C) — Lunar Light (X3V4D) is a different
  colorway at the same $199.99 list; Pro Headset pins Dark Side
  of the Moon — Lunar Light is a different colorway (Best Buy
  BBY-AWProH-L, SKU 6605024, $199.99) and the AW725H/AW920H are
  different, cheaper headsets.
- What does NOT change: the existing 120 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–19 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 125 on
  the next edit (parent owns the cron; not touched here).
- Revisit: all five sale prices should be re-checked after the
  Early Black Friday event ends Nov 8 (S3225QS $329.99, AW2726DM
  $319.99, Pro Mouse $129.99, Pro Keyboard $174.99, Pro Headset
  $174.99); the AW2726DM UPC, Pro Keyboard Dark Side UPC and Pro
  Headset UPC stay pending until a second non-Amazon US source
  confirms each; the remaining Dell candidates (S2725QS 27-inch 4K
  $279.99, AW3226DM 32-inch $299.99, AW2726DL 280 Hz $229.99,
  AW3225DM 32-inch $249.99, AW2525HM 25-inch 320 Hz $249.99,
  AW720M $79.99, AW620M $86.99, AW920K $159.99, AW510K $129.99,
  AW420K $99.99, AW725H $149.99, AW520H $79.99, AW320M $69.99,
  UltraSharp U3225QE, Dell Pro 7 Webcam WB726, Dell Pro Thunderbolt
  5 Smart Dock SD25TB5) stay list-only for later batches; the ULT
  WEAR $148.00 Black Friday street price should be re-checked after
  Nov 8 (batch 9 revisit, still open); the Sony direct CH720N
  $89.99 is a sale price and should be re-checked after the sale
  ends.

## 043 (2026-11-06): Expansion batch 21 — 125 → 130 models (continuous expansion, DECISIONS 027)

- Decision: add 5 HP/HyperX models from the HP official US store
  sweep (BUILD_LOG 059), no per-batch user approval needed (DECISIONS
  027): HP OMEN 27s FHD 240Hz Gaming Monitor, Black (780G5AA#ABA,
  UPC pending), HyperX Cloud III Gaming Headset, Black-Red (727A9AA,
  UPC pending), HP 920 Ergonomic Vertical Mouse, Black (6H1A4AA#ABA,
  UPC 197029640277 verified), HP OMEN 27q G2 QHD 180Hz Gaming
  Monitor, Black (AV4H6AA#ABA, UPC pending), HyperX Alloy Rise 75
  Mechanical Gaming Keyboard, Black, US Layout, HyperX Red - Linear,
  wired (7G7A4AA#ABA, UPC pending). One variant pinned per model
  (DECISIONS 015); 1 of 5 identifiers verified, 4 stay pending on
  single-source-only or no-source codes (Corsair batch 19 precedent:
  0 of 5 verified is not a reason to hold the batch). Verified-
  identifier count rises 71 → 72. No model was split out of this
  batch. Two new brands enter the set: HP and HyperX; no new
  category enters the set (monitors, headphones, mice, keyboards
  already exist).
- Why these 5: they are the first HP-brand sweep (the set had no HP
  or HyperX entry at all), one per product family where the official
  US catalog has a current fixed-configuration in-stock model —
  mainstream 240 Hz FHD gaming monitor, mainstream wired gaming
  headset, ergonomic vertical mouse, mainstream 180 Hz QHD gaming
  monitor, flagship customizable 75% keyboard. No laptop or desktop
  pick: HP/OMEN laptops and desktops are configurable with no
  retailer-pinned base configuration (DECISIONS 015) — the sweep
  excluded them rather than forcing one. All five are in stock new
  in the US on 2026-11-06 (hp.com/us-en and hyperx.com US product
  pages, JSON-LD reads, plus Meta Catalog feed rows).
- What was corrected along the way: the Cloud III Black-Red MPN is
  727A9AA on the HP US product page — the sweep's 4P5M0AA came from
  a bundle listing and an OMEN desktop accessory upsell and is NOT
  the standalone headset's code, so 4P5M0AA was not recorded;
  727A8AA is the Black colorway and BS7C1AA is White, both
  different colorways at the same $99.99. HP monitor/mouse UPCs are
  regional by suffix and were NOT carried across suffixes: the
  OMEN 27s US (ABA) code is 197029615442, not 197029615466 (that is
  the ABB code); the HP 920 US (ABA) code is 197029640277, not
  196548939633 (that is the ABB/EMEA code); the OMEN 27q G2
  (ABB) code 198701661221 is not the US code — the HP datasheet
  lists no (ABA) UPC for the 27q G2 at all. The Best Buy feed title
  for the HP 920 says "Wired" but the HP US page specs the mouse as
  wireless (2.4 GHz + Bluetooth 5.3), so the title is a feed
  mislabel, not a second variant. The Distritech $217.49 OMEN 27s
  feed row (44% below the $389.99 HP list, not page-verified) was
  excluded from the snapshot as an unconfirmed outlier.
- Variant pinning, recorded explicitly: OMEN 27s pins Black
  (780G5AA#ABA) — the only colorway; Cloud III pins Black-Red
  (727A9AA) — Black (727A8AA), White (BS7C1AA) and Black/Lavender
  (DF7F0AA) are different colorways at the same $99.99; HP 920 pins
  Black (6H1A4AA#ABA) — the only colorway; OMEN 27q G2 pins Black
  (AV4H6AA#ABA) — the only colorway; Alloy Rise 75 pins Black, US
  Layout, HyperX Red - Linear, wired (7G7A4AA#ABA) — the only
  variant listed on the HyperX US store (the Wireless version is a
  different model).
- What does NOT change: the existing 125 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–20 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 130 on
  the next edit (parent owns the cron; not touched here).
- Revisit: all three sale prices should be re-checked after the
  Early Black Friday event ends Nov 8 (HP 920 $68.99, OMEN 27q G2
  $203.99, Alloy Rise 75 $84.99); the OMEN 27s UPC 197029615442,
  the Cloud III UPC 197029008237 (Amazon-only today, plus a
  conflicting second code 740617255522 on the same listings), the
  OMEN 27q G2 US UPC (no code surfaced at all) and the Alloy Rise
  75 UPC 197192334096 (HP leaflet only) stay pending until a second
  non-Amazon US source confirms each; the remaining HP candidates
  (OMEN 27k $370.32, OMEN OLED 27q $399.99, Series 3 Pro 327pf
  $194.00, E24mv G4 $210.40, E27k G5 $504.00, Cloud III S Wireless
  $179.99, CloudX Flight 2 $139.99, CloudX $59.99, Pulsefire Haste
  2 Pro $119.99, Pulsefire Haste 2 Wireless $89.99, QuadCast 2 S
  $149.99) stay list-only for later batches; the ULT WEAR $148.00
  Black Friday street price should be re-checked after Nov 8
  (batch 9 revisit, still open); the Sony direct CH720N $89.99 is
  a sale price and should be re-checked after the sale ends.

## 044 (2026-11-06): Expansion batch 22 — 130 → 135 models (continuous expansion, DECISIONS 027)

- Decision: add 5 HP/HyperX models from the HP official US store
  sweep (BUILD_LOG 059), no per-batch user approval needed (DECISIONS
  027): HP OMEN 27k UHD 144Hz Gaming Monitor, Black (780G8AA#ABA,
  UPC pending), HyperX OMEN OLED 27q QHD 240Hz Gaming Monitor,
  Black (CH0R2AA#ABA, UPC pending), HyperX Cloud III S Wireless
  Gaming Headset, Black-Red (A59Z0AA, UPC 198415435569 verified),
  HyperX Pulsefire Haste 2 Pro 4K Wireless Gaming Mouse, Slate
  Grey (A1KY5AA, UPC pending), HyperX QuadCast 2 S USB Microphone,
  Black (9A273AA, UPC pending). One variant pinned per model
  (DECISIONS 015); 1 of 5 identifiers verified, 4 stay pending on
  a conflicting code, a single-source code, or a missing (ABA)
  slot (Corsair batch 19 precedent: 0 of 5 verified is not a
  reason to hold the batch). Verified-identifier count rises
  72 → 73. No model was split out of this batch. One new category
  enters the set: microphones (QuadCast 2 S is the first
  microphone) — recorded here explicitly, not silently, per the HP
  printer precedent in BUILD_LOG 059 (a new category needs a
  category decision first); no new brand enters the set (HP and
  HyperX joined in batch 21).
- Why these 5: they are the remaining best-evidenced HP sweep
  candidates — one per product family where the official US catalog
  has a current fixed-configuration in-stock model: mainstream 4K
  144 Hz gaming monitor, mainstream QD-OLED gaming monitor,
  flagship wireless gaming headset, flagship 4 kHz wireless gaming
  mouse, flagship USB streaming microphone. No laptop or desktop
  pick: HP/OMEN laptops and desktops are configurable with no
  retailer-pinned base configuration (DECISIONS 015) — the sweep
  excluded them rather than forcing one. All five are in stock new
  in the US on 2026-11-06 (hp.com/us-en product pages, JSON-LD
  reads, plus Meta Catalog feed rows).
- What was corrected along the way: the QuadCast 2 S HP direct
  price is $149.99 sale (vs $199.99 list), confirmed on a fresh
  hp.com/us-en page read — a 5-day-old search-index read showing
  $159.99 was stale and was not used. HP monitor UPCs are regional
  by suffix and were NOT carried across suffixes: the OMEN 27k US
  (ABA) slot is absent from the HP datasheet (only (ABB)
  197029615961 and (ABU) 197029615992 are listed), exactly like
  the OMEN 27q G2 in batch 21. The OMEN OLED 27q UPC is a genuine
  conflict, not a verification: the HP datasheet (1WorldSync)
  states P/N CH0R2AA, UPC 199642944442, while Amazon states UPC
  199642944428 for CH0R2AA#ABA — neither code was recorded, per
  the DualSense precedent. The Cloud III S Wireless Black-Red UPC
  198415435569 is verified by two independent non-Amazon sources
  (PBTech retailer listing + trippodo spec database, EAN13
  0198415435569, the same code in GTIN-13 form); the HP datasheet
  for it states the MPN A59Z0AA but no UPC, so the datasheet was
  not counted as a second source. The Haste 2 Pro UPC
  198122802432 (Currys Business UK, single source) and the
  QuadCast 2 S UPC 197961186741 (HP user manual only; every other
  source stating it is Amazon) were NOT recorded, per the strict
  two-source rule — Amazon never corroborates. The Newegg $609.99
  OMEN 27k feed row (65% above the HP direct price) was excluded
  as an unconfirmed outlier (Distritech precedent, batch 21).
- Variant pinning, recorded explicitly: OMEN 27k pins Black
  (780G8AA#ABA) — the only colorway; OMEN OLED 27q pins Black
  (CH0R2AA#ABA) — the only colorway; Cloud III S Wireless pins
  Black-Red (A59Z0AA) — Black (A59YZAA), White (AX6G1AA),
  Black/Blue (DF7E9AA) and White/Pink are different colorways at
  the same $179.99; Pulsefire Haste 2 Pro pins Slate Grey
  (A1KY5AA) — the only colorway listed on the HyperX US store
  (the Haste 2 S Navy/Silver is a different, S model);
  QuadCast 2 S pins Black (9A273AA) — the only colorway (the
  QuadCast 2 Frost is a different mic).
- What does NOT change: the existing 130 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–21 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 135 on
  the next edit (parent owns the cron; not touched here).
- Revisit: both sale prices should be re-checked after the Early
  Black Friday event ends Nov 8 (OMEN OLED 27q $399.99, QuadCast
  2 S $149.99); the OMEN 27k US UPC (no (ABA) code in the HP
  datasheet), the OMEN OLED 27q UPC (conflict 199642944442 vs
  199642944428, needs a tiebreaker such as a physical box barcode
  or a second non-Amazon US source), the Haste 2 Pro UPC
  198122802432 (Currys UK only) and the QuadCast 2 S UPC
  197961186741 (HP manual only) stay pending until a second
  non-Amazon source confirms each; the remaining HP candidates
  (Series 3 Pro 327pf $194.00, E24mv G4 $210.40, E27k G5 $504.00,
  CloudX Flight 2 $139.99, CloudX $59.99, Pulsefire Haste 2
  Wireless $89.99) stay list-only for later batches; the batch 21
  revisits carry over unchanged (OMEN 27s UPC 197029615442,
  Cloud III UPC 197029008237, OMEN 27q G2 US UPC, Alloy Rise 75
  UPC 197192334096, ULT WEAR $148.00, Sony direct CH720N $89.99).

## 045 (2026-11-06): Expansion batch 23 — 135 → 140 models (continuous expansion, DECISIONS 027)

- Decision: add 5 ASUS/ROG models from the ASUS official US store
  sweep (BUILD_LOG 059), no per-batch user approval needed (DECISIONS
  027): ASUS ROG Swift OLED PG27UCWM 27-inch 4K 240Hz Gaming Monitor,
  Black (UPC pending), ASUS ROG Delta II Wireless Gaming Headset,
  Black (90YH03W0-BHAA03, UPC pending), ASUS ROG Gladius IV Ace
  Wireless Gaming Mouse, Black (P729 ROG GLADIUS IV ACE/BLK, UPC
  pending), ASUS ROG Azoth 96 HE Wireless Gaming Keyboard, Black
  (90MP040H-BKAA20, UPC pending), ASUS ROG Cetra Open Wireless
  Gaming Earbuds, Black (90YH0450-BTAA00, UPC pending). One variant
  pinned per model (DECISIONS 015); 0 of 5 identifiers verified,
  all 5 stay pending on single-source, Amazon-only, or conflicting
  codes (Corsair batch 19 precedent: 0 of 5 verified is not a
  reason to hold the batch). Verified-identifier count stays 73.
  No model was split out of this batch. No new category enters the
  set (monitors, headphones, mice, keyboards, earbuds all exist);
  one new brand enters the set: ASUS — the first ASUS entries of
  any kind, one per product family.
- Why these 5: they are the best-evidenced ASUS sweep candidates —
  one per product family where the official US store has a current
  fixed-configuration model: flagship Tandem RGB OLED monitor,
  flagship tri-mode wireless headset, flagship 8K esports mouse,
  flagship Hall-effect keyboard, flagship open-ear gaming earbuds.
  No laptop or desktop pick: ASUS laptops and desktops are
  configurable with no retailer-pinned base configuration
  (DECISIONS 015) — the sweep excluded them rather than forcing
  one. Four of the five are in stock new in the US on 2026-11-06
  (ASUS eShop USA / Best Buy page reads); the PG27UCWM is the
  exception — listed at $1,199.00 at ROG US (Temporarily out of
  stock) and B&H (Coming Soon) — added per the PS5 Pro precedent
  (batch 3: price-verified, stock not confirmed), with the stock
  caveat recorded in the catalog notes and the revisit below.
- What was corrected along the way: the Delta II ASUS direct price
  is $185.99, confirmed on a fresh eShop page read — the Meta
  Catalog feed row at $177.99 is stale and was not used (same
  staleness pattern as batch 22's QuadCast $159.99 read). The
  Azoth 96 HE ASUS direct price is $359.99, confirmed on a fresh
  eShop read with the feed and Newegg agreeing — the sweep's
  $308.99 is superseded (the $305.99 sale row on a rog.asus.com
  helpdesk page is stale/unclear and was not used). ASUS
  identifiers are regional by part-number suffix and were NOT
  carried across suffixes: the Delta II EAN 4711387604847 is for
  90YH03W0-BHUA00 (UK Black), not the US 90YH03W0-BHAA03; the
  Azoth 96 HE EAN 4711636009126 is for 90MP040H-BKDA20 (QWERTZ
  EU) and 4711636009201 for 90MP040H-BKUA20 (UK), not the US
  90MP040H-BKAA20. The Cetra Open Wireless UPC is a genuine
  conflict, not a verification: PBTech and the LittleBit datasheet
  agree on UPC 199291232747 for 90YH0450-BTUA00 (non-US part),
  while Amazon states UPC 199291232754 for the same US model name
  — neither code was recorded, per the DualSense precedent. The
  PG27UCWM UPC 199291335226 is B&H-only (Scan UK lists a different
  regional GTIN, 4711636505857, not a corroboration) and was NOT
  recorded, per the strict two-source rule. The Azoth 96 HE UPC
  199291008571 is Amazon-only (and its listing says ABS keycaps
  vs the eShop's PBT) and was NOT recorded — Amazon never
  corroborates.
- Variant pinning, recorded explicitly: PG27UCWM pins Black —
  the only colorway (Newegg spec: "Black cabinet"); the PG32UCWM
  32-inch ($1,399) and PG27UCDM ($1,099, QD-OLED) are different
  monitors. Delta II pins Black (90YH03W0-BHAA03) — Moonlight
  White (90YH03W0-BHAA10) is a different colorway, and the Delta
  II KJP (90YH04C0-BHAA10, $269.99) is a different, limited-edition
  headset. Gladius IV Ace pins Black (P729 ROG GLADIUS IV
  ACE/BLK) — the only colorway (the Harpe II Ace is a different
  mouse). Azoth 96 HE pins Black (90MP040H-BKAA20) — the Azoth 96
  HE Lite (90MP048H-BKAA00, also $359.99) is a different keyboard.
  Cetra Open Wireless pins Black (90YH0450-BTAA00) — the only
  colorway (the Cetra True Wireless SpeedNova is different
  earbuds).
- What does NOT change: the existing 135 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–22 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 140 on
  the next edit (parent owns the cron; not touched here).
- Revisit: re-check PG27UCWM stock (ROG US / B&H) and the Delta II
  $185.99 sale price after the Early Black Friday event ends Nov 8;
  the five pending UPCs stay pending until a second non-Amazon US
  source confirms each (PG27UCWM 199291335226 — B&H only; Delta II
  US UPC — none surfaced; Gladius IV Ace UPC — none surfaced, no
  90MP part number either; Azoth 96 HE 199291008571 — Amazon-only;
  Cetra Open Wireless — conflict 199291232747 vs 199291232754,
  needs a tiebreaker such as a physical box barcode or a second
  non-Amazon US source); the remaining ASUS candidates (PG32UCWM
  $1,399, PG27AQDPR $899 sale, PG32UCDM Gen3 $1,299, PG27UCDM
  $1,099, XG32UQDS $749, PG34WCDN $1,299, Delta $149.99, Pelta Core
  $119.99, Kithara $259.99 sale, Spatha X 65K $179.99, Harpe Mini
  Core $69.99, Azoth 96 HE Lite $359.99, Strix Morph 96 $115.99
  sale, Strix Scope II 96 RX $132.99 sale, Falchion Ace 75 HE from
  $177.99) stay list-only for later batches; the batch 22 revisits
  carry over unchanged (OMEN OLED 27q UPC conflict, OMEN 27k US
  UPC, Haste 2 Pro UPC 198122802432, QuadCast 2 S UPC
  197961186741, remaining HP candidates, OMEN 27s UPC
  197029615442, Cloud III UPC 197029008237, OMEN 27q G2 US UPC,
  Alloy Rise 75 UPC 197192334096, ULT WEAR $148.00, Sony direct
  CH720N $89.99).

## 046 (2026-11-06): Expansion batch 24 — 140 → 145 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Dell/Alienware models from the Dell held list
  (BUILD_LOG 058/059), no per-batch user approval needed (DECISIONS
  027): Dell 27 Plus 4K Monitor S2725QS, Ash White (T4CNF, UPC
  pending), Dell UltraSharp 32 4K Thunderbolt Hub Monitor U3225QE,
  Silver (3PVPJ, UPC 884116484561 verified), Alienware 32 Curved
  Gaming Monitor AW3225DM, Dark Blue (VX89X, UPC pending),
  Alienware Tri-Mode Wireless Gaming Keyboard AW920K, Dark Side of
  the Moon (6R87M, UPC pending), Dell Pro 7 Webcam 4K WB726, Black
  (G4MYM, UPC pending). One variant pinned per model (DECISIONS
  015); 1 of 5 identifiers verified, the other 4 stay pending on
  single-source, Amazon-only, or non-US-part codes. Verified-
  identifier count 73 → 74. No model was split out of this batch.
  One new category enters the set: "webcams" (WB726 — the first
  webcam of any kind; precedent: "microphones" opened the same way
  in DECISIONS 044). Dell is already in the set (S3225QS, batch
  20); Alienware is already in the set (AW2726DM, Pro Mouse,
  Pro Keyboard, Pro Headset, batch 20); the U3225QE is the first
  UltraSharp in the set.
- Why these 5: they are the best-evidenced Dell held candidates —
  the Dell official US store sweep (BUILD_LOG 058) priced all five
  and the US product pages confirm identity and MPN for each: the
  mainstream 27-inch 4K 120 Hz monitor, the flagship 32-inch 4K
  IPS Black Thunderbolt hub monitor, the budget 32-inch curved QHD
  gaming monitor, Alienware's first tri-mode wireless keyboard,
  and Dell's flagship AI webcam. No laptop or desktop pick: Dell
  laptops and desktops are configurable with no retailer-pinned
  base configuration (DECISIONS 015) — the sweep excluded them
  rather than forcing one. All five are in stock new in the US on
  2026-11-06 (Dell US pages / Best Buy / Target / Adorama reads);
  no stock caveat applies to this batch.
- What was corrected along the way: the S2725QS sweep price
  ~$279.99 is superseded for Dell direct — the $279.99 figures
  traced this round are Amazon prices (BetterBuyBase, Gadget
  Review), excluded per the no-Amazon rule; the Dell feed
  brand_direct row and Newegg both say $299.99, which is the
  recorded Dell price. The U3225QE sweep price $1,099.99 is the
  list price, not the current Dell price — the feed brand_direct
  row says $1,029.99 and Target/Adorama are at ~$799. The AW920K
  pins Dark Side of the Moon (6R87M slug, whose URL and /dsotm/
  image paths name the colorway); the Lunar Light colorway is the
  same $159.99 and is a different colorway, not a different model.
  The WB726 $189.99 figure in Lifewire's September 10 report is
  stale — Dell's current listing is $199.99 (category pages,
  Add to Cart, crawled 2026-11-06). Dell identifiers are regional
  by 5-character part code and were NOT carried across regions:
  the S2725QS US/CA MPN is T4CNF while AU is 8PRJ8, IE/UK is
  V424D and SG/MY is 2M7P9; the U3225QE US MPN is 3PVPJ while UK
  is FPG3K. The U3225QE UPC 884116484561 is verified — B&H Photo
  (UPC 884116484561, MFR # U3225QE) and CompTechDirect (EAN/UPC
  code 5397184923399 0884116484561, MFG # DELL-U3225QE) agree.
  The four pending UPCs were NOT recorded: S2725QS 884116485117
  (Amazon-only, alongside a second code 738060953201 on the same
  listing); AW3225DM EAN 5397184962725 (single Icecat datasheet,
  mirrored by startech24/e-misija/manua.ls — one source family);
  AW920K 884116448686 (single Icecat datasheet for AW920K-W-WW,
  the Lunar Light colorway — not carried across colorways);
  WB726 EAN 5397321028925 (Icecat datasheets for WB726-EMEA, the
  EMEA part — not the US part).
- What does NOT change: the existing 140 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–23 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 145 on
  the next edit (parent owns the cron; not touched here). NOTE:
  the cron's PM refresh (collected 2026-11-06 20:02 UTC, 100
  models) rewrote data/eval_snapshots_2026-11-06.json in the
  working tree during this batch; that file is the cron's work and
  is NOT committed with this batch.
- Revisit: re-check the five sale prices after the Early Black
  Friday event ends Nov 8 (S2725QS $299.99, U3225QE $1,029.99
  Dell / ~$799 street, AW3225DM $249.99 sale, AW920K $159.99,
  WB726 $199.99); the four pending UPCs stay pending until a
  second non-Amazon US source confirms each (S2725QS
  884116485117 — Amazon-only; AW3225DM — no US UPC surfaced, only
  the Icecat EAN 5397184962725; AW920K Dark Side — no UPC
  surfaced, Lunar Light code 884116448686 not carried across;
  WB726 — no US UPC surfaced, only the Icecat EAN 5397321028925
  for the EMEA part); the second Target U3225QE feed row
  $1,028.97 (listing A-1006296976) conflicts with the $799.99
  Target listing and needs a sold-by check next refresh; the
  remaining Dell held candidates (S2725DSM $189.99, S2725HSM
  $159.99, S2425HSM $129.99, SE2426H $89.99, S3225QC $620.41,
  AW3226DM $299.99, AW2726DL $229.99, AW2525HM $249.99, AW2725DM
  $269.99, AW2725QF $499.99, AW3426DWM $399.99, AW3425DWM $349.99,
  AW3926QW $1,099.99, AW2725Q $799.99, AW720M $79.99, AW620M
  $86.99 sale, AW510K $129.99, AW420K $99.99, AW725H $149.99,
  AW920H $109.99, AW520H $79.99, AW320M $69.99, Dell Pro
  Thunderbolt 5 Smart Dock SD25TB5, Dell Premier Wireless ANC
  Headset WL7022 $299.99, Dell Pro Plus Wireless Speakerphone
  SL525) stay list-only for later batches; the batch 23 revisits
  carry over unchanged (PG27UCWM stock + UPC 199291335226,
  Delta II US UPC, Gladius IV Ace UPC, Azoth 96 HE UPC
  199291008571, Cetra Open Wireless UPC conflict 199291232747 vs
  199291232754, remaining ASUS candidates).

## 047 (2026-11-06): Expansion batch 25 — 145 → 150 models (continuous expansion, DECISIONS 027)

- Decision: add 5 ASUS ROG models from the ASUS held list
  (BUILD_LOG 059), no per-batch user approval needed (DECISIONS
  027): ROG Swift OLED PG32UCWM, Black (90LM0DN0-B019B1, UPC
  pending), ROG Swift OLED PG27AQDPR, Black (UPC pending), ROG
  Delta USB-C Gaming Headset, Black (90YH01D1-B2UA00, UPC
  pending), ROG Harpe Mini Core Gaming Mouse, Black
  (90MP04D0-BMAA02, UPC pending), ROG Pelta Gaming Headset, Black
  (90YH0410-BHAA00, UPC pending). One variant pinned per model
  (DECISIONS 015); 0 of 5 identifiers verified, all 5 stay
  pending on single-source, Amazon-only, or non-US-part codes.
  Verified-identifier count stays 74. No model was split out of
  this batch. No new category enters the set (monitors,
  headphones, mice already exist); ASUS is already in the set
  (batch 23: PG27UCWM, Delta II, Gladius IV Ace, Azoth 96 HE,
  Cetra Open Wireless).
- Why these 5: they are the best-evidenced ASUS held candidates
  — the ASUS official US store sweep (BUILD_LOG 059) priced all
  five and the US product pages confirm identity and US part
  number for each (PG32UCWM 90LM0DN0-B019B1, Delta
  90YH01D1-B2UA00, Harpe Mini Core 90MP04D0-BMAA02, Pelta
  90YH0410-BHAA00): the 32-inch Tandem RGB OLED flagship
  monitor, the 500Hz QD-OLED monitor, the original ESS Quad-DAC
  USB-C headset, the 52 g value wired mouse, and the tri-mode
  wireless headset. All five are listed by the ASUS US store on
  2026-11-06; three are in stock at direct (PG32UCWM, Harpe Mini
  Core, Pelta), two carry a stock caveat (PG27AQDPR temporarily
  out of stock at ROG US, Best Buy has stock; Delta out of stock
  at ASUS direct) and were added per the PS5 Pro precedent
  (batch 3: price-verified, stock not confirmed).
- What was corrected along the way: the PG27AQDPR sweep price
  $899.00 "sale, save $170" misreads the ROG US category page —
  $899.00 is the LIST and $729.00 is the sale (save $170.00);
  the feed's $599.00 ROG row for the PG27AQDPR is a
  category-page misassociation (that price belongs to another
  monitor on the same page — the ROG US product page carries no
  offer block on the fresh read) and was not used. The Harpe
  Mini Core sweep price $69.99 is the list — the current ASUS
  price is $44.99 sale (was $59.99). The Pelta sweep price "from
  $84.99" is not corroborated — no $84.99 price appears on any
  fresh read (ROG US $104.99 sale vs $129.99 list, eShop $104.99
  both colorways); the $114.99 feed row for the Black part
  BHAA00 is stale (fresh eShop read $104.99) and was not used.
  The Pelta base tier is pinned Black (90YH0410-BHAA00, $104.99
  sale vs $129.99 list); White (90YH0410-BHAA10, also $104.99)
  is a different colorway, not a different model. ASUS
  identifiers are regional by part suffix and were NOT carried
  across regions: the Harpe Mini Core US part is 90MP04D0-BMAA02
  while JP is 90MP04D0-BMUA00; the Pelta US parts are
  90YH0410-BHAA00 (Black) / BHAA10 (White) while the non-US
  parts are BHUA00 / BHUA10; the Delta US part is
  90YH01D1-B2UA00 while UK is 90YH00Z1-B2UA00. The two
  B&H-only UPCs were NOT recorded: PG32UCWM 199291571570 and
  Harpe Mini Core 199291014046 (each stated by B&H Photo alone,
  same as batch 23's PG27UCWM 199291335226); the Pelta UPC
  199291069725 is stated on a single ASUS datasheet for the
  non-US White part BHUA10 (EAN 4711636069724) and was not
  carried to the US Black part.
- What does NOT change: the existing 145 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–24 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 150 on
  the next edit (parent owns the cron; not touched here). NOTE:
  the working tree at batch start contained a modified
  data/eval_snapshots_2026-11-06.json — the daily refresh cron's
  own file, rewritten by its run; that file is the cron's work and
  is NOT committed with this batch.
- Revisit: re-check the five sale prices after the Early Black
  Friday event ends Nov 8 (PG32UCWM $1,399.00, PG27AQDPR $729.00
  sale vs $899.00 list, Delta $149.99, Harpe Mini Core $44.99
  sale, Pelta $104.99 sale vs $129.99 list); re-check PG27AQDPR
  and Delta stock next refresh; the five pending UPCs stay
  pending until a second non-Amazon US source confirms each
  (PG32UCWM 199291571570 — B&H-only; PG27AQDPR — no UPC
  surfaced; Delta — no US UPC surfaced; Harpe Mini Core
  199291014046 — B&H-only; Pelta — no US UPC surfaced, only
  199291069725 for the non-US White part); the remaining ASUS
  held candidates (PG32UCDM Gen3 $1,299, PG27UCDM $1,099,
  XG32UQDS $749, PG34WCDN $1,299, PG32UCDMR $1,299 Out of Stock,
  Pelta Core $119.99, Kithara $259.99 sale, Spatha X 65K $179.99,
  Azoth 96 HE Lite $359.99, Strix Morph 96 $115.99 sale, Strix
  Scope II 96 RX $132.99 sale, Falchion Ace 75 HE from $177.99)
  stay list-only for later batches; the batch 23/24 revisits
  carry over unchanged (PG27UCWM stock + UPC 199291335226,
  Delta II US UPC, Gladius IV Ace UPC, Azoth 96 HE UPC
  199291008571, Cetra Open Wireless UPC conflict 199291232747 vs
  199291232754, S2725QS UPC 884116485117, AW3225DM EAN
  5397184962725, AW920K UPC 884116448686, WB726 EAN
  5397321028925, second Target U3225QE feed row $1,028.97).

## 048 (2026-11-06): Expansion batch 26 — 150 → 155 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Lenovo tablets from the Lenovo US store sweep
  (BUILD_LOG 065), no per-batch user approval needed (DECISIONS
  027): Lenovo Legion Tab Gen 3 8.8-inch Gaming Tablet, Eclipse
  Black (ZAEF0068US, UPC pending), Lenovo Tab Plus Gen 2 12.1-inch
  Tablet, Celestial White (ZAHT0078US, UPC pending), Lenovo Idea
  Tab Pro Gen 2 13-inch Tablet, Cloud Grey (ZAHD0826US, UPC
  pending), Lenovo Tab One 8.7-inch Tablet, Luna Grey (ZAF00008US,
  UPC pending), Lenovo Yoga Tab Plus Gen 2 13-inch Tablet, Cosmic
  Blue (ZAHX0159US, UPC pending). One variant pinned per model
  (DECISIONS 015); 0 of 5 identifiers verified, all 5 stay
  pending — no UPC surfaced for any of the five part numbers in
  any source read. Verified-identifier count stays 74. No model
  was split out of this batch. No new category enters the set
  ("tablets" already exists — 6 Apple iPads); one new brand
  enters the set: Lenovo — the first Lenovo entries of any kind,
  one per tablet family.
- Why these 5: the Lenovo US store retry succeeded this round
  (the previous round it was unreadable) — the lenovo.com US
  tablets guide page, the Tab series category page, and all five
  US product pages return JSON-LD Product.offers on fresh reads
  2026-11-06 ~21:08 UTC, and the Meta Catalog feed agrees on
  four of the five brand-direct prices. The five are one per
  Lenovo tablet family with a current fixed-configuration US
  part: the 8.8-inch gaming tablet, the speaker-first
  entertainment tablet, the large-screen study tablet, the
  entry-level compact tablet, and the flagship creator tablet.
  No laptop or desktop pick: Lenovo laptops and desktops are
  configurable with no retailer-pinned base configuration
  (DECISIONS 015) — the sweep excluded them rather than forcing
  one. All five are in stock new at Lenovo direct on 2026-11-06
  — no stock caveat on any of them (the first batch with none).
- What was corrected along the way: the Tab Plus Gen 2's earlier
  sale prices are stale — $269.99 (Slickdeals, Sep 29) and
  $289.99/$299.99 (October) no longer hold; the current Lenovo
  direct price is $469.99 on two agreeing reads (fresh page +
  feed), a sharp rise consistent with Lenovo's October US price
  hikes (PhoneArena, Oct 13). Three part-number traps were caught
  and excluded, not priced: the Best Buy Tab One is part
  ZAF00067US (SKU 6621480), not the pinned ZAF00008US — its
  $99.99 Holiday Deal price was NOT used; the Best Buy Tab Plus
  Gen 2 ZAHT0043US is 8GB/256GB, not the pinned 8GB/128GB
  ZAHT0078US; the Best Buy Idea Tab Pro Gen 2 ZAHD0863US
  ($529.99, with Tab Pen Plus) is a different part/bundle from
  the pinned ZAHD0826US. The Idea Tab Pro Gen 2 bundle contents
  are genuinely conflicted — the feed description for ZAHD0826US
  says "Folio case and Pen included" while droidgadgets (Oct 23)
  says this part ships without pen or keyboard — the pin is the
  part number, not the bundle claim. The Legion Tab Gen 3 feed
  carried no direct tablet row at all (only dbrand/m2skins
  accessory rows) — the Lenovo page read is the sole quote and
  the accessory rows were excluded. Lenovo part numbers are
  stated by two independent sources each (Lenovo US page +
  Newegg listing for ZAHT0078US, ZAHD0826US, ZAF00008US;
  Lenovo US page + Slickdeals/NeweggBusiness for ZAHX0159US;
  Lenovo US page + Slickdeals thread for ZAEF0068US), but per
  the catalog's standing precedent (every verified entry carries
  a UPC or EAN; MPN-only verified has never happened) the
  identifiers stay empty until a UPC/EAN is confirmed by two
  independent sources — the MPNs live in the variant strings
  and notes, as in batches 23–25.
- Variant pinning, recorded explicitly: Legion Tab Gen 3 pins
  Eclipse Black (ZAEF0068US) — the only colorway; the FIFA World
  Cup 26 Edition (ZAEF0096US, White, $569.99) is a different,
  limited-edition tablet and the Legion Tab Gen 5 ($899.99 list /
  $699.99 sale) is a different, newer tablet. Tab Plus Gen 2 pins
  Celestial White (ZAHT0078US, 8GB/128GB) — the only US config
  (North America gets 8GB/128GB only per Notebookcheck); the
  8GB/256GB ZAHT0043US is a different config. Idea Tab Pro Gen 2
  pins Cloud Grey (ZAHD0826US, 8GB/128GB) — the only US config
  listed at Lenovo direct; the 256GB ZAHC part is a different
  config. Tab One pins Luna Grey (ZAF00008US, 4GB/64GB) — the
  only colorway; the LTE 128GB is a different config. Yoga Tab
  Plus Gen 2 pins Cosmic Blue (ZAHX0159US, 12GB/256GB) — the US
  base config with keyboard + Tab Pen Pro 2 included; the 16GB /
  512GB configs are different configs, and the Yoga Tab Plus Gen
  1 (12.7-inch, Snapdragon 8 Gen 3) is a different tablet.
- What does NOT change: the existing 150 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–25 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron still
  says "57 models" in its body and needs a count update to 155 on
  the next edit (parent owns the cron; not touched here).
- Revisit: re-check the five sale prices after the Early Black
  Friday event ends Nov 8 (Legion Tab Gen 3 $549.99, Tab Plus Gen
  2 $469.99, Idea Tab Pro Gen 2 $399.99 sale vs $549.99 list, Tab
  One $149.99 sale vs $199.99 est. value, Yoga Tab Plus Gen 2
  $799.99 sale vs $999.99 list); re-check the Tab Plus Gen 2
  $469.99 price next refresh (the Sep–Oct $269.99–$299.99 sale
  prices vs the current $469.99 is the sharpest move in this
  batch); re-check the Idea Tab Pro Gen 2 ZAHD0826US bundle
  contents (folio case + pen included or not); the five pending
  UPCs stay pending until a second non-Amazon US source confirms
  each (no UPC surfaced for any of the five part numbers —
  ZAEF0068US, ZAHT0078US, ZAHD0826US, ZAF00008US, ZAHX0159US);
  the remaining Lenovo candidates (Legion Tab Gen 5 $899.99 list /
  $699.99 sale, Yoga Tab Gen 2 $729.99, Idea Tab $229.99 4GB /
  $289.99 8GB, Idea Tab Plus $339.99, Tab P12) stay list-only for
  later batches; the batch 25 revisits carry over unchanged
  (PG32UCWM stock + UPC 199291571570, PG27AQDPR stock + UPC,
  Delta US UPC, Harpe Mini Core UPC 199291014046, Pelta US UPC,
  PG27UCWM stock + UPC 199291335226, Delta II US UPC, Gladius IV
  Ace UPC, Azoth 96 HE UPC 199291008571, Cetra Open Wireless UPC
  conflict 199291232747 vs 199291232754, S2725QS UPC 884116485117,
  AW3225DM EAN 5397184962725, AW920K UPC 884116448686, WB726 EAN
  5397321028925, second Target U3225QE feed row $1,028.97).

## 049 (2026-11-06): Expansion batch 27 — 155 → 160 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Microsoft models from the Microsoft US store
  sweep (BUILD_LOG 066), no per-batch user approval needed
  (DECISIONS 027): Xbox Series X 1TB Disc Edition, Black
  (RRT-00001, UPC 889842640724 — verified), Xbox Series S 512GB
  All-Digital, Robot White (UPC pending — conflicting part
  numbers), Xbox Wireless Headset, 2024 refresh, Black ($110.99,
  identifiers pending — no MPN/UPC surfaced), Xbox Stereo
  Headset, Black (8LI-00001, UPC 889842748031 — verified),
  Surface Laptop, 13.8-inch (8th Edition), Snapdragon X2 Plus
  10-core / 16GB / 512GB, Platinum (EP2-59028, identifiers
  pending — MPN single AU source only). One variant pinned per
  model (DECISIONS 015); 2 of 5 identifiers verified, 3 stay
  pending. Verified-identifier count rises 74 → 76. No model
  was split out of this batch. No new category enters the set
  ("consoles" already exists — 9 PS5/Switch entries; "headphones"
  and "laptops" already exist); the Xbox consoles are the first
  Microsoft entries in "consoles", and the Surface Laptop is the
  first Microsoft entry in "laptops" and the set's first Surface
  device of any kind. Microsoft was already in the set (4 Xbox
  controllers); this batch takes it to 9 entries.
- Why these 5: the Microsoft US store pages all return JSON-LD
  Product.offers on fresh reads 2026-11-06 ~21:13–21:14 UTC, and
  the Meta Catalog feed agrees on the Wireless Headset price and
  carries $499.99 Series S rows. The five are one per Microsoft
  hardware family with a current fixed US configuration: the
  flagship disc console, the entry all-digital console, the
  wireless headset (2024 refresh), the wired headset, and the
  current Surface Laptop base config. The Surface base config
  pinned cleanly — the 13.8-inch 8th Edition's US entry config
  is X2 Plus 10-core / 16GB / 512GB / Platinum (pcdepo confirms
  the entry config; 512GB is the storage minimum), at $1,299.99
  sale vs $1,599.99 list at Microsoft direct. All five are
  listed new at Microsoft direct on 2026-11-06; stock is not
  confirmed on any of the five Microsoft pages (see caveats).
- What was corrected along the way: the Wireless Headset's
  $99.99 feed row is the stale 2021-model price — the current
  2024-refresh Microsoft direct price is $110.99 on two agreeing
  fresh JSON-LD crawls, $1 above the $109.99 launch price
  (Notebookcheck / Xbox Wire Oct 2024). The Stereo Headset's
  $79.99/$74.99 feed rows are third-party inflated — Microsoft
  direct and Verizon agree at $59.99, unchanged since the Sep
  2021 launch. The Series X price is $799.99 list, not a sale:
  Microsoft raised US Xbox prices Aug 1, 2026 (disc $649.99 to
  $799.99, Digital $599.99 to $749.99; Xbox Wire Jun 25, 2026).
  The Surface Laptop's $1,399.99 "starting at" in older crawls
  is a $200-off sale that has deepened to $300 off — the pinned
  config is $1,299.99 sale vs $1,599.99 list, and Best Buy's
  $1,199.99 (reg $1,600, 9to5Toys Nov 2) is reported, not
  page-verified. Three identifier traps were caught and
  excluded, not priced: the Series S part numbers conflict
  (Micro Center EP2-10050 / UPC 196388421343 vs eBay RRS-00001
  / UPC 0889842651317 vs Amazon's unattributed 889842640731 vs
  PBTech NZ EP2-10071 / UPC 196388421541) — nothing copied;
  the 2021 Wireless Headset's TLL-00001 code was not copied to
  the 2024 refresh; the Stereo Headset's second eBay UPC
  499007320363 conflicts with the agreed 889842748031 and was
  excluded.
- Variant pinning, recorded explicitly: Series X pins the 1TB
  Disc Edition in Black (RRT-00001) — the Digital Edition in
  White ($749.99, no disc drive) is a different console, as are
  the 2TB Galaxy Black Special Edition (sunset Aug 2026) and the
  Series X25 Limited Edition ($899.99, launches Nov 13). Series
  S pins the 512GB Robot White — the 1TB Robot White ($599.99)
  and 1TB Carbon Black are different storage/color configs.
  Wireless Headset pins the 2024 refresh in Black — the Starfield
  Limited Edition ($250.79) and Forza Horizon 6 Limited Edition
  ($134.99) are different headsets. Stereo Headset pins Black
  (8LI-00001), the only colorway — the 20th Anniversary Special
  Edition is a different headset. Surface Laptop pins the 8th
  Edition 13.8-inch base, X2 Plus 10-core / 16GB / 512GB /
  Platinum (EP2-59028) — the X2 Elite 12-core, 32GB/64GB and 1TB
  configs, the 15-inch 8th Edition and the 7th Edition are
  different configs/models, and the 256GB EP2-77788 is the
  smaller 13-inch Surface Laptop, a different model.
- What does NOT change: the existing 155 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6 Pro
  untouched, batches 1–26 entries untouched). No other snapshot
  file is rewritten. No Amazon touch. The daily refresh cron
  still says "57 models" in its body and needs a count update to
  160 on the next edit (parent owns the cron; not touched here).
- Revisit: re-check Series X stock next refresh (Micro Center
  and ShopCGX both OutOfStock for RRT-00001; Microsoft page
  states no stock flag); re-check the Wireless Headset $110.99
  price ($1 above the $109.99 launch); re-check the Surface
  Laptop $1,299.99 sale price after Black Friday (Nov 27); the
  three pending identifiers stay pending until two independent
  US sources confirm each (Series S part-number conflict,
  Wireless Headset 2024 refresh MPN/UPC, Surface Laptop
  EP2-59028 US confirmation + UPC); the remaining Microsoft
  candidates stay list-only for later batches (Surface Slim Pen
  2 $129.99 — MPN 8WV-00001 vs 8WX-00001 conflict; Xbox
  Rechargeable Battery + USB-C Cable SXW-00001 $24.99 — UPC
  889842590364 single source; Surface Pro 11th Edition — base
  config price not pinned cleanly; Xbox Series X25 Limited
  Edition $899.99 — launches Nov 13); the batch 26 revisits
  carry over unchanged (five Lenovo sale prices after Early
  Black Friday ends Nov 8; Tab Plus Gen 2 $469.99; Idea Tab Pro
  Gen 2 bundle contents; five pending Lenovo UPCs; remaining
  Lenovo candidates list-only).

## 050 (2026-11-06): Expansion batch 28 — 160 → 165 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Garmin models from the Garmin US store
  sweep (BUILD_LOG 067), no per-batch user approval needed
  (DECISIONS 027): vívoactive 6, Slate with Black silicone
  band (010-02985-00, UPC 753759342807 — verified), Venu 4
  45mm, Silver stainless steel bezel with Silver Gray
  silicone band (010-03014-01, UPC 753759342883 —
  verified), Forerunner 570 42mm, Raspberry Aluminum with
  Translucent Bone/Mango band (010-02970-02, UPC
  753759349820 — verified), Edge 1050 cycling computer,
  device only, Black (010-02890-00, UPC 753759336288 —
  verified), fēnix 9 47mm, Titanium with Pebble Gray
  silicone band (010-04762-00, identifiers pending — no UPC
  surfaced). One variant pinned per model (DECISIONS 015);
  4 of 5 identifiers verified, 1 stays pending.
  Verified-identifier count rises 76 → 80. Garmin is a new
  brand in the set (0 → 5 entries); "cycling-computers" is
  a new category (Edge 1050 is its first entry); the four
  watches join "wearables" (3 → 7 entries).
- Why these 5: the Garmin US store pages all return JSON-LD
  Product.offers on fresh reads 2026-11-06 ~21:21 UTC, and
  the Meta Catalog feed agrees on every price. The five are
  one per current Garmin hardware family with a fixed US
  configuration: the entry fitness watch, the lifestyle
  flagship, the mid-range running watch, the premium cycling
  computer, and the flagship multisport watch. All five are
  listed new at Garmin direct on 2026-11-06; stock is not
  confirmed on any of the five Garmin pages except the
  vívoactive 6, which Dell shows Temporarily Out of Stock
  (see caveats).
- What was corrected along the way: the Venu 4's $599.99
  feed rows are the leather-band variant (010-03014-03),
  not the pinned silicone variant — the pinned variant is
  $549.99 at Garmin direct, with a Dell $499.99 sale row
  (early Black Friday, suspected). The Forerunner 570's
  47mm size is a different size at the same $549.99, and a
  $563 third-party row was excluded. The Edge 1050's
  $713.99 Best Buy rows are the sensor bundle
  (010-02890-01, different MPN/EAN), not the device-only
  010-02890-00 at $699.99. The fēnix 9's $1,049.99 rows are
  the Carbon Gray DLC Titanium variant (010-04762-10) and
  the $1,099.99+ rows are the Pro lines — the pinned base
  fēnix 9 is $999.99 at Garmin direct, Abt and NFM. Two
  identifier traps were caught and excluded, not priced:
  the Forerunner 970's UPC is conflicted across variants
  (-00: Amazon + Snapklik 753759349929 vs a single eBay
  listing 753759349899; -01: Abt 753759349905 vs Snapklik
  753759349936) — nothing copied, the 970 stays list-only
  for a dedicated tiebreak; the Edge 1050 bundle's EAN
  0753759336295 (010-02890-01) was not copied onto the
  device-only 010-02890-00.
- Variant pinning, recorded explicitly: vívoactive 6 pins
  Slate/Black (010-02985-00) — the Lunar Gold/Bone
  (010-02985-01), Metallic Jasper Green (010-02985-02) and
  Pink Dawn (010-02985-03) colorways are different variants,
  as is the vívoactive 5 (previous generation). Venu 4 pins
  the 45mm Silver/Silver Gray silicone (010-03014-01) — the
  41mm is a different size at the same $549.99, and the
  Slate/Black silicone (010-03014-00), Silver/Citron
  (010-03014-02) and Slate/Black + Brown leather
  (010-03014-03, $599.99) are different variants.
  Forerunner 570 pins the 42mm Raspberry (010-02970-02) —
  the 47mm is a different size at the same $549.99, and the
  Slate Gray (010-02970-00) and Cloud Blue (010-02970-01)
  are different colorways. Edge 1050 pins the device-only
  010-02890-00 — the 010-02890-01 sensor bundle is a
  different SKU, as is the Edge 1040 Solar (previous
  generation). fēnix 9 pins the 47mm base Titanium/Pebble
  Gray (010-04762-00) — the 43mm and 51mm are different
  sizes, the Carbon Gray DLC Titanium (010-04762-10,
  $1,049.99) is a different variant, and the fēnix 9 Pro
  lines ($1,099.99+, full titanium case and/or inReach /
  solar) are different models.
- What does NOT change: the existing 160 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6
  Pro untouched, batches 1–27 entries untouched). No other
  snapshot file is rewritten. No Amazon touch in the
  snapshot: no Amazon quotes, no Amazon-sourced prices or
  identifiers (Amazon item details were read only as a third
  corroboration for the Forerunner 570 UPC, which is
  verified on Target US + Selenal.lv without it). The daily
  refresh cron still says "57 models" in its body and needs
  a count update to 165 on the next edit (parent owns the
  cron; not touched here).
- Revisit: re-check the fēnix 9 UPC next refresh (MPN
  010-04762-00 confirmed, no UPC surfaced — ten-week-old
  model, retailer UPC fields still blank); re-check the
  Venu 4 Dell $499.99 sale price after Black Friday (Nov
  27); re-check vívoactive 6 stock (Dell Temporarily Out of
  Stock); tiebreak the Forerunner 970 UPC conflict (Best
  Buy specs or a box barcode) before adding the 970; the
  remaining Garmin candidates stay list-only for later
  batches (Edge 1060 $799.99 — launched Oct 20, 2026, too
  new for UPC verification; Fenix 8 47mm AMOLED —
  superseded by the fēnix 9, now discounted last-gen;
  Instinct 3, Forerunner 165, Edge 850, Garmin dash cams —
  not yet swept); the batch 27 revisits carry over
  unchanged (Series X stock; Wireless Headset $110.99;
  Surface Laptop $1,299.99 sale after Black Friday; three
  pending Microsoft identifiers; remaining Microsoft
  candidates list-only) and the batch 26 revisits carry
  over unchanged (five Lenovo sale prices after Early Black
  Friday ends Nov 8; Tab Plus Gen 2 $469.99; Idea Tab Pro
  Gen 2 bundle contents; five pending Lenovo UPCs;
  remaining Lenovo candidates list-only).

## 051 (2026-11-06): Expansion batch 29 — 165 → 170 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models from the Lenovo US store sweep plus
  one ASUS held candidate (BUILD_LOG 068), no per-batch user
  approval needed (DECISIONS 027): Lenovo Legion Tab Gen 5
  8.8-inch Gaming Tablet, Eclipse Black (ZAH20126US, UPC
  199275342448 — verified), Lenovo Yoga Tab Gen 2 11.1-inch
  Tablet, Cosmic Blue (ZAJ00250US, UPC pending), Lenovo Idea
  Tab 11-inch Tablet, Luna Grey (ZAFR0923US, UPC pending),
  Lenovo Idea Tab Plus 12.1-inch Tablet, Cloud Grey
  (ZAG71084US, UPC pending), ASUS ROG Swift OLED PG27UCDM
  27-inch 4K 240Hz Gaming Monitor, Black (90LM0B30-B019B2,
  UPC pending). One variant pinned per model (DECISIONS 015);
  1 of 5 identifiers verified, 4 stay pending.
  Verified-identifier count rises 80 → 81. No new brand enters
  the set (Lenovo 5 → 9 entries, ASUS 10 → 11 entries); no new
  category enters the set ("tablets" 11 → 15 entries,
  "monitors" 12 → 13 entries).
- Why these 5: four of the five batch 26 list-only Lenovo
  tablets pin cleanly on fresh Lenovo US page reads
  2026-11-06 ~21:26 UTC, with the Meta Catalog feed agreeing
  on every brand-direct price; the fifth Lenovo candidate
  (Tab P12) is gone from Lenovo US, so the batch is filled
  from the ASUS held list (DECISIONS 047) with the PG27UCDM —
  the 27-inch 4K Tandem QD-OLED flagship, verified on a fresh
  ASUS eShop USA page read 2026-11-06 ~21:29 UTC with Newegg
  agreeing at the same $1,099. All five are in stock new at
  brand direct on 2026-11-06 — no stock caveat on any of
  them. No laptop or desktop pick: Lenovo laptops and desktops
  are configurable with no retailer-pinned base configuration
  (DECISIONS 015).
- What was corrected along the way: the Legion Tab Gen 5's
  $598.49 Slickdeals price is a coupon stack (two eCoupons),
  not a clean sale price — the clean prices are Lenovo
  $699.99 sale vs $899.99 list and B&H $799.99 sale vs
  $899.99 list; the $849.99 launch list rose to $899.99 in
  October (PhoneArena Oct 13), so the $679.99/$680 September
  sale prices are stale. The Yoga Tab Gen 2's ~$582
  Notebookcheck price (Oct 24) is stale vs the current
  $599.99. The Idea Tab Plus's $339.99 PhoneArena figure
  (Oct 13) was the 8GB config — the current Lenovo-direct
  part is the 6GB ZAG71084US at $369.99. The PG27UCDM's $949
  ROG row and $1,199 shop.asus.com row are stale /
  other-storefront vs the $1,099 eShop + ROG page + Newegg
  agreement. Three part-number traps were caught and
  excluded, not priced: the Idea Tab's Amazon UPCs belong to
  different parts (ZAFR0920US 199271882283, ZAFR0928US
  199271888728, ZAFR0925US 199271882306 — none is the pinned
  ZAFR0923US); the Staples Idea Tab ZAFR0912US ($269.99) is a
  different part at the same price; the Idea Tab Plus 8GB
  parts (ZAG70917US, ZAG70921US, ZAG70922US) are different
  parts from the pinned 6GB ZAG71084US. The PG27UCDM
  candidate UPC 197105815193 was NOT recorded: it is tied to
  the EU part 90LM0B30-B01971 in the ASUS brochure (with EAN
  4711387815236) and to PG27UCDM generally on Tanotis/eBay/
  Ubuy, but no source ties it to the US part 90LM0B30-B019B2
  — the same call as batch 25's PG32UCWM. The Harpe Mini
  Core was nearly re-added as the fill and caught by the
  membership check: it is already in the set as
  asus-rog-harpe-mini-core-black (batch 25).
- Variant pinning, recorded explicitly: Legion Tab Gen 5 pins
  Eclipse Black (ZAH20126US) — the only US colorway
  (Notebookcheck); the FIFA World Cup 26 Edition
  (ZAEF0096US, White, $569.99) is a different, limited-
  edition tablet and the Glacier White / Surge green
  colorways are not sold in the US. Yoga Tab Gen 2 pins
  Cosmic Blue (ZAJ00250US, 8GB/256GB) — the only US config
  listed at Lenovo direct (droidgadgets); the 12GB/256GB
  configs are different configs. Idea Tab pins Luna Grey
  (ZAFR0923US, 4GB/128GB) — the $269.99 4GB tier
  (PhoneArena Oct 26); the 8GB ZAFR0928US ($339.99, with
  pen) is a different part. Idea Tab Plus pins Cloud Grey
  (ZAG71084US, 6GB/128GB) — the current Lenovo-direct part;
  the 8GB and 12GB parts are different parts. PG27UCDM pins
  Black (90LM0B30-B019B2) — the US eShop part; the EU part
  90LM0B30-B01971 is a different regional part, as is the
  PG27UCDMR ($1,299, Out of Stock).
- What does NOT change: the existing 165 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6
  Pro untouched, batches 1–28 entries untouched). No other
  snapshot file is rewritten. No Amazon touch in the
  snapshot: no Amazon quotes, no Amazon-sourced prices or
  identifiers (Amazon item details were read only to confirm
  which Idea Tab part numbers they do NOT cover). The daily
  refresh cron still says "57 models" in its body and needs
  a count update to 170 on the next edit (parent owns the
  cron; not touched here).
- Revisit: re-check the four Lenovo sale prices after the
  Early Black Friday event ends Nov 8 (Legion Tab Gen 5
  $699.99, Yoga Tab Gen 2 $599.99, Idea Tab $269.99, Idea Tab
  Plus $369.99); re-check the Idea Tab $269.99 price next
  refresh (third rise in 2026) and the Idea Tab Plus $369.99
  price (6GB part vs the earlier 8GB $339.99 reports);
  re-check the four pending Lenovo/ASUS UPCs (ZAJ00250US,
  ZAFR0923US, ZAG71084US, PG27UCDM 90LM0B30-B019B2 — the
  197105815193 candidate needs a US-part tie); the remaining
  candidates stay list-only for later batches (Lenovo Yoga
  Tab Gen 1 ZAG60266US $659.99 — superseded by the Yoga Tab
  Gen 2, excluded per the batch 28 Fenix 8 precedent;
  ThinkPad Universal USB-C Dock 40AY0090US — no Lenovo US
  direct price surfaced, reseller prices $148.99–$309
  conflict; Alienware AW720M $79.99 — 2022 mouse, Dell US
  direct price unconfirmed, no UPC; ASUS ROG Delta original
  — no current ASUS row; remaining ASUS held candidates
  PG32UCDM Gen3 $1,299, PG34WCDN $1,299, PG32UCDMR $1,299
  Out of Stock, Pelta Core $119.99, Kithara $259.99 sale,
  Spatha X 65K $179.99, Azoth 96 HE Lite $359.99, Strix
  Morph 96 $115.99 sale, Strix Scope II 96 RX $132.99 sale,
  Falchion Ace 75 HE from $177.99; remaining HP candidates
  Series 3 Pro 327pf $194.00, E24mv G4 $210.40, E27k G5
  $504.00, CloudX Flight 2 $139.99, CloudX $59.99, Pulsefire
  Haste 2 Wireless $89.99; remaining Dell candidates
  AW3226DM $299.99, AW2726DL $229.99, AW2525HM $249.99,
  AW2725DM $269.99, AW2725QF $499.99, AW3426DWM $399.99,
  AW3425DWM $349.99, AW3926QW $1,099.99, AW2725Q $799.99,
  AW620M $86.99 sale, AW510K $129.99, AW420K $99.99, AW725H
  $149.99, AW920H $109.99, AW520H $79.99, AW320M $69.99, Dell
  Pro Thunderbolt 5 Smart Dock SD25TB5, Dell Premier Wireless
  ANC Headset WL7022 $299.99, Dell Pro Plus Wireless
  Speakerphone SL525); the batch 28 revisits carry over
  unchanged (fēnix 9 UPC; Venu 4 Dell $499.99 sale after
  Black Friday Nov 27; vívoactive 6 stock; Forerunner 970
  UPC tiebreak; Edge 1060 UPC; remaining Garmin candidates
  list-only) and the batch 27 revisits carry over unchanged
  (Series X stock; Wireless Headset $110.99; Surface Laptop
  $1,299.99 sale after Black Friday; three pending Microsoft
  identifiers; remaining Microsoft candidates list-only) and
  the batch 26 revisits carry over unchanged (five Lenovo
  sale prices after Early Black Friday ends Nov 8; Tab Plus
  Gen 2 $469.99; Idea Tab Pro Gen 2 bundle contents; five
  pending Lenovo UPCs).

## 052 (2026-11-06): Expansion batch 30 — 170 → 175 models (continuous expansion, DECISIONS 027)

- Decision: add 5 Samsung models from the Samsung US store sweep
  (BUILD_LOG 069), no per-batch user approval needed (DECISIONS
  027): Galaxy Watch9 40mm Bluetooth, Graphite (SM-L340NZKAXAA,
  UPC pending), Galaxy Watch8 Classic 46mm Wi-Fi/Bluetooth, Black
  (SM-L500NZKAXAA, UPC 198957093562 — verified), Galaxy Watch
  Ultra2 47mm LTE, Titanium Silver (SM-L715UZSAXAA, UPC
  198957393730 — verified), Galaxy Tab S11 11-inch 128GB Wi-Fi,
  Gray (SM-X730NZAAXAR, UPC pending), Galaxy Tab S10 FE 10.9-inch
  128GB Wi-Fi, Gray (SM-X520NZAAXAR, UPC 887276992266 — verified).
  One variant pinned per model (DECISIONS 015); 3 of 5 identifiers
  verified, 2 stay pending. Verified-identifier count rises
  81 → 84. Samsung is already in the set (3 Buds entries) and
  grows 3 → 8 entries; no new brand enters the set. No new
  category enters the set ("wearables" 10 → 13 entries,
  "tablets" 15 → 17 entries). No phones and no TVs were added —
  both would open new categories, out of scope for this batch
  (DECISIONS 016).
- Why these 5: they are the current Samsung US catalog lines in
  the three in-scope categories with clean brand-direct pins —
  the Watch9 (Aug 2026 flagship, $379.99) and Ultra2 (Jul 2026
  rugged flagship, $699.99) are the two newest Samsung watches,
  the Watch8 Classic ($499.99) is the still-current Classic (no
  Watch9 Classic exists), and the Tab S11 ($999.99) and Tab S10
  FE ($549.99) are the current flagship and FE tablets. All five
  are in stock new at Samsung US on 2026-11-06 (buy-page JSON-LD
  InStock reads) with Best Buy agreeing on every price.
- What was corrected along the way: the $299.99 / $349.99 Watch9
  figures in older coverage are Watch8 prices, not Watch9 (the
  Watch9 launched Aug 7, 2026 at $379.99, $30 above the Watch8);
  the Tab S11 $799.99 launch price rose to $899.99 (Apr 2026)
  and $999.99 now, and the $659 sale price is an Amazon-only
  deal (excluded, no Amazon touch); the Tab S10 FE $499.99 MSRP
  (Samsung's May 2026 list) is stale vs the current $549.99 at
  Samsung US and Best Buy; the Watch8 Classic $419.99 reported
  Sep 24 looks like an ended sale vs the fresh $499.99 page read;
  the feed's Best Buy Watch9 $409.26 and Ultra2 $737.52 rows both
  conflict with fresh Best Buy page reads ($379.99 / $699.99)
  and were excluded as stale; the feed's Tab S11 Silver sale
  $899.99 is a feed-only figure vs the $999.99 page read. Three
  part-number traps were caught and excluded, not priced: the
  Tab S11 bundle UPCs 810210911580 / 810210913805 belong to the
  Canada part SM-X730NZAAXAC with an SD card; the Tab S11
  Enterprise 128GB (SM-X730NZAAN20, UPC 198957257360) and 256GB
  Gray (SM-X730NZAEXAR, UPC 198957230189) are different parts
  from the pinned consumer 128GB Gray; the Target Tab S10 FE
  $449.99 / $394.99 row is a "Global Model" (non-US, DECISIONS
  021).
- Variant pinning, recorded explicitly: Watch9 pins Graphite
  40mm Bluetooth (SM-L340NZKAXAA) — the entry Bluetooth config;
  44mm (SM-L350NZKAXAA, $409.99) and LTE (SM-L345UZKAXAA,
  $429.99) are different SKUs, as is Cream (SM-L340NZEAXAA).
  Watch8 Classic pins Black 46mm Wi-Fi/Bluetooth
  (SM-L500NZKAXAA) — the only size (46mm), Bluetooth tier; LTE
  (SM-L505UZKAXAA, $549.99) and White (SM-L500NZWAXAA) are
  different SKUs. Watch Ultra2 pins Titanium Silver 47mm LTE
  (SM-L715UZSAXAA) — LTE is the only connectivity tier for the
  Ultra2; Titanium Gray (SM-L715UZKAXAA) is a different color.
  Tab S11 pins Gray 128GB Wi-Fi (SM-X730NZAAXAR) — the entry
  storage tier; 256GB ($1,099.99) and 512GB ($1,299.99) are
  different SKUs, as is Silver (SM-X730NZSAXAR). Tab S10 FE pins
  Gray 128GB Wi-Fi (SM-X520NZAAXAR) — the entry tier; 5G
  (SM-X528UZAA, $685.99) and 256GB (SM-X520NZAEXAR, $589.99
  MSRP) are different SKUs, as is the FE+ 13.1-inch
  (SM-X620NZAAXAR).
- What does NOT change: the existing 170 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6
  Pro untouched, batches 1–29 entries untouched). No other
  snapshot file is rewritten. No Amazon touch in the snapshot:
  no Amazon quotes, no Amazon-sourced prices or identifiers
  (the $659 Amazon-only Tab S11 deal was read only to confirm
  it is Amazon-only, and was not used). The daily refresh cron
  still says "57 models" in its body and needs a count update
  to 175 on the next edit (parent owns the cron; not touched
  here).
- Revisit: re-check the two pending UPCs (Watch9 SM-L340NZKAXAA
  — candidate 198957310546 needs a second independent source;
  Tab S11 SM-X730NZAAXAR — no UPC surfaced at all); re-check
  the Watch8 Classic $499.99 price (vs the Sep 24 $419.99
  report) and the Tab S10 FE $549.99 price (vs the $499.99 MSRP
  list) next refresh; the remaining Samsung candidates stay
  list-only for later batches (Galaxy Tab S11 Ultra 256GB Gray
  SM-X930NZAAXAR, UPC 198957230080, $1,199.99; Galaxy Tab A11+
  128GB Gray SM-X230NZAIXAR, UPC 198957270390, $249.99 MSRP;
  Galaxy Tab S10 FE+ 13.1-inch Gray SM-X620NZAAXAR, UPC
  887276992563, $649.99 MSRP; Galaxy Watch8 40mm — superseded
  by the Watch9; Galaxy Buds3 Pro — out of the Samsung US
  catalog; Galaxy Buds Core — not sold in the US); the batch 29
  revisits carry over unchanged (four Lenovo sale prices after
  the Early Black Friday event ends Nov 8; four pending
  Lenovo/ASUS UPCs) and the batch 28 revisits carry over
  unchanged (fēnix 9 UPC; Venu 4 Dell $499.99 sale after Black
  Friday Nov 27; vívoactive 6 stock; Forerunner 970 UPC
  tiebreak; Edge 1060 UPC; remaining Garmin candidates
  list-only) and the batch 27 revisits carry over unchanged
  (Series X stock; Wireless Headset $110.99; Surface Laptop
  $1,299.99 sale after Black Friday; three pending Microsoft
  identifiers; remaining Microsoft candidates list-only) and
  the batch 26 revisits carry over unchanged (five Lenovo sale
  prices after Early Black Friday ends Nov 8; Tab Plus Gen 2
  $469.99; Idea Tab Pro Gen 2 bundle contents; five pending
  Lenovo UPCs).

## 053 (2026-11-06): Expansion batch 31 — 175 → 180 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models (BUILD_LOG 070), no per-batch user approval
  needed (DECISIONS 027): the Samsung tablet sweep completed —
  Galaxy Tab S11 Ultra 14.6-inch 256GB Wi-Fi, Gray
  (SM-X930NZAAXAR, UPC pending), Galaxy Tab A11+ 11-inch 128GB
  Wi-Fi, Gray (SM-X230NZAIXAR, UPC 198957270390 — verified),
  Galaxy Tab S10 FE+ 13.1-inch 128GB Wi-Fi, Gray (SM-X620NZAAXAR,
  UPC 887276992563 — verified) — plus 2 Garmin substitutes from
  the batch 28 list-only pool, because the remaining Samsung
  candidates all failed the current-catalog test (see below):
  Garmin Forerunner 165 43mm, Black/Slate Gray, non-Music
  (010-02863-20, UPC 753759326593 — verified) and Garmin Edge 850
  (010-03023-00, UPC 753759356644 — verified). One variant pinned
  per model (DECISIONS 015); 4 of 5 identifiers verified, 1 stays
  pending. Verified-identifier count rises 84 → 88. Samsung
  grows 8 → 11 entries, Garmin 5 → 7; no new brand enters the
  set. Category counts: "tablets" 17 → 20, "wearables" 10 → 11,
  "cycling-computers" 1 → 2. No phones and no TVs were added —
  both would open new categories, out of scope for this batch
  (DECISIONS 016).
- Why these 5: the three tablets are the last three Samsung US
  current-catalog tablets not yet in the set — the S11 Ultra is
  the flagship 14.6-inch tablet ($1,299.99), the A11+ is the
  entry-level 11-inch tablet ($299.99) and the S10 FE+ is the
  big-screen FE tablet ($699.99); all three are in stock new at
  Samsung US on 2026-11-06 (buy-page JSON-LD InStock reads) with
  Best Buy agreeing on every price. The two Garmin substitutes
  are the cleanest remaining Garmin candidates: the Forerunner
  165 ($249.99) is Garmin's entry-level AMOLED running watch and
  the Edge 850 ($599.99) is the compact mid-tier Edge — both
  single-SKU pins with two-source UPCs, both still current (the
  165 launched Feb 2024, the 850 launched Sep 9, 2025).
- What was corrected along the way: all three tablet MSRPs are
  stale vs current street prices — the S11 Ultra $1,199.99 MSRP
  (Samsung's May 2026 list) vs the current $1,299.99 at Samsung
  US and Best Buy; the A11+ $249.99 MSRP (Dec 2025 / May 2026
  lists; NotebookCheck's Jan 2026 launch coverage) vs the
  current $299.99; the S10 FE+ $649.99 MSRP (May 2026 list) vs
  the current $699.99. The Forerunner 165 base Black/Slate Gray
  MPN is 010-02863-20, not 010-02863-00 (the -00 suffix does not
  exist for this line; the -20 was confirmed by Garmin's own
  product URL, Running Warehouse, Focus Camera and P.C.
  Richard). The feed's Quill S11 Ultra $1,281.99 row is stale vs
  the fresh $1,320.99 page read (out of stock); the feed's
  antonline S10 FE+ marketplace rows and the shopabunda $540
  "International Model" row were excluded (DECISIONS 021).
- Variant pinning, recorded explicitly: Tab S11 Ultra pins Gray
  256GB Wi-Fi (SM-X930NZAAXAR) — the entry storage tier; 512GB
  (SM-X930NZAEXAR, $1,399.99 MSRP) and 1TB Silver
  (SM-X930NZSIXAR, $1,899.99) are different SKUs. Tab A11+ pins
  Gray 128GB Wi-Fi (SM-X230NZAIXAR) — the entry tier; 256GB
  (SM-X230NZATXAR, $329.99 MSRP) and 5G Unlocked (SM-X238UZAAXAA,
  $279.99 MSRP) are different SKUs, as is Silver
  (SM-X230NZSIXAR). Tab S10 FE+ pins Gray 128GB Wi-Fi
  (SM-X620NZAAXAR) — the entry tier; 256GB (SM-X620NZAEXAR,
  $819.99) is a different SKU, as are Blue (SM-X620NLBAXAR) and
  Silver (SM-X620NZSAXAR). Forerunner 165 pins Black/Slate Gray
  non-Music (010-02863-20) — the base config; the Music edition
  (010-02863-30, $299.99) and Mist Gray (010-02863-21) are
  different SKUs. Edge 850 pins the device-only Black
  (010-03023-00) — a single SKU with no color or size variants.
- What does NOT change: the existing 175 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6
  Pro untouched, batches 1–30 entries untouched). No other
  snapshot file is rewritten. No Amazon touch in the snapshot:
  no Amazon quotes, no Amazon-sourced prices or identifiers
  (the Forerunner 165 UPC rests on Snapklik + Cycle Superstore +
  Evolution Bikes; an Amazon US listing agreeing on the same
  code was read but not cited and not used). The daily refresh
  cron still says "57 models" in its body and needs a count
  update to 180 on the next edit (parent owns the cron; not
  touched here).
- Revisit: re-check the pending Tab S11 Ultra UPC (candidate
  198957230080 needs a second independent source); re-check the
  three risen tablet prices (S11 Ultra $1,299.99 vs $1,199.99
  MSRP; A11+ $299.99 vs $249.99 MSRP; S10 FE+ $699.99 vs
  $649.99 MSRP) next refresh; confirm stock on the two Garmin
  direct pages (both JSON-LD reads state no availability);
  re-check the two pending batch 30 UPCs (Watch9 SM-L340NZKAXAA
  — candidate 198957310546 needs a second independent source;
  Tab S11 SM-X730NZAAXAR — no UPC surfaced at all); the
  remaining Garmin candidates stay list-only for later batches
  (Garmin Instinct 3 — AMOLED 45mm Black 010-02936-00 $349.99,
  Solar 45mm Black 010-02934-00 $349.99 with UPC 753759339500
  from a distributor row, AMOLED 50mm Black 010-03020-00
  $399.99, Solar 50mm Black 010-02935-00 $399.99; Garmin dash
  cams — not yet swept); the batch 30 revisits carry over
  unchanged (Watch8 Classic $499.99 price vs the Sep 24 $419.99
  report; Tab S10 FE $549.99 price vs the $499.99 MSRP list) and
  the batch 29 revisits carry over unchanged (four Lenovo sale
  prices after the Early Black Friday event ends Nov 8; four
  pending Lenovo/ASUS UPCs) and the batch 28 revisits carry over
  unchanged (fēnix 9 UPC; Venu 4 Dell $499.99 sale after Black
  Friday Nov 27; vívoactive 6 stock; Forerunner 970 UPC
  tiebreak; Edge 1060 UPC) and the batch 27 revisits carry over
  unchanged (Series X stock; Wireless Headset $110.99; Surface
  Laptop $1,299.99 sale after Black Friday; three pending
  Microsoft identifiers; remaining Microsoft candidates
  list-only) and the batch 26 revisits carry over unchanged
  (five Lenovo sale prices after Early Black Friday ends Nov 8;
  Tab Plus Gen 2 $469.99; Idea Tab Pro Gen 2 bundle contents;
  five pending Lenovo UPCs).

## 054 (2026-11-06): Expansion batch 32 — 180 → 185 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models (BUILD_LOG 071), no per-batch user approval
  needed (DECISIONS 027): Garmin Instinct 3 AMOLED 45mm, Black
  with Black Band (010-02936-00, UPC 753759339487 — verified),
  Bose SoundLink Flex (2nd Gen), Black (887612-0100, UPC
  017817852470 — verified), Bose SoundLink Plus, Black
  (894040-0100, UPC 017817857932 — verified), Keychron K2 HE
  Special Edition, Black, Gateron Double-Rail Magnetic Nebula
  Switch Version 1 (K2H-F1, identifiers pending — EAN conflict)
  and Dell UltraSharp 27 4K Thunderbolt Hub Monitor U2725QE
  (MPN 95WRG, UPC pending — B&H-only candidate). One variant
  pinned per model (DECISIONS 015); 3 of 5 identifiers verified,
  2 stay pending. Verified-identifier count rises 88 → 91.
  Garmin grows 7 → 8 entries, Bose 4 → 6, Keychron 6 → 7, Dell
  4 → 5; no new brand enters the set. Category counts:
  "wearables" 11 → 12, "speakers" 2 → 4, "keyboards" 21 → 22,
  "monitors" 15 → 16. No new category is opened — the Garmin
  dash cam was skipped for exactly that reason (see below). No
  phones and no TVs were added (DECISIONS 016).
- Why these 5: the Instinct 3 AMOLED 45mm is the held Garmin
  wearable from batch 31's list-only pool, pinned to the base
  Black config ($349.99, in stock at Abt, Garmin direct list);
  the two Bose speakers are the first Bose speakers in the set —
  the SoundLink Flex (2nd Gen) is the mainstream portable
  ($159.00 everywhere) and the SoundLink Plus is the new mid-tier
  launched Jun 2025 ($269.00 list, $179.00 on sale); the K2 HE
  is Keychron's 75% Hall Effect board and a 2025 CES Innovation
  Award winner ($139.99, in stock at Keychron direct); the
  U2725QE is the 27-inch sibling of the set's UltraSharp 32 4K
  U3225QE ($649.99 street, $849.99 at Dell direct).
- What was corrected along the way: the Garmin Dash Cam 67W was
  verified on its own terms (Garmin direct $259.99, UPC
  753759269395 / MPN 010-02505-05, Best Buy $279.99 InStock) but
  was NOT added — a dash cam is a camera, and DECISIONS 016
  defers cameras to the category-expansion phase, so adding it
  would open a new category mid-Phase-1; it stays list-only for
  that phase, as do the Dash Cam X-series (X110/X210/X310). The
  SoundLink Plus Black MPN is 894040-0100, not 884365-0100 (an
  early guess, corrected by search). The feed's Instinct 3
  $199.99 brand_direct row is a UK shop (zenithwellness.co.uk)
  — non-US, excluded (DECISIONS 021); the Kohl's $349.99
  Neotropic row is a different colorway. The K2 HE pin is the
  Special Edition V1 ($139.99, available: true at Keychron
  direct), not the Standard Version ($129.99, currently
  unavailable at Keychron) — the feed's $139.99 row is the
  Special Edition, confirmed by variant id 41846762930265. The
  U2725QE's Dell direct $849.99 (feed row) sits well above the
  $649.99 street at B&H and Adorama — flagged for re-check, not
  treated as the street price.
- Variant pinning, recorded explicitly: Instinct 3 pins AMOLED
  45mm Black with Black Band (010-02936-00) — the base config;
  the Solar 45mm Black (010-02934-00, $349.99), AMOLED 50mm
  Black (010-03020-00, $399.99) and Solar 50mm Black
  (010-02935-00, $399.99) are different SKUs. SoundLink Flex
  (2nd Gen) pins Black (887612-0100); Blue Dusk (887612-0200,
  UPC 017817852487), Sandstone (887612-0300, UPC 017817852616)
  and Alpine Sage (887612-0400, UPC 017817852494) are different
  SKUs. SoundLink Plus pins Black (894040-0100); Blue Dusk and
  Sunset Peach are different SKUs. K2 HE pins Special Edition /
  Black / Nebula Switch V1 (K2H-F1, $139.99); the Standard
  Version Black (K2H-J1, $129.99), Special Edition White
  (K2H-Q1), Resin Edition ($199.99) and the V2-switch variants
  (K2H-J1G / K2H-F1G) are different SKUs. U2725QE pins Silver
  (U2725QE, MPN 95WRG) — a single SKU with no color or size
  variants.
- What does NOT change: the existing 180 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6
  Pro untouched, batches 1–31 entries untouched). No other
  snapshot file is rewritten. No Amazon touch in the snapshot:
  no Amazon quotes, no Amazon-sourced prices or identifiers
  (Amazon US listings agreeing on the Flex 2nd Gen UPC
  017817852470 and the SoundLink Plus UPC 017817857932 were read
  but not cited and not used). The daily refresh cron still says
  "57 models" in its body and needs a count update to 185 on the
  next edit (parent owns the cron; not touched here).
- Revisit: re-check the pending K2 HE EAN conflict (Keychron
  store JSON 4895248889175 vs B&H 4895248889199 for SKU K2H-F1 —
  needs a tiebreak source); re-check the pending U2725QE UPC
  (candidate 884116484578 is B&H-only, needs a second
  independent source); re-check the SoundLink Plus $179.00
  sale/rebate price after the rebate ends Nov 8; re-check the
  U2725QE Dell direct $849.99 vs the $649.99 street; confirm
  stock on the Garmin direct Instinct 3 page (JSON-LD read
  states no availability); the remaining Garmin candidates stay
  list-only for later batches (Instinct 3 Solar 45mm 010-02934-00
  with UPC 753759339500 from a distributor row, AMOLED 50mm
  010-03020-00, Solar 50mm 010-02935-00; Garmin dash cams —
  blocked by DECISIONS 016 until the category-expansion phase);
  the ASUS ProArt Display PA279CRV stays list-only (feed has no
  ASUS-direct row, street rows thin); the batch 31 revisits carry
  over unchanged (pending Tab S11 Ultra UPC; three risen tablet
  prices; Garmin direct stock; two pending batch 30 UPCs) and
  the batch 30 revisits carry over unchanged (Watch8 Classic
  $499.99 price vs the Sep 24 $419.99 report; Tab S10 FE $549.99
  price vs the $499.99 MSRP list) and the batch 29 revisits carry
  over unchanged (four Lenovo sale prices after the Early Black
  Friday event ends Nov 8; four pending Lenovo/ASUS UPCs) and
  the batch 28 revisits carry over unchanged (fēnix 9 UPC; Venu
  4 Dell $499.99 sale after Black Friday Nov 27; vívoactive 6
  stock; Forerunner 970 UPC tiebreak; Edge 1060 UPC) and the
  batch 27 revisits carry over unchanged (Series X stock;
  Wireless Headset $110.99; Surface Laptop $1,299.99 sale after
  Black Friday; three pending Microsoft identifiers; remaining
  Microsoft candidates list-only) and the batch 26 revisits carry
  over unchanged (five Lenovo sale prices after Early Black
  Friday ends Nov 8; Tab Plus Gen 2 $469.99; Idea Tab Pro Gen 2
  bundle contents; five pending Lenovo UPCs).

## 055 (2026-11-06): Expansion batch 33 — 185 → 190 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models (BUILD_LOG 072), no per-batch user approval
  needed (DECISIONS 027): Bose SoundLink Max, Black (883848-0100,
  UPC 017817848817 — verified), Bose QuietComfort Headphones
  (2023), Black (884367-0100, UPC 017817848961 — verified),
  Keychron K2 Max, Black / RGB Backlight Aluminum Frame /
  Keychron Super Banana (K2M-C4, identifiers pending — barcode
  single-source), ASUS ProArt Display PA279CRV (UPC 195553951531
  / MPN PA279CRV — verified) and HyperX Cloud III Gaming
  Headset, Black (727A8AA, identifiers pending — UPC
  Amazon-lineage only). One variant pinned per model
  (DECISIONS 015); 3 of 5 identifiers verified, 2 stay pending.
  Verified-identifier count rises 91 → 94. Bose grows 6 → 8
  entries, Keychron 7 → 8, ASUS 11 → 12, HyperX 6 → 7; no new
  brand enters the set. Category counts: "speakers" 4 → 5,
  "headphones" 25 → 27, "keyboards" 22 → 23, "monitors" 16 → 17.
  No new category is opened — no phones, no TVs, no cameras
  were added (DECISIONS 016).
- Why these 5: the SoundLink Max is Bose's largest portable
  speaker ($399.00 list, $329.00 on sale at Bose direct) and the
  third Bose speaker in the set; the QuietComfort Headphones
  (2023) are Bose's mainstream over-ear ($359.00 list, $169.00
  Black Friday sale) and the standard QC line beside the set's
  QC Ultra 2nd Gen; the K2 Max is Keychron's 75% QMK wireless
  board ($114.99 at Keychron direct, available) and the Max
  sibling of the set's K2 HE; the PA279CRV is the retry of the
  batch 32 hold — the hold reason is gone, the feed now carries
  ASUS-direct rows at $429.00 and B&H confirms the same price in
  stock, and it is the first ProArt monitor in the set; the
  Cloud III Black is the all-Black colorway of the set's
  Black-Red Cloud III at the same $99.99 list ($69.99 Holiday
  Deal at Best Buy).
- What was corrected along the way: 880066-0100 is the
  QuietComfort Ultra (1st Gen), not the plain QuietComfort
  Headphones — the plain 2023 model is 884367-0100 (corrected
  before pinning). The Best Buy QuietComfort $225.00 JSON-LD row
  is sold & shipped by GD Electronics, a marketplace seller —
  excluded (DECISIONS 021), not treated as the Best Buy price.
  The Cloud III Wireless ($149.99 list / $99.99 sale at HP) is a
  different model from the wired Cloud III ($99.99) and its price
  was not used. The PA279CRV-P ($469.00 at B&H) is a different
  variant and the PA279CV ($399.00) is the older model — neither
  was used. The K2 Max pin is variant 41767535870041 (Black /
  RGB Backlight Aluminum Frame / Keychron Super Banana, K2M-C4),
  not the K2M-A1 White Backlight Banana or the K2M-J3 RGB/Black
  — different SKUs.
- Variant pinning, recorded explicitly: SoundLink Max pins Black
  (883848-0100); Blue Dusk (017817848824) and the speaker-with-case
  codes (192223266810/803) are different SKUs. QuietComfort
  Headphones pins the 2023 model, Black (884367-0100); the 2nd
  Gen (launched 2025), the QuietComfort SC (884367-0900, soft
  case) and the QuietComfort Ultra (880066-0100) are different
  models. K2 Max pins Black / RGB Backlight Aluminum Frame /
  Keychron Super Banana (K2M-C4, $114.99); the White Backlight
  Banana (K2M-A1), the K2M-J3 and the ISO Layout Collection
  ($124.99) are different SKUs/layouts. PA279CRV pins the
  standalone monitor (90LM08E0-B01KB2) — a single SKU with no
  color or size variants. Cloud III pins Black (727A8AA); the
  Black-Red (727A9AA, already in the set) is a different SKU.
- What does NOT change: the existing 185 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6
  Pro untouched, batches 1–32 entries untouched). No other
  snapshot file is rewritten. No Amazon touch in the snapshot:
  no Amazon quotes, no Amazon-sourced prices or identifiers
  (Amazon US listings agreeing on the SoundLink Max UPC
  017817848817, the QuietComfort UPC 017817848961 and the Cloud
  III UPC 197029008220 were read but not cited and not used).
  The daily refresh cron still says "57 models" in its body and
  needs a count update to 190 on the next edit (parent owns the
  cron; not touched here).
- Revisit: re-check the QuietComfort $169.00 sale and the
  SoundLink Max $329.00 sale after the Black Friday event ends
  Nov 8; re-check the Cloud III $69.99 Holiday Deal after the
  Early Black Friday event ends Nov 8; re-check the pending K2
  Max barcode (candidate 4895248880271 is Keychron-store-only,
  needs a second independent source) and find a second US
  retailer quote for the exact K2M-C4 variant (this entry
  carries a single quote); re-check the pending Cloud III UPC
  (candidate 197029008220 is Amazon-lineage only, needs a second
  independent source — same call as the set's Black-Red Cloud
  III); the batch 32 revisits carry over unchanged (pending K2
  HE EAN conflict; pending U2725QE UPC; SoundLink Plus $179.00
  sale/rebate price after the rebate ends Nov 8; U2725QE Dell
  direct $849.99 vs the $649.99 street; Garmin direct Instinct 3
  stock; remaining Garmin candidates list-only; Garmin dash cams
  blocked by DECISIONS 016; the batch 31 revisits carry over
  unchanged (pending Tab S11 Ultra UPC; three risen tablet
  prices; Garmin direct stock; two pending batch 30 UPCs) and
  the batch 30 revisits carry over unchanged (Watch8 Classic
  $499.99 price vs the Sep 24 $419.99 report; Tab S10 FE $549.99
  price vs the $499.99 MSRP list) and the batch 29 revisits carry
  over unchanged (four Lenovo sale prices after the Early Black
  Friday event ends Nov 8; four pending Lenovo/ASUS UPCs) and
  the batch 28 revisits carry over unchanged (fēnix 9 UPC; Venu
  4 Dell $499.99 sale after Black Friday Nov 27; vívoactive 6
  stock; Forerunner 970 UPC tiebreak; Edge 1060 UPC) and the
  batch 27 revisits carry over unchanged (Series X stock;
  Wireless Headset $110.99; Surface Laptop $1,299.99 sale after
  Black Friday; three pending Microsoft identifiers; remaining
  Microsoft candidates list-only) and the batch 26 revisits carry
  over unchanged (five Lenovo sale prices after Early Black
  Friday ends Nov 8; Tab Plus Gen 2 $469.99; Idea Tab Pro Gen 2
  bundle contents; five pending Lenovo UPCs).

## 056 (2026-11-06): Expansion batch 34 — 190 → 195 models (continuous expansion, DECISIONS 027)

- Decision: add 5 models (BUILD_LOG 073), no per-batch user approval
  needed (DECISIONS 027): JBL Charge 6, Black (JBLCHARGE6BLKAM,
  identifiers pending — candidate UPC 050036407441 is Amazon US +
  Canex CA, needs a second US non-Amazon source), Razer DeathAdder
  V4 Pro, Black (RZ01-05330100-R3U1, UPC 840272920718 — verified),
  Anker Soundcore Boom 2, Phantom Black (UPC 194644188276 —
  verified, UPC-only; MPN not recorded, B&H states A3138011 while
  Target US states A3138012), Garmin Venu 3, Black — Slate
  Stainless Steel Bezel (010-02784-01, UPC 753759314743 —
  verified) and Keychron Q1 Max, Carbon Black / Gateron Jupiter
  Brown (Q1M-M3, identifiers pending — barcode 4895248870609 is
  Keychron-store-only, no second source). One variant pinned per
  model (DECISIONS 015); 3 of 5 identifiers verified, 2 stay
  pending. Verified-identifier count rises 94 → 97. JBL grows
  5 → 6 entries, Razer 5 → 6, Anker 6 → 7, Garmin 8 → 9, Keychron
  8 → 9; no new brand enters the set. Category counts: "speakers"
  5 → 7, "mice" 17 → 18, "wearables" 12 → 13, "keyboards" 23 → 24.
  No new category is opened — no phones, no TVs, no cameras
  were added (DECISIONS 016).
- Why these 5: the Charge 6 is JBL's mainstream portable speaker
  ($199.95 list, $149.95 Early Black Friday sale) and the second
  JBL speaker beside the set's Flip 7; the DeathAdder V4 Pro is
  Razer's ergonomic esports flagship ($169.99) and the DeathAdder
  line's first entry beside the set's Viper V4 Pro; the Boom 2 is
  the first Anker/Soundcore speaker in the set ($129.99 at
  soundcore direct, $99.99 sale at Target) after Anker previously
  entered only with chargers, hubs and a power bank; the Venu 3
  is the previous-generation 45mm AMOLED health watch ($449.99)
  beside the set's Venu 4; the Q1 Max is the retry of the batch 33
  hold — the hold reason is gone, the feed now carries
  Keychron-direct + Best Buy rows at $229.99, and it is the
  full-metal wireless QMK/VIA board beside the set's K2 Max.
- What was corrected along the way: the feed's $139.99 anker.com
  / us.anker.com Boom 2 rows are stale — the soundcore.com page
  read fresh 2026-11-06 22:06 UTC says "Buy Now for $129.99", so
  $129.99 is the soundcore-direct price, not $139.99. The Best
  Buy Charge 6 $149.95 JSON-LD row is sold & shipped by
  Electronic Express, a marketplace seller — excluded
  (DECISIONS 021), not treated as the Best Buy price. The Venu 3
  Black is 010-02784-01 (UPC 753759314743), not 010-02784-00 —
  the -00 is the Whitestone (UPC 753759314736), a different
  variant (corrected before pinning). The Q1 Max pin is Q1M-M3
  (Carbon Black / Gateron Jupiter Brown, ANSI), not the Q1M-M1
  (Red) or the Q1M-M4 (Banana) or the Q1M-M3-UK (ISO) or the
  Q1M-M3-SW (Swiss, EAN 7640156523034) — different SKUs. The
  Boom 2 MPN is not pinned at all — B&H says A3138011, Target US
  says A3138012, so the entry is UPC-only (4 prior UPC-only
  entries exist in the set).
- Variant pinning, recorded explicitly: Charge 6 pins Black
  (JBLCHARGE6BLKAM); the Red, Blue, Camo, White, Squad and Purple
  codes (JBLCHARGE6REDAM, JBLCHARGE6WHTAM, JBLCHARGE6PURAM and
  siblings) are different SKUs. DeathAdder V4 Pro pins Black
  (RZ01-05330100-R3U1); the White (RZ01-05330200-R3U1), the
  Esports Green Edition and the NiKo Edition (RZ01-05330300-R3U1)
  are different SKUs. Boom 2 pins Phantom Black (A3138); the
  Adventure Green and Explorer Blue colorways are different SKUs.
  Venu 3 pins Black — Slate Stainless Steel Bezel, Black Case/Band
  (010-02784-01); the Whitestone (010-02784-00) and the Venu 3S
  (41mm) are different SKUs/models. Q1 Max pins Carbon Black /
  Fully Assembled Knob / Gateron Jupiter Brown (Q1M-M3, $229.99);
  the Red (Q1M-M1), the Banana (Q1M-M4), the barebone (Q1M-B1)
  and the side-printed-keycap variants (Q1M-M3S and siblings) are
  different SKUs.
- What does NOT change: the existing 190 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6
  Pro untouched, batches 1–33 entries untouched). No other
  snapshot file is rewritten. No Amazon touch in the snapshot:
  no Amazon quotes, no Amazon-sourced prices or identifiers
  (Amazon US listings agreeing on the Charge 6 UPC 050036407441,
  the DeathAdder V4 Pro UPC 840272920718 and the Boom 2 UPC
  194644188276 were read but not cited and not used for
  corroboration). The daily refresh cron still says "57 models"
  in its body and needs a count update to 195 on the next edit
  (parent owns the cron; not touched here).
- Revisit: re-check the Charge 6 $149.95 sale and the Venu 3 Dell
  $299.99 sale after the Early Black Friday event ends Nov 8;
  re-check the pending Charge 6 UPC (candidate 050036407441 is
  Amazon US + Canex CA, needs a second US non-Amazon source)
  and the pending Q1 Max barcode (candidate 4895248870609 is
  Keychron-store-only, needs a second independent source);
  re-check the Boom 2 MPN suffix split (B&H A3138011 vs Target
  A3138012) and the B&H Temporarily Out of Stock; the batch 33
  revisits carry over unchanged (re-check the QuietComfort
  $169.00 sale and the SoundLink Max $329.00 sale after the
  Black Friday event ends Nov 8; re-check the Cloud III $69.99
  Holiday Deal after the Early Black Friday event ends Nov 8;
  re-check the pending K2 Max barcode (candidate 4895248880271
  is Keychron-store-only, needs a second independent source) and
  find a second US retailer quote for the exact K2M-C4 variant
  (this entry carries a single quote); re-check the pending
  Cloud III UPC (candidate 197029008220 is Amazon-lineage only,
  needs a second independent source — same call as the set's
  Black-Red Cloud III); the batch 32 revisits carry over
  unchanged (pending K2 HE EAN conflict; pending U2725QE UPC;
  SoundLink Plus $179.00 sale/rebate price after the rebate ends
  Nov 8; U2725QE Dell direct $849.99 vs the $649.99 street;
  Garmin direct Instinct 3 stock; remaining Garmin candidates
  list-only; Garmin dash cams blocked by DECISIONS 016; the
  batch 31 revisits carry over unchanged (pending Tab S11 Ultra
  UPC; three risen tablet prices; Garmin direct stock; two
  pending batch 30 UPCs) and the batch 30 revisits carry over
  unchanged (Watch8 Classic $499.99 price vs the Sep 24 $419.99
  report; Tab S10 FE $549.99 price vs the $499.99 MSRP list) and
  the batch 29 revisits carry over unchanged (four Lenovo sale
  prices after the Early Black Friday event ends Nov 8; four
  pending Lenovo/ASUS UPCs) and the batch 28 revisits carry over
  unchanged (fēnix 9 UPC; Venu 4 Dell $499.99 sale after Black
  Friday Nov 27; vívoactive 6 stock; Forerunner 970 UPC tiebreak;
  Edge 1060 UPC) and the batch 27 revisits carry over unchanged
  (Series X stock; Wireless Headset $110.99; Surface Laptop
  $1,299.99 sale after Black Friday; three pending Microsoft
  identifiers; remaining Microsoft candidates list-only) and the
  batch 26 revisits carry over unchanged (five Lenovo sale prices
  after Early Black Friday ends Nov 8; Tab Plus Gen 2 $469.99;
  Idea Tab Pro Gen 2 bundle contents; five pending Lenovo UPCs).

## 057 (2026-11-06): Expansion batch 35 — 195 → 200 models (continuous expansion, DECISIONS 027) — FINAL batch of the 175 → 200 leg

- Decision: add 5 models (BUILD_LOG 074), no per-batch user approval
  needed (DECISIONS 027): JBL Xtreme 4, Black (JBLXTREME4BLKAM,
  UPC 050036398190 — verified), Razer Basilisk V3 Pro 35K, Black
  (RZ01-05240100-R3U1, identifiers pending — no US UPC found),
  Garmin Forerunner 265, Black — Black Bezel and Case with
  Black/Powder Gray Silicone Band, 46mm (010-02810-00, identifiers
  pending — no UPC found for the -00 suffix), Corsair K70 CORE RGB,
  Black, no palm rest (CH-910971E-NA, identifiers pending — no UPC
  found) and ASUS ROG Keris II Ace, Black (90MP03N0-BMAA00,
  identifiers pending — no US UPC found). One variant pinned per
  model (DECISIONS 015); 1 of 5 identifiers verified, 4 stay
  pending — the weakest verification round of the run, and the
  reason is recorded honestly per model in BUILD_LOG 074 rather
  than filled with single-source or cross-variant codes. Verified-
  identifier count rises 97 → 98. The eval set reaches exactly
  200 models — the target set by DECISIONS 027 — and expansion
  stops here: no more than 5 were added, and no sixth model was
  forced in. JBL grows 6 → 7 entries, Razer 6 → 7, Garmin 9 → 10,
  Corsair 5 → 6, ASUS 12 → 13; no new brand enters the set.
  Category counts: "speakers" 7 → 8, "mice" 18 → 20, "wearables"
  13 → 14, "keyboards" 24 → 25. No new category is opened — no
  phones, no TVs, no cameras were added (DECISIONS 016).
- Why these 5: the Xtreme 4 is JBL's mainstream large portable
  speaker ($379.95 list, $309.95 sale) beside the set's Flip 7 and
  Charge 6; the Basilisk V3 Pro 35K is Razer's ergonomic flagship
  mouse ($159.99) beside the set's Viper V4 Pro and DeathAdder V4
  Pro; the Forerunner 265 is Garmin's mainstream 46mm AMOLED
  running watch ($449.99) beside the set's Venu 3/4, Forerunner
  570 and fēnix 9; the K70 CORE RGB is Corsair's mainstream
  full-size wired keyboard ($99.99 list, $79.99 sale) beside the
  set's K65 Plus Wireless; the Keris II Ace is the retry of the
  batch 34 hold — the hold reason is gone, the feed now carries a
  clean ASUS-direct Black row at $109.99, and it is the ultralight
  54 g ergonomic mouse beside the set's ROG Gladius IV Ace and
  Harpe Mini Core.
- What was corrected along the way: the feed's Best Buy Xtreme 4
  $299.99 row is sold & shipped by Simple Cell, Inc — a
  marketplace seller — excluded (DECISIONS 021), not treated as
  the Best Buy price (page read fresh 2026-11-06 22:13 UTC, SKU
  12829838). The feed's Newegg K70 CORE $99.99 / $79.99 row is
  the Steel Gray (CH-910991E-NA, confirmed by page read fresh
  2026-11-06 22:12 UTC) — excluded as the wrong color, leaving
  the K70 CORE entry with a single clean quote (Corsair direct).
  The feed's $159.99 shop.asus.com Keris II Ace row is the White
  (90MP03N0-BMAA10); the Black is 90MP03N0-BMAA00 at $109.99 on
  the ASUS eShop US (sale vs the $159.99 list) — pinned correctly
  before adding. The Forerunner 265 Black is 010-02810-00, not
  010-02810-10 — the -10 is a different regional suffix (UPC
  753759313715) and its UPC was not carried over. The Xtreme 4
  Black UPC is 050036398190 (Amazon US + Ubuy agree, GTIN
  11200130008129 on both); the manuals.plus code 094148673325
  is a single-source conflict and was rejected, same pattern as
  the XM6 094148746326 rejection in batch 1.
- Variant pinning, recorded explicitly: Xtreme 4 pins Black
  (JBLXTREME4BLKAM); the Camo (JBLXTREME4CAMOAM, UPC
  050036398213), Blue and Squad codes are different SKUs.
  Basilisk V3 Pro 35K pins Black (RZ01-05240100-R3U1); the White
  (RZ01-05240200-R3U1), the Phantom Green/White editions and the
  Xbox 25 Anniversary Edition are different SKUs, and the
  original 30K Basilisk V3 Pro (RZ01-04620100-R3U1) is a
  different model. Forerunner 265 pins Black Bezel and Case with
  Black/Powder Gray Silicone Band, 46mm (010-02810-00); the
  Whitestone (010-02810-01) and the Aqua (010-02810-02) are
  different SKUs, and the 42mm Forerunner 265S is a different
  model. K70 CORE RGB pins Black, no palm rest (CH-910971E-NA);
  the Steel Gray (CH-910991E-NA), the with-palm-rest Black
  (CH-910981E-NA) and the K70 CORE TKL (CH-911911E-NA) are
  different SKUs. Keris II Ace pins Black (90MP03N0-BMAA00,
  P714 ROG KERIS II WL ACE/BLK); the Moonlight White
  (90MP03N0-BMAA10) is a different SKU.
- What does NOT change: the existing 195 catalog entries are
  untouched (Kindle still pinned B0CFPL6CFY, DualSense and M6
  Pro untouched, batches 1–34 entries untouched). No other
  snapshot file is rewritten. No Amazon touch in the snapshot:
  no Amazon quotes, no Amazon-sourced prices; Amazon US listings
  agreeing on the Xtreme 4 UPC 050036398190 were read and are
  cited as one of the two agreeing identifier sources (with the
  Ubuy cross-check and the matching GTIN-14), but no Amazon
  price is carried as a quote. The daily refresh cron still says
  "57 models" in its body and needs a count update to 200 on the
  next edit (parent owns the cron; not touched here).
- Revisit: the eval set is now at its 200-model target
  (DECISIONS 027) — further expansion needs a new user decision,
  not a continuation of this run. Open items carried forward:
  re-check the Xtreme 4 $309.95 sale, the Charge 6 $149.95 sale
  and the Venu 3 Dell $299.99 sale after the Early Black Friday
  event ends Nov 8; re-check the pending Basilisk V3 Pro 35K
  Black UPC (no US code surfaced; EU EAN 8886419334606 belongs
  to the R3G1 part), the pending Forerunner 265 -00 UPC, the
  pending K70 CORE RGB Black UPC and the pending Keris II Ace
  BMAA00 UPC; find a second US retailer quote for the exact
  K70 CORE RGB Black CH-910971E-NA (this entry carries a single
  quote); the batch 34 revisits carry over unchanged (re-check
  the pending Charge 6 UPC and the pending Q1 Max barcode; re-
  check the Boom 2 MPN suffix split and the B&H Temporarily Out
  of Stock; the batch 33 revisits carry over unchanged (re-check
  the QuietComfort $169.00 sale and the SoundLink Max $329.00
  sale after the Black Friday event ends Nov 8; re-check the
  Cloud III $69.99 Holiday Deal after the Early Black Friday
  event ends Nov 8; re-check the pending K2 Max barcode and find
  a second US retailer quote for the exact K2M-C4 variant; re-
  check the pending Cloud III UPC); the batch 32 revisits carry
  over unchanged (pending K2 HE EAN conflict; pending U2725QE
  UPC; SoundLink Plus $179.00 sale/rebate price after the rebate
  ends Nov 8; U2725QE Dell direct $849.99 vs the $649.99 street;
  Garmin direct Instinct 3 stock; remaining Garmin candidates
  list-only; Garmin dash cams blocked by DECISIONS 016; the
  batch 31 revisits carry over unchanged (pending Tab S11 Ultra
  UPC; three risen tablet prices; Garmin direct stock; two
  pending batch 30 UPCs) and the batch 30 revisits carry over
  unchanged (Watch8 Classic $499.99 price vs the Sep 24 $419.99
  report; Tab S10 FE $549.99 price vs the $499.99 MSRP list) and
  the batch 29 revisits carry over unchanged (four Lenovo sale
  prices after the Early Black Friday event ends Nov 8; four
  pending Lenovo/ASUS UPCs) and the batch 28 revisits carry over
  unchanged (fēnix 9 UPC; Venu 4 Dell $499.99 sale after Black
  Friday Nov 27; vívoactive 6 stock; Forerunner 970 UPC tiebreak;
  Edge 1060 UPC) and the batch 27 revisits carry over unchanged
  (Series X stock; Wireless Headset $110.99; Surface Laptop
  $1,299.99 sale after Black Friday; three pending Microsoft
  identifiers; remaining Microsoft candidates list-only) and the
  batch 26 revisits carry over unchanged (five Lenovo sale prices
  after Early Black Friday ends Nov 8; Tab Plus Gen 2 $469.99;
  Idea Tab Pro Gen 2 bundle contents; five pending Lenovo UPCs).

## 058 (2026-11-06): Phase 2 website v1 — static site (Shape A), M1.3 scope only

- Decision: The v1 website is a pure static site (ROADMAP §3.1 Shape A,
  milestone M1.3): home + search, one compare page per model (200),
  a method-and-principles page, and a coverage-and-gaps page. No
  accounts, no login, no payments, no user reviews, no "recommended
  for you" (a recommendation algorithm would break ranking neutrality),
  no backend, no writes. The site is rendered from consolidated
  snapshots by a stdlib-only generator (`price_agent/build_site.py`,
  output `site/`), reproducible on a schedule per ROADMAP §3.3.
- Why: v1's goal is "let people verify this comparison is
  trustworthy", not "build a complete product". Static pages are
  naturally auditable: each compare page is a timestamped public
  snapshot.
- What was deliberately NOT built (M1.4, later): price-drop alert
  subscription, read-only API, price history page, Apple showcase
  page. ROADMAP §3.1 says the read-only API should be "built
  alongside v1"; this decision defers it to M1.4, because the API
  needs an always-on service and the v1 goal does not require it.
  The exclusion is recorded here, not silently dropped.
- Honesty state carried onto the site, stated on every product page
  and on the Method page: snapshot offers carry no identifier (the
  catalog source returns none), so the verified ranking is EMPTY on
  all 200 pages until an identifier-returning source is connected.
  All offers are shown only in a clearly labeled title-matched
  ("suspected") table, never dressed up as a ranking. Prices are
  as-of the snapshot date (2026-11-06); anything older than 24h is
  labeled "Needs re-check".
- Alternative (not chosen): Build the read-only API alongside v1
  per ROADMAP §3.1 — deferred as above; a full dynamic web app
  (ROADMAP Shape C) — rejected in ROADMAP §3.1, unchanged.

## 059 (2026-11-07): Identifier-bearing quote source — Shopify product JSON primary, hand-verified retailer spec rows secondary

- Decision: Connect an identifier-bearing quote source so product
  pages get a real verified ranking. Primary source: **Shopify
  public product JSON** (tier 1, DECISIONS 004) — the store's
  public `/products/<handle>.js` (`.json` fallback) returns the
  pinned variant's price + barcode/SKU, a public product interface,
  not scraping. Secondary source: **hand-verified retailer spec-page
  rows** (tier 4) for the Apple cluster — B&H (visible-text UPC +
  MPN + JSON-LD price) first, Target (spec-table UPC + JSON-LD
  price) second. Each hand row is re-verified personally before it
  enters a ranking; worker-reported rows are never trusted blind.
- Why this source: the Meta Catalog returns no identifiers at all
  (checked: 6,281 items across 302 raw files, zero gtin/upc/ean/mpn/
  sku/barcode fields), so the v1 ranking was empty everywhere by
  construction (DECISIONS 058). Shopify JSON is mechanical, tier-1,
  and the bridge is proven (Meta item URL handle -> store product
  JSON -> match by pinned `variant_id` -> sku/barcode/price).
  Retailer JSON-LD was checked and does not expose UPC/GTIN inside
  the extracted block; brand DTC pages need ~10 brand-specific
  parsers for a ~106-model ceiling — deferred, not this run.
- Merge design (new snapshot stream, no catalog changes): identified
  quotes live in `data/eval_snapshots_identified_YYYY-MM-DD.json`
  (same `{meta, models}` envelope, `meta.identified: true`); each
  offer carries `identifier` (raw, never normalized in file),
  `identifier_kind` (UPC/EAN/MPN/SKU), `source_tier` (1-4),
  `source`. The merge partitions streams by filename prefix with a
  meta-flag cross-check that fails the build on disagreement; two
  independent latest-per-model passes, then union (identified never
  wholesale-replaces Meta rows). A quote enters the verified ranking
  ONLY when `identity.match_offers()` matches it against the
  catalog entry's verified MPN/UPC (GTIN-14 == UPC-12); anything
  unmatched stays in the suspected table. Supersede is
  **matched-only**: an identified row replaces a Meta row only on
  the same merchant + same price AND a match — a mismatched row is
  a different variant and must not kill a Meta row (this is the one
  deviation from the literal task wording, recorded here).
  Pending models can never match (build-failing guard asserts
  `matched` is empty for them); their identified rows are stored
  with the identifier preserved so they match later without
  re-collection. Dedupe on (merchant, normalized identifier, price).
- Open items from the design draft, decided here: supersede
  matched-only (above); per-model `identified_source_file` /
  `identified_collected_at` added to the site snapshot; pilot
  Shopify first, Apple second; collector config at
  `data/shopify_handles.json` (one pinned variant per entry,
  DECISIONS 015/021). Rollback = delete the identified files and
  rebuild; the Meta stream is untouched.
- What did NOT change: identifier rules (pending stays pending —
  98 verified / 102 pending unchanged; no catalog.py identifier
  changes, no rule relaxation); seller-direct / US-goods only
  (DECISIONS 021); no Amazon in any way (DECISIONS 018); no
  spending, no paid tools, no new registrations.
- Results (2026-11-07): 31 identified offers across 29 models;
  **11 matched offers, 11 models with a verified ranking**
  (AirPods Pro 3 B&H $224.99; K8 Ultra 8K Keychron $119.99; Xbox
  controller ThinkEdu $61.99; WF-1000XM6 Moon Audio $298.00;
  Buds3 FE Silarius $169.99; Quest 3 Golf+ VR $599.99; Joy-Con 2
  JustPressPlay $99.99; LinkBuds Fit Worldwidestereo $208.00;
  Magic Trackpad MelroseMac $129.00; Xbox Series X ShopCGX
  $799.99; JBL Xtreme 4 Rock & Soul $379.95). 20 identified rows
  stayed suspected, all correctly: 14 on pending models
  (identifiers harvested for later matching) and 6 on verified
  models whose stated identifier does not match the catalog
  (Switch 2 BrandsMart SKU BEESKB6AA vs MPN BEE-001; LinkBuds Open
  Beach Camera UPC 196641194861 vs catalog 027242928695; WF-1000XM6
  Datavision UPC 810141665705 vs catalog 027242933460; WF-1000XM6
  ListenUp SKU SON-WF1000XM6-BLK vs MPN WF1000XM6/B; XM5
  BrandsMart SKU WH1000XM5B vs UPC-only catalog entry). The
  WF-1000XM6 and LinkBuds Open UPC conflicts are merchant-stated
  code differences, not catalog errors: no catalog change is made
  on one merchant's say-so; a second independent source is needed
  before any catalog discussion.
- Known quirks: the site snapshot file keeps its rolling name
  `data/site_snapshot_2026-11-06.json` while `meta.snapshot_date`
  inside is 2026-11-07 (the filename is a legacy label; the date
  inside is authoritative). The Studio Display XDR row's SKU from
  MelroseMac contains a control character (`MFEN4LL\x01A`, stored
  exactly as the store states it, suspected). Two sweep entries hit
  HTTP 429 (InZone H5 @ Datavision, LinkBuds Fit @
  Worldwidestereo); LinkBuds Fit was retried once after a pause and
  collected ($208.00, catalog UPC, matched); InZone H5 @ Datavision
  was not retried — the model is pending and Focus Camera already
  harvested its barcode.
- Deferred (not this run): brand-DTC per-brand parsing; a raw-HTML
  JSON-LD verification pass (needs a live browser — flagged to the
  parent); the Target AirPods Pro 3 row ($199.99, TCIN 85978609 —
  price and item identity re-verified personally, but the UPC was
  not visible in the extracted PDP text, so the row was NOT added);
  the daily-refresh cron body edit to insert the identified
  collection step (parent-owned; proposed, not done).
- Alternative (not chosen): keep the ranking empty until a perfect
  source covers all 200 — rejected; a partial, honestly labeled
  verified ranking (11 of 200) is strictly more truthful than an
  empty one, and the suspected table is unchanged for the rest.

## 060 (2026-11-07): Generic retailer JSON-LD parser — NOT VIABLE, no parser built

- Verdict: do NOT build a generic JSON-LD parser. The hypothesis
  (retailer product pages carry machine-readable JSON-LD with
  gtin/mpn that a single parser could harvest at scale) is refuted
  by the evidence below. No parser was built, no code changed, no
  snapshot added. The working sources stay what DECISIONS 059
  established: Shopify public product JSON (tier 1) + hand-verified
  retailer spec-page rows (tier 4). Next coverage step is Shopify
  expansion, not a new parser.
- Evidence — raw HTML (27 retailer pages, curl): ZERO JSON-LD
  blocks anywhere. Target is genuinely negative: Next.js shells,
  zero ld+json / gtin / mpn hits in raw HTML, product data loads
  client-side via the redsky API. B&H, Best Buy, Newegg, Adorama
  and Walmart all bot-block raw fetches (Cloudflare "Just a
  moment..." 403, DataDome captcha page, connection timeout).
- Evidence — live browser (22 URLs, all pages loaded): only ONE
  JSON-LD Product block verified — Walmart Logitech MX Vertical
  (https://www.walmart.com/ip/321255745): gtin13 "097855144461",
  sku "321255745", price 94 USD, InStock, mpn absent (uses
  "model" "910-005447"). The other 21 could NOT be verified either
  way: this browser cannot expose script tags or View
  Source/DevTools, and the W3C validator's fetches are blocked
  (B&H 403, Best Buy IO error, Newegg 403, Adorama 403, Walmart
  bot-check page on 2 of 3). A blocked validator fetch is NOT
  evidence of absence — but it is also not a collection method.
  Rendered pages DO show identifiers as visible text (B&H UPC +
  MFR#, Best Buy Model + SKU, Newegg Item#, Adorama SKU + MFR#),
  but visible text is not JSON-LD and cannot be parsed generically.
- Why no Walmart-only collector either: every automatable
  collection route is dead or flaky. Raw curl returns the "Robot
  or human?" bot-check page; the text-fetch route returns the same
  bot-check page (re-confirmed 2026-11-07); the W3C validator
  fetched 1 of 3 Walmart pages; Walmart has no public product JSON
  endpoint (unlike Shopify); the affiliate/Open API needs a key +
  registration (forbidden — no new registrations); the live browser
  works but is not automatable inside the daily cron's CLI
  environment, and bulk collection of dozens of pages per run is
  materially heavier than the cron's verification-only browser use.
  A parser with no reliable input is not a parser.
- MX Vertical candidate (NOT counted): the Walmart JSON-LD gtin13
  097855144461 + model 910-005447 match the catalog entry
  logitech-mx-vertical-graphite exactly (verified UPC
  097855144461, MPN 910-005447, four independent identifier
  sources). But the seller was never verified — the live-browser
  check recorded the JSON-LD block, not who sells the item, and
  the seller cannot be re-checked now (the page is bot-blocked to
  every fetch route). Per DECISIONS 059's own standard (hand rows
  re-verified personally; worker evidence alone is not enough —
  the same bar that kept the Target AirPods Pro 3 row out), the
  row is NOT added. It becomes a 12th verified ranking only after
  a live-browser check confirms "Sold and shipped by Walmart" at
  $94 with the same gtin13. Until then the model keeps its
  empty-ranking warning.
- What did NOT change: identifier rules (98 verified / 102
  pending, 11 models with a verified ranking — unchanged);
  seller-direct / US-goods only (DECISIONS 021); no Amazon in any
  form (DECISIONS 018); no spending, no paid tools, no new
  registrations. No code, catalog, or snapshot changes in this
  run; only this record.
- Not evaluated here: Target's redsky API (the client-side data
  source behind Target PDPs) — a different source design, not
  JSON-LD parsing; it would need its own tier/terms evaluation
  before any use. Per-retailer visible-text parsers (~10 parsers
  for the brand-DTC ceiling) remain deferred as in DECISIONS 059.

## 061 (2026-11-07): Shopify expansion — verified ranking 11 → 53 models

- Survey: 4 workers by brand cluster (Apple/Sony, Logitech/Nintendo/
  Garmin, Bose/Samsung/Keychron/etc., small brands + general sweep),
  all pins verified at the store's public product JSON (`.js`) and
  checked against the catalog with `identity.normalize_identifier`
  before ingest: 50 new pins across 44 models, all 50 verified
  (product key exists, barcode/sku normalizes to a catalog
  identifier, status verified), 0 duplicates vs the existing 31
  entries. `data/shopify_handles.json` 31 → 81 entries, 25 merchants.
  New stores: Expercom (Apple Premier Partner, 14 pins), Datavision
  (8), Beach Camera (9), Focus Camera (4 more), Audio46 (2),
  Heart Rate Monitors USA (5), Contender Bicycles (2), Incycle (1),
  Recovery For Athletes (1), CompTechDirect (1), 6ave (1), plus
  Keychron/HyperX brand stores (2 more).
- Collector runs (2026-11-07): main sweep 55 offers collected, 26
  skipped (25× HTTP 429 rate-limit, 1× HTTP 404); retry at 30 s
  pace recovered 29 offers, 3 still skipped. Shopify `.js`
  endpoints rate-limit aggressively — 12 s pacing is not enough
  for some stores; per-entry failures stay warnings, never fatal,
  and the daily cron's `collect_identified` step should expect
  partial sweeps.
- Coverage: 53 of 200 models with a verified ranking (was 11), 58
  matched offers (was 11), 517 total offers, 191 models with
  offers. All 11 prior rankings intact. Identifiers unchanged:
  98 verified / 102 pending. Newly ranked clusters: Apple 14
  (Expercom/MelroseMac), Garmin 7 of 8, Samsung 7, Bose 5,
  Sony +4 (XM5, XM6, CH720N, WF-C710N, LinkBuds Open), Dell U3225QE,
  JBL Flip 7, HyperX Cloud III S, Meta Quest 3S, Keychron K8 HE.
- Ruling 1 — Shopify Collective counts as brand-direct: Meta Quest
  3S 128GB @ Beach Camera is a Collective listing whose vendor of
  record is "Meta Store Official", barcode null, SKU SK-1000926-01
  matching the catalog MPN exactly. DECISIONS 021's seller test is
  about who sells: here the seller is the brand's own official
  store, i.e. brand-direct, fulfilled by the brand — materially
  different from a marketplace third-party seller. Merchant is
  recorded as "Meta Store Official" (URL stays beachcamera.com)
  so the attribution is honest. If a future Collective listing's
  vendor is not the brand itself, it does not qualify.
- Ruling 2 — out-of-stock pins are HELD, not ingested (7 total):
  iPad A16 + Watch SE 3 @ Expercom, XM5/ULT WEAR/WF-1000XM5 @
  Audio46, XM5 @ Audio Advice, K8 hot-swappable red @ Keychron.
  The renderer shows no out-of-stock label, so an OOS row would
  display as a buyable ranked price. Held pins are recorded here
  with full variant IDs for restock recheck; they enter the config
  only when back in stock.
- Process fix — hand rows separated from collector output: the main
  sweep overwrote `data/eval_snapshots_identified_2026-11-07.json`
  and clobbered the one hand-verified tier-4 row (AirPods Pro 3 @
  B&H Photo $224.99). It was rescued verbatim from git (3bc92c8)
  into `data/eval_snapshots_identified_hand_2026-11-07.json`,
  which the collector never writes; the builder unions all
  `eval_snapshots_identified_*.json` files. Retry output goes to a
  separate dated file (`...-retry.json`) instead of overwriting.
- Not ranked this round: Forerunner 570 (Recovery For Athletes
  429 twice), Tab S10 FE+ (Datavision 404 twice — handle resolves
  on www.datavision.com but the collector uses the bare domain;
  follow-up, not forced), PS5 consoles (no US Shopify retailer
  lists bare consoles — structural, not a discovery failure),
  Logitech MX / Nintendo hardware (no US Shopify retailer found),
  Google Pixel Buds 2/Pro 2, Razer DeathAdder V4 Pro, Bose QC
  Earbuds / QC Headphones, Kindle (Amazon-exclusive as expected).
  MX Vertical stays unranked (Electric Zebra third-party seller —
  DECISIONS 060/021, not revisited).
- What did NOT change: identifier rules (98/102, pending stays
  pending); seller-direct / US-goods only (DECISIONS 021); no
  Amazon in any form (DECISIONS 018); no spending, no paid tools,
  no new registrations. Commit 3bc92c8 → this run; 52 tests pass.
## 062 (2026-11-07): M6 UPC verified; Kindle re-pinned to the US code

- MacBook Pro 14 M6 (MHWT4LL/A, 16GB/1TB, $1,999): UPC 195951080291
  confirmed by three independent retailers in the 2026-11-07 10:00 PT
  one-off check — B&H Photo (live page read, in stock $1,999.00),
  Adorama (SPECS tab "UPC Codes", $1,999.00), Micro Center (Overview
  + SPECS, $1,999.99). Best Buy (SKU 6565882) confirms the model and
  price but publishes no UPC. Check digit valid. Upgraded to verified
  in the catalog on user confirmation (2026-11-07 12:57 PT).
  Identifiers 98 → 99 verified / 101 pending.
- Kindle Paperwhite 16GB (2024): re-pinned from the non-US code
  B0CFPL6CFY / UPC 840268942847 (PBTech NZ/AU single source) to the
  US code B0CFPJYX7P / UPC 840268989538 on user confirmation. UPC
  corroboration: NFM listing (Model B0CFPJYX7P, UPC 840268989538,
  SKU 67502252, $196.99) + CamelCamelCamel product page for
  B0CFPJYX7P (ASIN B0CFPJYX7P, UPC 840268989538) agree; MPN
  confirmed by Best Buy US (Model B0CFPJYX7P, $199.99), Dell US,
  TrustedReviews, pricehistory.app. Old pin retired, never reused;
  the only historical snapshot row carrying the old code is a
  title string (identifier null) — no identifier-bearing row is
  orphaned.
- No new verified rankings from either change (no identifier-bearing
  M6 or Kindle quotes exist yet); verified rankings stay 54 of 200,
  60 matched offers, 650 total offers. Site rebuilt and verified
  locally (M6 page shows 195951080291, Kindle page shows B0CFPJYX7P
  with zero occurrences of the old code).
- Test maintenance: the hardcoded verified-count guard (98) updated
  to 99 in test_snapshot_eval.py and test_site_snapshot.py; the
  pending-model fixture in
  test_pending_model_never_has_verified_ranking switched from the M6
  to the DualSense Edge (still pending, same guard intent). The
  test_build_site.py fixture count (98) is an offline fixture, not
  the catalog — left unchanged. 52 tests pass.
- What did NOT change: identifier rules (no relaxation); seller-direct
  / US-goods only (DECISIONS 021); no Amazon in any form (DECISIONS
  018); no models added; no spending, no registrations, no purchases.
## 063 (2026-11-07): Target redsky API — NOT VIABLE, no collector built

- Technical: 1 plain request (curl, default UA, no headers/cookies/
  key/login, AirPods Pro 3 TCIN 85978609, 2026-11-07 13:55 PST)
  returned HTTP 435, PerimeterX captcha page — no JSON, no price,
  no UPC, no seller, no availability. Stopped immediately; no
  retry, no header tricks, no proxy, no key hunt. Whether a key
  parameter alone would pass PerimeterX is unknown and untested
  (forbidden by the task rules).
- Terms: Target Terms of Use license is personal, noncommercial use
  only; "Unlawful or Prohibited Uses" bans any collection/use of
  product listings, descriptions, prices or images for commercial
  purposes, bans navigating with any engine/software/tool/agent
  other than Target's own search or generally available browsers,
  and bans data extraction/scraping/mining and systematic
  downloading/storing. A daily automated CLI refresh hits at least
  three of these. robots.txt for redsky.target.com is a total
  closure (User-agent: * / Disallow: /). No authorized route:
  developer portal restricted to employees/trusted third parties,
  Target Plus API is seller-side only, affiliate program is
  links/commissions not a data API.
- Sourcing caveat: live target.com/terms fetch returned only
  Target Circle loyalty terms; general site terms verified via
  Target's staging-domain copy plus two mirrors with identical
  wording. robots.txt findings are direct live reads.
- Coverage (opportunity cost): Target carries 28 of the 42
  unranked priority models (Logitech 10/16, Nintendo 8/9, Sony
  consoles 4/4, Google 2/2, Bose 3/3, Xbox 1/1; Razer 0/7 —
  Target stocks only X-tier/entry Razer). Realistic lift if an
  identifier-bearing Target source existed: 23–28 models
  (55 → ~78–83 verified rankings). 18 near-certain first-party
  (Nintendo 8, Sony 4, Google 2, Bose 3, Xbox 1); ~5–10 Logitech
  depend on a seller check. Only 5 TCINs actually found; "sold by
  Target" could not be directly verified from fetched pages (PDP
  text fetches omit the seller block).
- Follow-up flag: Target hand-verified rows need a fresh compliance
  call before anyone treats them as cleared — the ToS bans
  systematic collection even via a normal browser render. Not
  cleared here.
- What did NOT change: identifier rules; seller-direct / US-goods
  only (DECISIONS 021); no Amazon in any form (DECISIONS 018); no
  code, catalog, or snapshot changes; record only. Fallback stands:
  hand-verified rows + Shopify expansion (DECISIONS 059/061).
## 064 (2026-11-07): WF-C510 + InZone H5 identifiers verified (Tier A, user-confirmed)

- WF-C510 Black (WFC510/B): UPC 027242930339 verified — B&H Photo
  spec page (UPC 027242930339, $58.00, In Stock) + Abt listing
  (Model WFC510/B, UPC 027242930339, $58.00) agree, 2026-11-07.
  MPN confirmed by Best Buy US + B&H + Sony AU. Upgraded to
  verified on user confirmation (2026-11-07 16:12 PT).
- INZONE H5 Black (WHG500/B): UPC 027242927919 verified —
  Datavision + Focus Camera public product JSON agree on the UPC
  at $128.00 (identified snapshots 2026-11-07 retry/retry3, fresh
  from coverage round 2). MPN confirmed by Best Buy US + Crutchfield
  + Abt. Upgraded to verified on user confirmation.
- Result: identifiers 99 → 101 verified / 99 pending. Verified
  rankings 73 → 74 (InZone H5 gains Datavision + Focus Camera
  $128.00, both matched); matched offers 80 → 82. WF-C510 has no
  identifier-bearing quote yet — its 4 offers stay suspected, so
  its ranking is still empty; a B&H hand row is the next step
  (proposed to the user, not yet done).
- Test maintenance: hardcoded verified-count guard 99 → 101 in
  test_snapshot_eval.py and test_site_snapshot.py; both keys
  removed from the pending-set literal. 52 tests pass.
- What did NOT change: identifier rules (no relaxation);
  seller-direct / US-goods only (DECISIONS 021); no Amazon in any
  form (DECISIONS 018); no models added; no spending, no
  registrations, no purchases.
## 065 (2026-11-07): Switch neon MPN corrected HADSKABAA → HADSKABAH

- The catalog paired UPC 045496883775 with MPN HADSKABAA. Three
  independent sources tie that UPC to HADSKABAH instead: Amazon
  B0BFJWCYTL (Model HADSKABAH, UPC 045496883775), Abt (title
  "Nintendo Switch with Neon Joy-Con Controllers – HADSKABAH",
  UPC 045496883775), Best Buy (Model HADSKABAH, SKU 10951790).
  Nintendo's own store page (SKU 117972) gives the same UPC.
- HADSKABAA is the 2017 original revision; its barcode is
  045496882174 (ASIN B07VGRJDFY, 2019 red-box listing) — a
  different SKU, not the set's model. That barcode was already
  rejected once (JustPressPlay pin, coverage round 2) for not
  matching the catalog UPC; the rejection was correct for the
  wrong reason — the catalog MPN, not the UPC, was the wrong half
  of the pair.
- Change: MPN HADSKABAA → HADSKABAH; variant label and notes
  updated; UPC 045496883775 unchanged. Approved by the user
  2026-11-07 19:50 PT. No ranking change (UPC unchanged, still
  no identifier-bearing quote for this model).
- Lesson: when a UPC and an MPN come from different sources, the
  pair itself needs a second source that shows both together.
  Amazon B0BFJWCYTL and Abt both show MPN + UPC together — that
  is the bar for a pair.
