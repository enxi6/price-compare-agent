"""Phase 1 evaluation set: 87 standardized electronics models, US market.

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
    # --- Expansion batch 6 (2026-11-06, continuous expansion per DECISIONS 027) ---
    # 52 -> 57 models. DECISIONS 028, BUILD_LOG 044.
    EvalProduct(
        key="apple-ipad-pro-m5-13",
        brand="Apple",
        model="iPad Pro 13-inch (M5, 2025)",
        variant="M5, 256GB Wi-Fi, Space Black (MDYJ4LL/A)",
        category="tablets",
        identifiers={"UPC": "195950398090", "MPN": "MDYJ4LL/A"},
        identifier_sources={
            "UPC": "Adorama US spec table (Space Black 256GB Wi-Fi "
            "Standard Glass: 195950398090) + eBay US (MPN MDYJ4LL/A, "
            "UPC 195950398090) agree. The Amazon renewed listing's "
            "728434107965 is a conflicting renewed-only code and was "
            "excluded."
        },
        notes="Apple direct $1,499.00 (apple.com US buy page JSON-LD, "
        "page-verified 2026-11-06); Staples $1,499.00; Abt $1,424.00 "
        "(Comp. Value $1,499). Candidate price $1,499 confirmed as "
        "the 256GB list price — PhoneArena's $1,299 MSRP figure is "
        "wrong/stale. Distinct from the 11-inch (MDWK4LL/A, UPC "
        "195950395419). Wi-Fi + Cellular (ME7W4LL/A, $1,699) and "
        "nano-texture glass tiers are different SKUs.",
        status="verified",
    ),
    EvalProduct(
        key="sony-playstation-portal",
        brand="Sony",
        model="PlayStation Portal Remote Player",
        variant="White (1000041319)",
        category="consoles",
        identifiers={"UPC": "711719579779", "MPN": "1000041319"},
        identifier_sources={
            "UPC": "eBay US (White, MPN 1000041319, UPC 0711719579779) "
            "+ Snapklik (Model 1000041319, UPC 711719579779) + Canex "
            "CA (SKU 711719579779) agree. The 711719580782 barcode "
            "(LDLC, Gamesmen AU) is a regional code and was excluded."
        },
        notes="PlayStation Direct $249.00 (price shown; crawl mixed "
        "'Currently Unavailable / Low stock' flags across variants, "
        "stock not confirmed there); NFM $249.99 (JSON-LD InStock); "
        "R.C. Willey $249.99 (Model 1000041319). Instruction-manual "
        "model CFI-Y1001; retail MPN is 1000041319. Midnight Black "
        "(1000044180) is a different colorway, not pinned. The "
        "$240 Ayoub row (CFI-Y1018) is an overseas seller, excluded.",
        status="verified",
    ),
    EvalProduct(
        key="nintendo-switch-neon",
        brand="Nintendo",
        model="Switch (original, HAC-001(-01))",
        variant="Neon Blue/Neon Red set (HADSKABAA; SKU 117972)",
        category="consoles",
        identifiers={"UPC": "045496883775", "MPN": "HADSKABAA"},
        identifier_sources={
            "UPC": "Nintendo US official store page itself (SKU 117972, "
            "UPC 00045496883775, $339.99 InStock) + Amazon B0BFJWCYTL "
            "(Model HADSKABAH, UPC 045496883775) agree. The older "
            "HADSKABAA UPC 045496882174 (ASIN B07VGRJDFY, 2019 "
            "red-box listing) conflicts with Nintendo's current page "
            "and was not pinned."
        },
        notes="Nintendo direct $339.99 (JSON-LD InStock); NFM $339.99; "
        "Best Buy $334.00 (Model HADSKABAH, SKU 10951790, "
        "search-index read, below MSRP). HACSKABAA is the 2017 "
        "original revision, a different SKU. Best Buy/Amazon spell "
        "the current model HADSKABAH; HADSKABAA is the retail part "
        "number used by BuyDig/Amazon B07VGRJDFY. Distinct from "
        "Switch OLED Neon (HEGSKABAA, UPC 045496883409) and from the "
        "Joy-Con pair alone (HACAJAEAA, UPC 045496590130).",
        status="verified",
    ),
    EvalProduct(
        key="logitech-g-pro-x-superlight-2-dex-black",
        brand="Logitech",
        model="G Pro X Superlight 2 DEX",
        variant="Black (910-007328)",
        category="mice",
        notes="MPN 910-007328 confirmed (Logitech G US store URL + "
        "Best Buy SKU 12726725 + Quill), but the UPC was not found "
        "in any US retailer spec page after repeated searches, so "
        "identifiers stay empty per the DualSense Edge precedent. "
        "B&H lists White 910-007363 (UPC 097855200471) and Magenta "
        "910-007371 (UPC 097855200457); the B&H Black page "
        "(LOPROXS2DBLK) exists but its UPC is not surfaced in the "
        "search index. Regional part numbers 910-007358/910-007359 "
        "excluded; DEX SE (910-007831, $129.99) is a different "
        "model. Logitech G direct $159.99 (In stock. Ready to ship, "
        "JSON-LD InStock); Best Buy $159.99; CDW $159.99. Distinct "
        "ergonomic asymmetric variant of the standard Superlight 2 "
        "Black (910-006628, UPC 097855177797).",
    ),
    EvalProduct(
        key="bose-ultra-open-earbuds-2nd-gen-black",
        brand="Bose",
        model="Ultra Open Earbuds (2nd Gen)",
        variant="Black (897806-0010)",
        category="earbuds",
        identifiers={"UPC": "017817862714", "MPN": "897806-0010"},
        identifier_sources={
            "UPC": "B&H Photo US spec page (Black, 897806-0010, UPC "
            "017817862714) + Snapklik (Model 897806-0010, UPC "
            "017817862714) + Harvey Norman AU (897806-0010, "
            "017817862714) agree."
        },
        notes="Bose direct $299.00 (price-only on page text; $299 "
        "confirmed by Bose press release 2026-09-17, available "
        "2026-10-01); Abt $299.00 (JSON-LD InStock); B&H $299.00 "
        "(In Stock). Announced 2026-09-17, launched 2026-10-01. "
        "Distinct from QC Earbuds (888507-0100) and QC Ultra "
        "Headphones 2nd Gen (890101-0100); 1st-gen Ultra Open "
        "Earbuds are a different model. White Smoke is 897806-0020, "
        "a different SKU.",
        status="verified",
    ),
    # --- Expansion batch 7 (2026-11-06, DECISIONS 029) ---
    EvalProduct(
        key="apple-macbook-neo-13-256gb-blush",
        brand="Apple",
        model="MacBook Neo 13-inch (A18 Pro, 2026)",
        variant="A18 Pro, 8GB/256GB, Blush (MHFH4LL/A)",
        category="laptops",
        notes="MPN MHFH4LL/A confirmed (Apple US buy page title 'Buy "
        "MacBook Neo, Blush, 256GB' + Best Buy US Model MHFH4LL/A, "
        "SKU 6615878), but the UPC was not found in any US source "
        "for this exact variant, so identifiers stay empty per the "
        "DualSense Edge / DEX precedent. The only Neo UPC found, "
        "195950852745, is Indigo MHFF4LL/A's (B&H standalone page + "
        "Canex CA + eBay agree) and must NOT be copied to Blush — "
        "different color, different UPC. Courts Barbados lists "
        "195950852745 against MHFH4LL/A but its fields are garbled "
        "(GTIN 472384200015) and it mislabels the color, so it was "
        "not used. EveryMac's $599 256GB figure is stale/wrong "
        "against live $699 (Apple feed + Best Buy + AppleInsider "
        "MSRP $699). Apple direct $699.00 (Meta Catalog brand_direct "
        "row); Best Buy $699.00 (page-verified JSON-LD InStock). "
        "NFM $854 is a Silver 256GB + 3-year AppleCare+ bundle, "
        "excluded. 512GB tiers (MHFC4LL/A, MHFJ4LL/A, MHFE4LL/A, "
        "MHFG4LL/A, $799) and Silver/Citrus/Indigo 256GB are "
        "different SKUs. Distinct from MacBook Pro 14 M6 "
        "(MHWT4LL/A) and MacBook Air 13/15 M5.",
    ),
    EvalProduct(
        key="sony-ps5-1tb",
        brand="Sony",
        model="PlayStation 5 Slim Console (1TB, disc)",
        variant="1TB, White, disc (CFI-2100 model group; retail MPN 1000049888)",
        category="consoles",
        identifiers={"UPC": "711719021452", "MPN": "1000049888"},
        identifier_sources={
            "UPC": "Amazon B0FRGTYSL5 (Model Number CFI-2100, MPN "
            "1000049888, UPC 711719021452) + two eBay US listings "
            "agree on UPC 711719021452. The eBay listings typo the "
            "MPN as 1000049988; the MPN itself rests on Amazon + "
            "Best Buy Model 1000049888."
        },
        notes="PlayStation Direct $649.00 (price-only; the Direct "
        "crawl mixes 'Currently Unavailable / Coming Soon / Low "
        "stock' flags across variants); Best Buy $649.99 "
        "(page-verified, sold by Best Buy, SKU 6646419); Sam's Club "
        "$649.00 (Meta Catalog standalone row). Correction vs the "
        "2026-10-31 candidate note: the US disc model is NOT "
        "CFI-2016 — that is the EU disc code (15 = US, 16 = EU; "
        "eBay US lists the CFI-2000-group disc as CFI-2015, UPC "
        "711719573364, and PCShop.ge lists the CFI-2100-group disc "
        "as CFI-2116). The current US disc console is the CFI-2100 "
        "model group (CFI-2115 per JNLGame), retail MPN 1000049888; "
        "the older CFI-2015 disc (UPC 711719573364) is superseded. "
        "Excluded: Staples $722.99 (old CFI-2000 model 1000039671), "
        "marketplace rows $789–$1,246.99, game bundles (Ghost of "
        "Yotei $1,040.99, NBA 2K25 $799.99, BJ's bundle $699.99), "
        "rental rows ($26.99/$29.99/$100). Distinct from the set's "
        "PS5 Digital 825GB (1000049898, UPC 711719021483) and PS5 "
        "Pro (CFI-7021).",
        status="verified",
    ),
    EvalProduct(
        key="nintendo-switch-pro-controller",
        brand="Nintendo",
        model="Switch Pro Controller",
        variant="Black, standard edition (HAC-013; retail MPN HACAFSSKA)",
        category="controllers",
        identifiers={"UPC": "045496590161", "MPN": "HACAFSSKA"},
        identifier_sources={
            "UPC": "Amazon B01NAWKYZ0 (GTIN 00045496590161, MPN "
            "HACAFSSKA) + Abt page title 'Nintendo Switch Pro "
            "Controller - 045496590161' + Newegg URL slug "
            "nintendo-045496590161-controller + Poggers item UPC "
            "agree. MPN HACAFSSKA from Amazon (model number + MPN); "
            "HAC-013 is the hardware model per Nintendo Support US "
            "and Wikipedia."
        },
        notes="Dell $79.99; NFM $79.99; Target $79.98 (product-page "
        "JSON-LD InStock, A-52180631; Target search listings show "
        "$79.99). Nintendo direct store page not re-reached in this "
        "batch (the 2026-10-31 sweep had it at $79.99 on "
        "nintendo.com); Abt lists it as no longer available, so no "
        "Abt quote. Excluded: Zelda/Mario/Smash special editions "
        "($54.99–$140.99), third-party controllers, Switch 2 Pro "
        "Controller rows ($89.99/$94.99). Distinct from the set's "
        "Switch 2 Pro Controller (BEE-008, UPC 045496885861). "
        "Wikipedia notes EU discontinuation February 2027; the US "
        "listing is current as of 2026-11-06.",
        status="verified",
    ),
    EvalProduct(
        key="logitech-mx-mechanical-tactile-quiet-graphite",
        brand="Logitech",
        model="MX Mechanical",
        variant="Full-size, Tactile Quiet switches, Graphite (920-010547)",
        category="keyboards",
        identifiers={"UPC": "097855174659", "MPN": "920-010547"},
        identifier_sources={
            "UPC": "Amazon B09LK1P1RD (GTIN 00097855174659, MPN "
            "920-010547, Tactile Quiet, Graphite) + eBay (UPC "
            "0097855174659, MPN 920-010547) agree. The Linear "
            "variant 920-010548 carries a different UPC "
            "(097855174666, TargetPC URL slug) and was excluded."
        },
        notes="Logitech direct $179.99 (page-verified JSON-LD "
        "InStock, 'In stock. Ready to ship'); Dell $169.99; Best "
        "Buy $179.99 (page-verified JSON-LD InStock, sold by Best "
        "Buy, SKU 6502579). Target $179.99 (JSON-LD InStock) also "
        "confirmed. Correction vs the 2026-10-31 candidate price: "
        "$149.99 was the Oct 31 LogiWork Deal Days sale price; the "
        "current full-size list is $179.99 and Dell is $169.99 — "
        "the $149.99 rows today are the MX Mechanical MINI "
        "(Clicky/Tactile/Linear, Dell), a different model, "
        "excluded. MPN mapping corrected: 920-010547 is Tactile "
        "Quiet (Amazon + eBay + Best Buy + Staples + Target "
        "agree); 920-010548 is Linear (Best Buy + BuyDig agree). "
        "Distinct from the set's MX Keys Mini Black (920-010475) "
        "and MX Keys S Pale Grey (920-011559).",
        status="verified",
    ),
    EvalProduct(
        key="xbox-elite-series-2-black",
        brand="Microsoft",
        model="Xbox Elite Wireless Controller Series 2",
        variant="Black (FST-00001)",
        category="controllers",
        identifiers={"UPC": "889842196344", "MPN": "FST-00001"},
        identifier_sources={
            "UPC": "Amazon B07SFKTLZM (first of three listed UPCs, "
            "item model number FST-00001) + eBay (UPC 889842196344, "
            "MPN FST-00001, Black) agree. Amazon's other two codes "
            "(889842613926, 750466003847) are unattributed variants "
            "and were excluded; the Core model (4IK-00001/4IK-00002) "
            "is a different line."
        },
        notes="Microsoft direct $167.99 (page-verified JSON-LD; "
        "stock not confirmed in the page text); Target $167.99; "
        "Best Buy $159.99 sale (list $179.99). CDW $183.99 not "
        "used. Amazon lists the ASIN as 'Is Discontinued By "
        "Manufacturer' but Microsoft Store, Target and Best Buy "
        "all list it new at $159.99–$179.99 on 2026-11-06, so it "
        "stays in the set as a current US line. Distinct from the "
        "set's Xbox Wireless Controller Carbon Black (1914, UPC "
        "196388518159) and from the Elite Series 2 Core "
        "($134.99–$149.99, different line).",
        status="verified",
    ),
    # --- Expansion batch 8 (2026-11-06, DECISIONS 030) ---
    EvalProduct(
        key="apple-imac-m6-24-10core-blue",
        brand="Apple",
        model="iMac 24-inch (M6, 2026)",
        variant="M6 10-core CPU/GPU, 16GB/256GB, Blue (MH094LL/A)",
        category="desktops",
        identifiers={"UPC": "195950838091", "MPN": "MH094LL/A"},
        identifier_sources={
            "UPC": "B&H Photo US spec page for the exact MPN "
            "(apple_mh094ll_a, 10-core/16GB/256GB/Blue, UPC "
            "195950838091). Single source so far — launch day; no "
            "second US source publishes this UPC yet (EveryMac "
            "still lists M6 iMac identifiers as Pending), so "
            "re-confirm on the next refresh. MPN MH094LL/A "
            "corroborated by Apple US buy page + Best Buy US Model "
            "MH094LL/A (SKU 6566940) + EveryMac + MacSolutions "
            "Plus. The neighbouring UPC 195950844627 is the Blue "
            "12-core 512GB (MH1J4LL/A) and was excluded."
        },
        notes="Apple direct $1,499.00 (US buy page MH094LL/A, "
        "JSON-LD price; stock not stated in the page-text crawl); "
        "Best Buy $1,499.00 (page-verified JSON-LD InStock, sold "
        "by Best Buy, SKU 6566940); B&H $1,499.00 (New Release, "
        "In Stock, JSON-LD InStock). Correction vs the 2026-10-31 "
        "candidate note: the new iMac is M6, not M5 — it skips M5 "
        "entirely (announced 2026-10-27, availability 2026-11-06, "
        "today). The Meta Catalog feed returned no M6 rows at all "
        "(all M4/M3/M1), so all three quotes are page-verified. "
        "12-core tiers ($1,699 MH114LL/A, $1,899 512GB, nano-"
        "texture $1,899 MH2U4LL/A) and the other six colors are "
        "different SKUs. Distinct from the set's Mac mini M6 "
        "(MHQK4LL/A) and the MacBook lines.",
        status="verified",
    ),
    EvalProduct(
        key="sony-wh1000xm4c-black",
        brand="Sony",
        model="WH-1000XM4C (M4 2nd Gen)",
        variant="Black (WH1000XM4C/B)",
        category="headphones",
        notes="MPN WH1000XM4C/B confirmed (Best Buy US Model + "
        "Sony US store + Adorama + Canada Computers + Abt "
        "WH1000XM4CB agree), but no UPC was found for the Black "
        "variant in any US source, so identifiers stay empty per "
        "the DualSense Edge / DEX / Neo precedent. The only XM4C "
        "barcode found, 4548736181861, is the Platinum Silver "
        "EAN (Harvey Norman AU, WH1000XM4CS) and must NOT be "
        "copied to Black — different color, different barcode. "
        "The original XM4 Black UPC 027242919419 (Abt) belongs "
        "to WH1000XM4/B, not the XM4C, and was excluded. Best "
        "Buy $299.99 (WH1000XM4C/B, SKU 6689199, sold by Best "
        "Buy); Target $299.99 (JSON-LD InStock, A-1012764580); "
        "Sweetwater $298.00 (feed row, WH1000XM4CB). Sony direct "
        "lists the model at $299.99 (store JSON-LD, same price "
        "all colors; Sony Sept 7 2026 announcement); Abt $298.00 "
        "and Nordstrom/Crutchfield $298.00 also confirmed. The "
        "XM4C is a 2026 hardware refresh of the 2020 XM4 "
        "(retuned sound, 10-band EQ, Bluetooth 6.0, replaceable "
        "battery; announced Sept 7 2026), not a new flagship — "
        "distinct from the set's WH-1000XM5 Black "
        "(027242923232) and WH-1000XM6 Black (027242930698). "
        "Lavender (WH1000XM4C/V) is a Sony-exclusive colorway.",
    ),
    EvalProduct(
        key="sony-pulse-elite-midnight-black",
        brand="Sony",
        model="PULSE Elite Wireless Headset",
        variant="Midnight Black (retail MPN 1000044173)",
        category="headphones",
        notes="MPN 1000044173 confirmed (Best Buy US Model + P.C. "
        "Richard MODEL + ShopCGX + Big Apple Buddy agree), but "
        "the UPC was not verified from a non-Amazon US source, "
        "so identifiers stay empty per the DualSense Edge / DEX "
        "/ Neo precedent. The only UPC seen for this variant, "
        "711719588009, appears on a single Amazon listing (with "
        "hardware model CFI-ZWH2) and no second source "
        "corroborates it, so it was not recorded. The EU retail "
        "code 1000044483 (barcode 711719590392, Salling Group "
        "datasheet) is a different retail code and was not "
        "copied. CFI-ZWH1 is the PULSE 3D headset, a different "
        "model — not the Elite. PlayStation Direct $149.00 "
        "(price-only; the Direct crawl mixes Currently "
        "Unavailable / Low stock / Coming Soon flags across "
        "variants); Best Buy $149.99 (page-verified JSON-LD "
        "InStock, sold by Best Buy, SKU 6614841); P.C. Richard "
        "$149.99 (JSON-LD InStock, ships by Mon, Nov 9). Newegg "
        "$149.99 and Walmart $149.00 also confirmed (feed rows). "
        "Midnight Black released 2025-02-20; the original White "
        "Elite (Feb 2024) is a different colorway. Distinct from "
        "the set's PlayStation Portal (1000041319) and DualSense "
        "lines.",
    ),
    EvalProduct(
        key="logitech-ergo-k860-graphite",
        brand="Logitech",
        model="ERGO K860",
        variant="Graphite, standard edition (920-009166)",
        category="keyboards",
        identifiers={"UPC": "097855151667", "MPN": "920-009166"},
        identifier_sources={
            "UPC": "Adorama US spec page (MFR 920-009166, UPC "
            "Code 097855151667) + B&H kit pages (K860 section "
            "UPC 097855151667, distinct from the Lift mouse's "
            "097855170927) + eBay US item specifics (UPC "
            "097855151667, MPN 920-009166) agree."
        },
        notes="Best Buy $149.99 (page-verified JSON-LD InStock, "
        "sold by Best Buy, SKU 6395346, Model 920-009166); Dell "
        "$149.99 (page text, Manufacturer part 920-009166); "
        "Newegg $149.99 (feed row, 920-009166). Correction vs "
        "the 2026-10-31 candidate price: $119.99 was an "
        "Amazon-only sale price (TechTimes 2026-10-19, 20% off "
        "the $149.99 MSRP) and no Amazon price is used; the "
        "current first-party list is $149.99. The feed's Dell "
        "$129.99 row is stale (page text now $149.99) and the "
        "feed's B&H $159.99 row is the K860 for Business "
        "(920-010175, Logi Bolt), not this variant. The Business "
        "variant (920-010175, Logi Bolt receiver) and regional "
        "MPNs 920-009167/920-010107/920-010348 are different "
        "SKUs; the standard 920-009166 ships with the Unifying "
        "receiver. Distinct from the set's MX Keys S Pale Grey "
        "(920-011559) and MX Keys Mini Black (920-010475).",
        status="verified",
    ),
    EvalProduct(
        key="keychron-k8-he-special-black",
        brand="Keychron",
        model="K8 HE",
        variant="Special Edition, Black, Gateron Double-Rail Magnetic Nebula Switch (K8H-F1)",
        category="keyboards",
        identifiers={"EAN": "4894979028990", "SKU": "K8H-F1"},
        identifier_sources={
            "EAN": "Keychron official store public product JSON, "
            "browser-verified 2026-11-06 (Special Edition / "
            "Black / Gateron Double-Rail Magnetic Nebula Switch, "
            "SKU K8H-F1, price $139.99, available: true, barcode "
            "4894979028990). JSON field is named 'barcode' (no "
            "separate GTIN/UPC/EAN field); recorded as EAN "
            "following the K8 Ultra 8K precedent (13-digit "
            "barcodes). Special Edition White K8H-Q1 is "
            "4894979029003; Standard Black K8H-J1 is "
            "4894979028952."
        },
        notes="Keychron direct $139.99 (official store JSON, "
        "available: true; the K8 HE is sold only through "
        "Keychron's own store per Notebookcheck). Correction vs "
        "the 2026-10-31 candidate note: $139.99 is the Special "
        "Edition (OSA double-shot PBT, wood trim); the Standard "
        "Version is $129.99 (K8H-J1) and is currently "
        "unavailable at Keychron. The feed's keychron.com "
        "$139.99 row is the Japan JIS Layout product, a "
        "different layout, and was not used; the quote is the US "
        "ANSI product. Newegg rows $221.48-$273.99 are "
        "third-party inflated prices, excluded. The All-Wood "
        "Special Edition ($199.99) and Lime-switch variants "
        "(unavailable, no barcode) are different variants. "
        "Distinct from the set's K8 Ultra 8K (K8U-J1, EAN "
        "4894979057969) — the K8 Pro page points to the K8 HE "
        "and K8 Ultra 8K as successors.",
        status="verified",
    ),
    # --- Expansion batch 9 (2026-11-06, DECISIONS 031) ---
    EvalProduct(
        key="apple-mac-studio-m5-max-36gb-512gb-silver",
        brand="Apple",
        model="Mac Studio (M5 Max, 2026)",
        variant="M5 Max 18-core CPU/32-core GPU, 36GB/512GB, Silver (MHL64LL/A)",
        category="desktops",
        identifiers={"UPC": "195951078564", "MPN": "MHL64LL/A"},
        identifier_sources={
            "UPC": "B&H Photo US spec page for the exact MPN "
            "(apple_mhl64ll_a, 18-core/32-core/36GB/512GB, UPC "
            "195951078564) + Adorama US spec page UPC Codes list "
            "(M5 Max 18-core/32-core 36GB 512GB: 195951078564) "
            "agree. MPN MHL64LL/A corroborated by Apple US buy "
            "page + Best Buy US Model MHL64LL/A (SKU 6566932) + "
            "EveryMac (Mac17,14, A3545). The neighbouring UPC "
            "195951078724 is the MHL64X/A (AU/NZ) variant and "
            "195951078380 is the UK MHL64B/A variant; both were "
            "excluded."
        },
        notes="Apple direct $2,499.00 (US buy page MHL64LL/A, "
        "JSON-LD price; stock not stated in the page-text "
        "crawl); B&H $2,499.00 (page-verified In Stock, JSON-LD "
        "InStock); Best Buy $2,499.00 (Model MHL64LL/A, SKU "
        "6566932, sold by Best Buy). Adorama $2,399.00 also "
        "seen. Correction vs the 2026-10-31 candidate note: "
        "the current Mac Studio is the M5 Max generation "
        "(announced 2026-08-25, available 2026-09-22), not the "
        "2025 M4 Max — the M4 Max MU963LL/A launched at "
        "$1,999 and is discontinued per EveryMac, and the "
        "feed's Apple row pairing MU963LL/A with $2,499 mixes "
        "the old MPN with the new price and was excluded. The "
        "M5 Ultra (from $5,499, MHL74LL/A), the 40-core GPU "
        "tiers (48GB/1TB $3,399 Z1U4000E9) and M1/M2/M4 "
        "marketplace rows are different configurations. "
        "Distinct from the set's Mac mini M6 (MHQK4LL/A) and "
        "the iMac M6 (MH094LL/A).",
        status="verified",
    ),
    EvalProduct(
        key="sony-ult-wear-black",
        brand="Sony",
        model="ULT WEAR",
        variant="Black (WHULT900N/B)",
        category="headphones",
        identifiers={"UPC": "027242928688", "MPN": "WHULT900N/B"},
        identifier_sources={
            "UPC": "Amazon.com (WHULT900NB.UC, UPC 027242928688) "
            "+ Simcoe Audio Video Canada, authorized Sony "
            "dealer (barcode 027242928688, Black) + ShopCGX US "
            "(Style: 027242928688, $149.99, InStock) agree. The "
            "White UPC 027242929449 and the Target Plus bundle "
            "UPC 880136519894 (third-party gSport case bundle) "
            "are different codes and were excluded."
        },
        notes="Best Buy $148.00 (WHULT900N/B, SKU 6576179, "
        "Holiday Deal, comp value $248.00); Crutchfield "
        "$148.00 (In Stock, Item 158ULT900B, MFR WHULT900N/B, "
        "$100 off $248.00); BuyDig $148.00 (WHULT900N/B). "
        "Correction vs the 2026-10-31 candidate price: $249.99 "
        "is the list price; the current street price is $148 "
        "at all three retailers (Black Friday deal, Best Buy "
        "deal ends Nov 8). Sony direct price was not captured "
        "in this batch. The ULT WEAR (WH-ULT900N, 2024, ULT "
        "Power Sound bass line) is distinct from the set's "
        "WH-1000XM5 Black (027242923232), WH-1000XM6 Black "
        "(027242930698) and WH-1000XM4C Black (pending). "
        "Excluded: headphone+adapter / headphone+stand / "
        "warranty bundles ($169.99-$386), Coolblue NL $106 "
        "(non-US), the $25 copy row, and the Macy's SD-card "
        "bundle ($386).",
        status="verified",
    ),
    EvalProduct(
        key="sony-pulse-explore-midnight-black",
        brand="Sony",
        model="PULSE Explore Wireless Earbuds",
        variant="Midnight Black (retail MPN 1000044170, CFI-ZWE1)",
        category="earbuds",
        notes="MPN 1000044170 confirmed (Best Buy US Model + "
        "ShopCGX Model + P.C. Richard MODEL + Big Apple Buddy "
        "agree; hardware model CFI-ZWE1 per playstation.com), "
        "but the UPC was not verified from a non-Amazon US "
        "source, so identifiers stay empty per the DualSense "
        "Edge / DEX / Neo / PULSE Elite precedent. The only US "
        "UPC seen, 711719587972, appears on Amazon listings "
        "(ASIN B0DSQSX7FB, CFI-ZWE1) with no second source. "
        "The UK/AU barcode 711719590231 (HMV + Gamesmen) is a "
        "different regional code and was not copied. Best Buy "
        "$149.99 (page-verified JSON-LD InStock, Model "
        "1000044170, SKU 6614843, sold by Best Buy); Target "
        "$149.99 (feed row, A-94472835); GameStop $149.99 "
        "(feed row). ShopCGX $149.99 (feed row, Model "
        "1000044170, InStock) also confirmed. Correction vs "
        "the 2026-10-31 candidate price: $149 is $149.99, a "
        "sale price off the $199.99 list (P.C. Richard "
        "$199.99, currently OutOfStock). Midnight Black "
        "released 2025-02-20; the original White Explore is a "
        "different colorway. Distinct from the set's PULSE "
        "Elite Midnight Black (retail MPN 1000044173) — the "
        "Elite is the over-ear headset, the Explore is the "
        "earbuds line (CFI-ZWE1, not CFI-ZWH1, which is the "
        "PULSE 3D headset).",
    ),
    EvalProduct(
        key="logitech-wave-keys-graphite",
        brand="Logitech",
        model="Wave Keys",
        variant="Graphite (920-011898)",
        category="keyboards",
        notes="MPN 920-011898 confirmed for the US Graphite "
        "keyboard (Amazon.com US listing, Mfr Part Number "
        "920-011898 + Ryans Graphite 920-011898 agree), but "
        "the UPC 097855191533 appears only on that Amazon "
        "listing, with no second US source, so identifiers "
        "stay empty per the DualSense Edge / DEX / Neo / "
        "PULSE Elite precedent. Logitech direct $69.99 "
        "(page-verified JSON-LD InStock; the page default "
        "color is Off-white and the price is uniform $69.99 "
        "across colors, Graphite included per the Lenovo feed "
        "rows); Lenovo $69.99 (feed row, 'Wave Keys Wireless "
        "Ergonomic Keyboard - Graphite' — suspected, no "
        "identifier in the feed row); Newegg $69.99 (feed row "
        "— suspected). Correction vs the 2026-10-31 candidate "
        "note: $69.99 is the current price (the 2023 launch "
        "price was $59.99 per Logitech's blog). Excluded: the "
        "MK670 Wave Keys + mouse combo 920-012059 ($89.99, "
        "Best Buy Model 920-012059, SKU 10953065), Wave Keys "
        "for Business 920-012058 ($76.99-$139.99), Wave Keys "
        "for Mac 920-012402, the 2026 Sand refresh 920-013925 "
        "(B&H $69.99, Staples $77.27 — a different colorway), "
        "Wave Keys + Lift combos ($119.99), Rose and Off-White "
        "colorways (Off-White is 920-012275), the US "
        "International layout 920-012304 (EAN 5099206117471), "
        "AU Graphite 920-012281, and 920-013269 (a "
        "single-source roundup figure that conflicts with "
        "920-011898). Distinct from the set's ERGO K860 "
        "Graphite (920-009166) — the K860 is the split "
        "keyboard, Wave Keys is the wavy-keyframe keyboard.",
    ),
    EvalProduct(
        key="bose-sport-open-earbuds-black",
        brand="Bose",
        model="Sport Open Earbuds (2026)",
        variant="Black (901149-0010)",
        category="earbuds",
        notes="MPN 901149-0010 confirmed (Best Buy US Model + "
        "Abt + The Good Guys AU + BuyDig feed agree), but no "
        "UPC was found for the Black variant in any US source, "
        "so identifiers stay empty per the DualSense Edge / "
        "DEX / Neo / PULSE Elite precedent. B&H publishes only "
        "the Eucalyptus Green UPC 017817865449, which must NOT "
        "be copied to Black — different color, different "
        "barcode (Black 901149-0010, White Smoke 901149-0020, "
        "Eucalyptus Green 901149-0030). Best Buy $199.00 "
        "(page-verified JSON-LD InStock, Model 901149-0010, "
        "SKU 6688450, sold by Best Buy); Abt $199 (page-"
        "verified price); Lenovo $199 (feed row, brand_direct "
        "— suspected, no identifier in the feed row). Bose "
        "direct price was not shown in the bose.com page text "
        "this batch. The 2026 Sport Open Earbuds (announced "
        "2026-09-17, available 2026-10-01, clip-on open-ear, "
        "IP54, $199) are a new product, distinct from the "
        "set's QC Earbuds Black (888507-0100) and Ultra Open "
        "Earbuds 2nd Gen Black (897806-0010, $299). Excluded: "
        "the original 2021 Sport Open Earbuds 857628-0010 "
        "(UPC 017817826211, ASIN B08VRLZGMF — a different "
        "in-ear product, IPX4), the Eucalyptus Green and White "
        "Smoke colorways, and the Best Buy charger bundle "
        "($202.99).",
    ),
    # --- Expansion batch 10 (2026-11-06, DECISIONS 032) ---
    EvalProduct(
        key="apple-studio-display-2026-standard-tilt",
        brand="Apple",
        model="Studio Display (2026)",
        variant="Standard glass, Tilt-adjustable stand (MFEX4LL/A)",
        category="monitors",
        identifiers={"UPC": "195950529173", "MPN": "MFEX4LL/A"},
        identifier_sources={
            "UPC": "B&H Photo US spec page for the exact MPN "
            "(apple_mfex4ll_a, 2026 Standard Glass "
            "Tilt-Adjustable Stand, UPC 195950529173) + the "
            "B&H Studio Display with AppleCare+ page, which "
            "lists the same display UPC 195950529173 "
            "alongside the kit UPC 195951182148, agree. MPN "
            "MFEX4LL/A corroborated by Abt US (Model "
            "MFEX4LL/A, Tilt-adjustable Stand, $1,599, "
            "InStock) + Apple US buy page (from $1,599). The "
            "neighbouring UPC 195950528794 is the MFEW4LL/A "
            "(tilt-and-height stand) and 195950528992 is the "
            "UK MFEX4B/A GTIN; both were excluded."
        },
        notes="Apple direct $1,599.00 (US buy page 'from "
        "$1,599', base tilt config; the page JSON-LD $1,999 "
        "is a different selected config); B&H $1,549.00 "
        "(page-verified In Stock, JSON-LD InStock; Holiday "
        "Savings $50 off $1,599, limited supply at this "
        "price); Abt $1,599.00 (Model MFEX4LL/A, JSON-LD "
        "InStock). Correction vs the 2026-10-31 candidate "
        "note: the current Studio Display is the March 2026 "
        "refresh (A19 chip, Thunderbolt 5, 12MP Center Stage "
        "camera with Desk View, 27-inch 5K 60Hz 600-nit "
        "panel, on sale 2026-03-11), NOT the 2022 model — "
        "the 2022 Studio Display (A13, Thunderbolt 3, "
        "MK0U3LL/A, UPC 0194253030447) is superseded and was "
        "not added, though the base price is coincidentally "
        "the same $1,599. The Studio Display XDR (mini-LED, "
        "120Hz, from $3,299) is a separate line and was not "
        "added. Other 2026 configs excluded: MFEW4LL/A "
        "tilt-and-height $1,999, MFEY4LL/A VESA $1,599, "
        "MFF14LL/A nano-texture tilt $1,899, MFF04LL/A "
        "nano-texture tilt-and-height $2,299, MFF24LL/A nano "
        "VESA. First monitor in the set; distinct from the "
        "set's Mac desktops (Mac Studio MHL64LL/A, Mac mini "
        "MHQK4LL/A, iMac MH094LL/A).",
        status="verified",
    ),
    EvalProduct(
        key="sony-linkbuds-fit-black",
        brand="Sony",
        model="LinkBuds Fit",
        variant="Black (WF-LS910N/B)",
        category="earbuds",
        identifiers={"UPC": "027242929289", "MPN": "WFLS910N/B"},
        identifier_sources={
            "UPC": "B&H Photo US spec page for the exact MPN "
            "(sony_wfls910n_b, UPC 027242929289) + Tanotis "
            "(Sony WFLS910N/B, UPC 027242929289) agree. MPN "
            "WFLS910N/B corroborated by Best Buy US Model "
            "WFLS910N/B (SKU 6594431) + Sony US "
            "(WF-LS910N/P is the Pink variant). The NZ EAN "
            "4548736157897 is a different regional code and "
            "was excluded."
        },
        notes="Best Buy $199.99 (Model WFLS910N/B, SKU 6594431, "
        "JSON-LD price; stock not stated in the page-text "
        "crawl); B&H $198.00 (page-verified, UPC "
        "027242929289; Special Order, expected availability "
        "2-4 Weeks — not in stock at B&H; Holiday Savings "
        "$30 off $228.00); Crutchfield $198.00 (feed row — "
        "suspected, no identifier in the feed row). "
        "Correction vs the 2026-10-31 candidate price: "
        "$229.99 is the list price; the current street price "
        "is $198–$199.99 (Dell Black $229.99 brand_direct and "
        "Sony direct Pink $229.99, sale $199.99, also seen). "
        "Distinct from the set's WF-1000XM5 Black "
        "(027242925601) and WF-1000XM6 Black (027242933460) "
        "— the LinkBuds Fit (WF-LS910N, 2024, open-fit "
        "Air Fitting Supporters) is a separate line, and "
        "from the LinkBuds Open (also $228), which was "
        "excluded. White, Sage Green, Pink and Violet are "
        "different colorways.",
        status="verified",
    ),
    EvalProduct(
        key="sony-access-controller-white",
        brand="Sony",
        model="Access Controller",
        variant="White (retail MPN 1000037579, CFI-ZAC1)",
        category="controllers",
        notes="Retail MPN 1000037579 confirmed (Best Buy US "
        "Model, SKU 12348387) and hardware model CFI-ZAC1 "
        "confirmed (playstation.com accessories page, Model "
        "Number - CFI-ZAC1 + SIE manuals), but no UPC was "
        "verified from a US source, so identifiers stay "
        "empty per the DualSense Edge / DEX / Neo / PULSE "
        "Elite precedent. The only barcode seen, "
        "711719567929, is a UK EAN (Very.co.uk) with no US "
        "source and was not copied. PlayStation Direct "
        "$89.00 (page-verified, Color: White, release "
        "12/06/2023; stock not stated in the page-text "
        "crawl); GameStop $89.99 (feed row — suspected, no "
        "identifier in the feed row); Target $87.99 (Target "
        "search listing — suspected, no identifier in the "
        "listing). Correction vs the 2026-10-31 candidate "
        "price: $89 is $89.00 direct / $89.99 list (Best "
        "Buy comp value $89.99; Best Buy's live $79.95 "
        "offer is sold by marketplace seller A2Z Games Inc "
        "and was excluded per DECISIONS 021). The Access "
        "controller is the only colorway (White); distinct "
        "from the set's DualSense White (pending) and "
        "DualSense Edge Black & White (CFI-ZCP1, pending) — "
        "the Access (CFI-ZAC1) is the PS5 accessibility "
        "controller kit, not a standard pad.",
    ),
    EvalProduct(
        key="logitech-pop-keys-cosmos",
        brand="Logitech",
        model="POP Keys",
        variant="Cosmos (920-011233)",
        category="keyboards",
        notes="MPN 920-011233 confirmed (Dell US Manufacturer "
        "Part Number + Colamco + BuyDig + iFixit agree; "
        "logitech.com product URL carries .920-011233), but "
        "the UPC 097855179401 appears only on the Amazon "
        "listing (ASIN B0BMX9KRDN), with no second US "
        "source, so identifiers stay empty per the Wave "
        "Keys / DualSense Edge precedent. Logitech direct "
        "$99.99 (page-verified JSON-LD InStock; Color "
        "Cosmos); Dell $89.99 (feed row, brand_direct — "
        "suspected, no identifier in the feed row; sale off "
        "the $99.99 list); Colamco $99.99 (search-verified, "
        "MPN 920-011233 stated). Correction vs the "
        "2026-10-31 candidate note: $99.99 is confirmed "
        "current (the feed's Best Buy Blast Yellow $69.99 "
        "and Heartbreaker Rose $117.22 rows are different "
        "colorways / sale prices). Excluded: Blast Yellow "
        "920-010707, Heartbreaker Rose 920-010709, Daydream, "
        "Mist 920-011232, the POP Icon Keys line ($49.99, a "
        "different keyboard), POP Mouse rows ($29.99–$39.99, "
        "the mouse not the keyboard), the AU Cosmos Lavender "
        "920-011227 (GTIN 097855179340, a different "
        "regional variant), and the POP Keys + POP Mouse "
        "combo. Distinct from the set's MX Mechanical "
        "Graphite (920-010547), MX Keys S Pale Grey "
        "(920-011559), MX Keys Mini Black (920-010475), "
        "ERGO K860 Graphite (920-009166) and Wave Keys "
        "Graphite (920-011898) — POP Keys is the "
        "typewriter-style emoji-key line.",
    ),
    EvalProduct(
        key="xbox-elite-series-2-core-white",
        brand="Microsoft",
        model="Xbox Elite Wireless Controller Series 2 – Core",
        variant="White (4IK-00001)",
        category="controllers",
        notes="MPN 4IK-00001 confirmed (Best Buy US Model + "
        "P.C. Richard MODEL + ThinkEdu + Microsoft Store "
        "agree), but the UPC was not verified from a US "
        "source, so identifiers stay empty per the "
        "DualSense Edge / DEX / Neo / PULSE Elite "
        "precedent. The only barcodes seen conflict and are "
        "both non-US: Gamesmen AU 889842717082 vs a "
        "Latvian listing 889842717075; neither was copied. "
        "Microsoft direct $111.74 (page-verified JSON-LD "
        "price; stock not confirmed in the page text); Best "
        "Buy $149.99 (Model 4IK-00001, SKU 6514400, price "
        "shown on the Best Buy reviews-page crawl); P.C. "
        "Richard $149.99 (MODEL: 4IK-00001, JSON-LD). "
        "Correction vs the 2026-10-31 candidate range "
        "$111.74–$139.99: $111.74 is the current Microsoft "
        "Store sale price and $149.99 is the current "
        "retailer list (Kohl's and Lenovo also $149.99; "
        "Target lists it at $109.99); the $139.99 ShopCGX "
        "feed row is titled 'Series 2', not Core, and was "
        "not used. Distinct from the set's full Elite "
        "Series 2 Black (FST-00001, UPC 889842196344, "
        "$159.99–$179.99) — the Core (4IK-00001) is the "
        "cheaper line without the component pack, dock and "
        "case — and from the set's Xbox Wireless Controller "
        "Carbon Black (1914). The 2025 Core colorways (Blue, "
        "Red and Blue, Green and Blue, Astral Purple, Gray, "
        "Dark Green, all $149.99 at Best Buy) are different "
        "models and were excluded.",
    ),
    # --- Expansion batch 11 (2026-11-06, continuous expansion per DECISIONS 027) ---
    # 77 -> 82 models. DECISIONS 033, BUILD_LOG 049.
    EvalProduct(
        key="apple-magic-trackpad-usbc",
        brand="Apple",
        model="Magic Trackpad (USB-C)",
        variant="White Multi-Touch Surface (MXK93AM/A)",
        category="mice",
        identifiers={"UPC": "195949654305", "MPN": "MXK93AM/A"},
        identifier_sources={
            "UPC": "Apple US official store page for MXK93AM/A "
            "(Part Number UPC or EAN No.: 195949654305) + "
            "Adorama US spec (SKU ACMXK93AMA, MFR MXK93AM/A, "
            "UPC 195949654305) + eBay US product identifiers "
            "(GTIN 0195949654305, MPN MXK93AMA) agree. The "
            "Black variant MXKA3AM/A is a different color and "
            "a different price ($149) and was excluded."
        },
        notes="Apple direct $129.00 (US store page JSON-LD, "
        "InStock, page-verified 2026-11-06); CDW $129.00 "
        "(feed row, White/Silver, authorized retailer); "
        "Target $129.99 (feed row, White Multi-Touch "
        "Surface, authorized retailer); P.C. Richard "
        "$129.00 (feed row, MXK93AM/A) also seen. "
        "Correction vs the 2026-10-31 candidate price: "
        "$129 is the White price; the Black trackpad "
        "(MXKA3AM/A) is $149 at Apple direct, Staples and "
        "P.C. Richard ($149.99 at Best Buy) and is a "
        "different colorway, not a price move. Distinct "
        "from the set's Magic Mouse USB-C White (MXK53AM/A, "
        "UPC 195949655883) — the Trackpad is the distinct "
        "glass-trackpad line, not a mouse.",
        status="verified",
    ),
    EvalProduct(
        key="sony-wh-ch720n-black",
        brand="Sony",
        model="WH-CH720N",
        variant="Black (WHCH720N/B)",
        category="headphones",
        identifiers={"UPC": "027242925397", "MPN": "WHCH720N/B"},
        identifier_sources={
            "UPC": "B&H Photo US spec page for WHCH720N/B "
            "(BH #SOWHCH720NB, UPC 027242925397) + eBay US "
            "product identifiers (MPN WH-CH720N/B, UPC "
            "027242925397) + Ubuy (Model WHCH720N/B, UPC "
            "027242925397) + Amazon.ca (Model WHCH720N/B, "
            "UPC 027242925397, ASIN B0BS1QCFHX) agree. The "
            "Blue WHCH720N/L UPC 027242925502 and the EU "
            "WHCH720NB.CE7 EAN 4548736142428 are different "
            "variants and were excluded."
        },
        notes="Sony direct $89.99 (electronics.sony.com "
        "WHCH720N/B page, JSON-LD $89.99, Save $90.00 off "
        "$179.99; free shipping, est. delivery Nov 3-4, "
        "page-verified 2026-11-06); BJ's $179.99 (feed row, "
        "authorized retailer); P.C. Richard $179.95 (feed "
        "row, WHCH720N-B, authorized retailer); B&H $178.00 "
        "(page-verified In Stock, JSON-LD InStock — page "
        "crawled 2026-09-12, so the price is dated). "
        "Correction vs the 2026-10-31 candidate price: "
        "$89.99 is the current Sony direct sale price, not "
        "a stale figure — the launch MSRP was $149.99 "
        "(Sony press release 2023-02-21), while Sony's own "
        "page now lists MSRP $179.99 and a $90 saving. "
        "Street price at retailers is $178–$180. Distinct "
        "from the set's WH-1000XM5/XM6 Black, WH-1000XM4C "
        "Black and ULT WEAR Black — the CH720N is Sony's "
        "lightweight mid-range noise-cancelling line "
        "(2023, Integrated Processor V1, 35-hour battery). "
        "Blue, White and Pink are different colorways.",
        status="verified",
    ),
    EvalProduct(
        key="logitech-g915-x-lightspeed-tactile-black",
        brand="Logitech",
        model="G915 X LIGHTSPEED",
        variant="Full-size, GL Tactile (Brown), Black (920-012670)",
        category="keyboards",
        identifiers={"UPC": "097855195005", "MPN": "920-012670"},
        identifier_sources={
            "UPC": "B&H Photo US spec page for 920-012670 "
            "(UPC 097855195005) + Abt US (Model 920-012670, "
            "UPC 097855195005, Tactile Wireless in Black) + "
            "Amazon US (Model 920-012670, UPC 097855195005, "
            "ASIN B0DB1WNZJY) + Desertcart (Mfr Part "
            "920-012670, UPC 097855195005) agree. The "
            "Linear 920-012696 UPC is 097855195166 and the "
            "Clicky 920-012704 UPC is 097855195029 — "
            "different switches, different codes, both "
            "excluded."
        },
        notes="Logitech G direct $259.99 (logitechg.com "
        ".920-012670 page, JSON-LD InStock, page-verified "
        "2026-11-06; Color Black); Best Buy $259.99 (Model "
        "920-012670, SKU 6595193, Sold by Best Buy, JSON-LD "
        "InStock, page-verified 2026-11-06); B&H $219.99 "
        "(sale, was $259.99, In Stock, search-index); "
        "Quill $259.99 (Model 920-012670) also seen. "
        "Correction vs the 2026-10-31 candidate price: "
        "$129.99 was an Amazon Clicky-switch deal price "
        "(Grail Alerts 2026-11-01; pricehistory.app Clicky "
        "920-012704 at $129.99), not the standard US "
        "Tactile price — the LIGHTSPEED full-size Tactile "
        "is $259.99 at Logitech G, Best Buy and Quill. "
        "Variant pinning: full-size LIGHTSPEED, GL Tactile "
        "(Brown), Black is the standard US variant — the "
        "logitechg.com page defaults to the full-size "
        "LIGHTSPEED line at $259.99 with per-switch URLs "
        "(.920-012670 Tactile, .920-012696 Linear, "
        ".920-012704 Clicky); TKL ($229.99, Tactile Black "
        "920-012726) and the wired Linear (920-012950, "
        "$199.99 / $169.99 at Staples) are different "
        "configurations. The feed's Best Buy $259.99 "
        "Tactile row is the White variant (SKU 6595195, "
        "920-012685) and was not used for the Black price. "
        "Distinct from the set's MX Mechanical, MX Keys "
        "Mini/S, ERGO K860, Wave Keys and POP Keys — the "
        "G915 X is Logitech G's low-profile wireless "
        "gaming keyboard line.",
        status="verified",
    ),
    EvalProduct(
        key="xbox-adaptive-controller",
        brand="Microsoft",
        model="Xbox Adaptive Controller",
        variant="White (JMU-00003)",
        category="controllers",
        notes="Retail MPN JMU-00003 confirmed (Best Buy US "
        "current listing, Model JMU-00003, SKU 6455394, "
        "Sold by Best Buy, $99.99, JSON-LD InStock, "
        "page-verified via search index 2026-11-06; "
        "Microsoft Store product page also $99.99, "
        "xbox.com JSON-LD InStock). The older Best Buy "
        "listing JMU-00001 (SKU 6381218) is no longer "
        "available in new condition and was not used. UPC "
        "is unresolved: 889842295368 (eBay product "
        "identifiers, GTIN 0889842295368, MPN JMU-00003) "
        "vs 889842439038 (PriceCharting, model 1836; also "
        "an eBay listing ties this code to JMU-00003) — "
        "two codes circulate for the same MPN and no US "
        "retailer spec page states a UPC, so identifiers "
        "stay empty per the DualSense Edge / DEX / Neo / "
        "PULSE Elite precedent. Microsoft direct $99.99 "
        "(microsoft.com / xbox.com JSON-LD; stock not "
        "confirmed in the microsoft.com page text — "
        "price-only); Best Buy $99.99 (Model JMU-00003, "
        "SKU 6455394, JSON-LD InStock). Correction vs the "
        "2026-10-31 candidate price: $99.99 is confirmed "
        "current at both Microsoft Store and Best Buy. "
        "Excluded: CDW $128.99 and BuyDig $124.99 (above "
        "list), FlexShopper $123.99 (marketplace, "
        "DECISIONS 021), the Adaptive Joystick ($29.99, a "
        "companion accessory, not the controller) and the "
        "Adaptive Dual Button ($59.99, a different "
        "accessory). Distinct from the set's Xbox Wireless "
        "Controller Carbon Black (1914), Elite Series 2 "
        "Black (FST-00001) and Elite Series 2 Core White "
        "(4IK-00001) — the Adaptive Controller (2018, "
        "still Microsoft's current accessibility "
        "controller, sold new at Microsoft Store and Best "
        "Buy) is the large-button hub for external "
        "switches, buttons, mounts and joysticks.",
    ),
    EvalProduct(
        key="keychron-k8-hot-swappable-red",
        brand="Keychron",
        model="K8",
        variant="White Backlight, Keychron Super Switch (Hot-Swappable), Red (K8-G1)",
        category="keyboards",
        identifiers={"UPC": "617748997921", "SKU": "K8-G1"},
        identifier_sources={
            "UPC": "Keychron official store public product "
            "JSON (product id 4669741170777, variant "
            "32018252791897, SKU K8-G1, barcode "
            "617748997921, $69.99) + Desertcart spec table "
            "(Mfr Part Number K8 G1, UPC 617748997921, "
            "ASIN B0875W65Z2) agree. The JSON field is "
            "named 'barcode' (no separate GTIN/UPC/EAN "
            "field); the 12-digit code is the UPC-A form, "
            "recorded as UPC (the K8 Pro / K8 Ultra 8K "
            "precedent recorded 13-digit barcodes as EAN). "
            "The old-K8 barcode 753610396260 does not "
            "appear in the current JSON and was not used; "
            "617748997846 is K8-A2 (Blue, Gateron G Pro), "
            "a different variant."
        },
        notes="Keychron direct $69.99 (keychron.com K8 page, "
        "variant K8-G1, price-only: K8-G1 shows out of "
        "stock in the 2026-11-06 JSON read but was "
        "Available in the search-index crawl 2 days "
        "earlier, and the Blue/Brown hot-swappable "
        "siblings K8-G2/K8-G3 are in stock — inventory "
        "churn, not discontinuation). Variant pinning: "
        "the base K8 line has 36 variants (White/RGB "
        "backlight, plastic/aluminum frame, Gateron G Pro "
        "/ Keychron Super / Gateron Optical / Keychron "
        "Optical, Red/Blue/Brown); the pinned variant "
        "mirrors the K8 Pro precedent (hot-swappable, "
        "White Backlight, Red) — K8-G1 is the "
        "hot-swappable Red, $69.99, page SKU K8-G1. The "
        "page-default K8-A1 (White Backlight, Gateron G "
        "Pro Mechanical, Red, $59.99) is the soldered "
        "version, not hot-swappable, and is also out of "
        "stock in this read, so it was not pinned. The "
        "RGB hot-swappable Red K8-H1 ($79.99, in stock) "
        "and the aluminum-frame variants ($79.99–$89.99) "
        "are different configurations. Correction vs the "
        "2026-10-31 candidate price: the base K8 starts "
        "at $59.99 (K8-A1) and the hot-swappable Red is "
        "$69.99. Excluded: Newegg K8 rows ($127.99 "
        "Version 2 QMK, $126.55 White Backlight — "
        "third-party/unclear variant, DECISIONS 021), "
        "Newegg K8 HE $221.48 and K8 Pro $217.91 "
        "(different models), Woot $39.99 (deal/clearance, "
        "variant ambiguous, 90-day warranty). Distinct "
        "from the set's K8 HE Special Black (K8H-F1) and "
        "K8 Ultra 8K (K8U-J1) — the base K8 (K8-G1) is "
        "the original tenkeyless line, not the Hall "
        "Effect or 8K-polling successor. Like the K8 HE, "
        "the base K8 is sold through Keychron's own store "
        "only, so it holds a single quote.",
        status="verified",
    ),
    EvalProduct(
        key="apple-magic-keyboard-touch-id-numeric-keypad-white",
        brand="Apple",
        model="Magic Keyboard with Touch ID and Numeric Keypad (USB-C)",
        variant="US English, White Keys (MJM64LL/A)",
        category="keyboards",
        notes="Apple direct $179.00 (US store page JSON-LD, InStock, "
        "page-verified 2026-11-06); Best Buy $179.99 (Model MJM64LL/A, "
        "SKU 6556937, Sold by Best Buy); NFM $180.00 (feed row, White). "
        "MPN MJM64LL/A confirmed (Apple US store page + Best Buy US "
        "listing agree). UPC 195951258324 is stated on the Apple US store "
        "page only — no second source surfaced (Adorama lists the older "
        "MXK73LL/A, Best Buy shows no UPC), so identifiers stay empty per "
        "the Adaptive Controller / DualSense precedent; re-check next "
        "refresh. Correction vs the 2026-10-31 candidate range $99-$199: "
        "$99 is the plain Magic Keyboard (different model) and $129 the "
        "Numeric-Keypad-only Lightning model; the Touch ID + Numeric "
        "Keypad USB-C White is $179 (Black Keys MJM74LL/A is $199, a "
        "different colorway). The 2026 MJM64LL/A supersedes the older "
        "MXK73LL/A (Adorama, $179.00, on backorder to 01/2027). Distinct "
        "from the set's Magic Mouse USB-C White (MXK53AM/A) and Magic "
        "Trackpad USB-C White (MXK93AM/A) — the Keyboard is the distinct "
        "typing line, not a mouse or trackpad.",
    ),
    EvalProduct(
        key="sony-wf-c710n-black",
        brand="Sony",
        model="WF-C710N",
        variant="Black (WFC710N/B)",
        category="earbuds",
        identifiers={"UPC": "027242931770", "MPN": "WFC710N/B"},
        identifier_sources={
            "UPC": "Amazon US product info (Model WFC710N/B, UPC "
            "027242931770, ASIN B0DWHPBK42) + Snapklik (Model WFC710N/B, "
            "UPC 027242931770) + Beach Camera Meta Catalog feed row "
            "(brand field 027242931770) agree. The White UPC is "
            "027242931794 and the Glass Blue UPC is 027242931817 — "
            "different colorways, both excluded."
        },
        notes="Best Buy $98.00 (Model WFC710N/B, SKU 6620461, Sold by Best "
        "Buy, JSON-LD InStock, page-verified 2026-11-06); Dell $129.99 "
        "(feed row, Black); Beach Camera $98.00, Crutchfield $98.00, Abt "
        "$98.00 (feed rows, Black). Correction vs the 2026-10-31 "
        "candidate price: $129.99 is the list price (Sony US store), "
        "while the current street/sale price is $98 at Best Buy, Abt, "
        "Crutchfield and Beach Camera. Sony direct Black price was not "
        "freshly confirmed (the Sony Black page crawl is stale at the "
        "$119.99 launch price; the White page shows a $99.99 sale) — "
        "re-check next refresh. Distinct from the set's WF-1000XM5/XM6 "
        "Black — the C710N (2025) is Sony's everyday mid-range "
        "noise-cancelling line. White, Glass Blue and Pink are different "
        "colorways.",
        status="verified",
    ),
    EvalProduct(
        key="sony-linkbuds-open-black",
        brand="Sony",
        model="LinkBuds Open",
        variant="Black (WFL910/B)",
        category="earbuds",
        identifiers={"UPC": "027242928695", "MPN": "WFL910/B"},
        identifier_sources={
            "UPC": "Amazon US product info (Model WFL910B.UC, UPC "
            "027242928695, ASIN B0DGVH7FJV) + Simcoe Audio Video "
            "(authorized Sony dealer, Barcode 027242928695, Black) + "
            "Ubuy (UPC 027242928695, Model WFL910B.UC) agree. The White "
            "UPC is 027242928701 (B&H + Abt agree) — a different "
            "colorway, excluded."
        },
        notes="Sony direct $229.99 (electronics.sony.com WFL910/B page, "
        "JSON-LD $229.99, 'Only 3 left', page-verified 2026-11-06); Dell "
        "$229.99 (feed row, Black); Best Buy $228.00 (feed row, Black); "
        "BuyDig $228.00 (Part # WFL910/B, In Stock, page-verified). "
        "Correction vs the 2026-10-31 candidate price: $229.99 is "
        "confirmed current at Sony direct and Dell. Distinct from the "
        "set's LinkBuds Fit Black (WFLS910N/B) — the Open (WF-L910, "
        "2024, open-ring driver) is the distinct open-ear line, not the "
        "noise-cancelling Fit; the LinkBuds Clip (WFLC900, 2026 clip-on "
        "line) is a different model and its rows were excluded. Sony "
        "direct stock is low ('Only 3 left') — re-check next refresh.",
        status="verified",
    ),
    EvalProduct(
        key="logitech-pro-x-tkl-lightspeed-tactile-black",
        brand="Logitech",
        model="PRO X TKL LIGHTSPEED",
        variant="GX Brown Tactile, Black (920-012127)",
        category="keyboards",
        notes="Lenovo US $219.99 (Black, page-verified 'Available Soon' — "
        "price-only, stock not confirmed); Focus Camera $219.99 "
        "(920-012127, feed row); CDW $219.99 (feed row). MPN 920-012127 "
        "confirmed (Best Buy US Model 920-012127, SKU 10111534 + BuyDig "
        "Part # 920-012127 + manuals.plus spec table + Amazon US ASIN "
        "B0BQBSH6NQ agree). UPC 097855188984 appears in eBay product "
        "identifiers only — no second source surfaced, so identifiers "
        "stay empty per the Adaptive Controller / DualSense precedent; "
        "re-check next refresh. Correction vs the 2026-10-31 candidate "
        "price: $219.99 is confirmed as the current list (the launch SRP "
        "was $199); the Logitech G direct US price was not confirmed in "
        "page text — re-check. White 920-012143 ($151.99 sale) and "
        "Magenta 920-012154 ($189.99 sale) are different colorways; "
        "Linear Black 920-012122 is a different switch; the PRO X TKL "
        "RAPID (920-013131, wired Hall-Effect) and the PRO X 60 (60%) "
        "are different models. Distinct from the set's G915 X "
        "LIGHTSPEED Tactile Black (920-012670, low-profile) and the PRO "
        "X Superlight 2 mice — the PRO X TKL is Logitech G's standard "
        "tenkeyless wireless gaming keyboard.",
    ),
    EvalProduct(
        key="keychron-q1-knob-navy-blue-red",
        brand="Keychron",
        model="Q1 (Version 2)",
        variant="Fully Assembled Knob, Navy Blue - B, Gateron G Pro Red (Q1-O1Z)",
        category="keyboards",
        notes="Keychron direct $89.99 (sale, was $189.99; official store "
        "public product JSON, variant Q1-O1Z available:true, "
        "page-verified 2026-11-06). SKU Q1-O1Z and EAN 4895248817345 "
        "come from the Keychron JSON only — no second source surfaced, "
        "so identifiers stay empty per the Adaptive Controller / "
        "DualSense precedent; re-check next refresh. Correction vs the "
        "2026-10-31 candidate range $229.99-$254.99: that was the Q-line "
        "range (the Q1 Max is $229.99), not the base Q1 — the base Q1 V2 "
        "fully assembled knob lists $189.99 and is currently $89.99 on "
        "sale at Keychron direct. Variant pinning: the page-default "
        "in-stock variant — Fully Assembled Knob / Navy Blue - B / "
        "Gateron G Pro Red; the Carbon Black knob Red Q1-M1Z (EAN "
        "4895248817284) and all Carbon Black / Silver Grey knob variants "
        "are out of stock in this read, while Navy Blue - B Red/Blue/"
        "Brown and the Barebone Knob Carbon Black / Navy Blue are in "
        "stock. The Q1 Pro / Max / HE / Ultra 8K are different models. "
        "Distinct from the set's K8 lines (K8-G1, K8 HE, K8 Ultra 8K) — "
        "the Q1 is the original 75% full-aluminum Q-series line. Like "
        "the K8, the base Q1 is sold through Keychron's own store only, "
        "so it holds a single quote.",
    ),
    EvalProduct(
        key="apple-macbook-pro-14-proled-xdr",
        brand="Apple",
        model="MacBook Pro 14-inch with PROLED XDR Display",
        variant="M5 Pro 15-core CPU/16-core GPU, 24GB/1TB, Space Black, Standard display (MJ2K4LL/A)",
        category="laptops",
        notes="Apple direct $2,899 (US store buy page, 'Available starting "
        "11.6', page-verified 2026-11-06 — the page text lists the "
        "configuration but not the price; $2,899 per the Apple "
        "announcement and Best Buy); Best Buy $2,899 (Model MJ2K4LL/A, "
        "SKU 6565892, Sold by Best Buy, JSON-LD InStock, page-verified; "
        "free $100 e-gift card promo with purchase). MPN MJ2K4LL/A "
        "confirmed by Best Buy US only (the AU/NZ MJ2K4X/A is the same "
        "configuration in a different region suffix, not a US "
        "confirmation), and UPC 195951196749 is stated in the Adorama "
        "spec table only — no second source surfaced for either, so "
        "identifiers stay empty per the Adaptive Controller / DualSense "
        "precedent; re-check next refresh. Correction vs the 2026-10-31 "
        "candidate note 'from $2,899 (pre-order 11.6)': confirmed "
        "current, and the base 14-inch is M5 Pro 15-core/16-core with "
        "24GB/1TB — not M6. The 16-inch (from $3,399), M5 Max "
        "configurations (from $4,499), the 48GB/1TB Space Black "
        "MMF64LL/A ($3,699 at Adorama) and the Nano-texture display "
        "are different configurations. Distinct from the set's "
        "apple-macbook-pro-14-m6 (the separate entry-level M6 line, "
        "MHWT4LL/A, $1,999, UPC pending) and from the Liquid Retina "
        "XDR M5 Pro 24GB/1TB (MGDR4LL/A, $2,499) — the PROLED XDR is "
        "the distinct touchscreen tandem-OLED line announced 2026-10-28, "
        "on sale from 2026-11-06.",
    ),
    EvalProduct(
        key="sony-wf-c510-black",
        brand="Sony",
        model="WF-C510",
        variant="Black (WFC510/B)",
        category="earbuds",
        notes="Best Buy $59.99 (Model WFC510/B, SKU 6594425, JSON-LD "
        "InStock, page-verified 2026-11-06); B&H Photo $58.00 (In "
        "Stock, was $68.00, page-verified); Abt $58.00 (feed row; "
        "manufacturer rebate ends 11/08/2026, comp. value $68); "
        "Electronic Express $58.00 and Focus Camera $58.00 (feed rows, "
        "Black); Fred Meyer $69.99 (JSON-LD InStock, page-verified — "
        "the list price). MPN WFC510/B confirmed (Best Buy US Model + "
        "B&H + Sony AU Model WFC510B agree), but UPC 027242930339 is "
        "stated on the B&H spec page only — no second non-Amazon US "
        "source surfaced, so identifiers stay empty per the Adaptive "
        "Controller / DualSense / PULSE Elite precedent; re-check next "
        "refresh. Correction vs the 2026-10-31 candidate price $69.99: "
        "that is the list price — the current street price is $58 at "
        "B&H, Abt, Electronic Express and Focus Camera and $59.99 at "
        "Best Buy. White (UPC 027242930346), Blue and Yellow are "
        "different colorways. Distinct from the set's WF-C710N Black "
        "(WFC710N/B) and WF-1000XM5/XM6 Black — the C510 (2024) is "
        "Sony's compact everyday budget line, no noise cancelling.",
    ),
    EvalProduct(
        key="sony-inzone-h5-black",
        brand="Sony",
        model="INZONE H5",
        variant="Black (WHG500/B)",
        category="headphones",
        notes="Focus Camera $128.00 (Black, $128 vs $178, page-verified "
        "2026-11-06 — the Meta Catalog feed row for the same URL was "
        "$178, so the price has dropped since the feed was cut); "
        "Datavision $128.00 (feed row, Black); Abt $128.00 "
        "(page-verified — price-only: 'Notify me when this item is "
        "available', PreOrder; manufacturer rebate ends 11/22/2026, "
        "comp. value $178). MPN WHG500/B confirmed (Best Buy US Model "
        "WHG500/B, SKU 6562125 + Crutchfield MFR # WHG500/B + Abt "
        "agree), but UPC 027242927919 appears in the Sony spec sheet "
        "via manuals.plus only — no second non-Amazon US source "
        "surfaced, so identifiers stay empty per the Adaptive "
        "Controller / DualSense / PULSE Elite precedent; re-check next "
        "refresh. Correction vs the 2026-10-31 candidate price "
        "~$249.99: that matches no current US price — the current US "
        "street price is $128 at Focus Camera, Datavision and Abt "
        "(comp. value $178); Sony direct lists the White at $159.99 "
        "sale / $179.99 original (stale category crawl; the Black "
        "direct price was not confirmed) and is not quoted. White "
        "(UPC 027242927896) is a different colorway. Distinct from "
        "the set's PULSE Elite / PULSE Explore headsets and from the "
        "INZONE Buds (WF-G700N) and INZONE H9 — the H5 (WH-G500, "
        "2023) is the first INZONE headset in the set, Sony's "
        "mid-range wireless gaming headset (360 Spatial Sound, 28-hour "
        "battery, no active noise cancelling).",
    ),
    EvalProduct(
        key="logitech-pro-x2-superstrike-lunar-eclipse",
        brand="Logitech",
        model="PRO X2 SUPERSTRIKE LIGHTSPEED",
        variant="Lunar Eclipse (910-007700)",
        category="mice",
        notes="B&H Photo $179.99 (In Stock, page-verified 2026-11-06); "
        "Abt $179.99 (Lunar Eclipse, search-index read); Target "
        "$179.99, Lenovo $179.99 and Electronic Express $179.99 "
        "(feed rows, 910-007700 / Lunar Eclipse). The candidate called "
        "this a gaming keyboard — it is a MOUSE: the PRO X2 "
        "SUPERSTRIKE LIGHTSPEED wireless gaming mouse with the Haptic "
        "Inductive Trigger System (HITS), HERO 2 sensor, 8 kHz "
        "polling, 61 g, white casing with black buttons (the only US "
        "colorway, Lunar Eclipse). MPN 910-007700 confirmed (B&H + "
        "Abt + Electronic Express agree), but UPC 097855211309 is "
        "stated on the B&H spec page only — no second non-Amazon US "
        "source surfaced, so identifiers stay empty per the Adaptive "
        "Controller / DualSense / PULSE Elite precedent; re-check next "
        "refresh. The Logitech G direct US price was not confirmed in "
        "page text (Notebookcheck reports $179.99 at the Logitech "
        "online store). The PRO X3 SUPERSTRIKE (910-007876, $199.99 "
        "at Best Buy, Midnight Black) is the newer successor, a "
        "different model — not added. The EU/Asia 910-007777 / "
        "910-007778 part numbers are different regional variants. "
        "Distinct from the set's PRO X Superlight 2 Black "
        "(910-006628) and Superlight 2 DEX — the Superstrike is "
        "Logitech G's haptic-trigger PRO mouse line, not a Superlight.",
    ),
    EvalProduct(
        key="keychron-b40-deep-black",
        brand="Keychron",
        model="B40",
        variant="75% Alice, Deep Black (B40-K9)",
        category="keyboards",
        notes="Keychron direct $49.99 (official store, Deep Black variant "
        "Available, page-verified 2026-11-06). SKU B40-K9 comes from "
        "the Keychron official store page only and no UPC/EAN for the "
        "B40 surfaced anywhere, so identifiers stay empty per the "
        "Adaptive Controller / DualSense precedent; re-check next "
        "refresh. Correction vs the 2026-10-31 candidate price: $49.99 "
        "is confirmed current at Keychron direct. Variant pinning: "
        "Deep Black is the only colorway sold (75% Alice layout, "
        "scissor-key, tri-mode 2.4 GHz / Bluetooth 5.2 / USB-C, "
        "800 mAh, up to 330 hours in 2.4 GHz mode). The B39 (96% "
        "Alice, $54.99, B39-K9) is the larger sibling, a different "
        "model — not added. Distinct from the set's K8 lines (K8-G1, "
        "K8 HE, K8 Ultra 8K) and Q1 — the B40 is Keychron's budget "
        "Alice-layout scissor-switch line, sold through Keychron's own "
        "store only, so it holds a single quote.",
    ),
]


def get_product(key: str) -> EvalProduct:
    for product in EVAL_SET:
        if product.key == key:
            return product
    raise KeyError(f"unknown eval model key: {key}")
