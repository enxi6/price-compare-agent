# Track C — Batch-6 Rework Findings (Samsung / Apple / ASUS / HP / Dell / Microsoft / Meta / Google / Keychron / HyperX / Corsair / Bose)

- Date: 2026-11-20 (all observations via `browser.search` / `browser.open`, text fetch only)
- Draft: `data/candidates_batch6_500.md` (50 candidates, catalog 450 → 500)
- Scope note (method pivot, 2026-11-20): Lenovo items 14, 15, 16 (ThinkPad X1 Carbon Gen 13, Legion Pro 5 16IRX9, ThinkPad T14 Gen 6) are EXCLUDED from this track — a dedicated Lenovo.com sweep track now covers all Lenovo systematically. This file covers the remaining 23 models only (draft entries 1–13, 17–26).

## Rules applied
- US-market models only; seller-direct or retailer-direct only; no Amazon in any form; no eBay; no marketplace / third-party sellers.
- Identifier VERIFIED only when TWO independent qualifying sources agree on the code for the exact model/variant. Qualifying: B&H spec page, Abt spec page, Micro Center spec, Crutchfield, Newegg spec page, brand official site/spec, authorized distributor spec. NOT qualifying: Amazon, eBay, aggregators (Snapklik, Desertcart, Ubuy, etc.), price-tag photos, Q&A pages, search snippets alone. A single retailer spec page is NOT enough. Nothing invented.
- Same-brand-family corroboration (e.g. hp.com datasheet + hp.com product page; keychron.com + keychron regional stores) is flagged as such and does NOT upgrade a verdict to VERIFIED on its own.
- Manufacturer datasheets (HP datasheet, Dell datasheet) are treated as brand spec even when hosted on a mirror (files.bbystatic.com, Icecat); the hosting is always stated so the verdict can be re-judged.
- Distributor specs (ADI Global Distribution, Zoro, Ferguson) are treated as "authorized distributor spec" where they print full identifiers; the distributor nature is always stated.

---

## 1. Samsung SmartTag 2 Black — MPN EI-T5600BBEGUS
- **Best Buy** (model field): Model EI-T5600BBEGUS; $25.00 (comp $29.99); promo-sensitive $25–$26.93; one crawl says "no longer available in new condition".
- **Micro Center** (spec page): "Samsung Galaxy SmartTag2 EI-T5600BBEGUS", SKU 715300, Mfr Part# EI-T5600BBEGUS, UPC 887276765358, Color Black.
- **NFM (Nebraska Furniture Mart)** (not on the qualifying list): SKU# 65045197, UPC 887276765358, Model EI-T5600BBEGUS, $29.99, Not Currently Available.
- **Verdicts:** MPN **VERIFIED** (Best Buy + Micro Center). UPC **PENDING + lead 887276765358** (Micro Center only qualifying; NFM agrees but is outside the qualifying list).
- **Price/stock:** Best Buy $25.00.

## 2. Samsung HW-Q800F Black — MPN HW-Q800F/ZA
- **Crutchfield** (page opened 2026-11-20): Item # 305HWQ800F, MFR # HW-Q800F/ZA, $1,097.99, In stock. A `browser.find` for "UPC" on this page returned no match — Crutchfield prints no UPC.
- **B&H** (page opened 2026-11-20): HW-Q800F 5.1.2-Channel Dolby Atmos Soundbar System, UPC 887276934242, $1,097.99, In Stock.
- **ADI Global Distribution** (distributor spec): "Samsung HW-Q800F/ZA Q Series 5.1.2-Channel Soundbar with Subwoofer", UPC Code 887276934242.
- **Walts** (not on the qualifying list): Model HW-Q800F, MPN HW-Q800F/ZA, UPC 887276934242.
- **Verdicts:** MPN **VERIFIED** (Crutchfield + B&H, plus Best Buy). UPC **VERIFIED** (B&H + ADI Global Distribution) — 887276934242. Note the second source is a distributor listing, not a core retailer.
- **Price/stock:** $1,097.99 (B&H, Crutchfield, In Stock); Best Buy list $1,099.99.

