"""Batch 8 add-time writer: appends the 50 approved models to price_agent/catalog.py.

Adjudication (add-time re-verification 2026-11-21, text fetch):
- Dual-verified (UPC verified): 26/50 = draft 24 + 2 upgrades (Z Flip8, WHOOP).
  Z Flip8: databitinc retailer + ProvarTech distributor spec pairing.
  WHOOP: Amazon product page pairs model+UPC + manuals.plus + eBay GTIN;
  conflicting lead 810114363270 has zero support.
- Upgrades DECLINED (kept pending, leads recorded): iPhone Air UPC
  195950621303 (PayMore used-chain scan + eBay seller table — same evidence
  grade the draft coordinator rejected for Watch Ultra 3 / iPhone 17 Pro Max);
  OnePlus 15 UPC 6921815630302 (Swiftronics + eBay.ie + ImportItAll, all
  reseller/marketplace-grade, no brand/retailer spec page or distributor
  table). Watch Ultra 3 / iPhone 17 Pro Max UPCs stay pending: Best Buy
  text fetch never renders a UPC field; live-browser spec-page check still
  needed.
- MPN downgrades (2): Keris II Ace White BMUA10 -> pending-conflict
  (ASUS eShop US white page lists BMAA10); TUF M3 Gen II BMAA00 ->
  pending-conflict (eShop US in-stock page lists BMAA03).
- UPC lead FALSIFIED (1): M3 Gen II 195553909112 binds to non-US MPN
  BMUA00 (PBTech NZ + NationalPC India) — lead void, no valid lead.
- MPN verified final: 42/50. All 50 models enter the catalog; holds are on
  price rows only (Onyx Studio 9 Newegg row, OnePlus 15 row).
Run: python3 data/rework8/add_batch8.py  (inserts before the closing ] of
EVAL_SET, then imports the catalog and prints the new counts).
"""

import re
import textwrap

CATALOG = "price_agent/catalog.py"

