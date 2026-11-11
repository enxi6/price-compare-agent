# Batch 2 candidate list — catalog 250 → 300

- **Date:** 2026-11-11
- **Status:** LIST ONLY — candidate list for user approval. Nothing in this file has been added to the catalog. No repo file other than this one was modified; nothing committed or pushed.
- **How it was built:** 55 initial passes verified in 4 groups (Sony/Bose/JBL; Logitech/Razer/HyperX/Corsair; Apple/Samsung/Nintendo/Garmin/Keychron/Microsoft/Lenovo; Anker/Alienware/Dell/HP/Google/Amazon/Meta/ASUS) → 55 passes total. Synthesis trimmed 4 firm passes to fit exactly 50 (see "Cut at synthesis") and held 1 as Reserve (see bottom). Group reports saved at /tmp/batch2_groupA.md, /tmp/batch2_groupB.md, /tmp/batch2_groupC.md, /tmp/batch2_groupD.md.
- **Rules applied:** DECISIONS 001–005, 015, 016, 020, 021, 027, 057, 068. Mainstream/new products from brands already in the catalog; US-market versions only; seller-direct only (brand direct or retailer direct); no Amazon in any form, no third-party/marketplace sellers, no parallel imports, no international variants, no second-hand/refurbished/clearance-only/discontinued stock. Every candidate checked against all 250 catalog rows (key/model/MPN/UPC, including different colors/configs of the same model) — no duplicates (verified again at synthesis: 0 collisions).
- **Identifier honesty:** UPC/MPN is marked VERIFIED only when found on a retailer/manufacturer spec page or an official source. Otherwise PENDING, with the lead value (if any) and what was checked. Amazon-only values are never treated as verified. Suggested `key` values follow existing catalog slug conventions and are proposals only.
- **Identifier tally for the 50:** UPC VERIFIED 11 / PENDING 39. MPN present for 48; MPN pending for 2 (Switch 2 Camera, Switch 2 Dock Set). Note: the verified rate (22%) is lower than batch 1 (44%) — this round's remaining mainstream models are disproportionately brand-direct-only (Razer/HyperX/Corsair/Keychron publish MPNs but not UPCs on their pages; Best Buy spec pages need a live check). No rule change is proposed; identifiers stay pending per the standing rule.
- **New categories in this batch (precedent: handheld-consoles entered with batch 1):** accessories (Apple Pencils, Joy-Con 2 Charging Grip), cameras (Switch 2 Camera), docks (Switch 2 Dock Set).
- **Brands with zero passes this round:** Microsoft, Lenovo, Google, Meta — every idea for them either duplicates a catalog model or failed on availability. See rejections.

## Candidates (50)

### 1. Sony ULT FIELD 7, Black — `sony-ult-field-7-black`
- **Category:** speakers
- **Variant pinned:** Black, single colorway (MPN SRSULT70)
- **Why it qualifies:** Current ULT-series flagship portable speaker (IP67, 30h battery); sold new in the US.
- **Identifiers:** MPN SRSULT70; UPC **027242928961 — VERIFIED** (B&H spec + Adorama spec agree).
- **Price/stock:** Best Buy sold-by-Best-Buy $499.99; B&H $498.00.
- **Flag:** B&H crawls conflict (one "Temporarily Out of Stock", one "In Stock") — re-check at add time.

### 2. Sony ULT FIELD 3, Black — `sony-ult-field-3-black`
- **Category:** speakers
- **Variant pinned:** Black (SRSULT30/B; Off White and Forest Gray are separate variants — do not mix UPCs)
- **Why it qualifies:** Current-gen ULT portable speaker, launched Apr 9, 2025 (replaces SRS-XE300); Sony direct + retailers.
- **Identifiers:** MPN SRSULT30/B; UPC **027242931886 — VERIFIED** (Adorama spec lists Black 027242931886 / Off White 027242931893; Amazon corroborates Black).
- **Price/stock:** Sony direct $149.99 (list $209.99); Adorama $208.00 on backorder (expected 11/29/2026).

### 3. Sony ULT FIELD 5, Black — `sony-ult-field-5-black`
- **Category:** speakers
- **Variant pinned:** Black (SRSULT50/B)
- **Why it qualifies:** Current-gen ULT portable speaker, launched Apr 9, 2025 (replaces SRS-XG300); 25h battery, IP66/IP67.
- **Identifiers:** MPN SRSULT50/B; UPC **027242931947 — VERIFIED** (Adorama spec lists Black 027242931947 / Off White 027242931954; Amazon corroborates Off White).
- **Price/stock:** Adorama $348.00, on backorder (expected 11/23/2026); launch list ~$329.99.
- **Flag:** backorder at Adorama — confirm a live in-stock channel (Sony direct) at add time.

### 4. Sony INZONE Buds, Black — `sony-inzone-buds-black`
- **Category:** earbuds
- **Variant pinned:** Black (WFG700N/B; White WFG700N/W and Glass Purple WFG700N/V are separate)
- **Why it qualifies:** Sony's only true-wireless gaming earbuds (2.4 GHz dongle + LE Audio, ANC, 12h buds / 24h case); still sold new by Best Buy, no successor.
- **Identifiers:** MPN WFG700N/B; UPC PENDING — conflicting leads, do not pick one: 027242927957 (Canadian authorized dealer Simcoe, Sony-prefix) vs 196641115897 (manuals.plus, Amazon-ASIN-derived).
- **Price/stock:** Best Buy sold-by-Best-Buy $159.99 in stock (list $199.99).
- **Flag:** 2023 model; price has drifted down from $199.99 list.

### 5. Sony BRAVIA Theatre Bar 6, Black — `sony-bravia-theatre-bar-6-black`
- **Category:** soundbars
- **Variant pinned:** Black, 3.1.2ch with wireless subwoofer (HTB600 / HT-B600)
- **Why it qualifies:** Sony's current mid-tier Atmos soundbar (2025, successor to the HT-A3000 line); Best Buy sold-by-Best-Buy.
- **Identifiers:** MPN HTB600; UPC PENDING — no lead found.
- **Price/stock:** Best Buy sold-by-Best-Buy $549.99 in stock (comp. value $699.99, was $999.99). Note: Best Buy spells it "Theater"; Sony branding is "Theatre" — key spelling is a proposal only.

### 6. Bose QuietComfort Ultra Earbuds (2nd Gen), Black — `bose-qc-ultra-earbuds-2nd-gen-black`
- **Category:** earbuds
- **Variant pinned:** Black (896637-0010; White Smoke 896637-0020, Deep Plum -0030, Desert Gold -0040, Midnight Violet -0050 are separate)
- **Why it qualifies:** Bose flagship ANC earbuds, launched Sept 2025 (successor to 1st-gen Ultra Earbuds); Best Buy + Abt + Bose direct.
- **Identifiers:** MPN 896637-0010; UPC PENDING — lead 017817861120 (Amazon only, 3 listings, ASIN B0F7M3HPBD; Amazon-only values are never verified per standing rule). Do not confuse with Midnight Violet lead 017817861083.
- **Price/stock:** Best Buy sold-by-Best-Buy $299.00 in stock (SKU 6628900); Abt $299.
- **Flag:** one Best Buy Black listing (SKU 11871043) is sold by marketplace seller ThrillingAudio — pin the Best Buy-sold SKU.

### 7. Bose Smart Ultra Soundbar, Black — `bose-smart-ultra-soundbar-black`
- **Category:** soundbars
- **Variant pinned:** Black (882963-1100; Arctic White 882963-1200 separate)
- **Why it qualifies:** Bose Dolby Atmos flagship soundbar (5.1.2, ADAPTiQ, A.I. Dialogue Mode); Bose's own release says it replaced the Soundbar 900.
- **Identifiers:** MPN 882963-1100; UPC **017817848244 — VERIFIED** (Adorama spec: Black 017817848244 / White 017817848343).
- **Price/stock:** Best Buy sold-by-Best-Buy $679.00 in stock (SKU 6550611, list $999).
- **Flag:** previous flagship — Bose launched the Lifestyle Ultra Soundbar (May 2026, $1,099) as the new flagship; Smart Ultra is still sold new, but watch for clearance drift.

