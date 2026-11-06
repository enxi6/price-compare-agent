# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
While the major version is 0, the API and snapshot formats may change in minor
releases; breaking changes are called out in the release notes.

## [Unreleased]

### Added

- Expansion batch 6 (DECISIONS 028, continuous expansion per
  DECISIONS 027): eval set 52 → 57 models, 47 → 51 verified
  identifiers. New: iPad Pro 13-inch M5 256GB Wi-Fi Space Black
  (MDYJ4LL/A, UPC 195950398090), PlayStation Portal Remote Player
  White (1000041319, UPC 711719579779), Nintendo Switch Neon
  Blue/Neon Red set (HADSKABAA, UPC 045496883775), Logitech G Pro X
  Superlight 2 DEX Black (910-007328, identifiers pending — UPC not
  found in any US retailer spec page), Bose Ultra Open Earbuds 2nd
  Gen Black (897806-0010, UPC 017817862714). New snapshot
  `data/eval_snapshots_batch6_2026-11-06.json` holds 15 quotes
  across the 5 models (3 each). DECISIONS 021 applied to every
  quote: no marketplace/third-party rows, no non-US rows, no Amazon.

- Continuous expansion authorized (DECISIONS 027, user 2026-11-06):
  eval set expands 52 → 200 models without per-batch approval;
  batches of 5 remain the documentation unit only. Same flow as
  batches 1–5 (expansion skill + DECISIONS 021), first exhausting
  the remaining candidates from the five brand sweeps, then new
  mainstream US electronics brands one at a time.

- Selection and quote-eligibility rules (DECISIONS 021, user
  2026-11-06): no third-party/marketplace sellers for now, no
  non-US-market goods, selection stays each brand's mainstream or
  new products with gradual expansion later. No catalog entry
  changes; the rule bites on quote eligibility only (the Newegg
  $117 Astonlink row is excluded from future snapshots).

- Expansion batch 1 (DECISIONS 022, user 2026-11-06): eval set
  28 → 33 models — Nintendo Switch 2 base system (BEE-001, UPC
  045496885816), Sony WH-1000XM6 Black (WH1000XM6/B, UPC
  027242930698), Apple Watch Series 12 GPS 42mm Black Aluminum
  Black Sport Band S/M (MJEA4LS/A, UPC pending — M6 precedent),
  Logitech MX Anywhere 3S Graphite (910-006928, UPC 097855184030),
  Samsung Galaxy Buds4 Black (SM-R540NZKAXAR, UPC 198957277207).
  New snapshot `data/eval_snapshots_batch1_2026-11-06.json` holds
  16 quotes across the 5 models (Switch 2: 5, XM6: 3, Watch 12: 2,
  Anywhere 3S: 3, Buds4: 3), all DECISIONS 021-clean. Existing 28
  entries untouched; no Amazon touch. Eval: 33 models, 30 verified
  identifiers, 16 quotes, 0 identifier-matched, 16 suspected.

- Expansion batch 2 (DECISIONS 023, user 2026-11-06): eval set
  33 → 38 models — Sony WF-1000XM6 Black (WF1000XM6/B, UPC
  027242933460), Apple Watch Ultra 4 GPS + Cellular 49mm Natural
  Titanium Sand Trail Loop M/L (MJAQ4LS/A, UPC pending — single
  source only, M6 precedent), Nintendo Switch 2 Pro Controller
  Black (BEE-008, UPC 045496885861), Logitech MX Keys Mini Black
  (920-010475, UPC 097855169617), Samsung Galaxy Buds3 FE Black
  (SM-R420NZKAXAR, UPC 0198957213090). New snapshot
  `data/eval_snapshots_batch2_2026-11-06.json` holds 19 quotes
  across the 5 models (WF-1000XM6: 4, Ultra 4: 2, Pro Controller:
  5, MX Keys Mini: 3, Buds3 FE: 5), all DECISIONS 021-clean.
  Existing 33 entries untouched; no Amazon touch. Eval: 38 models,
  34 verified identifiers, 19 quotes, 0 identifier-matched, 19
  suspected. Two direct prices are price-only (stock not confirmed
  in page text): Sony direct WF-1000XM6 $298.00 and Apple direct
  Ultra 4 $799.00.