# Each row: key, brand, model, variant, category, mpn, upc, verified,
# sources (identifier_sources dict), notes.
# Keys copied verbatim from data/rework8/candidates_batch8_50.tsv.
ENTRIES = [
    dict(key="shokz-opendots-2-black", brand="Shokz", model="OpenDots 2",
         variant="Black", category="earbuds",
         mpn="E320-ST-BK-US", upc="810202687523", verified=True,
         sources={"UPC": "B&H spec page + Abt product page agree (batch-8 verification 2026-11-21).",
                   "MPN": "B&H URL slug + Abt product page agree."},
         notes="B&H $139.95 (was $199.95, Holiday Savings $60) In Stock at add time. "
               "Do not mix with OpenDots Air (E210). (batch-8 verification 2026-11-21)."),
    dict(key="beats-solo-4-matte-black", brand="Beats", model="Solo 4",
         variant="Matte Black", category="headphones",
         mpn="MUW23LL/A", upc="195949121708", verified=True,
         sources={"UPC": "B&H spec page + Abt agree (batch-8 verification 2026-11-21).",
                   "MPN": "Best Buy model field + B&H slug + Abt agree."},
         notes="Best Buy $99.99 (Black Friday Deal, was $199.99) InStock at add time. "
               "Amazon Exclusive Metallic Pink $80 is a different color, not a price source. "
               "(batch-8 verification 2026-11-21)."),
    dict(key="skullcandy-crusher-anc-2-black-tan", brand="Skullcandy", model="Crusher ANC 2",
         variant="Black/Tan", category="headphones",
         mpn="S6CAW-S978", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 810145320808 (eBay listings only); no brand/retailer "
                          "spec-page second source at add time (batch-8 verification 2026-11-21)."},
         notes="MPN S6CAW-S978 confirmed (Best Buy model field, SKU 6580349). Best Buy $119.99 "
               "(Black Friday Deal, was $239.99) InStock at add time. Do not mix with Crusher Evo "
               "(batch 7). (batch-8 verification 2026-11-21)."),
    dict(key="nothing-headphone-1-pro-black", brand="Nothing", model="Headphone (1) Pro",
         variant="Black", category="headphones",
         mpn="B192", upc="", verified=False,
         sources={"UPC": "UPC/EAN pending — lead 6974434229471 (Swiftronics CA + Kogan AU only, "
                          "non-US); no US retailer spec-page second source at add time "
                          "(batch-8 verification 2026-11-21)."},
         notes="MPN B192 confirmed (iFixit device page + Best Buy Canada + Nothing product page). "
               "US Best Buy model field prints A11300048 (SKU 6693512) — a separate US retailer "
               "model code, not mixed with B192. Live row Best Buy US $319.00 (Black Friday Deal, "
               "was $399.00) InStock at add time; Nothing US $399 is list price, not the row. "
               "Do not mix with 2025 Headphone (1) (B186). (batch-8 verification 2026-11-21)."),
    dict(key="amazon-echo-dot-max-graphite", brand="Amazon", model="Echo Dot Max",
         variant="Graphite", category="speakers",
         mpn="B0D6SX8VLQ", upc="", verified=False,
         sources={"UPC": "UPC pending — none written: 4 aggregator codes (840414628809 / "
                          "840414663176 / 840414694620 / 84041466007) mutually exclusive, none from "
                          "a US retailer spec page (batch-8 verification 2026-11-21)."},
         notes="MPN B0D6SX8VLQ confirmed (Best Buy model field, SKU 6642849). Best Buy $49.99 "
               "(Black Friday Deal, Save $70, comp $119.99) InStock at add time. Alexa+ needs "
               "Prime or $19.99/month subscription. (batch-8 verification 2026-11-21)."),
    dict(key="harman-kardon-soundsticks-5-white", brand="Harman Kardon", model="SoundSticks 5",
         variant="White", category="speakers",
         mpn="HKSOUNDSTK5WAM2", upc="050036422468", verified=True,
         sources={"UPC": "B&H spec page + Amazon UPC + PicClick agree (batch-8 verification 2026-11-21).",
                   "MPN": "B&H MFR # + Amazon Model Number agree."},
         notes="White/Clear only. B&H $279.95 (was $349.95) InStock at add time. Black version "
               "(HKSOUNDSTK5BAM2) has no US UPC and was not in stock at B&H; do not mix with "
               "SoundSticks 5 Wi-Fi version. (batch-8 verification 2026-11-21)."),
    dict(key="harman-kardon-onyx-studio-9-black", brand="Harman Kardon", model="Onyx Studio 9",
         variant="Black", category="speakers",
         mpn="HKOS9BLKAM", upc="028292291104", verified=True,
         sources={"UPC": "Amazon UPC + Newegg + NeweggBusiness agree; eBay 610214681881 / "
                          "724129192612 excluded as eBay-generated/refurb codes "
                          "(batch-8 verification 2026-11-21).",
                   "MPN": "Harman Kardon US Item# + Amazon + Newegg agree."},
         notes="Newegg $219.50 row HELD at add time: Sold by Global Mobiles Inc marketplace + "
               "Used - Like New listing. No valid self-operated in-stock row at add time; "
               "Harman Kardon US $299.95 OutOfStock. (batch-8 verification 2026-11-21)."),
    dict(key="garmin-venu-x1-black", brand="Garmin", model="Venu X1",
         variant="Black / Slate Titanium", category="wearables",
         mpn="010-02980-00", upc="753759342746", verified=True,
         sources={"UPC": "Micro Center spec table + CompSource UPC EAN + Petra UPC + Garmin "
                          "announcement PDF agree (batch-8 verification 2026-11-21).",
                   "MPN": "Best Buy model field + Micro Center Mfr Part# + CompSource agree."},
         notes="Best Buy $499.99 (comp $699.99) InStock at add time. Size per Garmin official: "
               "46mm case / 2-inch screen (51mm is the screen diagonal, not the case); key "
               "carries no size. Moss (010-02980-01) is a different colorway. Do not take the "
               "$509.99 SKU (10891072, 2-year warranty bundle). (batch-8 verification 2026-11-21)."),
    dict(key="oura-ring-5-size-8-silver", brand="Oura", model="Ring 5",
         variant="Silver, Size 8", category="wearables",
         mpn="JZ90-61403-08", upc="", verified=False,
         sources={"UPC": "UPC pending — no lead: only 13-digit EAN 6430060156975 (Harvey Norman "
                          "AU, non-US); Best Buy spec text has no UPC field "
                          "(batch-8 verification 2026-11-21)."},
         notes="MPN JZ90-61403-08 confirmed (Best Buy model field + Slickdeals thread). Best Buy "
               "$299.00 (comp $399.00) InStock at add time. Membership: first month free, then "
               "$5.99/month or $69.99/year — first-year price excludes later membership. Size 8 "
               "is the anchored size (sizing kit required). (batch-8 verification 2026-11-21)."),
    dict(key="whoop-5-0-peak-obsidian", brand="WHOOP", model="5.0 Peak",
         variant="Obsidian", category="wearables",
         mpn="973-004-000", upc="810114363317", verified=True,
         sources={"UPC": "Amazon product page (ASIN B0DY2SWV16) pairs Model 973-004-000 with UPC "
                          "810114363317 + manuals.plus spec table + eBay GTIN agree; conflicting "
                          "lead 810114363270 has zero support (batch-8 verification 2026-11-21, "
                          "upgraded at add time).",
                   "MPN": "Best Buy model field + Amazon Model Number agree."},
         notes="Best Buy $199.00 (Black Friday Deal, comp $239.00) InStock at add time. Price is "
               "a 12-month Peak membership bundle (device included); renewal $239/year. Do not "
               "mix with One ($189) or MG/Life ($299, ECG). (batch-8 verification 2026-11-21)."),
    dict(key="amazon-echo-time-graphite", brand="Amazon", model="Echo Time",
         variant="Graphite", category="smart-home",
         mpn="B0FRPDXJYC", upc="", verified=False,
         sources={"UPC": "UPC pending — aggregator-only: matteralpha + bestpricescanner agree on "
                          "840414694712 but neither is a brand/retailer spec page; 840414627574 "
                          "belongs to the White model (B0GFY8SZTK) (batch-8 verification 2026-11-21)."},
         notes="MPN B0FRPDXJYC confirmed (Best Buy model field; White B0GFY8SZTK, Coral Pink "
               "B0GG1YNSPD are separate codes). Live row Best Buy $99.99 (Black Friday Deal, "
               "Save $100, comp $199.99) InStock at add time — draft $199.99 list price "
               "superseded; price fell intraday $149.99 to $99.99. (batch-8 verification 2026-11-21)."),
    dict(key="apple-watch-ultra-3-49mm-black-ocean-band", brand="Apple", model="Watch Ultra 3",
         variant="Black Titanium + Black Ocean Band", category="wearables",
         mpn="MF0J4LW/A", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 195950484311 (eBay GTIN + PayMore scans + box "
                          "photos); no brand/retailer spec page; Best Buy text fetch never renders "
                          "a UPC field — needs live-browser spec-page check "
                          "(batch-8 verification 2026-11-21)."},
         notes="MPN MF0J4LW/A confirmed (Best Buy model field, SKU 6572972). Best Buy $549.00 "
               "(was $799.00) InStock at add time. Refurb/open-box rows excluded; Costco $449.97 "
               "is in-store-only, not a row. (batch-8 verification 2026-11-21)."),
    dict(key="apple-iphone-17-pro-max-256gb-cosmic-orange", brand="Apple", model="iPhone 17 Pro Max 256GB",
         variant="Cosmic Orange", category="phones",
         mpn="MFXH4LL/A", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 195950638004 (PayMore scans + BarcodesInc GTIN "
                          "0195950638004 + eBay + tekfeed); no brand/retailer spec page; Best Buy "
                          "text fetch never renders a UPC field — needs live-browser spec-page "
                          "check (batch-8 verification 2026-11-21)."},
         notes="MPN MFXH4LL/A confirmed (Best Buy model field, SKU 6473213). Best Buy $1,099.99 "
               "(was $1,199.99) InStock at add time — connect-later unlocked price; $999.99 is "
               "the carrier-activated price, not written. Open-box $1,011.99–$1,044.99 and refurb "
               "$972.97+ excluded. Cosmic Orange only. (batch-8 verification 2026-11-21)."),
    dict(key="samsung-galaxy-z-flip8-256gb-graphite", brand="Samsung", model="Galaxy Z Flip8 256GB",
         variant="Graphite", category="phones",
         mpn="SM-F776UZKAXAA", upc="0198957311260", verified=True,
         sources={"UPC": "shop.databitinc.com + ProvarTech distributor spec pairing "
                          "(SM-F776UZKAXAA … 0198957311260) agree (batch-8 verification 2026-11-21, "
                          "upgraded at add time).",
                   "MPN": "Best Buy model field (SKU 6681665)."},
         notes="Best Buy $999.99 (was $1,199.99) InStock at add time. Verizon version "
               "SM-F776UZKAVZW and Pink SM-F776ULIAXAA are different MPNs. Marketplace rows "
               "$815.99–$1,239.84 excluded. (batch-8 verification 2026-11-21)."),
    dict(key="samsung-galaxy-tab-s10-fe-256gb-gray", brand="Samsung", model="Galaxy Tab S10 FE 256GB",
         variant="Gray", category="tablets",
         mpn="SM-X520NZAEXAR", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 887276992259 (Samsung US official MSRP Price List, "
                          "8 editions 2025-03 to 2026-07); single publisher, no second source at "
                          "add time (batch-8 verification 2026-11-21)."},
         notes="MPN SM-X520NZAEXAR confirmed (Best Buy model field + Samsung MSRP list). Best Buy "
               "$469.99 (comp $669.99, Black Friday Deal) confirmed as new self-operated row at "
               "add time (Sold by Best Buy; $874.69 is Merchant Expo marketplace, open-box "
               "$392.99–$422.99 excluded). Blue UPC 887276992273 is a different color "
               "(SM-X520NLBEXAR). No collision with the 128GB model (SM-X520NZAAXAR). "
               "(batch-8 verification 2026-11-21)."),
    dict(key="apple-iphone-air-256gb-space-black", brand="Apple", model="iPhone Air 256GB",
         variant="Space Black", category="phones",
         mpn="MG184LL/A", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 195950621303 (BarcodesInc GTIN 0195950621303 + "
                          "PayMore Thornton scan + eBay seller table); reseller/marketplace-grade "
                          "legs only, no brand/retailer spec page or distributor table — same bar "
                          "as Watch Ultra 3 / iPhone 17 Pro Max, not upgraded at add time "
                          "(batch-8 verification 2026-11-21)."},
         notes="MPN MG184LL/A confirmed (Best Buy model field, SKU 6473225; Model A3260). Best "
               "Buy $799.99 (comp $1,099.99) InStock at add time — connect-later unlocked price; "
               "$699.99 is carrier-activated, not written. Light Gold / Sky Blue $999.99 / "
               "$919.99 prices are stale (four colors now $799.99). (batch-8 verification 2026-11-21)."),
    dict(key="google-pixel-10-pro-128gb-obsidian", brand="Google", model="Pixel 10 Pro 128GB",
         variant="Obsidian", category="phones",
         mpn="GA09887-US", upc="", verified=False,
         sources={},
         notes="MPN GA09887-US confirmed (Best Buy model field, SKU 6637725). No UPC lead found "
               "anywhere. Best Buy $999.00 InStock at add time. Google Store $749 not verified "
               "at add time (store.google.com/config/pixel_10_pro renders no price in text "
               "fetch; 2025 Black Friday $749 ended 2025-12-03) — not written. Third-party "
               "$869.99 (Platinum Supply Group) and refurb $442.68–$559 excluded. "
               "(batch-8 verification 2026-11-21)."),
    dict(key="oneplus-15-12gb-256gb-infinite-black", brand="OnePlus", model="OnePlus 15 12GB + 256GB",
         variant="Infinite Black", category="phones",
         mpn="CPH2749", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 6921815630302 (Swiftronics + eBay.ie listing + "
                          "ImportItAll); reseller/marketplace-grade legs only, no brand/retailer "
                          "spec page or distributor table — not upgraded at add time "
                          "(batch-8 verification 2026-11-21)."},
         notes="MPN CPH2749 (North America) confirmed (Swiftronics/myworldphone + FCC). Price "
               "row HELD at add time: oneplus.com US store closed per 2026-07-16 announcement "
               "(after-sales only, no store, no EXTRA100 code) — draft $799.00 code price is "
               "dead; Swiftronics $959.99 is a reseller, Amazon signals conflict ($833 vs "
               "$1,049), Best Buy only has 512GB Sand Storm $999.99. OnePlus has said it will "
               "not launch new phones in North America; 15 is the last North America flagship. "
               "(batch-8 verification 2026-11-21)."),
    dict(key="samsung-s90h-65", brand="Samsung", model='S90H 65" OLED',
         variant='65"', category="tvs",
         mpn="QN65S90HAEXZA", upc="198957270574", verified=True,
         sources={"UPC": "QVC tech spec PDF + manuals.plus Samsung spec table + B&H + Walts + "
                          "shopmyexchange + Big Screen Store agree (batch-8 verification 2026-11-21).",
                   "MPN": "Crutchfield MFR # + Samsung 2026 spec table + Best Buy model field agree."},
         notes="Best Buy $1,399.99 (Black Friday, comp $2,699.99) InStock at add time. Conflict "
               "resolved: 198957276095 is the Canadian variant QN65S90HAEXZC (suffix C), not "
               "the US ZA model. Costco $1,399.99 includes an Allstate plan bundle, not the main "
               "row. (batch-8 verification 2026-11-21)."),
    dict(key="lg-oled-evo-c6-65", brand="LG", model='OLED evo C6 65"',
         variant='65"', category="tvs",
         mpn="OLED65C6PUA", upc="195174137666", verified=True,
         sources={"UPC": "B&H + EnergyStar list (OLED65C6PU* family) + Value Electronics + Amazon "
                          "+ Adorama agree (batch-8 verification 2026-11-21).",
                   "MPN": "Best Buy model field (SKU 6673112)."},
         notes="Best Buy $1,399.99 (Black Friday, comp $2,699.99) InStock at add time. EnergyStar "
               "also lists 195174137703 (another PU* suffix variant) and Visions CA lists "
               "195174137673 (regional) — neither is this model. LG also has OLED65C6WUA; Best "
               "Buy row uses PUA. (batch-8 verification 2026-11-21)."),
    dict(key="samsung-hw-q990h-black", brand="Samsung", model="HW-Q990H",
         variant="Black", category="soundbars",
         mpn="HW-Q990H/ZA", upc="198957269394", verified=True,
         sources={"UPC": "Walts retailer spec page + B&H + Amazon agree (batch-8 verification 2026-11-21).",
                   "MPN": "Samsung US + Best Buy model field (SKU 6670431) agree."},
         notes="Best Buy $1,497.99 (self-operated); Samsung US $1,499.99. Woot $857.99 not used "
               "(suspected international/parallel stock, seller identity unverified). Do not mix "
               "with HW-Q990F (previous generation, pending). (batch-8 verification 2026-11-21)."),
    dict(key="jbl-cinema-sb580-black", brand="JBL", model="Cinema SB580",
         variant="Black", category="soundbars",
         mpn="JBLSB580BLKAM", upc="050036408530", verified=True,
         sources={"UPC": "Crowdfused model/UPC table + goWholesale + VIP Outlet SKU "
                          "VIP050036408530MN agree (batch-8 verification 2026-11-21).",
                   "MPN": "Crowdfused + goWholesale + VIP Outlet agree; JBL US Item# is "
                          "JBLSB580BLKAM-Z (same model, -Z suffix)."},
         notes="Walmart $199.00 (Sold and shipped by Walmart.com) InStock at add time. In-store "
               "clearance posts as low as $50 are isolated stores, not the online row; Walmart "
               "product page was bot-blocked for text fetch — Add to Cart needs live-browser "
               "check. (batch-8 verification 2026-11-21)."),
    dict(key="samsung-smart-monitor-m70f-43-black", brand="Samsung", model='Smart Monitor M7 M70F 43"',
         variant="Black", category="monitors",
         mpn="LS43FM702UNXZA", upc="198957005435", verified=True,
         sources={"UPC": "camelcamelcamel (ASIN B0F5VLWQY6) + DataVision + LayawayLand agree "
                          "(batch-8 verification 2026-11-21).",
                   "MPN": "Samsung US + Best Buy model field (SKU 6632216) + Abt agree."},
         notes="Samsung US $499.99; Abt $499.99 InStock at add time. Best Buy $399.99 clearance "
               "and Amazon $279.99 clearance posts exist but are not the main row; Samsung US / "
               "Abt / B&H show no clearance flag — still regular sale. Different size from the "
               '32" M70F (LS32FM703UNXZA). (batch-8 verification 2026-11-21).'),
    dict(key="samsung-odyssey-g73sh-32-black", brand="Samsung", model='Odyssey OLED G7 G73SH 32"',
         variant="Black", category="monitors",
         mpn="LS32HG732SNXZA", upc="198957301674", verified=True,
         sources={"UPC": "Micro Center + Walts + MonitorPug (+ eBay) agree (batch-8 verification 2026-11-21).",
                   "MPN": "Costco Item 2084100 model field + Samsung promo terms Exhibit A + "
                          "Samsung US agree."},
         notes="Costco $699.99 + $100 Costco Shop Card (digital card by email, up to 2 weeks to "
               "process) InStock at add time. Write $699.99 + card note, NOT a $599.99 net "
               "price. Samsung US list $1,099.99. (batch-8 verification 2026-11-21)."),
    dict(key="hisense-qd7-55", brand="Hisense", model='QD7 Series 55"',
         variant='55"', category="tvs",
         mpn="55QD75SFC", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 888143028279 (Hisense official spec PDF hosted on "
                          "Costco gdx-assets only); no second source at add time "
                          "(batch-8 verification 2026-11-21)."},
         notes="MPN 55QD75SFC confirmed (Costco Item 9655750 model field + Hisense spec PDF). "
               "Costco $269.99 (through 11/30/26) at add time; stock mixed — one fetch InStock, "
               "one OutOfStock; costcodrops 2026-11-21 11:50 AM PT said in stock. Stock needs "
               "live-browser / next-refresh confirmation. Do not mix with Best Buy 75QD7QF "
               "(2025 QD7QF series). (batch-8 verification 2026-11-21)."),
    dict(key="asus-rog-strix-xg27ucgr-black", brand="ASUS", model="ROG Strix XG27UCG Gen2",
         variant="Black", category="monitors",
         mpn="XG27UCGR", upc="", verified=False,
         sources={},
         notes="MPN XG27UCGR confirmed (ROG US + ASUS eShop; internal part 90LM0CS0-B013B2). No "
               "UPC lead found anywhere (EU EAN 4711636268141 is a different part number "
               "90LM0CS0-B01371; white XG27UCGR-W GTIN 0199291268227 is a different color; "
               "XG27UCGR-G co-brand EAN 4711636689298 is a different variant). ROG US / ASUS "
               "eShop $399 InStock at add time; Staples $449; Target $425.99. Do NOT borrow the "
               "XG27UCG UPC 197105564633. (batch-8 verification 2026-11-21)."),
    dict(key="lenovo-legion-pro-7-gen-10-83ru0006us", brand="Lenovo", model="Legion Pro 7 Gen 10",
         variant="Eclipse Black", category="laptops",
         mpn="83RU0006US", upc="199271660232", verified=True,
         sources={"UPC": "PSREF PDF (EAN / UPC / JAN: 199271660232) + CompSource + "
                          "SimplifiedComputers + Venditore + Bonanza agree (batch-8 verification 2026-11-21).",
                   "MPN": "Best Buy model field (SKUs 12629843, 13259871) + PSREF PDF + CompSource agree."},
         notes="Adorama $4,949.00 InStock at add time. Best Buy same price is Sold and shipped by "
               "Adorama marketplace, not a Best Buy row. Newegg $4,495.62 seller identity "
               "unverified, not used. PSREF shows TopSeller: No (draft said TopSeller — "
               "corrected, does not affect UPC). Config pinned: Ryzen 9 9955HX3D / RTX 5080 16GB "
               "/ 32GB DDR5-5600 / 2TB PCIe Gen5 / 16-inch WQXGA OLED 240Hz / Win 11 Pro. Do not "
               "mix with the 1TB config ($2,849.99, expired) or 83RU0005US (RAM disputed). "
               "(batch-8 verification 2026-11-21)."),
    dict(key="alienware-16-aurora-lac16250-7469blu-blue", brand="Alienware", model="16 Aurora",
         variant="Blue", category="laptops",
         mpn="LAC16250-7469BLU-PUS", upc="884116430469", verified=True,
         sources={"UPC": "D&H Consumer spec table + Product Setup - New Age spec table + "
                          "Electronic Express + B&H agree (batch-8 verification 2026-11-21).",
                   "MPN": "AntOnline (Manufacturer Part Number LAC16250-7469BLU-PUS) + Best Buy "
                          "model field + Newegg agree."},
         notes="Live row B&H $1,549.00 In Stock at add time (top-tier retailer, $600.99 below "
               "AntOnline $2,149.99 — AntOnline row superseded; HOLD on AntOnline lifted "
               "2026-11-21, B&H row adopted instead). Best Buy SKU 13279039 Sold Out; Dell.com "
               "configurator $2,699.99 list is a different 32GB config. Config pinned: Core 7 "
               "240H / RTX 5060 8GB / 16GB DDR5-5600 / 1TB / 16-inch WQXGA 120Hz / Win 11 Home. "
               "B&H lists the lid as Interstellar Indigo, 5.67 lb vs D&H 5.49 lb — same SKU "
               "(URL + UPC), wording only. (batch-8 verification 2026-11-21)."),
    dict(key="lenovo-loq-essential-15arp11-83va001pus", brand="Lenovo", model="LOQ Essential 15ARP11",
         variant="Eclipse Black", category="laptops",
         mpn="83VA001PUS", upc="", verified=False,
         sources={"MPN": "MPN pending — 83VA001PUS single source (Best Buy model field, SKU "
                          "6673556); lenovo.com US shows LOQ Essential 15IRH11 (Intel), not "
                          "15ARP11; no B&H hit (batch-8 verification 2026-11-21)."},
         notes="Best Buy $1,049.99 (Comp. Value $1,499.99) InStock at add time. Best Buy title "
               "says 2K but the spec panel says FHD 1920x1080 144Hz — panel governs. $999.99 "
               "Black Friday variant and $1,299.00 PC Heaven marketplace SKU not used. "
               "(batch-8 verification 2026-11-21)."),
    dict(key="asus-rog-zephyrus-g14-ga403um-r9hx4-white", brand="ASUS", model="ROG Zephyrus G14 (2025)",
         variant="Platinum White", category="laptops",
         mpn="GA403UM-G14.R9HX4", upc="", verified=False,
         sources={"MPN": "MPN pending — GA403UM-G14.R9HX4 single source (Best Buy model field, "
                          "SKU 6629420); Velztorm marketplace / Smartprix / Slickdeals are not "
                          "qualifying second sources; no B&H / ASUS US store hit "
                          "(batch-8 verification 2026-11-21)."},
         notes="Best Buy $2,299.99 InStock at add time. Open-box $1,154.99 / $1,085.99 / "
               "$1,015.99 and Velztorm Upgraded rows excluded; Tom's Guide $1,349 is a 2025-07 "
               "old price. (batch-8 verification 2026-11-21)."),
    dict(key="hp-omen-transcend-14-14-fb1043dx-black", brand="HP", model="OMEN Transcend 14",
         variant="Shadow Black", category="laptops",
         mpn="14-fb1043dx", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 821844495667 (HP datasheet PDF only); no second "
                          "source at add time (batch-8 verification 2026-11-21)."},
         notes="MPN 14-fb1043dx / D8KM3UA#ABA confirmed (Best Buy model field, SKU 6672941 + HP "
               "datasheet PDF). Best Buy $2,499.99 InStock at add time (list price, no promo; "
               "Win 11 Home confirmed, not Pro). Do not mix with 32GB 14-fb1013dx (Best Buy "
               "dead). (batch-8 verification 2026-11-21)."),
    dict(key="samsung-galaxy-book5-360-15-np750qha-ka1us-gray", brand="Samsung", model='Galaxy Book5 360 15.6"',
         variant="Gray", category="laptops",
         mpn="NP750QHA-KA1US", upc="", verified=False,
         sources={},
         notes="MPN NP750QHA-KA1US confirmed (Best Buy model field + Quill + Connection + "
               "Staples, four sources). No UPC lead found. Connection $1,695.95 In Stock "
               "(Ships in 1–2 Business Days) / Quill $1,702.99 InStock at add time — tier "
               "accepted: both are US direct online retailers (PC Connection, Staples-owned "
               "Quill) selling direct to consumers; two independent rows agree at about $1,700. "
               "Best Buy $358.99 clearance vs $2,187.81 conflict both Unavailable, irrelevant. "
               "Staples $1,419.69 out of stock (193+ days old). (batch-8 verification 2026-11-21)."),
    dict(key="lenovo-yoga-7i-2-in-1-14-83tc003xus-luna-grey", brand="Lenovo", model='Yoga 7i 2-in-1 14" Gen 11',
         variant="Luna Grey", category="laptops",
         mpn="83TC003XUS", upc="", verified=False,
         sources={"UPC": "UPC pending — lead 199275077982 (TekFeed aggregator only); Newegg shows "
                          "the code only as a third-party bundle listing internal model# prefix, "
                          "not a retailer spec page for this SKU; PSREF 14IPH11 not found "
                          "(batch-8 verification 2026-11-21)."},
         notes="MPN 83TC003XUS confirmed (Best Buy model field, SKU 6671007 + Newegg + "
               "NotebookCheck). Best Buy $999.99 (Save $650, Comp. Value $1,649.99) InStock at "
               "add time. Open-box $765.99–$812.99, refurb $1,199.99 (IST Computers) and "
               "Upgraded marketplace rows excluded. Do not mix with Yoga 7i 16-inch 83JT0000US "
               "or 83TE0004US. (batch-8 verification 2026-11-21)."),
    dict(key="dell-xps-13-ldx13260-5960sky-sky", brand="Dell", model="XPS 13 (2026)",
         variant="Sky", category="laptops",
         mpn="LDX13260-5960SKY-PUS", upc="", verified=False,
         sources={"MPN": "MPN pending — LDX13260-5960SKY-PUS (Best Buy model field, SKU 6683772 + "
                          "retail box photos); no second retailer (-PUS is a Best Buy retail SKU; "
                          "dell.com configurator does not carry it) (batch-8 verification 2026-11-21).",
                   "UPC": "UPC pending — lead 884116652960 (eBay listing item 327296803592 + "
                          "mirrors only); no retailer/distributor second source "
                          "(batch-8 verification 2026-11-21)."},
         notes="Best Buy $999.99 InStock at add time. Slickdeals $699.99 expired (promo ended "
               "Nov 18) — not written. Best Buy SKU 13223232 $969.00 seller unknown, not used. "
               "Title says 3K but spec panel says 2560x1600 (2.5K) 120Hz — panel governs. Do not "
               "mix with 8GB LDX13260-5953SKY-PUS. (batch-8 verification 2026-11-21)."),
    dict(key="dji-osmo-action-5-pro-standard-combo-black", brand="DJI", model="Osmo Action 5 Pro Standard Combo",
         variant="Black", category="action-cameras",
         mpn="CP.OS.00000377.01", upc="190021114616", verified=True,
         sources={"UPC": "B&H spec page + Micro Center spec table (SKU 754903) agree "
                          "(batch-8 verification 2026-11-21).",
                   "MPN": "B&H URL slug + Micro Center Mfr Part # agree."},
         notes="B&H $319.00 In Stock at add time; Micro Center $319.99. "
               "(batch-8 verification 2026-11-21)."),
    dict(key="dji-osmo-pocket-3-black", brand="DJI", model="Osmo Pocket 3",
         variant="Black", category="cameras",
         mpn="CP.OS.00000301.01", upc="190021094970", verified=True,
         sources={"UPC": "B&H spec page + NFM agree (batch-8 verification 2026-11-21).",
                   "MPN": "B&H (BH # DJOP3) + Crutchfield MFR # agree; different from Creator "
                          "Combo CP.OS.00000302.01."},
         notes="B&H $373.00 (was $439.00) In Stock at add time; Best Buy same price $373 (Sold "
               "by Best Buy). Amazon $373 is corroboration only, not a price source. "
               "(batch-8 verification 2026-11-21)."),
    dict(key="dji-mini-5-pro-rc-n3-gray", brand="DJI", model="Mini 5 Pro",
         variant="Gray", category="drones",
         mpn="CP.MA.00000838.03", upc="190021121126", verified=True,
         sources={"UPC": "B&H spec page + Target product page (TCIN 1012392891) agree "
                          "(batch-8 verification 2026-11-21).",
                   "MPN": "B&H URL slug + Adorama MFR agree (Adorama K suffix is its bundle SKU, "
                          "not taken)."},
         notes="B&H $759.00 In Stock at add time. New category: drones (user-approved batch 8). "
               "Slickdeals posts are AliExpress prices ($508–$825) — heat signal only, not a "
               "price source. (batch-8 verification 2026-11-21)."),
    dict(key="dji-neo-2-drone-only-gray", brand="DJI", model="Neo 2",
         variant="Gray", category="drones",
         mpn="CP.FP.00000270.01", upc="190021157224", verified=True,
         sources={"UPC": "B&H spec page + Target product page (TCIN 1015573677) + Visions CA agree "
                          "(batch-8 verification 2026-11-21).",
                   "MPN": "Adorama MFR + B&H URL slug + Visions CA agree."},
         notes="B&H $259.00 In Stock / Adorama $259.00 In Stock at add time. New category: drones "
               "(user-approved batch 8). Neo 2 is not on DJI US direct (UFLPA customs) — US rows "
               "are authorized dealers (B&H, Adorama, djiusa.com), still retailer-direct. "
               "(batch-8 verification 2026-11-21)."),
    dict(key="insta360-x5-standard-bundle-black", brand="Insta360", model="X5 Standard Bundle",
         variant="Black", category="action-cameras",
         mpn="CINSAAHA_X501", upc="842126110955", verified=True,
         sources={"UPC": "B&H spec page + NFM agree; B&H Motorcycle Bundle parts list also "
                          "carries the same UPC (batch-8 verification 2026-11-21).",
                   "MPN": "B&H URL slug + NFM Model field agree."},
         notes="B&H $439.99 (was $549.99) In Stock at add time; Insta360 US store $439.99; "
               "Target $439.99. Do not mix with the Best Buy / Costco X5 Bundle (MPN CINSAAHA, "
               "UPC 842126113239, different bundle SKU). (batch-8 verification 2026-11-21)."),
    dict(key="insta360-x6-standard-bundle-midnight-black", brand="Insta360", model="X6 Standard Bundle",
         variant="Midnight Black", category="action-cameras",
         mpn="CINSABXA-X601", upc="842126120213", verified=True,
         sources={"UPC": "Micro Center spec table + Visions CA agree (batch-8 verification 2026-11-21).",
                   "MPN": "Micro Center Mfr Part # + Visions CA agree; B&H slug cinsabxa_x602 is "
                          "the Arctic White X602, not mixed."},
         notes="Live row B&H $629.99 (was $699.99, Holiday Savings $70) In Stock at add time — "
               "draft $699.99 list price corrected. Adorama $699.99 InStock as secondary "
               "reference. B&H also lists EAN 6942590200337 (different numbering system); UPC "
               "used, EAN not written. (batch-8 verification 2026-11-21)."),
    dict(key="gopro-hero13-black-black", brand="GoPro", model="HERO13 Black",
         variant="Black", category="action-cameras",
         mpn="CHDHX-131-TH", upc="810116381821", verified=True,
         sources={"UPC": "B&H spec page + The Pixel Hub barcode field agree (batch-8 verification 2026-11-21).",
                   "MPN": "B&H (BH # GOH13BLK) + Berger Bros SKU agree."},
         notes="B&H $349.99 (was $429.99) Temporarily Out of Stock at add time, expected "
               "availability Dec 07, 2026 — row is out of stock, identifiers verified. Scuba "
               "CHDHX-131-RW / UPC 810116381616 variant not verified, not attached to this "
               "model. (batch-8 verification 2026-11-21)."),
    dict(key="insta360-go-3s-standard-bundle-128gb-midnight-black", brand="Insta360", model="GO 3S Standard Bundle 128GB",
         variant="Midnight Black", category="action-cameras",
         mpn="CINSAATA_GO3S13", upc="842126106989", verified=True,
         sources={"UPC": "B&H spec page + Micro Center spec table (SKU 721472) agree "
                          "(batch-8 verification 2026-11-21).",
                   "MPN": "B&H slug + Micro Center Mfr Part # + CompSource agree."},
         notes="B&H $299.99 (was $379.99) In Stock at add time; Micro Center $299.99. Do not mix "
               "with Target GO 3S Action Bundle (UPC 842126107641) or B&H Camera Only "
               "(CINSAATA_GO3S11, UPC 842126106965). (batch-8 verification 2026-11-21)."),
    dict(key="asus-rog-delta-ii-white", brand="ASUS", model="ROG Delta II",
         variant="Moonlight White", category="headphones",
         mpn="", upc="", verified=False,
         sources={"MPN": "MPN pending — conflict: Newegg US lists 90YH03W0-BHAA10, SG/EU channels "
                          "list 90YH03W0-BHUA10 (suspected US vs APAC suffix split); do not choose "
                          "(batch-8 verification 2026-11-21).",
                   "UPC": "UPC pending — lead 197105907362 (SG channels only, no US retailer spec "
                          "page); 197105907355 is FALSIFIED (Ubuy misattribution — ASIN B0DGZY13L6 "
                          "is the Black model, UPC 197105604858); 197105604858 is the Black "
                          "model's UPC, not this one (batch-8 verification 2026-11-21)."},
         notes="Best Buy $149.99 (Black Friday Deal, comp $229.99) InStock at add time, SKU "
               "6637821, Model A701 ROG DELTA II/WHT. Best Buy spec page could not be expanded "
               "in text fetch — UPC needs live-browser See all specifications check. Different "
               "color from the Black model (asus-rog-delta-ii-black, pending). "
               "(batch-8 verification 2026-11-21)."),
    dict(key="asus-rog-keris-ii-ace-white", brand="ASUS", model="ROG Keris II Ace",
         variant="Moonlight White", category="mice",
         mpn="", upc="", verified=False,
         sources={"MPN": "MPN pending — conflict found at add time: ASUS eShop US white page lists "
                          "90MP03N0-BMAA10 ($159.99) vs IPCStore/PBTech/SquareDeals 90MP03N0-BMUA10; "
                          "same US/APAC suffix shape as Delta II; downgraded from VERIFIED at add "
                          "time 2026-11-21.",
                   "UPC": "UPC pending — conflict: 197105394612 (PBTech NZ / SquareDeals SG / "
                          "Dynacore SG / Carousell SG, bound to BMUA10) vs 197105394582 (Amazon "
                          "ASIN B0D3CX3QMD data + SpaceBoundSolutions US distributor, item "
                          "1017783); both check digits valid — needs a US retailer spec page to "
                          "decide (batch-8 verification 2026-11-21)."},
         notes="IPCStore $179.00 in stock at add time (US retailer, MPN-bound listing). ASUS "
               "eShop $94.99 Starting at does NOT cover White (white page BMAA10 is $159.99); "
               "Best Buy $182.43 is antonline marketplace (excluded); Target $129.99 "
               "OutOfStock. Different color from the Black model (asus-rog-keris-ii-ace-black, "
               "pending). (batch-8 verification 2026-11-21)."),
    dict(key="asus-rog-strix-scope-ii-96-wireless-white-nx-storm", brand="ASUS", model="ROG Strix Scope II 96 Wireless",
         variant="Moonlight White", category="keyboards",
         mpn="90MP037B-BKAA30", upc="", verified=False,
         sources={"MPN": "MPN pending — 90MP037B-BKAA30 single source (ASUS eShop US white Storm "
                          "page, Product Name X901 SCOPE II 96 WL/WHT/NXSM/CA/PBT); eShop Color "
                          "field reads Black (template mismatch), Product Name /WHT/ governs "
                          "(batch-8 verification 2026-11-21).",
                   "UPC": "UPC pending — lead 197105487154 (Target spec page + Newegg Model # + "
                          "Snapklik agree on the model string, but Target page is Target Plus "
                          "Partner marketplace info and no US retailer spec table backs it) "
                          "(batch-8 verification 2026-11-21)."},
         notes="ASUS eShop US $131.99 InStock at add time. Best Buy only carries the Snow "
               "(linear) white model (SKU 6595753, $109.99) — different switch, do not mix. NX "
               "Snow white (90MP037A-BKAA30, Canada eShop) not selected (no US UPC; EU EANs are "
               "non-US). Newegg $129.99–$149.99 is a from range, seller unclear, not the main "
               "row. (batch-8 verification 2026-11-21)."),
    dict(key="asus-zenwifi-bt8-3-pack-white", brand="ASUS", model="ZenWiFi BT8 3-pack",
         variant="White", category="routers",
         mpn="BT8(W-3-PK)", upc="197105532090", verified=True,
         sources={"UPC": "B&H spec page (retailer) + SHI distributor UPC field agree "
                          "(batch-8 verification 2026-11-21).",
                   "MPN": "ASUS US Tech Specs (BT8(W-3-PK) / BT8(W-2-PK) / BT8(W-1-PK)) + "
                          "Microless agree."},
         notes="B&H $699.99 (was $849.99, Holiday Savings $150) InStock at add time; ASUS eShop "
               "US same price $699.99. Independent model from the 2-pack "
               "(asus-zenwifi-bt8-2-pack-white, verified, UPC 197105532045). "
               "(batch-8 verification 2026-11-21)."),
    dict(key="asus-zenwifi-bt10-1-pack-white", brand="ASUS", model="ZenWiFi BT10 1-pack",
         variant="White", category="routers",
         mpn="BT10(W-1-PK)", upc="197105429833", verified=True,
         sources={"UPC": "B&H spec page (retailer) + DirectDial distributor (MFG PART BT10(W-1-PK) "
                          "+ UPC) agree (batch-8 verification 2026-11-21).",
                   "MPN": "ASUS US Tech Specs + DirectDial manufacturer part number agree."},
         notes="B&H $346.00 In Stock at add time; ASUS US $359.99. Independent model from the "
               "2-pack (asus-zenwifi-bt10-2-pack-white, pending, lead UPC 197105429895); 1-pack "
               "UPC …9833 vs 2-pack lead …9895, do not mix. (batch-8 verification 2026-11-21)."),
    dict(key="asus-tuf-gaming-m3-gen-ii-black", brand="ASUS", model="TUF Gaming M3 Gen II",
         variant="Black", category="mice",
         mpn="", upc="", verified=False,
         sources={"MPN": "MPN pending — conflict found at add time: Newegg Model # + B&H MFR # "
                          "list 90MP0320-BMAA00, but the ASUS eShop US in-stock page lists Part "
                          "Number 90MP0320-BMAA03 (same product name P309 TUF GAMING M3 GEN II); "
                          "suspected replacement SKU / version change; downgraded from VERIFIED "
                          "at add time 2026-11-21.",
                   "UPC": "UPC pending — lead 195553909112 FALSIFIED at add time: PBTech NZ + "
                          "NationalPC India bind it to the non-US MPN 90MP0320-BMUA00 (with EAN "
                          "4711081909118), not the US BMAA00 — lead void, no valid lead "
                          "(batch-8 verification 2026-11-21)."},
         notes="Adorama $25.99 InStock at add time; ASUS eShop $24.99 now InStock (draft said out "
               "of stock — corrected) and is the cheaper direct row. B&H discontinued (old "
               "$28.64). Newegg self-operated $22.99 (WorstDealsEver, 2026-10-26) not live "
               "re-verified. No M3 Gen II in the catalog before (only TUF M4 Air and TUF K3 Gen "
               "II). (batch-8 verification 2026-11-21)."),
    dict(key="8bitdo-sn30-pro-hall-effect-g-classic", brand="8BitDo", model="SN30 Pro",
         variant="G Classic", category="controllers",
         mpn="80DJ04", upc="", verified=False,
         sources={"MPN": "MPN pending — 80DJ04 single source (Best Buy model field); grey is "
                          "80DM02, a different model (batch-8 verification 2026-11-21).",
                   "UPC": "UPC/EAN pending — lead 6922621509547 (13-digit EAN, Target spec page "
                          "only); no second source (B&H does not carry it) "
                          "(batch-8 verification 2026-11-21)."},
         notes="Best Buy $34.99 (Black Friday Deal, comp $44.99) InStock at add time, SKU 6590319, "
               "Sold by Best Buy. Target $44.99 InStock as second row. Best Buy SKU 10189263 "
               "also lists Model 80DJ04 but no page was found — relationship unconfirmed. Hall "
               "Effect version pinned by with Hall Effect Joysticks + Model 80DJ04; do not mix "
               "with the old non-Hall-Effect version. (batch-8 verification 2026-11-21)."),
    dict(key="microsoft-xbox-wireless-controller-forza-horizon-6-limited-edition", brand="Microsoft", model="Xbox Wireless Controller Forza Horizon 6 Limited Edition",
         variant="Forza Horizon 6 LE", category="controllers",
         mpn="EP2-42276", upc="196388601059", verified=True,
         sources={"UPC": "GameStop US retailer spec page (UPC + Vendor PN EP2-42276) + goWholesale "
                          "distributor agree (batch-8 verification 2026-11-21).",
                   "MPN": "Walmart Model field + GameStop Vendor Part Number + Lenovo US "
                          "Manufacturer PN agree."},
         notes="Walmart $49.00 (was $84.00) sold/shipped by Walmart at add time. Limited Edition "
               "but widely in stock at Walmart/Best Buy/GameStop, not clearance — included per "
               "user approval (batch 8). Target $74.99 InStock as backup row. GameStop own price "
               "$89.99/$69.99 Currently Unavailable, not a row. Different colorway from the "
               "standard Black controller (xbox-wireless-controller-black). "
               "(batch-8 verification 2026-11-21)."),
]


