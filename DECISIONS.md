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
