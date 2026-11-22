# Track E — Laptops — Batch 8 findings (2026-11-21/22)

Researcher: Track E (laptops). Skill: `~/workspace/custom-skills/price_compare_expansion/SKILL.md`.
All live page opens: 2026-11-22 00:00–00:07 UTC (= 2026-11-21 16:00–16:07 PST), via `browser.open` text fetch unless noted as search-snippet evidence.
Membership reference: `data/rework8/catalog_ref_550.tsv` (550 models). Every candidate checked by key, model-name substring (normalized, both directions), MPN, and UPC. Zero collisions on all 12 models below; sibling adjudications noted per model.

## Summary table

| # | Model (pinned config) | MPN | UPC | Live direct row | Verdict |
|---|---|---|---|---|---|
| 1 | Lenovo Legion Pro 7 Gen 10 AMD 83RU0006US | VERIFIED | VERIFIED 199271660232 | Adorama $4,949.00 InStock | **KEEP** |
| 2 | Alienware 16 Aurora LAC16250-7469BLU-PUS, Blue | VERIFIED | VERIFIED 884116430469 | AntOnline $2,149.99 InStock | **KEEP** (HOLD released; see flag) |
| 3 | Lenovo LOQ Essential 15ARP11 83VA001PUS | PENDING (Best Buy only) | PENDING (no lead) | Best Buy $1,049.99 InStock | **KEEP-PENDING** |
| 4 | ASUS ROG Zephyrus G14 2025 GA403UM-G14.R9HX4, Platinum White | PENDING (Best Buy only) | PENDING (no lead) | Best Buy $2,299.99 InStock | **KEEP-PENDING** |
| 5 | HP OMEN Transcend 14 2025 14-fb1043dx, Shadow Black | VERIFIED | PENDING + lead 821844495667 | Best Buy $2,499.99 InStock | **KEEP-PENDING** |
| 6 | Samsung Galaxy Book5 360 15.6" NP750QHA-KA1US, Gray | VERIFIED | PENDING (no lead) | Connection $1,695.95 InStock; Quill $1,702.99 InStock | **KEEP-PENDING** (queue exit) |
| 7 | Lenovo Yoga 7i 2-in-1 14" 83TC003XUS, Luna Grey (deal-site add) | VERIFIED | PENDING + lead 199275077982 | Best Buy $999.99 InStock | **KEEP-PENDING** |
| 8 | Dell XPS 13 2026 LDX13260-5960SKY-PUS, Sky (deal-site add) | PENDING (Best Buy + packaging) | PENDING + lead 884116652960 | Best Buy $999.99 InStock | **KEEP-PENDING** |
| 9 | Lenovo ThinkPad T16 Gen 4 21QN0045US, Black | VERIFIED | VERIFIED 198158520584 | None confirmed (see §9) | **QUEUE** |
| 10 | Lenovo ThinkPad T14 Gen 5 21MC000NUS, Gray | VERIFIED | VERIFIED 198153286256 | None (B&H discontinued; Adorama backorder Jan 2027) | **QUEUE** |
| 11 | ASUS Vivobook S 14 Q423SA-U5512, Neutral Black | VERIFIED | PENDING (eBay only) | None (Best Buy dead; Newegg no price) | **QUEUE** |
| 12 | Lenovo Legion 5i 15.1" 83LY0000US, Eclipse Black (recheck) | VERIFIED w/ caveat | CONTESTED 198155802546 | None (Walmart robot wall, 3rd time) | **QUEUE** |