## 3. Samsung HW-QS700F Black — MPN HW-QS700F/ZA
- **B&H** (page opened 2026-11-20): BH # SAHWQS700F, MFR # HW-QS700F/ZA, $597.99 (was $797.99, Holiday Savings $200), In Stock, UPC 887276934273.
- **Abt** (page opened 2026-11-20): "Samsung HW-QS700F/ZA Q Series Soundbar 3.1.2 Channel with Subwoofer", $597.99, "Price includes manufacturer rebate which ends 11/22/2026", Comp. Value $797.99, InStock. No UPC printed on the Abt page.
- **SHI** (authorized distributor): Mfr Part # HW-QS700F/ZA, $704.00, stock 17, MSRP $799.99.
- **ADI Global Distribution** (distributor spec): "Samsung HW-QS700F/ZA Q Series 3.1.2.-Channel Dolby Soundbar", UPC Code 887276934273.
- **Datavision / Worldwide Stereo** (not on the qualifying list): both print MFR HW-QS700F/ZA + UPC 887276934273, $597.99.
- **Verdicts:** MPN **VERIFIED** (B&H + Abt + SHI). UPC **VERIFIED** (B&H + ADI Global Distribution) — 887276934273. Note the second source is a distributor listing.
- **Price/stock:** $597.99 (B&H, Abt, InStock); Best Buy $347.99 Black Friday (ends Nov 28, 2026) per draft; Crutchfield $597.99 per draft.

## 4. Samsung Odyssey G5 G55H 27" Black — MPN LS27HG552ENXZA, SKU 6685398
- **Best Buy** (only qualifying source found): Model LS27HG552ENXZA, SKU 6685398, Sold by Best Buy, $299.99 list / $149.99 Black Friday in different crawls; open-box $281.99–$290.99.
- **Samsung US official page**: names the same G55H 27" QHD 180Hz curved monitor but with code **LS27HG550ENXZA**, $249.99 — **suffix conflict (550 vs 552)**. Do not treat them as the same code.
- No B&H / Newegg hit. G50D flat IPS is a different variant — do not mix.
- **Verdicts:** MPN **PENDING** (Best Buy only; Samsung official gives a different code). UPC **NO LEAD**.
- **Price/stock:** Best Buy $299.99 list / $149.99 Black Friday.

## 5. Apple 140W USB-C Power Adapter White — MPN MKFQ4AM/A, SKU 6530838
- **Best Buy** (model field): MKFQ4AM/A, SKU 6530838.
- **B&H**: BH # APMKFQ4AMA, MFR # MKFQ4AM/A, $99.00. (One B&H category crawl oddly shows "Preorder / New Item - Coming Soon" next to this listing; the product page itself lists $99.00.)
- **Apple.com** (shop product MKFQ4AM/A): 140W Power Adapter, $99.00, InStock.
- **Adorama** (not on the qualifying list): SKU ACMKFQ4AMA, MFR MKFQ4AM/A, $129.00, InStock.
- **Abt**: its 140W page is for the OLD model MLYU3AM/A ("no longer available") but the page body also prints "Model: MKFQ4AM/A, $99".
- Do NOT confuse with MW2M3AM/A (B&H lists it as a 140W adapter with UPC 195949376955 — a different, newer part) or old MLYU3AM/A (UPC 194252750629). Old SKU 6485370 is a different (older) model.
- **Verdicts:** MPN **VERIFIED** (Best Buy + B&H + Apple.com). UPC **NO LEAD** for MKFQ4AM/A — no qualifying source prints a UPC for this part.
- **Price/stock:** $99.00 (Apple.com, B&H, InStock); Adorama $129.00.

## 6. Apple 35W Dual USB-C Compact Adapter White — MPN MW2H3AM/A
- **B&H**: BH # APMW2H3AMA, MFR # MW2H3AM/A, $59.99.
- **Apple.com** (shop product MW2H3AM/A, page opened 2026-11-20): 35W Dual USB-C Port Compact Power Adapter, $59.00, InStock.
- **Micro Center** (spec page): SKU 703462, Mfr Part# MW2H3AM/A, **UPC 195949376535**, Enclosure Color White, 35 Watts.
- **NFM / Datavision** (not on the qualifying list): both print Model MW2H3AM/A + UPC 195949376535 (Datavision $59.00).
- **Correction:** the UPC 195949376573 found on apple.com belongs to the NON-compact MW2K3AM/A, NOT the compact MW2H3AM/A. Compact = 195949376535; non-compact = 195949376573. MW2K3AM/A is the larger non-compact version — pin compact only. (Earlier US part MNWM3AM/A is the legacy compact part number.)
- **Verdicts:** MPN **VERIFIED** (B&H + Apple.com + Micro Center) — supersedes the draft's single non-qualifying source (in-store price-tag photo). UPC **PENDING + lead 195949376535** (Micro Center only qualifying; NFM + Datavision agree but are outside the qualifying list).
- **Price/stock:** $59.00 (Apple.com, InStock); $59.99 (B&H).

