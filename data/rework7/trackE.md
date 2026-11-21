# Track E — Batch 7 draft research (action cameras / laptops, 10 models)

- **Date:** 2026-11-21 (all prices / stock checked 2026-11-21; B&H and Best Buy pages re-opened live, crawls <1 hr old at 20:54–20:55 UTC).
- **Researcher:** Track E (subagent, depth 2/2). Skill `price_compare_expansion` read before work. No catalog, DECISIONS, snapshot, or site files touched.
- **Scope:** 10 models from the brief — 6 action cameras (items 1–6) + 2 laptops from deal-site gaps (7–8) + 2 queue-top laptops from the batch-6 backlog alternates (9–10).
- **Result tally: KEEP 9 / DROP 1.**
  - Both identifiers VERIFIED: 3 (GoPro LIT Hero, DJI Osmo Pocket 3 Creator Combo, Lenovo Legion 5a 83Q70068US).
  - MPN VERIFIED / UPC PENDING: 3 (Yoga 7i 83JT0000US, Zenbook A14 UX3407QA-PS76, OmniBook 3 14-hz0788dx).
  - Both identifiers PENDING: 3 (Osmo Action 4 Essential, Osmo Action 6 Essential, Insta360 Ace Pro 2 Xplorer Costco bundle).
  - DROP: 1 (Osmo 360 Skiing Combo — no MPN, no qualifying UPC, no in-stock direct row; DJI US OutOfStock).
- **Amazon rule applied throughout:** no Amazon price is used as a price source anywhere below. Amazon figures appear only as (a) the deal-site evidence the brief cited, explicitly marked unusable, or (b) a non-qualifying identifier agreement, explicitly marked non-qualifying.

## Membership check