**Identifier tally (12 models):** both identifiers verified: 4 (#1, #2, #9, #10). MPN verified / UPC pending: 2 (#5, #6). MPN pending / UPC pending: 4 (#3, #4, #7*, #8*) — *#7 MPN verified, UPC pending; #8 MPN pending, UPC pending. MPN verified + UPC contested: 1 (#12). MPN verified + UPC pending (eBay-only lead): 1 (#11).
**Rows:** 8 models have a live direct row (2 KEEP + 6 KEEP-PENDING). 4 stay in queue for lack of a row / conflict.

---

## 1. Lenovo Legion Pro 7 Gen 10 AMD — 83RU0006US [KEEP]

- **Proposed key:** `lenovo-legion-pro-7-gen-10-83ru0006us`
- **Brand / model / pinned variant:** Lenovo / Legion Pro 7 16AFR10H / Eclipse Black, Ryzen 9 9955HX3D, RTX 5080 16GB, 32GB DDR5-5600, 2TB PCIe Gen5 SSD, 16" WQXGA OLED 240Hz, Win 11 Pro.
- **MPN 83RU0006US — VERIFIED.** Best Buy model field (SKUs 12629843, 13259871) + PSREF PDF for 16AFR10H (shoprbc.com mirror) + CompSource.
- **UPC 199271660232 — VERIFIED.** PSREF PDF ("EAN / UPC / JAN: 199271660232", TopSeller, Announce 2025-09-13) + CompSource distributor ("UPC EAN CODE: 199271660232") + Bonanza / SimplifiedComputers / DirectDial / PC-Canada / Venditore agreeing. Manufacturer + distributor pair = acceptable per precedent.
- **Price row:** **Adorama $4,949.00, InStock (JSON-LD), Adorama direct** (live open 2026-11-22 00:02 UTC; title/specs confirm 9955HX3D / 32GB / 2TB / RTX 5080 / Win 11 Pro). Best Buy SKU 12629843 shows the same $4,949.00 but is "Sold & shipped by Adorama" — marketplace, NOT a Best Buy direct row; do not use as Best Buy row. Newegg lists $4,495.62 (seller status unchecked — not used).
- **Do-not-mix warnings:** (a) Slickdeals/Best Buy 1TB config from thread 2026-11-08 ($2,849.99, expired) is a different config with unknown MPN — do not mix. (b) Sibling 83RU0005US has conflicting RAM claims (CompSource title 32GB/2TB, UPC 199271660218; ek.ua aggregator says 64GB) — not the pinned config. (c) 83RU000LPB (64GB) also exists.
- **Membership:** no collision in catalog_ref_550.tsv ("legion-pro-7", 83RU0006US, 199271660232 all clear).
- **Open items:** none for add. Newegg $4,495.62 seller check optional at add time.

## 2. Alienware 16 Aurora — LAC16250-7469BLU-PUS, Blue [KEEP — HOLD released]

- **Proposed key:** `alienware-16-aurora-lac16250-7469blu-blue` (same key as Batch 6 trackD §9)
- **Brand / model / pinned variant:** Alienware / 16 Aurora / Blue, Intel Core 7 240H (10C/16T, up to 5.2GHz), RTX 5060 8GB GDDR7, 16GB DDR5-5600, 1TB SSD, 16" WQXGA 2560×1600 IPS 120Hz, Win 11 Home, 5.49 lb. Model LAC16250-7469BLU-PUS.
- **MPN LAC16250-7469BLU-PUS — VERIFIED.** Batch 6 record (Newegg spec page + D&H distributor spec sheet; Best Buy model field agrees). Confirmed again live: AntOnline product page prints "Manufacturer Part Number LAC16250-7469BLU-PUS".
- **UPC 884116430469 — VERIFIED.** Batch 6 record (D&H Consumer spec sheet + "Product Setup - New Age" spec sheet, both listing UPC 884116430469 for this MPN; Hilltown Tech agrees). Repo grep confirms Batch 6 evidence (`data/rework6/trackD.md:122-128`, `data/candidates_batch6_500.md:594`). Note: Batch 7's brief claimed "双标识已核实" for Aurora but no LAC16250 evidence exists in `data/rework7/*.md` — the evidence is Batch 6's, not Batch 7's.
- **Price row — HOLD CONDITION NOW MET:** **AntOnline $2,149.99, JSON-LD InStock, new condition** (live open 2026-11-22 00:03 UTC, `antonline.com/Dell/Computers/Computer_Systems/Notebooks/1535284`). Batch 6's hold note said "antonline.com direct $2,149.99 does not show the model code" — the live page NOW shows the model code (Manufacturer Part Number LAC16250-7469BLU-PUS), so that objection is resolved. AntOnline (Atlanta Network Technologies, Inc., Atlanta GA, in business since 1995) is a direct US online retailer, not a marketplace.
- **Flag for coordinator:** AntOnline is a smaller/non-top-tier retailer, and $2,149.99 is above Best Buy's sold-out $1,707.70. Batch 6's hold asked for "Sold-by-Best-Buy, sold-by-Newegg, or dell.com direct row" — this row is AntOnline direct instead. Best Buy SKU 13279039 live open (2026-11-22 00:03 UTC): model confirmed but **Sold Out** at $1,707.70 (JSON-LD misleadingly says InStock; page says Sold Out); marketplace rows $1,649.00–$2,223.99 excluded. Dell.com configurator shows only the 32GB/1TB/RTX 5060 config at $2,699.99 list (snippets inconsistent, $1,799.99–$1,999.99) and does not map to the retail PUS SKU — not used.
- **Do-not-mix:** 32GB sibling LAC16250-7568BLU-PUS had a $999.99 Best Buy deal in a Slickdeals thread dated 2025-11-21 (a year old, expired) — do not use. Best Buy "Upgraded" PC Heaven listings (AC16250-Upgraded, $2,149.00–$3,099.00) are third-party-modified — excluded. Distinct from in-catalog `alienware-16-area-51-rtx-5070-ti-2tb-liquid-teal` (LAA16250-9499BLU-PUS; Aurora LAC vs Area-51 LAA, different family/tier).
- **Membership:** no collision ("aurora", "16-aurora", LAC16250-7469BLU-PUS all clear).
- **Open items:** none for add, subject to coordinator accepting AntOnline as the direct row.

## 3. Lenovo LOQ Essential 15ARP11 — 83VA001PUS [KEEP-PENDING]

- **Proposed key:** `lenovo-loq-essential-15arp11-83va001pus`
- **Brand / model / pinned variant:** Lenovo / LOQ Essential 15ARP11 / Eclipse Black, Ryzen 7 170 (8C/16T, up to 4.75GHz), RTX 5050 8GB GDDR7 65W, 16GB DDR5-4800, 512GB PCIe 4.0 SSD, 15.6" FHD 1920×1080 IPS 144Hz 100% sRGB, Win 11 Home. Announced Feb 2026.
- **MPN 83VA001PUS — PENDING (single qualifying source).** Best Buy model field only (SKU 6673556, live open 2026-11-22 00:01 UTC). No lenovo.com / Newegg / B&H hit in search. (The PSREF LOQ Essential 15ARP11 PDF is a *platform* spec — 7 pages, no per-model EAN/UPC table — so it does NOT list 83VA001PUS; an earlier outgeeked.net citation of PSREF for this MPN could not be verified against the PDF itself.)
- **UPC — PENDING, no lead.** PSREF platform PDF has no model-level UPC line. No UPC found in any search.
- **Price row:** **Best Buy $1,049.99** (Comp. Value $1,499.99, Save $450), Add to Cart, JSON-LD InStock, sold by Best Buy (live open SKU 6673556, 2026-11-22 00:01 UTC). Search crawls also show a Black Friday $999.99 variant and a $1,299.00 PC Heaven marketplace SKU (12974439) — do not use marketplace. Lenovo.com US list $1,892.99 per NotebookCheck/The Gadgeteer (2026-11-10) is a list price, not the row.
- **Flag:** Best Buy title says "2K" but its own spec panel says 1920×1080 FHD 144Hz — pin FHD per spec panel + PSREF platform spec; note title-vs-spec conflict.
- **Membership:** no collision (83VA001PUS clear).
- **Open items:** UPC (no lead at all — needs a retailer/distributor spec page printing it); MPN second source (lenovo.com US product page or B&H).

## 4. ASUS ROG Zephyrus G14 2025 — GA403UM-G14.R9HX4, Platinum White [KEEP-PENDING]

- **Proposed key:** `asus-rog-zephyrus-g14-ga403um-r9hx4-white`
- **Brand / model / pinned variant:** ASUS / ROG Zephyrus G14 (2025) GA403UM / Platinum White, Ryzen 9 270 (8C/16T, up to 5.2GHz), RTX 5060 8GB GDDR7, 16GB LPDDR5X-7500, 1TB PCIe 4.0 SSD, 14" 3K 2880×1800 OLED 120Hz 500-nit, Win 11 Home, 3.31 lb.
- **MPN GA403UM-G14.R9HX4 — PENDING (single qualifying source).** Best Buy model field only (SKU 6629420, live open 2026-11-22 00:02 UTC). Corroboration is non-qualifying only: Velztorm marketplace listings on Best Buy print "Model No: GA403UM-G14.R9HX4"; Smartprix aggregator lists it; Slickdeals threads name it. No B&H / Newegg / ASUS store hit. (ASUS ROG site lists the 2026 GA403 family with different CPUs, not the 2025 GA403UM retail SKU suffix.)
- **UPC — PENDING, no lead.** Best Buy spec panel did not print it in the fetch; no UPC found in any search (only Amazon ASINs for HIDevolution bundles).
- **Price row:** **Best Buy $2,299.99, Sold by Best Buy**, Add to cart, JSON-LD InStock, 4.4 stars / 509 reviews (live open SKU 6629420, 2026-11-22 00:02 UTC). Smartprix claims $1,976.99 at Walmart (aggregator, unverified — do not use). Slickdeals open-box $1,154.99 Excellent / $1,085.99 Good / $1,015.99 Fair are open-box, not new rows. Tom's Guide $1,349 is stale July 2025. Velztorm "Upgraded" listings ($2,049.99–$2,149.99) are third-party-modified — excluded.
- **Membership:** no collision ("zephyrus-g14", GA403UM, GA403UM-G14.R9HX4 all clear).
- **Open items:** MPN second source (ASUS US store / B&H); UPC (no lead).

## 5. HP OMEN Transcend 14 2025 — 14-fb1043dx, Shadow Black [KEEP-PENDING]

- **Proposed key:** `hp-omen-transcend-14-14-fb1043dx-black`
- **Brand / model / pinned variant:** HP / OMEN Transcend 14 / Shadow Black, Intel Core Ultra 7 255H, RTX 5060 8GB GDDR7, 16GB LPDDR5x-7467, 1TB PCIe Gen4 SSD, 14" 3K 2880×1800 OLED 120Hz, Win 11 Home, 3.6 lb, up to 14h45m battery.
- **MPN 14-fb1043dx / D8KM3UA#ABA — VERIFIED.** Best Buy model field (SKU 6672941) + HP's own datasheet PDF (files.bbystatic.com, "OMEN by HP Transcend 14 inch Gaming Laptop PC 14-fb1043dx", Product number D8KM3UA#ABA).
- **UPC 821844495667 — PENDING + lead (single source).** HP datasheet PDF only ("UPC Code • 821844495667"). No second source found (search for the UPC returns only the datasheet; Walmart Business lists the same config at $1,330.00 but Out of stock and prints no UPC).
- **Price row:** **Best Buy $2,499.99, Sold by Best Buy**, Add to cart, JSON-LD InStock, 4.8 stars / 37 reviews (live open SKU 6672941, 2026-11-22 00:02 UTC). List price, no promo. Earlier snippet text mentioning "Win 11 Pro" and "+1TB Dock" belonged to a different (upgraded/marketplace) listing — pinned config is Win 11 Home per live page.
- **Do-not-mix / dead sibling:** 32GB sibling 14-fb1013dx / B94GQUA#ABA (SKU 6618922, clearance $1,600.99 in search snippets) is DEAD — Best Buy live open (2026-11-22 00:02 UTC) says "This item is no longer available in new condition." Do not use.
- **Membership:** no collision ("transcend-14", "omen-transcend" — only hit is the in-catalog 32" *monitor* `hp-omen-transcend-32-black`, a different product).
- **Open items:** UPC second source (B&H / Newegg spec page printing 821844495667).

## 6. Samsung Galaxy Book5 360 15.6" — NP750QHA-KA1US, Gray [KEEP-PENDING — queue exit]

- **Proposed key:** `samsung-galaxy-book5-360-15-np750qha-ka1us-gray`
- **Brand / model / pinned variant:** Samsung / Galaxy Book5 360 / Gray, Core Ultra 7 256V, 16GB LPDDR5X, 512GB SSD, 15.6" FHD AMOLED touch, Win 11 Home, Copilot+ PC.
- **MPN NP750QHA-KA1US — VERIFIED (new this round).** Best Buy model field + Quill (Model # NP750QHA-KA1US) + Connection (MFG Part# NP750QHA-KA1US) + Staples (Model NP750QHA-KA1US).
- **UPC — PENDING, no lead.** Neither Connection nor Quill prints a UPC in the fetched text. Samsung.com US product page did not surface in search (no samsung.com listing found for this MPN).
- **Price rows (live, both 2026-11-22 00:06 UTC):** **Connection $1,695.95, In Stock, Ships in 1–2 Business Days** (live open; search snippet's $1,315.95 was stale — live page says $1,695.95). **Quill $1,702.99, JSON-LD InStock**, delivery Nov 25–27 (live open). The two agree at ~$1,700. Staples $1,419.69 is out of stock (stale, 193+ days).
- **Best Buy recheck (2026-11-22 00:00 UTC):** SKU 6613609 clearance **$358.99** (Save $991, Comp. Value $1,349.99) with **Unavailable**; SKU 13224856 $2,187.81, also Unavailable. The $358.99-vs-$2,187.81 conflict persists but is now moot — Best Buy is out of stock and the row comes from Connection/Quill.
- **Flag for coordinator:** both rows are from smaller/B2B-leaning retailers (Connection is an IT reseller, Quill is office supply), not Samsung direct or Best Buy. Prices are consistent with each other, which supports them.
- **Membership:** no collision ("galaxy-book5", "book5-360", NP750QHA all clear).
- **Open items:** UPC (no lead); Samsung.com second MPN/price source if it ever lists the model again.

## 7. Lenovo Yoga 7i 2-in-1 14" — 83TC003XUS, Luna Grey [KEEP-PENDING — deal-site add]

- **Proposed key:** `lenovo-yoga-7i-2-in-1-14-83tc003xus-luna-grey`
- **Brand / model / pinned variant:** Lenovo / Yoga 7i 2-in-1 Gen 11 Aura Edition 14IPH11 / Luna Grey, Intel Core Ultra 7 355 (Panther Lake, Series 3), 24GB LPDDR5X-7467 (soldered), 512GB PCIe NVMe SSD, 14" 1920×1200 2K OLED touch 60Hz 400-nit, Win 11 Home, Copilot+ PC, 3.08 lb.
- **MPN 83TC003XUS — VERIFIED.** Best Buy model field (SKU 6671007) + Newegg listing (Model Name 83TC003XUS, specs match: Ultra 7-355, 24GB, 512GB, 14" WUXGA OLED touch, Luna Grey, 14IPH11). NotebookCheck (2026-11-21) also names it "Yoga 7i 2-in-1 Gen 11 Aura Edition 14" 83TC003XUS".
- **UPC 199275077982 — PENDING + lead (single non-qualifying source).** TekFeed aggregator only ("SKU 83TC003XUS, Model 83TC003XUS, UPC 199275077982"). No PSREF hit for 83TC003XUS / 14IPH11 in search.
- **Price row:** **Best Buy $999.99** (Save $650, Comp. Value $1,649.99), Add to Cart, JSON-LD InStock, 4.8 stars / 49 reviews (live open SKU 6671007, 2026-11-22 00:07 UTC; search crawls 1–2 days ago confirm "Sold by Best Buy"). Slickdeals frontpage thread 2026-11-19 (Dr.W) + NotebookCheck 2026-11-21 "lowest-ever price". Open-box rows ($765.99–$812.99) and refurbished ($1,199.99, IST Computers) excluded; "Upgraded" marketplace listings (83TC003XUS-Upgraded, $1,629–$1,729) excluded.
- **Do-not-mix:** distinct from Batch 7's Yoga 7i 2-in-1 16" 83JT0000US (Ultra 5 226V, 16GB, 16" WUXGA IPS) and from the twin-config 83TE0004US (Ultra 5 322, 16GB, $1,649.99 list) flagged in Batch 7. Different size/CPU/RAM = different model.
- **Membership:** zero hits in catalog_ref_550.tsv for 83TC003XUS / "yoga-7i-2-in-1-14".
- **Open items:** UPC second source (PSREF 14IPH11 model PDF or a retailer spec page printing 199275077982).

## 8. Dell XPS 13 2026 — LDX13260-5960SKY-PUS, Sky [KEEP-PENDING — deal-site add]

- **Proposed key:** `dell-xps-13-ldx13260-5960sky-sky`
- **Brand / model / pinned variant:** Dell / XPS 13 (2026) DX13260 / Sky, Intel Core 5 320 (Series 3), 16GB LPDDR5X, 512GB SSD, 13.4" 2560×1600 (2.5K) touch 120Hz 500-nit, Intel Graphics, Win 11 Home, Wi-Fi 7, ~2.2 lb.
- **MPN LDX13260-5960SKY-PUS — PENDING (Best Buy + manufacturer packaging).** Best Buy model field (SKU 6683772) + retail-box photos (Facebook, 2026-10-10/11-04) showing the model code and matching specs on Dell packaging. No second retailer found (the "-PUS" suffix is a Best Buy retail SKU; dell.com configurator does not carry it).
- **UPC 884116652960 — PENDING + lead (single non-qualifying source family).** eBay listing (item 327296803592) + picclick / myus / seekknowhow mirrors of the same eBay listing. No retailer/distributor second source.
- **Price row:** **Best Buy $999.99, Sold by Best Buy**, Add to cart, JSON-LD InStock, 4.3 stars / 47 reviews (live open SKU 6683772, 2026-11-22 00:07 UTC). **The Slickdeals $699.99 price is EXPIRED** (thread 2026-11-16, offer valid through Nov 18; crawls 5 days ago $699.99, crawl 1 day ago $999.99). Do not write $699.99. A second Best Buy SKU 13223232 for the same model shows $969.00 — seller unclear, do not use.
- **Flag:** Best Buy title says "3K" but its own spec panel says 2560×1600 (2.5K) 120Hz — pin 2560×1600 per spec panel; note title-vs-spec. Do not mix with the 8GB sibling LDX13260-5953SKY-PUS (also $699.99 at one point).
- **Membership:** zero hits in catalog_ref_550.tsv for LDX13260 / "xps-13" / 5960SKY.
- **Open items:** MPN second retailer; UPC second source (B&H / Newegg / Dell spec sheet).

## 9. Lenovo ThinkPad T16 Gen 4 — 21QN0045US, Black [QUEUE — identifiers done, row unresolved]

- **Proposed key:** `lenovo-thinkpad-t16-gen-4-21qn0045us-black`
- **Brand / model / pinned variant:** Lenovo / ThinkPad T16 Gen 4 (AMD) / Black, Ryzen AI 5 PRO 340 (6C/12T), Radeon 840M, 16GB DDR5-5600 (1×16GB), 256GB SSD, 16" WUXGA 1920×1200 IPS 400-nit, Win 11 Pro, Wi-Fi 7, 5MP camera, fingerprint reader, TopSeller, Announce 2025-05-22.
- **MPN 21QN0045US — VERIFIED.** PSREF model PDF + CDW listing + Dihuni listing + Newegg listing + Best Buy model field (SKUs 11522697, 11885055).
- **UPC 198158520584 — VERIFIED.** PSREF ("EAN / UPC / JAN: 198158520584", mirrors: getuniqcli, etilize, flatironnetworks) + **atticusgoods.com retail listing ("UPC 0198158520584")** + Icecat (Lenovo-fed catalog, same value in multiple locales). Manufacturer + retail listing agree.
- **Price row — UNRESOLVED.** Best Buy SKUs are marketplace-only (11885055: Merchant Expo LLC $1,697.05; 11522697: $1,575.58, marketplace). Newegg listing is sold by **antonline** at $1,378.08 InStock (JSON-LD) — marketplace, not Newegg direct; its return policy line reads "covered by antonline Return Policy". AntOnline's own site lists it at **$1,359** in category-page crawls (13–22 days old) but the direct product page was not live-opened (URL not recoverable from search results; do not guess). CDW page (8391839) shows specs but no price in the fetch. atticusgoods $1,330.99 is **Sold out**. Dihuni $1,514.00 and IP Security Depot $1,417.99 are small non-standard resellers. Amazon ~$1,329 per aggregator — Amazon cannot be a price source per project rules. No lenovo.com US listing found.
- **Distinct from** in-catalog `lenovo-thinkpad-t16-gen-4-black` (21QN005XUS: Ryzen AI 7 PRO 350, 512GB) — different CPU + storage.
- **Membership:** no collision (21QN0045US, 198158520584 clear).
- **Open items:** live direct row — re-check AntOnline product page / CDW price / lenovo.com at add time; the AntOnline $1,359 (own site) vs $1,378.08 (via Newegg) $19 gap also needs settling.

## 10. Lenovo ThinkPad T14 Gen 5 — 21MC000NUS, Gray [QUEUE — both verified, no live row]

- **Proposed key:** `lenovo-thinkpad-t14-gen-5-21mc000nus-gray`
- **Brand / model / pinned variant:** Lenovo / ThinkPad T14 Gen 5 / Gray, Ryzen 5 PRO 8540U (6C, 3.2–4.9GHz), Radeon 740M, 16GB DDR5, 256GB SSD, 14" WUXGA 1920×1200 IPS 400-nit, Win 11 Pro.
- **MPN 21MC000NUS — VERIFIED.** B&H (BH #1830116) + SHI (Mfr Part # 21MC000NUS, $1,356.00, MSRP $1,619.00) + Adorama (MFR: 21MC000NUS).
- **UPC 198153286256 — VERIFIED.** B&H spec page ("UPC: 198153286256") + Adorama spec panel ("UPC Code 198153286256"). Distinct from catalog black row's UPC lead 198153286874.
- **Price rows — all dead:** B&H = Discontinued (stale $1,323.58 shown). Adorama live open (2026-11-22 00:03 UTC) = $1,249.99 but "Temporarily On Backorder — Expected Availability: 01/2027". SHI $1,356.00 is a distributor, not a retail row. No in-stock direct row → stays in queue; re-check after restock.
- **Flag:** Adorama's title/spec text wrongly says "Ryzen 7 PRO 8540U" — 8540U is Ryzen 5 PRO (B&H, SHI, PSREF agree); Adorama's error does not affect the MPN/UPC.
- **Distinct from** in-catalog `lenovo-thinkpad-t14-gen-5-black` (21MC000CUS: Ryzen 7 PRO 8840U, 512GB) — different CPU + storage + color.
- **Membership:** no collision (21MC000NUS, 198153286256 clear).
- **Open items:** restock watch (B&H / Adorama).

## 11. ASUS Vivobook S 14 — Q423SA-U5512, Neutral Black [QUEUE — no live row]

- **Proposed key:** `asus-vivobook-s-14-q423sa-u5512-black`
- **Brand / model / pinned variant:** ASUS / Vivobook S 14 / Neutral Black, Core Ultra 5 226V, 16GB LPDDR5X-8533, 512GB PCIe 4.0 SSD, 14" WUXGA 1920×1200 OLED 60Hz 400-nit (600-nit HDR), Intel Arc, Win 11 Home, Copilot+, 2.87 lb, 75Wh. 2024 model.
- **MPN Q423SA-U5512 — VERIFIED.** Best Buy model field (SKU 6595523) + Newegg model number.
- **UPC 197105728660 — PENDING (eBay only).** Two eBay listings, same listing family — single non-qualifying source.
- **Price rows — dead:** Best Buy live open (SKU 6595523, 2026-11-22 00:03 UTC) = "This item is no longer available in new condition" (clearance $235.99 shown in search snippets, Unavailable). Newegg live open (2026-11-22 00:03 UTC) confirms specs/model but shows **no price and no stock signal** — effectively no live row. Historical Best Buy prices ($649.99 Nov 2024, $599.99 Jan 2025, $549.99 Feb 2025, $449.99 Mar 2025) all expired.
- **Membership:** no collision ("vivobook-s-14", Q423SA clear).
- **Open items:** restock watch; UPC second source (B&H / ASUS store spec page).

## 12. Lenovo Legion 5i 15.1" — 83LY0000US, Eclipse Black [QUEUE — recheck: stays]

- **Proposed key:** `lenovo-legion-5i-15-83ly0000us-black`
- **Brand / model / pinned variant:** Lenovo / Legion 5i 15IRX10 / Eclipse Black, i7-14700HX, RTX 5060 8GB, 16GB DDR5, 1TB SSD, 15.1" WQXGA 165Hz OLED, Win 11 Home.
- **MPN 83LY0000US — VERIFIED w/ caveat** (per Batch 7: PSREF).
- **UPC 198155802546 — CONTESTED, cannot be claimed verified.** PSREF (Lenovo's own Legion 5 15IRX10 spec sheet, via itbato.com and afraa.shop PDF mirror) lists EAN/UPC/JAN 198155802546 for 83LY0000US. But HowManyFPS and Ubuy attach the same UPC 198155802546 to a different config, 83DF00AQUS (32GB/2TB). The qualifying source (PSREF) supports 83LY0000US; the conflicting sources are non-qualifying aggregator/marketplace — but the conflict means UPC cannot be claimed verified. Do not attach the UPC until the 83DF00AQUS conflict is resolved (e.g. a second qualifying source printing 198155802546 for 83LY0000US specifically).
- **Price row — Walmart re-try FAILED again.** Walmart direct open (verbatim URL `walmart.com/ip/Lenovo-Legion-5i-15-1-WQXGA-165Hz-Gaming-Laptop-Core-i7-14700HX-Nvidia-GeForce-RTX-5060-16GB-RAM-1TB-SSD-3-Month-Microsoft-365/14618706354`) hit the robot wall ("Robot or human?") — **third consecutive wall** (Batch 7 had two). Per brief: stays in queue, never write a row from second-hand price. Search-result evidence only (not usable as a row): Walmart $1,499.00 new (crawl 1 day old); Slickdeals thread 2026-11-09: Walmart $1,499 sold/shipped by Walmart.com; Newegg $1,705.99, Best Buy $1,949.00 per same thread.
- **Membership:** no collision (83LY0000US, "legion-5i", 198155802546 clear).
- **Open items:** Walmart re-try next batch (or a non-Walmart direct row: Best Buy / Newegg direct at add time); UPC conflict resolution.

---

## Drops (named, with reasons)

| Dropped candidate | Reason |
|---|---|
| ASUS ROG Strix G16 (Slickdeals frontpage: i7-14650HX, 16" 1200p, 16GB, RTX 5060, $1,180 Amazon) | Already added in Batch 7 (brief's do-not-repeat list). |
| Apple MacBook Air M5 (Slickdeals: 13.6"/15.3", M5, $1,100–$1,549) | Already added in Batch 7. |
| Lenovo Legion 5a (Slickdeals: Ryzen 7 250, 15.3", $1,250 B&H) | Already added in Batch 7. |
| Lenovo Yoga Slim 7x (Slickdeals: Snapdragon X2P-42-100, 14" 2K OLED, $650 Best Buy) | Already added in Batch 7. |
| Acer Predator Helios Neo 16S AI (Slickdeals: Ultra 9 275HX, RTX 5070 Ti, 32GB, $1,620 eBay) | Refurbished via eBay — not a new-condition direct row. |
| HP OMEN Transcend 14 32GB sibling 14-fb1013dx / B94GQUA#ABA | Dead: Best Buy "no longer available in new condition" (live open 2026-11-22). |
| Legion Pro 7 1TB config (Slickdeals 2026-11-08, $2,849.99) | Different config, MPN unknown, deal expired — do not mix with pinned 83RU0006US. |
| Alienware 16 Aurora 32GB sibling LAC16250-7568BLU-PUS | $999.99 Slickdeals deal dated 2025-11-21 (a year old, expired) — do not use. |

**Deal-site leads NOT researched this round (left for a later batch, not dropped):** ASUS Zenbook S14 UX5406AA (Ultra 9 386H, 14" 3K OLED, 32GB, 1TB, $1,299.99 Best Buy); MSI Prestige 16 (Core Ultra X7 358H, 2.8K OLED 120Hz touch, 32GB, 1TB, $1,200 Costco); Dell 16S (Core Ultra 7 355, 16" 1200p touch, 16GB, 512GB, $800 Best Buy); HP OmniBook X 16 (Snapdragon X2 Elite, 16" FHD+ OLED touch, 24GB, 512GB, $900 Best Buy); ASUS ROG Strix G18 18" RTX 5060 ($2,000 Costco).

## Method notes / caveats for the coordinator

- **B&H UPC rule applied:** B&H's T16 listing UPC 199272895022 belongs to a different config (21QFS1E700, $1,799) — NOT attached to 21QN0045US (Batch 6 T14 Gen 6 lesson).
- **Best Buy "3K"/"2K" title vs spec-panel conflicts** noted for LOQ (title "2K", panel FHD 1920×1080), Zephyrus G14 is fine (3K 2880×1800 confirmed), XPS 13 (title "3K", panel 2560×1600). Pin the spec panel.
- **JSON-LD trap:** Best Buy Alienware SKU 13279039 JSON-LD says InStock while the page says Sold Out — page text wins.
- **AntOnline as a row source:** used twice (Alienware $2,149.99 live with model code; T16 $1,359 category-level only). It is a legitimate direct US retailer, but smaller than Best Buy/Newegg/Dell — coordinator to confirm the tier is acceptable for the catalog.
- **Connection/Quill as row sources (Book5 360):** both live-confirmed and price-consistent (~$1,696 vs $1,703), but both are B2B-leaning retailers, not Samsung direct or Best Buy — coordinator to confirm.
- **Black Friday price volatility:** several rows are Black Friday/promo prices that may move (LOQ $1,049.99, Yoga 7i 14" $999.99, XPS 13 $999.99 after $699.99 expired, Legion Pro 7 Adorama $4,949.00). Re-verify live at add time.
- Nothing in this file was added to the catalog; `catalog.py`, `DECISIONS.md`, snapshots, and site untouched; nothing submitted.
