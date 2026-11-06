"""Phase 1 evaluation set: 52 standardized electronics models, US market.

Identifier policy (DECISIONS 002): an identifier is recorded only when a
retailer or manufacturer listing states it for the exact pinned variant.
Color and bundle variants get different UPCs, so every verified entry
pins its variant. Entries without a verified identifier keep
``identifiers={}`` and status ``"pending"``; they must never enter the
matched ranking on title similarity alone.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class EvalProduct:
    key: str
    brand: str
    model: str
    variant: str  # pinned variant, or "unpinned" while not yet verified
    category: str
    identifiers: dict[str, str] = field(default_factory=dict)
    identifier_sources: dict[str, str] = field(default_factory=dict)
    status: str = "pending"  # "verified" or "pending"
    notes: str = ""


EVAL_SET: list[EvalProduct] = [
    # --- Verified identifiers (2026-10-31, retailer/manufacturer listings) ---
    EvalProduct(
        key="sony-wh1000xm5-black",
        brand="Sony",
        model="WH-1000XM5",
        variant="Black (WH1000XM5/B)",
        category="headphones",
        identifiers={"UPC": "027242923232"},
        identifier_sources={
            "UPC": "Abt + B&H Photo listings agree for WH1000XM5/B (silver is a "
            "different UPC, 027242923249)"
        },
        status="verified",
    ),
    EvalProduct(
        key="apple-airpods-pro-3",
        brand="Apple",
        model="AirPods Pro 3",
        variant="White (MFHP4LL/A)",
        category="earbuds",
        identifiers={"UPC": "195950543698", "MPN": "MFHP4LL/A"},
        identifier_sources={
            "UPC": "Best Buy US + eBay GTIN agree for MFHP4LL/A "
            "(Pro 2 Lightning MQD83AM/A is the previous generation; "
            "refurbished-only codes excluded)"
        },
        status="verified",
    ),
    EvalProduct(
        key="logitech-mx-master-4-graphite",
        brand="Logitech",
        model="MX Master 4",
        variant="Graphite, standard edition (910-007558)",
        category="mice",
        identifiers={"UPC": "097855207623", "MPN": "910-007558"},
        identifier_sources={
            "UPC": "CamelCamelCamel (ASIN B0FC5SJNQX, Model 910-007558) "
            "+ WantItAll spec (ItemPartNumber 910-007558, Graphite) "
            "agree. Part map: Graphite 910-007558, Pale Gray "
            "910-007559, Black 910-007560 (Avadirect + MCS spec "
            "tables). Logitech US direct URL pins Graphite to "
            "910-007558. 910-007562 and 910-007565 are different "
            "codes and were excluded."
        },
        notes="Replaces logitech-mx-master-3s-graphite (retired "
        "2026-11-01, user-confirmed, DECISIONS 017): the 3S "
        "standard edition is no longer listed in Logitech's "
        "consumer catalog (BUILD_LOG 024). The old key is "
        "retired, never reused.",
        status="verified",
    ),
    EvalProduct(
        key="nintendo-switch-oled-white",
        brand="Nintendo",
        model="Switch - OLED Model",
        variant="White set (SKU 115461)",
        category="consoles",
        identifiers={"UPC": "045496883386", "SKU": "115461"},
        identifier_sources={
            "UPC": "Nintendo official store (shown as GTIN 00045496883386; "
            "UPC-A form 045496883386)"
        },
        status="verified",
    ),
    EvalProduct(
        key="bose-qc-ultra-2-black",
        brand="Bose",
        model="QuietComfort Ultra Headphones (2nd Gen)",
        variant="Black (890101-0100)",
        category="headphones",
        identifiers={"UPC": "017817859585", "MPN": "890101-0100"},
        identifier_sources={
            "UPC": "Amazon listings agree for 890101-0100 (White Smoke is "
            "017817859561; 1st-gen White Smoke is 017817846141)"
        },
        status="verified",
    ),
    EvalProduct(
        key="samsung-buds4-pro-white",
        brand="Samsung",
        model="Galaxy Buds4 Pro",
        variant="White, US version (SM-R640NZWAXAR)",
        category="earbuds",
        identifiers={"UPC": "198957273582", "MPN": "SM-R640NZWAXAR"},
        identifier_sources={
            "UPC": "Best Buy spec + distributor catalog (channelonline, "
            "GTIN 0198957273582, same code) + T-Mobile URL sku agree "
            "for SM-R640NZWAXAR (Amazon SM-R640NZWFXAR / 198957273568 "
            "is a different variant, excluded; MEA and Latino Americana "
            "suffixes excluded)"
        },
        status="verified",
    ),
    # --- Further verified identifiers ---
    EvalProduct(key="sony-wf1000xm5-black", brand="Sony",
                model="WF-1000XM5", variant="Black (WF1000XM5/B)",
                category="earbuds",
                identifiers={"UPC": "027242925601"},
                identifier_sources={
                    "UPC": "Adorama + Amazon US + Abt + eBay agree for WF1000XM5/B "
                    "(international version and bundles carry different UPCs)"
                },
                status="verified"),
    EvalProduct(key="apple-airpods-5-usbc", brand="Apple",
                model="AirPods 5", variant="USB-C case (MKFW4LL/A)",
                category="earbuds",
                identifiers={"UPC": "195951378978", "MPN": "MKFW4LL/A"},
                identifier_sources={
                    "UPC": "B&H Photo spec (195951378978) + eBay US "
                    "product identifiers (GTIN 0195951378978, the same "
                    "code) agree for MKFW4LL/A. Best Buy US confirms "
                    "Model MKFW4LL/A, SKU 6376553, $129. Wireless "
                    "charging case MKFT4LL/A ($149) and AU MKFT4X/A "
                    "are different variants."
                },
                notes="Replaces apple-airpods-4-usbc (retired 2026-10-31, "
                "user-confirmed, DECISIONS 014): AirPods 4 is no longer "
                "available on apple.com (BUILD_LOG 020). The old key "
                "is retired, never reused.",
                status="verified"),
    EvalProduct(key="apple-watch-se3-40mm", brand="Apple",
                model="Watch SE 3 (40mm, GPS)", variant="Midnight, GPS (MEH94LW/A)",
                category="wearables",
                identifiers={"UPC": "195950387070", "MPN": "MEH94LW/A"},
                identifier_sources={
                    "UPC": "Multiple eBay listings agree for MEH94LW/A "
                    "(Best Buy's current GPS 40mm Midnight listings are Navy "
                    "Blue band variants MJL14LW/A / MJKY4LW/A; band detail "
                    "to be pinned at snapshot time)"
                },
                notes="MEH94LW/A mapping corroborated 2026-10-31 by a Best Buy "
                    "refurbished listing (GPS 40mm Midnight, S/M, Midnight Sport "
                    "Band, model MEH94LW/A shown); no new-unit page displaying "
                    "MEH94LW/A found that day, so new-unit quotes are still 0 "
                    "(refurbished excluded per DECISIONS 006).",
                status="verified"),
    EvalProduct(key="kindle-paperwhite-16gb-2024", brand="Amazon",
                model="Kindle Paperwhite (16GB, 2024)",
                variant="Black, 16GB (B0CFPL6CFY)",
                category="e-readers",
                identifiers={"UPC": "840268942847", "MPN": "B0CFPL6CFY"},
                identifier_sources={
                    "UPC": "PBTech NZ/AU listing for B0CFPL6CFY (single seller; "
                    "color/storage variants differ)"
                },
                notes="Update 2026-10-31: amazon.com refused AI-agent "
                "access (Conditions of Use wall) during the small- "
                "brands sweep (BUILD_LOG 025); official currency "
                "unverified. Entry unchanged — neither confirmed nor "
                "removed on this basis; needs live-browser takeover or "
                "a retailer currency check.",
                status="verified"),
    EvalProduct(key="logitech-mx-keys-s-pale-grey", brand="Logitech",
                model="MX Keys S", variant="Pale Grey (920-011559)",
                category="keyboards",
                identifiers={"UPC": "097855187857", "MPN": "920-011559"},
                identifier_sources={
                    "UPC": "Amazon + distributor listings agree for 920-011559. "
                    "Correction: 920-011559 is Pale Grey, not Graphite "
                    "(Graphite is 920-011406); the eval entry was renamed."
                },
                status="verified"),
    EvalProduct(key="keychron-k8-ultra-8k", brand="Keychron",
                model="K8 Ultra 8K",
                variant="Fully Assembled, Black, Apex Red (K8U-J1)",
                category="keyboards",
                identifiers={"EAN": "4894979057969", "SKU": "K8U-J1"},
                identifier_sources={
                    "EAN": "Keychron official store public product "
                    "JSON, browser-verified 2026-11-01 (Red K8U-J1 "
                    "barcode 4894979057969; Brown K8U-J3 "
                    "4894979057976; Banana K8U-J4 4894979057983). "
                    "JSON field is named 'barcode' (no separate "
                    "GTIN/UPC/EAN field); recorded as EAN following "
                    "the K8 Pro precedent (13-digit barcodes).",
                    "SKU": "Keychron official product page, "
                    "browser-verified 2026-11-01: Red K8U-J1 "
                    "(page default), Brown K8U-J3, Banana K8U-J4, "
                    "all $119.99, all stocked in the US warehouse. "
                    "Old-K8 barcodes (753610396260, 617748997846) "
                    "belong to the original K8, not the Ultra 8K, "
                    "and were excluded."
                },
                notes="Replaces keychron-k8-pro (retired 2026-11-01, "
                "user-confirmed, DECISIONS 019): the K8 Pro is "
                "listed on keychron.com but sold out (BUILD_LOG "
                "025); the page points to K8 HE & K8 Ultra 8K as "
                "successors. The old key is retired, never "
                "reused; the old $49.99 quote is NOT carried over "
                "(different product). Brown and Banana switches "
                "share the $119.99 price on the same page.",
                status="verified"),
    EvalProduct(key="nintendo-switch-lite-turquoise", brand="Nintendo",
                model="Switch Lite", variant="Turquoise (HDHSBAZAA)",
                category="consoles",
                identifiers={"UPC": "045496882266", "MPN": "HDHSBAZAA"},
                identifier_sources={
                    "UPC": "eBay + Desertcart + Ubuy agree for HDHSBAZAA "
                    "(Nintendo Canada refurbished SKU 113304 is a different code)"
                },
                status="verified"),
    EvalProduct(key="sony-dualsense-white", brand="Sony",
                model="DualSense Wireless Controller", variant="White",
                category="controllers",
                notes="UPC conflict unresolved: Amazon US 711719574293 vs "
                "NZ/AU PBTech 711719575856 vs other 711719541080; needs a "
                "second check against a US manufacturer/retailer page; "
                "left unverified for now. Update 2026-10-31: Best Buy "
                "spec-comparison table gives a FOURTH code, 711719023197, "
                "for the standard White column (other columns: Chroma Teal "
                "711719022497, GTA VI LE 711719072683, 007 LE 711719027119); "
                "still pending, no code promoted without a tiebreaker "
                "(physical box barcode or Sony spec sheet). Second update "
                "2026-10-31: a FIFTH code, 711719541226, appears on eBay "
                "and a refurbished-goods store; Amazon/Camel code "
                "711719574293 is tied to model CFI-ZCT1W. Still no "
                "tiebreaker; entry stays pending. Third update "
                "2026-10-31: Sony official-catalog sweep (BUILD_LOG "
                "022) confirms the model is current (PlayStation "
                "Direct $74.00) but no official Sony/PlayStation page "
                "states a UPC, and none of the five codes appears on "
                "official pages. PlayStation Support does list "
                "CFI-ZCT1W as a DualSense model code (manuals page + "
                "serial-number article), but neither page ties it to "
                "White or states a UPC — model code confirmed in "
                "general, not white-specific; UPC conflict stays "
                "unresolved; entry stays pending."),
    EvalProduct(key="xbox-wireless-controller-black", brand="Microsoft",
                model="Xbox Wireless Controller",
                variant="Carbon Black, Series X|S (1914)",
                category="controllers",
                identifiers={"UPC": "196388518159", "MPN": "1914"},
                identifier_sources={
                    "UPC": "PayMore + eBay listings agree for 1914 Carbon Black "
                    "(older QAT-00001 code 0889842611588 and another PayMore "
                    "code 889842654776 excluded as different revisions)"
                },
                status="verified"),
    EvalProduct(key="meta-quest-3s-128gb", brand="Meta",
                model="Quest 3S (128GB)", variant="128GB (SK-1000926-01)",
                category="vr",
                identifiers={"UPC": "815820025825", "MPN": "SK-1000926-01"},
                identifier_sources={
                    "UPC": "B&H Photo + Amazon US + PayMore agree for SK-1000926-01 "
                    "(SG SK-1000815-01, NZ SK-1000207-01, renewed SK-1000253-01 "
                    "and Target refurbished codes are different SKUs)"
                },
                status="verified"),
    EvalProduct(key="anker-prime-100w", brand="Anker",
                model="Prime Charger (100W)",
                variant="100W, 3-port (A2688)",
                category="chargers",
                identifiers={"UPC": "194644040635", "MPN": "A2688"},
                identifier_sources={
                    "UPC": "Ubuy + Desertcart (multiple regions) + "
                    "CamelCamelCamel agree for A2688 (ASIN B0CZ6LXL8R); "
                    "Anker US official spec confirms Model A2688, 100W, "
                    "2 USB-C + 1 USB-A. A2688341 (UPC 194644041021) is a "
                    "different variant and was excluded; B&H US listing "
                    "code A2688J41."
                },
                notes="Replaces anker-737-120w (retired 2026-10-31, "
                "user-confirmed, DECISIONS 012): the 737 has no "
                "qualifying US new-unit offer (BUILD_LOG 016). The old "
                "key is retired, never reused.",
                status="verified"),
    EvalProduct(key="apple-magic-mouse-usbc", brand="Apple",
                model="Magic Mouse (USB-C)", variant="White (MXK53AM/A)",
                category="mice",
                identifiers={"UPC": "195949655883", "MPN": "MXK53AM/A"},
                identifier_sources={
                    "UPC": "Apple official store page for MXK53AM/A "
                    "(NZ PBTech code 195949655975 is regional; Black is "
                    "195949656002)"
                },
                status="verified"),
    EvalProduct(key="logitech-g-pro-x-superlight-2-black", brand="Logitech",
                model="G Pro X Superlight 2", variant="Black (910-006628)",
                category="mice",
                identifiers={"UPC": "097855177797", "MPN": "910-006628"},
                identifier_sources={
                    "UPC": "Abt (US) lists Model 910-006628, UPC 097855177797, "
                    "Color Black; DirectDial agrees (MFG part 910-006628, "
                    "UPC 0097855177797, same code in GTIN-13 form). "
                    "Supersedes the 910-006630 / EAN 5099206104525 pinning, "
                    "which was the European reference (see DECISIONS 010); "
                    "Logitech G US store URL also shows 910-006628"
                },
                status="verified"),
    EvalProduct(key="google-pixel-buds-pro-2-porcelain", brand="Google",
                model="Pixel Buds Pro 2", variant="Porcelain, US (GA05760-US)",
                category="earbuds",
                identifiers={"UPC": "840244604448", "MPN": "GA05760-US"},
                identifier_sources={
                    "UPC": "B&H Photo + DirectDial agree for GA05760-US "
                    "(840244604516 group is a different regional version; "
                    "AU 840244605155 excluded)"
                },
                status="verified"),
    # --- Apple cluster (added 2026-10-31, refreshed 2026-10-31) ---
    # All pinned to base configs. Discontinued generations were replaced
    # with current models per DECISIONS 006 (in-sale new products only),
    # user-confirmed 2026-10-31. iPhone deliberately excluded: carrier
    # financing and lock status make "cheapest" non-comparable without
    # contract context.
    EvalProduct(key="apple-macbook-air-13-m5", brand="Apple",
                model="MacBook Air 13-inch (M5, 2026)",
                variant="M5, 16GB/512GB, Midnight (MDHE4LL/A)",
                category="laptops",
                identifiers={"UPC": "195950690200", "MPN": "MDHE4LL/A"},
                identifier_sources={
                    "UPC": "Best Buy US (SKU 6397846) + B&H Photo agree for "
                    "MDHE4LL/A. Other colors are different part numbers; "
                    "the UK B/A GTIN differs from the US LL/A UPC."
                },
                status="verified"),
    EvalProduct(key="apple-macbook-air-15-m5", brand="Apple",
                model="MacBook Air 15-inch (M5, 2026)",
                variant="M5, 16GB/512GB, Midnight (MDVH4LL/A)",
                category="laptops",
                identifiers={"UPC": "195950697087", "MPN": "MDVH4LL/A"},
                identifier_sources={
                    "UPC": "Best Buy US (SKU 6571043) + eBay listings agree for "
                    "MDVH4LL/A. Other colors are different part numbers."
                },
                status="verified"),
    EvalProduct(key="apple-macbook-pro-14-m6", brand="Apple",
                model="MacBook Pro 14-inch (M6, 2026)",
                variant="M6, 16GB/1TB, Space Black (MHWT4LL/A)",
                category="laptops",
                notes="Current generation announced 2026-10-27; in stock from launch day 2026-11-06 (Apple + Best Buy, $1,999). "
                "Part number MHWT4LL/A confirmed by "
                "iClarified order number + Best Buy pre-order page "
                "(SKU 6565882, $1,999). UPC not yet published: stays pending "
                "(identifiers empty, never matched) until a retailer "
                "listing states the UPC. User confirmed 2026-10-31 to track "
                "the M6 base over the in-stock M5 24GB/1TB (MDE34LL/A)."),
    EvalProduct(key="apple-mac-mini-m6", brand="Apple",
                model="Mac mini (M6, 2026)",
                variant="M6, 16GB/256GB, Silver (MHQK4LL/A)",
                category="desktops",
                identifiers={"UPC": "195951021089", "MPN": "MHQK4LL/A"},
                identifier_sources={
                    "UPC": "Adorama spec table for the 16GB/256GB 2.5Gb config "
                    "(single source); Best Buy US (SKU 6566933) confirms "
                    "the MPN. M4 mini is discontinued."
                },
                status="verified"),
    EvalProduct(key="apple-ipad-a16-11", brand="Apple",
                model="iPad 11-inch (A16, 2025)",
                variant="A16, 128GB Wi-Fi, Silver (MD3Y4LL/A)",
                category="tablets",
                identifiers={"UPC": "195950086232", "MPN": "MD3Y4LL/A"},
                identifier_sources={
                    "UPC": "Best Buy bundle listings + eBay agree for MD3Y4LL/A. "
                    "Wi-Fi + Cellular is a different SKU; one eBay listing "
                    "pairing this MPN with another UPC was excluded."
                },
                status="verified"),
    EvalProduct(key="apple-ipad-air-m4-11", brand="Apple",
                model="iPad Air 11-inch (M4, 2026)",
                variant="M4, 128GB Wi-Fi, Space Gray (MH304LL/A)",
                category="tablets",
                identifiers={"UPC": "195950823578", "MPN": "MH304LL/A"},
                identifier_sources={
                    "UPC": "eBay US + Amazon-derived listings agree for MH304LL/A; "
                    "Best Buy US (SKU 6586895) confirms the MPN. OnBuy code "
                    "195950823516 excluded as a suspected non-US variant. "
                    "Wi-Fi + Cellular is a different SKU."
                },
                status="verified"),
    EvalProduct(key="apple-ipad-pro-m5-11", brand="Apple",
                model="iPad Pro 11-inch (M5, 2025)",
                variant="M5, 256GB Wi-Fi, Space Black (MDWK4LL/A)",
                category="tablets",
                identifiers={"UPC": "195950395419", "MPN": "MDWK4LL/A"},
                identifier_sources={
                    "UPC": "Micro Center (SKU 941617) + multiple listings agree for "
                    "MDWK4LL/A. Single-seller eBay code 195950391077 "
                    "excluded as conflicting. Wi-Fi + Cellular is a "
                    "different SKU."
                },
                status="verified"),
    EvalProduct(key="apple-airpods-max-2", brand="Apple",
                model="AirPods Max 2 (USB-C, 2026)",
                variant="USB-C, Midnight (MHWK4AM/A)",
                category="headphones",
                identifiers={"UPC": "195951039060", "MPN": "MHWK4AM/A"},
                identifier_sources={
                    "UPC": "Abt + Best Buy US (SKU 6494847) agree for MHWK4AM/A. "
                    "The 2024 USB-C model MWW43AM/A is the previous "
                    "generation; Lightning version is a different model."
                },
                status="verified"),
    # --- Expansion batch 1 (added 2026-11-06, user-approved) ---
    # 28 -> 33 models. DECISIONS 022, BUILD_LOG 038.
    EvalProduct(
        key="nintendo-switch-2",
        brand="Nintendo",
        model="Switch 2",
        variant="Base system, 256GB (BEE-001)",
        category="consoles",
        identifiers={"UPC": "045496885816", "MPN": "BEE-001"},
        identifier_sources={
            "UPC": "Nintendo US store page (shown as GTIN 00045496885816; "
            "UPC-A form 045496885816) + Visions Electronics + eBay "
            "listings agree for BEE-001. The Best Buy bundle UPC "
            "196993181687 is a Pro Controller bundle, not the base "
            "system, and was excluded."
        },
        notes="Base system only: the Mario Kart World ($549.99) and "
        "Sports ($529.99) bundles are different SKUs and are excluded. "
        "Nintendo US direct $499.99, in stock 2026-11-06.",
        status="verified",
    ),
    EvalProduct(
        key="sony-wh1000xm6-black",
        brand="Sony",
        model="WH-1000XM6",
        variant="Black (WH1000XM6/B)",
        category="headphones",
        identifiers={"UPC": "027242930698", "MPN": "WH1000XM6/B"},
        identifier_sources={
            "UPC": "B&H Photo (kit page) + DataVision + Visions "
            "Electronics + Walts + Amazon.ca listings agree for "
            "WH1000XM6/B. A single conflicting code, 094148746326, "
            "appears only in the Sony manual hosted on manuals.plus "
            "and was not used. MPN confirmed by Best Buy US (Model "
            "WH1000XM6/B, SKU 6620467) + Sony Electronics."
        },
        notes="Bare unit only: Best Buy / Macy's / BuyDig / FocusCamera "
        "accessory bundles at $378-$458 are excluded. Sony direct "
        "lists $379.99 (was $459.99); stock on the Sony page was not "
        "confirmed in the page text (see BUILD_LOG 038).",
        status="verified",
    ),
    EvalProduct(
        key="apple-watch-series-12-42mm-gps-black",
        brand="Apple",
        model="Watch Series 12 (GPS, 42mm)",
        variant="GPS, 42mm, Black Aluminum, Black Sport Band S/M (MJEA4LS/A)",
        category="wearables",
        notes="Order number MJEA4LS/A confirmed by Abt (US) + iClarified "
        "+ Apple's own buy-page URL parameter (product=mjea4ls/a). "
        "US UPC not yet found: stays pending (identifiers empty, never "
        "matched) per the MacBook Pro 14 M6 precedent. PBTech NZ UPC "
        "195951225470 belongs to MJEA4X/A (NZ variant) and Very UK "
        "EAN 195951225395 is regional; neither was used. GPS + "
        "Cellular and 46mm are different SKUs. Apple direct $399, "
        "BJ's $389.99 (2026-11-06).",
    ),
    EvalProduct(
        key="logitech-mx-anywhere-3s-graphite",
        brand="Logitech",
        model="MX Anywhere 3S",
        variant="Graphite, standard edition (910-006928)",
        category="mice",
        identifiers={"UPC": "097855184030", "MPN": "910-006928"},
        identifier_sources={
            "UPC": "Logitech's own spec sheet (Part # 910-006928, Bar "
            "code 097855184030) + B&H Photo spec table (UPC "
            "097855184030) agree. MPN confirmed by B&H + Staples "
            "(Model # 910-006928, Color Graphite) + Woot (Graphite "
            "(910-006928)). PBTech NZ graphite 910-006932 / UPC "
            "097855184047 is a different regional SKU and was "
            "excluded, as was Logitech US direct pale grey 910-006926."
        },
        notes="Graphite is sold as 'Black' by B&H / Staples / Lenovo / "
        "Sweetwater; Logitech calls the color Graphite. The $69.99 "
        "candidate price in BUILD_LOG 024 was the pale grey sale "
        "price (Newegg), not graphite: graphite street price is "
        "$89.99 (B&H, Sweetwater, Lenovo, 2026-11-06).",
        status="verified",
    ),
    EvalProduct(
        key="samsung-buds4-black",
        brand="Samsung",
        model="Galaxy Buds4",
        variant="Black (SM-R540NZKAXAR)",
        category="earbuds",
        identifiers={"UPC": "198957277207", "MPN": "SM-R540NZKAXAR"},
        identifier_sources={
            "UPC": "Abt (US) + ChannelOnline agree for SM-R540NZKAXAR. "
            "MPN confirmed by the Samsung US buy-page URL "
            "(galaxy-buds4-black-sku-sm-r540nzkaxar) + Abt. The EU "
            "EAN 8806097998563 (SM-R540NZKAEUE) and the MEA "
            "SM-R540NZKAMEA are different regional variants and were "
            "excluded."
        },
        notes="Samsung US direct $179.99, in stock 2026-11-06; NFM and "
        "Best Buy also $179.99. White is a different SKU "
        "(SM-R540NZWAXAR); Buds4 Pro is a different model.",
        status="verified",
    ),
    # --- Expansion batch 2 (added 2026-11-06, user-approved) ---
    # 33 -> 38 models. DECISIONS 023, BUILD_LOG 039.
    EvalProduct(
        key="sony-wf1000xm6-black",
        brand="Sony",
        model="WF-1000XM6",
        variant="Black (WF1000XM6/B)",
        category="earbuds",
        identifiers={"UPC": "027242933460", "MPN": "WF1000XM6/B"},
        identifier_sources={
            "UPC": "Abt (US) product page (Model WF1000XM6/B, UPC "
            "027242933460) + B&H Photo spec page (UPC 027242933460, "
            "Black) + eBay product identifiers (GTIN 0027242933460) "
            "agree for WF1000XM6/B. Amazon bundle UPC 196641206649 "
            "and renewed UPC 728434235248 are different products "
            "and were not used."
        },
        notes="Bare unit only: Moon Audio / DataVision care-program "
        "bundles and the Target earbud-tips bundle at $298-$328.48 "
        "are excluded, as are the Platinum Silver rows. Sony direct "
        "lists $298.00 (was $329.99); the Sony page itself 403'd on "
        "direct fetch, so stock is not confirmed — price-only, "
        "flagged in the snapshot notes (see BUILD_LOG 039).",
        status="verified",
    ),
    EvalProduct(
        key="apple-watch-ultra-4-49mm-gps-cellular-natural",
        brand="Apple",
        model="Watch Ultra 4 (GPS + Cellular, 49mm)",
        variant="GPS + Cellular, 49mm, Natural Titanium, Sand Trail Loop M/L (MJAQ4LS/A)",
        category="wearables",
        notes="GPS + Cellular only — there is no GPS-only Ultra 4 "
        "tier (Apple buy page, EveryMac). Order number MJAQ4LS/A "
        "confirmed by Apple's own buy-page URL parameter "
        "(product=mjaq4ls/a) + Best Buy US (Model MJAQ4LS/A, SKU "
        "6597850). US UPC not yet verified: Adorama's spec table "
        "lists 195951394480 for Natural M/L Sand Trail Loop, but "
        "no second independent US source states it, so identifiers "
        "stay empty per the MacBook Pro 14 M6 precedent. Black "
        "Titanium, Desert Alpine Loop (MJAE4LS/A), Milanese Loop "
        "and Ocean Band are different SKUs. Apple direct $799.00, "
        "Best Buy $799.00 (2026-11-06).",
    ),
    EvalProduct(
        key="nintendo-switch-2-pro-controller",
        brand="Nintendo",
        model="Switch 2 Pro Controller",
        variant="Black, standard edition (BEE-008)",
        category="controllers",
        identifiers={"UPC": "045496885861", "MPN": "BEE-008"},
        identifier_sources={
            "UPC": "Nintendo US store page itself (SKU 123674, UPC "
            "00045496885861) + Dell (manufacturer part "
            "045496885861, $89.99) + eBay product identifiers (GTIN "
            "0045496885861) + PayMore + Ubuy agree. MPN BEE-008 "
            "confirmed by Nintendo Support (US). The single eBay "
            "code 0219341384384 is uncorroborated and was not used; "
            "4902370552843 is the Japan JAN, not the US UPC."
        },
        notes="Standard black controller only: the Zelda 40th "
        "Anniversary edition ($99.99) and Resident Evil Requiem "
        "edition ($119) are different SKUs. Nintendo US direct "
        "$89.99, in stock 2026-11-06.",
        status="verified",
    ),
    EvalProduct(
        key="logitech-mx-keys-mini-black",
        brand="Logitech",
        model="MX Keys Mini",
        variant="Black, standard edition (920-010475)",
        category="keyboards",
        identifiers={"UPC": "097855169617", "MPN": "920-010475"},
        identifier_sources={
            "UPC": "Logitech's own spec sheet (Part # 920-010475, "
            "Bar code 097855169617, hosted by P.C. Richard) + "
            "manuals.plus (UPC 097855169617) + Adorama (UPC "
            "097855169617) + DirectDial agree. Best Buy Q&A "
            "(answered by Logitech) confirms 920-010475 is Black "
            "and 920-010388 is Graphite — different SKUs."
        },
        notes="Black is sold as 'Graphite' in some Logitech "
        "materials; the Graphite part 920-010388 is a different "
        "SKU and was excluded, as were for-Mac (920-010389 / "
        "920-012644) and for-Business (920-010594). Pale Grey "
        "(920-010473) and Rose (920-010474) are different colors. "
        "Logitech direct $89.99 (was $99.99), in stock "
        "2026-11-06.",
        status="verified",
    ),
    EvalProduct(
        key="samsung-buds3-fe-black",
        brand="Samsung",
        model="Galaxy Buds3 FE",
        variant="Black (SM-R420NZKAXAR)",
        category="earbuds",
        identifiers={"UPC": "0198957213090", "MPN": "SM-R420NZKAXAR"},
        identifier_sources={
            "UPC": "ChannelOnline (multiple storefronts: Part # "
            "SM-R420NZKAXAR, UPC 0198957213090, Black) + eBay "
            "product identifiers (GTIN 0198957213090) + SHI (Mfr "
            "Part # SM-R420NZKAXAR, Black, MSRP $149.99) agree. "
            "Regional codes SM-R420NZKAASA (AU), SM-R420NZKAXSE, "
            "SM-R420ZNAXNU and SM-R420NZAFXAR are different "
            "variants and were excluded."
        },
        notes="Samsung US direct $149.99, in stock 2026-11-06. "
        "Gray is a different SKU (SM-R420NZAAXAR); the older "
        "Galaxy Buds FE is a different model. Macy's $149.99 row "
        "is shipped and sold by DataVision (marketplace) and is "
        "excluded per DECISIONS 021.",
        status="verified",
    ),
    # --- Expansion batch 3 (added 2026-11-06, user-approved) ---
    # 38 -> 42 models. DECISIONS 024, BUILD_LOG 040. AirPods 5 was
    # already in the set (apple-airpods-5-usbc, MKFW4LL/A, UPC
    # 195951378978) and was NOT re-added: 4 new models, not 5.
    EvalProduct(
        key="sony-ps5-pro",
        brand="Sony",
        model="PlayStation 5 Pro",
        variant="2TB, White, all-digital (1000046529 / CFI-7019B01X)",
        category="consoles",
        identifiers={"UPC": "711719595946", "MPN": "1000046529"},
        identifier_sources={
            "UPC": "Best Buy US (Model 1000046529, SKU 10145289, UPC "
            "711719595946) + Amazon US (ASIN B0DGY63Z2H, UPC "
            "711719595946, MPN 1000046529, Model CFI-7019B01X) + "
            "Desertcart + SeekMonkey (EAN 0711719595946) agree. "
            "711719581124 was an unverified guess and was not used."
        },
        notes="Bare 2TB console only: no disc drive included (sold "
        "separately). PlayStation's current PDP lists model CFI-7021 "
        "and Best Buy's current listing (SKU 6601524) shows Model "
        "1000046529/1000050805, so the UPC is verified for the "
        "launch revision (CFI-7019B01X / 1000046529); a separate UPC "
        "for the CFI-7021 revision was not found and is flagged, not "
        "assumed. US MSRP $899.99 since 2026-04-02 (PlayStation "
        "Direct displays $899 rounded); broadly out of stock in the "
        "US since mid-September 2026 (Best Buy sold out, GameStop "
        "new unavailable, 2026-11-06).",
        status="verified",
    ),
    EvalProduct(
        key="nintendo-switch-oled-neon",
        brand="Nintendo",
        model="Switch - OLED Model",
        variant="Neon Blue/Neon Red set (HEGSKABAA; SKU 115464)",
        category="consoles",
        identifiers={"UPC": "045496883409", "MPN": "HEGSKABAA"},
        identifier_sources={
            "UPC": "Nintendo US store page itself (SKU 115464, GTIN "
            "00045496883409; UPC-A form 045496883409) + Micro Center "
            "(SKU 642595, Mfr Part# 045496883409, UPC 045496883409) + "
            "J&L Game + eBay product identifiers agree for the Neon "
            "set. Console model HEG-001 (Nintendo hardware page)."
        },
        notes="Neon Blue/Neon Red Joy-Con set only: the White set is "
        "already in the catalog (nintendo-switch-oled-white, UPC "
        "045496883386) and is a different SKU; Splatoon 3, Mario Red "
        "and Zelda editions are different SKUs. Nintendo US direct "
        "$399.99, in stock 2026-11-06; Best Buy $399.00 (Model "
        "HEGSKABAA, SKU 11897850).",
        status="verified",
    ),
    EvalProduct(
        key="logitech-lift-graphite",
        brand="Logitech",
        model="Lift",
        variant="Graphite, standard right-handed (910-006466)",
        category="mice",
        identifiers={"UPC": "097855170927", "MPN": "910-006466"},
        identifier_sources={
            "UPC": "Logitech's own spec sheet (Part # 910-006466, "
            "Bar code 097855170927, EAN-13) + Desertcart (multiple "
            "regions, UPC 097855170927, GTIN 00097855170927, ASIN "
            "B09J1TB35S) + Ubuy agree. A manuals.plus snippet's "
            "'097855170972' is a truncated typo of the same code."
        },
        notes="Right-handed standard edition only: the left-handed "
        "Lift, for-Business and for-Mac are different SKUs; Rose and "
        "Off-White are different colors. Logitech direct $79.99, in "
        "stock 2026-11-06; Dell $69.99 (sale), B&H $74.99.",
        status="verified",
    ),
    EvalProduct(
        key="meta-quest-3-512gb",
        brand="Meta",
        model="Quest 3 (512GB)",
        variant="512GB (899-00583-01)",
        category="vr",
        identifiers={"UPC": "815820024071", "MPN": "899-00583-01"},
        identifier_sources={
            "UPC": "B&H Photo (BH # MEQ3512, MFR # 899-00583-01, UPC "
            "815820024071) + Amazon US (ASIN B0CD1JTBSC, UPC "
            "815820024071) + Amazon.ca + Desertcart/Ubuy agree. "
            "Amazon's 'Model Number 899-00585-01' is a different "
            "code (bundle/box) and was not used; the 128GB Quest 3 "
            "was phased out in 2024, so 512GB is the only current "
            "Quest 3 storage tier."
        },
        notes="Bare 512GB headset only: the Target GOLF+ bundle and "
        "the Elite Strap kit are different SKUs; Quest 3S (128GB / "
        "256GB) is a different model and is already in the set "
        "(meta-quest-3s-128gb). Meta direct $599.99, in stock "
        "2026-11-06; NFM, Abt and Newegg also $599.99.",
        status="verified",
    ),
    # --- Expansion batch 4 (2026-11-06, user-approved, DECISIONS 025) ---
    EvalProduct(
        key="apple-ipad-mini-a20-128gb-wifi-starlight",
        brand="Apple",
        model="iPad mini (A20 Pro)",
        variant="Wi-Fi 128GB, Standard Glass, Starlight (MJ6J4LL/A)",
        category="tablets",
        identifiers={"UPC": "195951205595", "MPN": "MJ6J4LL/A"},
        identifier_sources={
            "UPC": "B&H Photo spec page (MJ6J4LL/A, UPC 195951205595, "
            "128GB Wi-Fi Only Starlight) + Adorama spec table "
            "(Starlight 128GB Wi-Fi Standard Glass: 195951205595) "
            "agree. MPN MJ6J4LL/A confirmed by Best Buy US (SKU "
            "6638325), CDW (CDW# 9296012), EveryMac (Model A3595) "
            "and B&H."
        },
        notes="Wi-Fi 128GB standard-glass Starlight only: Midnight "
        "is MJ6F4LL/A, 256GB is MJ6R4LL/A, nano-texture glass is a "
        "different option (256GB/512GB only). Released 2026-11-06. "
        "The Meta Catalog feed's Apple brand_direct rows were the "
        "outgoing A17 Pro model (Space Gray/Purple/Blue, $599-$849) "
        "and were excluded; the $999/$1,249 NFM rows are the 512GB "
        "A20 Pro variant. Apple direct $699.00 (apple.com US buy "
        "page JSON-LD, price-only); Best Buy $699.00 (sold by Best "
        "Buy, InStock); B&H $699.00 (In Stock, New Release).",
        status="verified",
    ),
    EvalProduct(
        key="sony-ps5-digital-825gb",
        brand="Sony",
        model="PlayStation 5 Slim Digital Edition (825GB)",
        variant="825GB, White, all-digital (CFI-2015)",
        category="consoles",
        identifiers={"UPC": "711719541035", "MPN": "CFI-2015"},
        identifier_sources={
            "UPC": "PayMore US spec table (Slim Digital Edition "
            "825GB, MPN CFI-2015, UPC 711719541035) + eBay product "
            "catalog (GTIN 0711719541035, 825GB, CFI-2015) agree. "
            "Best Buy's page (Model 1000049898, SKU 6646420) states "
            "no UPC. The 1TB CFI-2015 revision carries a different "
            "UPC (711719548539) and was excluded; CFI-1015B is the "
            "launch (non-Slim) digital model."
        },
        notes="Slim Digital 825GB bare console only: bundles "
        "(Fortnite, Marvel's Wolverine) and the 1TB revision are "
        "different SKUs. Best Buy $599.99 (sold by Best Buy, Add to "
        "cart, JSON-LD InStock on the page read 2026-11-06; one "
        "earlier crawl showed Unavailable for shipping, so stock "
        "signals were mixed); Sam's Club $599.00 (feed, "
        "authorized_retailer). Candidate price $599 corrected to "
        "$599.99.",
        status="verified",
    ),
    EvalProduct(
        key="nintendo-joy-con-2-pair-light-blue-light-red",
        brand="Nintendo",
        model="Joy-Con 2 (L)/(R)",
        variant="Light Blue / Light Red pair (BEEAJAAAA)",
        category="controllers",
        identifiers={"UPC": "045496885892", "MPN": "BEEAJAAAA"},
        identifier_sources={
            "UPC": "Nintendo US official store page (SKU 123677, "
            "UPC 00045496885892) + Snapklik (Model BEEAJAAAA, Part "
            "number 123677, UPC 045496885892) agree. PBTech NZ UPC "
            "045496321413 is regional and was excluded."
        },
        notes="Light Blue/Light Red pair only: Light Purple/Light "
        "Green and Blue/Light Yellow are different SKUs; single "
        "Joy-Con 2 (L) or (R) are $54.99 singles. Nintendo direct "
        "$99.99 (JSON-LD InStock, page read 2026-11-06); Electronic "
        "Express $94.99.",
        status="verified",
    ),
    EvalProduct(
        key="logitech-g502-x-plus-black",
        brand="Logitech",
        model="G502 X PLUS",
        variant="Black, HERO 25K (910-006160)",
        category="mice",
        identifiers={"UPC": "097855166951", "MPN": "910-006160"},
        identifier_sources={
            "UPC": "ErgoDirect (Part 910-006160, UPC 097855166951) "
            "+ Desertcart (Mfr Part 910-006160, UPC 097855166951, "
            "ASIN B092CB69Q4) + Amazon US (Model 910-006160, UPC "
            "097855166951) + DirectDial (MFG 910-006160, UPC "
            "0097855166951) + eBay agree. White is 910-006169 / "
            "910-006172, a different SKU."
        },
        notes="Original HERO 25K Black only. Logitech refreshed the "
        "line in fall 2026 with a HERO 44K sensor and new colorways "
        "(Black/Purple, White/Mint, Dark Lilac); the 44K part "
        "numbers conflict across retailers (910-007808 on "
        "Logitech's US page and Best Buy's Dark Lilac listing vs "
        "910-007812 on PBTech NZ / Scorptec AU for Black/Purple) "
        "and no UPC was found for any 44K part number — the 44K "
        "UPC is an open item for a later refresh and the 25K UPC "
        "was NOT carried over to it. Logitech direct $159.99 list "
        "(current PDP defaults to the 44K Black/Purple at the same "
        "price, In stock); Best Buy $159.99 (HERO 25K Black); "
        "Adorama $159.99 (InStock); Staples $188.99 (Black "
        "910-006160). Candidate price $149.99 was stale; current "
        "street price is $159.99.",
        status="verified",
    ),
    EvalProduct(
        key="google-pixel-buds-2a-hazel",
        brand="Google",
        model="Pixel Buds 2a",
        variant="Hazel (GA06155-US)",
        category="earbuds",
        identifiers={"UPC": "840353930506", "MPN": "GA06155-US"},
        identifier_sources={
            "UPC": "eBay product catalog (MPN GA06155US, GTIN "
            "0840353930506, Hazel) + Poshmark US seller listing "
            "(Google Model # GA06155-US, UPC 840353930506) + "
            "Snapklik / ImportItAll / WantItAll (UPC 840353930506, "
            "Hazel) agree. OnBuy UK lists a conflicting 840353930520 "
            "for Hazel — single UK source, not used (likely a "
            "different regional variant; JP is 840353933019, EU is "
            "840353930537). MPN GA06155-US confirmed by Best Buy US "
            "(SKU 6642707) + B&H (BH # GOPBUD2AHAZ, MFR # GA06155-US)."
        },
        notes="Hazel only: Iris, Fog and Berry are different colors "
        "(Google support compare page). Best Buy $129.00 (sold by "
        "Best Buy, InStock); B&H $129.00 (In Stock); Google Store "
        "$129 (Google support compare page lists Pixel Buds 2a From "
        "$129, price-only); T-Mobile $129.99. The Best Buy $119.99 "
        "row (SKU 12951378) is sold by TheRightOne, a marketplace "
        "seller — excluded per DECISIONS 021.",
        status="verified",
    ),
    # --- Expansion batch 5 (2026-11-06, user-approved, DECISIONS 026) ---
    # 47 -> 52 models.
    EvalProduct(
        key="apple-ipad-air-m4-13",
        brand="Apple",
        model="iPad Air 13-inch (M4, 2026)",
        variant="M4, 128GB Wi-Fi, Space Gray (MH5N4LL/A)",
        category="tablets",
        identifiers={"UPC": "195950797817", "MPN": "MH5N4LL/A"},
        identifier_sources={
            "UPC": "Abt US (Model MH5N4LL/A, UPC 195950797817) + "
            "iGiftcardz (MPN MH5N4LL/A, UPC 195950797817, EAN "
            "0195950797817) agree. Regional part numbers MH5N4TY/A "
            "(CY), MH5N4QA/A (ZA), MH5N4X/A (AU), MH5N4KN/A (IE) are "
            "different SKUs; US is MH5N4LL/A. Best Buy US (SKU "
            "6586913) confirms the MPN. Wi-Fi + Cellular (MH9D4LL/A) "
            "is a different SKU."
        },
        notes="Apple direct $949.00 (apple.com US buy page JSON-LD, "
        "price-only); Best Buy $949.00 (sold by Best Buy, InStock, "
        "SKU 6586913).",
        status="verified",
    ),
    EvalProduct(
        key="sony-dualsense-edge-black-white",
        brand="Sony",
        model="DualSense Edge Wireless Controller",
        variant="Black & White (CFI-ZCP1)",
        category="controllers",
        notes="MPN CFI-ZCP1 confirmed (PlayStation official page, "
        "PBTech, Desertcart, eBay) but the UPC is unresolved: "
        "711719444190 (Desertcart GTIN 00711719444190 + Albagame "
        "barcode + itworkup EAN + startech24 datasheet) vs "
        "711719585552 (eBay product catalog, ePID 10058650690, "
        "Glacier White) vs 711719586555 (PBTech NZ, regional) — no "
        "two independent US sources agree, so identifiers stay "
        "empty per the DualSense White precedent. Midnight Black "
        "(MPN 1000046706, UPC 711719596554) is a different colorway "
        "whose support is Amazon-derived only, not pinned. Kohl's "
        "$199.99 (Black & White); P.C. Richard $199.99 (Black & "
        "White, Model 1000035016); R.C. Willey $199.99 (Black and "
        "White); Abt $199.99 (Model 1000035016). PlayStation Direct "
        "US page not reached; the feed's direct.playstation.com "
        "$30 row is not a real price and was excluded.",
        status="pending",
    ),
    EvalProduct(
        key="nintendo-joy-con-pair-neon-red-neon-blue",
        brand="Nintendo",
        model="Joy-Con (L)/(R)",
        variant="Neon Red/Neon Blue (HACAJAEAA)",
        category="controllers",
        identifiers={"UPC": "045496590130", "MPN": "HACAJAEAA"},
        identifier_sources={
            "UPC": "Nintendo US official store page (SKU 104882, UPC "
            "00045496590130) + eBay product catalog (MPN HACAJAEAA, "
            "UPC 0045496590130) + PayMore US spec table (MPN HAC-015, "
            "UPC 045496590130) agree. HAC-015 / HAC-016 are the "
            "individual left/right controller model numbers; the "
            "retail pair MPN is HACAJAEAA. One PayMore storefront "
            "lists an outlier UPC 190403045002, not used."
        },
        notes="Nintendo direct $89.99 (nintendo.com US store, "
        "JSON-LD InStock, SKU 104882); NFM $89.99. Best Buy $115.61 "
        "excluded (above MSRP); Newegg $89.99 excluded (seller not "
        "confirmed as merchant itself); Ayoub $79 excluded "
        "(overseas seller, DECISIONS 021).",
        status="verified",
    ),
    EvalProduct(
        key="logitech-mx-vertical-graphite",
        brand="Logitech",
        model="MX Vertical Ergonomic Wireless Mouse",
        variant="Graphite (910-005447)",
        category="mice",
        identifiers={"UPC": "097855144461", "MPN": "910-005447"},
        identifier_sources={
            "UPC": "Govets (Part # 910-005447, UPC 097855144461) + "
            "Compsource (MPN 910-005447, UPC 097855144461) + "
            "Desertcart (GTIN 00097855144461, Mfr Part 910-005447) + "
            "CamelCamelCamel (UPC 097855144461, Model 910-005447, "
            "list $119.99) agree. The 910-005449 row in the feed is "
            "a different regional SKU."
        },
        notes="Logitech direct $99.99 (sale, was $119.99, In stock, "
        "JSON-LD); Staples $99.99 (sale, was $119.99, Graphite "
        "910-005447); Dell $99.99 (sale, was $119.99). Candidate "
        "price $99.99 is the current sale price, not the list "
        "($119.99). The feed's B&H $74.99 sale figure was not "
        "page-verified and was not carried; a second conflicting "
        "Dell feed row ($99.99 / sale $89.99) was excluded.",
        status="verified",
    ),
    EvalProduct(
        key="bose-qc-earbuds-black",
        brand="Bose",
        model="QuietComfort Earbuds (2024)",
        variant="Black (888507-0100)",
        category="earbuds",
        identifiers={"UPC": "017817853460", "MPN": "888507-0100"},
        identifier_sources={
            "UPC": "Abt US (Model 888507-0100, UPC 017817853460) + "
            "Adorama spec table (Black Earbuds: 017817853460) + "
            "Ubuy (GTIN 00017817853460, Mfr Part 888507-0100) + "
            "Desertcart (GTIN 00017817853460, ASIN B0D8BZDPXB) + "
            "eBay (MPN 888507-0100, UPC 017817853460) agree. The "
            "2020 QC Earbuds (831262-0010, UPC 017817804516) is a "
            "different model. White Smoke is 888507-0200, a "
            "different SKU."
        },
        notes="Bose direct $119.00 (sale, was $179.00, ends "
        "2026-11-08); P.C. Richard $129.00 (sale, was $179.00); "
        "Macy's $179.00; CDW $179.00 (Black). Candidate price $129 "
        "was wrong as a list price: list is $179.00, $129 is "
        "P.C. Richard's sale price and $119 is Bose direct's "
        "current sale price.",
        status="verified",
    ),
]


def get_product(key: str) -> EvalProduct:
    for product in EVAL_SET:
        if product.key == key:
            return product
    raise KeyError(f"unknown eval model key: {key}")
