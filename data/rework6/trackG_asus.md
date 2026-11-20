# Track G — ASUS / ROG sweep (batch-6 rework)

- **Date:** 2026-11-20
- **Scope:** asus.com / rog.asus.com current mainstream lineup, only in categories the catalog already carries (monitors, keyboards, mice, headphones, routers, laptops). No mini PCs, motherboards, GPUs or other components.
- **Catalog state at sweep time:** 450 models in `price_agent/catalog.py`, 28 of them ASUS (see membership notes per model). Batch-6 draft (`data/candidates_batch6_500.md`) already carries 2 ASUS picks — ROG Falchion Ace HFX (entry 33) and ZenWiFi AXE7800 3-pack (entry 34) — not re-proposed here.
- **Method:** `browser.search` + `browser.open` (text fetch only), 2026-11-20. Identifier VERIFIED only when TWO independent qualifying sources agree on the code for the exact model/variant/config. Qualifying: B&H spec page, Abt spec page, Micro Center spec, Crutchfield, CDW spec page, Newegg spec page, Best Buy spec panel, brand official site/spec, authorized distributor spec (SHI, CompSource treated as distributor spec — see flags where this is the second source). NOT qualifying: Amazon, eBay, aggregators, price-tag photos, Q&A pages, search snippets alone. A single retailer spec page is NOT enough. No identifier was invented; every code below traces to a named page read in-session.
- **Result: 10 picks carried** (6 VERIFIED identifiers, 4 PENDING — see per-model verdicts), **13 queued in backlog**, **~42 checked and skipped** (details below). Total models checked: **65** (10 carried + 13 backlog + 27 already-in-catalog re-confirmed + 2 already-in-draft + 13 discontinued/OOS/no-row).
- **Prices are Black Friday-season snapshots (2026-11-20).** Best Buy Black Friday deals end Nov 28, 2026; B&H Holiday Savings prices move too. Re-verify every price/stock state at add time.

## PICKS (10) — proposed batch-6 replacements

### 1. ASUS ROG Swift OLED PG32UCDM 32" 4K 240Hz — Black
- **Key:** `asus-rog-swift-oled-pg32ucdm-black`
- **Category:** monitors
- **Variant pinned:** Black, original PG32UCDM (QD-OLED, 240Hz)
- **Membership:** NOT in catalog. Catalog has PG32UCWM (Tandem RGB OLED flagship, different model) and PG27UCDM (27-inch). No key/MPN/UPC collision.
- **Why it qualifies:** Flagship 32-inch 4K QD-OLED ROG monitor; two retailer-direct in-stock rows.
- **Identifiers — VERIFIED:** MPN `PG32UCDM`, UPC `197105413726`.
  - Source 1: B&H spec page — MFR # PG32UCDM, UPC 197105413726, $1,229.00 InStock.
  - Source 2: Micro Center spec — SKU 668913, Mfr Part# PG32UCDM, UPC 197105413726.
  - Both sources agree on MPN + UPC for the same model.
- **Price / stock:** B&H $1,229.00 InStock (retailer-direct row). Micro Center also lists it (price not captured in-session; B&H is the row).
- **Flag:** Do NOT mix with PG32UCDM3 Gen3 (UPC 199291274662, B&H $1,278.70) or PG32UCDMR (UPC 199291033863, B&H $899 Holiday / $1,299.99 list) — distinct variants with their own UPCs. Pin original PG32UCDM only.

### 2. ASUS RT-BE86U BE6800 Dual-Band Wi-Fi 7 Router — Black
- **Key:** `asus-rt-be86u-black`
- **Category:** routers
- **Variant pinned:** Black
- **Membership:** NOT in catalog. Catalog's only router is RT-BE58U (verified). No collision.
- **Why it qualifies:** Mainstream Wi-Fi 7 router (successor to RT-AX86U); Best Buy + B&H + Micro Center rows.
- **Identifiers — VERIFIED:** MPN `RT-BE86U`, UPC `197105581432`.
  - Source 1: B&H spec page — UPC 197105581432, $239.99 InStock.
  - Source 2: Micro Center spec — SKU 792663, Mfr Part# RT-BE86U, UPC 197105581432.
  - Best Buy model field also reads RT-BE86U (SKU 6594279, sold by Best Buy).
