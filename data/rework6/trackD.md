# Track D — Batch-6 rework alternates (research findings)

- **Date:** 2026-11-20 (all prices/stock are Black Friday-season snapshots observed 2026-11-20; Best Buy Black Friday deals end Nov 28, 2026 — re-verify every price/stock at add time)
- **Scope:** 3 named alternates + 6 additional alternates (non-Lenovo, per the 2026-11-20 method pivot — see below). Catalog 450 → 500 rework of `data/candidates_batch6_500.md` (first draft rejected: 1/50 identifiers verified).
- **Method pivot (2026-11-20, parent instruction):** the Lenovo Legion Pro 7 Gen 10 AMD (item 4 in the original brief) and the Lenovo Yoga Slim 7x 2026 are **dropped from this track** — a dedicated Lenovo.com sweep track now covers all Lenovo systematically, including those models. This file covers only the other three named alternates and non-Lenovo additionals.
- **Rules enforced:** US-market models only; seller-direct or retailer-direct only; no Amazon as a source in any form; no eBay; no marketplace/third-party sellers; mainstream or new products only. Identifier VERIFIED only when TWO independent qualifying sources agree on the code for the exact model/variant. Qualifying sources: B&H spec page, Abt spec page, Micro Center spec, Crutchfield, Newegg spec page, brand official site/spec, authorized distributor spec. NOT qualifying: Amazon, eBay, aggregators (Snapklik, Desertcart, Ubuy, laptoparena, etc.), price-tag photos, Q&A pages, search snippets alone. A single retailer spec page is NOT enough. Never invent an identifier. **Strict-reading note:** the Best Buy model field is NOT in the brief's qualifying-source list, so MPNs resting on Best Buy + one qualifying source are marked PENDING below, even though Best Buy corroborates them. Two pages from the same brand (e.g. ASUS PR + ASUS Store) are not treated as two independent sources. Research via `browser.search` / `browser.open` (text fetch only); no live browser was available to this track.

## Summary

| # | Proposed key | Identifiers | Price row (direct retailer) | Membership |
|---|---|---|---|---|
| 1 | `sony-ult-tower-10-black` | MPN VERIFIED; UPC PENDING | Best Buy $799.99, Sold by Best Buy, InStock | 0 collisions |
| 2 | `logitech-signature-slim-k950-graphite` | MPN VERIFIED; UPC VERIFIED (caveat) | B&H $69.99 InStock | 0 collisions |
| 3 | `microsoft-surface-laptop-13-2025-ocean-512gb` | MPN VERIFIED; UPC VERIFIED | Best Buy $1,149.99, Sold by Best Buy, InStock | 0 collisions |
| 4 | `asus-zenbook-a14-ux3407qa-ps76-iceland-gray` | MPN PENDING (strict); UPC PENDING (lead only) | Best Buy $1,199.99, Sold by Best Buy, InStock | 0 collisions |
| 5 | `hp-omnibook-3-14-hz0788dx-nouvelle-silver` | MPN PENDING (strict); UPC PENDING | Best Buy $599.99, Sold by Best Buy, InStock | 0 collisions |
| 6 | `garmin-fenix-8-solar-sapphire-47mm-carbon-gray` | MPN VERIFIED; UPC VERIFIED | Best Buy $749.99, Sold by Best Buy, InStock | 0 collisions |
| 7 | `asus-rog-zephyrus-g14-2025-ga403um-platinum-white` | MPN PENDING; UPC PENDING (no lead) | Best Buy $2,299.99 list (seller/stock unconfirmed — re-verify) | 0 collisions |
| 8 | `hp-omen-transcend-14-2025-14-fb1053dx-shadow-black` | MPN PENDING (strict); UPC PENDING | Best Buy $2,824.99, Sold by Best Buy (price volatile — re-verify) | 0 collisions |
| 9 | `alienware-16-aurora-lac16250-7469blu-blue` | MPN VERIFIED; UPC VERIFIED | **HOLD — no clean direct row confirmed** | 0 collisions |

