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
