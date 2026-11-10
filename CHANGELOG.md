# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
While the major version is 0, the API and snapshot formats may change in minor
releases; breaking changes are called out in the release notes.

## [Unreleased]

### Added

- Identifier-bearing quote source (DECISIONS 059): Shopify public
  product JSON (tier 1) via new `price_agent/collect_identified.py`
  + `data/shopify_handles.json` (31 pinned-variant entries), and
  hand-verified retailer spec-page rows (tier 4) for the Apple
  cluster. New identified snapshot stream
  `data/eval_snapshots_identified_YYYY-MM-DD.json`; the merge
  (`price_agent/build_site_snapshot.py`) admits an offer into the
  verified ranking only when its identifier matches the catalog
  entry's verified MPN/UPC, with matched-only supersede and a
  build-failing guard against matched offers on pending models.
  Result: 31 identified offers across 29 models, 11 matched offers
  in 11 verified rankings (AirPods Pro 3, K8 Ultra 8K, Xbox
  controller, WF-1000XM6, Buds3 FE, Quest 3, Joy-Con 2, LinkBuds
  Fit, Magic Trackpad, Xbox Series X, JBL Xtreme 4); 20 rows stayed
  suspected, all correctly (14 pending models, 6 verified models
  with non-matching identifiers). Site rebuilt (470 offers);
  home/method/coverage copy now reflects the populated rankings.
  No catalog identifier changes, no rule relaxation, no spending,
  no registrations, no Amazon.

- Shopify expansion (DECISIONS 061): 50 new pinned variants across
  44 models added to `data/shopify_handles.json` (31 → 81 entries,
  25 merchants — Expercom, Datavision, Beach Camera, Focus Camera,
  Audio46, Heart Rate Monitors USA, Contender Bicycles, Incycle,
  Recovery For Athletes, CompTechDirect, 6ave, Keychron, HyperX).
  Main sweep collected 55 offers (26 skipped on rate-limits); a
  30 s-pace retry recovered 29 more. Result: verified ranking
  11 → 53 of 200 models, 58 matched offers, 517 total offers; all
  11 prior rankings intact; identifiers unchanged (98 verified /
  102 pending). Two rulings: Shopify Collective counts as
  brand-direct when the vendor of record is the brand's own
  official store (Meta Quest 3S); 7 out-of-stock pins held, not
  ingested (the renderer shows no out-of-stock label). Process
  fix: hand-verified rows now live in a separate
  `eval_snapshots_identified_hand_*.json` file the collector never
  overwrites (the B&H AirPods Pro 3 row was rescued from git after
  a sweep overwrote it). Still unranked: PS5 consoles, Logitech
  MX / Nintendo hardware, Google Pixel Buds, Razer DeathAdder V4
  Pro, Bose QC Earbuds / QC Headphones.

- Generic retailer JSON-LD parser ruled out (DECISIONS 060): raw
  fetch of 27 retailer pages found zero JSON-LD blocks (Target
  genuinely negative — client-side data via the redsky API; B&H,
  Best Buy, Newegg, Adorama, Walmart all bot-block raw fetches),
  and a live-browser check of 22 URLs verified exactly one
  JSON-LD Product block (Walmart MX Vertical, gtin13
  097855144461, $94). No parser built: no reliable automatable
  collection route exists (curl and text-fetch both hit Walmart's
  bot-check page, the W3C validator is flaky, no public product
  JSON endpoint, the affiliate API needs a key + registration).
  The Walmart MX Vertical row is a candidate 12th verified ranking
  but is NOT counted — its identifiers match the catalog exactly,
  but the seller was never verified. Coverage unchanged: 11 of 200
  models with a verified ranking. No code, catalog, or snapshot
  changes; record only.

- M6 UPC verified + Kindle re-pinned to the US code (DECISIONS 062):
  MacBook Pro 14 M6 (MHWT4LL/A) UPC 195951080291 confirmed by three
  independent retailers (B&H Photo $1,999.00, Adorama $1,999.00,
  Micro Center $1,999.99) and upgraded to verified on user
  confirmation; identifiers 98 → 99 verified / 101 pending.
  Kindle Paperwhite 16GB (2024) re-pinned from the non-US code
  B0CFPL6CFY / UPC 840268942847 to the US code B0CFPJYX7P / UPC
  840268989538 (NFM + CamelCamelCamel agree on the UPC; Best Buy
  US, Dell US, TrustedReviews, pricehistory.app confirm the US
  code); the old non-US pin is retired, never reused. No new
  verified rankings yet (no identifier-bearing M6 or Kindle quotes
  exist); site rebuilt, 54 models with a verified ranking, 650
  offers. Test count guard updated (98 → 99) and the pending-model
  fixture switched from the M6 to the DualSense Edge; 52 tests pass.

- M6 first verified ranking (hand row, DECISIONS 059 mechanism):
  B&H Photo $1,999.00 for the MacBook Pro 14 M6 (UPC 195951080291,
  in stock, price + UPC on the same spec page, re-verified
  2026-11-07 before ingest) added to the hand-identified file.
  Verified ranking 54 → 55 of 200 models, matched offers 60 → 61.

- Target redsky API ruled out (DECISIONS 063): one plain request
  returned HTTP 435 (PerimeterX captcha, no data); Target's terms
  ban commercial collection of listings/prices and automated
  tools, and redsky's robots.txt disallows everything. No
  collector built. Opportunity cost is real — Target carries 28
  of the 42 unranked priority models (lift would have been 23–28)
  — but unattainable via this route. Target hand rows need a fresh
  compliance call and are not cleared here.

- WF-C510 + InZone H5 identifiers verified (DECISIONS 064):
  WF-C510 UPC 027242930339 (B&H spec page + Abt agree); InZone H5
  UPC 027242927919 (Datavision + Focus Camera public product JSON
  agree at $128). Both upgraded to verified on user confirmation;
  identifiers 99 → 101 verified / 99 pending. Rankings 73 → 74
  (InZone H5 gains Datavision + Focus Camera $128). WF-C510 has no
  identifier-bearing quote yet, so its ranking stays empty.

- WF-C510 first verified ranking (hand row, DECISIONS 059 mechanism):
  B&H Photo $58.00 for the Sony WF-C510 (UPC 027242930339, in stock,
  price + UPC on the same spec page, re-verified 2026-11-08 before
  ingest) added to the hand-identified file. Verified ranking
  74 → 75 of 200 models, matched offers 82 → 83.

- Coverage round 5 (Micro Center): 0 new rows — the strict same-page
  bar (price + catalog UPC + In Stock on one page) cannot be met
  through text reads at Micro Center: /product/ pages show price +
  availability but never the specs table, while quickView pages show
  the specs (UPC/MPN) but never price or stock. Split evidence
  (same product ID) exists for 6 models and is held pending a
  decision on whether it counts: Joy-Con Neon $89.99, Portal
  $249.99, Switch Neon $339.99, Xbox Elite 2 $199.99, Dell S3225QS
  $329.99, Tab S10 FE+ $699.99 (accepting them would take the
  ranking 76 → 82; a live-browser check of the specs tab is the
  alternative that keeps the bar intact). Ranking stays 76/200.

- Switch neon MPN corrected HADSKABAA → HADSKABAH (DECISIONS 065):
  UPC 045496883775 belongs to HADSKABAH per Abt, Amazon and Best
  Buy; the old HADSKABAA barcode 045496882174 is the 2017
  revision. UPC unchanged; no ranking change.