- Expansion batch 3 (DECISIONS 024, user 2026-11-06): eval set
  38 → 42 models — Sony PlayStation 5 Pro 2TB White
  (1000046529 / CFI-7019B01X, UPC 711719595946), Nintendo Switch
  OLED Model Neon Blue/Neon Red set (HEGSKABAA, SKU 115464, UPC
  045496883409), Logitech Lift Graphite (910-006466, UPC
  097855170927), Meta Quest 3 512GB (899-00583-01, UPC
  815820024071). Apple AirPods 5 was NOT added: already in the
  set since 2026-10-31 as `apple-airpods-5-usbc` (MKFW4LL/A, UPC
  195951378978) — the batch is 4 new models, not 5. New snapshot
  `data/eval_snapshots_batch3_2026-11-06.json` holds 13 quotes
  across the 4 models (PS5 Pro: 4, OLED Neon: 2, Lift: 3,
  Quest 3: 4), all DECISIONS 021-clean. Existing 38 entries
  untouched; no Amazon touch. Eval: 42 models, 38 verified
  identifiers, 13 quotes, 0 identifier-matched, 13 suspected.
  One direct price is price-only (stock not confirmed):
  PlayStation Direct PS5 Pro $899.00 — the console is broadly out
  of stock in the US since mid-September 2026.

- Expansion batch 4 (DECISIONS 025, user 2026-11-06): eval set
  42 → 47 models — Apple iPad mini (A20 Pro) Wi-Fi 128GB Standard
  Glass Starlight (MJ6J4LL/A, UPC 195951205595; released
  2026-11-06), Sony PlayStation 5 Slim Digital Edition 825GB White
  (CFI-2015, UPC 711719541035), Nintendo Joy-Con 2 (L)/(R) Light
  Blue / Light Red pair (BEEAJAAAA, UPC 045496885892), Logitech
  G502 X PLUS Black HERO 25K (910-006160, UPC 097855166951),
  Google Pixel Buds 2a Hazel (GA06155-US, UPC 840353930506).
  Membership check re-run against the 42-model set (BUILD_LOG 041):
  no candidate matched an existing model by name, MPN, or UPC, so
  all five were added — no split, no drop. New snapshot
  `data/eval_snapshots_batch4_2026-11-06.json` holds 15 quotes
  across the 5 models (iPad mini A20: 3, PS5 Digital: 2, Joy-Con 2:
  2, G502 X PLUS: 4, Pixel Buds 2a: 4), all DECISIONS 021-clean.
  Existing 42 entries untouched; no Amazon touch. Eval: 47 models,
  43 verified identifiers, 15 quotes, 0 identifier-matched, 15
  suspected. Three direct prices are price-only (stock not
  confirmed): Apple direct iPad mini $699.00, Logitech direct G502
  X PLUS $159.99 (current PDP defaults to the HERO 44K refresh),
  Google Store Pixel Buds 2a $129. Open items: G502 X PLUS HERO
  44K UPC (part numbers conflict across retailers), PS5 Digital
  UPC second-source strength (PayMore + eBay; Best Buy states no
  UPC).

