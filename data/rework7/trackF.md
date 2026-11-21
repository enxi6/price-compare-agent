# Track F — rework 7: displays / accessories / queue top (12 models)

- **Date:** 2026-11-21 (all prices/stock are Black Friday-season snapshots observed 2026-11-21; Best Buy Black Friday deals end Nov 28, 2026 — re-verify every price/stock at add time)
- **Scope:** 12 models — items 1–4 are deal-site gaps (Slickdeals Tech / DealMoon), items 5–12 are queue-top positions from `data/candidates_batch6_500.md` "Queued backlogs" (see per-item source tags).
- **Method:** `browser.search` / `browser.open` (text fetch only). No live browser, no purchases, no sign-ins. Identifier VERIFIED only when TWO independent qualifying sources agree on the code for the exact model/variant/config. Qualifying: B&H spec page, Abt spec page, Micro Center spec, Crutchfield, CDW spec page, Newegg spec page, Best Buy spec panel, brand official site/spec, authorized distributor spec, brand-authored datasheet/PSREF (even when mirrored on a distributor host — the batch-6 Brio 100 precedent). NOT qualifying: Amazon in any form, eBay, aggregators (Snapklik, laptoparena, camelcamelcamel, etc.), price-tag photos, Q&A pages, search snippets alone. A single retailer spec page is NOT enough. No identifier was invented; every code below traces to a named page read in-session.
- **Membership:** checked 2026-11-21 against `/tmp/catalog_ref_500.tsv` (500 rows, verified 211 / pending 289) by exact key, normalized model-name substring (both directions), MPN, and UPC (including pending leads). **Result: 0 true collisions for all 12.** Two false positives adjudicated below. NOTE: the `/tmp/catalog_ref_500.tsv` file disappeared from /tmp after the membership greps ran (verified gone at write time); the greps themselves ran clean while it was present, and the two adjudications are recorded here. A re-run against a rebuilt reference at coordination time is cheap and recommended.
  - `echo show 8` grep hit `jbl-live-flex-3-black` — only because that row's notes field says "swapped in for Echo Show 8 per the user's approval (2026-11-16 …)". Not a model collision. (See item 3 for the history.)
  - `echo hub` / `ult tower 10` / `mag 321up` / `yeti gx` / `g614pr` / `watch7` / `SM-L300` / `book5 360` / `NP750QHA` / `e16 gen 3` / `21ST0008US` / `xg27ucg` / `yoga slim 7x` / `83QR000AUS` / `t14 gen 6` / `21QJ00CSUS` / `199272842804` — no catalog rows. Catalog has no MSI brand at all, no Yeti, no Watch7 (Watch8/Watch9/Ultra2 only), no Book5 360, no E16, no XG27UCG, no Yoga Slim 7x, no T14 Gen 6.
  - Sibling adjudications: MAG 321UP (165Hz) vs catalog 32" QD-OLEDs (Alienware AW3225QF, ASUS PG32UCDM, ProArt PA32UCDM) — different brand/model; vs the 240Hz X24 sibling (different model, different UPC — see item 1). Watch7 40mm Green vs catalog Watch8/Watch9/Ultra2 — different generation. G614PR vs catalog (no ASUS laptop in catalog) — new. E16 Gen 3 vs catalog (no Lenovo laptop in catalog) — new.
- **Result: 11 carries, 1 DROP.** MPN VERIFIED 10/11, UPC VERIFIED 4/11 (one with a caveat — see item 10). The single DROP is Book5 360 (price conflict still unresolved — see item 8). No rule was loosened; nothing was forced to fill the slots.

## Verdicts at a glance

