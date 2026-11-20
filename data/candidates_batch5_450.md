# Batch 5 candidate list — catalog 400 → 450

- **Date:** 2026-11-20
- **Status:** LIST ONLY — candidate list for user approval. Nothing in this file has been added to the catalog. No repo file other than this one was modified; nothing committed or pushed.
- **How it was built:** 12 seeds from `data/candidates_batch5_450_seed.md` (re-checked 2026-11-20) + 4 parallel fresh-pick research groups (seeds re-check; ASUS/Dell/HP/HyperX/Corsair/Keychron; Samsung/Google/Apple/Nintendo + Bose/Microsoft/Lenovo/Alienware/Meta; Sony/Logitech/JBL/Razer/Anker/Garmin) + 1 synthesis probe (JBL Authentics 300). Synthesis re-verified every brief-supplied identifier against the two-source rule and downgraded 10 brief "VERIFIED" markings to PENDING (see "Corrections to brief-supplied markings"); the brief groups' membership claims were re-run at synthesis with a model-name check added — the final 50 has 0 true collisions (see "Membership check").
- **Rules applied:** DECISIONS 001–005, 015, 016, 020, 021, 027, 057, 068. Mainstream/new products; US-market versions only; seller-direct only (brand direct or retailer direct); no Amazon in any form, no third-party/marketplace sellers, no parallel imports, no international variants, no second-hand/refurbished/clearance-only/discontinued stock. Every candidate checked against all 400 catalog rows (key/model/MPN/UPC, including different colors/configs of the same model) — no duplicates (verified at synthesis by script: 0 true collisions; 2 adjudicated size/model siblings, see "Membership check").
- **Identifier honesty:** UPC/EAN is marked VERIFIED only when found on a retailer/manufacturer spec page or an official source, ideally two independent sources. A single retailer spec page is NOT enough (batch-4 Endurance Race 2 precedent) — single-source codes are PENDING with the lead and what was checked. Amazon-only and eBay-only values are never treated as verified. Non-US suffixes (R3G1, EUB, CE7) are never carried as the US code. Keychron EAN + SKU follows the K8 Ultra 8K precedent (identifiers recorded as EAN + SKU, not UPC). Suggested `key` values follow existing catalog slug conventions and are proposals only.
- **Identifier tally for the 50:** UPC/EAN VERIFIED 21 / PENDING 29. The verified rate (42%) is below batch 4's draft (46%) — the fresh-pick groups supplied fewer two-source codes this round, and synthesis downgraded 10 brief-supplied "VERIFIED" markings to PENDING (see "Corrections to brief-supplied markings"). No rule change is proposed; identifiers stay pending per the standing rule. The tally here is counted from the per-entry markings in this file.
- **New categories in this batch:** routers (RT-BE58U is the first router in the set — needs approval at add time, DECISIONS 016). No other new category. (Bose Bass Module 700 is categorized under speakers — the catalog has no subwoofers category.)
- **Brands with zero models in the final 50:** none of the standing gaps — all five gap brands are filled this round (Bose 1, Microsoft 2, Lenovo 1, Alienware 2, Meta 2).

## Candidates (50)

### 1. Sony BRAVIA Theatre Rear 9, Black — `sony-bravia-theatre-rear-9-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN SA-RS9 (Sony US PDP "Model: SA-RS9"; Best Buy model SARS9, SKU 6673696).
- **Why it qualifies:** Current Sony rear-speaker pair (2026, 180W, Dolby Atmos/DTS:X, 360 Spatial Sound Mapping); pairs with Bar 9/8/7 and HT-A7000/A5000/A3000. Sony direct list $749.99.
- **Identifiers:** MPN SA-RS9; UPC **027242934221 — VERIFIED** (B&H spec page + NFM "UPC + Model SARS9" + DataVision "MFR SARS9, $548").
- **Price/stock:** Best Buy $549.99 InStock, sold by Best Buy, Add to cart (fresh page fetch 2026-11-20, SKU 6673696) — restock due today has landed; Abt $548 InStock; Target $548 InStock; Sony direct $749.99 list.
- **Flag:** Promo price ($548–549.99 vs $749.99 comp, Black Friday ends Nov 28). Abt rebate ended 11/18 but price held at $548. Note Best Buy shows multiple SKUs (6673696 / 12655141 / 12722006) with $548 vs $549.99 — use $549.99 fresh fetch.