### 8. JBL Live Buds 3, Black — `jbl-live-buds-3-black`
- **Category:** earbuds
- **Variant pinned:** Black (JBLLIVEBUDS3BLKAM)
- **Why it qualifies:** JBL 2024 true-wireless ANC earbuds with smart touchscreen case; Best Buy + B&H.
- **Identifiers:** MPN JBLLIVEBUDS3BLKAM; UPC **050036401661 — VERIFIED** (B&H spec; Amazon.ca + Snapklik corroborate).
- **Price/stock:** Best Buy sold-by-Best-Buy $147.99 in stock (list $229.95); B&H $229.95 in stock.
- **Flag:** 2024 model at a deep discount ($147.99 vs $229.95 list) — promo/clearance drift watch at add time; refurbished units also circulate at Best Buy (Electronics Expo) — pin new Best Buy-sold SKU 6582669.

### 9. JBL Boombox 4, Black — `jbl-boombox-4-black`
- **Category:** speakers
- **Variant pinned:** Black (JBLBOOMBOX4BLKAM; Blue JBLBOOMBOX4BLUAM UPC 050036413251 and Squad JBLBOOMBOX4SQUADAM UPC 050036413237 are separate — do not mix)
- **Why it qualifies:** JBL's most powerful portable speaker, launched Sept 2025 (IP68, 34h battery, Auracast); JBL direct + B&H + Sweetwater.
- **Identifiers:** MPN JBLBOOMBOX4BLKAM; UPC **050036413220 — VERIFIED** (Amazon + eBay + Canadian dealer Clef de Sol agree; B&H Blue-variant spec confirms the per-color pattern).
- **Price/stock:** $549.95 list; Sweetwater Black $429.95 in stock; JBL.com $549.95 InStock; B&H Blue $549.95 in stock.

### 10. JBL PartyBox 330, Black — `jbl-partybox-330-black`
- **Category:** speakers
- **Variant pinned:** Black (JBLPB330BLKAM; White JBLPB330WHTAM separate)
- **Why it qualifies:** Brand-new 2026 PartyBox (announced May 12, 2026; presale June 7, 2026; 280W, 18h swappable battery, AI karaoke); successor to the in-catalog Stage 320, distinct model.
- **Identifiers:** MPN JBLPB330BLKAM; UPC **050036422154 — VERIFIED** (B&H spec; White UPC 050036422161 per Electronic Express).
- **Price/stock:** Best Buy sold-by-Best-Buy $629.95 in stock (SKU 6677352); B&H $629.95 in stock. Cleanest pass in the batch.

### 11. JBL PartyBox 130, Black — `jbl-partybox-130-black`
- **Category:** speakers
- **Variant pinned:** Black (JBLPB130BLKAM; White JBLPB130WHTAM separate)
- **Why it qualifies:** Brand-new compact 2026 PartyBox (announced May 12, 2026 alongside the 330; 200W, foldable handle, optical TV input); JBL direct + Best Buy.
- **Identifiers:** MPN JBLPB130BLKAM; UPC PENDING — no lead found.
- **Price/stock:** JBL.com $449.95 InStock; Best Buy White sold-by-Best-Buy $449.95 in stock.

### 12. JBL Tune Beam 2, Black — `jbl-tune-beam-2-black`
- **Category:** earbuds
- **Variant pinned:** Black (JBLTBEAM2BLKAM; US JBL.com page confirmed for White JBLTBEAM2WHTAM)
- **Why it qualifies:** JBL current mid-tier ANC earbuds (10mm drivers, 48h total, IP54); JBL US direct $109.95 in stock.
- **Identifiers:** MPN JBLTBEAM2BLKAM; UPC PENDING — no US lead (UK item JBLTBEAM2BLK carries EAN 1200130016479 — not a US UPC, do not use).
- **Price/stock:** JBL.com $109.95 InStock (White variant page).
- **Flag:** Black variant's live US page was not directly confirmed in this crawl — re-check at add time.

### 13. Logitech G915 X LIGHTSPEED TKL, Black, GL Tactile — `logitech-g915-x-tkl-tactile-black`
- **Category:** keyboards
- **Variant pinned:** TKL, GL Brown Tactile, Black
- **Why it qualifies:** Current Logitech low-profile wireless flagship in TKL form; distinct from the full-size G915 X already in the catalog.
- **Identifiers:** MPN 920-012715 (first guess 920-012681 was wrong); UPC **097855194794 — VERIFIED** (Logitech spec sheet via manuals.plus, corroborated by Amazon listing).
- **Price/stock:** Best Buy sold-by-Best-Buy $209.99 (was $249.99), SKU 6595187.

### 14. Logitech G Pro X Superlight 2c, Black — `logitech-g-pro-x-superlight-2c-black`
- **Category:** mice
- **Variant pinned:** Black, 51 g compact, HERO 2
- **Why it qualifies:** New (Sept 2025) compact Superlight; distinct from Superlight 2 and Superlight 2 DEX in the catalog.
- **Identifiers:** MPN 910-007518 (Adorama spec page confirms); UPC PENDING, lead 097855203632 (single non-US source, Tanotis — Adorama page shows no UPC).
- **Price/stock:** Adorama $149.99 (list $159.99), InStock, ships from manufacturer.
- **Flag:** White 910-007528 / Pink 910-007529 / Magenta 910-007546 (EU) are different SKUs; AU black pack 910-007533 — do not mix.

### 15. Logitech MX Master 3S Bluetooth Edition, Black — `logitech-mx-master-3s-bluetooth-black`
- **Category:** mice
- **Variant pinned:** Bluetooth Edition (no Logi Bolt receiver, no cable), Black
- **Why it qualifies:** Previous-gen but still sold new in the US; MX Master 4 is a different model in the catalog.
- **Identifiers:** MPN 910-007500 (Best Buy confirms, SKU 12028852, 390 reviews); UPC PENDING, lead 097855201812 (Amazon-only). Do NOT use standard-edition Black 910-006556 (current US availability unknown) or Graphite 910-006559 (EU pack).
- **Price/stock:** Best Buy $79.99 on sale Oct 2026 (list $99.99).
- **Flag:** Bluetooth-only; 1-year warranty per BuyDig (vs 2-year standard).