| # | Model | Verdict | MPN | UPC | Price row |
|---|---|---|---|---|---|
| 1 | MSI MAG 321UP 32" QD-OLED 4K 165Hz | CARRY | VERIFIED | VERIFIED | B&H $569.99 InStock |
| 2 | Logitech G Yeti GX Black | CARRY | VERIFIED | VERIFIED | Best Buy $89.99 BF, Sold by Best Buy |
| 3 | Amazon Echo Show 8 (2025) Glacier White | CARRY (category flag) | VERIFIED | PENDING + lead | Best Buy $129.99 BF |
| 4 | Amazon Echo Hub White | CARRY (category flag) | VERIFIED | PENDING + lead | Best Buy $74.99 BF, Sold by Best Buy |
| 5 | Sony ULT Tower 10 Black | CARRY | VERIFIED | PENDING + lead | Best Buy $799.99, Sold by Best Buy |
| 6 | ASUS ROG Strix G16 G614PR Eclipse Gray | CARRY | VERIFIED | PENDING, no lead | Best Buy $1,749.99 BF, Sold by Best Buy |
| 7 | Samsung Galaxy Watch7 40mm Green | CARRY | VERIFIED | PENDING + lead | Best Buy $249.99, Sold by Best Buy |
| 8 | Samsung Galaxy Book5 360 NP750QHA-KA1US | DROP — stays in backlog | PENDING (single-source) | PENDING, no lead | No clean row (conflict persists) |
| 9 | Lenovo ThinkPad E16 Gen 3 21ST0008US | CARRY — now fully verified | VERIFIED | VERIFIED (new) | B&H $1,217.50 InStock |
| 10 | ASUS ROG Swift OLED XG27UCG Black | CARRY (caveats) | VERIFIED | VERIFIED with caveat | Adorama $464.99 / Micro Center $349.96 in-store-only — row to confirm at add time |
| 11 | Lenovo Yoga Slim 7x 83QR000AUS Cosmic Blue | CARRY (MPN pending) | PENDING (single-source) | PENDING, no lead | Best Buy $649.99 Holiday Deal, Sold by Best Buy — price may have moved |
| 12 | Lenovo ThinkPad T14 Gen 6 21QJ00CSUS | CARRY — promoted (direct row found) | VERIFIED | PENDING, no lead | CDW $1,811.99 InStock |

## Deal-site evidence (items 1–4)

- **1. MAG 321UP:** brief-reported "Slickdeals Tech 今日榜, B&H $569.99" — **not independently re-found in-session.** The only Slickdeals thread surfaced is the expired 2026-10-06 Newegg $571.14 one (`slickdeals.net/f/20110209`). No current Slickdeals thread for the B&H price, no saves count captured. Treat the deal-site leg as brief-reported / single-source; the B&H price itself is independently confirmed (see item 1).
- **2. Yeti GX:** brief-reported "Slickdeals Tech, Amazon $89.99" — Amazon price disregarded per the rule (never used as a source). The $89.99 price is independently confirmed at **Best Buy direct** (Black Friday Deal, fresh page open 2026-11-21) and at Staples $89.99 InStock. No current Slickdeals thread re-found in-session (only an expired 2024 thread); deal-site leg is brief-reported.
- **3. Echo Show 8:** brief-reported "Slickdeals Tech / DealMoon, Best Buy $99.99" — **the $99.99 is NOT confirmed and looks wrong.** Live Best Buy price is **$129.99 Black Friday Deal** (comp $199.99), confirmed across multiple 2-day crawls; Abt $129.99 InStock agrees. Correction recorded; do not carry $99.99.
- **4. Echo Hub:** brief-reported "Slickdeals Tech, Best Buy $74.99" — **confirmed.** Best Buy $74.99 Black Friday Deal (comp $179.99), Sold by Best Buy, multiple crawls; B&H $109.99 InStock.

## Category judgment (items 3–4)

The brief invited a DROP if the smart-display / smart-home category is unsuitable. I carried both, and here is why — the category picture changed since batch 3:

- Batch 3 (2026-11-16) swapped Echo Show 8 (3rd Gen) OUT because **both identifiers were pending — it was the weakest entry in the batch**, not because of a category ban. The "smart-displays category drops out with Echo Show 8" line in DECISIONS records the consequence of that swap, not a standing ban.
- Batch 6 then admitted **Google Nest Hub (2nd Gen) into the catalog under category `smart-home`** (`google-nest-hub-2nd-gen-charcoal`, verified 2026-11-20). Smart-home control/display hardware is therefore already in scope, and the batch-3 "Smart home, out of scope" line for Nest Hub/Doorbell is superseded.
- Both items here are also **better-evidenced than the batch-3 entry**: Echo Show 8 (2025) is a new generation (8.7" vs 8" 3rd-gen) with MPN VERIFIED and a Best Buy direct Black Friday row; Echo Hub has MPN VERIFIED and a Best Buy direct row.
- **Flag for the coordinator/user:** both are carried under the **existing `smart-home` category** (same as Nest Hub — no new category invented). The Echo Show 8 is a display-form-factor addition to that category; if the user wants smart displays kept out, drop both together at batch approval. The evidence is recorded in full below so either call is cheap.