- Expansion batch 5 (DECISIONS 026, user 2026-11-06): eval set
  47 → 52 models — Apple iPad Air 13-inch (M4) 128GB Wi-Fi Space
  Gray (MH5N4LL/A, UPC 195950797817), Sony DualSense Edge Black &
  White (CFI-ZCP1, UPC pending — three conflicting codes, no two
  independent US sources agree), Nintendo Joy-Con (L)/(R) Neon
  Red/Neon Blue pair (HACAJAEAA, UPC 045496590130), Logitech MX
  Vertical Graphite (910-005447, UPC 097855144461), Bose
  QuietComfort Earbuds (2024) Black (888507-0100, UPC
  017817853460). Membership check re-run against the 47-model set
  (BUILD_LOG 042): no candidate matched an existing model by name,
  MPN, or UPC, so all five were added — no split, no drop. New
  snapshot `data/eval_snapshots_batch5_2026-11-06.json` holds 15
  quotes across the 5 models (iPad Air 13: 2, DualSense Edge: 4,
  Joy-Con pair: 2, MX Vertical: 3, QC Earbuds: 4), all DECISIONS
  021-clean. Existing 47 entries untouched; no Amazon touch. Eval:
  52 models, 47 verified identifiers, 15 quotes, 0
  identifier-matched, 15 suspected. Two direct prices are
  price-only (stock not confirmed): Apple direct iPad Air 13
  $949.00, Bose direct QC Earbuds $119.00 sale (was $179.00, ends
  2026-11-08). Open items: DualSense Edge UPC (711719444190 vs
  711719585552 vs 711719586555); Bose candidate price $129
  corrected (list $179.00); MX Vertical $99.99 is the sale price,
  list $119.99.

### Changed

- Daily price refresh 2026-11-06 (first daily run): all 28 models
  re-queried through Meta Catalog (549 raw listings, 28 files
  `data/meta_catalog_raw_*_2026-11-06.json`, gitignored); new
  snapshot `data/eval_snapshots_2026-11-06.json` holds 56 quotes
  across 23 of 28 models (prior round: 59 quotes). No
  same-merchant price changed at all — every move is merchant
  churn (quotes appearing/disappearing) or a new merchant at a
  different price. Notable: WF-1000XM5 Black street price down
  (Suncoast $299.99 gone; Best Buy $248 sale, P.C. Richard $248
  sale, FocusCamera $199.99 new — the FocusCamera row is a >$5
  move and is flagged for a merchant-page recheck); MX Keys S
  down (ThinkEdu Pale Grey $138.99 gone from the feed; Staples
  $129.99, Lenovo $129.99, Newegg $117 sale new); Kindle now
  has 5 quotes with a new low of $196.99 (NFM); iPad Air M4
  B&H $699 deal and AirPods Max 2 Best Buy $499 deal are gone
  from the feed. Five models hold zero qualifying rows this
  round — a catalog-feed gap, not a delisting: Watch SE 3,
  MacBook Air 13 M5, MacBook Air 15 M5, iPad A16, iPad Pro M5
  11. MacBook Pro 14 M6 is in stock on launch day (Apple and
  Best Buy $1,999, launch-day browser check — the catalog round
  itself returned no base row); its UPC is still unpublished
  and the 2026-11-07 10:00 PT UPC check stands. MX Master 4
  Graphite still has no US retailer row (B&H also checked:
  no listing). Kindle entry unchanged (still B0CFPL6CFY),
  DualSense identifiers unchanged, no new models, no Amazon
  touch. Eval: 56 quotes, 0 identifier-matched, 56 suspected
  (catalog gives no UPC — the rule working, not a bug).

### Fixed

- Corrected the G Pro X Superlight 2 Black eval identifier from the
  European reference (910-006630 / EAN 5099206104525) to the US reference
  (910-006628 / UPC 097855177797), agreed by Abt (US), DirectDial,
  Best Buy Canada, and the Logitech G US store URL. The two $159.99
  quotes already collected stand.
- Anker 737 (A2148111) re-check: no qualifying US new-unit offer found
  as of 2026-10-31 (Ayoub Lebanon/A2148311 and Newegg marketplace
  TECHVAULT rows both excluded on browser verification). Entry keeps
  0 quotes; replacement or removal awaits a user decision, no
  auto-swap.
- DualSense White UPC conflict now counts five codes (added
  711719541226); still unresolved, no code promoted.
