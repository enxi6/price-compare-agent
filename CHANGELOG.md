# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
While the major version is 0, the API and snapshot formats may change in minor
releases; breaking changes are called out in the release notes.

## [Unreleased]

### Added

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