---

## 1. MSI MAG 321UP 32" QD-OLED 4K 165Hz — Black

- **Key:** `msi-mag-321up-qd-oled-black`
- **Category:** monitors
- **Variant pinned:** Black, 31.5" QD-OLED, 3840x2160, 165Hz, 0.03ms, MAG321UPQDOLED (2024 model; first MSI model in the catalog — 0 MSI rows today)
- **Why it qualifies:** Mainstream MSI 4K QD-OLED gaming monitor; B&H direct in-stock Holiday Savings row + Micro Center spec row. Both identifiers VERIFIED — the strongest deal-site item in this track.
- **Identifiers:**
  - MPN MAG321UPQDOLED — **VERIFIED** (B&H page slug/title `msi_mag321upqdoled` + Micro Center spec "Mfr Part# MAG 321UP QD-OLED" + AVADirect "MPN: MAG 321UP QD-OLED", all for the same 165Hz model).
  - UPC 824142363720 — **VERIFIED** (B&H spec page "UPC: 824142363720" + Micro Center spec "UPC, 824142363720", agree).
- **Price / stock:** B&H $569.99 In Stock (was $699.99, Holiday Savings $130.00), free delivery Wed, Nov 25 (crawl 2 days ago; Pangoly price history confirms $569.99 first hit 2026-11-19, lowest ever). MSI US Store lists the model (price not captured — B&H is the row).
- **Flag:** Do NOT mix with the **MAG 321UP QD-OLED X24** (240Hz, MPN MAG321UPQDOLEDX24, UPC 824142449561, B&H $799.99) — a different, newer model with its own UPC. Pin the 165Hz original only. Deal-site leg is brief-reported (see "Deal-site evidence" above).

## 2. Logitech G Yeti GX — Black