- **Price / stock:** B&H $239.99 InStock (row). Best Buy $255.99–$269.99, sold by Best Buy (price varies across crawls; one crawl showed $179.99 — likely open-box/clearance confusion, do not use). ASUS list $249.99 (ChannelOnline MSRP).
- **Flag:** Re-check Best Buy price at add time; use B&H $239.99 as the row unless Best Buy direct is lower and confirmed.

### 3. ASUS RT-BE92U BE9700 Tri-Band Wi-Fi 7 Router — Black
- **Key:** `asus-rt-be92u-black`
- **Category:** routers
- **Variant pinned:** Black
- **Membership:** NOT in catalog. Distinct from RT-BE86U (dual-band BE6800) and RT-BE58U (in catalog). No collision.
- **Why it qualifies:** Mainstream tri-band Wi-Fi 7 router with 10G port; Best Buy + B&H + ASUS rows.
- **Identifiers — VERIFIED:** MPN `RT-BE92U`, UPC `197105580633`.
  - Source 1: B&H spec page — UPC 197105580633, $285.99.
  - Source 2: Micro Center spec — SKU 800631, Mfr Part# RT-BE92U, UPC 197105580633.
  - Best Buy model field also reads RT-BE92U (SKU 6594276 / 11124612).
- **Price / stock:** Best Buy $265.51 InStock (1-day crawl; list $289.99) — retailer-direct row. B&H $285.99; ASUS US $289.99 InStock.
- **Flag:** Best Buy price is promo-sensitive ($265.51 vs $289.99 list across crawls) — re-verify at add time. Refurbished RT-BE92U-RB (SKU 12760801, $166.24) is a different listing — do not mix.

### 4. ASUS ZenWiFi BT8 BE14000 Tri-Band Wi-Fi 7 Mesh System (2-Pack) — White
- **Key:** `asus-zenwifi-bt8-2-pack-white`
- **Category:** routers
- **Variant pinned:** White, 2-pack `BT8(W-2-PK)`
- **Membership:** NOT in catalog. Batch-6 draft carries ZenWiFi AXE7800 3-pack (different product/generation). No collision.
- **Why it qualifies:** Current mainstream Wi-Fi 7 mesh; B&H + Micro Center + ASUS rows.
- **Identifiers — VERIFIED:** MPN `BT8(W-2-PK)`, UPC `197105532045`.
  - Source 1: B&H spec page — MFR # BT8(W-2-PK), UPC 197105532045, $449.99 InStock.
  - Source 2: Micro Center spec — SKU 800656, Mfr Part# BT8(W-2-PK), UPC 197105532045.
  - ASUS tech-spec page confirms model names BT8(W-1-PK) / BT8(W-2-PK) / BT8(W-3-PK).
- **Price / stock:** B&H $449.99 InStock, Holiday Savings $130 off (was $579.99) — retailer-direct row. Micro Center $599.99 InStoreOnly (not the row). ASUS 2-pack list $599.99.
- **Flag:** Promo price — Holiday Savings, re-verify at add time. 1-pack (UPC 197105531987, B&H $329.99, currently OutOfStock) and 3-pack (UPC 197105532090, B&H $699.99) are different pack sizes with different UPCs — pin 2-pack only. A Target refurbished 3-pack listing shows UPC 724129265927 — a refurb/Target-specific code, ignore; do not treat as a conflict.