## 7. Apple Magic Keyboard for iPad Air 11" (M2) White — MPN MJQJ3LL/A
- **Best Buy** (model field): Model MJQJ3LL/A, $261.99–$262.99 (comp $299.00); new listings **sold & shipped by HHGregg (marketplace)**; Geek Squad Certified Refurbished $149.99; Clearance $119.99 (SKU 6340387 — seller for the clearance listing not verified in the crawls).
- **Newegg** (refurbished listing): Apple Magic Keyboard MJQJ3LL/A White, UPC 194252439067.
- **Apple.com**: price/stock NOT captured — the apple.com shop page for MJQJ3LL/A fetched as a generic Apple navigation page with no product offer. (Apple list price is $299.00 per Best Buy comp value and camelcamelcamel list price.)
- **camelcamelcamel** (not qualifying): ASIN B0931V9M9D, UPC 194252439067, MODEL MJQJ3LL/A, list price $299.00.
- **Important:** MJQJ3LL/A is the older Magic Keyboard for iPad Pro 11" (1st–4th gen) and iPad Air (4th/5th gen), not an M2-exclusive keyboard. Best Buy's own spec lists compatibility with iPad Air (M2) 11 and iPad Air (M3) 11.
- **Verdicts:** MPN **VERIFIED** (Best Buy + Newegg — note the Newegg listing is refurbished). UPC **PENDING + lead 194252439067** (Newegg only qualifying; camelcamelcamel/eBay agree but are not qualifying).
- **Price/stock:** Best Buy marketplace new $261.99–$262.99; refurbished $149.99; clearance $119.99 (seller unverified). Apple.com price/stock NOT captured.
- **Retailer-direct row: NO** — no clean Best Buy-direct new row found (marketplace new + refurbished + unverified clearance only); no B&H/Adorama direct row found.

## 8. ASUS ROG Falchion Ace HFX Black — MPN ROG FALCHION ACE M605
- **ASUS eShop USA**: Product Name "M605 ROG FALCHION ACE HFX/HFX/CA/PBT", Part Number 90MP03VE-BKAA23, $199.99, Black. ROG site: $199.99.
- **Newegg** (product page opened 2026-11-20, N82E16823193158): standard Black HFX, 65% compact, ROG HFX magnetic switches, 8000 Hz — but the fetched page text contains only overview/FAQ; the Specs tab (MPN/part number/UPC) was not in the extracted text, so Newegg does NOT confirm the part number here.
- **Slickdeals**: Newegg $129.99, $94.99 with promo code BFEFE58 starting Nov 20 (expired-deal note in the crawl).
- ZywOo edition M606 is a different variant — pin standard Black M605 only.
- **Verdicts:** MPN **PENDING + lead M605 / part 90MP03VE-BKAA23** (ASUS official only; Newegg page opened but its spec table was not captured). UPC **NO LEAD**.
- **Price/stock:** ASUS eShop $199.99; Newegg $129.99 list ($94.99 with promo per Slickdeals).

## 9. ASUS ZenWiFi AXE7800 3-pack White — MPN ZenWiFi AXE7800
- **ASUS eShop / asus.com**: Model Name AXE7800 (W-3-PK), $299.99, InStock. (ASUS tech-spec page: Model ASUS ZenWiFi AXE7800, Model Name AXE7800 (W-3-PK); the hardware is also sold as ZenWiFi ET9 — the retail 3-pack is AXE7800 (W-3-PK).)
- **Newegg** (spec page): Part Number 90IG07D0-MA1A2V, Model # ZenWiFi AXE7800, 3-Pack, $329.99.
- **B&H**: NO AXE7800 (ET9) listing found. B&H carries the ZenWiFi XT9 (different model, 2-pack, No Longer Available) and RT-AXE7800 (different model, No Longer Available) — do not mix.
- **Best Buy**: the current listing is sold/shipped by **Newegg Official (marketplace)** at $356.49 — NOT Best Buy direct. The draft's $302.49 Best Buy-direct row no longer holds.
- **Verdicts:** MPN **VERIFIED** (ASUS official + Newegg). UPC **NO LEAD** (qualifying); eBay GTIN 0197105421790 is not qualifying.
- **Price/stock:** ASUS $299.99 InStock; Newegg $329.99; Best Buy now marketplace-only $356.49.

## 10. HP Victus 15 (15-fb3093dx) Mica Silver — MPN 15-fb3093dx / BM4X8UA#ABA, SKU 6623881
- **Best Buy** (model field): 15-fb3093dx/BM4X8UA#ABA, SKU 6623881.
- **HP datasheet** (files.bbystatic.com, HP document): "Victus by HP 15.6 inch Gaming Laptop PC 15-fb3093dx", Product number BM4X8UA#ABA, UPC Code 199251266874.
- **eBay** (excluded): also prints MPN 15-fb3093dx/BM4X8UA#ABA + UPC 199251266874 — does not count.
- **Verdicts:** MPN **VERIFIED** (Best Buy + HP datasheet). UPC **PENDING + lead 199251266874** (HP datasheet only — needs a second qualifying source).
- **Price/stock:** Best Buy $949.99 Holiday Deal per draft; a $639.99 snippet exists (possibly an older deal).