def _wrap(s, indent):
    """Split a string into <=95-char chunks joined by implicit concatenation."""
    if len(s) <= 95:
        return '"%s"' % s.replace('\\', '\\\\').replace('"', '\\"')
    chunks = textwrap.wrap(s, width=95, break_long_words=False, break_on_hyphens=False)
    out = []
    for c in chunks:
        out.append('"%s"' % c.replace('\\', '\\\\').replace('"', '\\"'))
    return ("\n" + " " * indent).join(out)


def render(e):
    lines = ["    EvalProduct("]
    lines.append('        key="%s",' % e["key"])
    lines.append('        brand="%s",' % e["brand"].replace('\\', '\\\\').replace('"', '\\"'))
    lines.append('        model=%s,' % _wrap(e["model"], 8))
    lines.append('        variant=%s,' % _wrap(e["variant"], 8))
    lines.append('        category="%s",' % e["category"])
    if e["verified"]:
        lines.append("        identifiers={")
        lines.append('            "UPC": "%s",' % e["upc"])
        lines.append('            "MPN": "%s",' % e["mpn"])
        lines.append("        },")
    else:
        lines.append("        identifiers={},")
    if e["sources"]:
        lines.append("        identifier_sources={")
        for k, v in e["sources"].items():
            lines.append('            "%s": %s,' % (k, _wrap(v, 12)))
        lines.append("        },")
    else:
        lines.append("        identifier_sources={},")
    lines.append('        status="%s",' % ("verified" if e["verified"] else "pending"))
    lines.append('        notes=%s,' % _wrap(e["notes"], 8))
    lines.append("    ),")
    return "\n".join(lines)


