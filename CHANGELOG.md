# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
While the major version is 0, the API and snapshot formats may change in minor
releases; breaking changes are called out in the release notes.

## [Unreleased]

### Added

- Selection and quote-eligibility rules (DECISIONS 021, user
  2026-11-06): no third-party/marketplace sellers for now, no
  non-US-market goods, selection stays each brand's mainstream or
  new products with gradual expansion later. No catalog entry
  changes; the rule bites on quote eligibility only (the Newegg
  $117 Astonlink row is excluded from future snapshots).

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