- Identified-stream merge bug fixed (DECISIONS 066): the identified
  stream now unions across files per model instead of taking the
  latest file per model. Latest-per-model had silently dropped the
  Switch 2 Micro Center hand row (the hand file's meta timestamp
  is stale, so retry3's mismatched BrandsMart row won) and the
  Edge 850 Incycle row lost to a 429 in round 2. Live-browser
  verification of the 10 Micro Center/Abt pages confirmed 7 rows
  (Joy-Con $89.99, Portal $249.99, Switch Neon $339.99, Dell
  S3225QS $329.99, Tab S10 FE+ $699.99, Switch OLED White $399.99,
  Switch 2 $499.99, all Micro Center, Tustin in stock); Xbox Elite
  2 has no Micro Center listing at all and Watch SE 3's Micro
  Center page is the Midnight variant (different UPC/MPN), so
  neither got a row. Ranking 76 → 83, matched offers 84 → 92.
  Regression test added.

- DeathAdder V4 Pro first verified ranking (hand row, DECISIONS 059
  mechanism): Abt $169.99 for the Razer DeathAdder V4 Pro Black
  (UPC 840272920718, MPN RZ01-05330100-R3U1, price + UPC + MPN on
  the product page, live-browser verified 2026-11-08). Stock
  evidence is ADD TO CART available plus Abt's search listing
  showing "In Stock"; added on user approval. Verified ranking
  83 → 84 of 200 models, matched offers 92 → 93.

- PS5 Digital 825GB corrected per DECISIONS 067 (user approved
  option B): variant MPN CFI-2015 → "CFI-2100 model group";
  UPC 711719541035 returned to pending (evidence points to the
  2020 launch CFI-1015B, not the Slim); status verified → pending.
  Model name and prices unchanged. Verified identifiers 101 → 100;
  verified ranking unchanged (model was never ranked).

- Out-of-stock annotation on offer tables (stabilization,
  DECISIONS 068): both product-page tables gained a Stock column
  ("In stock", or "Out of stock" in red bold). It surfaced two
  rows that were silently out of stock in the ranking: XM5 @ Focus
  Camera $198.00 and Xbox Series X 1TB @ ShopCGX $799.99. Counts
  unchanged; rows stay ranked, now labeled.

- Two Best Buy hand rows (live-browser verified 2026-11-08, spec
  pages carry UPC): Xbox Stereo Headset Black @ Best Buy $59.99
  (UPC 889842748031; snapshot feed price was $74.99) and Pixel
  Buds 2a Hazel @ Best Buy $129.00 (UPC 840353930506; Hazel page
  SKU 6642707). Verified ranking 84 → 86 of 200, matched offers
  93 → 95. Not added: WF-1000XM5 (marketplace seller),
  MX Master 4 graphite (no Best Buy listing found), Kindle
  Paperwhite (clean page but the "Amazon exclusive, skip" note
  needs a separate user decision).

- Price history page deferred to early December (DECISIONS 069):
  only 3 days of daily snapshots exist; the dated snapshots in git
  already are the complete record. Merged snapshot renamed to the
  rolling `data/site_snapshot.json` (was dated 2026-11-06 but
  overwritten every rebuild).

- Coverage round 4 — Abt hand rows (1 new ranking, 75 → 76):
  Logitech G Pro X Superlight 2 Black @ Abt $159.99 (UPC
  097855177797, InStock, price + UPC on the same page,
  re-verified 2026-11-08 before ingest) added to the
  hand-identified file. The other 24 models failed at Abt: mostly
  not carried or discontinued; PS5 Digital ($599.99) and
  PlayStation Portal ($249.99) are in stock and priced but their
  UPCs do not surface in the fetched page text; Switch 2 ($499.99
  InStock) fails the MPN rule (Abt's MPN is BEESKB6AA, not
  BEE-001). Switch neon evidence recorded (Abt page shows
  HADSKABAH + UPC 045496883775) — catalog pairing still open.

- Coverage round 3 (2026-11-07, BUILD_LOG 086): the 26
  verified-but-unranked models were re-checked against fresh
  B&H/Adorama pages — 0 new hand rows. The models are mostly not
  carried or discontinued at those two retailers; where in stock,
  the UPC does not surface in the page text (G Pro X Superlight 2,
  Lift). Closest near-misses: Bose QC Headphones @ Adorama $359
  (UPC confirmed, no "In Stock" wording) and Boom 2 @ B&H (UPC
  confirmed, still out of stock). Ranking stays 75/200, matched
  offers 83. No snapshot or site change.

- Coverage round 2 (Shopify + hand rows): verified ranking 55 → 73
  of 200 models, matched offers 61 → 80. Four new JustPressPlay
  pins (Switch 2 Pro Controller $89.99, Switch Pro Controller
  $79.99, Switch OLED Neon $399.99, Switch Lite Turquoise $229.99)
  and 16 hand-verified rows across 14 models (14 B&H + 2 Adorama).
  A full-sweep overwrite dropped 2 rankings while 28 pins were
  rate-limited; a 30 s-pace retry recovered all but Edge 850 @
  Incycle (still 429). No catalog identifier changes (99/101).
  Identifier evidence collected as proposals only (strongest:
  WF-C510, InZone H5).

- Phase 2 website v1 (DECISIONS 058, ROADMAP §3.2 M1.3): pure static
  site — home + search across the 200 models, one compare page per
  model, a method-and-principles page, and a coverage-and-gaps page.
  New `price_agent/build_site_snapshot.py` merges all 46 eval snapshots
  into `data/site_snapshot_2026-11-06.json` (200 models, 98 verified /
  102 pending identifiers, 448 offers, 182 models with offers); new
  `price_agent/build_site.py` renders `site/` (203 pages). Honest by
  construction: snapshot offers carry no identifier, so the verified
  ranking is empty on every product page and all offers appear only in
  a clearly labeled title-matched table; prices older than 24h are
  labeled "Needs re-check". Excluded from this build (M1.4, later):
  alert subscription, read-only API, price history, Apple showcase.

- Expansion batch 26 (DECISIONS 048, continuous expansion per
  DECISIONS 027): eval set 150 → 155 models, verified identifiers
  stay 74 (0 of 5 new identifiers verified — all pending; no UPC
  surfaced for any of the five Lenovo part numbers). New: Lenovo
  Legion Tab Gen 3 8.8-inch Gaming Tablet, Eclipse Black
  (ZAEF0068US, UPC pending — no code surfaced; $549.99 at Lenovo
  direct, InStock — the first Lenovo tablet and first Android
  gaming tablet in the set), Lenovo Tab Plus Gen 2 12.1-inch
  Tablet, Celestial White (ZAHT0078US, UPC pending — no code
  surfaced; $469.99 at Lenovo direct, $299.99 at Newegg — the
  current $469.99 supersedes the stale $269.99–$299.99 sale
  prices), Lenovo Idea Tab Pro Gen 2 13-inch Tablet, Cloud Grey
  (ZAHD0826US, UPC pending — no code surfaced; $399.99 sale vs
  $549.99 list at Lenovo direct, $527.99 at Newegg — bundle
  contents conflicted: feed says folio case + pen included,
  droidgadgets says neither), Lenovo Tab One 8.7-inch Tablet,
  Luna Grey (ZAF00008US, UPC pending — no code surfaced; $149.99
  sale vs $199.99 est. value at Lenovo direct — Best Buy's
  $99.99 is a different part, ZAF00067US, and was not used),
  Lenovo Yoga Tab Plus Gen 2 13-inch Tablet, Cosmic Blue
  (ZAHX0159US, UPC pending — no code surfaced; $799.99 sale vs
  $999.99 list at Lenovo direct — the flagship creator tablet).
  Lenovo is a new brand in the set; the Lenovo US store was
  readable again this round after being unreadable in the
  previous round. Not added: the remaining Lenovo candidates
  (Legion Tab Gen 5, Yoga Tab Gen 2, Idea Tab, Idea Tab Plus,
  Tab P12) stay list-only for later batches.
- Expansion batch 27 (DECISIONS 049, continuous expansion per
  DECISIONS 027): eval set 155 → 160 models, verified identifiers
  74 → 76 (2 of 5 new identifiers verified). New: Xbox Series X
  1TB Disc Edition, Black (RRT-00001, UPC 889842640724 —
  Micro Center + marknet agree; $799.99 at Microsoft direct,
  the Aug 1, 2026 list price — the set's first Xbox console;
  stock caveat: OutOfStock at Micro Center and ShopCGX),
  Xbox Series S 512GB All-Digital, Robot White (UPC pending —
  part numbers conflict: Micro Center EP2-10050 / UPC
  196388421343 vs eBay RRS-00001 / UPC 0889842651317; $499.99
  at Microsoft direct), Xbox Wireless Headset, 2024 refresh,
  Black (identifiers pending — no MPN/UPC surfaced; $110.99 at
  Microsoft direct, $1 above the $109.99 launch — the stale
  $99.99 feed row is the 2021-model price), Xbox Stereo
  Headset, Black (8LI-00001, UPC 889842748031 — Ubuy + eBay
  agree; $59.99 at Microsoft direct and Verizon, unchanged
  since the Sep 2021 launch), Surface Laptop, 13.8-inch
  (8th Edition), Snapdragon X2 Plus 10-core / 16GB / 512GB,
  Platinum (EP2-59028, identifiers pending — MPN single AU
  source only; $1,299.99 sale vs $1,599.99 list at Microsoft
  direct, Best Buy $1,199.99 reported — the set's first Surface
  device and first Microsoft laptop). Microsoft grows from 4 to
  9 entries. Not added: Surface Slim Pen 2 (MPN 8WV-00001 vs
  8WX-00001 conflict), Xbox Rechargeable Battery + USB-C Cable
  SXW-00001 (UPC single source), Surface Pro 11th Edition (base
  config price not pinned cleanly), Xbox Series X 2TB Galaxy
  Black (sunset Aug 2026) and Xbox Series X25 Limited Edition
  ($899.99, launches Nov 13) — all stay list-only for later
  batches.
- Expansion batch 28 (DECISIONS 050, continuous expansion per
  DECISIONS 027): eval set 160 → 165 models, verified identifiers
  76 → 80 (4 of 5 new identifiers verified). New: Garmin
  vívoactive 6, Slate with Black silicone band (010-02985-00,
  UPC 753759342807 — Petra + HeartRateMonitorsUSA agree;
  $299.99 at Garmin direct, Dell Temporarily Out of Stock —
  the set's first Garmin entry), Garmin Venu 4 45mm, Silver
  stainless steel bezel with Silver Gray silicone band
  (010-03014-01, UPC 753759342883 — Petra +
  HeartRateMonitorsUSA agree; $549.99 at Garmin direct, Dell
  $499.99 sale — the set's first Venu), Garmin Forerunner 570
  42mm, Raspberry Aluminum with Translucent Bone/Mango band
  (010-02970-02, UPC 753759349820 — Target US + Selenal.lv
  agree; $549.99 at Garmin direct and Target, In Stock — the
  set's first Forerunner), Garmin Edge 1050 cycling computer,
  device only, Black (010-02890-00, UPC 753759336288 —
  HeartRateMonitorsUSA + 6ave + Pro's Closet + SunnySports
  agree; $699.99 at Garmin direct — the set's first cycling
  computer and first entry in the new "cycling-computers"
  category; the Edge 1060 launched Oct 20, 2026 at $799.99
  but the 1050 is still sold at $699.99, not discontinued),
  Garmin fēnix 9 47mm, Titanium with Pebble Gray silicone
  band (010-04762-00, identifiers pending — MPN confirmed by
  Garmin US + Abt + RA Cycles, no UPC surfaced; $999.99 at
  Garmin direct, Abt and NFM — the set's first fēnix).
  Garmin is a new brand in the set (0 → 5 entries). Not
  added: Forerunner 970 47mm Carbon Gray DLC Titanium
  010-02969-00 ($749.99 — UPC conflicted: Amazon + Snapklik
  753759349929 vs a single eBay listing 753759349899, and the
  -01 variant is likewise conflicted; needs a dedicated
  tiebreak), Edge 1060 ($799.99, too new for UPC
  verification), Fenix 8 47mm AMOLED (superseded by the
  fēnix 9, now discounted last-gen), Instinct 3, Forerunner
  165, Edge 850 and Garmin dash cams (not yet swept) — all
  stay list-only for later batches.
- Expansion batch 29 (DECISIONS 051, continuous expansion per
  DECISIONS 027): eval set 165 → 170 models, verified identifiers
  80 → 81 (1 of 5 new identifiers verified). New: Lenovo Legion
  Tab Gen 5 8.8-inch Gaming Tablet, Eclipse Black (ZAH20126US,
  UPC 199275342448 — B&H Photo + TempDeals/edealinfo agree;
  $699.99 sale vs $899.99 list at Lenovo direct, $799.99 sale
  at B&H — the set's flagship Lenovo gaming tablet), Lenovo Yoga
  Tab Gen 2 11.1-inch Tablet, Cosmic Blue (ZAJ00250US, UPC
  pending — no code surfaced; $599.99 sale vs $729.99 list at
  Lenovo direct, pen + keyboard included — the set's mid-size
  Lenovo creator tablet), Lenovo Idea Tab 11-inch Tablet, Luna
  Grey (ZAFR0923US, UPC pending — no code surfaced for this
  part; the Amazon UPCs for ZAFR0920US/ZAFR0925US/ZAFR0928US
  are different parts and were not copied; $269.99 at Lenovo
  direct — the set's entry-level Lenovo student tablet), Lenovo
  Idea Tab Plus 12.1-inch Tablet, Cloud Grey (ZAG71084US, UPC
  pending — no code surfaced; $369.99 at Lenovo direct, $279.00
  at Newegg — the current Lenovo-direct part is the 6GB config,
  not the earlier-reported 8GB $339.99), ASUS ROG Swift OLED
  PG27UCDM 27-inch 4K 240Hz Gaming Monitor, Black
  (90LM0B30-B019B2, UPC pending — candidate 197105815193 is
  tied to the EU part, not the US part; $1,099 at ASUS eShop
  USA and Newegg — the set's 27-inch 4K Tandem QD-OLED
  flagship). Lenovo grows 5 → 9 entries, ASUS 10 → 11. Not
  added: Lenovo Tab P12 (2023 tablet — no longer sold at
  Lenovo US, effectively discontinued in the US), Lenovo Yoga
  Tab Gen 1 ZAG60266US ($659.99 — superseded by the Yoga Tab
  Gen 2), ASUS ROG Harpe Mini Core (already in the set, batch
  25 — duplicate catch), ThinkPad Universal USB-C Dock
  40AY0090US (no Lenovo US direct price; reseller prices
  $148.99–$309 conflict), Alienware AW720M (2022 mouse, Dell
  US price unconfirmed, no UPC), ASUS ROG Delta original (no
  current ASUS row) — all stay list-only for later batches.
- Expansion batch 30 (DECISIONS 052, continuous expansion per
  DECISIONS 027): eval set 170 → 175 models, verified identifiers
  81 → 84 (3 of 5 new identifiers verified). New: Samsung Galaxy
  Watch9 40mm Bluetooth, Graphite (SM-L340NZKAXAA, UPC pending —
  candidate 198957310546 is Samsung-MSRP-list-only, no second
  source; $379.99 at Samsung direct, Best Buy and Abt — the
  first Samsung wearable in the set and its current mainstream
  smartwatch), Samsung Galaxy Watch8 Classic 46mm Wi-Fi/Bluetooth,
  Black (SM-L500NZKAXAA, UPC 198957093562 — Samsung Wearables
  MSRP lists ×4 editions + eBay GTIN agree; $499.99 at Samsung
  direct and Best Buy — the still-current Classic, no Watch9
  Classic exists), Samsung Galaxy Watch Ultra2 47mm LTE, Titanium
  Silver (SM-L715UZSAXAA, UPC 198957393730 — Samsung Wearables
  MSRP list + T-Mobile URL sku agree; $699.99 at Samsung direct,
  Best Buy and Abt — the rugged flagship), Samsung Galaxy Tab S11
  11-inch 128GB Wi-Fi, Gray (SM-X730NZAAXAR, UPC pending — no
  code surfaced for the exact pinned US part; $999.99 at Samsung
  direct and Best Buy, $899.99 at Macy's — the first Samsung
  tablet in the set and its flagship 11-inch tablet), Samsung
  Galaxy Tab S10 FE 10.9-inch 128GB Wi-Fi, Gray (SM-X520NZAAXAR,
  UPC 887276992266 — Samsung tablet MSRP lists ×6 editions +
  manuals.plus mirror agree; $549.99 at Samsung direct and Best
  Buy, $529.99 at BJ's — the mid-range FE tablet). Samsung grows
  3 → 8 entries; no phones and no TVs added (new categories, out
  of scope). Not added: Galaxy Buds3 Pro (out of the Samsung US
  catalog, superseded by the Buds4 Pro), Galaxy Buds Core (not
  sold in the US — LatAm/MEA stock only), Galaxy Watch8 40mm
  (superseded by the Watch9), Tab S11 Ultra / Tab A11+ / Tab S10
  FE+ (held for later batches) — all stay list-only.
- Expansion batch 31 (DECISIONS 053, continuous expansion per
  DECISIONS 027): eval set 175 → 180 models, verified identifiers
  84 → 88 (4 of 5 new identifiers verified). New: Samsung Galaxy
  Tab S11 Ultra 14.6-inch 256GB Wi-Fi, Gray (SM-X930NZAAXAR, UPC
  pending — candidate 198957230080 is Samsung-MSRP-list-only, no
  second source; $1,299.99 at Samsung direct and Best Buy,
  $1,320.99 out of stock at Quill — the flagship 14.6-inch
  tablet), Samsung Galaxy Tab A11+ 11-inch 128GB Wi-Fi, Gray
  (SM-X230NZAIXAR, UPC 198957270390 — Samsung tablet MSRP lists
  ×2 editions + eBay agree; $299.99 at Samsung direct, Best Buy
  and Walmart — the entry-level 11-inch tablet), Samsung Galaxy
  Tab S10 FE+ 13.1-inch 128GB Wi-Fi, Gray (SM-X620NZAAXAR, UPC
  887276992563 — Samsung tablet MSRP lists ×7 editions +
  manuals.plus mirror agree; $699.99 at Samsung direct, Best Buy
  and bkstr — the big-screen FE tablet), Garmin Forerunner 165
  43mm, Black/Slate Gray, non-Music (010-02863-20, UPC
  753759326593 — Snapklik + Cycle Superstore + Evolution Bikes
  agree; $249.99 at Garmin direct, Crutchfield and Running
  Warehouse — Garmin's entry-level AMOLED running watch), Garmin
  Edge 850 (010-03023-00, UPC 753759356644 —
  HeartRateMonitorsUSA + The Pro's Closet agree; $599.99 at
  Garmin direct, Best Buy and BikeTiresDirect — the compact
  mid-tier Edge). Samsung grows 8 → 11 entries, Garmin 5 → 7.
  Not added: Galaxy Buds3 base, Tab S9 FE and Tab A9+ (all three
  Samsung US buy pages now redirect to their successors — out of
  the current catalog), Galaxy Buds3 Pro and Buds Core (still
  out / not sold in the US), Galaxy Watch8 40mm (superseded),
  Garmin Instinct 3 (held for a later batch) — all stay
  list-only.
- Expansion batch 35 (DECISIONS 057, continuous expansion per
  DECISIONS 027) — FINAL batch of the 175 → 200 leg: eval set
  195 → 200 models, verified identifiers 97 → 98 (1 of 5 new
  identifiers verified). New: JBL Xtreme 4, Black
  (JBLXTREME4BLKAM, UPC 050036398190 — Amazon US + Ubuy agree,
  GTIN 11200130008129 on both, Best Buy US confirms the MPN;
  $379.95 list / $309.95 sale at JBL direct, $379.99 at Target
  and Rock & Soul — JBL's mainstream large portable speaker
  beside the set's Flip 7 and Charge 6; the feed's Best Buy
  $299.99 row was sold by Simple Cell, Inc, a marketplace seller,
  and was excluded), Razer Basilisk V3 Pro 35K, Black
  (RZ01-05240100-R3U1, identifiers pending — no US UPC found,
  EU EAN 8886419334606 not used; $159.99 at Razer direct,
  $159.99 / $99.99 sale at Macy's, $167.99 at CDW, $127.00 at
  ShopMyExchange — Razer's ergonomic flagship mouse beside the
  set's Viper V4 Pro and DeathAdder V4 Pro), Garmin Forerunner
  265, Black — Black Bezel and Case with Black/Powder Gray
  Silicone Band, 46mm (010-02810-00, identifiers pending — no UPC
  found for the -00 suffix, 753759313715 belongs to the -10
  suffix; $449.99 at Abt, Kohl's, BikeTiresDirect, BuyDig and
  Sportsman's — Garmin's mainstream 46mm AMOLED running watch
  beside the set's Venu 3/4, Forerunner 570 and fēnix 9), Corsair
  K70 CORE RGB, Black, no palm rest (CH-910971E-NA, identifiers
  pending — no UPC found, the palm-rest variant's 840006665762
  not used; $99.99 list / $79.99 sale at Corsair direct, the only
  clean quote — the feed's Newegg $99.99 / $79.99 row is the
  Steel Gray and was excluded as the wrong color — Corsair's
  mainstream full-size wired keyboard beside the set's K65 Plus
  Wireless), ASUS ROG Keris II Ace, Black (90MP03N0-BMAA00,
  identifiers pending — no US UPC found, EU BMUA00 EAN
  4711387394571 not used; $109.99 sale at ASUS eShop US,
  $159.99 list / $118.99 sale at MicroCenter — the retry of the
  batch 34 hold, whose reason is gone now that a clean
  ASUS-direct Black row exists; the ultralight 54 g ergonomic
  mouse beside the set's ROG Gladius IV Ace and Harpe Mini Core).
  JBL grows 6 → 7 entries, Razer 6 → 7, Garmin 9 → 10, Corsair
  5 → 6, ASUS 12 → 13. The eval set reaches exactly 200 models —
  the target set by DECISIONS 027 — and expansion stops here.
  Not added: Anker Soundcore Boom 2 Plus Black (no clean
  single-color US row pinned), Microsoft Bluetooth Ergonomic
  Mouse and Dell UltraSharp U3425WE (carried over, still messy /
  bundle-only) — all stay list-only.
- Expansion batch 34 (DECISIONS 056, continuous expansion per
  DECISIONS 027): eval set 190 → 195 models, verified identifiers
  94 → 97 (3 of 5 new identifiers verified). New: JBL Charge 6,
  Black (JBLCHARGE6BLKAM, identifiers pending — candidate UPC
  050036407441 is Amazon US + Canex CA, needs a second US
  non-Amazon source; $199.95 list / $149.95 Early Black Friday
  sale at JBL direct, T-Mobile and Dell, $149.95 at Sweetwater
  and Crutchfield — JBL's mainstream portable speaker with a
  built-in powerbank; the Best Buy $149.95 row was sold by
  Electronic Express, a marketplace seller, and was excluded),
  Razer DeathAdder V4 Pro, Black (RZ01-05330100-R3U1, UPC
  840272920718 — Amazon US + Layup agree, Best Buy US confirms
  the MPN; $169.99 at Razer direct, Newegg, Abt and Best Buy,
  $166.99 at NFM — Razer's ergonomic esports flagship beside the
  set's Viper V4 Pro), Anker Soundcore Boom 2, Phantom Black
  (UPC 194644188276 — B&H + Romanian importer label agree; MPN
  not recorded, B&H states A3138011 while Target US states
  A3138012; $129.99 at soundcore direct — page-read fresh,
  superseding the feed's stale $139.99 anker.com rows — $99.99
  sale at Target, $139.99 at Newegg — the first Anker/Soundcore
  speaker in the set), Garmin Venu 3, Black — Slate Stainless
  Steel Bezel (010-02784-01, UPC 753759314743 — Petra US
  distributor + PB Tech NZ + HeartRateMonitorsUSA table agree;
  $449.99 at Kohl's, Best Buy and Cabela's, $449.99 list /
  $299.99 Dell sale — the previous-generation 45mm AMOLED health
  watch beside the set's Venu 4), Keychron Q1 Max, Carbon Black
  / Gateron Jupiter Brown (Q1M-M3, identifiers pending — barcode
  4895248870609 is Keychron-store-only, no second source; $229.99
  at Keychron direct and Best Buy — the retry of the batch 33
  hold, whose reason is gone now that Keychron-direct + Best Buy
  rows exist). JBL grows 5 → 6 entries, Razer 5 → 6, Anker
  6 → 7, Garmin 8 → 9, Keychron 8 → 9. Not added: ASUS ROG
  Keris II Ace Black (no clean brand_direct Black row), Samsung
  Galaxy Buds Core (Latin American stock and marketplace rows
  only, no clean US row), Keychron K3 Max (no feed row at all),
  Corsair HS80 MAX Black (no Black variant exists — White and
  Steel Gray only), Microsoft Bluetooth Ergonomic Mouse and Dell
  UltraSharp U3425WE (carried over from batch 33, still messy /
  bundle-only) — all stay list-only.
- Expansion batch 33 (DECISIONS 055, continuous expansion per
  DECISIONS 027): eval set 185 → 190 models, verified identifiers
  91 → 94 (3 of 5 new identifiers verified). New: Bose SoundLink
  Max, Black (883848-0100, UPC 017817848817 — Adorama spec table
  + Layup agree; $399.00 at Bose direct on sale $329.00, Adorama
  and Abt — the largest Bose portable speaker in the set), Bose
  QuietComfort Headphones (2023), Black (884367-0100, UPC
  017817848961 — Best Buy specs + Reverb + BuyAdvanced GTIN
  agree; $359.00 list, $169.00 Black Friday sale at Bose direct,
  $359.00 at Crutchfield — the standard QC line beside the set's
  QC Ultra 2nd Gen; the Best Buy $225.00 marketplace row was
  excluded), Keychron K2 Max, Black / RGB Backlight Aluminum
  Frame / Keychron Super Banana (K2M-C4, identifiers pending —
  barcode 4895248880271 is Keychron-store-only, no second source;
  $114.99 at Keychron direct, available — the 75% QMK wireless
  board; single quote this round, no second US retailer row for
  the exact variant), ASUS ProArt Display PA279CRV (UPC
  195553951531 / MPN PA279CRV — B&H + EPA ENERGY STAR + EPEAT
  agree; $429.00 at ASUS eShop, B&H and ASUS direct — the retry
  of the batch 32 hold, whose reason is gone now that
  ASUS-direct rows exist; the first ProArt monitor in the set),
  HyperX Cloud III Gaming Headset, Black (727A8AA, identifiers
  pending — candidate UPC 197029008220 is Amazon-lineage only,
  same call as the set's Black-Red Cloud III; $99.99 at HP
  direct, $69.99 Holiday Deal at Best Buy — the all-Black
  colorway of the set's Black-Red Cloud III). Bose grows 6 → 8
  entries, Keychron 7 → 8, ASUS 11 → 12, HyperX 6 → 7. Not
  added: Microsoft Bluetooth Ergonomic Mouse (feed messy after
  Microsoft's accessories exit — Incase rows, a Peach $107.98
  Microsoft row, no clean Black US row to pin), Dell UltraSharp
  34 Curved U3425WE (bundle rows only, no clean standalone
  Dell-direct row), Keychron K3 Max and Q1 Max (no clean feed
  rows) — all stay list-only.
- Expansion batch 32 (DECISIONS 054, continuous expansion per
  DECISIONS 027): eval set 180 → 185 models, verified identifiers
  88 → 91 (3 of 5 new identifiers verified). New: Garmin Instinct
  3 AMOLED 45mm, Black with Black Band (010-02936-00, UPC
  753759339487 — distributor feed row + DID Electrical EAN agree;
  $349.99 at Garmin direct, $332.99 in stock at Abt — the held
  Garmin wearable from batch 31), Bose SoundLink Flex (2nd Gen),
  Black (887612-0100, UPC 017817852470 — B&H + Volza import
  records agree; $159.00 at Bose direct, Abt and B&H — the first
  Bose speaker in the set), Bose SoundLink Plus, Black
  (894040-0100, UPC 017817857932 — B&H + manuals.plus agree;
  $269.00 at Bose direct, $179.00 in stock at B&H and Abt on a
  rebate ending Nov 8 — the new mid-tier speaker, launched Jun
  2025), Keychron K2 HE Special Edition, Black, Nebula Switch V1
  (K2H-F1, identifiers pending — EAN conflict: Keychron store
  JSON 4895248889175 vs B&H 4895248889199, no tiebreak; $139.99
  at Keychron direct, available — the 75% Hall Effect board, a
  2025 CES Innovation Award winner), Dell UltraSharp 27 4K
  Thunderbolt Hub Monitor U2725QE (MPN 95WRG, UPC pending —
  candidate 884116484578 is B&H-only; $849.99 at Dell direct,
  $649.99 at B&H and Adorama — the 27-inch sibling of the set's
  U3225QE). Garmin grows 7 → 8 entries, Bose 4 → 6, Keychron
  6 → 7, Dell 4 → 5. Not added: Garmin Dash Cam 67W (verified on
  its own terms — Garmin direct $259.99, UPC 753759269395 — but
  a dash cam is a camera and DECISIONS 016 defers cameras to the
  category-expansion phase, so no new category is opened
  mid-Phase-1), ASUS ProArt Display PA279CRV (no ASUS-direct
  feed row, street rows thin) — both stay list-only.
- Expansion batch 25 (DECISIONS 047, continuous expansion per
  DECISIONS 027): eval set 145 → 150 models, verified identifiers
  stay 74 (0 of 5 new identifiers verified — all pending). New:
  ASUS ROG Swift OLED PG32UCWM 32-inch 4K 240Hz Gaming Monitor,
  Black (90LM0DN0-B019B1, UPC pending — code 199291571570 is
  B&H-only; $1,399.00 at ASUS direct and B&H, $1,399.99 at
  Newegg — ASUS's 32-inch Tandem RGB OLED flagship monitor, the
  second ASUS monitor in the set), ASUS ROG Swift OLED PG27AQDPR
  27-inch QHD 500Hz Gaming Monitor, Black (UPC pending — no code
  surfaced; $729.00 sale vs $899.00 list at ASUS direct, $999.99
  at Best Buy — ASUS's 500Hz QD-OLED monitor, the third ASUS
  monitor in the set; temporarily out of stock at ASUS direct),
  ASUS ROG Delta USB-C Gaming Headset, Black (90YH01D1-B2UA00,
  UPC pending — no US code surfaced; $149.99 at ASUS direct,
  $102.78 at Newegg — the original 2018 ESS Quad-DAC ROG
  headset, the second ASUS headset in the set; out of stock at
  ASUS direct), ASUS ROG Harpe Mini Core Gaming Mouse, Black
  (90MP04D0-BMAA02, UPC pending — code 199291014046 is B&H-only;
  $44.99 at ASUS direct, $29.99 at B&H, $32.00 at Newegg — the
  52 g value wired mouse, the second ASUS mouse in the set),
  ASUS ROG Pelta Gaming Headset, Black (90YH0410-BHAA00, UPC
  pending — the only code found, 199291069725, is for the
  non-US White part; $104.99 sale vs $129.99 list at ASUS direct
  — the tri-mode wireless headset, the third ASUS headset in the
  set). Not added: the remaining ASUS held candidates stay
  list-only for later batches.

- Expansion batch 24 (DECISIONS 046, continuous expansion per
  DECISIONS 027): eval set 140 → 145 models, verified identifiers
  73 → 74 (1 of 5 new identifiers verified). New: Dell 27 Plus 4K
  Monitor S2725QS, Ash White (T4CNF, UPC pending — code
  884116485117 is Amazon-only; $299.99 at Dell direct, $299.99 at
  Newegg, $284.99 at ThinkEdu — Dell's mainstream 27-inch 4K 120
  Hz monitor, the second Dell monitor in the set), Dell UltraSharp
  32 4K Thunderbolt Hub Monitor U3225QE, Silver (3PVPJ, UPC
  884116484561 verified — B&H Photo + CompTechDirect agree;
  $1,029.99 at Dell direct, $799.99 at Target, $799.00 at Adorama,
  $949.99 at CDW — Dell's flagship 32-inch 4K IPS Black hub
  monitor, the first UltraSharp in the set), Alienware 32 Curved
  Gaming Monitor AW3225DM, Dark Blue (VX89X, UPC pending — only
  the Icecat EAN 5397184962725; $249.99 sale at Dell direct,
  $319.99 at Best Buy — Alienware's budget 32-inch curved QHD
  gaming monitor, the second Alienware monitor in the set),
  Alienware Tri-Mode Wireless Gaming Keyboard AW920K, Dark Side of
  the Moon (6R87M, UPC pending — the only code found, 884116448686,
  is Icecat-only for the Lunar Light colorway; $159.99 at Dell
  direct — Alienware's first tri-mode wireless keyboard, the second
  Alienware keyboard in the set), Dell Pro 7 Webcam 4K WB726, Black
  (G4MYM, UPC pending — only the Icecat EAN 5397321028925 for the
  EMEA part; $199.99 at Dell direct — Dell's flagship AI webcam,
  the first webcam in the set — new category "webcams"). Not added:
  all Dell laptops and desktops (configurable, no retailer-pinned
  base configuration — DECISIONS 015); the remaining Dell held
  candidates stay list-only for later batches.

- Expansion batch 23 (DECISIONS 045, continuous expansion per
  DECISIONS 027): eval set 135 → 140 models, verified identifiers
  stay 73 (0 of 5 new identifiers verified — all pending). New:
  ASUS ROG Swift OLED PG27UCWM 27-inch 4K 240Hz Gaming Monitor,
  Black (UPC pending — code 199291335226 is B&H-only; $1,199.00 at
  ROG US and B&H, temporarily out of stock / coming soon — ASUS's
  flagship Tandem RGB OLED monitor, the first ASUS monitor in the
  set), ASUS ROG Delta II Wireless Gaming Headset, Black
  (90YH03W0-BHAA03, UPC pending — the UK EAN 4711387604847 was not
  carried across regions; $185.99 InStock at ASUS eShop USA,
  $199.99 at Target — ASUS's flagship tri-mode headset, the first
  ASUS headset in the set), ASUS ROG Gladius IV Ace Wireless
  Gaming Mouse, Black (P729 ROG GLADIUS IV ACE/BLK, UPC pending —
  no MPN/UPC surfaced; $169.99 InStock at Best Buy — ASUS's
  flagship 8K esports mouse, the first ASUS mouse in the set),
  ASUS ROG Azoth 96 HE Wireless Gaming Keyboard, Black
  (90MP040H-BKAA20, UPC pending — code 199291008571 is
  Amazon-only; $359.99 InStock at ASUS eShop USA, $339.99 sale at
  Target — ASUS's flagship Hall-effect keyboard, the first ASUS
  keyboard in the set), ASUS ROG Cetra Open Wireless Gaming
  Earbuds, Black (90YH0450-BTAA00, UPC pending — PBTech/LittleBit
  code 199291232747 conflicts with Amazon's 199291232754, neither
  recorded; $229.99 at ASUS eShop USA and Best Buy — ASUS's
  flagship open-ear gaming earbuds, the first ASUS earbuds in the
  set). ASUS is a new brand in the set; no new category enters.
  Not added: all ASUS laptops and desktops (configurable, no
  retailer-pinned base configuration — DECISIONS 015), limited
  20th-anniversary editions, and the remaining ASUS candidates,
  which stay list-only for later batches.

- Expansion batch 22 (DECISIONS 044, continuous expansion per
  DECISIONS 027): eval set 130 → 135 models, verified identifiers
  72 → 73 (1 of 5 new identifiers verified). New: HP OMEN 27k UHD
  144Hz Gaming Monitor, Black (780G8AA#ABA, UPC pending — the HP
  datasheet lists no (ABA) UPC, only (ABB) 197029615961 and (ABU)
  197029615992; $370.32 at HP direct — HP's mainstream 4K 144 Hz
  gaming monitor, the first HP 4K monitor in the set), HyperX OMEN
  OLED 27q QHD 240Hz Gaming Monitor, Black (CH0R2AA#ABA, UPC
  pending — HP datasheet code 199642944442 conflicts with
  Amazon's 199642944428, neither recorded; $399.99 sale at HP
  direct, $379.99 at Best Buy — HyperX's mainstream QD-OLED
  monitor, the first OLED monitor in the set), HyperX Cloud III S
  Wireless Gaming Headset, Black-Red (A59Z0AA, UPC 198415435569
  verified — PBTech retailer listing + trippodo spec database
  agree; $179.99 at HP direct, $129.99 at Best Buy and Target —
  HyperX's flagship wireless headset, the first HyperX wireless
  headset in the set), HyperX Pulsefire Haste 2 Pro 4K Wireless
  Gaming Mouse, Slate Grey (A1KY5AA, UPC pending — code
  198122802432 is Currys UK only; $119.99 at HP direct, $99.99 at
  Best Buy — HyperX's first true-4kHz mouse, the first HyperX
  mouse in the set), HyperX QuadCast 2 S USB Microphone, Black
  (9A273AA, UPC pending — code 197961186741 is HP-manual-only,
  all other sources are Amazon; $149.99 sale at HP direct —
  HyperX's flagship USB streaming mic, the first microphone in
  the set — new category "microphones", decided explicitly in
  DECISIONS 044). Not added: all OMEN / Victus / HP laptops and
  OMEN 35L desktops (configurable, no retailer-pinned base
  configuration — DECISIONS 015) and all HyperX bundles (bundles,
  not standalone lines); the remaining HP candidates stay
  list-only for later batches.

- Expansion batch 21 (DECISIONS 043, continuous expansion per
  DECISIONS 027): eval set 125 → 130 models, verified identifiers
  71 → 72 (1 of 5 new identifiers verified). New: HP OMEN 27s FHD
  240Hz Gaming Monitor, Black (780G5AA#ABA, UPC pending — the US
  (ABA) code 197029615442 is HP-datasheet-only; $389.99 at HP
  direct, $309 at Newegg — HP's mainstream 240 Hz FHD gaming
  monitor, the first HP monitor in the set), HyperX Cloud III
  Gaming Headset, Black-Red (727A9AA, UPC pending — the only UPC
  found, 197029008237, is Amazon-only; $99.99 at HP direct,
  $104.59 at Staples — HyperX's mainstream wired headset, the
  first HyperX headset in the set; the sweep's 4P5M0AA MPN was a
  bundle/upsell code and was not used), HP 920 Ergonomic Vertical
  Mouse, Black (6H1A4AA#ABA, UPC 197029640277 verified — HP
  datasheet + eBay US product catalog agree; $68.99 sale at HP
  direct, $68.99 at Best Buy — HP's ergonomic vertical mouse, the
  first HP mouse in the set), HP OMEN 27q G2 QHD 180Hz Gaming
  Monitor, Black (AV4H6AA#ABA, UPC pending — the HP datasheet
  lists no (ABA) UPC; $203.99 sale at HP direct, $218.99 at
  Newegg — HP's mainstream 180 Hz QHD gaming monitor, the first
  HP QHD monitor in the set), HyperX Alloy Rise 75 Mechanical
  Gaming Keyboard, Black, US Layout, HyperX Red - Linear, wired
  (7G7A4AA#ABA, UPC pending — the US (ABA) code 197192334096 is
  HP-leaflet-only; $84.99 sale at HyperX direct, $84.99 at Best
  Buy and Target — HyperX's flagship customizable 75% board, the
  first HyperX keyboard in the set). Not added: all OMEN / Victus
  / HP laptops and OMEN 35L desktops (configurable, no
  retailer-pinned base configuration — DECISIONS 015) and all
  HyperX bundles (bundles, not standalone lines); the remaining HP
  candidates stay list-only for later batches.

- Expansion batch 20 (DECISIONS 042, continuous expansion per
  DECISIONS 027): eval set 120 → 125 models (the 125-model
  milestone), verified identifiers 69 → 71 (2 of 5 new identifiers
  verified). New: Dell 32 Plus 4K Monitor S3225QS, Ash White
  (F06FR, UPC 884116485131 verified — Icecat datasheet + eBay US
  product catalog agree; $329.99 sale at Dell direct, $379.99 at
  Best Buy, $399.99 at Micro Center — Dell's current mainstream
  32-inch 4K monitor, the first Dell monitor in the set),
  Alienware 27 240Hz QD-OLED Gaming Monitor AW2726DM, Black (JW05F,
  UPC pending — only the EU EAN 5397321030553 on a single Icecat
  datasheet; $319.99 sale at Dell direct, $349.99 at Best Buy —
  Alienware's current budget QD-OLED monitor, the first Alienware
  monitor in the set), Alienware Pro Wireless Gaming Mouse, Dark
  Side of the Moon (PRO-MS-G-DEAM, UPC 884116464914 verified —
  Icecat datasheet + axitech.be Black listing agree; $129.99 sale
  at Dell direct, $160.99 at Newegg — Alienware's flagship pro
  mouse), Alienware Pro Wireless Gaming Keyboard, Dark Side of the
  Moon (WR47C, UPC pending — the only UPC found, 884116464853,
  belongs to the Lunar Light board; $174.99 sale at Dell direct,
  $294.99 at Newegg — Alienware's flagship pro keyboard),
  Alienware Pro Wireless Gaming Headset, Dark Side of the Moon
  (UPC pending — 884116469728 on manuals.plus alone, 884116469759
  is the Lunar Light code; $174.99 sale at Dell direct, $199.99 at
  Best Buy — Alienware's flagship pro headset). Not added: all Dell
  laptops and desktops (configurable, no retailer-pinned base
  configuration — DECISIONS 015; Alienware 16 Aurora featured
  config also Sold Out); the remaining Dell/Alienware candidates
  stay list-only for later batches. All five sale prices should be
  re-checked after the Early Black Friday event ends Nov 8.
- Expansion batch 19 (DECISIONS 041, continuous expansion per
  DECISIONS 027): eval set 115 → 120 models, verified identifiers
  stay 69 (all 5 new Corsair identifiers stay pending on
  single-source-only or no-source codes). New: Corsair M65 RGB
  Ultra, Black, wired (CH-9309411-NA2, UPC pending — 840006657613
  on the Micro Center feed row only; the original CH-9309411-NA
  SKU is Discontinued; $59.99 at Corsair direct and Micro Center,
  $84.99 at CDW — Corsair's flagship wired FPS mouse, the first
  Corsair entry in the set), Corsair K65 Plus Wireless, Midnight
  Grey, MLX Red linear (CH-91D401L-NA, UPC pending — no UPC
  surfaced anywhere; $159.99 at Corsair direct and Best Buy — a
  $129.99 crawl is treated as a lapsed sale; Corsair's current 75%
  wireless keyboard), Corsair Virtuoso Max Wireless, Carbon
  (CA-9011372-WW, UPC pending — 840440484615 on manuals.plus +
  eBay + Amazon only, no retailer or manufacturer listing states
  it; $249.99 at Corsair direct and Best Buy, a holiday sale price
  vs the $299.99 list — Corsair's flagship wireless headset),
  Corsair FRAME 4000D RS ARGB, Black (CC-9011296-WW, UPC pending —
  840440487715 on Amazon.in only; $119.99 at Corsair direct,
  $114.99 at Newegg — suspected, the feed title reads 'Non-LED' —
  the first PC case in the set), Corsair iCUE LINK Titan II 360 RX
  RGB, Black (CW-9061037-WW, UPC pending — GTIN 840440419464 on
  Scan UK only; $179.99 at Corsair direct, Best Buy and Newegg —
  Corsair's current flagship 360 mm AIO, the first CPU cooler in
  the set). Not added: K70 MAX and RM850x (Discontinued); XENEON
  27QHD240 OLED (direct OutOfStock); WARTHOG case (pre-order
  only); Vengeance RGB DDR5 32GB 6000 CL30 (volatile pricing);
  M65 RGB Ultra Wireless and HS80 Max Wireless (list-only for
  later batches). No controller pick — Corsair sells no
  first-party controller on corsair.com US.
- Expansion batch 18 (DECISIONS 040, continuous expansion per
  DECISIONS 027): eval set 110 → 115 models, verified identifiers
  stay 69 (all 5 new Razer identifiers stay pending on
  single-source-only or no-source codes). New: Razer Viper V4 Pro,
  Black (RZ01-05630100-R3U1, UPC pending — no US UPC surfaced;
  the EU EAN 8887910085134 belongs to the R3G1 variant and was not
  copied; $159.99 at Razer direct and Best Buy, $156.99 at NFM —
  Razer's current flagship symmetrical esports mouse, the first
  Razer entry in the set), Razer BlackWidow V4 Pro, Green switches,
  Black (RZ03-04680200-R3U1, UPC pending — 840272903315 on the B&H
  page only; $229.99 at Razer direct, $199.99 at B&H, $267.93 at
  Staples — Razer's flagship full-size keyboard), Razer BlackShark
  V3 Pro, PC version, Black (RZ04-05400100-R3U1, UPC pending —
  840272919484 on Amazon listings only; $249.99 at Razer direct,
  Best Buy and Electronic Express — Razer's flagship esports
  headset), Razer Wolverine V3 Pro, Black (RZ06-05200100-R3U1, UPC
  pending — no UPC surfaced anywhere; $199.99 at Razer direct,
  $169.99 at Best Buy, $166.99 at NFM — Razer's flagship Xbox/PC
  controller), Razer Kraken V4 Pro, Black (RZ04-05160100-R3U1, UPC
  pending — PBTech's 840272909980 is listed against the R3M1
  variant; $399.99 at Razer direct, $299.99 at Best Buy and Beach
  Camera — Razer's flagship haptic lifestyle headset). Not added:
  DeathAdder V4 Pro and Basilisk V4 Pro (both $169.99, list-only
  for later batches); Blade laptops (configurable — no single
  retailer-pinned base config, DECISIONS 015).
- Expansion batch 17 (DECISIONS 039, continuous expansion per
  DECISIONS 027): eval set 105 → 110 models, verified identifiers
  68 → 69 (the Flip 7 Black is verified; the other 4 new
  identifiers stay pending on single-source-only or no-source
  codes). New: JBL Flip 7, Black (JBLFLIP7BLKAM, UPC 050036407342
  verified — JBL/Harman Salsify syndication catalog + eBay
  listing agree; $129.95 sale at JBL direct, $129.99 at Target —
  the first JBL entry and the first portable Bluetooth speaker in
  the set), JBL Tour One M3 Smart Tx, Black (JBLTOM3AVIBLKAM, UPC
  pending — 050036414029 on snapklik + tanotis aggregators only;
  $449.95 at JBL direct, Abt and Best Buy — the $199.95 sale has
  ended; JBL's flagship over-ear ANC headphones, the first JBL
  headphones in the set), JBL Tour Pro 3, Black
  (JBLTOURPRO3BLKAM, UPC pending — 050036402392 on Amazon
  listings only; $329.95 at JBL direct, Crutchfield and Abt —
  JBL's flagship true-wireless earbuds, the first JBL earbuds in
  the set), JBL Bar 1300XMK2, Black (JBLBAR1300XM2BLKAM, UPC
  pending — 050036414869 on Amazon + an eBay refurbished listing
  + Target Plus partner data only; $1,699.95 at JBL direct, Best
  Buy and Abt, $1,199.95 sale at Macy's — the first soundbar in
  the set; the US XMK2 with a 12-inch sub is a different regional
  variant from the non-US 1300MK2), JBL PartyBox Stage 320,
  Black (JBLPBSTAGE320AM, UPC pending — no UPC surfaced
  anywhere; $569.95 at JBL direct, $629.95/$629.99 at Best Buy
  and Target — the first party speaker in the set). Not added:
  the PartyBox 330 (new 2026 successor — US price conflicting,
  $499.95 vs $630, revisit next sweep).

- Expansion batch 16 (DECISIONS 038, continuous expansion per
  DECISIONS 027): eval set 100 → 105 models, verified identifiers
  stay 68 (all 5 new identifiers pending on single-source-only or
  no-source codes). New: Anker MagGo 2 Pro Magnetic Power Bank
  (10K, Qi2 25W, Active Cooling), Phantom Gray (A110R, UPC pending
  — no UPC surfaced anywhere; $109.99 at Anker direct and Newegg
  — Anker's flagship magnetic power bank, the first magnetic power
  bank in the set), Anker Prime Power Bank (26K, 300W), Black
  (A110A, UPC pending — no US UPC on any retailer spec page;
  $199.99 sale at Anker direct, $229.99 at Best Buy — Anker's
  flagship laptop power bank, the first high-capacity power bank in
  the set), Anker Desktop USB-C Hub, 10-in-1 Dual 4K (A210C, UPC
  pending — 194644340506 only on pickoryx, which mirrors the Amazon
  ASIN listing; $79.99 sale at Anker direct — the first USB-C hub in
  the set), Anker Prime Wireless Car Charger (MagGo, AirCool, Pad)
  (A2933, UPC pending — no UPC surfaced anywhere; $89.99 at Anker
  direct and Target — the first car-mount charger in the set; the
  anker.com feed row saying $135 is stale, the live page says
  $89.99), Anker Nano Charger (70W, 3 Ports), Black Stone (B121A,
  UPC pending — 194644241247 for Black on Amazon listings only;
  $39.99 at Anker direct, Newegg and Impulse Cameras — Anker's
  compact 3-port 70W GaN charger; the Anker page says B121A while
  Notebookcheck/Amazon say A121A, the Anker page takes precedence).
  Not added: the Nano Charger (45W, Smart Display, A121D) — two
  different US pages ($34.99 PreOrder vs $39.99 InStock) with no
  color-to-variant mapping stated, so no color can be pinned cleanly;
  the Nano 70W replaces it as this batch's charger pick.

- Expansion batch 15 (DECISIONS 037, continuous expansion per
  DECISIONS 027): eval set 96 → 100 models, verified identifiers
  stay 68 (all 4 new identifiers pending on single-source-only or
  no-source codes). New: Apple Studio Display XDR, Standard glass,
  Tilt- and height-adjustable stand (MFEL4LL/A, UPC pending — the
  B&H UPC 195950527650 belongs to the VESA MFEN4LL/A and was not
  copied; $3,299 confirmed current at Apple direct, Best Buy and
  Abt — the separate mini-LED 120Hz XDR line vs the non-XDR Studio
  Display 2026), Sony MDR-M1, Black (MDRM1, UPC pending —
  027242930612 on the B&H spec page only; $268 at B&H and
  Sweetwater, $269.99 at Vintage King — Sony's modern pro reference
  closed monitor line vs the 1991 MDR-7506), Sony MDR-MV1, Black
  (MDRMV1, UPC pending — 027242926585 in an eBay listing only;
  $339.99 matched no US price, the MSRP is $419.99 and the street
  price is $418–$419.99 at Sweetwater, Macy's, SoundPure, Unique
  Photo and Impulse Cameras — the open-back reference monitor
  sibling of the M1), Keychron B39, 96% Alice, Deep Black (B39-K9,
  UPC pending — SKU on the Keychron page only; $54.99 confirmed
  current at Keychron direct, the only seller — the larger 96%
  sibling of the 75% B40). Sony INZONE H7 was NOT added: it is
  discontinued by Sony and only ListenUp still lists it ($228.00);
  the "~$349.99 launch price" was wrong (it launched in 2022 at
  $229.99 US). New snapshot
  `data/eval_snapshots_batch15_2026-11-06.json` holds 17 quotes
  across the 4 models (Studio Display XDR: 5, MDR-M1: 6, MDR-MV1:
  5, B39: 1). DECISIONS 021 applied to every quote:
  no marketplace/third-party rows, no non-US rows, no Amazon.

- Expansion batch 14 (DECISIONS 036, continuous expansion per
  DECISIONS 027): eval set 92 → 96 models, verified identifiers
  stay 68 (all 4 new identifiers pending on single-source-only or
  no-source codes). New: Sony MDR-7506, Black (MDR7506, no UPC
  surfaced on any US spec page; $114.99 confirmed current at Sony
  direct, $113 at Abt and Sweetwater — the set has no MDR model),
  Sony PlayStation Pulse Wireless Headset, White ($99.99 pre-order,
  launches 2026-11-19, no identifiers published yet — the new base
  planar-magnetic headset below the Elite, not the PULSE 3D),
  Sony LinkBuds Clip, Black (WF-LC900/B, UPC pending —
  027242934054 on the BuyDig spec table only; $229.99 is the launch
  SRP, the current street price is $198 at Best Buy, Sweetwater,
  BuyDig and Abt), Nintendo 64 Controller, Gray (HAC-043, Nintendo
  SKU 128577, UPC pending — 00045496894948 on the Nintendo US page
  only; $49.99 was the 2021 launch price, the current Nintendo
  direct price is $54.99, paid Nintendo Switch Online membership
  required to purchase). Apple Pro Display XDR was NOT added: it
  was discontinued March 3, 2026 and replaced by the Studio Display
  XDR — the $3,299 candidate figure is the Studio Display XDR
  launch price, not a Pro Display XDR configuration; the Studio
  Display XDR itself was not substituted in and is a candidate for
  a future batch. New snapshot
  `data/eval_snapshots_batch14_2026-11-06.json` holds 15 quotes
  across the 4 models (MDR-7506: 8, Pulse: 1, LinkBuds Clip: 5,
  N64 controller: 1). DECISIONS 021 applied to every quote:
  no marketplace/third-party rows, no non-US rows, no Amazon.

- Expansion batch 13 (DECISIONS 035, continuous expansion per
  DECISIONS 027): eval set 87 → 92 models, verified identifiers
  stay 68 (all 5 new identifiers pending on single-source-only
  codes). New: Apple MacBook Pro 14-inch with PROLED XDR Display,
  M5 Pro 15-core/16-core, 24GB/1TB, Space Black, Standard display
  (MJ2K4LL/A, UPC pending — 195951196749 in the Adorama spec table
  only; $2,899 at Apple direct and Best Buy — the base 14-inch runs
  M5 Pro, not M6, and is the distinct touchscreen tandem-OLED line
  vs the M6 and the Liquid Retina M5 Pro), Sony WF-C510 Black
  (WFC510/B, UPC pending — 027242930339 on the B&H spec page only;
  $69.99 is the list price, the current street price is $58 at B&H,
  Abt, Electronic Express and Focus Camera, $59.99 at Best Buy),
  Sony INZONE H5 Black (WHG500/B, UPC pending — 027242927919 in the
  Sony spec sheet via manuals.plus only; the ~$249.99 candidate
  price matches no current US price — the current street price is
  $128 at Focus Camera, Datavision and Abt, comp. value $178),
  Logitech PRO X2 SUPERSTRIKE LIGHTSPEED, Lunar Eclipse
  (910-007700, UPC pending — 097855211309 on the B&H spec page
  only; $179.99 — the candidate note called this a keyboard, it is
  a wireless gaming mouse, and the $199.99 Best Buy row is the newer
  PRO X3 SUPERSTRIKE, a different model), Keychron B40 75% Alice,
  Deep Black (B40-K9, no UPC/EAN found; $49.99 confirmed current at
  Keychron direct, the only colorway sold). New snapshot
  `data/eval_snapshots_batch13_2026-11-06.json` holds 17 quotes
  across the 5 models (PROLED XDR: 2, WF-C510: 6, INZONE H5: 3,
  Superstrike: 5, B40: 1). DECISIONS 021 applied to every quote:
  no marketplace/third-party rows, no non-US rows, no Amazon.

- Expansion batch 12 (DECISIONS 034, continuous expansion per
  DECISIONS 027): eval set 82 → 87 models, 66 → 68 verified
  identifiers. New: Apple Magic Keyboard with Touch ID and Numeric
  Keypad USB-C, US English, White Keys (MJM64LL/A, UPC pending —
  195951258324 stated on the Apple US store page only; $179 at
  Apple direct, $179.99 at Best Buy — the $99–$199 candidate range
  spanned three different models, and the 2026 MJM64LL/A supersedes
  the older MXK73LL/A), Sony WF-C710N Black (WFC710N/B, UPC
  027242931770; $129.99 is the list price while the current
  street/sale price is $98 at Best Buy, Abt, Crutchfield and Beach
  Camera), Sony LinkBuds Open Black (WFL910/B, UPC 027242928695;
  $229.99 confirmed current at Sony direct and Dell — Sony direct
  stock is low, "Only 3 left"), Logitech PRO X TKL LIGHTSPEED GX
  Brown Tactile Black (920-012127, UPC pending — 097855188984 in
  eBay product identifiers only; $219.99 is the current list, launch
  SRP was $199; Logitech G direct US price not confirmed in page
  text), Keychron Q1 Version 2 Fully Assembled Knob, Navy Blue - B,
  Gateron G Pro Red (Q1-O1Z, EAN pending — 4895248817345 in the
  Keychron product JSON only; $89.99 sale, was $189.99 — the
  $229.99–$254.99 candidate range was the Q-line range, the Q1 Max
  is $229.99). New snapshot
  `data/eval_snapshots_batch12_2026-11-06.json` holds 16 quotes
  across the 5 models (Magic Keyboard: 3, WF-C710N: 5, LinkBuds
  Open: 4, PRO X TKL: 3, Q1: 1). DECISIONS 021 applied to every
  quote: no marketplace/third-party rows, no non-US rows, no Amazon.

- Expansion batch 11 (DECISIONS 033, continuous expansion per
  DECISIONS 027): eval set 77 → 82 models, 62 → 66 verified
  identifiers. New: Apple Magic Trackpad USB-C White (MXK93AM/A,
  UPC 195949654305; $129 is the White price — the Black trackpad
  is $149 and is a different colorway), Sony WH-CH720N Black
  (WHCH720N/B, UPC 027242925397; $89.99 is the current Sony direct
  sale price while retailer street price is $178–$180), Logitech
  G915 X LIGHTSPEED full-size Tactile Black (920-012670, UPC
  097855195005; the $129.99 candidate price was an Amazon
  Clicky-switch deal — the standard US Tactile is $259.99, B&H
  $219.99 sale), Microsoft Xbox Adaptive Controller White
  (JMU-00003, UPC pending — 889842295368 vs 889842439038 conflict,
  no US retailer spec page; JMU-00001 is the older listing, no
  longer available new), Keychron K8 hot-swappable Red (K8-G1, UPC
  617748997921; the base K8 starts at $59.99 soldered, the pinned
  hot-swappable Red is $69.99 — K8-G1 stock flips between reads).
  New snapshot `data/eval_snapshots_batch11_2026-11-06.json` holds
  12 quotes across the 5 models (Trackpad: 3, CH720N: 3, G915 X:
  3, Adaptive: 2, K8: 1). DECISIONS 021 applied to every quote:
  no marketplace/third-party rows, no non-US rows, no Amazon.

- Expansion batch 10 (DECISIONS 032, continuous expansion per
  DECISIONS 027): eval set 72 → 77 models, 60 → 62 verified
  identifiers. New: Apple Studio Display (2026) Standard glass,
  Tilt-adjustable stand (MFEX4LL/A, UPC 195950529173 — the current
  Studio Display is the March 2026 refresh with Thunderbolt 5 and
  Desk View, not the 2022 A13 model; B&H $1,549.00 sale, Apple/Abt
  $1,599.00), Sony LinkBuds Fit Black (WFLS910N/B, UPC
  027242929289; list $229.99, current street $198.00–$199.99),
  Sony Access Controller White (retail MPN 1000037579, CFI-ZAC1,
  UPC pending — the only barcode seen, 711719567929, is a UK EAN),
  Logitech POP Keys Cosmos (920-011233, UPC pending — the only UPC
  found, 097855179401, is Amazon-only), Xbox Elite Wireless
  Controller Series 2 – Core White (4IK-00001, UPC pending — the
  only barcodes seen, AU 889842717082 vs LV 889842717075,
  conflict). New snapshot
  `data/eval_snapshots_batch10_2026-11-06.json` holds 15 quotes
  across the 5 models (3 each). DECISIONS 021 applied to every
  quote: no marketplace/third-party rows, no non-US rows, no
  Amazon.

- Expansion batch 9 (DECISIONS 031, continuous expansion per
  DECISIONS 027): eval set 67 → 72 models, 58 → 60 verified
  identifiers. New: Mac Studio M5 Max 36GB/512GB Silver (MHL64LL/A,
  UPC 195951078564 — the current Mac Studio is the M5 Max
  generation, not the M4 Max MU963LL/A at $1,999),
  Sony ULT WEAR Black (WHULT900N/B, UPC 027242928688; list $249.99,
  current street price $148.00 at three retailers), Sony PULSE
  Explore Midnight Black (retail MPN 1000044170, UPC pending — the
  only US UPC seen, 711719587972, is Amazon-only), Logitech Wave
  Keys Graphite (920-011898, UPC pending — 920-012059 is the MK670
  combo, not the standalone keyboard), Bose Sport Open Earbuds
  Black (901149-0010, UPC pending — a new 2026 product, not the
  2021 original 857628-0010). New snapshot
  `data/eval_snapshots_batch9_2026-11-06.json` holds 15 quotes
  across the 5 models (3 each). DECISIONS 021 applied to every
  quote: no marketplace/third-party rows, no non-US rows, no
  Amazon.

- Expansion batch 8 (DECISIONS 030, continuous expansion per
  DECISIONS 027): eval set 62 → 67 models, 55 → 58 verified
  identifiers. New: iMac 24-inch M6 10-core Blue (MH094LL/A, UPC
  195950838091 — the new iMac is M6, not M5, and skips M5 entirely;
  on sale 2026-11-06), Sony WH-1000XM4C Black (WH1000XM4C/B, UPC
  pending — the 2026 M4 refresh, not the XM5/XM6 flagships),
  Sony PULSE Elite Midnight Black (retail MPN 1000044173, UPC
  pending — not CFI-ZWH1, which is the PULSE 3D headset),
  Logitech ERGO K860 Graphite (920-009166, UPC 097855151667;
  current first-party list $149.99, not the Oct 31 Amazon-only
  sale price $119.99), Keychron K8 HE Special Edition Black
  (K8H-F1, EAN 4894979028990 — $139.99 is the Special Edition;
  the $129.99 Standard is currently out of stock at Keychron).
  New snapshot `data/eval_snapshots_batch8_2026-11-06.json` holds
  13 quotes across the 5 models (iMac: 3, XM4C: 3, PULSE Elite: 3,
  K860: 3, K8 HE: 1 — the K8 HE is sold only through Keychron's
  own store). DECISIONS 021 applied to every quote: no
  marketplace/third-party rows, no non-US rows, no Amazon.

- Expansion batch 7 (DECISIONS 029, continuous expansion per
  DECISIONS 027): eval set 57 → 62 models, 51 → 55 verified
  identifiers. New: MacBook Neo 13-inch 256GB Blush (MHFH4LL/A,
  UPC pending — the only Neo UPC found, 195950852745, is Indigo
  MHFF4LL/A's and was not copied across colors), PlayStation 5
  Slim Console 1TB disc (CFI-2100 model group, retail MPN
  1000049888, UPC 711719021452 — not CFI-2016, which is the EU
  disc code), Nintendo Switch Pro Controller Black (HAC-013;
  retail MPN HACAFSSKA, UPC 045496590161), Logitech MX Mechanical
  full-size Tactile Quiet Graphite (920-010547, UPC 097855174659;
  current list $179.99, not the Oct 31 sale price $149.99),
  Xbox Elite Wireless Controller Series 2 Black (FST-00001, UPC
  889842196344). New snapshot
  `data/eval_snapshots_batch7_2026-11-06.json` holds 14 quotes
  across the 5 models (Neo: 2, PS5 1TB: 3, Pro Controller: 3, MX
  Mechanical: 3, Elite Series 2: 3). DECISIONS 021 applied to every
  quote: no marketplace/third-party rows, no non-US rows, no Amazon.

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

- Logitech Lift Graphite hand row (B&H Photo $74.99, In Stock, UPC
  097855170927, live-browser verified 2026-11-09, user-approved):
  matched offers 98→99, verified rankings 86→87. B&H/Adorama
  re-probe of the other 9 verified-unranked models found no addable
  row (5 not listed at either merchant; Watch SE 3 wrong MPN at
  Adorama; Anker Prime 100W page UPC 194644289638 conflicts with
  catalog 194644040635 — flag open; Bose QC 884367-0100
  discontinued at B&H; Boom 2 out of stock at B&H).

- First 50-model expansion batch added (200 → 250 models, DECISIONS
  070, user-approved 2026-11-09): 22 UPC verified / 28 UPC pending
  (identifiers stay empty for pending, leads recorded); reserve
  Corsair HS80 v2 MAX held out; 7 flagged items kept in for
  add-time row verification. New category "handheld-consoles".
  Site copy and tests updated to 250 models / 122 verified / 128
  pending.

- PS5 1TB disc hand row (Best Buy $649.99, UPC 711719021452 /
  MPN 1000049888, live-browser verified 2026-11-10,
  user-approved): matched offers 96→97, verified rankings
  87→88. GameStop lists a different SKU (UPC 711719573364)
  — no row, no catalog change.

### Changed

- Daily price refresh 2026-11-07: full 200-model Meta Catalog sweep
  (3,984 raw listings, 200/200 calls OK); snapshot
  `data/eval_snapshots_2026-11-07.json` holds 580 quotes across 165
  of 200 models (prev: 192 quotes / 82 of 100 — the set grew to 200
  with the Shopify expansion, so the jump is coverage, not a price
  move). Identified stream: targeted retry of the 3 still-skipped
  products recovered Edge 850 @ Incycle and @ Contender Bicycles
  $599.99 and Forerunner 570 @ Recovery For Athletes $549.99 (all
  UPC-matched); Tab S10 FE+ @ Datavision still 404 (handle resolves
  on www, not the bare domain). Verified ranking 53 → 54 models
  (60 matched offers, 650 total offers in the site snapshot).
  Confirmed moves: PS5 Pro now $899.99 at PlayStation Direct,
  Boolchand and NFM (Sony raised the US list price $200 on Apr 2,
  2026 — the old $749.99 baseline is stale; sold out at major
  retailers ahead of GTA 6 on Nov 19); iPad Air M4 13" Apple
  $949.00 for MH5N4LL/A (apple.com JSON-LD confirms — up from the
  $799 launch price; the feed did not return the row today, so the
  snapshot has no Apple offer for this model); Nintendo Switch neon
  $299.99 at nintendo.com (SKU 117972-3, in stock — the $339.99
  listing is a stale duplicate); Target MX Master 4 Graphite
  $119.99 (browser-verified, Target A-95007381 — retailer hunt
  resolved, carried as a new quote). Feed rows proven wrong and
  excluded: DualSense Edge Macy's $224.95 (all-black variant, and
  the page says "Shipped and sold by Offer Express" — third-party
  marketplace; Macy's own price stays $209.99), DualSense White
  Kohl's $84.99 (page shows Color: Red, not White; Kohl's White
  stays $74.99), Samsung Buds4 Pro Target $219.99 ("Global Model"
  — non-US; US Target price $259.99), B&H MX Master 4 $319.98
  (MX Master 4 + MX Creative bundle). Unverified on the merchant
  page (feed-only): Lift Dell $69.99 / $79.99 (two Dell listings
  for the right-handed Graphite; Dell's page did not render a
  price), PlayStation Portal Macy's $288.99 -> $283.99, Buds4 Pro
  Target $259.99. Builder fixes (snapshot builder, durable copy in
  the goal hidden_files): non-US TLD list completed (.lb, .pa, .uk,
  .ee, .lt, .lv and 60+ more) + country-subdomain check (uy.jbl.com
  is JBL Uruguay — blocked); Shopezio block typo fixed
  ("shopeizio" -> "shopezio"); T-Mobile store-locator pages
  (/stores/pd/) excluded (monthly-installment prices poisoned the
  Watch 9 median — Samsung $379.99 / Best Buy $409.26 now kept);
  color words added (mocha, latte, whitestone, mist, porcelain,
  peony, moonstone) + Pop Keys colorway rule (Cosmos/Mist/
  Heartbreaker/Daydream/Blast); "global model/version" and
  "international model/version" excluded; handedness rule now
  catches "left mouse"; "12-core" spec strip + Unicode-hyphen
  normalization (Datavision Mac mini $898 recovered); "palm rest",
  "lock fit", "headphone cable/cord" excluded; designer-collab
  exclusion (Thom Browne $950 Bose row dropped); Roman-numeral
  suffixes (ii/iii/iv) and CN/UK/DE/FR/JP/KR layouts; title-word
  extra-suffix check (Forerunner 265S rows dropped). Sony patrol:
  WH-1000XM6 in stock at electronics.sony.com, $379.99 sale (was
  $459.99); PULSE 3D not listed on Sony's electronics store (it is
  a PlayStation product; sony.com/en-us/store/search is retired
  and 404s). Zero-quote models (35): feed gaps, not delistings —
  incl. G502 X Plus (feed returned only wrong-color / 44K-sensor
  rows today), PS5 Digital 825GB (original 825GB model
  discontinued), PULSE 3D. M6 Pro UPC 195951080291 confirmed by
  B&H, Adorama and Micro Center (10:00 PT check); catalog entry
  still pending until the user confirms the upgrade to verified.
  Kindle pin unchanged (B0CFPL6CFY). Eval: 580 quotes, 0
  identifier-matched, 580 suspected. 52 tests pass.
- Daily price refresh 2026-11-06 (second run, PM): scope frozen at 100
  models (92 swept at run start + 8 more; expansion batches 16+ join the
  consolidated snapshot tomorrow), 1,987 raw listings; the snapshot
  `data/eval_snapshots_2026-11-06.json` supersedes the morning 28-model
  file and holds 192 quotes across 82 of 100 models. One confirmed
  same-merchant move: Keychron Q1 $89.99 -> $69.99 (keychron.com sale,
  verified). One move unverified: WH-CH720N BJ's $179.99 -> $99.99
  (BJ's shows "Member Only Price", sign-in required; item in stock).
  Five feed rows proven wrong by merchant-page checks and excluded:
  PS5 Digital Best Buy $729 (RYTEK marketplace), Quest 3S Best Buy
  $422.82 (EZ Tech marketplace), Xbox controller Best Buy $89.25
  (IPC-STORE marketplace), Kindle Best Buy $229.99 (marketplace range
  top; Best Buy own price $199.99 carried forward, browser-verified),
  MX Vertical Dell $89.99 (page shows $119.99, carried) and Logitech
  $84.99 (page shows $99.99). Samsung Buds4 $135 was a Panama shop row
  (shop.samsung.com/latin/pa/) and is excluded; US price $179.99.
  PS5 Digital has no seller-direct quotes this round (Best Buy own
  listing out of stock). 18 models hold zero qualifying rows — feed
  gaps, not delistings. MX Master 4 Graphite retailer hunt (Walmart)
  blocked by a bot-check page, no workaround; still only Logitech
  direct $119.99. Apple patrol: no Apple model delisted. M6 Pro UPC
  still unpublished (2026-11-07 10:00 PT check stands). Kindle pin
  unchanged (B0CFPL6CFY). Eval: 192 quotes, 0 identifier-matched,
  192 suspected (catalog gives no UPC — the rule working, not a bug).
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

- Daily refresh 2026-11-10: first full 250-model Meta Catalog sweep
  (4,951 raw listings, 250/250 calls OK) + Shopify identified sweep
  (84 offers, 73 models; Datavision Tab S10 FE+ 404 skipped, same as
  2026-11-07/08/09). Twenty-five feed rows proven wrong and excluded
  via KNOWN_BAD, plus a beirutcart.com host block (Lebanon):
  accessories (Keychron Folio Case $29.99, V1 MAX PE Foam $12.00,
  Legion Go S Carry Case $24.99, silicone cover $8.04); wrong
  variant (Corsair M75 AIR (EU) $14.99, Alienware AW3425DWM $349.99,
  Forerunner 965 Whitestone/Powder Grey $599.99, Studio Display XDR
  nano glass $3,599); non-Sony access hardware (Covisec $94.99,
  Proteccontrols $369.50, Uslocksupply $177/$303, Homecontrols
  $168.95 — all Seco-Larm door-access gear); AT&T Galaxy Watch8
  $11.12/$11.95 monthly installments; MelroseMac standard display
  $2,899 is an XDR-priced variant on the merged page; Bose
  SoundLink Max $279 is Citrus, not Black; JBL Flip 7 $134.96 is
  White on jbl.pr/es; marketplace rows confirmed on their pages
  and excluded per DECISIONS 021 (Macy's PS5 $869.99 is Velztorm,
  Macy's XM5 $326.00 is Adorama, Best Buy Watch9 $446.54 is
  SpaceBound; Macy's SoundLink Plus page shows $269.00 from Offer
  Express, not the feed's $179.00; Bose QC Earbuds $119.00 is the
  Chilled Lilac page at $179.00). Confirmed moves (live-browser
  verified): JBL Flip 7 @ JBL $129.95 -> $149.95, Logitech MX
  Vertical @ Sweetwater $119.99 -> $99.99 (only 1 left), HyperX
  Cloud III S @ HyperX $139.99 -> $129.99, Keychron K2 HE @ Byok
  $139.99 -> $129.99. Identified stream: one move, Bose QC Ultra 2
  @ Beach Camera $399 -> $449 (page-verified). Merge fix:
  identified dedupe now collapses on (merchant, identifier)
  keeping the newest read, so stale prices no longer linger as
  second matched rows (QC Ultra 2, Flip 7 Datavision, Cloud III S,
  QuadCast 2 S, Alloy Rise 75); exact dedupe keeps the newest
  read for identical rows (QuadCast $149.99 -> $159.99 -> $149.99).
  Snapshot 679 offers / 205 models with quotes; site 776 offers,
  96 matched, 87 verified rankings (unchanged). PS5 1TB now has
  zero quotes — its only row was a marketplace listing. Tests 56
  pass (2 new regression tests).

- Anker Prime 100W first-row probe, Best Buy / Adorama
  (BUILD_LOG 105): Best Buy spec page matches UPC
  194644040635 and MPN A2688 at $69.99, but the offer is
  sold/shipped by marketplace seller AnkerDirect, so no
  row added; Adorama was bot-blocked and unverifiable.
  Spec-page route exhausted except Adorama.

- Anker Prime 100W first-row probe (BUILD_LOG 104): CDW and
  Newegg spec pages both fail — CDW lists variant A2688141
  with no UPC shown; Newegg shows MPN A2688 but no UPC and
  is an Anker Official Store marketplace listing. Model
  stays unranked; Best Buy / Adorama spec pages unprobed.

- Anker Prime 100W UPC flag closed (BUILD_LOG 103): catalog UPC
  194644040635 vindicated by a fourth source (Amazon AnkerDirect,
  ASIN B0CZ6LXL8R); B&H A2688J41-1 (UPC 194644289638) is a
  different SKU/packaging, so its $69.99 row was not added. No
  catalog change; the model stays unranked.

- Daily refresh 2026-11-09: full 200-model Meta Catalog sweep (3,963
  raw listings, 200/200 calls OK) + Shopify identified sweep (84
  offers, 73 models; Datavision Tab S10 FE+ 404 skipped, same as
  2026-11-07/08). Eighteen feed rows proven wrong on merchant pages
  and excluded via KNOWN_BAD (B&H Mac mini M6 $1,199 is the 24GB/512GB
  MHQM4LL/A and $1,699 the M6 Pro config, catalog pins MHQK4LL/A;
  Lenovo Legion Tab $899.99 — Lenovo's own page still shows $699.99;
  Target Pixel Buds Pro 2 $229.99 is Hazel, not Porcelain; Best Buy
  and Crutchfield Xtreme 4 $379.95 are Camouflage/Camo; Abt SoundLink
  Plus $269 — page still $179; Best Buy MX Master 4 $144.46 is the
  Black 910-007560 from marketplace seller IPC-STORE; T-Mobile Tab
  A11+ $339.99 is the 5G variant; NFM DualSense $79.99 is Chroma
  Pearl; Focus Camera QC Earbuds $179 is Rosewood Mauve; Target/NFM
  SoundLink Flex 2nd Gen are Sandstone/Rosewood Mauve; Best Buy
  Switch Lite $324.10 is the Pokémon edition; MelroseMac XDR $2,899
  sits on a merged standard/XDR page; Clemson Mac mini $799 is a
  campus-store education price; BrandsMart Flip 7 $149.95 is Squad;
  Bloomingdale's Tour Pro 3 $229.95 is a Live Beam 3 page; HP Cloud
  III Black-Red $69.99 points at the Black PDP). Builder hardened:
  nine color words (hazel, sandstone, rosewood, mauve, pearl, chroma,
  camo, camouflage, squad), a 5G-variant check, and host blocks for
  clemsontigertechshop.com (campus store) and mikesrenttoown.com
  (lease pricing). Confirmed moves: Bose SoundLink Plus @ Best Buy
  and Lenovo $179 -> $269, JBL Xtreme 4 @ JBL $309.95 -> $379.95,
  ASUS ROG Azoth 96 HE $359.99 -> $299.99, Pixel Buds Pro 2 @ Best
  Buy $169 -> $229, JBL Charge 6 @ JBL $149.95 -> $199.95, Dell
  S3225QS @ Best Buy $369.99 -> $329.99, HyperX Cloud III S @ HP
  $179.99 -> $139.99 (page shows $139.38), HyperX Cloud III @ HP
  $99.99 -> $69.99, JBL Flip 7 @ Sweetwater $129.95 -> $149.95,
  Sony LinkBuds Open @ Beach Camera $239.99 -> $228, HyperX
  QuadCast 2 S @ HyperX $159.99 -> $149.99. Snapshot 549 offers /
  162 models with quotes; site 651 offers, 98 matched, 86 verified
  rankings (unchanged). Tests 54 pass.
- Daily refresh 2026-11-08: full 200-model Meta Catalog sweep (3,966
  raw listings, 200/200 calls OK) + Shopify identified sweep (84
  offers, 73 models; Datavision Tab S10 FE+ 404 skipped, same as
  2026-11-07). Seven feed rows proven wrong on merchant pages and
  excluded via KNOWN_BAD (MelroseMac XDR $1,599 is the 2026 standard
  display, not the XDR tilt-height; Bose QC Earbuds $129 is a
  /p/service/ replacement page; B&H MX Keys S $223.98 and Ergo K860
  $245.98 are combo kits, not the standalone models; Dell Switch Pro
  Controller $59.99 is a Zen PRO third-party controller; Best Buy
  Switch OLED $411.38 is a marketplace seller's White model; CDW Tab
  A11+ $329.99 is the AT&T 5G variant, catalog pins Wi-Fi). Builder
  also gains "chocolate" as a color word (Melted/Cherry Chocolate
  rows no longer pass as Black). Confirmed moves: Corsair K65 Plus
  $129.99, HyperX Alloy Rise 75 $169.99, MX Vertical @ B&H $119.99,
  HyperX Cloud III S $139.99, LinkBuds Fit @ Bloomingdale's $228.00,
  HyperX QuadCast 2 S $159.99, Keychron K2 HE @ Byok $139.99 (sold
  out). Stale B&H MX Vertical hand row refreshed $74.99 -> $119.99.
  Snapshot 567 offers / 163 models with quotes; site 668 offers,
  96 matched, 86 verified rankings (unchanged). Tests 54 pass.
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
- Snapshot quotes go stale after 24 hours; the CLI flags them for
  re-check instead of presenting them as current prices.
