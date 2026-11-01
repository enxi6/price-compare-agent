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