def main():
    # Sanity: keys must match the TSV exactly, no dupes, 50 rows.
    import csv
    tsv = list(csv.DictReader(open("data/rework8/candidates_batch8_50.tsv"), delimiter="\t"))
    tsv_keys = [r["key"] for r in tsv]
    assert len(tsv_keys) == 50 and len(set(tsv_keys)) == 50, "TSV key count wrong"
    assert set(tsv_keys) == {e["key"] for e in ENTRIES}, "ENTRY keys != TSV keys"
    assert len(ENTRIES) == 50
    # Per-entry sanity: verified entries need both codes; pending need none in identifiers.
    for e in ENTRIES:
        if e["verified"]:
            assert e["upc"] and e["mpn"], e["key"]
        assert e["key"] not in open(CATALOG).read(), "key already in catalog: " + e["key"]
    src = open(CATALOG).read()
    idx = src.index("\ndef get_product")
    end = src.rindex("\n]", 0, idx)  # the \n before the ] closing EVAL_SET
    block = "    # --- Batch 8 (2026-11-21, user-approved draft; add-time re-verification) ---\n"
    block += "\n".join(render(e) for e in ENTRIES) + "\n"
    src = src[:end] + "\n" + block + src[end + 1:]
    open(CATALOG, "w").write(src)
    # Verify by import.
    import sys
    sys.path.insert(0, ".")
    from price_agent.catalog import EVAL_SET
    ver = sum(1 for p in EVAL_SET if p.status == "verified")
    pen = sum(1 for p in EVAL_SET if p.status == "pending")
    print("total=%d verified=%d pending=%d" % (len(EVAL_SET), ver, pen))
    assert len(EVAL_SET) == 600 and ver == 255 and pen == 345, "counts wrong"
    # Verify the new drones category landed.
    drones = [p.key for p in EVAL_SET if p.category == "drones"]
    print("drones:", drones)
    assert len(drones) == 2
    print("OK: 50 entries appended")


if __name__ == "__main__":
    main()