- **Key:** `logitech-g-yeti-gx-black`
- **Category:** microphones
- **Variant pinned:** Black, dynamic USB-C, supercardioid, LIGHTSYNC RGB
- **Why it qualifies:** Mainstream Logitech G streaming microphone (2023, still current); Best Buy direct Black Friday row + B&H in-stock row. Both identifiers VERIFIED — the second fully-verified pair in this track.
- **Identifiers:**
  - MPN 988-000567 — **VERIFIED** (B&H "MFR #988-000567" + Best Buy model field 988-000567, SKU 6556755 + Dell "Manufacturer Part Number, 988-000567" + Lenovo US "Manufacturer PN, 988-000567" + Staples title). **Correction to the brief:** the brief's guessed "988-000570" does not exist for this mic — 988-000567 is Black; 988-000574 is White (B&H white page, UPC 097855190987). Do not use 988-000570.
  - UPC 097855190994 — **VERIFIED** (B&H spec page "UPC: 097855190994" + CompSource distributor spec "UPC EAN CODE: 097855190994" for 988-000567 + Logitech's own package-spec datasheet PDF: "Part # 988-000567 … Bar code 097855190994 (EAN-13)" — brand-authored content, same shape as the batch-6 Brio 100 precedent).
- **Price / stock:** Best Buy $89.99 Black Friday Deal (comp $169.99), Sold by Best Buy, Add to cart, InStock — **page opened fresh 2026-11-21 12:55 PST** (crawl 2026-11-21 20:55 UTC). B&H $169.99 In Stock (list reference). Staples $89.99 InStock (corroborating direct row at the same price).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Amazon $89.99 (brief) was never used as a source. Do not mix with White (988-000574 / 097855190987) or Yeti Orb (different mic).

## 3. Amazon Echo Show 8 (2025) — Glacier White [CARRY with category flag]

- **Key:** `amazon-echo-show-8-2025-glacier-white`
- **Category:** smart-home (existing category — see "Category judgment" above; no new category invented)
- **Variant pinned:** Glacier White, 2025 release / 4th Gen, 8.7" HD touchscreen, spatial audio, Alexa+, model B0DC93K4NW (AZ3 Pro chip, 13MP camera). Distinct from the batch-3 3rd-gen Echo Show 8 (8" HD) that was swapped out — different generation, different size, different ASIN.
- **Why it qualifies:** Current-generation Amazon smart display; Best Buy direct Black Friday row + Abt in-stock row. MPN VERIFIED.
- **Identifiers:**
  - MPN B0DC93K4NW — **VERIFIED** (Best Buy model field, SKU 6642846 + Staples "Model #: B0DC93K4NW" + Abt "Model: B0DC93K4NW" + Dell "Manufacturer Part Number, B0DC93K4NW").
  - UPC 840414682108 — **PENDING + lead (non-qualifying only).** camelcamelcamel lists it for B0DC93K4NW (ASIN-derived, non-qualifying); an eBay description page and a wholesale Instagram post agree — both non-qualifying. No qualifying retailer spec page prints it. Do NOT use the Graphite UPC 840414684003 (BJ's, for B0DC8ZMR1P) for this white pin.
- **Price / stock:** Best Buy $129.99 Black Friday Deal (comp $199.99), SKU 6642846, InStock, Add to cart (multiple 2-day crawls). Abt $129.99 InStock (manufacturer rebate ends 11/30/2026, comp $199.99). Staples $199.99, Out of stock for delivery. **Correction:** the brief's $99.99 was not confirmed anywhere — $129.99 is the live Best Buy price.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Amazon's own price never used. A second Best Buy SKU 12376837 shows $156.55 — pin SKU 6642846 ($129.99) only. Category flag: display-form-factor addition to `smart-home`; drop at batch approval if the user wants smart displays out (see "Category judgment").

## 4. Amazon Echo Hub 8" — White [CARRY with category flag]

- **Key:** `amazon-echo-hub-white`
- **Category:** smart-home (existing category — same as Nest Hub)
- **Variant pinned:** White, 8" smart home control panel, Alexa+, model B0BCR7M9KX (hardware model G6A87E; Zigbee/Matter/Thread)
- **Why it qualifies:** Current Amazon smart-home control panel; Best Buy direct Black Friday row + B&H in-stock row. MPN VERIFIED.
- **Identifiers:**
  - MPN B0BCR7M9KX — **VERIFIED** (Best Buy model field, SKU 6562248 + B&H page slug/title `amazon_b0bcr7m9kx_echo_hub`).
  - UPC 840268960544 — **PENDING + lead (B&H only).** B&H spec page prints it; the only other prints are non-qualifying (everzento mirror, tanotis, eBay, camelcamelcamel). No second qualifying source found.
- **Price / stock:** Best Buy $74.99 Black Friday Deal (comp $179.99), SKU 6562248, Sold by Best Buy, InStock (multiple crawls 2–7 days old; a Threads screenshot of the Best Buy page the same day also shows $74.99). B&H $109.99 In Stock (was $179.99, Holiday Savings $70.00).
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Amazon's own price never used. Category flag: same as item 3 — drop with item 3 if the user wants smart-home control panels out. Note a BrickSeek post flagged Walmart clearance $45 (Aug 2026) — clearance chatter, not a usable row; the Best Buy new row is clean.

## 5. Sony ULT Tower 10 — Black [queue: strongest non-carried alternate, track D]

- **Key:** `sony-ult-tower-10-black`
- **Category:** speakers
- **Variant pinned:** Black, SRSULT1000 (360° party speaker, wireless mic included)
- **Why it qualifies:** Mainstream Sony party speaker; Best Buy direct row re-confirmed live. MPN VERIFIED; UPC still single-source (unchanged from track D).
- **Identifiers:**
  - MPN SRSULT1000 — **VERIFIED** (B&H spec page "MFR # SRSULT1000" + Crutchfield "MFR # SRSULT1000" + Best Buy model field, SKU 6577679).
  - UPC 027242928978 — **PENDING + lead (Adorama only).** Adorama spec page lists "UPC Code 027242928978" for SRSULT1000 — the same single source as track D; no second qualifying source surfaced in this session (Amazon/eBay/camelcamelcamel agree, all non-qualifying). B&H spec page still prints no UPC; Best Buy crawled page contains no UPC.
- **Price / stock:** Best Buy $799.99 (comp $1,199.99, Save $400), Sold by Best Buy, SKU 6577679, InStock (multiple crawls 1–3 days old; open-box $567.99–$610.99 — pin new only). B&H "No Longer Available"/Discontinued (track D) — Best Buy is the row.
- **Flag:** UPC needs one more qualifying source. Costco $789.99/$799.99 (item 1916855) is Instagram price-tag only — not a row.

## 6. ASUS ROG Strix G16 G614PR — Eclipse Gray [queue: strongest ASUS backlog item, track G]

- **Key:** `asus-rog-strix-g16-g614pr-rtx-5070-ti-eclipse-gray`
- **Category:** laptops
- **Variant pinned:** Eclipse Gray, G614PR-G16.R95070TI — Ryzen 9 8940HX, RTX 5070 Ti 12GB, 16GB DDR5-5600, 1TB SSD, 16" WUXGA 1920x1200 165Hz, Win 11 Home
- **Why it qualifies:** Current ROG gaming laptop; Best Buy direct Black Friday row. **MPN now VERIFIED — the missing leg from track G is closed this session** (ROG official spec page names the exact config).
- **Identifiers:**
  - MPN G614PR-G16.R95070TI — **VERIFIED** (Best Buy model field, SKU 6613956 + ROG official spec page `rog.asus.com/us/laptops/rog-strix/rog-strix-g16-2025-g614/spec/`, opened 2026-11-21, which lists "G614PR-G16.R95070TI" twice in its config list).
  - UPC — **PENDING, no lead for this config.** No qualifying source prints a UPC for G614PR-G16.R95070TI. laptoparena lists 197105821606, but that is for a DIFFERENT regional config (G614PR-RV003W, 90NR0NJ7-M000M0) — do NOT attach it to the US Best Buy config. B&H does not carry this config.
- **Price / stock:** Best Buy $1,749.99 Black Friday Deal, SKU 6613956, Sold by Best Buy, InStock (multiple 2-day crawls; JSON-LD confirms InStock). A second Best Buy SKU 10936980 shows $2,209.99 — pin SKU 6613956 only. Open-box Excellent $1,267.99 (Slickdeals, expired) — not a new row.
- **Flag:** Promo price — Black Friday ends Nov 28, 2026. Best Buy price was volatile in track G ($1,749.99–$2,209.99 across SKUs/crawls) — re-check at add time. ASUS Store US lists the G614 family from $2,099.99 (different configs).

## 7. Samsung Galaxy Watch7 40mm BT — Green [queue B1, track F]

- **Key:** `samsung-galaxy-watch7-40mm-green`
- **Category:** wearables
- **Variant pinned:** Green, 40mm BT, SM-L300NZGAXAA (2024; sibling color of track-F F4 Cream)
- **Why it qualifies:** Prior-generation Samsung watch, still sold new by Best Buy; Best Buy direct row. MPN VERIFIED on the same two legs as the Cream sibling.
- **Identifiers:**
  - MPN SM-L300NZGAXAA — **VERIFIED** (Best Buy model field, SKU 6585116 + Samsung official Wearables MSRP Price Lists, Mar/Jun/Jul/Sep 2026 editions, all agree — the same pair that verified the Cream sibling F4 in track F).
  - UPC 887276868905 — **PENDING + lead (Samsung MSRP list only).** The Samsung MSRP price list (Mar 2026 PDF) ties SM-L300NZGAXAA = Galaxy Watch7 BT 40mm Green, UPC 887276868905, MSRP $249.99 — but that is one publisher; no B&H/Abt retailer spec page printing the same UPC was found in-session. Do not mark VERIFIED until that second source is found.
- **Price / stock:** Best Buy $249.99, SKU 6585116, Sold by Best Buy, InStock (multiple 2–3 day crawls; JSON-LD confirms InStock). **Note the color split:** the Cream sibling is $149.99 Black Friday; Green shows $249.99 with no Black Friday deal in crawls (one crawl showed $229.99 on a different SKU 10923234 — seller unclear, do not use). Refurbished Excellent $134.97 (Networkstore marketplace) and open-box $64.99 exist — pin the new SKU 6585116 only.
- **Flag:** Prior generation (2024), superseded by Watch8/Watch9, but still sold new by Best Buy — not clearance (no clearance tag on the new row). Membership: catalog has no Watch7 at all; distinct from Watch8 40mm Graphite (SM-L320NDAAXAA) and Watch9 40mm (SM-L340NZKAXAA).

## 8. Samsung Galaxy Book5 360 15.6" — Gray (NP750QHA-KA1US) [queue B2, track F — DROP, stays in backlog]

- **Key (if ever carried):** `samsung-galaxy-book5-360-15-6-gray`
- **Category:** laptops
- **Variant pinned:** Gray, 15.6" FHD AMOLED touch 2-in-1, Core Ultra 7 256V, 16GB, 512GB, NP750QHA-KA1US
- **Why it drops:** the price conflict that put it in the backlog is **still unresolved after re-check**, and the identifiers have not improved. Not forced.
- **Identifiers:**
  - MPN NP750QHA-KA1US — **PENDING (Best Buy model field only).** No second qualifying source found in-session.
  - UPC — **PENDING, no lead found.**
- **Price / stock — conflicted, no clean row:**
  - Best Buy crawl A (3 days ago): **$358.99**, "Save $991, Comp. Value: $1,349.99" — implausible for a $1,349.99 laptop; reads as a pricing glitch / Q&A-page artifact (the same $358.99 appears on the Best Buy Q&A page).
  - Best Buy crawl B (2–4 days ago): **$2,187.81, Unavailable** (SKU 13224856).
  - buybeststores.com mirror: $609.99 "In Stock (On Sale)" — a Best Buy mirror site, not a qualifying retailer.
  - No samsung.com row surfaced; no clean Best Buy direct in-stock price at any consistent value.
- **Flag:** DROP — leave in the Samsung backlog. Re-check only if a single consistent Best Buy direct price appears and a second MPN source is found. Do NOT carry on the $358.99 (glitch-shaped) or the $2,187.81 (unavailable). Do not confuse with Galaxy Book5 15.6" NP750XHD-KB1US (track-F F5, different model — Best Buy $799.99 BF) or Book5 Pro 360 (marketplace-only at Best Buy).

## 9. Lenovo ThinkPad E16 Gen 3 — Black (21ST0008US) [queue: Lenovo sweep pick not carried, track E]

- **Key:** `lenovo-thinkpad-e16-gen-3-black`
- **Category:** laptops
- **Variant pinned:** Black, 21ST0008US — AMD Ryzen 7 250, 16GB DDR5, 512GB SSD, 16" WUXGA 1920x1200 touchscreen IPS, Win 11 Pro
- **Why it qualifies:** **The UPC gap from track E is closed this session — now a fully VERIFIED MPN+UPC pair**, plus a fresh B&H direct in-stock row. Strongest queue promotion in this track.
- **Identifiers:**
  - MPN 21ST0008US — **VERIFIED** (CDW spec page "MFG#: 21ST0008US | CDW#: 9084576" + NeweggBusiness spec page "Part Number | 21ST0008US", same config; B&H page slug `lenovo_21st0008us` agrees).
  - UPC 198157339941 — **VERIFIED (new)** (B&H spec page, opened fresh 2026-11-21: "UPC: 198157339941" on the 21ST0008US page, Ryzen 7 250 / 16GB / 512GB / touchscreen + Lenovo official PSREF for ThinkPad E16 Gen 3 (AMD), hosted on Ingram Micro: "21ST0008US … EAN / UPC / JAN : 198157339941". Brand-authored PSREF + retailer spec page — same shape as the batch-6 Brio 100 datasheet precedent. technologygalaxy / simplifiedcomputers agree, non-qualifying.)
- **Price / stock:** B&H $1,217.50 In Stock, Add to cart, free delivery Wed, Nov 25 (page opened fresh 2026-11-21). CDW In Stock, $1,212.99 advertised (track E, search crawl — re-check at add time; B&H is the row). Best Buy listing is Merchant Expo marketplace ($1,311.63) — not usable.
- **Flag:** None on identifiers. Note the B&H page also lists a Ryzen 5 / 256GB config and a non-touch option — pin the Ryzen 7 250 / 512GB / Multi-Touch config only.

## 10. ASUS ROG Swift OLED XG27UCG 27" — Black [queue: ASUS backlog, track G]

- **Key:** `asus-rog-strix-xg27ucg-black`
- **Category:** monitors
- **Variant pinned:** Black, 27" 4K 160Hz / FHD 320Hz dual-mode Fast IPS, XG27UCG
- **Why it qualifies:** Current ROG dual-mode gaming monitor; MPN VERIFIED (unchanged from track G); UPC now two-sourced — see caveat. Price row is the weak leg (see Flag).
- **Identifiers:**
  - MPN XG27UCG — **VERIFIED** (Micro Center product name + CompSource "Mfr Part # XG27UCG", per track G; Adorama "MFR: XG27UCG" agrees).
  - UPC 197105564633 — **VERIFIED with caveat** (CompSource distributor spec "UPC EAN CODE: 197105564633" for XG27UCG + ASUS official brochure/catalog-object print for 90LM0AG1-B01370 (XG27UCG): "4711387564646 0197105564633 / 197105564633" — brand-authored content mirrored via distributor catalog hosts; Adorama spec page also prints "UPC Code 197105564633". **Caveat:** track G called this PENDING on a stricter reading (CompSource single-source + Adorama not on its qualifying list). This verdict upgrades on the ASUS brochure leg, not on Adorama. If the coordinator applies the strictest reading, downgrade to PENDING + lead (CompSource) — the code itself is not in doubt, only the leg-counting.)
- **Price / stock:** No single clean row — re-confirm at add time:
  - Best Buy $464.99–$469.99 (Model XG27UCG, SKU 12567152; 8–10 day crawls) — **seller of the main offer not confirmed** ("More options from Marketplace sellers $464.99–$575.93"); do not use as the row without a fresh seller check.
  - Micro Center $349.96 InStoreOnly (track G) — in-store-only row, weak.
  - Adorama $464.99 (170-day crawl) / $469.99 — retailer-direct, but Adorama has not been used as the price row in prior batches; corroboration only unless the coordinator accepts it.
  - Slickdeals 2026-04-15: Best Buy $299 (expired); Pangoly 90-day average $444, lowest $299.
- **Flag:** Price row to confirm at add time (Best Buy seller check first). **Supersession risk:** the Gen2 XG27UCGR (4K 162Hz / FHD 485Hz) is current at ROG US $399.00 InStock and Micro Center $399.99 — the original XG27UCG is being superseded; if the Best Buy row is dead at add time, consider the Gen2 instead (it has no UPC lead yet — see track G backlog item 4). Do NOT mix with XG27UCSR (UPC conflicted) or XG27UCDMG / XG27UQDMS (OLED, different models).

## 11. Lenovo Yoga Slim 7x 14" — Cosmic Blue (83QR000AUS) [queue B2, track E]

- **Key:** `lenovo-yoga-slim-7x-14-cosmic-blue`
- **Category:** laptops
- **Variant pinned:** Cosmic Blue, 83QR000AUS — Snapdragon X2 Plus X2P-42-100 (2026), 16GB LPDDR5X, 512GB SSD, 14" 2K OLED touchscreen (1920x1200, 60Hz, 600 nits), Copilot+ PC
- **Why it qualifies:** Current 2026 ARM ultraportable; Best Buy direct Holiday Deal row. MPN still single-source — the second source sought this session was not found (see Identifiers).
- **Identifiers:**
  - MPN 83QR000AUS — **PENDING (Best Buy model field only).** Targeted re-search for a second source (lenovo.com, B&H, PSREF, "14Q8Y11") surfaced only Best Buy listings and a review-site mention ("Yoga Slim 7 14Q8Y11 (83QR000AUS)" — non-qualifying). No lenovo.com page, no B&H listing, no PSREF hit in-session. One second source away from a pick, same as track E.
  - UPC — **PENDING, no lead found.**
- **Price / stock:** Best Buy SKU 6672161, Sold by Best Buy, Holiday Deal **$649.99** (comp $1,299.99), Add to cart (5-day crawl; Slickdeals confirms $649.99, Nov 16). **Price may have moved:** the freshest 1–2 day crawls show $1,299.99 as the main offer price, with the $649.99 appearing only in the older crawl — re-check live at add time and carry the live price. A second Best Buy SKU 12949047 ($949.00) is sold by PC Heaven (marketplace) — pin SKU 6672161 only. Open-box Excellent $584.99.
- **Flag:** MPN single-source + price in flux ($649.99 vs $1,299.99 across crawls). Do not mix with the 2024 X Elite version (83ED0001US/83ED004WUS/83ED0003US, 14.5" 3K) or the 1TB config 83QR0002US (Best Buy $1,649.99, single-source).

## 12. Lenovo ThinkPad T14 Gen 6 — Black (21QJ00CSUS) [queue B3, track E — PROMOTED]

- **Key:** `lenovo-thinkpad-t14-gen-6-black`
- **Category:** laptops
- **Variant pinned:** Black, 21QJ00CSUS — AMD Ryzen AI 7 PRO 350, 16GB DDR5, 512GB SSD, 14" WUXGA 1920x1200, Win 11 Pro
- **Why it qualifies:** **The missing direct price row from track E is found this session — CDW In Stock with an advertised price.** MPN VERIFIED (unchanged). Promoted from backlog.
- **Identifiers:**
  - MPN 21QJ00CSUS — **VERIFIED** (CDW spec page: "MFG#: 21QJ00CSUS | CDW#: 8391802", Ryzen AI 7 PRO / 16GB / 512GB / WUXGA + Best Buy model field, multiple SKUs).
  - UPC — **PENDING, no lead found.** **Do NOT attach B&H's UPC 199272842804 — that belongs to a DIFFERENT T14 Gen 6 config (21QDS2VV00, $1,699.00).** Repeated here because the warning matters: the code is one search away and wrong for this pin.
- **Price / stock:** CDW In Stock, **$1,811.99 advertised** (CDW#: 8391802; "Ships same day if ordered before 2 PM CT" — multiple CDW search crawls agree on $1,811.99; one crawl showed $1,712.99). **Caveat:** the CDW crawls are 167–173 days old — the price must be re-verified live at add time (track-E caveat 2: CDW prices come from search crawls, not the direct open). Best Buy new listings remain marketplace (Mobile Advance $1,744.14; $1,663.58–$1,856.01 range) or refurbished ($1,049.00, SKU 12834639) — not usable; CDW is the row. No lenovo.com US page for this exact part surfaced.
- **Flag:** CDW price is stale-dated (see above) — re-check at add time; if CDW no longer lists it in stock, this drops back to backlog. Distinct from the carried T14 Gen 5 (21MC000CUS, different generation) and from the Intel config 21QC007CUS (lenovo.com $667.99, different pin).

---

## Tally

- **Models researched in-session: 12** (all 12 in the brief; no substitutes added).
- **Carries: 11. DROP: 1** (Book5 360 — price conflict unresolved, stays in Samsung backlog; do not force).
- **Identifier tally (11 carries): MPN VERIFIED 10 / 11** (only Yoga Slim 7x pending); **UPC VERIFIED 4 / 11** (MAG 321UP, Yeti GX, E16 Gen 3, XG27UCG-with-caveat); **UPC PENDING 7 / 11** (Echo Show 8 lead, Echo Hub lead, ULT Tower 10 lead, G614PR no lead, Watch7 Green lead, Yoga Slim 7x no lead, T14 Gen 6 no lead).
- **Queue progress this session:** 3 backlog items materially advanced — E16 Gen 3 UPC VERIFIED (was non-qualifying lead only), G614PR MPN VERIFIED (was single-source), T14 Gen 6 direct row found (was quoteless). 2 items unchanged after re-check — ULT Tower 10 UPC still single-source, Yoga Slim 7x MPN still single-source. 1 item confirmed still blocked — Book5 360 price conflict persists.
- **Corrections to the brief (recorded, not silently fixed):** (a) Yeti GX Black MPN is **988-000567**, not the brief's guessed 988-000570; White is 988-000574. (b) Echo Show 8 Best Buy price is **$129.99**, not $99.99. (c) MAG 321UP Slickdeals thread for the B&H $569.99 price could not be independently re-found (only an expired 2026-10-06 Newegg thread); the B&H price itself is confirmed.
- **Membership check:** 0 true collisions vs the 500-model reference (see header; reference file disappeared from /tmp after the greps — re-run at coordination time).
- **Nothing else modified:** only this findings file was written. No changes to catalog.py, DECISIONS.md, snapshots, or the site. Prices are 2026-11-21 snapshots; re-verify every price/stock/identifier at add time, especially the promo rows (Best Buy Black Friday ends Nov 28, 2026).