### 16. Razer DeathAdder V3 HyperSpeed, Black — `razer-deathadder-v3-hyperspeed-black`
- **Category:** mice
- **Variant pinned:** Black, wireless, Focus X 26K
- **Why it qualifies:** Current Razer mid-tier wireless esports mouse; distinct from V3 Pro / V4 Pro in the catalog.
- **Identifiers:** MPN RZ01-05140100-R3U1 (Best Buy + Canada Computers agree); UPC PENDING, no lead (guessed 840272911235 was NOT confirmed — do not use; the wired V3's UPC 840272903018 belongs to a different model).
- **Price/stock:** Best Buy $99.99, SKU 6580802, 4.7★/195 reviews.

### 17. Razer Kraken V4 (wireless), Black — `razer-kraken-v4-black`
- **Category:** headphones
- **Variant pinned:** wireless (2.4 GHz + Bluetooth + USB), Black
- **Why it qualifies:** Current Razer wireless headset; distinct from Kraken V4 Pro in the catalog. Do not confuse with Kraken V4 X (wired, RZ04-05180100), a different cheaper model.
- **Identifiers:** MPN RZ04-05170100-R3U1 (Best Buy confirms, SKU 6586394); UPC PENDING, no lead.
- **Price/stock:** Best Buy $179.99.

### 18. Razer Seiren V3 Mini, Black — `razer-seiren-v3-mini-black`
- **Category:** microphones
- **Variant pinned:** Black
- **Why it qualifies:** Current Razer compact USB mic; distinct from Seiren V3 Chroma in the catalog.
- **Identifiers:** MPN RZ19-05050100-R3U1 (Best Buy confirms, SKU 6573619); UPC PENDING, lead 840272911327 (Amazon/camelcamelcamel only).
- **Price/stock:** Best Buy $48.99 (list $59.99).

### 19. Razer Viper V3 HyperSpeed, Black — `razer-viper-v3-hyperspeed-black`
- **Category:** mice
- **Variant pinned:** Black, wireless, Focus Pro 30K, 280-hour AA battery
- **Why it qualifies:** Current Razer symmetric wireless mouse; distinct from Viper V4 Pro in the catalog.
- **Identifiers:** MPN RZ01-04910100-R3U1 (Best Buy + Canada Computers agree — guessed RZ01-05160100 was wrong); UPC PENDING, lead 840272911228 (Canex SKU field, single source).
- **Price/stock:** Best Buy $69.99 (list $99.99), SKU 6558751; Razer US $69.99 InStock.

### 20. HyperX Cloud Stinger 2 (wired), Black — `hyperx-cloud-stinger-2-black`
- **Category:** headphones
- **Variant pinned:** wired, Black
- **Why it qualifies:** Current HyperX budget wired headset; no Stinger model in the catalog.
- **Identifiers:** MPN 519T1AA (HP.com US confirms); UPC PENDING, lead 196188736906 (Clove UK barcode, single non-US source).
- **Price/stock:** HP.com US $49.99 InStock.
- **Flag:** Stinger 2 Wireless and Stinger 2 Core (PS/Xbox/PC) are different models.

### 21. HyperX Pulsefire Haste 2 Wireless, Black — `hyperx-pulsefire-haste-2-wireless-black`
- **Category:** mice
- **Variant pinned:** Black, 61 g, dual wireless
- **Why it qualifies:** Current HyperX wireless mouse; distinct from wired Haste 2 and Haste 2 Pro 4K in the catalog.
- **Identifiers:** MPN 6N0B0AA (HP.com US confirms; White is 6N0A9AA — do not mix); UPC PENDING, no lead.
- **Price/stock:** HP.com US $89.99 InStock; HyperX US $78.99 Black available.
- **Flag:** Haste 2 Core (8R2E6AA) is a different cheaper model.

### 22. HyperX QuadCast 2, Black — `hyperx-quadcast-2-black`
- **Category:** microphones
- **Variant pinned:** Black
- **Why it qualifies:** Current HyperX USB mic; distinct from QuadCast 2 S in the catalog.
- **Identifiers:** MPN 872V1AA (HP.com US confirms; Frost is AN1D9AA); UPC PENDING, no lead (eBay's 198122243846 is tied to odd MPN CL006A — not used).
- **Price/stock:** HP.com US $149.99 InStock; HyperX US $119.99 on sale (list $149.99).

### 23. Corsair Scimitar Elite Wireless SE, Gun Metal — `corsair-scimitar-elite-wireless-se-gun-metal`
- **Category:** mice
- **Variant pinned:** SE, Gun Metal, MARKSMAN S sensor
- **Why it qualifies:** Newer SE variant (33K DPI) with live US channels; distinct from the plain Scimitar Elite Wireless (rejected below).
- **Identifiers:** MPN CH-9314014-WW (Best Buy + Scan agree); UPC PENDING, lead 840440492276 (Scan UK GTIN, single source).
- **Price/stock:** Best Buy $139.99, SKU 6622828 (Deal of the Day); Corsair US $139.99 (SE Black & Yellow CH-9314415-WW InStock).
- **Flag:** SE White CH-9314011-WW is out of stock at Corsair — pin Gun Metal only.

### 24. Apple Pencil Pro, White — `apple-pencil-pro-white`
- **Category:** accessories
- **Variant pinned:** White, MX2D3AM/A
- **Why it qualifies:** Apple current stylus; Best Buy sold-by-Best-Buy $129.00 in stock (SKU 6535042, page opened and read); Apple $129.
- **Identifiers:** MPN MX2D3AM/A VERIFIED (Best Buy); UPC PENDING, lead 195949573040 (shopsavvy only — single source, not a retailer spec page).

### 25. Apple Pencil (USB-C), White — `apple-pencil-usb-c-white`
- **Category:** accessories
- **Variant pinned:** White, MUWA3AM/A
- **Why it qualifies:** Apple $79 in stock; Best Buy $69 early-Black-Friday sale.
- **Identifiers:** MPN MUWA3AM/A VERIFIED (Best Buy); UPC **195949133626 — VERIFIED** (Apple.com Part Number section, same pattern as batch-1 Magic Keyboard).

### 26. Apple Magic Keyboard with Touch ID (USB-C, no numeric keypad), White — `apple-magic-keyboard-touch-id-usb-c-white`
- **Category:** keyboards
- **Variant pinned:** US English, White keys, compact/TKL, Touch ID, no numpad. Distinct from plain Magic Keyboard USB-C (in catalog) and Touch ID + Numeric Keypad (in catalog).
- **Why it qualifies:** Apple $149; Best Buy sold-by-Best-Buy $149.99 (SKU 6276711; $89.99 Deal of the Day seen).
- **Identifiers:** MPN MXCK3LL/A VERIFIED (Best Buy + Insight Apple price list; brief's MKK63LL/A was the Lightning-era part — do not use); UPC PENDING, lead 195949634079 (JumpPlus Canada barcode field, single source).

### 27. Apple Watch SE 3 (GPS, 44mm), Starlight — `apple-watch-se3-44mm-gps-starlight`
- **Category:** wearables
- **Variant pinned:** 44mm GPS, Starlight aluminum, Sand Sport Band S/M, MJL34LW/A. Distinct size from the 40mm Midnight already in the catalog.
- **Why it qualifies:** Best Buy sold-by-Best-Buy $279.00 (SKU 6572722).
- **Identifiers:** MPN MJL34LW/A VERIFIED (Best Buy); UPC PENDING, no lead found.
- **Note:** Midnight 44mm GPS exists too (M/L = MEHQ4LW/A per price tracker); Starlight S/M pinned because its Best Buy-sold listing is cleanly in stock.

### 28. Apple Watch Series 12 (GPS, 46mm), Dark Bronze — `apple-watch-series-12-46mm-gps-dark-bronze`
- **Category:** wearables
- **Variant pinned:** 46mm GPS, Dark Bronze aluminum, Olive Sport Band S/M, MJEQ4LS/A. Distinct size from the 42mm Black already in the catalog (pending).
- **Why it qualifies:** Best Buy sold-by-Best-Buy $449.00 (SKU 6572740).
- **Identifiers:** MPN MJEQ4LS/A VERIFIED (Best Buy); UPC PENDING, no lead found.
- **Flag:** the Black 46mm M/L listing showed "Unavailable" in crawls — Dark Bronze/Olive pinned as the in-stock variant.

### 29. Samsung Galaxy Buds3 Pro, Silver — `samsung-galaxy-buds3-pro-silver`
- **Category:** earbuds
- **Variant pinned:** Silver, SM-R630NZAAXAR
- **Why it qualifies:** Samsung current flagship buds (Buds4 Pro is a different, newer model in the catalog). Best Buy sold-by-Best-Buy $149.99 holiday deal (list $249.99), in stock, SKU 6585614; Samsung US list $249.99.
- **Identifiers:** MPN SM-R630NZAAXAR VERIFIED (Best Buy); UPC PENDING, no lead — the only UPC found, 887276868141, belongs to the **White** variant (SM-R630NZWAXAR, CompSource) and must not be transferred to Silver.
- **Flag:** previous generation (Buds4 Pro exists) but still sold new at a major retailer; watch for clearance drift.

### 30. Nintendo Switch 2 Camera — `nintendo-switch-2-camera`
- **Category:** cameras
- **Variant pinned:** single colorway, black, USB-C, 1080p. Launched June 5, 2025.
- **Why it qualifies:** Nintendo US Store $54.99; also Target/Best Buy/Walmart.
- **Identifiers:** MPN PENDING (Nintendo store product code 123682 US / 10015282 EU; BEE-014 is a Joy-Con code, not the camera — do not use); UPC PENDING, lead 045496321468 (single source: Carrefour IT product doc).
- **Flag:** GameStop briefly sold it at $9.99 in July 2026 (82% off) — promo anomaly, not the standing price; Nintendo Store purchase may require NSO membership for GameChat use (not for purchase).

### 31. Nintendo Switch 2 Dock Set — `nintendo-switch-2-dock-set`
- **Category:** docks
- **Variant pinned:** dock + AC adapter + USB-C cable + Ultra High Speed HDMI cable. Launched June 5, 2025; was $109.99 at announcement, raised to $124.99.
- **Why it qualifies:** Nintendo US $124.99.
- **Identifiers:** MPN PENDING (dock unit itself is BEE-005; no retail MPN for the set found); UPC PENDING, no lead found.

### 32. Nintendo Joy-Con 2 Charging Grip — `nintendo-joy-con-2-charging-grip`
- **Category:** accessories
- **Variant pinned:** black charging grip, includes BEE-016 USB cable; Joy-Con 2 not included. Distinct from the non-charging grip bundled with the console.
- **Why it qualifies:** Target US $39.99 in stock (Oct 28, 2026 check); Nintendo $39.99.
- **Identifiers:** MPN BEE-010 VERIFIED (Nintendo support page); UPC PENDING, no lead found.

### 33. Garmin Forerunner 970, Black — `garmin-forerunner-970-black`
- **Category:** wearables
- **Variant pinned:** 47mm, Carbon Gray DLC Titanium, Black case, Black/Translucent Whitestone band. Garmin current flagship running watch (May 2025).
- **Why it qualifies:** Garmin/Best Buy $749.99 list, $649.99 sale; Best Buy SKU 6633098.
- **Identifiers:** MPN 010-02969-00 VERIFIED (Best Buy + Amazon product data; initial guess 010-03046 was wrong — do not use); UPC PENDING, lead 753759349929 (Amazon listing only).

### 34. Garmin Forerunner 570, 47mm, Slate Gray — `garmin-forerunner-570-47mm-slate-gray`
- **Category:** wearables
- **Variant pinned:** 47mm, Slate Gray aluminum, Translucent Black band. Distinct size from the 42mm Raspberry in the catalog.
- **Why it qualifies:** Best Buy $549.99 in stock (Indigo 010-02971-02 shown); Abt lists 47mm Slate Gray $549.99.
- **Identifiers:** MPN 010-02971-00 VERIFIED (Abt + retailer SKU tables); UPC PENDING, no lead found.

### 35. Garmin fēnix 8 AMOLED Sapphire, 47mm, Carbon Gray DLC Titanium — `garmin-fenix-8-47mm-carbon-gray`
- **Category:** wearables
- **Variant pinned:** 47mm AMOLED Sapphire, Carbon Gray DLC Titanium, 010-02904-20
- **Why it qualifies:** Best Buy sold-by-Best-Buy $999.99 in stock (SKU 6594317).
- **Identifiers:** MPN 010-02904-20 VERIFIED (Best Buy); UPC PENDING, no lead found.
- **Flag:** **previous generation** — fēnix 9 47mm is already in the catalog (pending). Other Best Buy SKUs for this model are marketplace sellers (HRM USA, 6ave, FrontRow) — pin the Best Buy-sold SKU 6594317 only.

### 36. Keychron Q1 HE, Carbon Black — `keychron-q1-he-carbon-black`
- **Category:** keyboards
- **Variant pinned:** Fully Assembled Knob, Carbon Black, Gateron Double-Rail Magnetic Nebula
- **Why it qualifies:** Keychron current QMK/VIA wireless custom keyboard; keychron.com US $239.99.
- **Identifiers:** MPN Q1H-M1 VERIFIED (multiple retailer listings); UPC PENDING (Keychron norm — no UPC found, consistent with all existing Keychron entries).

### 37. Keychron Q6 Max, Carbon Black — `keychron-q6-max-carbon-black`
- **Category:** keyboards
- **Variant pinned:** Fully Assembled Knob, Carbon Black, Gateron Jupiter Brown (Keychron's own guide recommends Brown as the default)
- **Why it qualifies:** keychron.com US $239.99; also Best Buy US SKU 6600176.
- **Identifiers:** MPN Q6M-M3 VERIFIED (Newegg, Best Buy US/CA); UPC PENDING (Keychron norm).

### 38. Keychron Q5 Max, Carbon Black — `keychron-q5-max-carbon-black`
- **Category:** keyboards
- **Variant pinned:** Fully Assembled Knob, 96%, Carbon Black, Gateron Jupiter Red
- **Why it qualifies:** keychron.com US from $199.99.
- **Identifiers:** MPN Q5M-M1 VERIFIED (tech.co.za, alza.de — Red switch); UPC PENDING (Keychron norm).
- **Flag:** exact-variant ANSI stock not directly read on keychron.com US (ISO Red was out of stock; UK-ISO Red available). Re-check stock at add time — same flag pattern as batch-1 V1 Max.

### 39. Anker Soundcore Liberty 5 Pro, Black — `anker-liberty-5-pro-black`
- **Category:** earbuds
- **Variant pinned:** Black (Midnight Black), D1203Z11. Launched May 21, 2026, $169.99 list.
- **Why it qualifies:** Current flagship ANC earbuds (Thus AI chip, Guinness-certified call quality); Soundcore US direct in stock $169.99; Abt $169.99; B&H $149.99 sale.
- **Identifiers:** MPN D1203Z11; UPC **194644311063 — VERIFIED** (Abt retailer spec page, model D1203Z11).
- **Price/stock:** $149.99–$169.99, in stock.
- **Flags:** Best Buy US listing is sold by AnkerDirect (marketplace), not Best Buy itself — do not use as the Best Buy row. Conflicting Amazon-only UPC 194644330989 exists — **not adopted**; do not use. Distinct from Liberty 5 Pro Max (D1204Z11, UPC 194644316440 at B&H).

### 40. Anker Prime Power Bank (20K, 220W) — `anker-prime-power-bank-20k-220w-black`
- **Category:** power-banks
- **Variant pinned:** Black, A110B, 20,100mAh, 220W total, 2× USB-C + 1× USB-A, smart display
- **Why it qualifies:** The *current* 20K Prime power bank (successor to the A1336 200W, which is sold out — see rejections); Anker US direct $179.99 in stock ($50 off, list $229.99).
- **Identifiers:** MPN A110B; UPC PENDING — no lead found.
- **Price/stock:** $179.99 sale / $229.99 list, in stock at Anker US.
- **Note:** the brief's "A1289" is the 737 Power Bank 24K, not a 20K Prime — corrected.

### 41. Alienware AW2725Q — `alienware-aw2725q`
- **Category:** monitors
- **Variant pinned:** 27" 4K QD-OLED 240Hz, single colorway, MPN 2MHGG
- **Why it qualifies:** Current flagship 27" 4K QD-OLED (launched 2025); Dell US direct $799.99 sale / $899.99 list; Best Buy $699.99.
- **Identifiers:** MPN 2MHGG (Dell USA tech specs); UPC **884116493297 — VERIFIED (single source)** (Megekko retailer spec PDF, EAN 0884116493297).
- **Price/stock:** $699.99–$899.99, in stock.
- **Flag:** UPC is single-source verified — treat as VERIFIED per the retailer-spec-page standard, but re-confirm at add time. Distinct from AW2725DM (IPS QHD), AW2725D (QD-OLED QHD 280Hz, #43 below), AW2725DF (360Hz).

### 42. Alienware AW2725DM — `alienware-aw2725dm`
- **Category:** monitors
- **Variant pinned:** 27" QHD 180Hz Fast IPS, single colorway
- **Why it qualifies:** Current budget Alienware 27" (launched Feb 2025, successor to AW2724DM); Dell USA page live; list $269.99.
- **Identifiers:** MPN FC46N (Dell USA tech specs; Canada/Amazon show 6R0H2 — regional MPNs differ, pin FC46N for US); UPC PENDING, lead 884116492764 (camelcamelcamel, Amazon-derived only — weak, do not promote).
- **Price/stock:** list $269.99; street ~$199.99 (Amazon-tracked, excluded channel).
- **Flag:** Dell US price was not exposed in the page crawl — confirm Dell US price at add time. Not in catalog (AW2726DM is; different model).

### 43. Alienware AW2725D — `alienware-aw2725d`
- **Category:** monitors
- **Variant pinned:** 27" QHD 280Hz QD-OLED, MPN CPVH4
- **Why it qualifies:** Current mid-range QD-OLED (launched summer 2025, $549.99 MSRP); Dell US direct $549.99 in stock (verified Nov 10, 2026, Dell storefront).
- **Identifiers:** MPN CPVH4; UPC PENDING, lead 884116639633 (PriceDrop GTIN listing — aggregator only, not a retailer spec page).
- **Price/stock:** $499–$549.99, in stock at Dell.
- **Flag:** none. Distinct from AW2725Q (4K 240Hz) and AW2725DF (360Hz).

### 44. Dell UltraSharp 40 Curved Thunderbolt Hub Monitor U4025QW — `dell-u4025qw`
- **Category:** monitors
- **Variant pinned:** 40" 5K2K (5120×2160) curved IPS Black, 120Hz, Thunderbolt 4 hub, 140W
- **Why it qualifies:** Current Dell flagship 40" pro monitor (launched Feb 2024, $2,399.99 list); Best Buy $2,389.99 (Nov 2, 2026); Dell $1,799.99 per ShopSavvy.
- **Identifiers:** MPN U4025QW; UPC PENDING, lead 884116452041 (ShopSavvy aggregator only).
- **Price/stock:** $1,799.99–$2,399.99, wide spread; in stock.
- **Flags:** very wide price spread — re-check Dell US price at add time. Best Buy's standalone listing is a 6ave Electronics 2-pack bundle — do not use that row.

### 45. HP OMEN 27qs G2 — `hp-omen-27qs-g2-black`
- **Category:** monitors
- **Variant pinned:** Black, 27" QHD 280Hz IPS, MPN AW3V0AA#ABA
- **Why it qualifies:** Current G2 refresh (launched Jan 2025, $449.99); HP.com US $499.99 in stock.
- **Identifiers:** MPN AW3V0AA#ABA; UPC PENDING — no lead found.
- **Price/stock:** $449.99–$499.99, in stock at HP.com.
- **Flags:** successor to the original 27qs, which is now Best Buy clearance (see rejections). Distinct from OMEN 27q G2 (AV4H6AA#ABA, in catalog).

### 46. HP OMEN Transcend 32 — `hp-omen-transcend-32-black`
- **Category:** monitors
- **Variant pinned:** Black, 31.5" UHD 240Hz OLED, MPN 9R181AA#ABA
- **Why it qualifies:** Current HP flagship 32" OLED gaming monitor; HP.com US $779.99 in stock.
- **Identifiers:** MPN 9R181AA#ABA; UPC PENDING — no lead found.
- **Price/stock:** $779.99 at HP.com, in stock.
- **Flags:** none. (The brief's "OMEN 32" is a 2017 discontinued model — see rejections; Transcend 32 is the current distinct model in that size class.)

### 47. Amazon Kindle (2024) 16GB, Black — `amazon-kindle-16gb-2024-black`
- **Category:** e-readers
- **Variant pinned:** Black, 16GB, 6" 300ppi, 11th generation, with lockscreen ads (MSRP $109.99)
- **Why it qualifies:** Current entry Kindle (The Verge, Nov 10, 2026, still calls the 2024 model "the most recent entry-level Kindle"); Target $149.99; Abt $149.99 in stock; Best Buy also carries it.
- **Identifiers:** MPN B0CNV9F72P (ASIN as retail code, consistent with the catalog's Kindle Paperwhite/Scribe practice); UPC PENDING — no UPC surfaced on Target/Abt spec pages.
- **Price/stock:** $109.99 MSRP (with ads) vs $149.99 observed at Target & Abt — **unresolved $40 gap** (may be ad-free repricing); in stock.
- **Flags:** ads vs ad-free variant not cleanly pinned by ASIN — confirm at add time. One Target review mentions "new 2027 kindles" — unverified user chatter, but a generational risk to watch.

### 48. ASUS ROG Strix Scope II 96 Wireless, Black — `asus-rog-strix-scope-ii-96-wireless-black`
- **Category:** keyboards
- **Variant pinned:** Black, 96% layout, ROG NX Snow (NXSW) switches, MPN 90MP037A-BKAA01 (X901 STRIX SCOPE II 96 WL/NXSW/CA/PBT)
- **Why it qualifies:** Current ROG wireless keyboard; ASUS ROG US store $179.99 in stock.
- **Identifiers:** MPN 90MP037A-BKAA01; UPC PENDING — no lead found.
- **Price/stock:** $179.99, in stock at ASUS US.
- **Flags:** do not confuse with the Scope II 96 **RX** Wireless (optical switches, different model) or the white variant (90MP037A-BKAA30).

### 49. ASUS ROG Azoth, Black — `asus-rog-azoth-black`
- **Category:** keyboards
- **Variant pinned:** Black, 75%, ROG NX Snow switches, MPN 90MP031A-BKAA01 (M701 ROG AZOTH/NXSW/CA/PBT)
- **Why it qualifies:** Still sold new at full list by ASUS US eShop, $249.99 in stock. Distinct from ROG Azoth 96 HE (90MP040H-BKAA20, in catalog).
- **Identifiers:** MPN 90MP031A-BKAA01; UPC PENDING — only an EU EAN found (4711081875963, Finland store) — not a US UPC, do not use.
- **Price/stock:** $189.99 (older sale crawl) – $249.99 list, in stock.
- **Flags:** **previous generation** (2023; Azoth X / Azoth 96 HE are successors) but still sold new at list by brand direct — same posture as batch-1 INZONE H9 / Forerunner 965.

### 50. ASUS ROG Xbox Ally X — `asus-rog-xbox-ally-x-black`
- **Category:** handheld-consoles
- **Variant pinned:** Black, 7" FHD 120Hz, AMD Ryzen AI Z2 Extreme, 24GB, 1TB SSD, MPN RC73XA-XB_ALLYX.Z2E.24
- **Why it qualifies:** Current premium Xbox handheld (launched Oct 2026, $999.99); Best Buy sold-by-Best-Buy $999.99 in stock. Successor to the ROG Ally X (clearance — see rejections). Category precedent: Legion Go S (SteamOS) is in the catalog.
- **Identifiers:** MPN RC73XA-XB_ALLYX.Z2E.24; UPC PENDING — no lead found.
- **Price/stock:** $999.99, in stock at Best Buy.
- **Flags:** do not confuse with the ROG Xbox Ally X20 ($1,299.99, OLED anniversary model) or the base ROG Xbox Ally ($599.99).

## Reserve (passed verification, held out to keep the batch at exactly 50)

### R1. Bose TV Speaker (2nd Gen), Black — `bose-tv-speaker-2nd-gen-black`
- **Category:** soundbars
- **Variant pinned:** Black, single colorway
- **Why it qualifies:** Refreshed compact dialogue soundbar, launched Sept 2026 (center tweeter, HDMI cable in box); Bose direct $299. Distinct from the 1st-gen TV Speaker (838309-1100, 2020) — do not confuse.
- **Identifiers:** MPN BOSETVSPEAKER2 (per Abt listing); UPC PENDING — no lead found anywhere (model is ~2 months old).
- **Why held out:** Bose-direct only so far — no second US retailer listing surfaced. Same single-channel caveat as the batch-1 HS80 v2 MAX reserve. First in line if any of the 50 fails re-check at add time.

## Cut at synthesis (passed group verification, held for a future batch — cut only to fit 50)

| Model | Key | Why cut |
|---|---|---|
| Logitech K780 Multi-Device, White/Grey | `logitech-k780` | 2016 model; thinnest retail in the batch (distributor-only: CompSource $76.99, OfficeSupplyInc $79.80; no Best Buy/B&H live listing). UPC 097855122834 verified (single-source distributor spec). |
| Anker Soundcore Sleep A20, Off-White | `anker-sleep-a20-off-white` | Previous generation (Sleep A30 successor); Abt delisted; clearance-drift signal (Best Buy $99.99 vs Anker list $179.99). UPC 194644192228 verified (Abt spec + manual). |
| Keychron K10 Max, Black | `keychron-k10-max-black` | MPN K10M-H3 is a single-distributor lead (Selenal), not fully verified; exact-variant stock not directly read. Weakest Keychron in the batch. |
| Corsair K70 CORE TKL RGB (wired), Black | `corsair-k70-core-tkl-rgb-black` | Corsair US stock/price not directly confirmed — price rests on an independent guide (~$89.99, Nov 4); own US page for the wired TKL NA did not surface. UPC lead 840006678786 (Amazon.in only). |

## Summary

### Per brand (50)
| Brand | Count | Models |
|---|---|---|
| Sony | 5 | ULT FIELD 7, ULT FIELD 3, ULT FIELD 5, INZONE Buds, BRAVIA Theatre Bar 6 |
| JBL | 5 | Live Buds 3, Boombox 4, PartyBox 330, PartyBox 130, Tune Beam 2 |
| Apple | 5 | Pencil Pro, Pencil (USB-C), Magic Keyboard Touch ID, Watch SE 3 44mm, Watch Series 12 46mm |
| Razer | 4 | DeathAdder V3 HyperSpeed, Kraken V4, Seiren V3 Mini, Viper V3 HyperSpeed |
| Logitech | 3 | G915 X TKL, Superlight 2c, MX Master 3S Bluetooth |
| HyperX | 3 | Cloud Stinger 2, Haste 2 Wireless, QuadCast 2 |
| Nintendo | 3 | Switch 2 Camera, Switch 2 Dock Set, Joy-Con 2 Charging Grip |
| Garmin | 3 | Forerunner 970, Forerunner 570 47mm, fēnix 8 47mm |
| Keychron | 3 | Q1 HE, Q6 Max, Q5 Max |
| Alienware | 3 | AW2725Q, AW2725DM, AW2725D |
| ASUS | 3 | Scope II 96 Wireless, ROG Azoth, ROG Xbox Ally X |
| Bose | 2 | QC Ultra Earbuds 2nd Gen, Smart Ultra Soundbar |
| Anker | 2 | Liberty 5 Pro, Prime Power Bank 20K 220W |
| HP | 2 | OMEN 27qs G2, Transcend 32 |
| Corsair | 1 | Scimitar Elite Wireless SE |
| Samsung | 1 | Buds3 Pro Silver |
| Dell | 1 | U4025QW |
| Amazon | 1 | Kindle 16GB 2024 |
| **Total** | **50** | **18 brands** |

### Per category (50)
| Category | Count |
|---|---|
| keyboards | 7 |
| mice | 6 |
| monitors | 6 |
| speakers | 6 |
| earbuds | 6 |
| wearables | 5 |
| accessories | 3 |
| soundbars | 2 |
| headphones | 2 |
| microphones | 2 |
| cameras | 1 |
| docks | 1 |
| e-readers | 1 |
| handheld-consoles | 1 |
| power-banks | 1 |
| **Total** | **50** |

### Identifier status (50)
- UPC VERIFIED: 11 — ULT FIELD 7, ULT FIELD 3, ULT FIELD 5, Smart Ultra Soundbar, Live Buds 3, Boombox 4, PartyBox 330, G915 X TKL, Pencil (USB-C), Liberty 5 Pro, AW2725Q.
- UPC PENDING: 39 — INZONE Buds (conflicting leads), BRAVIA Theatre Bar 6 (no lead), QC Ultra Earbuds 2nd Gen, PartyBox 130 (no lead), Tune Beam 2 (no US lead), Superlight 2c, MX Master 3S Bluetooth, DeathAdder V3 HyperSpeed (no lead), Kraken V4 (no lead), Seiren V3 Mini, Viper V3 HyperSpeed, Cloud Stinger 2, Haste 2 Wireless (no lead), QuadCast 2 (no lead), Scimitar Elite Wireless SE, Pencil Pro, Magic Keyboard Touch ID, Watch SE 3 44mm (no lead), Watch Series 12 46mm (no lead), Buds3 Pro (no lead), Switch 2 Camera, Switch 2 Dock Set (no lead), Joy-Con 2 Charging Grip (no lead), Forerunner 970, Forerunner 570 (no lead), fēnix 8 (no lead), Q1 HE, Q6 Max, Q5 Max, Prime Power Bank 20K 220W (no lead), AW2725DM, AW2725D, U4025QW, OMEN 27qs G2 (no lead), OMEN Transcend 32 (no lead), Kindle 16GB 2024, Scope II 96 Wireless (no lead), ROG Azoth, ROG Xbox Ally X (no lead).
- MPN pending (2): Switch 2 Camera, Switch 2 Dock Set. All other 48 have an MPN recorded (Kindle MPN is an ASIN retail code, consistent with the catalog's existing Paperwhite/Scribe practice).

## Considered and rejected (71 group rejections + 2 borderline dropped)

| Model | Reason |
|---|---|
| Sony WH-1000XM6 | Duplicate — in catalog as `sony-wh1000xm6-black` (verified). |
| Sony LinkBuds Fit | Duplicate — in catalog as `sony-linkbuds-fit-black` (verified). |
| Sony LinkBuds Open | Duplicate — in catalog as `sony-linkbuds-open-black` (verified). |
| Sony SRS-XB100 | Superseded by ULT FIELD 1 (in catalog); no brand/retailer-direct new US listing — only marketplace/international stock. |
| Bose QuietComfort Earbuds (2024) | Duplicate — in catalog as `bose-qc-earbuds-black` (verified). |
| Bose Soundbar 900 | Superseded by Smart Ultra Soundbar (Bose's own FAQ/press release); retailers clearing stock; new Lifestyle Ultra Soundbar (May 2026) is now flagship. |
| Bose Smart Soundbar 300 | Discontinued — Bose discontinued it; Abt: "no longer available". |
| Bose Smart Soundbar (2024 rebrand, MPN 892079-1100) | Not a separate model — the 2024 rebrand of the in-catalog Smart Soundbar 600 (873973-1100); proposing it risks a duplicate. |
| Bose TV Speaker (1st Gen, 838309-1100) | Superseded by the 2nd Gen (held as Reserve); Bose still sells 1st-gen at $279, but the current model is the 2nd Gen. |
| JBL Charge 6 | Duplicate — in catalog as `jbl-charge-6-black` (pending). |
| JBL Xtreme 4 | Duplicate — in catalog as `jbl-xtreme-4-black` (verified). |
| JBL PartyBox 320 | Duplicate — "PartyBox 320" is the marketing name for the in-catalog PartyBox Stage 320 (`jbl-partybox-stage-320-black`, MPN JBLPBSTAGE320AM). The distinct 2026 successor, PartyBox 330, is in this batch as #10. |
| JBL Pulse 5 | No live direct new stock: Best Buy "Unavailable", JBL.com OutOfStock; 2023 model. |
| JBL PartyBox Club 120 | Replaced by PartyBox 130 (May 2026, in this batch as #11); Abt delisted ("no longer available"). |
| JBL Endurance Peak 3 | Borderline — dropped on Group A recommendation: end-of-life watch (Abt delisted, Crutchfield low stock, 2023 model). |
| JBL Authentics 300 | Borderline — dropped on Group A recommendation: Best Buy clearance + 2023 model + unverified UPC (weak Rakuten-slug lead only). |
| Logitech G502 HERO | Excluded per the research brief; synthesis found it is NOT in the 250 catalog at all (only G502 X / G502 X PLUS) and its identifier is unresolved (part-number conflict, no UPC). See decision item 5. |
| Logitech G713 | Discontinued (CompSource marks 920-010413 DISCONTINUED); street $47–85 vs $169.99 MSRP = clearance drift. |
| Logitech POP Mouse | Original colorways winding down; no live Logitech-direct or major-retailer US listing confirmed — only small resellers + Amazon. |
| Razer BlackWidow V4 Pro | Duplicate — in catalog as `razer-blackwidow-v4-pro-green-black` (pending). |
| Razer Basilisk V3 Pro 35K | Duplicate — in catalog as `razer-basilisk-v3-pro-35k-black` (pending). |
| HyperX Alloy Rise 75 | Duplicate — in catalog as `hyperx-alloy-rise-75-black` (pending). |
| HyperX Cloud III Wireless (non-S) | Superseded by Cloud III S (already in catalog); no live HP/HyperX US listing — only Amazon-fulfilled "only 1 left" and a used/demo EU listing. |
| Corsair K65 PLUS Wireless | Duplicate — in catalog as `corsair-k65-plus-wireless-midnight-grey` (pending). |
| Corsair K70 CORE (as named) | Duplicate: "K70 CORE" *is* the RGB model already in catalog (CH-910971E-NA); no non-RGB K70 CORE exists. The TKL RGB was cut at synthesis (see above). |
| Corsair Darkstar Wireless | No live US brand/retailer-direct listing confirmed; Corsair EU out of stock; US street ~$87–96 vs $169.99 list = clearance drift. |
| Corsair Scimitar Elite Wireless (plain, CH-9314311-NA) | Corsair US OutOfStock; Revival refurb listed; only Amazon-fulfilled stock. SE variant passes as #23. |
| Corsair K100 AIR | No clean US direct channel: Best Buy shows a marketplace seller ($249.99) plus a $57.99 anomaly (clearance/open-box signal); CompSource out of stock; Amazon $140.28 excluded. Same end-of-life pattern as rejected K100 RGB. |
| Corsair Sabre Pro / Sabre RGB Pro | Discontinued — Corsair US page states "Discontinued" for CH-9303111-NA; Revival only. |
| Corsair Virtuoso Pro (CA-9011370-NA) | No live US brand/retailer-direct listing confirmed (Best Buy Canada is a marketplace seller; LDLC sold out / White "no longer on sale"); only Amazon $149.99 cited. |
| Apple AirPods 4 (MX2X3LL/A) | Discontinued — Apple store page now redirects to AirPods 5 (Sept 2026); Best Buy listings are marketplace-only (UNITED TECHNOLOGY, Fulfillio); no Best Buy-sold listing. |
| Apple iPad 11th gen (A16) | Duplicate — in catalog as `apple-ipad-a16-11` (MD3Y4LL/A). |
| Apple Magic Mouse (USB-C) | Duplicate — in catalog as `apple-magic-mouse-usbc`. |
| Apple Magic Trackpad (USB-C) | Duplicate — in catalog as `apple-magic-trackpad-usbc`. |
| Apple Watch SE 3 40mm | Duplicate — in catalog as `apple-watch-se3-40mm` (pending). 44mm passes as #27. |
| Samsung Galaxy Buds FE (SM-R400) | Effectively discontinued — no live retailer-direct new US listing; Staples out of stock, Best Buy US page stale, only renewed/open-box elsewhere. Successor Buds3 FE is in the catalog. |
| Samsung Galaxy Watch Ultra (original, SM-L705) | Previous-gen + clearance: the $454.99 Best Buy-sold listing is the **2025 refresh** (SM-L705UZS1XAA) tagged Clearance; 2024 model (SM-L705UZTAXAA) has no clean Best Buy-sold price, other SKUs are marketplace sellers. Ultra2 is in the catalog. |
| Samsung Galaxy Tab S11 FE | Model does not exist (no such Samsung tablet as of Nov 2026); Tab S11 itself is already in the catalog (pending). |
| Samsung Galaxy Book5 Pro 14" (NP940XHA-KG1US / KG3US) | Clearance-only at Best Buy — 16GB/512GB $307.99 clearance, 32GB/1TB $1,484.99 clearance and sold out. |
| Samsung Odyssey G5/G6/G7 | Not pinned — family confusion: the 2020 G7 27" (LC27G75TQSNXZA) is on Best Buy clearance $664.99; current 2025 models (G70F 27" dual-mode 4K, G75F 37") lack a verified US MPN/price pair in this pass. Re-probe the G70F 27" separately. |
| Samsung Galaxy Watch FE | Already rejected in batch 1 (discontinued) — not re-proposed. |
| Nintendo Joy-Con 2 (pair) | Duplicate — in catalog as `nintendo-joy-con-2-pair-light-blue-light-red`. |
| Garmin Venu 4 | Duplicate — in catalog as `garmin-venu-4-45mm-silver-gray`. |
| Garmin Instinct 3 | Duplicate — in catalog as `garmin-instinct-3-amoled-45mm-black`. |
| Garmin Edge 850 | Duplicate — in catalog as `garmin-edge-850`. |
| Microsoft Surface Laptop 7 (13.8", 7th Ed, Snapdragon X Elite) | Superseded + clearance/marketplace-only: Best Buy's own-stock listing is Clearance $1,444.99 (Black 512GB, ZGP-00037); all other Best Buy listings are marketplace sellers. The 8th Edition (Snapdragon X2 Plus) is in the catalog. |
| Microsoft Xbox Wireless Controller | Duplicate — in catalog as `xbox-wireless-controller-black`. |
| Microsoft Surface Headphones 2+ | Discontinued (2021 business model) — no live brand/retailer-direct US listing; only $149 at Amazon (excluded channel). |
| Lenovo Legion Go 2 | Rejected on price/stock instability — launched $1,349.99 (Oct 2025), now $1,999.99 at Best Buy (1TB, reported unavailable Oct 5), $2,849.99–$3,081.99 at Lenovo US (2TB, out of stock / "available soon"); only B&H 2TB $1,849.99 was live. No verified US MPN/UPC pair. Re-probe later if pricing stabilizes. |
| Lenovo Legion Tab Gen 3 | Duplicate — in catalog as `lenovo-legion-tab-gen-3-eclipse-black` (pending). |
| Anker Prime Charger 65W (brief's A2664/A2666) | Brief MPNs wrong: A2664 = 715 Nano II 65W single-port (2022); A2667 = 735 GaNPrime 65W 3-port (2022). No "Prime Charger 65W" exists. No live US brand/retailer-direct price confirmed for either (Amazon-only evidence). |
| Anker Prime Power Bank 20K 200W (A1336) | Sold out at Anker (US/NZ/AU pages show SoldOut); only Amazon pricing survives. Superseded by A110B 220W (in this batch as #40). |
| Anker 737 GaNPrime Charger (A2148; brief's "A2145" doesn't exist) | Sold out at Anker NZ ($149.95); US evidence is Amazon-only at $57–63 vs $94.99 MSRP = clearance drift. |
| Anker 737 Power Bank (A1289, 24K 140W) | No live US brand/retailer-direct channel confirmed (AU page + Amazon only). |
| Alienware AW420K keyboard | 2022 model, superseded twice (AW920K, Pro Wireless keyboard); no clean US Dell direct price surfaced. |
| Alienware AW720M mouse | 2022 model, superseded by Pro Wireless mouse; $49.99 Amazon-fulfilled clearance signal. |
| Dell U2725QE | Duplicate — in catalog (95WRG). |
| Dell 27 Plus 4K S2725QS | Duplicate — in catalog (T4CNF). |
| HP OMEN 27qs (original, 240Hz) | Best Buy clearance $100.99, Unavailable. Superseded by 27qs G2 (in this batch as #45). |
| HP OMEN 32 (original, 2017, 75Hz) | Long discontinued. Current 32" line is OMEN 32x (in catalog) / OMEN Transcend 32 (in this batch as #46). |
| HP OMEN 32x | Duplicate — in catalog (99Z68AA#ABA, batch 1). |
| HP 930 Creator Wireless Mouse | 2021 model, $89.99 MSRP; no live US HP.com/retailer-direct channel found; NZ clearance $49.99. |
| HP 935 Creator Wireless Mouse | No live US HP.com listing confirmed (HK limited availability, AU only). 2021 model. |
| Google Pixel Watch 3 (41mm) | Discontinued by Google (not on Google Store), two generations back (Watch 5 now out); only residual Target ($249.99 list) / Amazon ($180–204) stock = clearance drift. |
| Google Pixel Buds Pro 2 (any color) | Duplicate — Pro 2 Porcelain in catalog (GA05760-US); other colors = same model. |
| Google Pixel Buds 2a (any color) | Duplicate — Buds 2a Hazel in catalog (GA06155-US); other colors = same model. |
| Amazon Fire HD 10 (2023) | Amazon-only channel (no non-Amazon US retailer row); previous-gen (2025 Kids refresh exists). |
| Meta Quest 3S (any config) | Duplicate — Quest 3S 128GB in catalog (SK-1000926-01); other storage = same model. |
| Meta Quest 3 (any config) | Duplicate — Quest 3 512GB in catalog (899-00583-01); 128GB discontinued anyway. |
| ASUS ROG Ally X | Best Buy clearance $809.99, Unavailable. Superseded by ROG Xbox Ally X (in this batch as #50). |
| ASUS TUF Gaming VG27AQML1A | One retailer lists it EOL; no US Best Buy or ASUS-store row found; US price only via Amazon ($369.99). |
| ASUS ROG Keris II Ace | Duplicate — in catalog (90MP03N0-BMAA00). |
| ASUS ProArt PA279CRV | Duplicate — in catalog (verified, UPC 195553951531). |

## Corrections to brief-supplied identifiers (for the record)
- G915 X TKL: MPN 920-012715, not 920-012681. Viper V3 HyperSpeed: MPN RZ01-04910100-R3U1, not RZ01-05160100. DeathAdder V3 HyperSpeed: guessed UPC 840272911235 NOT confirmed — do not use.
- Magic Keyboard Touch ID: MPN MXCK3LL/A, not MKK63LL/A (Lightning-era part). Forerunner 970: MPN 010-02969-00, not 010-03046. Switch 2 Camera: BEE-014 is a Joy-Con code, not the camera MPN; Nintendo store code is 123682 US. Switch 2 Dock Set: dock unit is BEE-005; no retail MPN for the set.
- "Prime Charger 65W (A2664/A2666)" does not exist as briefed; "Prime Power Bank 20000mAh (A1289)" conflates the 737 Power Bank (A1289, 24K) with the Prime 20K (A1336 sold out / A110B current); "737 GaNPrime (A2145)" — A2145 doesn't exist, A2148 is the charger, A1289 the power bank; "OMEN 32" is a 2017 model, Transcend 32 is the current distinct one; "Kindle basic B0CFPJYX7P" is wrong — that ASIN is the Paperwhite; basic is B0CNV9F72P.
- JBL PartyBox 320 is the marketing name for the in-catalog PartyBox Stage 320 (JBLPBSTAGE320AM); the distinct 2026 successor is PartyBox 330. Bose Smart Soundbar (2024 rebrand, MPN 892079-1100) is the in-catalog Smart Soundbar 600 (873973-1100). "K70 CORE" (as named) IS the RGB model already in the catalog (CH-910971E-NA); no non-RGB K70 CORE exists.
- G502 HERO: the brief said it was pending in the catalog — synthesis verified it is NOT in the 250 catalog (only G502 X / G502 X PLUS exist). Identifier unresolved (part-number conflict, no UPC).

## Membership-check record (repeatable)
Checked against all 250 catalog rows (`/tmp/catalog250.json`) by key, model, MPN, UPC at synthesis (scripted): 0 collisions across all 55 group passes, and 0 collisions among the 55 themselves. Group-level checks recorded in /tmp/batch2_groupA.md, /tmp/batch2_groupB.md, /tmp/batch2_groupC.md, /tmp/batch2_groupD.md. Duplicates found and excluded are in the rejections table above.

## Needs the user's decision
1. **Approve this batch of 50 for adding to the catalog?** (Per DECISIONS 068, per-batch approval.) Nothing is added until the user says so.
2. **Reserve:** Bose TV Speaker (2nd Gen) passed verification but is held out at exactly 50 because only Bose-direct stock is confirmed so far and it has no UPC lead yet. Include it as #51 now, or keep it as first reserve for the next batch / for any of the 50 that fails re-check at add time?
3. **Flagged items — approve as-is, hold, or drop?** ULT FIELD 7 (B&H stock conflict), ULT FIELD 5 (Adorama backorder), INZONE Buds (2023, price drift), QC Ultra Earbuds 2nd Gen (marketplace listing to avoid — pin Best Buy-sold SKU), Smart Ultra Soundbar (previous flagship), Live Buds 3 (deep discount, refurb circulation), Tune Beam 2 (Black US page unconfirmed), MX Master 3S Bluetooth (previous-gen, Bluetooth-only), Buds3 Pro (previous-gen), fēnix 8 (previous-gen), ROG Azoth (previous-gen), Q5 Max (ANSI stock unread), AW2725DM (Dell US price uncaptured), U4025QW (wide price spread), Kindle 16GB 2024 ($40 price gap + ads-variant ambiguity), Watch Series 12 46mm (Black variant unavailable — Dark Bronze pinned), Watch SE 3 44mm (Starlight pinned over Midnight), PartyBox 130 (no UPC lead), Switch 2 Camera (promo-anomaly history). If any is dropped, the Reserve is the first replacement; the 4 cut-at-synthesis models are next in line.
4. **Pending identifiers:** 39 of 50 have UPC pending (11 verified, vs batch 1's 22/50). Per the standing rule the identifiers stay pending — no rule change is proposed. Re-probe the pending UPCs on the next refresh rather than promoting Amazon-only leads. MPN pending for 2 (Switch 2 Camera, Switch 2 Dock Set).
5. **G502 HERO discrepancy:** memory said it was pending in the catalog, but synthesis verified it is NOT in the 250 catalog at all. Its identifier is unresolved (part-number conflict, no UPC). Add to a future batch after fresh verification, or leave out?
6. **Not in this batch (unchanged, still open):** the Kindle Paperwhite "Amazon exclusive, skip" note question (Best Buy row) is separate from this list and still awaits the user's separate decision. Follow-up probes for later: Samsung Odyssey G70F 27" US pin, Lenovo Legion Go 2 re-probe if pricing stabilizes, Bose Lifestyle Ultra Soundbar ($1,099, May 2026 flagship — MPN/UPC unverified), Sony ULT TOWER 9/5, JBL Vibe Beam 2 / Tune Flex 2 / PartyBox 520, Samsung Galaxy Buds Core, Garmin Venu 4 41mm, Lenovo Legion Go S Windows version.