- Checked against `/tmp/catalog_ref_500.tsv` (500 rows) by exact key, model-name substring (normalized, both directions), MPN, and UPC (including pending leads): **0 collisions.** The file has since disappeared from `/tmp` between exec calls, so the check was re-run directly against `price_agent/catalog.py` (regex parse of `EvalProduct(...)` entries; 478/500 entries captured by that quick parse — the shortfall is a parser-formatting gap, not a catalog gap; the earlier full-TSV check covered all 500 rows). Re-run result: **0 raw hits** on every candidate term (model names, MPNs, UPCs).
- Sibling adjudications (not duplicates):
  - No DJI, GoPro, or Insta360 camera of any kind is in the catalog — the action-camera category is new to the set. Action 4 vs Action 6, Pocket 3 vs Osmo 360 are distinct models by sensor, MPN family, and combo contents.
  - `lenovo-yoga-7i` vs in-catalog Yoga *Tab* models (Yoga Tab Plus Gen 2, Yoga Tab Gen 2): tablets, not the Yoga 7i 2-in-1 laptop. Distinct.
  - `lenovo-legion-5a` (83Q70068US) vs in-catalog Legion Pro 5 Gen 10 (83LT000MUS, RTX 5060 / Ryzen 7 8745HX, 16" OLED): different line (5a vs Pro 5), different chassis/CPU. Distinct. Also distinct from the backlog Legion 5i 83LY0000US and from sibling config 83Q70003US (1TB, same $1,249 — do not mix).
  - `asus-zenbook-a14` / `hp-omnibook-3-14-hz0788dx`: no Zenbook A14 and no OmniBook of any kind in the catalog.
- Intra-track duplicates: none (10 distinct keys / MPN families).

## Candidates

### 1. DJI Osmo Action 4 Essential Combo — Black [KEEP, both identifiers PENDING]

- **Key:** `dji-osmo-action-4-essential-combo-black`
- **Category:** action-cameras (new category)
- **Variant pinned:** Black, Essential Combo — camera + 1× Extreme Battery + Horizontal-Vertical Protective Frame + Quick-Release Adapter Mount + Locking Screw + Type-C to Type-C PD Cable + Lens Hood + Anti-Slip Pad. (Per DJI US store "In the Box"; the Standard Combo adds a Curved Adhesive Base, the Adventure Combo adds 2 more batteries, battery case, extension rod — pin Essential only.)
- **Why it qualifies:** Mainstream DJI action camera (1/1.3" sensor, 4K/120fps); brand-direct row at DJI US store below list. No camera of this model in the catalog.
- **Identifiers:** MPN — **PENDING, no qualifying lead.** Do NOT attach the Standard Combo MPN CP.OS.00000269.01 or the Adventure Combo MPN CP.OS.00000270.01 (both confirmed on B&H pages for those combos, not Essential). UPC — **PENDING + lead 190021133402** (Sharaf DG UAE retailer listing only — single source, non-qualifying; Amazon prints EAN 6937224107922 for this combo, also non-qualifying). Neither code is verified.
- **Price / stock:** DJI US store **$169.00** (was $229.00), variant 67781549949002, page fetched 2026-11-21. Explicit InStock wording was not captured in the fetch — re-check stock at add time. Best Buy Essential listing (SKU 12596918) is $229.00 Sold Out via Focus Camera (marketplace) — not usable. B&H does not list the Essential Combo as a separate SKU (only Standard/Adventure + B&H kits).
- **Flag:** The brief's Amazon $155.35 (list $239) cannot be used — Amazon in any form is not a price source. The live direct price is $169.00, i.e. higher than the Amazon deal price; the catalog row would carry $169.00, not $155.35. Refurb/used AliExpress rows (~$111–$129) are excluded.
- **Deal-site evidence:** Slickdeals thread 2026-11-08, $189 Amazon (DJI Tech Hub via Amazon), marked still available in-thread; a 2026-11-21 Amazon price report puts it at $155.35 (brief's figure). DealMoon asserted by the brief — not independently re-verified in this session. Saves counts not captured. Single-side-verified (Slickdeals only, in-session).

### 2. GoPro LIT Hero 4K60 — Black [KEEP, both identifiers VERIFIED]

- **Key:** `gopro-lit-hero-4k60-black`
- **Category:** action-cameras
- **Variant pinned:** Black, standalone LIT Hero (built-in light, 4K60, 12MP, 93 g). Pin the standalone camera, not the Best Buy accessory bundles (CHDXF-131/132/133/134, CHDHF-132-AT_EDI_1).
- **Why it qualifies:** GoPro's 2025 compact HERO (successor to the original HERO CHDHF-131-AT); Best Buy direct in-stock row + B&H in-stock row. Both identifiers VERIFIED — the cleanest camera in this track.
- **Identifiers:** MPN CHDHF-132-AT — **VERIFIED** (Best Buy model field, SKU 6642404 and SKU 12726374 + B&H "MFR # CHDHF-132-AT", BH # GOLITHERO). UPC 810116384129 — **VERIFIED** (B&H spec page "UPC: 810116384129" + GoPro's own LIT HERO sell-sheet PDF, hosted on Aqipa's asset server — Aqipa is a GoPro distributor; the PDF is verbatim GoPro and prints "UPC: 810116384129 SKU: CHDHF-132-AT"). Retailer + manufacturer-PDF/distributor pair, same shape as the batch-5/6 accepted precedents.
- **Price / stock:** Best Buy **$269.99** InStock, sold by Best Buy (SKU 6642404; second SKU 12726374 also $269.99 InStock — same model, two SKUs; use 6642404). B&H $269.99 In Stock (BH # GOLITHERO). No promo at either direct channel.
- **Flag:** Do NOT attach Amazon bundle UPC 197684015847 (belongs to the CHDHF-132-AT_EDI_2 accessory bundle) or the NZ variant CHDHF-132-AS / UPC 810116384143 (different region). The brief's Slickdeals Amazon $169.99 (list $269.99) is Amazon-only and unusable — the direct-channel price is the $269.99 list price, so this entry adds a list-price row, not a deal row.
- **Deal-site evidence:** Slickdeals Tech, Amazon $169.99 (brief-asserted; thread not independently re-verified in-session). Single-source deal evidence; saves count not captured.

### 3. DJI Osmo Action 6 Essential Combo 8K — Black [KEEP, both identifiers PENDING]

- **Key:** `dji-osmo-action-6-essential-combo-black`
- **Category:** action-cameras
- **Variant pinned:** Black, Essential Combo — camera + 1× Extreme Battery Plus (1950 mAh) + Dual-Direction Quick-Release Adapter Mount + Locking Screw + USB-C to USB-C PD Cable (USB 3.1) + Anti-Slip Pad. (Per DJI store "In the Box"; the Standard Combo adds a Curved Adhesive Base, the Adventure Combo adds 2 more batteries, battery case, extension rod — pin Essential only.) 1/1.1" square sensor, 8K video, 50 GB built-in storage.
- **Why it qualifies:** Current DJI flagship action camera (announced 2025-11-18); brand-direct row at DJI US store. No Action 6 of any kind in the catalog.
- **Identifiers:** MPN — **PENDING, no qualifying lead.** An eBay UK listing prints "CPOS0000037701" for the Essential Combo — eBay is non-qualifying and the number does not fit the Standard/Adventure sequence (CP.OS.00000505.02 / CP.OS.00000506.02), so it is recorded here as an unconfirmed lead only and must NOT be attached. UPC — **PENDING + lead 190021161696** (Amazon + TradeKorea + Ubuy agree — all three non-qualifying; no retailer spec page prints it). Do NOT attach UPC 190021997370 (Essential + Street Photography Handle Kit bundle) or 190021998407 (Essential + 58-piece kit bundle).
- **Price / stock:** DJI US store **$426.00**, Essential variant 67656937701450 (variant table fetched live 2026-11-21; Standard $436.00, Adventure $454.00 on the same page). Explicit InStock wording not captured in the fetch — re-check stock at add time; djiindex's 2026-11-20 DJI-store check also lists the Essential at $426. B&H does not list the Essential Combo separately (Standard $436.00 In Stock / Adventure $454.00 In Stock only).
- **Flag:** The brief's Amazon $376 (list $446) cannot be used. The direct price is $426.00 — only $10 under the Standard Combo, so the Essential's value vs Standard is thin (the missing piece is one curved adhesive base); keep the entry as briefed, but do not present $376 anywhere. Note the brief's "2026 新款" is slightly off: launched 2025-11-18, still the current model.
- **Deal-site evidence:** DealMoon, Amazon $376 (brief-asserted; thread not independently re-verified in-session). Single-source deal evidence; saves count not captured.

### 4. DJI Osmo Pocket 3 Creator Combo — Black [KEEP, both identifiers VERIFIED]

- **Key:** `dji-osmo-pocket-3-creator-combo-black`
- **Category:** cameras (3-axis gimbal camera — suggest `cameras`, not `action-cameras`; coordinator to confirm)
- **Variant pinned:** Black, Creator Combo — Pocket 3 + DJI Mic 2 Transmitter + Wide-Angle Lens + Battery Handle + Osmo Mini Tripod + Carrying Bag. (Per B&H "Kit Contains" and Micro Center "What's in the Box"; the plain Pocket 3 and the B&H accessory-bundle variants DJOP3CCAK / DJOP3CC are different listings — pin the DJI Creator Combo only.)
- **Why it qualifies:** Mainstream DJI 3-axis gimbal camera (1" CMOS, 4K120); B&H Top Seller in-stock row. Both identifiers VERIFIED.
- **Identifiers:** MPN CP.OS.00000302.01 — **VERIFIED** (B&H page slug/title `dji_cp_os_00000302_01_osmo_pocket_3_creator` + Micro Center "Mfr Part #: CP.OS.00000302." + Adorama "MFR: CP.OS.00000302.01 A"). UPC 190021095007 — **VERIFIED** (Micro Center spec panel "UPC: 190021095007" + Target UPC field 190021095007 + Adorama bundle UPC-codes list includes 190021095007 for the Creator Combo kit).
- **Price / stock:** B&H **$466.00** In Stock (was $549.00, Holiday Savings $83.00), Add to Cart, free delivery Wed Nov 25, page opened live 2026-11-21. Micro Center lists $549.99 (OutOfStock in one crawl) — B&H is the row.
- **Flag:** Do NOT attach any B&H component UPC from this page to the kit: 190021094970 is the Pocket 3 camera alone, 190021094949 the wide-angle lens, 190021094932 the battery handle, 190021094918 the mini tripod, 190021094796 the carrying bag. Kit UPC is 190021095007 only.
- **Deal-site evidence:** DealMoon, Amazon $466 (list $629) (brief-asserted; thread not independently re-verified in-session). Note the B&H direct price is also $466.00 — the deal price coincides with the direct row. Single-source deal evidence; saves count not captured.

### 5. DJI Osmo 360 Skiing Combo — Black [DROP]

- **Key (proposed, not to be added):** `dji-osmo-360-skiing-combo-black`
- **Category:** action-cameras
- **Variant pinned (as briefed):** Skiing Combo — Osmo 360 Standard Combo + 1.2m Invisible Selfie Stick + Adjustable Quick-Release Adapter Mount and more (per DJI US store). Distinct from the Standard Combo (CP.OS.00000441.04), Adventure Combo (CP.OS.00000442.04), Vlog, Helmet, and Vortex combos.
- **Why it does NOT qualify — DROP, with reasons:**
  1. **MPN: no lead at all.** No B&H, Best Buy, or other retailer spec page for the Skiing Combo was found; no CP.OS. number surfaced in any qualifying source. (Standard = CP.OS.00000441.04, Adventure = CP.OS.00000442.04 — neither belongs to the Skiing Combo.)
  2. **UPC: non-qualifying lead only.** Amazon prints UPC 190021996731 for the Skiing Combo — Amazon only, non-qualifying, and its "Built-In Media" text contradicts DJI's own box contents (Amazon says a 1.5m selfie stick; DJI says 1.2m), so even the lead is unreliable.
  3. **No in-stock direct row.** The only direct price found is DJI US store **$618.99, OutOfStock** (JSON-LD, repeated across crawls 2026-11-21). B&H carries only the Standard/Adventure combos; no Best Buy Skiing listing found.
- **Price / stock (for the record, not a row):** DJI US $618.99 OutOfStock. EU DJI stores show it in stock (e.g. €530.99) — non-US, not usable.
- **Flag:** If the coordinator wants a 360 camera instead, the Standard Combo is the available substitute: CP.OS.00000441.04, B&H $404.77 In Stock (was $509.77, Holiday Savings $105), DJI US list $549.99 — but that is a different model and needs its own brief; do not silently swap it in for the Skiing Combo. Revisit the Skiing Combo only if DJI restocks it and a qualifying MPN/UPC surfaces.
- **Deal-site evidence:** DealMoon榜单 (brief-asserted; not independently re-verified in-session). No price evidence beyond DJI US $618.99.

### 6. Insta360 Ace Pro 2 Xplorer Action Camera Bundle — Black (Costco) [KEEP, both identifiers PENDING]

- **Key:** `insta360-ace-pro-2-xplorer-bundle-costco-black`
- **Category:** action-cameras
- **Variant pinned (bundle contents nailed down — Costco.com):** Ace Pro 2 camera + **2 total batteries + Xplorer Grip Kit + Quick Release Standard Mount + USB-C Cable + Mic Cap + Wrist Strap + 128GB microSD card**. Costco Item 9536006, Model "Ace Pro 2 Xplorer Bundle", Black, Online Only, Limit 5 Per Member. This is the Costco-exclusive bundle — NOT the Target/Best Buy "Xplorer Pro Bundle" (Pro grip, no card) and NOT the Best Buy "Octa Edition" (see Flag).
- **Why it qualifies:** Mainstream Insta360 flagship action camera (8K, Leica optics, 1/1.3" sensor); Costco retailer-direct row with contents fully pinned. Bundle composition is unambiguous, so the brief's DROP condition (unclear contents) does not trigger.
- **Identifiers:** MPN — **PENDING, no lead.** Costco lists only the model name "Ace Pro 2 Xplorer Bundle" and Item 9536006 (a Costco item number, not a manufacturer MPN); Newegg repeats "MPN: 9536006", which is the same Costco number, not an Insta360 MPN. The base camera MPN CINSBBGA belongs to the camera alone, not this bundle — do not attach it. UPC — **PENDING + weak lead 6977644766460** (13-digit EAN; Newegg listing for the "Xplorer Dual Battery … with 128GB Card" bundle only, and that Newegg page is a third-party-seller bundle — single weak source; no second source found).
- **Price / stock:** Costco **$389.99**, "Available", "While supplies last" (Costco.com crawl 9 days old; a second crawl showed OutOfStock, so re-check stock at add time). Costco membership required to buy — flag for the coordinator (Costco is retailer-direct, but gated).
- **Flag — brief's numbers are stale, do not carry them:** the brief says Costco $309.99 (list $339.99). The $309.99 was a Slickdeals thread from 2026-06-23 (valid through 7/5/26, expired); other Slickdeals threads show $329.99 (2026-03-16, valid 3/16–3/31/26; and 2026-05-16, valid through 5/26/26) and $379.99 (2025-10-06, valid until 10/16/25). Current Costco price is $389.99; no current $309.99/$339.99 figures exist. Do NOT mix with: Best Buy "Ace Pro2 Xplorer Bundle Octa Edition" (Model ACEPRO2140, SKU 6665553, $359.99 Black Friday, comp $449.99) — a different bundle/edition; Target "Xplorer Pro Bundle" UPC 842126120657 — a different bundle; Best Buy SKU 13265746 "Dual Battery Xplorer Bundle, Slate Gray" $479.99 — sold/shipped by Adorama (marketplace), not a direct row.
- **Deal-site evidence:** Slickdeals Tech — threads 2026-06-23 ($309.99, expired 7/5/26), 2026-05-16 ($329.99), 2026-03-16 ($329.99), 2025-10-06 ($379.99). All expired; current deal evidence is stale. Saves counts not captured.

### 7. Lenovo Yoga 7i 2-in-1 16" — Luna Grey (83JT0000US) [KEEP, MPN VERIFIED / UPC PENDING]

- **Key:** `lenovo-yoga-7i-2-in-1-16-gen-10-luna-grey`
- **Category:** laptops
- **Variant pinned:** Luna Grey, **83JT0000US** — Yoga 7i 2-in-1 Gen 10 (16" Intel), Intel Core Ultra 5 226V (Series 2), 16GB, 512GB SSD, 16" WUXGA 1920×1200 IPS touch, Win 11 Home, Copilot+ PC. (Per lenovo.com product page 83jt0000us + Best Buy model field + Newegg "Yoga 7 16ILL10, Part Number 83JT0000US, Ultra 5 226V".)
- **Why it qualifies:** Mainstream Lenovo convertible; Best Buy direct Black Friday Doorbuster row + lenovo.com in-stock row. MPN two-sourced (three, counting Newegg).
- **Identifiers:** MPN 83JT0000US — **VERIFIED** (lenovo.com product page, $899.99 InStock + Best Buy model field, SKU 6615769 + Newegg model number). UPC 198155420948 — **PENDING + lead** (Slickdeals thread + eBay listings agree — both non-qualifying; the Best Buy spec panel did not reproduce the UPC in the live page open, so no qualifying second source yet).
- **Price / stock:** Best Buy **$649.99** Doorbuster, sold by Best Buy, InStock (JSON-LD), comp value $999.99, SKU 6615769, page opened live 2026-11-21. Black Friday ends **Nov 28, 2026**. lenovo.com $899.99 InStock as the non-promo reference.
- **Flag — twin-config trap, the most important flag in this track:** Best Buy lists a SECOND Yoga 7i at the same $649.99 — **83TE0004US** (2026 model, Intel Core Ultra 5 322 Series 3, 16GB/512GB, Luna Grey, SKU 6672158, list $1,649.99, Holiday Deal $649.99; Slickdeals thread 2026-11-19). The two configs are different generations with different CPUs and different list prices. The brief's "原价 $899.99" matches 83JT0000US (lenovo.com $899.99), NOT 83TE0004US ($1,649.99) — so 83JT0000US is the pinned config. Do not mix the two, and do not attach the 83TE0004US price history to 83JT0000US. Also ignore marketplace/refurb SKUs for this model (e.g. SKU 13168212 JW Tech LLC, SKU 13199730/13263455 refurbished, $579.99–$949.99).
- **Deal-site evidence:** DealMoon (brief-asserted; not independently re-verified). Independently confirmed: DealNews 2026-11-19, "Lenovo Yoga 7i Core Ultra 5 16\" 2-in-1 Touchscreen Laptop: $650 — 83JT0000US", Best Buy Black Friday Doorbuster, "best price we've seen", expires 11/28/2026; Slickdeals threads 2026-11-10 and 2026-11-19 for 83JT0000US at $649.99 (UPC 198155420948 printed in-thread). Dual-source deal evidence for the pinned config. Saves counts not captured.

### 8. Lenovo Legion 5a 15.3" — Eclipse Black (83Q70068US) [KEEP, both identifiers VERIFIED]

- **Key:** `lenovo-legion-5a-15-3-eclipse-black`
- **Category:** laptops
- **Variant pinned:** Eclipse Black, **83Q70068US** — Legion 5a Gen 11, AMD Ryzen 7 250 (8-core, 3.3–5.1 GHz), NVIDIA GeForce RTX 5060 8GB GDDR7 (115W TGP), 16GB DDR5 (1×16GB, 2 slots, up to 32GB), 512GB M.2 NVMe SSD, 15.3" WQXGA 2560×1600 OLED 165Hz, Win 11 Home, Wi-Fi 7. (Per B&H product page + Slickdeals spec list + Target listing.)
- **Why it qualifies:** Mainstream 2026 Legion gaming laptop; B&H direct in-stock row with the largest holiday cut in this track. Both identifiers VERIFIED — the strongest laptop in this track.
- **Identifiers:** MPN 83Q70068US — **VERIFIED** (B&H "MFR # 83Q70068US", BH # LE83Q70068US + Target "Model name: 83Q70068US" + Slickdeals thread naming 83Q70068US). UPC 199276132093 — **VERIFIED** (B&H spec page "UPC: 199276132093" + Target UPC field 199276132093 + MyNavyExchange "UPC 199276132093 / Model 83Q70068US" — three agreeing sources).
- **Price / stock:** B&H **$1,249.99** In Stock (was $1,799.99, Holiday Savings $550.00), Add to Cart, free delivery Tue Nov 24, page crawls 1 day old; B&H flags "Limited supply at this price". Target lists the same config at $1,399.99 (reg $1,799.99) as the non-promo reference.
- **Flag:** Do not mix with sibling config **83Q70003US** (same Ryzen 7 250 / RTX 5060 / 16GB but **1TB** SSD, also $1,249 at Walmart in a July 2026 Slickdeals thread) — different MPN, different storage. The B&H row is a Holiday Savings price with no stated end date — re-check at add time.
- **Deal-site evidence:** Slickdeals thread 2026-11-17, "Lenovo Legion 5a Gaming Laptop: Ryzen 7 250, 15.3\" OLED, 16GB DDR5, RTX 5060 — $1249.99", B&H, free S&H. Single-source (Slickdeals) deal evidence; saves count not captured.

### 9. ASUS Zenbook A14 UX3407QA-PS76 — Iceland Gray [KEEP, MPN VERIFIED / UPC PENDING] — 队列顶位

- **Key:** `asus-zenbook-a14-ux3407qa-ps76-iceland-gray`
- **Category:** laptops
- **Variant pinned:** Iceland Gray, **UX3407QA-PS76** — Qualcomm Snapdragon X (X1-26-100), 32GB LPDDR5X, 1TB PCIe 4.0 SSD, 14" WUXGA 1920×1200 OLED 60Hz 600-nit, Win 11 Home, 70Wh, 2.18 lb. (Per ASUS press release spec table + ASUS Store + Best Buy.) This is the batch-6 alternate, re-checked live 2026-11-21.
- **Why it qualifies:** ASUS's lightest Copilot+ PC (launch Jan 2025, still current); Best Buy direct row confirmed live at the brief's price. MPN VERIFIED.
- **Identifiers:** MPN UX3407QA-PS76 — **VERIFIED** (ASUS US press release, spec table "Model UX3407QA-PS76" + ASUS Store product page, Part Number 90NB1502-M00FM0 + Best Buy model field, SKU 6616965). UPC 197105832077 — **PENDING + lead** (laptoparena.net "EAN/UPC code 0197105832077, 197105832077" only — spec aggregator, single source, non-qualifying; no retailer spec page prints it).
- **Price / stock:** Best Buy **$1,199.99** (comp $1,599.99), sold by Best Buy, Add to Cart, InStock (JSON-LD), SKU 6616965, page opened live 2026-11-21. ASUS Store lists the same config at $1,599.99. The batch-6 alternate's "$1,199.99 direct" claim is confirmed live.
- **Flag:** Ignore the Best Buy "Upgraded" bundles carrying this model number (SKU 12927567 $2,099.00 with 4TB SSD + dock; SKU 12939083 $1,579 with 1TB dock set) — third-party-modified, not the direct row. Do not mix with the Zabriskie Beige sibling UX3407QA-X1P512 (16GB/512GB, Snapdragon X Plus) or with ASUS part suffix 90NB1502-M00Z60 seen on overseas resellers (different region/config).
- **Deal-site evidence:** None — **队列顶位** (batch-6 backlog alternate, not a deal-site gap). No Slickdeals/DealMoon thread cited or found for this model in-session.

### 10. HP OmniBook 3 14 hz0788dx — Nouvelle Silver [KEEP, MPN VERIFIED with caveat / UPC PENDING] — 队列顶位

- **Key:** `hp-omnibook-3-14-hz0788dx-nouvelle-silver`
- **Category:** laptops
- **Variant pinned:** Nouvelle Silver, **14-hz0788dx / DM2Z9UA#ABA** — Snapdragon X X1-26-100 (8-core), Qualcomm Hexagon NPU 45 TOPS, 16GB, 512GB PCIe Gen4 NVMe SSD, 14" 2K (1920×1200) OLED UWVA, Win 11 Home, Copilot+ PC, 41h45m video playback, 3.13 lb. (Per Best Buy model field + HP datasheet PDF.) This is the batch-6 alternate, re-checked live 2026-11-21.
- **Why it qualifies:** Mainstream HP Copilot+ laptop; Best Buy direct Black Friday row confirmed live at the brief's price.
- **Identifiers:** MPN 14-hz0788dx / DM2Z9UA#ABA — **VERIFIED with caveat** (Best Buy model field "14-hz0788dx/DM2Z9UA#ABA", SKU 6679357 + HP's own datasheet PDF "HP OmniBook 3 14 inch Laptop Next Gen AI PC 14-hz0788dx", hosted on Best Buy's static file server files.bbystatic.com — the content is verbatim HP, but the host is not hp.com; same caveat shape as the batch-6 Brio 100 acceptance. A direct hp.com product-page re-check at add time would remove the caveat.) UPC — **PENDING, no lead.** No qualifying (or non-qualifying) UPC surfaced in any search.
- **Price / stock:** Best Buy **$599.99** Black Friday (comp $799.99, save $200), sold by Best Buy, Add to Cart, InStock (JSON-LD), SKU 6679357, page opened live 2026-11-21. Black Friday ends **Nov 28, 2026**. A second Best Buy SKU for the same model (13225916) shows $689.90 — use SKU 6679357 at $599.99.
- **Flag:** Do not mix with the Starlit Blue 8GB/256GB OmniBook 3 sibling ($399.99) or the 256GB Nouvelle Silver variant — different configs. The OLED-vs-UWVA wording conflict on the Best Buy page is resolved by HP's datasheet (2K OLED panel; UWVA is the viewing-angle technology).
- **Deal-site evidence:** None — **队列顶位** (batch-6 backlog alternate, not a deal-site gap). No Slickdeals/DealMoon thread cited or found for this model in-session. (A 2026-11-12 social post notes the same $599 Best Buy price.)

## Summary table

| # | Model | Verdict | MPN | UPC | Direct row (2026-11-21) |
|---|---|---|---|---|---|
| 1 | DJI Osmo Action 4 Essential Combo | KEEP | PENDING (no lead) | PENDING + lead 190021133402 (non-qual only) | DJI US $169.00 (was $229) |
| 2 | GoPro LIT Hero 4K60 | KEEP | VERIFIED CHDHF-132-AT | VERIFIED 810116384129 | Best Buy $269.99 InStock; B&H $269.99 |
| 3 | DJI Osmo Action 6 Essential Combo | KEEP | PENDING (no lead) | PENDING + lead 190021161696 (non-qual only) | DJI US $426.00 |
| 4 | DJI Osmo Pocket 3 Creator Combo | KEEP | VERIFIED CP.OS.00000302.01 | VERIFIED 190021095007 | B&H $466.00 InStock (was $549) |
| 5 | DJI Osmo 360 Skiing Combo | **DROP** | No lead | Non-qual lead only (Amazon 190021996731) | DJI US $618.99 **OutOfStock** — no row |
| 6 | Insta360 Ace Pro 2 Xplorer (Costco) | KEEP | PENDING (no lead) | PENDING + weak lead 6977644766460 | Costco $389.99 (membership; re-check stock) |
| 7 | Lenovo Yoga 7i 16" 83JT0000US | KEEP | VERIFIED 83JT0000US | PENDING + lead 198155420948 (non-qual only) | Best Buy $649.99 BF InStock (ends 11/28) |
| 8 | Lenovo Legion 5a 83Q70068US | KEEP | VERIFIED 83Q70068US | VERIFIED 199276132093 | B&H $1,249.99 InStock (was $1,799.99) |
| 9 | ASUS Zenbook A14 UX3407QA-PS76 | KEEP | VERIFIED UX3407QA-PS76 | PENDING + lead 197105832077 (non-qual only) | Best Buy $1,199.99 InStock, direct |
| 10 | HP OmniBook 3 14-hz0788dx | KEEP | VERIFIED w/ caveat 14-hz0788dx / DM2Z9UA#ABA | PENDING (no lead) | Best Buy $599.99 BF InStock (ends 11/28) |

## Notes for the coordinator

- **No gap-filling was done for the DROP (item 5).** The Standard Combo substitute is noted in item 5 only as a possible re-brief, not added.
- **Three brief prices were wrong or stale and must not be carried:** (1) Action 4's $155.35 and (3) Action 6's $376 are Amazon-only — the direct rows are $169.00 and $426.00. (6) Insta360's $309.99/$339.99 is a June 2026 expired Slickdeals price — current Costco price is $389.99. (2) GoPro's $169.99 is likewise Amazon-only; the direct price is the $269.99 list.
- **Re-check at add time (per skill):** Action 4 Essential DJI stock wording; Action 6 Essential DJI stock wording; Insta360 Costco stock (one crawl showed OutOfStock); Yoga 7i UPC 198155420948 on a qualifying spec page (Best Buy "See all specifications" panel); OmniBook 3 MPN on hp.com to clear the datasheet-host caveat; Zenbook A14 UPC 197105832077 on a second source; Legion 5a "Limited supply" B&H price.
- **Deal-site evidence limits, stated honestly:** saves counts were not captured for any thread in this session. DealMoon threads for items 1, 3, 4, 5, 7 are brief-asserted and were not independently re-opened; Slickdeals threads were independently confirmed for items 1, 6, 7, 8 (with dates in the entries above). Items 9–10 are queue-top items with no deal-site evidence, as briefed.
- **New category needed:** `action-cameras` (items 1, 2, 3, 6; item 5 if ever revived). Pocket 3 (item 4) is proposed as `cameras` — coordinator to confirm the category split.