## 11. HP 430 Multi-Device Wireless Mouse Black — no lead in draft
- **HP.com official datasheet** (hp.com): Product number 3B4Q2AA; UPC number (ABB) 195908246558; (ABL) 195908246565; (UUF) 195908246572; Product color Jet black.
- **HP.com US product page**: HP 430 Multi-Device Wireless Mouse (3B4Q2AA#ABL), Product # 3B4Q2AA#ABL, $48.99.
- **Best Buy** listing SKU 10949983: HP 430 Multi-Device Wireless Mouse, $28.99 (comp $48.99), sold & shipped by **HP Inc** (not Best Buy direct). Best Buy model field / spec-page UPC NOT confirmed in this round.
- **Target**: $48.99, sold & shipped by HP Official Store.
- **Verdicts:** MPN **PENDING + lead 3B4Q2AA** (HP datasheet + hp.com product page — same brand family only; no second independent qualifying source yet). UPC **PENDING + lead 195908246565** for the US #ABL variant (HP datasheet only).
- **Price/stock:** HP.com $48.99; Best Buy via HP Inc $28.99.

## 12. Dell XPS 14 9440 Platinum — config XPS9440-7816SLV-PUS
- **Best Buy** product page SKU 6586149, Model XPS9440-7816SLV-PUS: "This item is no longer available in new condition." Best Buy Q&A page price $1,199.99. Open-box prices $570.99–$645.99 are for a different OLED config (XPS9440-7892SLV-PUS), not this config.
- **Dell datasheet** (via Icecat, manufacturer document): Brand DELL, Article code XPS9440-7816SLV-PUS, XPS 14 9440, Intel Core Ultra 7 155H, 14.5" Full HD+ 1920x1200, 16 GB LPDDR5x, 1 TB SSD, Windows 11 Home, Silver; UPC/EAN 884116470816. (Color note: draft title says "Platinum"; the datasheet says Silver — Dell's Platinum is the silver finish.)
- No dell.com price found for this config in search.
- **Verdicts:** MPN **VERIFIED** (Best Buy product page + Dell datasheet — note the datasheet was read via Icecat hosting). UPC **PENDING + lead 884116470816** (Dell datasheet only — needs a second qualifying source).
- **Price/stock:** No new product-page price — the pinned config is not available new at Best Buy (Q&A $1,199.99 only).

## 13. Dell G16 7630 Gray — exact config RTX 4070 / i9-13900HX / 32GB / 1TB
- **Dell.com** (Dell USA product page, crawls 88 and 135 days old): "Dell G16 Gaming Laptop", Order Code **useghbto7630glmf** $1,959.99 and Order Code **useghbto7630fwmg** $1,949.99; Tech Specs on both: 13th Gen Intel Core i9-13900HX, NVIDIA GeForce RTX 4070 8GB GDDR6, 32 GB (2 x 16 GB) DDR5 4800 MT/s, 1 TB SSD, 16" QHD+ — the exact pinned config. **Correction to the earlier read: Dell.com DOES still list this config; the "discontinued at Dell" conclusion is withdrawn.** Prices are from stale crawls — re-verify the current price at add time.
- **Icecat** (Dell datasheet mirror, not qualifying): Article code **CN76154**, DELL G16 7630, i9-13900HX, 32 GB, 1 TB, RTX 4070, QHD+, Windows 11 Home, color Black ("Zwart") — a different code format from Dell's order codes; color shown as Black vs the draft's Gray (G16's dark finish is Metallic Night — treat color naming as unverified).
- **Slickdeals** (not qualifying, older): $1,299.99 / $1,170.99 with 10% sign-up code (Mar 2025 / Feb 2025 posts) — historical only.
- **Best Buy**: only an "Upgraded" third-party config at $2,879 per draft — not usable.
- **Verdicts:** MPN **PENDING + lead (Dell order codes useghbto7630glmf / useghbto7630fwmg)** — no single MPN; two order codes seen for the same spec (likely differing in minor config options); Icecat CN76154 is a different code format and not a second source for the same code. UPC **NO LEAD**.
- **Price/stock:** Dell.com $1,949.99–$1,959.99 (stale crawls — re-verify).
- **Retailer-direct row: YES** — Dell.com direct row exists for the exact pinned config (price to be re-verified at add time).

## 17. Microsoft Surface Thunderbolt 4 Dock Black — no lead in draft
- **B&H**: Microsoft Surface Thunderbolt 4 Dock for Business, T8I-00001, UPC 196388142200.
- **Newegg** (spec page): Microsoft Surface Thunderbolt 4 Dock for Business, Part Number T8I-00001, Model # T8I-00001, $251.99 range.
- **Best Buy**: Model T8I-00001, SKU 11149146 / 12476006.
- **Zoro** (distributor spec): Mfr # T8I-00001, UPC # 196388142200, $272.99.
- **Target** (Target Plus partner-supplied, weaker): also prints Model T8I-00001, UPC 196388142200.
- **Verdicts:** MPN **VERIFIED** (B&H + Newegg + Best Buy). UPC **VERIFIED** (B&H + Zoro) — 196388142200.
- **Price/stock:** Best Buy $299.99 per draft (one crawl $214.99 promo); Newegg ~$251.99; Zoro $272.99.

## 18. Meta Oakley Vanguard White (Prizm Black lenses) — no lead in draft
- **Abt** (customer-reviews page): Oakley Meta Vanguard Sunglasses 52mm in White with Prizm Black Lenses — OW8001800105, Model # OW8001800105, UPC # 888392690388.
- **Best Buy**: Oakley Meta Vanguard, Prizm Black lenses, White, Model **0OW8001 3928 46**, SKU 6643077.
- **Meta.com** (brand official): "Buy Oakley Meta Vanguard - White with Prizm™ Black Lenses", $499 list / **$424.15 Black Friday** (was $499), InStock. No model code printed on the Meta page.
- **EU retailers** (not qualifying, but convergent): bike24 "Oakley Meta Vanguard Glasses - White/Prizm Black - OW8001-0552"; eye-oo "Vanguard Meta OW8001 05 Prizm Black", $740.00; scopelist "OW8001-05"; alltricks "Ref: OW8001-05"; shadestation "OW8001-05 52", White / Prizm Black. (52 = 52mm lens width.)
- **o-review database** (not qualifying): Meta Vanguard White / Prizm Black, SKU OW8001-0552, UPC 888392690388, $499.
- **CONFLICT unresolved:** OW8001800105 (Abt) vs 0OW8001 3928 46 (Best Buy) vs OW8001-05 / OW8001-0552 (EU retailers + o-review). The Abt code looks like a concatenation/mangling; the EU "OW8001-05 52" form is the most widely repeated but no qualifying source prints it. Do not pick one yet.
- **Verdicts:** MPN **NOT VERIFIED (conflict)**. UPC **PENDING + lead 888392690388** (Abt reviews page only qualifying; o-review agrees but is not qualifying).
- **Price/stock:** Meta.com $499 list / $424.15 Black Friday; Best Buy $424.00 Black Friday (comp $499.00) per draft.

## 19. Meta Ray-Ban Skyler Gen 2 Green / Shiny Black — MPN lead 0RW4014_601/7152
- **Best Buy** (product page, SKU 6642578): "Ray-Ban Meta - Skyler (Gen 2) glasses … Green lenses - Shiny Black", **Model: 0RW4014_601/7152**, **Sold by Best Buy**, $379.00, InStock (one crawl shows $284 — likely a promo variation; list is $379.00).
- **Meta.com** (brand official): Ray-Ban Meta Skyler (Gen 2), Shiny Black frame, Green lenses, $379, InStock. No model code printed.
- **Bonanza** (marketplace, not qualifying): prints MPN 0RW4014_601/7152 for Shiny Black / G-15 Green.
- **Swappa** (marketplace): RW4014 601/71. **specifications.global** (aggregator): RW4014 601/71 52-20, G-15 Green, $379.
- The Transitions Green variant is a DIFFERENT model: Best Buy Model **0RW4014_601/1M52**, SKU 6642596, Sold by Best Buy, $459.00. Abt carries only the Transitions variant (RW4014-6011M52, $459).
- **Verdicts:** MPN **PENDING + lead 0RW4014_601/7152** (Best Buy product page only qualifying — upgraded from Q&A-only, but still a single qualifying source; meta.com does not print the code). UPC **NO LEAD**.
- **Price/stock:** Best Buy $379.00 InStock, Sold by Best Buy; Meta.com $379 InStock.

## 20. Google Nest Hub (2nd Gen) Charcoal — MPN GA01892-US
- **Best Buy** (model field): GA01892-US.
- **Abt**: Google GA01892-US Charcoal Nest Hub (2nd Gen) — "Sorry, this item is no longer available" (page still names the model for Charcoal).
- **Ferguson** (distributor spec): "Google Nest Hub (2nd gen) - Charcoal", Part #GGA01892US, Manufacturer Part #GA01892-US, UPC 193575009223, $105.90, OutOfStock.
- **Zoro** (distributor spec): "Google Nest Google Nest HUB Smart Home Assistant - Charcoal GA01892-US", MFR # GA01892-US, UPC # 193575009223.
- **Google Store**: Nest Hub (2nd gen), $99.99.
- **B&H**: B&H # GONHUB2C, MFR # GA01892-US (seen via a DealMoon snippet — the B&H page itself was not opened; no B&H price/stock captured).
- **Verdicts:** MPN **VERIFIED** (Best Buy + Abt + Ferguson + Zoro). UPC **VERIFIED** (Ferguson + Zoro) — 193575009223. Note: both UPC sources are distributor specs; no core retailer (B&H/Abt/Newegg/Crutchfield) printed the UPC.
- **Price/stock:** Google Store $99.99; Ferguson $105.90 OutOfStock.

## 21. Keychron K11 Max Black (Alice) — no lead in draft
- **Keychron.com** (official): Keychron K11 Max (Alice Layout), SKU K11M-A1, $89.99, header says "Sold out"; variant table shows Black / PixArt 3395 (4K) $59.99, Black / PixArt 3395 (1K) RGB $49.99, Black / PixArt 3950 (8K) $59.99 and sold-out variants. Variant/price ambiguity: the $89.99 list price attaches to a sold-out configuration while cheaper in-stock Black variants exist at $49.99/$59.99.
- **Keychron.be** (Keychron EU store): SKU K11M-A1, €109.99. (Same brand family — does not count as an independent second source.)
- **B&H**: Keychron brand page exists but no K11 Max listing / MPN / price identified on it.
- **bulsuk.com** (review blog, Aug 2026 availability update, not qualifying): "Keychron has quietly retired both the K11 Pro and the K11 Max. Neither is sold new by Keychron any more. Its successor, the K15 Max…" — flag for add time: the model may be discontinued; successor is K15 Max.
- **Tom's Guide**: "starts at $94 … from Keychron only" (older review).
- Lookalike domains keychroncompany.us and keychron-shop.us ($35–$43) are NOT official — do not use.
- **Verdicts:** MPN **PENDING + lead K11M-A1** (Keychron family only). UPC **NO LEAD**.
- **Price/stock:** Keychron.com $89.99 list, sold-out header; in-stock Black variants $49.99/$59.99.
- **Retailer-direct row: NO** — no B&H or other US retailer direct row found.

## 22. Keychron Q0 Max Carbon Black — MPN Q0M-M1 (Keychron's own SKU only)
- **Keychron.com** (official): Keychron Q0 Max QMK Wireless Custom Number Pad, SKU Q0M-M1, $113.99 (was $129.99), extra $10 off code MAX10; Fully Assembled Knob / Carbon Black / Gateron Jupiter Red — Available; Brown out of stock; Banana available. "Stocked in the US warehouse."
- **Keychron.ca**: SKU Q0M-M1, CA$189.99, sold out. **Keychron SG**: SKU Q0M-M1, $119 SGD, sold out. **Keychron.es**: SKU Q0M-M1, €139.49 (was €154.99). (All same brand family — do not count as independent second sources.)
- **B&H**: no Q0 Max listing found in search.
- **It is a NUMBER PAD, not a keyboard** — note at add time.
- **Verdicts:** MPN **PENDING + lead Q0M-M1** (Keychron family only; no independent US retailer second source). UPC **NO LEAD**.
- **Price/stock:** Keychron.com $113.99, Carbon Black / Jupiter Red Available.
- **Retailer-direct row: NO** — no US retailer direct row found.

## 23. HyperX Cloud III Wireless Black — MPN 77Z45AA
- **Best Buy** (model field): 77Z45AA.
- **HyperX.com** (brand official, press release): "HyperX Cloud III Wireless Gaming Headset Specifications: Part Number 77Z45AA Black, 77Z46AA Black-Red." Launch price $169.99 via HyperX US Shop.
- **HyperX.com product page**: "HyperX Cloud III Wireless - Discontinued! Shop HyperX Cloud III S Wireless Headset Instead", $149.99, **OutOfStock**. Flag: the model is discontinued at the HyperX US shop.
- **UPC lead (non-qualifying only):** 197029611727 printed with MPN 77Z45AA by shipfreedefense, shop.vb.net, PB Tech NZ, Desertcart — none qualifying. eBay prints a conflicting UPC 786513757593 — ignore (eBay, likely a different bundle).
- **Verdicts:** MPN **VERIFIED** (Best Buy + hyperx.com). UPC **PENDING + lead 197029611727** (no qualifying source at all yet).
- **Price/stock:** HyperX US shop discontinued / OutOfStock $149.99; Best Buy price/stock not re-verified this round.

## 24. HyperX Alloy Origins 60 Black — MPN 4P5N4AA#ABA
- **Best Buy** (model field): 4P5N4AA#ABA.
- **Newegg** (spec page): HyperX Alloy Origins 60, HX Red, US Layout; Brand HP; Model 4P5N4AA; MPN 4P5N4AA#ABA; UPC 196188048948; sold by Official HP Store; price range $69.99–$114.99 in crawls.
- **HP.com** (brand official product page): Product # 4P5N4AA#ABA, "HyperX Alloy Origins 60 - Mechanical Gaming Keyboard - HX Red - US Layout", $114.99, InStock.
- **HP datasheet** (via Icecat, HP document): HyperX Alloy Origins 60 (4P5N4AA), UPC 196188048948. (Also lists 196188048955 / 5704174946502 for other variants — do not mix.)
- Draft also mentions alternate model HKBO1S-RB-US/G (Amazon-derived — do not use as the lead).
- **Verdicts:** MPN **VERIFIED** (Best Buy + Newegg + HP.com). UPC **VERIFIED** (Newegg spec + HP datasheet) — 196188048948. Note the datasheet was read via Icecat hosting.
- **Price/stock:** HP.com $114.99 InStock; Best Buy $77.99–$86.99 per draft.

## 25. Corsair K65 PRO MINI Black (OPX) — no lead in draft
- **Correct US code is CH-91A401A-NA** (NA layout). The guessed code CH-9199114 was wrong — do NOT use it. CH-91A401A-ND is the Nordics layout, a different variant.
- **Best Buy**: CORSAIR K65 PRO MINI RGB 65% Optical-Mechanical, OPX, Black, Model CH-91A401A-NA, SKU 6547466, $149.99; SKU 11085001, $72.98 (comp $149.99).
- **Newegg**: Corsair K65 PRO Mini, Part Number CH-91A401A-NA, Model # CH-91A401A-NA, $109.99+.
- **Corsair.com US**: certified-refurbished NA page exists (CH-91A401A-NA-RF); the new-product NA page was not captured with a US price (CN store shows OutOfStock; EU ND pages are different variants). Corsair direct $79.99 per draft (pricertoday, unverified).
- **UPC lead (non-qualifying only):** 840006698432 (aio.lv prints "MPN CH-91A401A-NA, EAN 840006698432"; camelcamelcamel / Desertcart agree). Corsair's own SKU sheet (littlebit.de PDF) lists only ES/IT variants in the visible excerpt (840006698388 / 840006698401). No B&H listing found.
- **Verdicts:** MPN **VERIFIED** (Best Buy + Newegg). UPC **PENDING + lead 840006698432** (no qualifying source yet).
- **Price/stock:** Best Buy $72.98 promo / $149.99 list; Newegg $109.99+.

## 26. Bose Solo Soundbar Series II Black — MPN 845194-2100 (single source, batch-5 draft)
- **Bose.com**: Bose Solo Soundbar Series II, $199.00 new; certified refurbished also listed. Bose.com pages do not print an MPN or UPC in the fetched text.
- **manuals.plus** (manual PDF, not qualifying): Model Number 845194-2100, UPC 017817827355.
- **Desertcart** (aggregator, not qualifying): UPC 017817827355.
- No B&H / Crutchfield / Abt / Newegg / Costco spec page found printing the MPN or UPC in this round. Costco $212.99 InStock per draft (Costco page not re-checked for identifiers).
- **Verdicts:** MPN **PENDING** (single source — batch-5 draft). UPC **NO LEAD** (qualifying) — 017817827355 is unproven under the rules (manual PDF + aggregator only).
- **Price/stock:** Bose.com $199.00 new.

---

## Tally (23 models; Lenovo items 14–16 excluded per pivot)

| # | Model | MPN | UPC |
|---|---|---|---|
| 1 | Samsung SmartTag 2 | VERIFIED (Best Buy + Micro Center) | PENDING 887276765358 (Micro Center only) |
| 2 | Samsung HW-Q800F | VERIFIED (Crutchfield + B&H) | VERIFIED (B&H + ADI) 887276934242 |
| 3 | Samsung HW-QS700F | VERIFIED (B&H + Abt + SHI) | VERIFIED (B&H + ADI) 887276934273 |
| 4 | Samsung Odyssey G5 G55H | PENDING (Best Buy only; Samsung says LS27HG550ENXZA) | NO LEAD |
| 5 | Apple 140W MKFQ4AM/A | VERIFIED (Best Buy + B&H + Apple.com) | NO LEAD |
| 6 | Apple 35W compact MW2H3AM/A | VERIFIED (B&H + Apple.com + Micro Center) | PENDING 195949376535 (Micro Center only) |
| 7 | Apple Magic Keyboard MJQJ3LL/A | VERIFIED (Best Buy + Newegg refurb) | PENDING 194252439067 (Newegg only) |
| 8 | ASUS Falchion Ace HFX | PENDING M605 / 90MP03VE-BKAA23 (ASUS only) | NO LEAD |
| 9 | ASUS ZenWiFi AXE7800 | VERIFIED (ASUS + Newegg) | NO LEAD |
| 10 | HP Victus 15 | VERIFIED (Best Buy + HP datasheet) | PENDING 199251266874 (HP datasheet only) |
| 11 | HP 430 mouse | PENDING 3B4Q2AA (HP family only) | PENDING 195908246565 #ABL (HP datasheet only) |
| 12 | Dell XPS 14 9440 | VERIFIED (Best Buy + Dell datasheet) | PENDING 884116470816 (Dell datasheet only) |
| 13 | Dell G16 7630 | PENDING (Dell order codes useghbto7630glmf / fwmg) | NO LEAD |
| 17 | MS Surface TB4 Dock | VERIFIED (B&H + Newegg + Best Buy) | VERIFIED (B&H + Zoro) 196388142200 |
| 18 | Oakley Vanguard | NOT VERIFIED (conflict) | PENDING 888392690388 (Abt only) |
| 19 | Ray-Ban Skyler Gen 2 | PENDING 0RW4014_601/7152 (Best Buy product page only) | NO LEAD |
| 20 | Google Nest Hub 2nd Gen | VERIFIED (Best Buy + Abt) | VERIFIED (Ferguson + Zoro) 193575009223 |
| 21 | Keychron K11 Max | PENDING K11M-A1 (Keychron family only) | NO LEAD |
| 22 | Keychron Q0 Max | PENDING Q0M-M1 (Keychron family only) | NO LEAD |
| 23 | HyperX Cloud III Wireless | VERIFIED (Best Buy + hyperx.com) | PENDING 197029611727 (no qualifying source) |
| 24 | HyperX Alloy Origins 60 | VERIFIED (Best Buy + Newegg + HP.com) | VERIFIED (Newegg + HP datasheet) 196188048948 |
| 25 | Corsair K65 PRO MINI | VERIFIED (Best Buy + Newegg) | PENDING 840006698432 (no qualifying source) |
| 26 | Bose Solo Series II | PENDING 845194-2100 (single source) | NO LEAD |

- MPN VERIFIED: 14 of 23. UPC VERIFIED: 5 of 23 (2, 3, 17, 20, 24).
- Retailer-direct row: item 7 NO; item 13 YES (Dell.com, price to re-verify); item 21 NO; item 22 NO. (Lenovo items 14–16 excluded per pivot.)

## Flags / conflicts for the parent
1. **Odyssey G5 suffix conflict** — Samsung.com LS27HG550ENXZA vs Best Buy LS27HG552ENXZA. Do not merge; needs a channel-variant ruling.
2. **Oakley Vanguard model-format conflict** — Abt OW8001800105 vs Best Buy 0OW8001 3928 46 vs EU-retailer consensus OW8001-05 52. No qualifying pair agrees.
3. **ZenWiFi AXE7800 Best Buy row dead** — current Best Buy listing is Newegg Official marketplace ($356.49); the draft's $302.49 Best Buy-direct row no longer holds.
4. **Dell G16 7630 is NOT discontinued at Dell** — dell.com lists the exact pinned config at $1,949.99–$1,959.99 (stale crawls, re-verify price). Earlier "discontinued" read withdrawn.
5. **XPS 14 9440 pinned config not available new at Best Buy** — product page says so; only Q&A $1,199.99 and open-box of a different config.
6. **Magic Keyboard MJQJ3LL/A is the older keyboard** (Pro 11" 1st–4th gen / Air 4th–5th gen), not M2-exclusive; Apple.com price/stock not captured; no retailer-direct new row.
7. **K11 Max may be discontinued** — keychron.com header "Sold out"; bulsuk.com (Aug 2026) says K11 Pro/Max retired, successor K15 Max.
8. **HyperX Cloud III Wireless discontinued at hyperx.com** (OutOfStock, $149.99) — Best Buy may be the only live row.
9. **Apple 35W UPC split** — compact MW2H3AM/A = 195949376535; non-compact MW2K3AM/A = 195949376573. Do not cross them.
10. **HP 430 / Keychron MPNs rest on same-family corroboration only** (HP datasheet + hp.com; Keychron regional stores) — kept PENDING, not upgraded.
11. **UPC second sources for items 2, 3, 20 are distributor specs** (ADI, Ferguson, Zoro), not core retailers — flagged in each entry for re-judging.