### 2. JBL Authentics 500, Black — `jbl-authentics-500-black`
- **Category:** speakers (smart-home speaker with Alexa/Google voice)
- **Variant pinned:** Black, MPN JBLAUTH500BLKAM (JBL.com + Crutchfield MFR # agree).
- **Why it qualifies:** Current JBL flagship home speaker, Dolby Atmos Music, Wi-Fi/Bluetooth; clean direct rows at Abt/Sweetwater.
- **Identifiers:** MPN JBLAUTH500BLKAM; UPC **050036396264 — VERIFIED** (B&H spec page + Erikson Consumer distributor spec "Model JBLAUTH500BLKAM").
- **Price/stock:** Abt $399.95 InStock (rebate to 12/05/2026); Sweetwater $399.95; Crutchfield $749.95 InStock (fresh fetch Nov 12 — the $449.95 sale has ended, now list); JBL direct OutOfStock.
- **Flag:** Price moved — live range is $399.95–$749.95. Promo price (Abt rebate ends 12/05/2026). Smart-home category. Do NOT use the JBLAUTH500BLKAM-Z listing ($562.95) as price evidence — -Z is a different listing.

### 3. JBL Vibe Flex 2, Black — `jbl-vibe-flex-2-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN JBLVFLEX2BLKAM (JBL.com Item#; White is JBLVFLEX2WHTAM).
- **Why it qualifies:** Current JBL true-wireless earbuds (2024–now, 12mm drivers, Smart Ambient); JBL direct $69.95.
- **Identifiers:** MPN JBLVFLEX2BLKAM; UPC **050036404921 — VERIFIED** (Erikson Consumer spec "Model JBLVFLEX2BLKAM" + Visions + Addison Électronique).
- **Price/stock:** JBL direct Black $69.95 InStock (2-day-old crawl) — seed's OOS flag is reversed; Black is back in stock.
- **Flag:** Variant stays Black — no switch to White (White also in stock, but Black is live). No Best Buy US or B&H US listing found. Do NOT use gen-1 codes: UPC 050036391368 and eBay GTIN 0050036391344 belong to the gen-1 Vibe Flex (JBLVFLEXMITAM etc.).

### 4. Razer Leviathan V2 X, Black — `razer-leviathan-v2-x-black`
- **Category:** soundbars
- **Variant pinned:** Black, MPN RZ05-04280100-R3U1 (Best Buy model, SKU 6521035).
- **Why it qualifies:** Current Razer compact PC soundbar (USB-C, Bluetooth 5.0, Chroma RGB, no subwoofer); Best Buy $99.99 sold by Best Buy.
- **Identifiers:** MPN RZ05-04280100-R3U1; UPC **810056146771 — VERIFIED** (B&H spec page + Abt spec "Model RZ05-04280100-R3U1" + Electronic Express).
- **Price/stock:** Best Buy $99.99, sold by Best Buy, InStock (fresh fetch, SKU 6521035); B&H $99.99; Staples $106.66 InStock.
- **Flag:** Clean row, no promo flag. Do NOT use R3M1 (UK/EU, EAN 8886419379645) or the Kuromi edition RZ05-04280300-R3M1. Distinct from in-catalog Leviathan V2 (has subwoofer; V2 X has none). Note: the in-catalog Leviathan V2's own MPN is unresolved — its identifiers are empty, its variant string carries RZ05-03920100-R3U1, and the seed file cited RZ05-04160100-R3U1 (see "Membership check").

### 5. Razer Nommo V2 Pro, Black — `razer-nommo-v2-pro-black` — HOLD
- **Category:** speakers
- **Variant pinned:** Black, 2.1 with wireless subwoofer + wireless control pod, THX Spatial Audio.
- **Why it qualifies:** Razer's top desktop speaker set; Razer US list $449.99 (confirmed Nov 12, 2026).
- **Identifiers:** MPN **RZ05-04740100-R3U1 — CONFIRMED** (Razer.com URL + Best Buy model field, fresh fetch) — the seed's suffix trap is resolved; R3G1 is UK/EU, correctly not carried. UPC PENDING, strong lead **840272904794** (Best Buy spec panel only, 135-day-old crawl) + Amazon mirrors; no second independent retailer source.
- **Price/stock:** Best Buy new row is DEAD — fresh fetch: "This item is no longer available in new condition" (it already said so 135 days ago; the $449.99 in search snippets was a stale reviews-page remnant). Razer US lists $449.99, but the text fetch shows no buy box/stock signal — stock unconfirmed.
- **Flag:** HOLD as pending seed; add only if Razer US stock confirms at add time. Do not use Best Buy as the row. Distinct from in-catalog Nommo V2 (mid tier, wired sub) — Pro has wireless sub + control pod + rear-projection Chroma.

### 6. Razer Nommo V2 X, Black — `razer-nommo-v2-x-black`
- **Category:** speakers
- **Variant pinned:** Black, 2.0, no subwoofer, THX Spatial Audio, MPN RZ05-04760100-R3U1 (Best Buy model, SKU 6547859).
- **Why it qualifies:** Entry tier of the Nommo V2 line; Razer US list $149.99; Best Buy $149.99.
- **Identifiers:** MPN RZ05-04760100-R3U1 (Best Buy model, fresh fetch); UPC PENDING, lead **840272904510** (Desertcart only — Amazon-data mirror, not independent). EAN 8887910060292 belongs to the UK R3G1 — do not attach.
- **Price/stock:** Best Buy $149.99, sold by Best Buy, InStock (fresh fetch, SKU 6547859); Razer US $149.99 InStock.
- **Flag:** No promo flag. Distinct from in-catalog Nommo V2 — V2 X has no subwoofer, no control pod, no Chroma. Keep separate.

### 7. HyperX Cloud Stinger 2 Core, PC, Black — `hyperx-cloud-stinger-2-core-pc-black`
- **Category:** headphones
- **Variant pinned:** PC version, Black, MPN 683L9AA — confirmed as the PC version by 4 sources: HyperX US (Compatibility: PC), HP.com (Product # 683L9AA), Best Buy (Model 683L9AA), Micro Center (Mfr Part # 683L9AA).
- **Why it qualifies:** Current HyperX entry-level wired PC headset (40mm drivers, swivel-to-mute); HyperX US $39.99 InStock (Black Available).
- **Identifiers:** MPN 683L9AA; UPC **196548418183 — VERIFIED** (Micro Center "Mfr Part # 683L9AA" + Newegg "MPN 683L9AA").
- **Price/stock:** HyperX US $39.99 InStock; Best Buy $39.99 InStock, Add to cart; HP.com $39.99 InStock.
- **Flag:** Strongest seed this round — MPN and UPC both now verified from non-Amazon sources. PS version is 6H9B5AA (White) / 6H9B6AA (Black), Xbox version is "CloudX Stinger 2 Core" — this entry pins the PC version 683L9AA only. Distinct from in-catalog Cloud Stinger 2 (non-Core).

### 8. Sony INZONE E9, Black — `sony-inzone-e9-black`
- **Category:** earbuds (wired IEM)
- **Variant pinned:** Black, MPN IER-G900B (Sony US PDP, model IER-G900B; US variant IERG900B.UC; EU CE7 is IERG900B.CE7 — different suffix, do not mix).
- **Why it qualifies:** Current Sony IEM (Aug 2025 launch with Fnatic; no mic; Glass Purple is a new colorway Oct 2026, not a separate model).
- **Identifiers:** MPN IER-G900B; UPC **027242933187 — VERIFIED** (DataVision "MFR IERG900B, Condition: New, $118" + Kawartha TV "UPC 027242933187").
- **Price/stock:** Target Black $118 InStock (reg $148, 1-day crawl); Best Buy Black $118 InStock (Model IERG900/B, 2-day crawl); Audio46 Black $119.99 in stock. Sony direct page is stale (Apr 14 crawl, $139.99 sale) — current Sony stock unknown, but Target + Best Buy suffice.
- **Flag:** Promo — $118 vs $149.99 list (Black Friday). Do NOT attach EAN 4548736171107/4548736171084 (different suffixes/regions). Glass Purple is a colorway, not a separate model.

### 9. JBL Charge 5, Black — `jbl-charge-5-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN JBLCHARGE5BLKAM (Best Buy model, fresh fetch).
- **Why it qualifies:** Previous-gen JBL speaker still sold new at JBL US ($139.95) and Best Buy ($139.99).
- **Identifiers:** MPN JBLCHARGE5BLKAM; UPC PENDING — strong lead 050036380218 (Abt spec "Model JBLCHARGE5BLKAM", 10–18-day crawls + Zoro per 11-18 seed; needs a second fresh retailer source at add time).
- **Price/stock:** JBL US new $139.95 (19-day crawl); Best Buy $139.99, comp $179.95, Add to cart (1–2-day crawls; marketplace rows $114.95–$129.99 excluded).
- **Flag:** Do NOT quote $134.95 as the new price — the fresh JBL.com fetch showing $134.95 InStock was the refurbished-variant URL. Discontinued tension unchanged: Zoro still marks it Discontinued; Charge 6 is current and in catalog. KEEP as pending with the flag, not as a current-generation pick.

### 10. ASUS RT-BE58U, Black — `asus-rt-be58u-black`
- **Category:** routers — NEW category (no ASUS router is in the 400-model catalog; needs approval at add time, DECISIONS 016).
- **Variant pinned:** Black, single unit (BE3600 dual-band WiFi 7, 2.5G WAN/LAN).
- **Why it qualifies:** Current ASUS WiFi 7 dual-band router; ASUS direct $149.99 InStock.
- **Identifiers:** MPN RT-BE58U (ASUS US + Adorama MFR agree); UPC **197105452916 — VERIFIED** (Adorama spec page "UPC Code 197105452916" + CompSource "UPC EAN CODE: 197105452916, MARKET: US" agree).
- **Price/stock:** ASUS direct $149.99, InStock (asus.com, crawled 2026-11-19); Adorama $169.00. (Target $124.99 listing is manufacturer-refurbished — excluded.)
- **Flag:** Minor note that ASUS lists a HW Ver 2.0 firmware — no variant split seen in US retail.

### 11. ASUS ROG Strix OLED XG27ACDMS, Black — `asus-rog-strix-oled-xg27acdms-black`
- **Category:** monitors (27" QD-OLED QHD 280Hz, 0.03ms)
- **Variant pinned:** Black, single colorway.
- **Why it qualifies:** Current ASUS 27" QD-OLED gaming monitor; Best Buy $399.99 InStock, sold by Best Buy.
- **Identifiers:** MPN XG27ACDMS (Best Buy model; ASUS eShop part 90LM0B60-B013C1 vs NationalPC 90LM0B60-B01311 — suffix discrepancy, use XG27ACDMS as the catalog MPN); UPC **197105871380 — VERIFIED** (PBTech retailer spec page "UPC 197105871380, MPN XG27ACDMS", seen across multiple crawls + NationalPC.in "UPC 197105871380, EAN 4711387871386" agree).
- **Price/stock:** Best Buy $399.99, InStock, sold by Best Buy, Add to cart (comp. value $649.99 — Black Friday promo); ASUS direct $649.00, OutOfStock.
- **Flag:** Promo price — $399.99 is $250 off list; re-check at add time.

### 12. Dell UltraSharp 34 Curved Thunderbolt Hub Monitor U3425WE, Silver — `dell-ultrasharp-34-curved-u3425we-silver`
- **Category:** monitors (34.1" UWQHD 3440×1440, 120Hz IPS Black, Thunderbolt 4 hub, 90W PD)
- **Variant pinned:** Silver (single colorway).
- **Why it qualifies:** Current Dell 34" ultrawide Thunderbolt hub monitor; Adorama and Abes of Maine carry it new.
- **Identifiers:** MPN V124N (Dell US tech specs, "Manufacturer Part Number, V124N") — note HK variant is X2RV9, do not mix; catalog convention for Dell uses the Dell config code (cf. U3225QE = 3PVPJ). UPC PENDING — lead 884116452034 (single source: ComptechDirect EAN/UPC list, on a Grade-A-refurbished listing — weak; verify at add time).
- **Price/stock:** Adorama $769.00 (search snippets say InStock; but the fetched Adorama page's JSON-LD says Availability: Discontinued — conflicting signals, flag); Abes of Maine $789.00, In stock (list $999; page mixes several Dell monitors, price attributed to SKU DELL-U3425WE). Dell.com US price/stock NOT captured — the fetched Dell.com page returned tech specs only, no offer block.
- **Flag:** Weakest price evidence of the 13 — Dell.com price + Adorama stock conflict must be re-checked at add time; do not add on the Adorama row alone.

### 13. Dell Pro 32 Plus 4K USB-C Hub Monitor P3225QE, Black — `dell-pro-32-plus-4k-p3225qe-black`
- **Category:** monitors (31.5" 4K UHD 3840×2160 IPS, 100Hz, USB-C hub, 90W PD)
- **Variant pinned:** Black/Gray (single colorway).
- **Why it qualifies:** Current Dell 32" 4K USB-C hub monitor; Adorama, B&H and Target all carry it new.
- **Identifiers:** MPN P3225QE; UPC PENDING — EAN lead 5397184962527 (Target PDP "UPC" field; 13-digit, so treat as EAN lead, not a US UPC — verify at add time).
- **Price/stock:** Adorama $499.00 new (via Klarna comparison); B&H $499.99; Target $525.00.
- **Flag:** Distinct from in-catalog U3225QE (Thunderbolt) and S3225QS — this is the Pro-line USB-C model.

### 14. HP 975 Dual-Mode Wireless Keyboard, Black — `hp-975-dual-mode-wireless-keyboard-black`
- **Category:** keyboards (full-size, BT + 2.4GHz, rechargeable, programmable)
- **Variant pinned:** Black (single colorway).
- **Why it qualifies:** Current HP full-size dual-mode wireless keyboard; HP.com $124.00 list, still current-sale.
- **Identifiers:** MPN 3Z726AA#ABA (HP.com product #); UPC **195908664512 — VERIFIED** (DirectDial spec page "MFG PART 3Z726AA#ABA, UPC 0195908664512" + Caretek spec page "same UPC" + StockInTheChannel HP GTIN "(ABA) 195908664512" all agree).
- **Price/stock:** HP.com $124.00 (list); DirectDial $110.00, Backordered.
- **Flag:** 2021-era model, still current-sale on HP.com — but StockInTheChannel reports 0 distributor stock, so HP.com direct is effectively the only clean row; thin channel.

### 15. HP 710 Rechargeable Silent Mouse, Black — `hp-710-rechargeable-silent-mouse-black`
- **Category:** mice (compact ambidextrous, BT + 2.4GHz, USB-C rechargeable, silent clicks)
- **Variant pinned:** Black, 6E6F2AA#ABL (Silver is 6E6F1AA#ABL — OOS at HP.com; do not mix).
- **Why it qualifies:** Current HP rechargeable silent-click wireless mouse; HP.com $89.99.
- **Identifiers:** MPN 6E6F2AA#ABL; UPC PENDING — lead 196548822690 (Best Buy spec panel prints UPC 196548822690 for this exact Black listing; eBay GTIN 0196548822690 agrees but eBay is not a qualifying source — see "Corrections"). Conflict to re-check at add time: LT Online Store prints 196548822683 for 6E6F2AA (it prints the same code for 6E6F1AA too, so LT looks like a copy error, but flag it).
- **Price/stock:** HP.com $89.99 (6E6F2AA#ABL). Best Buy's fetched page is a stale Feb 2026 crawl ($31.99) — do not use; current Best Buy price not captured.
- **Flag:** Variant matrix (Black/Silver share the "710" name); Best Buy current price needs a fresh check at add time.

### 16. HyperX Cloud Alpha Wireless, Black-Red — `hyperx-cloud-alpha-wireless-black-red`
- **Category:** headphones (300-hour battery, DTS Headphone:X, dual-chamber drivers)
- **Variant pinned:** Black-Red, 4P5D4AA.
- **Why it qualifies:** Current HyperX wireless gaming headset; Best Buy and HP.com both carry it new at the same Black Friday price.
- **Identifiers:** MPN 4P5D4AA (HP.com product # + Best Buy model agree); UPC PENDING, no lead found (targeted search 2026-11-20; Best Buy spec panel in fetched text shows no UPC — spec-panel check at add time).
- **Price/stock:** Best Buy $108.99, InStock, sold by Best Buy, Add to cart (Black Friday Deal, comp. $199.99); HP.com $108.99, InStock (same promo).
- **Flag:** Promo price — $108.99 is 46% off the $199.99 list; 2022-era model but still current-sale at HP/Best Buy.

### 17. HyperX Alloy Rise (Full-size), Black — `hyperx-alloy-rise-black`
- **Category:** keyboards (full-size, hot-swappable, gasket mount, HyperX Red linear)
- **Variant pinned:** Black, US Layout, HyperX Red – Linear, wired, 7G7A3AA#ABA.
- **Why it qualifies:** Current HyperX full-size hot-swappable keyboard; HyperX direct, HP.com and Best Buy all carry it new at $199.99.
- **Identifiers:** MPN 7G7A3AA#ABA (HP.com product # + Best Buy model + Amazon item model agree); UPC PENDING, no lead found (targeted search 2026-11-20; no retailer spec page printed one).
- **Price/stock:** HyperX direct $199.99, Available (Black/Red linear variant); HP.com $199.99; Best Buy $199.99, InStock (SKU 11006257 — use this one; the other Best Buy SKU 13226682 is sold/shipped by Adorama, not Best Buy).
- **Flag:** Distinct from in-catalog Alloy Rise 75 (7G7A4AA#ABA) — full-size vs 75%; keep separate.

### 18. Corsair VOID Wireless v2, Carbon — `corsair-void-wireless-v2-carbon`
- **Category:** headphones (2.4GHz + Bluetooth, Dolby Atmos, 70h battery)
- **Variant pinned:** Carbon (Black), CA-9011379-WW (White is CA-9011380-WW — do not mix).
- **Why it qualifies:** Current Corsair wireless gaming headset (2025 model); Best Buy $69.99 InStock, sold by Best Buy.
- **Identifiers:** MPN CA-9011379-WW (Corsair.com SKU + Best Buy model agree); UPC PENDING, no lead found (targeted search 2026-11-20; Best Buy spec panel in fetched text shows no UPC).
- **Price/stock:** Best Buy $69.99, InStock, sold by Best Buy, Add to cart (Black Friday Deal, comp. $129.99); Corsair.com $129.99, InStock.
- **Flag:** Promo price — $69.99 is $60 off list; 2025 model, current.

### 19. Corsair DARKSTAR Wireless RGB MMO Gaming Mouse, Black — `corsair-darkstar-wireless-black`
- **Category:** mice (MARKSMAN 26K sensor, 15 programmable buttons, 6-button thumb cluster, Slipstream + BT)
- **Variant pinned:** Black, CH-931A011-NA (EU is CH-931A011-EU — do not use).
- **Why it qualifies:** Current Corsair MMO wireless gaming mouse; Corsair.com $149.99 list.
- **Identifiers:** MPN CH-931A011-NA (Corsair.com SKU + Newegg part # agree); UPC PENDING — lead 840006649489 (BuildCores + Desertcart + Snapklik + DealTargets all print it, but all are weak aggregator/marketplace feeds, no retailer spec page seen — verify at add time).
- **Price/stock:** Corsair.com $149.99 (category list, crawled 2026-11-18; stock not confirmed on the fetched page — verify at add time); Newegg $129.99–$149.99 (seller not confirmed).
- **Flag:** 2023-era model; a Revival Series SKU (CH-931A011-NA-RV, $69.99) exists and is OutOfStock — do not confuse with the main SKU; current-stock confirmation is the main gap on this one.

### 20. Corsair SABRE v2 PRO Wireless FPS Gaming Mouse, White — `corsair-sabre-v2-pro-wireless-white`
- **Category:** mice (8K polling, lightweight FPS shape)
- **Variant pinned:** White, CH-931G101-WW.
- **Why it qualifies:** Current Corsair wireless FPS gaming mouse; Best Buy $99.99, sold by Best Buy.
- **Identifiers:** MPN CH-931G101-WW (Best Buy model); UPC PENDING, no lead found (no targeted UPC search run in this round — check at add time).
- **Price/stock:** Best Buy $99.99, sold by Best Buy (comp. value $149.99 — Black Friday promo).
- **Flag:** Previous generation — the SABRE v3 PRO PureVector line launched 2026-10-20 ($179.99+); v2 Pro is still sold new at Best Buy but note the supersession risk at add time.

### 21. Keychron K10 Max QMK Wireless Mechanical Keyboard, Black, Super Red — `keychron-k10-max-black-red`
- **Category:** keyboards (100% full-size, QMK/VIA, 2.4GHz + BT + wired, hot-swappable)
- **Variant pinned:** Fully Assembled, Black, RGB Backlight, Keychron Super Red (K10M-H1). (Brown = K10M-H3, Banana = K10M-H4 — do not mix; EANs differ per switch.)
- **Why it qualifies:** Current Keychron full-size QMK/VIA wireless keyboard; Keychron direct $119.99.
- **Identifiers:** MPN K10M-H1; EAN **4895248884569 — VERIFIED** (Micro Center spec page "Mfr Part# K10M-H1, UPC 4895248884569" + OX.ee "EAN 4895248884569 for K10M-H1" + SquareDeals table "KYCN-K10M-H1 → 4895248884569" + Albagame "EAN 4895248884569 for K10M-H1" all agree). 13-digit code → EAN column per the Keychron catalog precedent; Micro Center labels it "UPC".
- **Price/stock:** Keychron direct $119.99; Micro Center lists the model (SKU 740191) but its price was not captured in the page fetch — flag. (Walmart $119.99 listing is the Banana variant — not usable for this Red pin.)
- **Flag:** Switch-label discrepancy — Micro Center calls the switch "Keychron K Pro Red Linear" while Keychron.com/Dynacore say Super Red; pinned as Super Red per the brand. No promo seen.

### 22. Keychron Q2 Max QMK/VIA Wireless Custom Mechanical Keyboard, Carbon Black, Jupiter Brown — `keychron-q2-max-carbon-black-brown`
- **Category:** keyboards (65%, full aluminum, knob, QMK/VIA, 2.4GHz + BT + wired)
- **Variant pinned:** Fully Assembled Knob, Carbon Black, Gateron Jupiter Brown (Q2M-M3) — the variant showing Available at Keychron direct (Red Q2M-M1 and Banana Q2M-P4 are the other switches; do not mix).
- **Why it qualifies:** Current Keychron 65% QMK/VIA wireless keyboard; Keychron direct $203.99 Available.
- **Identifiers:** MPN Q2M-M3 (Keychron mirror + PBTech Mfr Part No agree); EAN PENDING, no lead (the only EAN found, 4895248864059 via Snapklik, belongs to the Red Q2M-M1 variant — deliberately not attached).
- **Price/stock:** Keychron direct $203.99, Available (list $229.99, MAX20 $20-off auto-applied at checkout — promo price); no second US retailer-direct row found in this round (keeb-finder cites "$205 at MK" — unverified, not used as evidence).
- **Flag:** Single-retailer row (Keychron direct only) + promo pricing; find a second retailer at add time. Fills the 65% gap in the Q Max line (Q1/Q3/Q5/Q6 Max already in catalog).

### 23. Bose Bass Module 700, Black — `bose-bass-module-700-black`
- **Category:** speakers (wireless bass module for Bose Smart soundbars; categorized under speakers — the catalog has no subwoofers category)
- **Variant pinned:** Black.
- **Why it qualifies:** Bose's current flagship wireless bass module; Best Buy $899.00 InStock, sold by Best Buy; Bose direct list also $899.
- **Identifiers:** MPN 809108-1100 (World Wide Stereo spec page; Amazon item details agree); UPC PENDING — lead 017817789592 (World Wide Stereo spec page "Model: 809108-1100 | UPC: 017817789592"; Amazon item details + eBay agree but are not qualifying sources — see "Corrections").
- **Price/stock:** Best Buy $899.00, sold by Best Buy, InStock (JSON-LD, crawled 2026-11-19/20). Bose direct list is also $899.
- **Flag:** AGE — launched 2018, but still Bose's current flagship bass module with no successor; sold new at Best Buy/Bose. eBay also shows a second GTIN 0017817798136 attached to the same MPN — unresolved, do not attach; re-check at add time. No Bose bass module of any kind exists in the catalog, so no collision — but the MPN/UPC pairing rests on a single retailer spec page; re-confirm at add time.

### 24. Microsoft Surface Slim Pen 2, Matte Black — `microsoft-surface-slim-pen-2-matte-black`
- **Category:** accessories (stylus)
- **Variant pinned:** Matte Black, retail (not commercial).
- **Why it qualifies:** Microsoft's current rechargeable stylus for Surface devices; Best Buy $109.99 Black Friday, sold by Best Buy.
- **Identifiers:** MPN 8WV-00001 (Best Buy model; NFM spec page "Model: 8WV00001"); UPC PENDING — lead 889842778717 (NFM retailer spec page for 8WV00001; eBay listings for 8WV-00001 agree but eBay is not a qualifying source — see "Corrections").
- **Price/stock:** Best Buy $109.99 (Black Friday, comp $129.99) / list $129.99; Adorama lists the commercial twin at $124.99 — do not use as the price for this SKU.
- **Flag:** PROMO price ($109.99 vs $129.99 list). Twin-SKU trap: commercial channel MPN 8WX-00001 has a DIFFERENT UPC 889842778861 (CompSource + Adorama + Howard agree) — never mix the two. Age: 2021 launch, but still the current pen, bundled with the Surface Pro 12" keyboard (2025).

### 25. Microsoft Surface Laptop, 15-inch (8th Edition), Platinum — `microsoft-surface-laptop-15-8th-edition-platinum`
- **Category:** laptops
- **Variant pinned:** Snapdragon X2 Elite 12-core, 16GB/1TB, Platinum.
- **Why it qualifies:** Current Microsoft 15" laptop (8th Edition, Snapdragon X2 Elite); Abt $1,899.99, Staples $2,161.99.
- **Identifiers:** MPN EP2-60128 (Abt, Target, Best Buy SKU 12740531 all agree); UPC PENDING — lead 196388728855 (Target spec page: Model name EP2-60128, UPC 196388728855; single retailer-spec source — re-confirm via Best Buy spec panel at add time).
- **Price/stock:** Abt $1,899.99, comp $2,199.99 (manufacturer rebate ends 12/06/2026); Staples $2,161.99; Microsoft Store business page lists 15" from $2,099.99.
- **Flag:** PROMO/rebate price at Abt. Size sibling of in-catalog 13.8" (EP2-59028) — same precedent as Watch8 40/44mm, MacBook Air 13/15, iPad Air 11/13 in the catalog.

### 26. Lenovo Legion Go 2, 32GB/1TB, Eclipse Black — `lenovo-legion-go-2-32gb-1tb-eclipse-black`
- **Category:** handheld-consoles
- **Variant pinned:** Windows 11, Ryzen Z2 Extreme, 32GB, 1TB, Eclipse Black.
- **Why it qualifies:** Current Lenovo Windows handheld gaming device; Best Buy $1,999.99 InStock, sold by Best Buy.
- **Identifiers:** MPN 83N0000BUS (Best Buy model, SKU 6643145; eBay agrees); UPC PENDING — lead 0199271412718 (eBay-only, conflicted). Multiple eBay listings give 0199271412718 for 83N0000BUS, but one eBay listing for a "2TB NEW" unit also claiming MPN 83N0000BUS gives 199271412701. No retailer spec page found. Verify via Best Buy spec panel at add time; do not carry either value as verified.
- **Price/stock:** Best Buy $1,999.99, sold by Best Buy, in stock (Add to cart). Entry 16GB/1TB config is a different SKU (Best Buy $1,349.99, UPC 199271412763 per Slickdeals) — not this entry.
- **Flag:** Price has moved a lot (launch $1,350 for the 32GB config per XDA/PCGuide; now $1,999.99) — record as-of 2026-11-20, re-check at add time. Distinct from in-catalog Legion Go S SteamOS (83L30030US) — different device/OS.

### 27. Alienware 16 Area-51, Liquid Teal — `alienware-16-area-51-rtx-5070-ti-2tb-liquid-teal`
- **Category:** laptops
- **Variant pinned:** Ultra 9 275HX, 32GB, RTX 5070 Ti, 2TB, Liquid Teal, 16" 240Hz QHD.
- **Why it qualifies:** Current Alienware flagship gaming laptop (2025 Area-51 line); Best Buy $4,174.99, sold by Best Buy.
- **Identifiers:** MPN LAA16250-9499BLU-PUS (Best Buy model, SKU 6632697); UPC PENDING — lead 884116651499 (eBay-only). Single eBay listing gives UPC 884116651499 for MPN LAA16250-9499BL (note: without the Best Buy "-PUS" suffix). No retailer spec page found. Verify at add time.
- **Price/stock:** Best Buy $4,174.99 (sold by Best Buy per listing; "New $3,699.99–$4,174.99" range shown across crawls). Dell direct from $3,099 for the line (different configs).
- **Flag:** Laptop config matrix — the AA16250 chassis ships in many configs (RTX 5070/5070 Ti/5080, 1TB/2TB/4TB); pin the exact config above. Price is high vs Dell's own $3,569.99 for the 5070 Ti/32GB/1TB config — the Best Buy unit is 2TB.

### 28. Alienware AW2725QF, Black — `alienware-aw2725qf-black`
- **Category:** monitors
- **Variant pinned:** 27" 4K IPS dual-resolution (4K 180Hz / FHD 360Hz), Black.
- **Why it qualifies:** Current Alienware 27" dual-mode gaming monitor; Best Buy $549.00.
- **Identifiers:** MPN AW2725QF (Best Buy model, SKU 12688409; Dell model); UPC PENDING — strong lead 884116469711. PB Tech (AU retailer), TopMarket, eBay UK and AlmaCommerce all agree on 884116469711; EAN 5397184821787 (Icecat). No US retailer spec page seen — verify via Best Buy spec panel at add time.
- **Price/stock:** Best Buy $549.00, shipping available (pickup unavailable in crawl); Newegg $577 (via Klarna). Seed file noted a $499.99 row for this model — price has moved; promo-sensitive.
- **Flag:** Distinct from in-catalog AW2725Q (QD-OLED 240Hz 4K, $899.99, MPN 2MHGG) — different panel/tech/price tier. Do not merge.

### 29. Meta Oakley Meta HSTN, Clear Lenses, Black — `meta-oakley-meta-hstn-clear-black`
- **Category:** wearables (AI smart glasses)
- **Variant pinned:** Clear Lenses, Black frame.
- **Why it qualifies:** Current Meta/Oakley AI smart glasses; Best Buy $399.00 list, sold by Best Buy.
- **Identifiers:** MPN 0OW8002 800207 (Best Buy model, SKU 6636602); UPC PENDING — no lead found. Targeted search 2026-11-20 returned no UPC for this model code. Best Buy spec-panel check at add time.
- **Price/stock:** Best Buy $399.00 list; one crawl showed $349.00 — treat $349 as promo/unconfirmed, carry $399.00 as list. Sold by Best Buy.
- **Flag:** PROMO uncertainty ($349 vs $399 across crawls). Large variant matrix — 10+ lens/frame combos at Best Buy (Transitions $479, Prizm $399–$449, Vanguard is a separate model at $579); pin only the Clear/Black 800207 entry. Distinct from in-catalog Ray-Ban Meta Gen 2 Wayfarer (different frame line, 8-hr battery, 3K video).

### 30. Meta Quest 3S, 256GB, White — `meta-quest-3s-256gb`
- **Category:** vr
- **Variant pinned:** 256GB, White.
- **Why it qualifies:** Current Meta VR headset (256GB config); Best Buy and B&H both carry it new at $449.99.
- **Identifiers:** MPN SK-1000927-01 (Best Buy model, SKU 6665817; Adorama MFR + B&H MFR agree); UPC PENDING — lead 815820025832 (conflicted). eBay (×2) + Ubuy (×2) give 815820025832; one Walmart-clearance post gives 815820025833. No retailer spec page prints a UPC. Verify via Best Buy spec panel at add time; do not carry either as verified.
- **Price/stock:** Best Buy $449.99, sold by Best Buy, Add to cart; B&H $449.99 In Stock; Adorama $449.99, temporarily on backorder.
- **Flag:** Storage config of in-catalog Quest 3S 128GB (SK-1000926-01, UPC 815820025825) — same precedent as other storage/size siblings in the catalog, but flag for the parent's call. Best Buy listing title includes a GOLF+ game bundle — same hardware SKU, promo bundle, not a separate model.

### 31. Samsung Galaxy Watch9, 44mm, Bluetooth, Graphite — `samsung-galaxy-watch9-44mm-bt-graphite`
- **Category:** wearables
- **Variant pinned:** 44mm, Bluetooth, Graphite.
- **Why it qualifies:** Current Samsung smartwatch (2026); Best Buy $409.99, sold by Best Buy.
- **Identifiers:** MPN SM-L350NZKAXAA (Best Buy model, SKU 6684212; Samsung MSRP list agrees); UPC **198957312281 — VERIFIED** (Samsung's own official US MSRP price lists, July 2026 AND September 2026 editions, images.samsung.com: "SM-L350NZKAXAA — Galaxy Watch9 44mm BT - Graphite — $409.99 — UPC 198957312281"; Provartech listing agrees, 0198957312281).
- **Price/stock:** Best Buy $409.99, sold by Best Buy; T-Mobile LTE version is a different SKU.
- **Flag:** None. Cleanest verified entry in the batch. Size sibling of in-catalog Watch9 40mm (SM-L340NZKAXAA, pending). Note: an initial guess SM-L330 was wrong — that is the Watch8 44mm; Watch9 44mm is SM-L350.

### 32. Google TV Streamer 4K, Porcelain — `google-tv-streamer-4k-porcelain`
- **Category:** streaming-devices (new category for Google; catalog already has Apple TV 4K 4th gen)
- **Variant pinned:** Porcelain, 32GB.
- **Why it qualifies:** Current Google 4K streaming device; Best Buy $149.99, sold by Best Buy.
- **Identifiers:** MPN GA05662-US (Best Buy model, SKU 6586840); UPC PENDING — lead 810037291315 (Ferguson retailer spec page: Manufacturer Part # GA05662-US, UPC 810037291315; eBay, HiBid, Mozeve all agree but are not qualifying sources — see "Corrections").
- **Price/stock:** Best Buy $149.99, sold by Best Buy, Add to cart. Hazel is a separate SKU (GA05802-US) — not this entry.
- **Flag:** 2024 launch, still current with no successor. Price has been $99.99 on promo before (Dec 2025 shelf photo) — current $149.99 is list; watch for Black Friday movement.

### 33. Apple AirPods 4 with Active Noise Cancellation, White — `apple-airpods-4-anc-white`
- **Category:** earbuds
- **Variant pinned:** White, with ANC (USB-C case).
- **Why it qualifies:** Current Apple mid-tier earbuds (2024); Adorama $169.00, Apple direct $179.00 list.
- **Identifiers:** MPN MXP93LL/A (Adorama MFR; Costco item 1611943 + eBay agree); UPC PENDING — lead 195949689604 (Adorama spec page "UPC Code 195949689604" for MXP93LL/A; eBay listings agree but eBay is not a qualifying source — see "Corrections").
- **Price/stock:** Adorama $169.00 (was $179.00); Apple direct list $179.00; Costco $119.97 (Sept 2026 shelf photo — member price, do not use as primary row).
- **Flag:** PROMO at Adorama ($169 vs $179 list). Distinct from in-catalog AirPods 5 (MKFW4LL/A) and AirPods Pro 3 — AirPods 4 ANC is the 2024 mid-tier, still sold new.

### 34. Nintendo Switch 2 All-in-One Carrying Case, Black — `nintendo-switch-2-all-in-one-carrying-case-black`
- **Category:** accessories (carrying cases)
- **Variant pinned:** Black, holds console + dock + Pro Controller + cables + 6 game cards.
- **Why it qualifies:** Current Nintendo first-party carrying case; Best Buy $84.99.
- **Identifiers:** MPN BEEADECAA (Best Buy model, SKU 6625990; GameStop Model Number agrees); UPC PENDING — lead 045496886042 (GameStop spec page: UPC 00045496886042, Model Number BEEADECAA; single retailer-spec source — re-confirm via Best Buy spec panel at add time).
- **Price/stock:** Best Buy $84.99. GameStop also lists it (price not captured in crawl).
- **Flag:** Distinct from in-catalog Switch 2 Carrying Case & Screen Protector (BEEAPSSAA, UPC 045496886073, $39.99, currently sold out/restock-wait) — larger case that holds the dock; do not merge.

### 35. Sony SRS-XB100, Black — `sony-srs-xb100-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN SRSXB100/B (Best Buy model SRSXB100/B; bundle SKUs SRSXB100B-CR/-KNHC are different listings — do not use their prices).
- **Why it qualifies:** Current Sony compact portable speaker (IP67, 16h battery); Best Buy/Abt/Sweetwater all carry it new.
- **Identifiers:** MPN SRSXB100/B (Best Buy, B&H, Abt agree); UPC **027242926059 — VERIFIED** (B&H spec page + Abt "Model # SRSXB100/B, UPC # 027242926059" + Micro Center agree).
- **Price/stock:** Best Buy $63.00; Abt $63.00 InStock; Sweetwater $47.70 (via Klarna, 2026-11-18). Older Best Buy crawl showed $49.99 — treat $63.00 as current.
- **Flag:** Ignore Target refurbished listing UPC 732388845965 (refurb listing code, not the manufacturer UPC).

### 36. Sony INZONE M10S, Black — `sony-inzone-m10s-black`
- **Category:** monitors
- **Variant pinned:** 27" OLED QHD 480Hz, MPN SDM27Q10S (Best Buy model SDM27Q10S).
- **Why it qualifies:** Current Sony 27" OLED gaming monitor (480Hz); Best Buy and Sony direct both carry it new.
- **Identifiers:** MPN SDM27Q10S (Best Buy, Sony); UPC PENDING — lead 027242930360 (B&H spec page only; CamelCamelCamel and Desertcart agree but are not qualifying sources — see "Corrections"). Snapklik renewed listing shows 724129293920 — ignore, renewed.
- **Price/stock:** Best Buy $1,098.00 (crawl 5 days ago); Sony direct sale $949.99 (orig $1,199.99, stale crawl); PlayStation Direct $749.99 promo until Nov 23, 2026 (per tech-insider.org, read Nov 12).
- **Flag:** Promo price + wide price spread — re-verify at add time. M10S II (540Hz) now exists; M10S is previous-gen but still sold new. Ignore a Best Buy "$237.99 clearance / Unavailable" artifact on the same page — not the new price.

### 37. Logitech Brio 500, Graphite — `logitech-brio-500-graphite`
- **Category:** webcams
- **Variant pinned:** Graphite, MPN 960-001493 (Best Buy model 960-001493, SKU 6520150).
- **Why it qualifies:** Current Logitech 1080p business webcam with auto-framing; Best Buy $99.99 Black Friday, sold by Best Buy.
- **Identifiers:** MPN 960-001493; UPC **097855180452 — VERIFIED** (Micro Center "Mfr Part# 960-001493, UPC 097855180452" + Govets agree; BarcodesInc corroborates).
- **Price/stock:** Best Buy $129.99 list, $99.99 Black Friday, sold by Best Buy. (Rose 960-001432 and Off-White 960-001427 are other colors — do not mix.)
- **Flag:** Promo price ($99.99).

### 38. Logitech G305 LIGHTSPEED, Black — `logitech-g305-lightspeed-black`
- **Category:** mice
- **Variant pinned:** Black, MPN 910-005280 (Best Buy model 910-005280, SKU 6214343).
- **Why it qualifies:** Long-running Logitech budget wireless gaming mouse, still sold new at Best Buy/Logitech direct — mainstream budget staple, not clearance.
- **Identifiers:** MPN 910-005280; UPC **097855137692 — VERIFIED** (Newegg "Model 910-005280, UPC 097855137692" + Zoro + Tech-America + Electronic Express agree). Compsource lists a conflicting 695977037243 — single outlier, ignore.
- **Price/stock:** Best Buy $29.49, $26.99 Black Friday deal, sold by Best Buy (comp $49.99).
- **Flag:** Promo price; 2018-era model but still sold new.

### 39. JBL PartyBox Club 120, Black — `jbl-partybox-club-120-black`
- **Category:** speakers
- **Variant pinned:** Black, MPN JBLPBCLUB120AM (Best Buy model JBLPBCLUB120AM, SKU 12146571). White is JBLPBCLUB120SWAM — do not mix.
- **Why it qualifies:** Current JBL party speaker (160W, IPX4, AI Sound Boost); Best Buy $279.95 sold by Best Buy.
- **Identifiers:** MPN JBLPBCLUB120AM; UPC **050036399517 — VERIFIED** (Abt "Model # JBLPBCLUB120AM, UPC # 050036399517" + Zoro + Electronic Express + Reverb agree).
- **Price/stock:** Best Buy $279.95 (comp $449.95, Black Friday promo, InStock per JSON-LD).
- **Flag:** Promo price. Abt page now says "no longer available" and Zoro marks it "Discontinued" — Best Buy is the live new row; re-verify at add time.

### 40. JBL Live 670NC, Black — `jbl-live-670nc-black`
- **Category:** headphones
- **Variant pinned:** Black, MPN JBLLIVE670NCBLKAM (Best Buy model JBLLIVE670NCBLKAM, SKU 12146538).
- **Why it qualifies:** Current JBL adaptive noise-cancelling over-ear (65h battery); Best Buy $129.95 InStock, sold by Best Buy.
- **Identifiers:** MPN JBLLIVE670NCBLKAM; UPC **050036397599 — VERIFIED** (Abt "Model # JBLLIVE670NCBLKAM, UPC # 050036397599" + NFM + Erikson Consumer agree).
- **Price/stock:** Best Buy $129.95 InStock.
- **Flag:** One Amazon listing shows UPC 703670638084 for a "JBL LIVE670NCBLK" (no AM suffix) listing — do not use; 050036397599 is the AM-variant code.

### 41. JBL Vibe Buds 2, Black — `jbl-vibe-buds-2-black`
- **Category:** earbuds
- **Variant pinned:** Black, MPN JBLVBUDS2BLKAM (Best Buy model JBLVBUDS2BLKAM, SKU 6611537).
- **Why it qualifies:** Current JBL true-wireless earbuds (Smart Ambient, 40h total); Best Buy and JBL direct both carry them new.
- **Identifiers:** MPN JBLVBUDS2BLKAM; UPC **050036405164 — VERIFIED** (Abt "Model # JBLVBUDS2BLKAM, UPC # 050036405164" + NFM + CPR Accessories agree).
- **Price/stock:** Best Buy $39.95 Black Friday (comp $64.95, sold by Best Buy, InStock); JBL direct $39.95 InStock.
- **Flag:** Promo price. Do not confuse with gen-1 Vibe Buds (JBLVBUDSBLKAM, UPC 050036391412) — Abt explicitly lists Vibe Buds 2 as the replacement model. Ignore Target refurb UPC 732388845767.

### 42. Razer Viper V3 Pro, Black — `razer-viper-v3-pro-black`
- **Category:** mice
- **Variant pinned:** Black, MPN RZ01-05120100-R3U1 (Best Buy model RZ01-05120100-R3U1, SKU 6576242). Sentinels (RZ01-05120400) and Faker (RZ01-05120500) editions are different MPNs — do not mix.
- **Why it qualifies:** Current Razer flagship esports wireless mouse (8K polling, 54g); Best Buy $99.99 Black Friday, Add to cart.
- **Identifiers:** MPN RZ01-05120100-R3U1; UPC PENDING — strong lead 840272913888 (XcelSource + Ubuy + eBay agree, but no Best Buy/B&H/Abt spec page seen yet — verify at add time via Best Buy spec panel).
- **Price/stock:** Best Buy $99.99 Black Friday (comp $159.99), Add to cart.
- **Flag:** Promo price; Snapklik renewed listing shows conflicting UPC 703670538209 — ignore (renewed).

### 43. Razer BlackWidow V4 75%, Black, Orange switches — `razer-blackwidow-v4-75-black`
- **Category:** keyboards
- **Variant pinned:** 75%, wired, Orange Tactile switches, Black, MPN RZ03-05000200-R3U1 (Best Buy model RZ03-05000200-R3U1, SKU 6554665).
- **Why it qualifies:** Current Razer 75% hot-swappable gaming keyboard; Best Buy $129.99, Razer direct $189.99 in stock.
- **Identifiers:** MPN RZ03-05000200-R3U1 (Razer official API confirms this MPN, $189.99, inStock); UPC PENDING — lead 840272909607 (B&H product page only; eBay + BarcodeIndex agree but are not qualifying sources — see "Corrections").
- **Price/stock:** Best Buy $129.99 (comp $199.99); Razer direct $189.99 in stock (stockLevel 20); B&H $129.99 Temporarily Out of Stock.
- **Flag:** White variant is RZ03-05001700-R3M1 — do not mix. B&H OOS; Best Buy/Razer are the live rows.

### 44. Razer Wolverine V3 Tournament Edition, Black (Xbox-licensed) — `razer-wolverine-v3-tournament-edition-black`
- **Category:** controllers
- **Variant pinned:** Xbox-licensed wired, Black, MPN RZ06-05210100-R3U1 (Best Buy model RZ06-05210100-R3U1, SKU 6594729).
- **Why it qualifies:** Current Razer Xbox-licensed tournament controller (Hall Effect sticks, 1000Hz polling); Best Buy $74.99.
- **Identifiers:** MPN RZ06-05210100-R3U1; UPC PENDING — conflicted, no usable lead: 840272903537 (eBay GTIN / Slickdeals / Ubuy) vs 8886419351467 (multiple eBay listings) vs 840272919774 (Snapklik). No retailer spec page seen; needs Best Buy spec-panel tiebreaker at add time.
- **Price/stock:** Best Buy $74.99; Walmart (sold by Walmart.com) $79.88; Staples $99.99.
- **Flag:** Variant-matrix risk — a separate PC-only "8K" Tournament Edition (RZ06-05550100-R3U1, $99.99 at Best Buy) shares the name; pin the Xbox version only. Distinct from in-catalog Wolverine V3 Pro.

### 45. Anker Soundcore Space Q45, Black — `anker-soundcore-space-q45-black`
- **Category:** headphones
- **Variant pinned:** Black, MPN A3040Z11 (Best Buy model A3040Z11, SKU 6514486).
- **Why it qualifies:** Current Anker flagship ANC over-ear (98% noise reduction, 65h battery); Best Buy $149.99.
- **Identifiers:** MPN A3040Z11; UPC PENDING — lead 194644105310 (Abt spec page only; eBay UPC 0194644105310 agrees but is not a qualifying source — see "Corrections").
- **Price/stock:** Best Buy $149.99.
- **Flag:** Blue variant is listed under plain A3040 — pin Black A3040Z11 only.

### 46. Anker Soundcore Liberty 4 NC, Black — `anker-soundcore-liberty-4-nc-black`
- **Category:** earbuds
- **Variant pinned:** Black (Velvet Black), MPN A3947Z11 (Best Buy model A3947Z11, SKU 12486564).
- **Why it qualifies:** Current Anker ANC true-wireless earbuds (98.5% noise reduction, Hi-Res); Best Buy and soundcore direct both carry them new.
- **Identifiers:** MPN A3947Z11; UPC **194644126124 — VERIFIED** (Abt "Model # A3947Z11, UPC # 194644126124" + Micro Center "Mfr Part# A3947Z11, UPC 194644126124" + Newegg agree).
- **Price/stock:** Best Buy $79.99 InStock (comp $99.99, deal ends Nov 19, 2026); soundcore direct $79.99.
- **Flag:** Abt no longer carries it; bundle listings (A3947Z11 + 20W charger, $74.99) are separate — do not use bundle price. Newegg also lists a second UPC 194644132125 and Snapklik a renewed 194644150860 — unresolved, likely other colors; 194644126124 is the Abt/Micro Center code for A3947Z11.

### 47. Garmin Edge 840, Black (Standard, device only) — `garmin-edge-840-black`
- **Category:** cycling-computers
- **Variant pinned:** Standard (non-Solar), device only, MPN 010-02695-00 (Best Buy model 010-02695-00, SKU 6567545).
- **Why it qualifies:** Current Garmin GPS bike computer (touchscreen + buttons, solar optional); Best Buy $399.99 Add to cart.
- **Identifiers:** MPN 010-02695-00 (Garmin.com confirms Standard Edition part number); UPC **753759299927 — VERIFIED** (Abt "Model # 010-02695-00, UPC # 753759299927" + HLC + HeartRateMonitorsUSA table agree).
- **Price/stock:** Best Buy $399.99 (comp $449.99, Add to cart); Performance Bike $399.99; Crutchfield $449.99.
- **Flag:** Solar version is 010-02695-20 (UPC 753759300005) — pin non-Solar only.

### 48. Garmin Approach S70, 47mm, Black — `garmin-approach-s70-47mm-black`
- **Category:** wearables
- **Variant pinned:** 47mm, Black ceramic bezel / Black silicone band, MPN 010-02746-02 (Best Buy model 010-02746-02, SKU 6545137).
- **Why it qualifies:** Current Garmin premium golf GPS watch (AMOLED, 43,000+ courses); Best Buy/Abt/Cabela's all carry it new.
- **Identifiers:** MPN 010-02746-02; UPC **753759323622 — VERIFIED** (HeartRateMonitorsUSA table "MPN + UPC" + Abt "Model # 010-02746-02, UPC # 753759323622" agree).
- **Price/stock:** Best Buy $599.99 (comp $699.99); Abt $599.99; Cabela's $599.99.
- **Flag:** 42mm variants are different MPNs (010-02746-00 White, 010-02746-01 Powder Gray) — pin 47mm Black only. Ignore Best Buy 6ave bundle listings (010-02746-00-xx, $684.95+) — bundles, not the standalone row.

### 49. Garmin Descent Mk3, 43mm, Stainless Steel / Fog Gray — `garmin-descent-mk3-43mm-steel-fog-gray`
- **Category:** wearables
- **Variant pinned:** 43mm, Stainless Steel with Fog Gray silicone band, MPN 010-02753-03 (Best Buy SKU 10924918).
- **Why it qualifies:** Current Garmin dive computer/smartwatch (AMOLED, 200m, multi-gas); Best Buy and The GPS Store both carry it new.
- **Identifiers:** MPN 010-02753-03; UPC **753759333027 — VERIFIED** (HeartRateMonitorsUSA table "MPN + UPC + $1,199.99 MSRP" + Scuba.com "MFR 010-02753-03, UPC Code 753759333027" agree).
- **Price/stock:** Best Buy $899.99 (comp $1,199.99); The GPS Store $899.99 in stock; Garmin holiday promo Nov 13–Dec 28, 2026 ($899.99, was $1,199.99).
- **Flag:** Promo price (holiday promo). Distinct from seed Descent G1 and in-catalog Descent G2/X10; Mk3i (air-integrated, 010-02753-10) is a different model.

### 50. JBL Authentics 300, Black — `jbl-authentics-300-black`
- **Category:** speakers (smart-home speaker with Alexa/Google voice)
- **Variant pinned:** Black, MPN JBLAUTH300BLKAM (JBL.com official + Crutchfield MFR # agree).
- **Why it qualifies:** Current JBL portable smart home speaker (Wi-Fi/Bluetooth, 8h battery, retro design); JBL direct and Sweetwater both carry it new.
- **Identifiers:** MPN JBLAUTH300BLKAM; UPC PENDING — lead 050036396271 (Amazon item details only, four listings agree — Amazon-only, not verified; needs a retailer spec page at add time). Plausible by series (Authentics 500 is ...6264) but unproven.
- **Price/stock:** JBL direct $249.95 (was $449.95, Black Friday promo); Sweetwater $249.95 ($250 off through 12/5/2026); Crutchfield $499.95 (stale 70-day crawl); Best Buy $450 list.
- **Flag:** Promo price. Distinct from in-catalog Authentics 500 (entry 2) — 300 is the portable battery model, 500 is the flagship.

## Not carried (dropped / cut during research — do not re-add without new evidence)

### Seeds (from `data/candidates_batch5_450_seed.md`, re-check verdicts 2026-11-20)
- **Samsung Galaxy Tab A11 (base)** — DROP: no US retailer-direct row exists (Samsung US has no Tab A11 listing; Walmart deal expired Nov 15, now OutOfStock; only international-version sellers and refurbished). Distinct from in-catalog Tab A11+ (verified).
- **Garmin Descent G1 (non-Solar)** — DROP: new stock sold out / discontinued signals everywhere mainstream (GPS Nation "Sale Sold out", Bluewater "Currently Unavailable" + "DISCONTINUED", Adorama Special Order only). 2022-era; G2 already in catalog.
- **Apple Watch Ultra 3, Black Titanium / Black Alpine Loop Medium** — CUT, four reasons: (1) superseded — Ultra 4 already in catalog (pending); (2) clearance pricing — Best Buy $549 is $250 off list, matching 9to5Mac's "clearance pricing" framing (2026-11-06); (3) UPC conflict unresolved (Target 195950484991 vs Littlewoods UK EAN 195950484892); (4) Medium MPN unconfirmed on any retailer spec page (lead MF0X4LW/A from Slickdeals only).

### C group (ASUS/Dell/HP/HyperX/Corsair/Keychron)
- **Corsair K70 MAX RGB (CH-910961G-NA)** — Corsair.com marks it Discontinued; Best Buy "no longer available in new condition"; Revival Series OOS at $109.99. Fails the new-stock rule.
- **Dell S2725H** — Dell.com $169.99 OutOfStock; Best Buy new stock $135.99 Clearance/Unavailable. Fails the new-stock rule.
- **ASUS ROG Strix XG27ACS** — ASUS US $229 OutOfStock; only thin third-party/aggregator price signals (Newegg $283.99, seller unconfirmed). Held, not proposed; XG27ACDMS is the ASUS monitor pick instead.
- **Corsair NIGHTSABRE Wireless (CH-931B011-NA)** — Corsair.com $149.99 list, but no US retailer-direct price/stock row found in this round (only Amazon-fulfilled listings). Held in favor of Sabre v2 Pro White, which has a clean Best Buy direct row.

### D group (Samsung/Google/Apple/Nintendo + Bose/Microsoft/Lenovo/Alienware/Meta)
- **Samsung Galaxy Buds Core (SM-R410)** — DROPPED: not a US-market product. Every US listing is an international version: Woot "2025 International Model" $36.99, Walmart "Latin American Stock" $44, Best Buy Canada "International Version" sold by a third-party seller. No Samsung US / Best Buy US listing exists. Fails the US-market rule outright.
- **Lenovo ThinkPad X1 Carbon Gen 13 Aura Edition (21NS0163US / 21NS0166US)** — DROPPED: no retailer-direct row. All Best Buy listings are marketplace sellers (Beach Audio, IST Computers — resealed/upgraded units, warranty by seller not manufacturer). No clean Best Buy-direct or Lenovo-direct price confirmed in this round. Re-check Lenovo.com direct before any future batch.
- **Microsoft Surface Arc Mouse** — NOT re-proposed (seed file: 2017-era, age).
- **Meta Quest 3S white colorway** — NOT proposed as a separate entry (same model as in-catalog, different colorway). Note: the 256GB storage config (entry 30) IS proposed — storage sibling, different SKU.

### B group (Sony/Logitech/JBL/Razer/Anker/Garmin)
- **Sony HT-S2000** — Best Buy Clearance $121.99 (comp $499.99) + "no longer available in new condition" in older crawl. Clearance-only → fails rule.
- **Sony SRS-XG300** — Best Buy Clearance $69.99 (comp $349.99), Unavailable. Clearance-only → fails rule.
- **Razer Leviathan V2 Pro** — Best Buy "no longer available in new condition"; Razer direct OutOfStock ($499.99). No shippable new row → fails rule. (Leviathan V2 X is entry 4.)
- **Razer Kiyo Pro** — B&H "No Longer Available" / Discontinued; Best Buy "no longer available in new condition". Discontinued → fails rule. (Kiyo Pro Ultra 4K, RZ19-04420100-R3U1, $429.99 at Best Buy, was not pursued.)
- **Garmin Epix Pro (Gen 2) Standard 47mm, Slate Gray (010-02803-00)** — Best Buy shows $1,062.12, above the $899.99 list, seller unclear; Sapphire 47mm sibling is Best Buy clearance $599.99. Dropped on the suspicious above-MSRP row; Descent Mk3 replaces it as the Garmin premium pick.

### Synthesis probes (mine, 2026-11-20 — not carried; the 50 was already full without them)
- **Sony SRS-XG500** — B&H "No Longer Available" / Discontinued. Fails the new-stock rule.
- **Sony LinkBuds S (WF-LS900N/B)** — Audio46 "Discontinued", Black/White both Out of stock; Best Buy shows a clearance $31.99 artifact for White. 2022-era, winding down — do not carry.
- **Razer Kiyo Pro Ultra 4K (RZ19-04420100-R3U1)** — UPC 840272900376 is conflicted (same code tied to Kiyo Pro MPN RZ19-03640100-R3U1 in an eBay listing); price confusion ($299.99 Razer direct vs $399.99 vs $429.95); Kiyo V2 Pro successor announced Sep 24, 2026. Do not carry without a tiebreaker.
- **HP 930 Creator Wireless Mouse (1D0K9AA)** — 2021-era; no confirmed current US direct price/stock row and no UPC lead in this round. Do not carry.
- **Bose Solo Soundbar Series II (845194-2100)** — Bose.com $199.00 new, but 2021-era and the only identifier source is a manual site (EAN 0017817827355 → UPC 017817827355) — no retailer spec page. Held as an unnumbered reserve; needs a retailer spec page at add time.

## Corrections to brief-supplied markings (synthesis downgrades — all 10 were marked VERIFIED in a brief; each is PENDING under the two-source rule)

1. **HP 710 UPC 196548822690** (entry 15): brief said VERIFIED (Best Buy spec panel + eBay GTIN). eBay is not a qualifying source — only the Best Buy spec panel qualifies → PENDING, lead 196548822690. Conflict code 196548822683 (LT Online Store) noted in the entry.
2. **Bose Bass Module 700 UPC 017817789592** (entry 23): brief said VERIFIED (World Wide Stereo + Amazon + eBay). Amazon and eBay are not qualifying sources — only World Wide Stereo qualifies → PENDING, lead 017817789592. Conflicting GTIN 0017817798136 (eBay) noted in the entry.
3. **Microsoft Slim Pen 2 UPC 889842778717** (entry 24): brief said VERIFIED (NFM + eBay). eBay is not a qualifying source — only NFM qualifies → PENDING, lead 889842778717.
4. **Microsoft Surface Laptop 15" UPC 196388728855** (entry 25): brief said VERIFIED (Target spec page) but flagged it single-source itself — only Target qualifies → PENDING, lead 196388728855.
5. **Google TV Streamer 4K UPC 810037291315** (entry 32): brief said VERIFIED (Ferguson + eBay/HiBid/Mozeve). eBay, HiBid and Mozeve are not qualifying sources — only Ferguson qualifies → PENDING, lead 810037291315.
6. **Apple AirPods 4 ANC UPC 195949689604** (entry 33): brief said VERIFIED (Adorama + eBay). eBay is not a qualifying source — only Adorama qualifies → PENDING, lead 195949689604.
7. **Nintendo Switch 2 All-in-One Case UPC 045496886042** (entry 34): brief said VERIFIED (GameStop spec page) but flagged it single-source itself — only GameStop qualifies → PENDING, lead 045496886042.
8. **Sony INZONE M10S UPC 027242930360** (entry 36): brief said VERIFIED (B&H + CamelCamelCamel + Desertcart). CamelCamelCamel is Amazon-derived and Desertcart is an international marketplace — neither is a qualifying source → PENDING, lead 027242930360.
9. **Razer BlackWidow V4 75% UPC 840272909607** (entry 43): brief said VERIFIED (B&H + eBay + BarcodeIndex). eBay and BarcodeIndex are not qualifying sources — only the B&H product page qualifies → PENDING, lead 840272909607.
10. **Anker Soundcore Space Q45 UPC 194644105310** (entry 45): brief said VERIFIED (Abt + eBay). eBay is not a qualifying source — only Abt qualifies → PENDING, lead 194644105310.

Kept VERIFIED (two or more qualifying sources): Rear 9, Authentics 500, Vibe Flex 2, Leviathan V2 X, Stinger 2 Core, INZONE E9, RT-BE58U, XG27ACDMS, HP 975 keyboard, K10 Max EAN, Galaxy Watch9, XB100, Brio 500, G305, PartyBox Club 120, Live 670NC, Vibe Buds 2, Liberty 4 NC, Edge 840, Approach S70, Descent Mk3 (21).

## Membership check (so a later session can repeat it)
- Reference: `price_agent/catalog.py` EVAL_SET, 400 models — rebuilt as `/tmp/catalog_ref_400.tsv` by importing the module (2026-11-20), 400 rows; verified identifiers 173 / pending 227.
- Script: `/tmp/batch5_real50_check.py` — checks all 50 candidates by key, model name, MPN and UPC/EAN against all 400 rows, including intra-batch collisions. Run 2026-11-20: **0 key collisions, 0 MPN collisions, 0 UPC/EAN collisions, 0 intra-batch collisions**.
- Model-name hits adjudicated (2, both distinct siblings — do not merge):
  - HyperX Alloy Rise full-size (7G7A3AA#ABA) vs in-catalog Alloy Rise 75 (7G7A4AA#ABA) — different model (full-size vs 75%), different MPN.
  - Samsung Galaxy Watch9 44mm (SM-L350NZKAXAA) vs in-catalog Watch9 40mm (SM-L340NZKAXAA) — size sibling, different MPN; same precedent as Watch8 40/44mm, MacBook Air 13/15, iPad Air 11/13 in the catalog.
- Other siblings confirmed distinct (same family, different model — do not merge): Leviathan V2 (in catalog) vs V2 X (entry 4); Nommo V2 (in catalog) vs V2 Pro / V2 X (entries 5–6); Cloud Stinger 2 (in catalog) vs Stinger 2 Core PC (entry 7); Tab A11+ (in catalog, verified) vs Tab A11 base (not carried); Descent G2/X10 (in catalog) vs Descent G1 (not carried); Charge 6 (in catalog) vs Charge 5 (entry 9); Rear 8 (in catalog, verified, SA-RS8) vs Rear 9 (entry 1); Ultra 4 (in catalog, pending) vs Ultra 3 (not carried); Cloud Alpha (wired, in catalog) and Cloud Alpha 2 Wireless (in catalog) vs Cloud Alpha Wireless (entry 16); Alloy Rise 75 (in catalog) vs Alloy Rise full-size (entry 17); Surface Laptop 13.8" (in catalog, EP2-59028) vs 15" (entry 25); Legion Go S SteamOS (in catalog, 83L30030US) vs Legion Go 2 (entry 26); AW2725Q (in catalog, 2MHGG) vs AW2725QF (entry 28); Ray-Ban Meta Gen 2 Wayfarer (in catalog) vs Oakley Meta HSTN (entry 29); Quest 3S 128GB (in catalog, SK-1000926-01) vs 256GB (entry 30); Watch9 40mm (in catalog) vs 44mm (entry 31); AirPods 5 (in catalog, MKFW4LL/A) vs AirPods 4 ANC (entry 33); Switch 2 Carrying Case & Screen Protector (in catalog, UPC 045496886073) vs All-in-One Carrying Case (entry 34); Q1/Q3/Q5/Q6 Max (in catalog) vs Q2 Max (entry 22).
- Unresolved catalog-side discrepancy (not this batch's concern, do not "fix" here): in-catalog Leviathan V2 (`razer-leviathan-v2-black`) has empty identifiers; its variant string carries MPN RZ05-03920100-R3U1, while the seed file cited RZ05-04160100-R3U1. Flag for a later catalog-cleanup pass, not for batch 5.
- Note: the reference was built from the 2026-11-20 catalog (400 models). If the catalog changes before this draft is added, re-run the check against the new snapshot before adding anything.

## Needs the user's decision
1. **Approve the 50 as the batch-5 list (400 → 450)?** The list is a draft only; nothing is added until the user nods. Recommended: approve with the flags as written — the 10 downgraded identifiers and the promo-sensitive prices are all marked for the add-time re-verification.
2. **Routers as a new category (RT-BE58U, entry 10)?** First router in the set. Approve the category or cut the entry (the next-best ASUS pick was the ROG Strix XG27ACS, held for no US stock).
3. **Nommo V2 Pro (entry 5, HOLD)?** MPN is now confirmed (RZ05-04740100-R3U1) but the Best Buy new row is dead and Razer US stock is unconfirmed — add only if Razer US stock confirms at add time, or cut it from the 50 now.
4. **Dell U3425WE (entry 12, weakest)?** Dell.com price/stock not captured and Adorama's own page contradicts itself (snippets InStock $769 vs fetched JSON-LD "Discontinued"). Re-check Dell.com + Adorama before adding; if Dell.com has no shippable price, drop it.
5. **Quest 3S 256GB (entry 30, storage sibling)?** Same precedent as other storage/size siblings in the catalog, but flag for the parent's call.