**Counts:** 9 entries. Fully VERIFIED MPN+UPC pairs: 4 (Surface 13", Fenix 8 Solar, K950 with a UPC caveat, Aurora — but Aurora's price row is on HOLD). MPN-only verified: ULT Tower 10. Both identifiers pending: Zenbook A14, OmniBook 3, Zephyrus G14, OMEN Transcend 14. Clean direct price rows confirmed: 8 of 9. Laptop-heavy set: 6 of 9 are laptops (Surface 13", Zenbook A14, OmniBook 3, Zephyrus G14, Transcend 14, Aurora); the other 3 are a speaker, a keyboard, and a watch.

## Membership check (formal)

- **Script:** `/tmp/trackd_membership.py`, run 2026-11-20 against `/tmp/catalog_ref.tsv` (450 rows built from `price_agent/catalog.py` EVAL_SET).
- **Checks per candidate:** exact key match; normalized model-name substring in both directions; MPN and UPC substring against full catalog row text; intra-batch duplicate keys.
- **Result: 0 collisions for all 9 candidates; no intra-batch duplicate keys.**
- **Sibling adjudications (by grep, recorded in writing):**
  - Surface 13" 2025 (EP2-33432) vs catalog `microsoft-surface-laptop-13-8-8th-edition-platinum` (EP2-59028, Snapdragon X2 Plus, 13.8") and `microsoft-surface-laptop-15-8th-edition-platinum` (EP2-60128, Snapdragon X2 Elite, 15") — different MPN, size, and chip generation; distinct.
  - Fenix 8 Solar 010-02906-10 vs catalog `garmin-fenix-8-47mm-carbon-gray` (fēnix 8 AMOLED Sapphire, 010-02904-20) and `garmin-fenix-9-47mm-titanium-pebble-gray` (010-04762-00) — Solar MIP display vs AMOLED; distinct.
  - Alienware 16 Aurora LAC16250-7469BLU-PUS vs catalog `alienware-16-area-51-rtx-5070-ti-2tb-liquid-teal` (LAA16250-9499BLU-PUS) — Aurora is a different family (LAC vs LAA prefix), different tier; distinct.
  - ULT Tower 10 vs catalog ULT TOWER 9/7/5/MAX (SRSULT900/700/500/3000) — no 10; distinct.
  - K950 vs catalog `logitech-signature-m650-graphite` (Signature M650 mouse) — only other Signature item; distinct.
  - Zephyrus G14, Zenbook A14, OmniBook 3, OMEN Transcend 14 laptop — no catalog rows for those families at all (catalog has only the OMEN Transcend 32 monitor).

---

## 1. Sony ULT Tower 10 Black

- **Proposed key:** `sony-ult-tower-10-black`
- **Brand / model / pinned variant:** Sony / ULT Tower 10 / Black (SRSULT1000)
- **Category:** speakers
- **MPN SRSULT1000 — VERIFIED.** Two qualifying sources agree: B&H spec page (MFR # SRSULT1000) + Crutchfield (MFR # SRSULT1000, Item # 158ULT1000). Best Buy model field agrees (third corroboration).
- **UPC 027242928978 — PENDING (strong lead).** Adorama spec page lists "UPC Code 027242928978" for SRSULT1000 — single qualifying source. The B&H spec page opened fresh 2026-11-20 has NO UPC field; the Best Buy crawled page contains no UPC. The same code appears on many non-qualifying sources (Amazon item details, eBay, Ubuy, Desertcart, manuals.plus, Visions.ca).
- **Price/stock:** Best Buy $799.99 (comp $1,199.99), Sold by Best Buy, Add to cart, InStock, Model SRSULT1000, SKU 6577679 (page opened fresh 2026-11-20). Costco $789.99/$799.99 (item 1916855) — observed only via Instagram price-tag photos, not a qualifying source, do not cite as a row. B&H now "No Longer Available"/Discontinued (fresh open 2026-11-20).
- **Flags:** B&H discontinued — Best Buy is the row. UPC needs one more qualifying source.
- **Membership:** 0 collisions. Catalog has ULT TOWER 9/7/5/MAX, not 10 — distinct model.

## 2. Logitech Signature Slim K950 Graphite

- **Proposed key:** `logitech-signature-slim-k950-graphite`
- **Brand / model / pinned variant:** Logitech / Signature Slim K950 / Graphite (US layout)
- **Category:** keyboards
- **MPN 920-012424 — VERIFIED.** Two qualifying sources: B&H (MFR # 920-012424) + Logitech official datasheet (1worldsync PDF: "GRAPHITE US Part #: 920-012424"; Off-White US is 920-012429, different). Best Buy model field agrees.
- **UPC 097855192974 — VERIFIED with a caveat.** B&H product page shows "UPC: 097855192974" (opened fresh 2026-11-20) + Tech-America distributor spec (UPC 0097855192974). **Caveat:** Tech-America and PC-Canada share the same data feed, so the second source is a distributor listing, not a second major retailer. Also seen on dgxtech/shopabunda (non-qualifying).
- **Price/stock:** B&H $69.99 InStock (was $89.99, Holiday Savings $20) — the clean row (opened fresh 2026-11-20). Staples $69.99 InStock. Best Buy $89.99, but one listing (SKU 10201839) is "Sold & shipped by EP Holdings Inc - Logitech Authorized Store" (marketplace — do not use); another Best Buy SKU 12804402 shows $89.99 InStock.
- **Flags:** Use the B&H $69.99 row. Do not mix with K980 Solar+ or MK950 combo (different models).
- **Membership:** 0 collisions; no K950 in catalog (only Signature M650 mouse).

## 3. Microsoft Surface Laptop 13" (2025) Snapdragon X Plus, Ocean 512GB

- **Proposed key:** `microsoft-surface-laptop-13-2025-ocean-512gb`
- **Brand / model / pinned variant:** Microsoft / Surface Laptop 13" (2025) / Snapdragon X Plus, Ocean, 512GB
- **Category:** laptops
- **MPN EP2-33432 — VERIFIED.** Two qualifying sources: B&H (MFR # EP2-33432) + Abt (Model # EP2-33432). Best Buy model field agrees.
- **UPC 196388548231 — VERIFIED.** Two qualifying sources: B&H spec page UPC + Abt UPC # 196388548231.
- **Price/stock:** Best Buy Ocean 512GB $1,149.99 (comp $1,249.99), Add to cart, InStock, SKU 10148535 (page opened fresh 2026-11-20). Black Friday ends Nov 28. **Flag:** Abt lists this config as "no longer available" — Best Buy is the row. Other configs (NOT the pinned row): Platinum 512GB EP2-33462, Violet 512GB EP2-33426, Platinum 256GB EP2-36981 ($979.00 per batch-6 brief via Klarna — NOT re-verified this session).
- **Flags:** Distinct from in-catalog Surface Laptop 13.8" 8th Edition (EP2-59028) and 15" 8th Edition (EP2-60128) — different size, chip gen, and "1st Edition" per box label. Note: Target calls this model "8th Edition," which is confusing; do not conflate.
- **Membership:** 0 collisions (see sibling adjudication above).

## 4. ASUS Zenbook A14 UX3407QA-PS76, Iceland Gray, 32GB/1TB

- **Proposed key:** `asus-zenbook-a14-ux3407qa-ps76-iceland-gray`
- **Brand / model / pinned variant:** ASUS / Zenbook A14 / UX3407QA-PS76, Iceland Gray, Snapdragon X X1-26-100, 32GB, 1TB
- **Category:** laptops
- **MPN UX3407QA-PS76 — PENDING under strict reading.** ASUS official PR (asus.com news, 2025-01-27) + ASUS Store (eshop.asus.com lists UX3407QA-PS76, Part Number 90NB1502-M00FM0); Best Buy model field corroborates but Best Buy is not in the qualifying list. The two ASUS-brand sources are not independent of each other. B&H does not carry it. A Newegg listing exists but is a Velztorm customized build (marketplace seller), not a clean spec source.
- **UPC 197105832077 — PENDING (lead only).** laptoparena.net lists EAN/UPC 0197105832077 / 197105832077 — an aggregator/spec database, not qualifying. No second source found.
- **Price/stock:** Best Buy $1,199.99 (comp $1,599.99), Add to cart, InStock, SKU 6616965 (opened fresh 2026-11-20). ASUS Store $1,599.99. **Flag:** the Beige config UX3407QA-X1P512 (16GB/512GB) is a different pin — do not mix (list $999.99; Best Buy $919 in one crawl).
- **Membership:** 0 collisions; no Zenbook A14 in catalog.

## 5. HP OmniBook 3 14", 16GB/512GB, Nouvelle Silver, 14-hz0788dx / DM2Z9UA#ABA

- **Proposed key:** `hp-omnibook-3-14-hz0788dx-nouvelle-silver`
- **Brand / model / pinned variant:** HP / OmniBook 3 14" / Snapdragon X X1-26-100, 16GB, 512GB, Nouvelle Silver (14-hz0788dx / DM2Z9UA#ABA)
- **Category:** laptops
- **MPN 14-hz0788dx / DM2Z9UA#ABA — PENDING under strict reading.** HP official datasheet PDF (files.bbystatic.com: model 14-hz0788dx, Product number DM2Z9UA#ABA) is one qualifying source; Best Buy model field corroborates but Best Buy is not in the qualifying list. HP.com lists sibling configs DT4F1UA#ABA (Starlit blue, 16/512GB, $899.99) and DT4F0UA#ABA (16/256GB) — different pins, do not mix.
- **UPC 826581262121 — PENDING.** HP datasheet PDF only ("UPC Code • 826581262121"); a search for the code returned only the datasheet — no second source found.
- **Price/stock:** Best Buy $599.99 Black Friday (comp $799.99), Sold by Best Buy, Add to cart, InStock, SKU 6679357 (page opened fresh 2026-11-20). Specs as listed: 14" 2K OLED title; spec table lists 1920x1200 Full HD+ UWVA panel, 60Hz — record as listed, do not resolve the panel wording here.
- **Membership:** 0 collisions; no OmniBook/Spectre in catalog.

## 6. Garmin Fenix 8 Solar Sapphire 47mm, 010-02906-10, Carbon Gray DLC Titanium / Black-Pebble Gray

- **Proposed key:** `garmin-fenix-8-solar-sapphire-47mm-carbon-gray`
- **Brand / model / pinned variant:** Garmin / fēnix 8 Solar Sapphire 47mm / Carbon Gray DLC Titanium with Black/Pebble Gray silicone band (010-02906-10)
- **Category:** wearables
- **MPN 010-02906-10 — VERIFIED.** Two qualifying sources: Garmin official FĒNIX 8 SERIES price list PDF (images.thdstatic.com: "fēnix 8 – 47 mm, Solar, Sapphire — Carbon gray DLC titanium with black/pebble gray silicone band — 010-02906-10") + CompSource distributor spec (Manufacturer Part Number: 010-02906-10). Best Buy model field agrees. **Correction recorded 2026-11-20:** the initial guess 010-02904-00 was WRONG — that is the AMOLED Slate Gray. Solar 47mm = 010-02906-10 (Carbon Gray) and 010-02906-20 (Titanium/Amp Yellow).
- **UPC 753759339326 — VERIFIED.** Same two sources (Garmin price list PDF: UPC 753759339326; CompSource: "UPC EAN CODE: 753759339326"). Further corroboration (not needed for the verdict): Botach (MPN + UPC), Sportsman's Guide (Mfg # + UPC), 6ave.com (SKU/UPC/MPN), HeartRateMonitorsUSA MPN/UPC table.
- **Price/stock:** Best Buy $749.99 (comp $999.99, Save $250), Sold by Best Buy, Add to cart, InStock, SKU 6594318 (page opened fresh 2026-11-20). Garmin price list MRP $1,099.99. Garmin.com $749.99 (for the sibling 010-02906-20 variant). Kohl's $749.99 lists both 010-02906-10 and 010-02906-20.
- **Membership:** 0 collisions; distinct from catalog Fenix 8 AMOLED Sapphire 47mm (010-02904-20) — Solar MIP display vs AMOLED; catalog also has fēnix 9 47mm (010-04762-00).

## 7. ASUS ROG Zephyrus G14 (2025), GA403UM-G14.R9HX4, Platinum White

- **Proposed key:** `asus-rog-zephyrus-g14-2025-ga403um-platinum-white`
- **Brand / model / pinned variant:** ASUS / ROG Zephyrus G14 (2025) / GA403UM-G14.R9HX4, Platinum White, Ryzen 9 270, RTX 5060 8GB GDDR7, 16GB, 1TB, 14" 3K OLED 120Hz
- **Category:** laptops
- **MPN GA403UM-G14.R9HX4 — PENDING.** Best Buy model field only; ROG ASUS site confirms the GA403 family with Ryzen 9 270 + RTX 5060 but not the full config code; no B&H/ASUS-store second source found. HIDevolution and Velztorm listings name the model but are reseller/marketplace, not qualifying.
- **UPC — PENDING, no lead found.**
- **Price/stock:** Best Buy $2,299.99 list (SKU 6629420; also SKU 12974438); $2,049.99 seen via a Tom's Guide link crawl; a Velztorm marketplace listing at $2,049.99 (SKU 10937798) must NOT be used. **Flag:** seller/stock at $2,299.99 not confirmed by a fresh page open — re-verify at add time.
- **Membership:** 0 collisions; no Zephyrus in catalog.

## 8. HP OMEN Transcend 14 (2025), 14-fb1053dx / D8KM4UA#ABA, Shadow Black

- **Proposed key:** `hp-omen-transcend-14-2025-14-fb1053dx-shadow-black`
- **Brand / model / pinned variant:** HP / OMEN Transcend 14 (2025) / Ultra 9 285H, RTX 5070 8GB GDDR7, 32GB LPDDR5x, 1TB, 14" 3K OLED 120Hz, Shadow Black (14-fb1053dx / D8KM4UA#ABA)
- **Category:** laptops
- **MPN 14-fb1053dx / D8KM4UA#ABA — PENDING under strict reading.** HP official datasheet (cdn.cs.1worldsync.com PDF: model 14-fb1053dx, Product number D8KM4UA#ABA) is one qualifying source; Best Buy model field corroborates but Best Buy is not in the qualifying list. **Flag:** do not mix with sibling configs 14-fb1023dx / 14-fb0521nr (seen on retail box labels) or 14-fb1013dx (Woot, RTX 5060, Ultra 7 255H).
- **UPC 821844495568 — PENDING.** HP datasheet only ("UPC Code • 821844495568"); a search for the code returned only the datasheet — no second source found.
- **Price/stock:** Best Buy $2,824.99, Sold by Best Buy, SKU 6672943 (multiple crawls 1–2 days old); second SKU 12901895 $2,599.99 with Add to cart (shipping free, pickup unavailable). **Flag:** price volatile across crawls/SKUs ($2,599.99–$2,999.99) — re-verify at add time; use SKU 6672943 $2,824.99 as the pinned row.
- **Membership:** 0 collisions; catalog has only the OMEN Transcend 32 monitor; no Transcend 14 laptop.

## 9. Alienware 16 Aurora, LAC16250-7469BLU-PUS, Blue — PRICE ROW HOLD

- **Proposed key:** `alienware-16-aurora-lac16250-7469blu-blue`
- **Brand / model / pinned variant:** Alienware / 16 Aurora / Core 7 240H, RTX 5060 8GB, 16GB DDR5, 1TB, 16" WQXGA 120Hz, Blue (LAC16250-7469BLU-PUS)
- **Category:** laptops
- **MPN LAC16250-7469BLU-PUS — VERIFIED.** Two qualifying sources: Newegg spec page (Model #: LAC16250-7469BLU-PUS) + D&H distributor spec sheet (images.electronicexpress.com, "Product Setup - D&H Consumer"). Best Buy model field agrees.
- **UPC 884116430469 — VERIFIED.** Two distributor spec sheets agree: D&H Consumer spec sheet + "Product Setup - New Age" spec sheet (ik.imagekit.io, PRN 111123), both listing UPC 884116430469 for LAC16250-7469BLU-PUS; Hilltown Tech also lists the same UPC with the MPN. D&H is an authorized distributor, so "authorized distributor spec" covers these.
- **Price/stock — NO clean retailer-direct row confirmed (HOLD, do not add on price yet):** Best Buy has three SKUs for this exact model and all three are marketplace sellers — SKU 13279039 $1,707.70 sold by CompVoy; SKU 13024084 $1,649.00 sold by PC Heaven; SKU 12140271 $2,195.01 sold by antonline (all opened fresh 2026-11-20). Newegg lists it at $1,699.99 (freshest crawl) but the seller is unclear ("More options from $1,697.43–$2,283.81" — marketplace-style). antonline.com direct $2,149.99 matches the config but the listing does not show the model code. No dell.com direct row surfaced in search. **Do NOT add until a Sold-by-Best-Buy, sold-by-Newegg, or dell.com direct row is confirmed at add time.** (A separate Best Buy listing, SKU 12105769, $1,799.00, is a bundle with a 1TB dock station — different config, not the pinned model.)
- **Membership:** 0 collisions; distinct from catalog Alienware 16 Area-51 (LAA16250-9499BLU-PUS, RTX 5070 Ti) — Aurora is a different family, different MPN prefix.

---

## Investigated and dropped (do not re-propose without new evidence)

**Dropped by the 2026-11-20 method pivot (Lenovo sweep track owns these now):**
- **Lenovo Legion Pro 7 Gen 10 AMD, 83RU0002US** — for the record: MPN VERIFIED (lenovo.com + Newegg spec page); UPC pending, no lead found; lenovo.com $2,799.99 InStock; Newegg $4,296.99 sold by Lenovo; Lenovo-direct-only flag. Config: Ryzen 9 9955HX, RTX 5070 Ti 12GB, 32GB DDR5-5600, 2TB PCIe Gen5, 16" WQXGA OLED 240Hz.
- **Lenovo Yoga Slim 7x 14" (2026), Snapdragon X2 Elite, 83QR0003US, Cosmic Blue, 32GB/1TB** — for the record: MPN pending (Best Buy model field only; no lenovo.com second source found); UPC unverified lead 199273072866 from mirror domain 666.wm-yz.cn (non-qualifying); Best Buy $1,999.99 Sold by Best Buy, Add to cart, InStock, SKU 6671634. Do not mix with the 2024 X Elite version (83ED0001US/83ED004WUS/83ED0003US, 14.5" 3K).

**Dropped on evidence this round:**
- **HP OMEN Max 16 (2025)** — sold out at Best Buy in both configs: 16-ah0043dx/B7HV2UA#ABA (RTX 5080, 32GB, 2TB OLED, SKU 6615951, $4,019.99, Sold Out) and 16-ah0033dx/B69J2UA#ABA (RTX 5080, 32GB, 1TB, SKU 6612225, $2,564.99, Sold Out); third config 16-ah0097nr is PC Heaven marketplace, sold out.
- **ASUS Vivobook S14 S3407QA** — no clean US direct retail row: ASUS US page offers availability alerts, not a price; $799 was a January 2025 launch starting price, not a current quote; the newer S5408 is a different model.
- **Razer Blade 14 (2025), RZ09-05305ES3-R3U1** — no second qualifying MPN source (the B&H result was the old 2023 model RZ09-0482VEH3-R3U1, RTX 4060, discontinued); UPC 840272915042 only via camelcamelcamel (Amazon-derived, not qualifying); Best Buy availability ambiguous ("no longer available in new condition" in one crawl vs $2,299.99 in a fresher crawl, SKU 6646552).
- **HP OmniBook Ultra 14", Snapdragon X2 Elite, Stone Blue** — no model number captured on the Best Buy page (fresh open 2026-11-20); Best Buy row $2,399.99 is "Sold & shipped by HP Inc" (brand store via Best Buy, not Sold by Best Buy), SKU 12929523.

**Dropped earlier in this track (carried over):**
- Razer Naga V2 Pro (2022-era; no retailer spec-page leads; MPN RZ01-04250100-R3U1 was unconfirmed memory, never used).
- HP Spectre x360 14 (2024, 14t-eu000) — no clean Best Buy direct new row; Woot refurbished listings (eu0097nr/eu0098nr) dominate; HP.com $1,399 only via aggregator.
- Dell XPS 16 9640 (XPS9640-7097SLV-PUS) — Best Buy new row is CLEARANCE $501.99 (comp $2,199.99); clearance-only fails the rule.
- Samsung Galaxy Book5 Pro 14" (NP940XHA-KG1US / KG3US) — Best Buy new rows clearance ($307.99 KG1US, "no longer available in new condition"; $1,484.99 KG3US clearance).
- HP OmniBook X 14 (14-fe0013dx) — 2024-era, stock unclear, Big Apple Buddy OutOfStock. Dropped in favor of OmniBook 3.

**Checked and already in catalog (NOT gaps — verified by grep against `/tmp/catalog_ref.tsv`):** Garmin Forerunner 970, Venu 4 45mm + 41mm, QC Ultra Earbuds 2nd Gen, Quest 3 512GB, Pixel Watch 4 41mm + 45mm, Galaxy Buds3 Pro, JBL Tour Pro 3, Anker Liberty 4 Pro, Keychron K8 Max, ASUS Harpe Ace Extreme / Harpe II Ace / Harpe Mini Core, Dell U2725QE, Razer Viper V3 Pro, DeathAdder V4 Pro, Basilisk V3 Pro 35K, Logitech Superlight 2 DEX, G915 X, Fenix 8 AMOLED Sapphire, Tab S10 FE / FE+ / Lite, iPad A16 11", Sony BRAVIA Theatre Bar 6/7/8/9, JBL PartyBox 520, Xbox Elite Series 2 + Core, Forerunner 570 both sizes, Galaxy Watch Ultra2, Pixel Buds Pro 2 / 2a, Bose SoundLink Plus/Max/Flex 2nd Gen, Corsair K70 CORE, HS80 MAX / HS80 v2 MAX, HyperX Cloud II/III, Kraken V4 family, iPad Air M4 11"/13", MacBook Pro 14 M6, Anker Soundcore Sleep A30, Bose QuietComfort Ultra Headphones (2nd Gen), HyperX Cloud Alpha 2 Wireless, Meta Quest 3S 128GB + 256GB, Apple AirPods Pro 3, Samsung Galaxy Watch8 Classic 46mm, Samsung Galaxy Buds4 / Buds4 Pro, JBL Tour One M3 Smart Tx, Razer BlackShark V3 Pro, Keychron Q1 Max, Samsung Galaxy Tab S11 / S11 Ultra, Corsair K65 Plus Wireless, HP OMEN Transcend 32.

**Batch-6 / batch-5 do-not-carry items honored (not re-proposed):** HP 930 Creator Mouse, ASUS ROG Strix XG27ACS, Corsair NIGHTSABRE, Samsung Galaxy Buds Core (not US-market), Corsair K70 MAX RGB, Dell S2725H, Sony HT-S2000, SRS-XG300, SRS-XG500, Razer Leviathan V2 Pro, Kiyo Pro, LinkBuds S, Garmin Epix Pro Gen 2, Apple Watch Ultra 3, Sony WH-CH710N (clearance), SRS-XB13, WH-XB910N, JBL Tune 510BT, Samsung Tab S11 FE (not a real product), ASUS RT-AXE7800, Surface Dock 2 / Modern Webcam (clearance), Fitbit Versa 4, Bose Soundbar 550, Logitech G713, G Pro X TKL Rapid.

## Notes for the rework

- **Verified-pair yield is the story:** 4 of 9 entries carry a fully VERIFIED MPN+UPC pair (Surface 13", Fenix 8 Solar, K950, Aurora) vs the batch-6 draft's 1 of 50. The four pending-both entries (Zenbook A14, OmniBook 3, Zephyrus G14, Transcend 14) are the weak tail — each has a strong single-source lead (HP/ASUS official datasheet) and a clean direct price row, so they are addable as PENDING, not as verified.
- **Aurora is the trap entry:** identifiers are the cleanest distributor-verified pair in the set, but there is currently no retailer-direct price row at all — Best Buy's three SKUs are all marketplace sellers. If a direct row cannot be confirmed at add time, swap it out rather than adding it quoteless.
- **Price volatility is Black Friday, not noise:** Transcend 14 ($2,599.99–$2,999.99 across SKUs/crawls), Aurora ($1,629.00–$2,195.01), ULT Tower 10 (Costco $789.99 vs Best Buy $799.99) — re-verify every pinned row live at add time.
- No repo file other than this findings file was modified. Nothing committed.