### 5. ASUS ZenWiFi BT10 BE18000 Tri-Band Wi-Fi 7 Mesh System (2-Pack) — White
- **Key:** `asus-zenwifi-bt10-2-pack-white`
- **Category:** routers
- **Variant pinned:** White, 2-pack `BT10(W-2-PK)`
- **Membership:** NOT in catalog. Distinct from BT8 (BE14000 vs BE18000, 2.5G vs 10G ports). No collision.
- **Why it qualifies:** Premium current Wi-Fi 7 mesh; B&H + Best Buy rows.
- **Identifiers — VERIFIED (with a second-source caveat, see flag):** MPN `BT10(W-2-PK)`, UPC `197105429895`.
  - Source 1: B&H spec page — MFR # BT10(W-2-PK), UPC 197105429895, $629.99.
  - Source 2: CompSource distributor spec — Mfr Part # ZenWiFi BT10 2PK, UPC EAN CODE 197105429895.
  - Best Buy model field also reads BT10 (W-2-PK) (SKU 11870821).
- **Price / stock:** B&H $629.99 (row). Best Buy $760.69 (seller not confirmed in-session — do not use as the row without a fresh seller check).
- **Flag:** Second UPC source is CompSource (distributor listing), not a second big-retailer spec page — the weakest VERIFIED call in this sweep. At add time, confirm the UPC on the Best Buy spec panel for SKU 11870821; if it does not agree, downgrade to PENDING. Do NOT use the 3-pack: Best Buy 3-pack (SKU 6578611) is Clearance $849.99 and "no longer available in new condition" — clearance-only fails the rule. 1-pack (B&H UPC 197105429833, $346.00 InStock) is a different pack size — see backlog.

### 6. ASUS ROG Strix Scope II X Full-Size Wired Mechanical Gaming Keyboard — Black (NX Snow V2)
- **Key:** `asus-rog-strix-scope-ii-x-black`
- **Category:** keyboards
- **Variant pinned:** Black, ROG NX Snow V2 switches (`XA14 ROG STRIX SCOPE II X/NXSWV2/CA/PBT`)
- **Membership:** NOT in catalog. Catalog has Scope II 96 Wireless, Scope II 96 RX Wireless, Azoth, Azoth 96 HE, Azoth X, Falchion RX Low Profile, TUF K3 Gen II. Full-size wired Scope II X is distinct. No collision.
- **Why it qualifies:** Current mainstream full-size ROG keyboard; Best Buy sold-by-Best-Buy row + ASUS eShop in-stock row.
- **Identifiers — MPN VERIFIED, UPC PENDING:**
  - MPN `XA14 ROG STRIX SCOPE II X/NXSWV2/CA/PBT` VERIFIED: ASUS eShop USA product name + B&H MFR # agree exactly.
  - UPC lead `197105899483` PENDING (single qualifying source: SHI distributor spec for XA14 ROG STRIX SCOPE II X; Snapklik and camelcamelcamel agree but are not qualifying).
  - ASUS part number conflict — do NOT record a 90MP number: eShop shows 90MP03XF-BKAA22 in one crawl and 90MP03XF-BKAA20 in another for the same NXSWV2 variant. Pin the XA14 model name, not the 90MP code.
- **Price / stock:** Best Buy $129.99, sold by Best Buy (SKU 12726810; also SKU 6633432 seen; price varied $104.99–$129.99 across crawls). ASUS eShop $104.99 InStock (NXSWV2) / $129.99 (NXSMV2 Storm variant). B&H $117.50.
- **Flag:** Two switch variants exist — NX Snow V2 (NXSWV2, UPC 197105899483) vs NX Storm V2 (NXSMV2, UPC 197105899582, ASUS part 90MP03XG-BKAA22). Pin Snow V2 only. Best Buy's model field reads "XA14 ROG STRIX SCOPE II X/NXSW" (no V2 suffix) — confirm at add time that the Best Buy listing is the Snow V2 board, not the Storm.