- Watch SE 3 (GPS) 40mm Midnight, S/M: first new-unit quote, BJ's
  $239.99, browser-verified 2026-10-31. The page states Model
  MEH94LW/A and UPC 195950387070, independently confirming the
  entry's part-number mapping. Combined quote coverage is now 27 of
  28 models; only Anker 737 still has no quote.
- Anker 737 retired and replaced by the Anker Prime Charger 100W
  (A2688, UPC 194644040635), user-confirmed. The old key
  anker-737-120w is retired, never reused. First quotes, both
  $69.99 (Anker direct, browser-verified in stock; B&H). All 28
  models now hold quotes.
- AirPods 4 retired and replaced by AirPods 5 with the USB-C case
  (MKFW4LL/A, UPC 195951378978), user-confirmed after the
  apple.com sweep found AirPods 4 no longer available. The old
  key apple-airpods-4-usbc is retired, never reused. First
  quotes, all $129 (Staples, Abt, Best Buy).
- MX Master 3S retired and replaced by MX Master 4 Graphite
  (910-007558, UPC 097855207623), user-confirmed after the
  Logitech sweep found no plain consumer 3S in the catalog. The
  old key logitech-mx-master-3s-graphite is retired, never
  reused. First quote: Logitech direct $119.99, browser-verified
  in stock (retailer Graphite rows pending).
- K8 Pro retired and replaced by K8 Ultra 8K (Black, Apex Red,
  SKU K8U-J1), user-confirmed after the Keychron sweep found the
  K8 Pro listed but sold out. The old key keychron-k8-pro is
  retired, never reused, and its $49.99 quote is not carried
  over. First quote: Keychron direct $119.99, browser-verified
  stocked in the US warehouse. Per-variant barcodes later found
  in Keychron's public product JSON (Red 4894979057969).

## [0.1.0] - 2026-10-31

First public release: the Phase 1 comparison core, working end to end from
the command line. Every price below is a snapshot: quotes expire after 24
hours by design and are flagged stale, never presented as live prices.

### Added

- Buyer-side comparison core: same-product matching by UPC / EAN / MPN /
  SKU. Title-similar listings go to a separate "suspected" table and never
  enter the ranking; ranking is decoupled from any revenue input.
- 28-model evaluation set (US market, standardized consumer electronics),
  26 verified identifiers. Every entry pins one exact configuration
  (model + color + storage / band / switch variant).
- Snapshot quote system: four dated snapshot files holding 55 quotes
  across 26 of 28 models (main, Apple, non-Apple, and Buds4 Pro rounds).
  Each quote records merchant, price, source URL, and collection time;
  shipping stays unknown and tax stays excluded unless a merchant page
  states them.
- Shopify public-JSON adapter and live-store CLI, verified against
  Keychron's official store (31 variants; the K8 Pro K8P-G1 quote is
  identifier-matched, the only matched quote so far — snapshot files
  carry no identifiers by design, so their quotes land in the suspected
  table).
- Full project documentation: README, PLAN, ARCHITECTURE, DECISIONS
  (001–009), ROADMAP, and a public BUILD_LOG (014 entries, including
  mistakes and rejected claims, not just wins).

### Known gaps (documented, not hidden)

- Anker 737 GaNPrime 120W (A2148): no current US quote found; availability
  unconfirmed, not declared discontinued.
- Apple Watch SE 3 (MEH94LW/A): no new-unit quote yet; the part-number
  mapping itself was corroborated by a refurbished listing.
- Sony DualSense White: four conflicting UPC codes from US sources;
  the entry stays pending until a tiebreaker (physical box barcode or a
  Sony spec sheet) appears.
- MacBook Pro 14 M6: UPC not yet published; the entry stays pending
  until post-launch retailer pages show it.
- Snapshot quotes go stale after 24 hours; the CLI flags them for
  re-check instead of presenting them as current prices.