### 7. ASUS ROG Strix Impact III Wireless Gaming Mouse — Black
- **Key:** `asus-rog-strix-impact-iii-wireless-black`
- **Category:** mice
- **Variant pinned:** Black, wireless (`P520 ROG STRIX IMPACT III WL`)
- **Membership:** NOT in catalog. Catalog has Gladius IV Ace, Harpe Mini Core, Harpe Ace Extreme, Harpe II Ace, Keris II Ace. No Impact III. No collision.
- **Why it qualifies:** Current mainstream lightweight ROG wireless mouse (57g, 36K DPI); Best Buy + ASUS eShop rows, both $53.99.
- **Identifiers — MPN VERIFIED, UPC PENDING:**
  - MPN `P520 ROG STRIX IMPACT III WL` VERIFIED: Best Buy model field "ROG STRIX IMPACT III P520" + ASUS eShop product name "P520 ROG STRIX IMPACT III" agree.
  - UPC lead `197105278134` PENDING (single qualifying source: CompSource distributor spec, Mfr Part # P520ROGSTRIXIMPACTIIIWL). Best Buy spec panel does not expose the UPC in text fetch ("See all specifications" is click-gated).
- **Price / stock:** Best Buy $53.99 (comp $69.99), Add to Cart, InStock — page read fresh 2026-11-20 (SKU 6606310). ASUS eShop $53.99 starting / $69.99 list.
- **Flag:** Best Buy's listing description text confusingly describes the WIRED Impact III (12,000 dpi, Paracord) while the title/model field is the wireless P520 — the model field governs; pin P520 wireless only. Wired Impact III (P518, UPC 195553810326) is a different model — do not mix. White wireless variant at Best Buy is sold by Beach Audio Inc (marketplace) — pin Black only.

### 8. ASUS TUF Gaming M4 Air Wired Gaming Mouse — Black
- **Key:** `asus-tuf-gaming-m4-air-black`
- **Category:** mice
- **Variant pinned:** Black (`P307 TUF GAMING M4 AIR`)
- **Membership:** NOT in catalog. No TUF mouse in the catalog. No collision.
- **Why it qualifies:** Mainstream ultralight TUF mouse (47g, 16,000 DPI); Best Buy + ASUS rows.
- **Identifiers — VERIFIED:** MPN `P307 TUF GAMING M4 AIR`, UPC `195553335454`.
  - Source 1: SHI distributor spec — Mfr Part # P307 TUF GAMING M4 AIR, UPC 195553335454, MSRP $49.99.
  - Source 2: Zoro spec — MFR # P307 TUF GAMING M4 AIR, UPC # 195553335454.
  - CompSource and OfficeCrave print the same UPC; Best Buy model field reads P307-TUF-GAMING-M4-AIR (SKU 11145905).
- **Price / stock:** Best Buy $57.99 (8-day crawl, Add to cart) — retailer-direct row; older crawls $44.99. ASUS US $49.99.
- **Flag:** Price moves ($44.99–$57.99) — re-verify at add time. UPC conflict noted and set aside: a Target marketplace listing (sold by Ideal sales, not qualifying) shows UPC 196384006247 for the same model name — marketplace-sourced, do not treat as a competing verified code.

### 9. ASUS ROG Harpe Ace Aim Lab Edition Wireless Gaming Mouse — Black
- **Key:** `asus-rog-harpe-ace-aim-lab-black`
- **Category:** mice
- **Variant pinned:** Black (`P713 ROG HARPE ACE AIM LAB EDITION/BLK`)
- **Membership:** NOT in catalog. Catalog has Harpe Mini Core, Harpe Ace Extreme, Harpe II Ace — the original Harpe Ace Aim Lab Edition is distinct. No collision.
- **Why it qualifies:** Mainstream ROG esports mouse; Best Buy Black Friday row, sold by Best Buy, InStock.
- **Identifiers — PENDING:**
  - UPC lead `195553936392` PENDING (single qualifying source: Best Buy spec panel, model ROGHARPEACEAIMB, SKU 6537579; ipcstore/Snapklik/camelcamelcamel agree but are not qualifying).
  - MPN PENDING: ASUS eShop product name is P713 ROG HARPE ACE AIM LAB EDITION; ASUS part number 90MP02W0-BMAA00 appears only on ipcstore (not qualifying). Best Buy's model code ROGHARPEACEAIMB is a different code system — do not record either as verified.
- **Price / stock:** Best Buy $69.99 Black Friday Deal (comp $99.99), Add to Cart, Sold by Best Buy, InStock — page read fresh 2026-11-20. ASUS eShop $69.99 starting / $149.99 list.
- **Flag:** B&H lists this mouse as No Longer Available / Discontinued ($149.99) — aging model, but the Best Buy direct row is live and in stock. White variant: Best Buy model P713 ROG HARPE ACE/WHT, SKU 6595752, $79.99 sold by Best Buy, UPC 197105136533 (also single-source) — same model, different color; Black is the pinned variant.

### 10. ASUS TUF Gaming A16 (FA608PP) 16" Gaming Laptop — Jaegar Gray (Ryzen 9 8940HX, RTX 5070, 16GB, 512GB)
- **Key:** `asus-tuf-gaming-a16-fa608pp-rtx-5070-jaegar-gray`
- **Category:** laptops
- **Variant pinned:** Jaegar Gray, Best Buy config `FA608PP-TF/A16_97` (Ryzen 9 8940HX, RTX 5070, 16GB, 512GB)
- **Membership:** NOT in catalog. No ASUS laptop in the catalog. No collision.
- **Why it qualifies:** Mainstream current TUF gaming laptop; Best Buy Black Friday row, Add to cart.
- **Identifiers — PENDING:**
  - MPN `FA608PP-TF/A16_97` PENDING (single source: Best Buy model field). No UPC lead found for this exact Best Buy config (laptop UPCs are config-specific; B&H carries a different A16 config, FA608WV-DB94, discontinued; Abt carries FA608UMI-NB73, RTX 5060, $1,799.99 — different config).
- **Price / stock:** Best Buy $1,549.99 Black Friday Deal (comp $2,224.99), Add to cart (2-day crawl). Other crawls show the same $1,549.99.
- **Flag:** Laptop config soup — FA608PP covers many regional/config variants (e.g. FA608PP-TU094W UK, FA608PP-RV019). Pin ONLY the Best Buy config FA608PP-TF/A16_97. Identifier pending; do not rank until a UPC lead is found on a retailer/manufacturer spec page for this exact config. The batch already carries 5 laptops; this is the single ASUS laptop pick — if a slot must be cut, cut this one first (see backlog for the G16 alternative).

## QUEUED ASUS BACKLOG (13) — verified or well-evidenced, not carried (cap / weaker than picks)

1. **ASUS ROG Strix G16 G614PR (RTX 5070 Ti, Ryzen 9 8940HX, 16GB, 1TB) — Eclipse Gray.** Best Buy model G614PR-G16.R95070TI, $1,749.99 Black Friday (comp $2,299.99), sold by Best Buy. Strongest backlog item. Not carried: no UPC lead found (B&H does not carry the 2025 G614PR config); Best Buy price volatile ($1,749.99–$2,209.99 across crawls). Key would be `asus-rog-strix-g16-g614pr-rtx-5070-ti-eclipse-gray`.
2. **ASUS ROG Strix XG27UCG 27" 4K 160Hz Dual-Mode — Black.** MPN XG27UCG VERIFIED (Micro Center product name + CompSource Mfr Part # agree); UPC 197105564633 PENDING (single qualifying source: CompSource; Adorama also prints it but Adorama is not on the qualifying list). Micro Center $349.96 InStoreOnly; Adorama $469.99. Not carried: in-store-only row is weak and the Gen2 (XG27UCGR) supersedes it at $399.99. Key would be `asus-rog-strix-xg27ucg-black`.
3. **ASUS ROG Strix XG27UCSR (XG27UCS Gen2) 27" 4K 160Hz Dual-Mode — Black.** ROG US $399.00 InStock; Best Buy model XG27UCSR SKU 12697071 (price unclear — $510.70 comp value in crawls, reviews cite $320–$400; Newegg $480.86). Not carried: UPC CONFLICTED — PB Tech (NZ, not qualifying) says 199291242951, Lakeshore IT says 199291242913; no qualifying source prints a UPC. Key would be `asus-rog-strix-xg27ucsr-black`.
4. **ASUS ROG Strix XG27UCG Gen2 (XG27UCGR) 27" 4K 162Hz Dual-Mode — Black.** Micro Center $399.99; ROG US $399. Current model. Not carried: no UPC lead found in-session; Gen2 family is confusing (XG27UCG vs XG27UCGR vs XG27UCSR) and the sweep already carries two monitors. Key would be `asus-rog-strix-xg27ucg-gen2-black`.
5. **ASUS ROG Delta II Wireless — White (A701 ROG DELTA II/WHT).** Best Buy SKU 6637821, $180.99 (comp $229.99). White variant of in-catalog Black Delta II (90YH03W0-BHAA03). Not carried: same-model color variant, UPC not captured. Key would be `asus-rog-delta-ii-white`.
6. **ASUS ROG Keris II Ace — White (P714 ROG KERIS II WL/WHT).** Best Buy SKU 10732514, $182.43–$219.99 InStock. White variant of in-catalog Black Keris II Ace. Not carried: same-model color variant, UPC not captured. Key would be `asus-rog-keris-ii-ace-white`.
7. **ASUS ROG Strix Scope II 96 Wireless — White (SCOPE II 96/WHT/NXSW/PBT).** Best Buy SKU 6595753, $109.99 Black Friday, sold by Best Buy. White variant of in-catalog Black Scope II 96 Wireless. Not carried: same-model color variant. Key would be `asus-rog-strix-scope-ii-96-wireless-white`.
8. **ASUS ZenWiFi BT8 (3-Pack) — White.** B&H UPC 197105532090, $699.99 Holiday Savings (was $849.99). Same model family as carried 2-pack. Not carried: pack-size sibling of a carried pick. Key would be `asus-zenwifi-bt8-3-pack-white`.
9. **ASUS ZenWiFi BT10 (1-Pack) — White.** B&H UPC 197105429833, $346.00 InStock. Sibling of carried 2-pack. Not carried: pack-size sibling. Key would be `asus-zenwifi-bt10-1-pack-white`.
10. **ASUS TUF Gaming VG27AQ1A 27" QHD 170Hz — Black.** ASUS US $229.00 InStock. Not carried: brand-direct-only (no Best Buy/B&H retailer-direct row found; Best Buy carries only the different VG27UQ1A 4K model via marketplace sellers). Flagged pending per the brand-direct-only rule (at most 1–2 such entries; the carried picks all have retailer rows). Key would be `asus-tuf-gaming-vg27aq1a-black`.
11. **ASUS TUF Gaming VG279QM5F 27" FHD 260Hz Series 5 — Black.** ASUS US $199.00 InStock (successor to the VG279QM). Not carried: ASUS-direct only, no retailer row or identifier lead found in-session. Key would be `asus-tuf-gaming-vg279qm5f-black`.
12. **ASUS TUF Gaming M3 Gen II Mouse — Black.** B&H MFR # 90MP0320-BMAA00. Not carried: conflicting stock signals — B&H showed $24.99 InStock in a 98-day-old crawl but Discontinued in a 27-day-old crawl; Adorama $29.99. No UPC lead. Key would be `asus-tuf-gaming-m3-gen-ii-black`.
13. **ASUS Vivobook S 14 Q423SA (Snapdragon) — Best Buy $650 Black Friday.** Not carried: laptop config soup (S5406SA/S5406MA/M5406WA/Q423SA all different configs), no identifier lead, and the sweep already carries one laptop. Re-check with a pinned config + UPC lead before any future carry.

## Checked and skipped

**Already in the 450-model catalog (re-confirmed, do not re-add):**
- ROG Swift OLED PG27UCDM, PG32UCWM, PG27AQDPR; ProArt PA279CRV, PA32UCDM; ROG Strix OLED XG27ACDMS; TUF VG27AQ3A; ZenScreen MB16ACV (monitors)
- ROG Delta II Black, ROG Delta USB-C, ROG Pelta (headsets); ROG Cetra Open Wireless, ROG Cetra SpeedNova (earbuds)
- ROG Azoth, ROG Azoth 96 HE, ROG Azoth X, ROG Strix Scope II 96 Wireless Black, ROG Strix Scope II 96 RX Wireless, ROG Falchion RX Low Profile, TUF K3 Gen II (keyboards)
- ROG Gladius IV Ace, ROG Harpe Mini Core, ROG Harpe Ace Extreme, ROG Harpe II Ace, ROG Keris II Ace Black (mice)
- RT-BE58U (routers); ROG Xbox Ally X (handheld-consoles)

**Already in the batch-6 draft (do not re-propose):**
- ROG Falchion Ace HFX (draft entry 33); ZenWiFi AXE7800 3-pack White (draft entry 34).

**Discontinued / out of stock / no clean retailer-direct row:**
- ROG Swift OLED PG27AQDM — 2023 model; Adorama Discontinued; no clean Best Buy/B&H new row; UPC leads conflict (two codes on aggregator pages, neither qualifying).
- ROG Strix XG27UCS — ROG US $399 OutOfStock; Best Buy new listing is the Gen2 XG27UCSR; only refurbished XG27UCS at Best Buy ($356.24).
- TUF Gaming VG27AQML1A — re-checked per brief: ASUS US $369 OutOfStock still; Adorama Discontinued. Drop again (same as earlier batches).
- TUF Gaming VG279QM — ASUS US $249 OutOfStock; 2020 model superseded by VG279QM5A / VG279QM5F; Best Buy listing seller unclear.
- TUF Gaming K5 — 2018 Mech-Brane keyboard; discontinued (QuietPC, PC Case Gear).
- TUF Gaming H3 — Newegg listings are marketplace sellers only (roboshine, Yongrui); 2020-era model.
- TUF Gaming H1 Wireless — Newegg only, seller unclear; aging model.
- ROG Keris II Origin (P722) — Best Buy Black "no longer available in new condition"; White marketplace-only (IPC-STORE). KJP Edition (P727) is Clearance $152.99 at Best Buy — clearance fails the rule.
- ASUS ROG Strix XG27ACS — already dropped in batch 6 (ASUS OOS); no new evidence.
- Vivobook S 14 S5406SA — config soup; Staples $899.99 deal expired (June 2025); Macy's OutOfStock.
- Zenbook 14 UX3405CA-U7512 — Best Buy new $649.99 was a Dec 2025 deal; now open-box only ($517+). UX3405MA-PH77 $1,299.99 stock unclear.
- ROG Strix G16 G615JPR (i9-14900HX, RTX 5070, 32GB) — Best Buy "Sold Out" at $2,134.99.
- TUF Gaming A16 FA608UP (Ryzen AI 9 270, RTX 5070, 32GB) — Best Buy Clearance $1,619.99, Sold Out.

## Notes for the add-time session
- Re-verify all 10 pick prices/stock (Black Friday / Holiday Savings pricing ends Nov 28, 2026 at Best Buy; B&H Holiday Savings also time-limited).
- Weakest VERIFIED call: ZenWiFi BT10 2-pack UPC (second source CompSource distributor spec) — confirm on the Best Buy spec panel (SKU 11870821) or downgrade to PENDING.
- Scope II X: confirm the Best Buy listing is the NX Snow V2 board (not Storm) and resolve the 90MP03XF-BKAA20 vs -BKAA22 conflict before recording any 90MP number; the UPC lead 197105899483 still needs a second qualifying source.
- Impact III Wireless: UPC lead 197105278134 still needs a second qualifying source (Best Buy spec panel is click-gated in text fetch; check live at add time).
- Harpe Ace Aim Lab Black: UPC lead 195553936392 still needs a second qualifying source.
- TUF A16: no UPC lead — do not rank until one is found for the exact config FA608PP-TF/A16_97.
- Category naming: used `routers` for all four networking picks to match the catalog (RT-BE58U is `routers`); the batch-6 draft used `networking` for its ZenWiFi entry — reconcile at add time.
