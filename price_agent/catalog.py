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
    EvalProduct(
        key="sony-mdr-7506",
        brand="Sony",
        model="MDR-7506",
        variant="Black, standard edition (MDR7506)",
        category="headphones",
        notes="Sony direct $114.99 (MSRP, JSON-LD price on electronics.sony.com; page crawled 2026-10-17, stock not stated in the page text); Abt $113.00 (JSON-LD InStock, page-verified); Sweetwater $113.00 (Open Graph instock, page-verified); Full Compass, Samy's and Vintage King $114.99 and Focus Camera $113.00 (feed rows — suspected, no identifier in the feed rows); MusicArts $89.99 (feed row — suspected; the low outlier vs $113–$114.99 elsewhere, not page-verified). Correction vs the 2026-10-31 candidate price: $114.99 is confirmed current at Sony direct. Identifiers PENDING: MPN MDR7506 confirmed (Sony US + Abt + Sweetwater agree), but no UPC for the MDR-7506 surfaced on any US manufacturer or retailer spec page checked (Sony direct, Abt, Sweetwater, B&H), so identifiers stay empty per the Adaptive Controller / DualSense / PULSE Elite precedent. Excluded: Best Buy $119.99 (bundle with a desktop headphone stand), Newegg $160.99 (open-box 'Level 2') and $163.99 (International Model, no US warranty), Sweetwater $162.99 (bundle with bag), B&H $157.94 (bundle with earpads and case). Distinct from the set's other Sony lines — the set has no MDR model at all; the MDR-7506 (1991, 40mm closed-back wired studio monitor, 63 ohm, folding) is Sony's pro studio line, not a WH-1000X flagship, not an INZONE gaming headset, and not the MDR-V6 (discontinued 2020, near-identical but a different model — not added). Black is the only colorway sold.",
    ),
    EvalProduct(
        key="sony-pulse-headset-white",
        brand="Sony",
        model="PlayStation Pulse Wireless Headset",
        variant="White (launch colorway; Midnight Black is the other launch colorway)",
        category="headphones",
        notes="PlayStation Direct $99.99 (PRE-ORDER — launches 2026-11-19; $99.99 recommended retail price per the official PlayStation Blog Oct 21 update; pre-orders via direct.playstation.com from Oct 29, 7am PT in the US; no Direct product-page URL surfaced, so the announcement URL is the quote URL. Best Buy, Walmart and Target pre-order listings at $99.99 are confirmed by IGN / The Shortcut, but no verbatim Best Buy product URL surfaced, so no second quote is recorded). Correction vs the 2026-10-31 candidate note: the $99 (pre-order) figure is the NEW PlayStation Pulse headset (2026, planar magnetic drivers, PlayStation Link + Bluetooth, up to 30 hours, White and Midnight Black), NOT the PULSE 3D (CFI-ZWH1, 2020, $99.99) — the PULSE 3D is the older base line and was not added. Identifiers PENDING: no hardware model number (CFI-...), retail MPN or UPC for the new Pulse has been published on any official or retailer page yet, so identifiers stay empty per the Adaptive Controller / DualSense / PULSE Elite precedent; re-check after the Nov 19 launch. Distinct from the set's PULSE Elite Midnight Black (1000044173, CFI-ZWH2, $149) and PULSE Explore Midnight Black (1000044170, CFI-ZWE1, $199) — the Pulse is the new base planar-magnetic headset line below the Elite, and from the PULSE 3D (CFI-ZWH1, different model). White is pinned as the first-listed launch colorway in Sony's announcement; Midnight Black is the other launch colorway. The Pulse Edge (ANC, detachable boom mic, early 2027, no price yet) is a different model — not added.",
    ),
    EvalProduct(
        key="sony-linkbuds-clip-black",
        brand="Sony",
        model="LinkBuds Clip",
        variant="Black (WF-LC900/B)",
        category="earbuds",
        notes="Best Buy $198.00 (Model WFLC900/B, SKU 12317215, JSON-LD InStock, page-verified; comp. value $228.00); Sweetwater $198.00 (feed row — suspected, $198 sale vs $228 list); BuyDig $198.00 (Part # WFLC900/B, In Stock, page-verified; list $229.99); Abt $198.00 (Model WFLC900B, comp. value $228, search-index read of the Greige page which lists the Black at $198; manufacturer rebate ends 11/08/2026); Sony direct SRP $229.99 (Greige page, electronics.sony.com — stale crawl, 270 days; same SRP across colors per the Jan 2026 announcement). Correction vs the 2026-10-31 candidate price: $229.99 is the launch SRP — the current US street price is $198. Identifiers PENDING: MPN WFLC900/B confirmed (Best Buy US Model + Abt + BuyDig + Sony AU agree; hardware model WF-LC900 / YY2999 per the Sony reference guide), but UPC 027242934054 is stated on the BuyDig spec table only — no second non-Amazon US source surfaced, so identifiers stay empty per the Adaptive Controller / DualSense / PULSE Elite precedent. The Greige UPC 027242934177 (BuyDig) is a different colorway and was not copied; the AU EAN 4548736173699 (Sony AU) is a different regional code and was not copied. Excluded: Datavision / Focus Camera bundle rows (with care program / case bundle), ListenUp Greige $198 and Best Buy Greige / Lavender / Green rows (different colorways), Best Buy Lavender $129.99 (a different colorway on a holiday deal — not the Black price). Distinct from the set's LinkBuds Fit Black (WFLS910N/B, UPC 027242929289) and LinkBuds Open Black (WFL910/B, UPC 027242928695) — the Clip (WF-LC900, 2026, clip-on open-ear, 10mm driver, IPX4, up to 37 hours total) is the distinct clip-on line. Black, Greige, Green and Lavender are the four colorways; only Black is pinned.",
    ),
    EvalProduct(
        key="nintendo-n64-controller",
        brand="Nintendo",
        model="Nintendo 64 Controller",
        variant="Gray, standard edition (HAC-043; Nintendo SKU 128577)",
        category="controllers",
        notes="Nintendo direct $54.99 (JSON-LD InStock, page-verified 2026-11-06; the only seller — Nintendo Store exclusive). Correction vs the 2026-10-31 candidate price: $49.99 was the 2021 launch price — the current Nintendo direct price is $54.99. Purchase requires a paid Nintendo Switch Online membership (free-trial holders excluded), limit four per Nintendo Account, ships to the US and Canada only. Identifiers PENDING: hardware model HAC-043 confirmed (Nintendo Support US: 'Nintendo 64 Controller (model No. HAC-043)') and Nintendo SKU 128577 confirmed (Nintendo US store page), but UPC 00045496894948 is stated on the Nintendo US store page only — no second US source surfaced, so identifiers stay empty per the Adaptive Controller / DualSense / PULSE Elite precedent. The revised HAC-043(-01) with a replaceable battery (Europe, early 2027) is a different hardware revision — not added. Distinct from the set's Joy-Con 2 pair, Joy-Con pair and Switch Pro Controller (HACAFSSKA, UPC 045496590161) — the N64 controller (2021, wireless, Bluetooth, built-in rumble, USB-C rechargeable, 5220 mAh) is the distinct retro NSO controller line; third-party N64-style pads (Retro Fighters Brawler64, 8BitDo 64, Retro-Bit Tribute) are different models and were not added. Gray is the only colorway sold.",
    ),
    EvalProduct(
        key="apple-studio-display-xdr-standard-tilt-height",
        brand="Apple",
        model="Studio Display XDR",
        variant="Standard glass, Tilt- and height-adjustable stand (MFEL4LL/A)",
        category="monitors",
        notes="Apple direct $3,299.00 (US buy page JSON-LD, search-index read 2026-11-06; stock not stated in the page text); Best Buy $3,299.99 (Model MFEL4LL/A, SKU 6505397, JSON-LD InStock, page-verified, sold by Best Buy); Abt $3,299.00 (Model MFEL4LL/A, JSON-LD InStock, page-verified, est. delivery Nov 10); Sam's Club $3,299.00 and Sweetwater $3,299.00 (feed rows — suspected, no identifier in the feed rows). Correction vs the 2026-10-31 candidate note: $3,299 is confirmed current — it is the standard-glass tilt-and-height config; the $2,899 figure is the standard-glass VESA config (MFEN4LL/A) and $3,599 / $3,199 are the nano-texture tilt-height / VESA configs. Identifiers PENDING: MPN MFEL4LL/A confirmed (Apple US + Best Buy US Model + Abt agree), but no UPC for MFEL4LL/A surfaced on any US retailer spec page checked — the B&H UPC 195950527650 belongs to the VESA config (MFEN4LL/A; the B&H MFEN page and the VESA + AppleCare+ kit page both list it), so it was not copied; the UK GTIN 195950527858 is the MFEP4B/A (different region) and was not copied — identifiers stay empty per the Adaptive Controller / DualSense / PULSE Elite precedent; re-check next refresh. Excluded: refurbished Apple $2,799 (refurbished, not new); NFM rows (bundles with 3-year AppleCare+); Melrose Mac $2,899 and SVA Campus Store $3,199 (VESA-config prices on tilt-height rows); nano-texture rows ($3,499–$3,599); non-US rows (Artifact Argentina $5,700, 961souq $3,000); MacExperience $6,998 (Pro Display XDR, different model). Distinct from the set's Studio Display 2026 (MFEX4LL/A, $1,599, non-XDR 60Hz) — the Studio Display XDR (27-inch 5K mini-LED, 120Hz, 2000 nits peak HDR, Thunderbolt 5, released March 11, 2026) is the separate XDR line; and from the discontinued Pro Display XDR (32-inch 6K, $4,999, discontinued March 3, 2026 — not added). Silver is the only finish sold.",
    ),
    EvalProduct(
        key="sony-mdr-m1",
        brand="Sony",
        model="MDR-M1",
        variant="Black, standard edition (MDRM1)",
        category="headphones",
        notes="Sony direct $249.99 (launch MSRP, page crawled 2024-10-22 — stale, stock not stated in the page text); B&H $268.00 (JSON-LD InStock, page-verified); Sweetwater $268.00 (Open Graph instock, page-verified); Guitar Center $268.00, Vintage King $269.99 and Focus Camera $268.00 (feed rows — suspected, no identifier in the feed rows). Correction vs the 2026-10-31 candidate price $269.99: confirmed current-ish — $268 at B&H and Sweetwater, $269.99 at Vintage King; $249.99 is the launch MSRP, not the current street price. Identifiers PENDING: MPN MDRM1 confirmed (Sony US + B&H + Sweetwater agree), but UPC 027242930612 is stated on the B&H US spec page only — the only other source stating it is manuals.plus, which mirrors the Amazon ASIN listing, and Amazon is not used for identifier corroboration, so identifiers stay empty per the Adaptive Controller / DualSense / PULSE Elite precedent; re-check next refresh. Excluded: MDR-M1ST $389.99 (Japan-domestic model, different model), 5-pack $1,002.99 bundle, WUQ / Newegg $426.99 (third-party seller row), MercadoLibre $219 (non-US marketplace), Walmart $268 feed row (marketplace ambiguity — seller not confirmed first-party), MDR-MV1 rows (different model), MDR-ZX110NC rows (different model). Distinct from the set's MDR-7506 (1991 closed-back, 63 ohm) — the MDR-M1 (2024, 40mm, 50 ohm, 216 g, 5Hz–80kHz, folding) is Sony's modern pro reference closed monitor line; and from the MDR-MV1 (open-back sibling, added in this same batch). Black is the only colorway sold.",
    ),
    EvalProduct(
        key="sony-mdr-mv1",
        brand="Sony",
        model="MDR-MV1",
        variant="Black, standard edition (MDRMV1)",
        category="headphones",
        notes="Sweetwater $418.00 (Open Graph instock, page-verified); Macy's $419.99, SoundPure $419.99, Unique Photo $418.00 and Impulse Cameras $419.99 (feed rows — suspected, no identifier in the feed rows). Correction vs the 2026-10-31 candidate price $339.99: that matches no US price — the MSRP is $419.99 (SoundGuys) and the current US street price is $418–$419.99; $399 was a launch-era figure in some reviews. The Sony direct US page returned 403 on 2026-11-06, so no direct quote is recorded. Identifiers PENDING: MPN MDRMV1 confirmed (Sony AU/NZ Product ID + Macy's + Sweetwater agree; EAN 4548736147836 is the AU/NZ regional code and was not copied), but UPC 027242926585 appears in an eBay listing only — no US retailer spec page surfaced, so identifiers stay empty per the Adaptive Controller / DualSense / PULSE Elite precedent; re-check next refresh. Excluded: Target $418 bundle (with hard shell case), Newegg 5-pack $1,002.99 bundle, Greentoe $386 ('make an offer' marketplace-style row), Voomisupply $928.42, Walmart $418 feed row (marketplace ambiguity), MDR-M1 rows (different model), 360 VME software $269 and the Mogami cable $204.95 (different products). Distinct from the set's MDR-7506 and MDR-M1 (added in this same batch) — the MDR-MV1 (2023, 40mm open-back, 24 ohm, 223 g, 5Hz–80kHz) is Sony's open-back reference monitor line for mixing, mastering and spatial audio. Black is the only colorway sold.",
    ),
    EvalProduct(
        key="keychron-b39-deep-black",
        brand="Keychron",
        model="B39",
        variant="96% Alice, Deep Black (B39-K9)",
        category="keyboards",
        notes="Keychron direct $54.99 (official store, Deep Black variant Available, page-verified 2026-11-06; the only seller — Keychron's own store only, so it holds a single quote, like the B40). Correction vs the 2026-10-31 candidate price $54.99: confirmed current at Keychron direct. Identifiers PENDING: SKU B39-K9 comes from the Keychron official store page only and no UPC/EAN for the B39 surfaced anywhere, so identifiers stay empty per the Adaptive Controller / DualSense precedent; re-check next refresh. Distinct from the set's B40 Deep Black (B40-K9, 75% Alice, $49.99) — the B39 (96% Alice with dedicated numpad, $54.99, 800 mAh, up to 330 hours in 2.4 GHz mode, quiet scissor switches, M1–M5 macro keys, tri-mode 2.4 GHz / Bluetooth 5.2 / USB-C) is the larger sibling, a different model; and from the set's K8 lines (K8-G1, K8 HE, K8 Ultra 8K) and Q1 — the B39 is Keychron's budget Alice-layout scissor-switch line. Deep Black is the only colorway sold.",
    ),
    EvalProduct(
        key="anker-maggo-2-pro-phantom-gray",
        brand="Anker",
        model="MagGo 2 Pro Magnetic Power Bank (10K, Qi2 25W, Active Cooling)",
        variant="Phantom Gray (A110R)",
        category="power-banks",
        notes="Anker direct $109.99 (JSON-LD InStock, page-verified 2026-11-06); Newegg $109.99 (feed row — suspected, no identifier in the feed row). Identifiers PENDING: MPN A110R confirmed (Anker US official page + reviews agree), but no UPC for A110R surfaced on any US retailer spec page or barcode source, so identifiers stay empty per the Adaptive Controller / DualSense / PULSE Elite precedent; re-check next refresh. Excluded: Member Exclusive page (same model/price, duplicate listing); Starlight Silver feed row (different color); MagGo 2 Pro + Nano 45W bundle kits $144.98/$149.98 and MagGo 2 Pro + Laptop Power Bank bundle $229.98 (bundles); MagGo Power Bank (10K) $135, MagGo Wireless Charging Station rows, 622/623 chargers (different models); refurbished 621 $42.99 (refurbished, not new). Distinct from the set's only other Anker entry, Prime Charger 100W (A2688, wall charger) — the MagGo 2 Pro is Anker's flagship magnetic power bank (Qi2.2 25W, 45W USB-C, SnapCool active cooling, smart display, fold-out stand); the first magnetic power bank in the set. Four colors sold (Starlight Silver, Polar Night Blue, Phantom Gray, Burgundy Red, per Android Headlines + the Anker page); Phantom Gray pinned — the page does not state which Shopify variant is Phantom Gray, so the color-to-variant mapping is recorded as unverified; price is color-independent ($109.99 for all colors in the feed).",
    ),
    EvalProduct(
        key="anker-prime-power-bank-26k-300w-black",
        brand="Anker",
        model="Prime Power Bank (26K, 300W)",
        variant="Black (A110A)",
        category="power-banks",
        notes="Anker direct $199.99 (sale — $30 off the $229.99 list; homepage shelf + '$30 OFF' banner, page-verified 2026-11-06; the product-page JSON-LD and the Meta feed both show the $229.99 list price); Best Buy $229.99 (Model A110A, SKU 11919239, page-verified 2026-11-06; feed row — suspected, no identifier in the feed row). Identifiers PENDING: MPN A110A confirmed (Anker US + Best Buy US agree), colour Black confirmed (Heavins IE lists A110AH11 Black — but its EAN 0194644239299 is the EU/IE regional code for the H11 variant and was not copied, per the MDR-MV1 EAN precedent), but no US UPC for A110A surfaced on any US retailer spec page, so identifiers stay empty per the Adaptive Controller / DualSense precedent; re-check next refresh. Excluded: Prime Power Bank (26K, 300W) with Charging Base $329.99 (bundle with the 150W charging base, different SKU B110A); CDW $229.99 feed row (title 'Anker Prime Power Bank - 2 X Usb-c, Usb - 300 Watt' does not name the 26K model); Prime 20K 220W / 27,650mAh 250W / 12,000mAh 130W / 9.6K 65W Fusion rows (different models); no Amazon rows used. Distinct from the set's MagGo 2 Pro (10K magnetic, added in this same batch) — the 26K is Anker's flagship laptop power bank (300W total, 140W single-port, 250W dual-port recharge, 26,250mAh, app control); the first high-capacity laptop power bank in the set.",
    ),
    EvalProduct(
        key="anker-desktop-usb-c-hub-10-in-1",
        brand="Anker",
        model="Desktop USB-C Hub",
        variant="10-in-1, Dual 4K (A210C)",
        category="hubs",
        notes="Anker direct $79.99 (sale — $20 off the $99.99 list; homepage shelf + Anker blog '$20 OFF, $79.99, Code: WSPDV2ONVYED'; the product-page JSON-LD and the Meta feed both show the $99.99 list price; JSON-LD InStock, page-verified 2026-11-06; the only seller in the feed — Anker's own store only, so it holds a single quote, like the B39). Identifiers PENDING: MPN A210C confirmed (Anker US official page), but the only UPC stating a code, 194644340506, comes from pickoryx, which mirrors the Amazon ASIN listing (B0H36FV12Q) — Amazon is not used for identifier corroboration, so identifiers stay empty per the MDR-M1 / Adaptive Controller precedent; re-check next refresh. Excluded: VALORANT Limited Edition $109.99 (same A210C base, different edition/price — not pinned); Anker 575 Docking Station $199.99, 13-port hub $149.99, 332/364/565 and other hubs (different models); Walmart/Target/Newegg generic hub rows (different models). Distinct from everything in the set — the first USB-C hub/dock in the set (10-in-1, HDMI 2.1 + DisplayPort 1.4, dual 2K@240Hz, smart display, magnetic base); no color claimed — the Anker page names no colorway (an Amazon-derived listing calls it Iron Gray, not corroborated).",
    ),
    EvalProduct(
        key="anker-prime-wireless-car-charger",
        brand="Anker",
        model="Prime Wireless Car Charger (MagGo, AirCool, Pad)",
        variant="MagGo, AirCool, Pad (A2933)",
        category="chargers",
        notes="Anker direct $89.99 (JSON-LD InStock, page-verified 2026-11-06); Target $89.99 (feed row — suspected, no identifier in the feed row; title 'Anker Prime Qi2 25W MagSafe Wireless Car Charger Mount, AirCool Phone Holder with Vent Clip, for iPhone 17-12 Series & More (Adapter Included)' matches the A2933 spec — Qi2 25W + AirCool + included 60W adapter). Identifiers PENDING: MPN A2933 confirmed (Anker US + manuals.plus agree), colour Matte Black per a Bangladesh listing only (not a US source), but no UPC for A2933 surfaced anywhere, so identifiers stay empty per the Adaptive Controller / DualSense precedent; re-check next refresh. Excluded: anker.com feed row $135 (stale/conflicting — the live page JSON-LD and the us.anker.com feed row both say $89.99); Target $69.99 'Anker Prime MagGo Wireless Car Charger with AirCool' (title does not establish Qi2 25W/A2933 — likely the older 15W MagGo car charger); K-Rauta $78.90 (Estonia, non-US); Nano Wireless Car Charger bundle $77.98 and Prime Wireless Charging Station rows (different products). Distinct from the set's MagGo 2 Pro (added in this same batch) — the car charger is the first car-mount charger in the set (Qi2 25W magnetic vent mount, TEC AirCool, locking vent clip, 60W car adapter included).",
    ),
    EvalProduct(
        key="anker-nano-charger-70w-3-ports-black-stone",
        brand="Anker",
        model="Nano Charger (70W, 3 Ports)",
        variant="Black Stone (B121A)",
        category="chargers",
        notes="Anker direct $39.99 (JSON-LD InStock, page-verified 2026-11-06); Newegg $39.99 (feed row — suspected, no identifier in the feed row, no color stated); Impulse Cameras $39.99 (feed row — suspected, no identifier in the feed row; names the pinned Black Stone colorway). Identifiers PENDING: MPN B121A confirmed (Anker US official page states Model Number B121A; Notebookcheck and Amazon listings call the same charger A121A — the Anker page takes precedence and A121A was not recorded as a separate identifier); UPC 194644241247 for Black is stated on Amazon listings only and Amazon is not used for identifier corroboration, so identifiers stay empty per the Adaptive Controller / DualSense precedent; re-check next refresh. Excluded: Best Buy White $34.99 (different colorway — white is cheaper than black at Best Buy, $34.99 vs $39.99); Walmart $39.99 feed row (marketplace ambiguity — seller not confirmed first-party); corexlb $45 (not_a_seller); Nano 70W + Nano Power Bank bundle $99.98 (bundle); Nano Power Strip $69.99, Zolo 70W, Nano Neo (different products). Distinct from the set's Prime Charger 100W (A2688) — the Nano 70W (B121A) is Anker's compact 3-port 70W GaN charger with cable included, four colors (green, pink, black, white per the Anker page); Black Stone pinned. Note: the bundle slug 'bundle-b121a111-a1638011' hints the black variant MPN may be B121A111 (mirroring A121D121 = White, confirmed by Best Buy Canada) — unverified, not recorded; check next refresh.",
    ),
    EvalProduct(
        key="jbl-flip-7-black",
        brand="JBL",
        model="Flip 7",
        variant="Black (JBLFLIP7BLKAM)",
        category="speakers",
        identifiers={"UPC": "050036407342", "MPN": "JBLFLIP7BLKAM"},
        identifier_sources={
            "UPC": "JBL/Harman Salsify syndication catalog + eBay listing "
            "187108565342 agree for JBLFLIP7BLKAM (manuals.plus/B&H data "
            "dump agrees; Amazon listings agree but Amazon is not used "
            "for identifier corroboration)",
            "MPN": "JBL/Harman Salsify syndication catalog + global.jbl.com "
            "Black page + Best Buy US Model (Blue sibling JBLFLIP7BLUAM) "
            "agree on the AM code",
        },
        status="verified",
        notes="JBL direct $129.95 (sale — $20 off the $149.95 list; "
        "product-page JSON-LD InStock, page-verified 2026-11-06; the "
        "Meta feed's jbl.com Black row also shows $129.95 against a "
        "$149.95 list); Target Black $129.99 (JSON-LD InStock, "
        "page-verified); Best Buy Blue $129.95 (comp. value $149.95 — "
        "a different colorway, not the Black price). The April 2025 "
        "launch price was $149.95 — the current JBL direct price is "
        "$129.95 on sale. Identifiers VERIFIED: UPC 050036407342 + "
        "MPN JBLFLIP7BLKAM (JBL/Harman Salsify syndication catalog + "
        "eBay listing 187108565342 agree for JBLFLIP7BLKAM; the "
        "manuals.plus/B&H data dump agrees; Amazon listings agree "
        "but Amazon is not used for identifier corroboration). Not "
        "copied: UPC 050036407250 on an eBay listing for MPN "
        "JBLFLIP7BLK (no AM suffix — a different variant); the JBL US "
        "page crawl shows Item# JBLFLIP7TBLUAM (an unexplained page "
        "artifact — the global.jbl.com Black page shows JBLFLIP7BLKAM, "
        "and Best Buy's Blue model is JBLFLIP7BLUAM, so the Black AM "
        "code stands). Excluded: Target feed row $114.99 (Red, "
        "A-1012443440 — a different colorway); Crutchfield $109.95 "
        "(stale crawl, 360 days old); Dell Camo/Purple/Red/Blue "
        "$149.95 feed rows (different colorways at list price); a "
        "Samsung-sold $114.99 feed row (not first-party JBL); "
        "crestline $851.76 (promotional-products bulk listing). "
        "Distinct from everything in the set — the first JBL entry "
        "and the first portable Bluetooth speaker in the set (35W, "
        "IP68 waterproof/dustproof/drop-proof, Bluetooth 5.4, "
        "Auracast, USB-C lossless, up to 16 hours with Playtime "
        "Boost, PushLock accessories, launched April 2025); the Flip "
        "6 is the previous generation and was not added. Multiple "
        "colorways sold (Black, Blue, White, Red, Purple, Squad, "
        "Camo); only Black is pinned.",
    ),
    EvalProduct(
        key="jbl-tour-one-m3-smart-tx-black",
        brand="JBL",
        model="Tour One M3 Smart Tx",
        variant="Smart Tx, Black (JBLTOM3AVIBLKAM)",
        category="headphones",
        notes="JBL direct $449.95 (Meta feed jbl.com Black row, "
        "brand_direct; the JBL US store lists the Smart Tx version at "
        "$449.95); Best Buy $449.95 (Model JBLTOM3AVIBLKAM, SKU "
        "6623867, page-verified 2026-11-06); Abt $449.95 (JSON-LD "
        "InStock, page-verified); PC Richard $449.95 (MPN "
        "JBLTOM3AVIBLKAM, JSON-LD InStock, page-verified); Sweetwater "
        "Blue $449.95 (a different colorway). Some April 2025 launch "
        "coverage quoted $399 — the current US list price is $449.95 "
        "at JBL direct, Abt, Best Buy, PC Richard and Sweetwater. "
        "The $199.95 sale: audiowords (checked 2026-11-01) says the "
        "Smart Tx was selling for $199.95 at JBL, and Slickdeals/Best "
        "Buy listed it at $199.95 about 8 days ago — but the Best Buy "
        "page now shows $449.95 and the JBL feed row shows $449.95, "
        "so the sale has ended; re-check next refresh (the Newegg "
        "Mocha feed row still shows $199.95 — a different colorway, "
        "suspected). Identifiers PENDING: MPN JBLTOM3AVIBLKAM "
        "confirmed (Abt + Best Buy US Model + PC Richard MPN + "
        "Crutchfield MFR# agree), but UPC 050036414029 is stated on "
        "snapklik + tanotis aggregator pages only — no US retailer "
        "spec page states it, so identifiers stay empty per the "
        "Adaptive Controller / DualSense / PULSE Elite precedent; "
        "re-check next refresh. Not copied: the Blue UPC 050036414098 "
        "and Latte UPC 050036414067 (Abt — different colorways); the "
        "global EAN 1200130025112 (regional code, per the MDR-MV1 EAN "
        "precedent). Excluded: Best Buy Mocha/Blue $472.45 feed rows "
        "(with case bundle — 'Smart Tx Wireless Headphones with "
        "Case'); the non-Tx Tour One M3 (JBLTOURONEM3BLKAM, "
        "headphones-only, no Smart Tx transmitter — a different "
        "product, sold outside the US; the US sells the Smart Tx "
        "bundle); the Tour One M2 (previous generation). Distinct "
        "from the set's Sony WH-1000XM5/XM6 and Bose QuietComfort "
        "Ultra — the Tour One M3 Smart Tx (2025, 40mm mica-dome "
        "drivers, True Adaptive ANC 2.0, LDAC, Auracast, USB-C "
        "lossless DAC, Spatial 360 with head tracking, up to 70 "
        "hours, Smart Tx touchscreen transmitter) is JBL's flagship "
        "over-ear ANC line; the first JBL headphones in the set. "
        "Black, Blue and Mocha (US: Latte) colorways sold; only "
        "Black is pinned.",
    ),
    EvalProduct(
        key="jbl-tour-pro-3-black",
        brand="JBL",
        model="Tour Pro 3",
        variant="Black (JBLTOURPRO3BLKAM)",
        category="earbuds",
        notes="JBL direct $329.95 (jbl.com category pages list the Tour "
        "Pro 3 at $329.95; the Meta feed's jbl.com Latte row is "
        "$329.95 brand_direct — price is color-independent: B&H "
        "Latte, Crutchfield Black, Abt Black and Audio Advice Black "
        "are all $329.95); B&H Latte $329.95 (In Stock, page-verified "
        "2026-11-06); Crutchfield Black $329.95 (JSON-LD InStock, "
        "page-verified; MFR# JBLTOURPRO3BLKAM); Abt Black $329.95 "
        "(JSON-LD InStock, page-verified); Audio Advice Black $329.95 "
        "(Available, page-verified). Identifiers PENDING: MPN "
        "JBLTOURPRO3BLKAM confirmed (Crutchfield MFR# + Abt + B&H "
        "Latte sibling JBLTOURPRO3LTTAM agree; JBL UK lists the "
        "non-AM JBLTOURPRO3BLK with EAN 1200130013836), but UPC "
        "050036402392 for Black is stated on Amazon listings only — "
        "Amazon is not used for identifier corroboration, so "
        "identifiers stay empty per the Adaptive Controller / "
        "DualSense precedent; re-check next refresh. Not copied: the "
        "Latte UPC 050036402415 (B&H — a different colorway). "
        "Excluded: the Meta feed's Abt $229.95 Black row — the live "
        "Abt page shows $329.95, so the $229.95 row is stale and was "
        "excluded (A2933 $135 precedent); Crutchfield's $229.95 "
        "'Save $100, ends 9/13' sale (ended); Best Buy $346.45 bundle "
        "rows (with gSport/weather-resistant case); the Charge 6 + "
        "Tour Pro 3 kit $476.91 (bundle); Greentoe $229.95/$329.95 "
        "(make-an-offer marketplace-style rows); icuracao $209.99 "
        "(non-US). Distinct from the set's Sony WF-1000XM5/XM6, "
        "AirPods Pro 3 and Galaxy Buds4 Pro — the Tour Pro 3 (2024, "
        "hybrid dual drivers, True Adaptive ANC 2.0, Spatial 360 "
        "with head tracking, Smart Charging Case with a 1.57-inch "
        "touchscreen that doubles as a Bluetooth audio transmitter, "
        "up to 44 hours total, wireless charging) is JBL's flagship "
        "true-wireless line; the first JBL earbuds in the set. Black "
        "and Latte colorways sold; only Black is pinned.",
    ),
    EvalProduct(
        key="jbl-bar-1300xmk2-black",
        brand="JBL",
        model="Bar 1300XMK2",
        variant="Black (JBLBAR1300XM2BLKAM)",
        category="soundbars",
        notes="JBL direct $1,699.95 (Meta feed jbl.com Black row, "
        "brand_direct; Harman press release June 9, 2025 lists "
        "$1,699.95); Best Buy $1,699.95 (Model JBLBAR1300XM2BLKAM, "
        "SKU 6643311, sold by Best Buy, page-verified 2026-11-06); "
        "Abt $1,699.95 (page-verified); Crutchfield $1,699.95, B&H "
        "$1,699.95 and Sweetwater $1,699.95 (feed rows — suspected, "
        "no identifier in the feed rows); Macy's $1,199.95 (feed row "
        "— suspected; the sale price vs $1,699.95 elsewhere, not "
        "page-verified). The US model is the Bar 1300XMK2 (12-inch "
        "subwoofer, 1570W max); the non-US Bar 1300MK2 (dual 8-inch "
        "subwoofer, 2470W) is a different regional variant and was "
        "not added — Best Buy lists the US bar as BAR1300MK2 with "
        "model JBLBAR1300XM2BLKAM. Identifiers PENDING: MPN "
        "JBLBAR1300XM2BLKAM confirmed (global.jbl.com Item# + Best "
        "Buy US Model + Abt + shopabunda agree), but UPC 050036414869 "
        "is stated on Amazon listings + an eBay refurbished listing "
        "+ Target Plus partner data only — no US retailer spec page "
        "states it, so identifiers stay empty per the Adaptive "
        "Controller / DualSense precedent; re-check next refresh. "
        "Not copied: the global EAN 1200130026843 (regional code, "
        "per the MDR-MV1 EAN precedent). Excluded: Best Buy $1,742.45 "
        "(with AudioQuest HDMI cable bundle); Newegg $1,499.90 (with "
        "2-year protection plan) and $1,514.99 (with Austere HDMI "
        "cable bundle); the jbl.com $1,690.94 bundle (bar + Austere "
        "HDMI cable); Belk $2,040 (outlier, $340 above list); "
        "Dolby.com $1,019.99 (the old Bar 1300X, 650W, 2022 — a "
        "different model); the Bar 1000MK2 $1,199 / 700MK2 $899 / "
        "500MK2 $649 / 300MK2 $449 (lower MK2 siblings, not added). "
        "Distinct from everything in the set — the first soundbar in "
        "the set (11.1.4 channels, detachable battery-powered "
        "wireless surround speakers that double as portable Bluetooth "
        "speakers, 12-inch wireless subwoofer, Dolby Atmos + DTS:X, "
        "MultiBeam 3.0, HDMI eARC with 4K Dolby Vision passthrough, "
        "AirPlay 2, launched October 2025). Black is the only "
        "colorway sold.",
    ),
    EvalProduct(
        key="jbl-partybox-stage-320-black",
        brand="JBL",
        model="PartyBox Stage 320",
        variant="Black (JBLPBSTAGE320AM)",
        category="speakers",
        notes="JBL direct $569.95 (product-page JSON-LD InStock, "
        "page-verified 2026-11-06; the page default Item# is "
        "JBLPBSTAGE320AM; the Meta feed's jbl.com White row is also "
        "$569.95, so direct pricing looks color-independent); Best "
        "Buy Black $629.95 (feed row — suspected, no identifier in "
        "the feed row); Target Black $629.99 (JSON-LD InStock, "
        "page-verified); Music & Arts $629.95 (feed row — suspected). "
        "The 2024 launch MSRP was $599.95/$599.99 (SoundGuys) — the "
        "current JBL direct price is $569.95 while Best Buy/Target "
        "hold $629.95/$629.99. Identifiers PENDING: MPN "
        "JBLPBSTAGE320AM confirmed as the US Black code (JBL US page "
        "Item# + Sharaf DG lists PARTYBOXSTAGE320AM as Black; the "
        "White code is JBLPBSTAGE320SWAM per shopabunda), but no UPC "
        "for the Black surfaced on any US manufacturer or retailer "
        "spec page, so identifiers stay empty per the Adaptive "
        "Controller / DualSense precedent; re-check next refresh. "
        "Excluded: RC Willey Black $499.95 (feed row — suspected; "
        "the low outlier vs $569.95–$629.99 elsewhere, not "
        "page-verified); the 'Stage 320 and The Works' bundle "
        "$739.90 (with Battery 400 + wireless mics, OutOfStock); "
        "Woot Grade A Refurbished $399.95 (refurbished, not new); "
        "B&H mic/PartyLight kits $729.90/$799.90 (bundles, "
        "discontinued); the PartyBox 330 (new 2026 successor — US "
        "price conflicting, $499.95 on the JBL US page per one source "
        "vs $630 per another, so it was not pinned this batch; "
        "revisit next sweep); the PartyBox 310 (previous generation, "
        "replaced by the 320). Distinct from the set's Flip 7 (added "
        "in this same batch) — the Stage 320 is JBL's wheeled party "
        "speaker line (240W, two 6.5-inch woofers + two 25mm "
        "tweeters, adaptive lightshow, IPX4, telescopic handle + "
        "wheels, replaceable BATTERY400, up to 18 hours, mic/guitar "
        "inputs, Auracast, launched 2024); the first party speaker "
        "in the set. Black and White colorways sold; only Black is "
        "pinned.",
    ),
    EvalProduct(
        key="razer-viper-v4-pro-black",
        brand="Razer",
        model="Viper V4 Pro",
        variant="Black (RZ01-05630100-R3U1)",
        category="mice",
        notes="Razer direct $159.99 (March 24, 2026 launch release: "
        "US$159.99 MSRP, available now at Razer.com; Windows Central: "
        "'retails for $159.99 and is available now, both directly "
        "from Razer's website as well as through digital retailers "
        "like Amazon and Best Buy'; the US product URL resolves to "
        "the Viper V4 Pro page — price-only, stock not confirmed in "
        "the page text, which returns only the 'more gear' "
        "carousel); Best Buy $159.99 (Model RZ01-05630100-R3U1, SKU "
        "6669259, sold by Best Buy, JSON-LD InStock, page-verified "
        "2026-11-06); NFM $156.99 (feed row — suspected). "
        "Identifiers PENDING: MPN RZ01-05630100-R3U1 confirmed "
        "(Best Buy US Model + Canada Computers MPN + ShopAbunda + "
        "Big Apple Buddy sourced from Best Buy agree), but no US "
        "UPC surfaced anywhere — the only barcode found is the EU "
        "EAN 8887910085134 for the R3G1 variant (Scan UK, Singular "
        "CY, startech24 datasheet), which was NOT copied across "
        "regions per the MDR-MV1 EAN precedent; re-check next "
        "refresh. Not copied: the White MPN RZ01-05630200-R3U1 "
        "(different colorway, 50 g vs 49 g). Excluded: the Ayoub "
        "$191 R3G1 row (non-US variant); the Lethal Aero Base Mod "
        "$14.99 (an accessory, not the mouse); DeathAdder V4 Pro "
        "and Basilisk V4 Pro rows (different models — the "
        "DeathAdder V4 Pro Black RZ01-05330100-R3U1 at $169.99 and "
        "the Basilisk V4 Pro Black RZ01-05670100-R3U1 at $169.99 "
        "stay list-only for later batches). Distinct from the set's "
        "Logitech G Pro X Superlight 2 / Superlight 2 DEX and the "
        "G502 X PLUS — the Viper V4 Pro (March 2026, 49 g, Focus "
        "Pro 50K Optical Sensor Gen-3, true 8,000 Hz wireless "
        "polling, HyperSpeed Wireless Gen-2, Gen-4 optical "
        "switches, up to 180 hours at 1,000 Hz) is Razer's current "
        "flagship symmetrical esports mouse and the first Razer "
        "entry in the set. Black and White colorways sold; only "
        "Black is pinned.",
    ),
    EvalProduct(
        key="razer-blackwidow-v4-pro-green-black",
        brand="Razer",
        model="BlackWidow V4 Pro",
        variant="Green switches, Black (RZ03-04680200-R3U1)",
        category="keyboards",
        notes="Razer direct $229.99 (Meta feed brand_direct row, URL "
        "carries RZ03-04680200-R3U1; $229.99 is the February 2023 "
        "launch MSRP); B&H $199.99 (Holiday Savings $50 off "
        "$249.99, In Stock, JSON-LD InStock, page-verified "
        "2026-11-06; the page states UPC 840272903315); Staples "
        "$267.93 (feed row for the exact MPN — suspected; above the "
        "$229.99 list, an outlier). Identifiers PENDING: MPN "
        "RZ03-04680200-R3U1 confirmed (B&H + Newegg + NeweggBusiness "
        "agree), but UPC 840272903315 is stated on the B&H page "
        "only — no second non-Amazon US source states it, so "
        "identifiers stay empty per the Adaptive Controller / "
        "DualSense precedent; re-check next refresh. Not copied: "
        "the Yellow-switch UPC 840272903339 (Amazon listing for "
        "RZ03-04681900-R3U1 — a different switch variant, and "
        "Amazon is not used for corroboration); the Orange-switch "
        "MPN RZ03-04683500-R3M1 (a non-US code on the Razer feed "
        "row); the EU Yellow code RZ03-04682200-R3F1. Excluded: "
        "the Best Buy White $199.99 sale row (different colorway, "
        "RZ03-04683600-R3U1); the gadgetlb $279 row (non-US); the "
        "BlackWidow V4 Pro 75% $299.99 (different model, "
        "RZ03-05130200-R3U1, list-only). Distinct from the set's "
        "Logitech MX / G915 X / PRO X TKL and Keychron boards — "
        "the BlackWidow V4 Pro (full-size wired, Green clicky "
        "switches, 8,000 Hz polling, Command Dial, 8 dedicated "
        "macro keys, doubleshot ABS keycaps, Chroma RGB, magnetic "
        "plush wrist rest) is Razer's flagship full-size keyboard "
        "and the first Razer keyboard in the set. Green, Yellow "
        "and Orange switches sold; only Green is pinned.",
    ),
    EvalProduct(
        key="razer-blackshark-v3-pro-black",
        brand="Razer",
        model="BlackShark V3 Pro",
        variant="Black, PC version (RZ04-05400100-R3U1)",
        category="headphones",
        notes="Razer direct $249.99 (Meta feed brand_direct row, URL "
        "carries RZ04-05400100-R3U1; Razer's US store price read "
        "2026-10-15 at $249.99 with Add to cart; the White, Xbox "
        "and PlayStation versions are the same price); Best Buy "
        "$249.99 (Model RZ04-05400100-R3U1, SKU 6632881, sold by "
        "Best Buy, search-index page read 2026-11-06); Electronic "
        "Express $249.99 (feed row — suspected). Identifiers "
        "PENDING: MPN RZ04-05400100-R3U1 confirmed (Best Buy US "
        "Model + manuals.plus + Amazon product info agree), but "
        "UPC 840272919484 is stated on Amazon listings only — "
        "Amazon is not used for identifier corroboration, so "
        "identifiers stay empty per the Adaptive Controller / "
        "DualSense precedent; re-check next refresh. Not copied: "
        "the White UPC (different colorway, RZ04-05400200-R3U1); "
        "the PlayStation Black code RZ04-05400500-R3G1 and the "
        "Xbox Black code RZ04-05400300-R3U1 (different platform "
        "variants at the same $249.99); the CS2 Edition code "
        "RZ04-05400800-R3M1 (GTIN 8887910061657, a different "
        "edition). Excluded: the Abt Xbox-variant row (different "
        "platform variant); the Sentinels team-store row (not a "
        "general retailer); the Esports Green / NiKo / CS2 edition "
        "rows (different editions). Distinct from the set's Sony "
        "WH-1000XM5/XM6, Bose QC Ultra 2 and JBL Tour One M3 — the "
        "BlackShark V3 Pro (July 2025, hybrid ANC, 50 mm TriForce "
        "Bio-Cellulose Gen-2 drivers, detachable HyperClear 12 mm "
        "full-band mic, HyperSpeed Wireless Gen-2, up to 70 hours, "
        "THX Spatial Audio, 367 g) is Razer's flagship esports "
        "headset and the first Razer headset in the set. The PC "
        "version in Black is pinned; the platform variants are "
        "different products.",
    ),
    EvalProduct(
        key="razer-wolverine-v3-pro-black",
        brand="Razer",
        model="Wolverine V3 Pro",
        variant="Black (RZ06-05200100-R3U1)",
        category="controllers",
        notes="Razer direct $199.99 (Meta feed brand_direct row, URL "
        "carries RZ06-05200100-R3U1; $199.99 is the August 2024 "
        "launch MSRP); Best Buy $169.99 (Model RZ06-05200100-R3U1, "
        "SKU 6594728, save $30 off comp. value $199.99, "
        "page-verified 2026-11-06); NFM $166.99 sale vs $199.99 "
        "list (feed row — suspected). Identifiers PENDING: MPN "
        "RZ06-05200100-R3U1 confirmed (Best Buy US Model + "
        "ShopAbunda + Eneba spec table agree), but no UPC surfaced "
        "on any US manufacturer or retailer spec page, so "
        "identifiers stay empty per the Adaptive Controller / "
        "DualSense precedent; re-check next refresh. Not copied: "
        "the White MPN RZ06-05200200-R3U1 (different colorway, "
        "Best Buy $191.99); the EU code RZ06-05200100-R3M1 "
        "(Overclockers UK — a different regional variant). "
        "Excluded: the FlexShopper $247.99 / $10 row (lease-to-own, "
        "not a straight price); the Staples White $213.60 row "
        "(different colorway); the Macy's Wolverine V3 Pro 8K PC "
        "row (a different, PC-only model, RZ06-05540100-R3U1, "
        "list-only); the Woot $109.99 White row (different "
        "colorway); the sigmatiendas $279.42 row (non-US). "
        "Distinct from the set's Xbox Elite Series 2 / Elite Core, "
        "Xbox Wireless Controller, DualSense / DualSense Edge and "
        "Switch Pro controllers — the Wolverine V3 Pro (August "
        "2024, Razer's first wireless Xbox controller, Hall Effect "
        "thumbsticks, 6 remappable buttons, Pro HyperTriggers, "
        "1,000 Hz PC Tournament Mode, ~20 hours) is Razer's "
        "flagship Xbox/PC controller and the first Razer controller "
        "in the set. Black and White colorways sold; only Black is "
        "pinned.",
    ),
    EvalProduct(
        key="razer-kraken-v4-pro-black",
        brand="Razer",
        model="Kraken V4 Pro",
        variant="Black (RZ04-05160100-R3U1)",
        category="headphones",
        notes="Razer direct $399.99 (Meta feed brand_direct row, URL "
        "carries RZ04-05160100-R3U1; $399.99 is the September 2024 "
        "launch MSRP); Best Buy $299.99 (Model RZ04-05160100-R3U1, "
        "SKU 6589878, comp. value $399.99, search-index page read "
        "2026-11-06); Beach Camera $299.00 (feed row — suspected; "
        "the same $299.00 row appears twice in the feed). "
        "Identifiers PENDING: MPN RZ04-05160100-R3U1 confirmed "
        "(Best Buy US Model + manuals.plus agree), but no US UPC "
        "surfaced — PBTech lists UPC 840272909980 against the "
        "R3M1 variant and the EU EAN is 8887910060094 (itworkup, "
        "trippodo), so neither code was carried across regions per "
        "the MDR-MV1 EAN precedent; re-check next refresh. Not "
        "copied: the Kraken V4 (non-Pro) UPC 840272910054 (a "
        "different model, RZ04-05170100-R3U1). Excluded: the "
        "Kraken V4 Pro + Base Station V2 Chroma bundle $469.98 "
        "(bundle); the Kraken V4 $179.99 and CDW Kraken V4 $205.99 "
        "rows (the non-Pro model); the Newegg Evangelion combo "
        "$1,149.99 (bundle). Distinct from the set's BlackShark V3 "
        "Pro (added in this same batch) — the Kraken V4 Pro "
        "(September 2024, Sensa HD Haptics, OLED Control Hub, 40 "
        "mm TriForce Bio-Cellulose drivers, 4 connectivity modes, "
        "9-zone Chroma RGB, retractable mic, up to 50 hours) is "
        "Razer's flagship lifestyle/haptic headset; the BlackShark "
        "is the esports line. Black is the only colorway sold.",
    ),
    EvalProduct(
        key="corsair-m65-rgb-ultra-black",
        brand="Corsair",
        model="M65 RGB Ultra",
        variant="Black, wired (CH-9309411-NA2)",
        category="mice",
        notes="Corsair direct $59.99 (US product page, $59.99 InStock, "
        "page-verified 2026-11-06; Meta feed brand_direct rows agree "
        "at $59.99); Micro Center $59.99 (feed authorized_retailer "
        "row, page-verified $59.99 InStock, JSON-LD, 2026-11-06; the "
        "feed row states Mfr Part # CH-9309411-NA2 and UPC "
        "840006657613); CDW $84.99 (feed row — suspected; above the "
        "$59.99 list, not page-verified). Identifiers PENDING: MPN "
        "CH-9309411-NA2 confirmed (Corsair US SKU + Micro Center "
        "feed row + ShopAbunda spec table agree; ShopAbunda also "
        "ties the SKU to Black), but UPC 840006657613 is stated on "
        "the Micro Center feed row only — no second non-Amazon US "
        "source states it, so identifiers stay empty per the "
        "Adaptive Controller / DualSense precedent; re-check next "
        "refresh. Not copied: the original CH-9309411-NA SKU (the "
        "US page shows $69.99 Discontinued — a superseded revision "
        "of the same mouse); the M65 RGB Ultra Wireless (CH-9319511, "
        "$129.99, a different connectivity variant); the M65 RGB "
        "Elite and M65 Pro RGB (different, older models). Excluded: "
        "the FlexShopper $3/$6/$7 rows (lease-to-own marketplace, "
        "not straight prices); the $469.97 mouse + headset + "
        "keyboard bundle. Distinct from the set's Logitech and "
        "Razer mice — the M65 RGB Ultra (2022, tunable weight "
        "97–115 g, 26,000 DPI MARKSMAN sensor, optical switches, "
        "QUICKSTRIKE buttons, AXON hyper-processing, aluminum "
        "frame) is Corsair's flagship wired FPS mouse and the first "
        "Corsair entry in the set. Black is pinned; the wireless "
        "version is a different SKU.",
    ),
    EvalProduct(
        key="corsair-k65-plus-wireless-midnight-grey",
        brand="Corsair",
        model="K65 Plus Wireless",
        variant="Midnight Grey, MLX Red linear (CH-91D401L-NA)",
        category="keyboards",
        notes="Corsair direct $159.99 (US product page, $159.99 InStock, "
        "page-verified 2026-11-06; MLX Red linear switches, NA "
        "layout, up to 266 hours with LEDs off; Meta feed "
        "brand_direct row agrees at $159.99); Best Buy $159.99 "
        "(Model CH-91D401L-NA, SKU 6572502, Black/Gray, "
        "search-index page read 2026-11-06). A stale crawl showed "
        "$129.99 InStock 4 days ago and a second crawl $159.99 "
        "OutOfStock — the live page read today says $159.99 "
        "InStock and Best Buy agrees at $159.99, so $159.99 is "
        "recorded and the $129.99 is treated as a lapsed sale, not "
        "the current price. Identifiers PENDING: MPN CH-91D401L-NA "
        "confirmed (Corsair US SKU + Best Buy US Model agree), but "
        "no UPC surfaced on any US manufacturer or retailer spec "
        "page, so identifiers stay empty per the Adaptive "
        "Controller / DualSense precedent; re-check next refresh. "
        "Not copied: the Tactile variant CH-91D441F-NA ($129.99, "
        "different switches); the licensed editions (Call of Duty: "
        "Black Ops 7 $129.99, Witcher 3 $169.99, Cyberpunk "
        "Edgerunners 2 $169.99, Cyberpunk 2077 Arasaka White "
        "$169.99 — different SKUs); the Frost White / Glacier Blue "
        "Mac-and-PC editions (different colorways); the K65 Plus "
        "(wired, $179.99) and the Revival Series $67.99 "
        "(refurbished). Excluded: the Revival/refurbished rows. "
        "Distinct from the set's Logitech, Keychron and Razer "
        "boards — the K65 Plus Wireless (2024, 75% hot-swappable, "
        "pre-lubed MLX Red linear switches, 2.4 GHz + Bluetooth + "
        "wired, 1,000 Hz) is Corsair's current 75% wireless "
        "keyboard and the first Corsair keyboard in the set. "
        "Corsair's own edition list calls the base colorway "
        "'Original (Midnight Grey)'; Best Buy lists it as "
        "Black/Gray. Only Midnight Grey / MLX Red is pinned.",
    ),
    EvalProduct(
        key="corsair-virtuoso-max-wireless-carbon",
        brand="Corsair",
        model="Virtuoso Max Wireless",
        variant="Carbon, Black (CA-9011372-WW)",
        category="headphones",
        notes="Corsair direct $249.99 (US product page, $249.99 InStock, "
        "page-verified 2026-11-06; Meta feed brand_direct rows "
        "agree at $249.99); Best Buy $249.99 (Model CA-9011372-WW, "
        "SKU 6594136, Carbon, Holiday Deal, save $50 off comp. "
        "value $299.99, page-verified 2026-11-06). The $249.99 is a "
        "holiday sale price against the $299.99 list (a stale "
        "checkout.corsair.com feed row still shows $299.99) and "
        "should be re-checked after the sale ends (the Early Black "
        "Friday event ends Nov 8). Identifiers PENDING: MPN "
        "CA-9011372-WW confirmed (Corsair US SKU + Best Buy US "
        "Model + manuals.plus agree), but UPC 840440484615 is "
        "stated only by manuals.plus (reproducing the manual's "
        "spec table), an eBay listing and Amazon — no retailer or "
        "manufacturer listing states it, and the Best Buy page text "
        "does not carry it, so identifiers stay empty per the "
        "Adaptive Controller / DualSense precedent; re-check next "
        "refresh. Not copied: the Silver UPC (EAN 0840440484622, "
        "CA-9011373-WW, a different colorway); the Xbox version "
        "CA-9011374-WW (EAN 0840440484639, a different platform "
        "variant at the same $249.99). Excluded: the Virtuoso RGB "
        "Wireless XT $199.99 and Virtuoso RGB Wireless $199.99 "
        "(previous-generation lines); the Revival Series $147.99 "
        "(refurbished); the ShopAbunda $229.99 row (Amazon-"
        "fulfilled). Distinct from the set's Sony, Bose, JBL and "
        "Razer headsets — the Virtuoso Max (2024, 50 mm graphene "
        "drivers, Dolby Atmos, ANC + transparency, SoundID, "
        "simultaneous 2.4 GHz + Bluetooth, up to 60 hours, "
        "detachable broadcast mic) is Corsair's flagship wireless "
        "headset and the first Corsair headset in the set. Carbon "
        "is pinned; Silver is the same price but a different SKU.",
    ),
    EvalProduct(
        key="corsair-frame-4000d-rs-argb-black",
        brand="Corsair",
        model="FRAME 4000D RS ARGB",
        variant="Black (CC-9011296-WW)",
        category="pc-cases",
        notes="Corsair direct $119.99 (US product page, $119.99 InStock, "
        "page-verified 2026-11-06; Meta feed brand_direct rows "
        "agree at $119.99); Newegg $114.99 (feed authorized_"
        "retailer row — suspected; the feed title reads 'Non-LED' "
        "while the model is RS ARGB, and the Newegg page text shows "
        "no price or MPN, so the row may belong to the non-ARGB "
        "FRAME 4000D RS instead — not page-verified). Identifiers "
        "PENDING: MPN CC-9011296-WW confirmed (Corsair US SKU + "
        "custompcgaming, mixed-news and Toppreise spec tables agree "
        "it is the Black RS ARGB case), but UPC 840440487715 is "
        "stated on Amazon.in only — Amazon is not used for "
        "identifier corroboration, so identifiers stay empty per "
        "the Adaptive Controller / DualSense precedent; re-check "
        "next refresh. Not copied: the White RS ARGB (CC-9011297-"
        "WW, $124.99, a different colorway); the fanless FRAME "
        "4000D ($104.99) and FRAME 4000D RS non-ARGB (CC-9011312-"
        "WW, $114.99 — a different fan configuration); the FRAME "
        "4000D LCD RS ARGB ($399.99, a different model with a "
        "pre-installed LCD). Excluded: the older iCUE 4000D RGB "
        "Airflow (Discontinued on corsair.com); the FRAME 4000D RS "
        "ARGB All-in-One bundles ($399.96/$484.96). Distinct from "
        "everything in the set — the FRAME 4000D RS ARGB (2025, "
        "fully modular mid-tower, 3x RS120 ARGB fans, InfiniRail "
        "mounting, dual 360 mm radiators, reverse-connector "
        "motherboard support, GPU anti-sag arm) is Corsair's "
        "current modular mid-tower case and the first PC case in "
        "the set. Black is pinned.",
    ),
    EvalProduct(
        key="corsair-titan-ii-360-rx-rgb-black",
        brand="Corsair",
        model="iCUE LINK Titan II 360 RX RGB",
        variant="Black (CW-9061037-WW)",
        category="cpu-coolers",
        notes="Corsair direct $179.99 (US product page, $179.99 InStock, "
        "page-verified 2026-11-06); Best Buy $179.99 (Model "
        "CW-9061037-WW, SKU 6683807, Black, sold by Best Buy, Add "
        "to cart, JSON-LD InStock, page-verified 2026-11-06 — the "
        "page's 'About this product' block wrongly describes the "
        "Titan II Ultra 360 LX LCD, a Best Buy copy error; the "
        "Model, SKU, color and price are for this cooler); Newegg "
        "$179.99 (feed authorized_retailer row — suspected; no "
        "identifier in the feed row, not page-verified). "
        "Identifiers PENDING: MPN CW-9061037-WW confirmed (Corsair "
        "US SKU + Best Buy US Model + Newegg + Scan UK agree), but "
        "GTIN 840440419464 is stated on the Scan UK page only — no "
        "second, US source states it, so identifiers stay empty "
        "per the Adaptive Controller / DualSense precedent; "
        "re-check next refresh. Not copied: the White GTIN "
        "840440419471 (CW-9061038-WW, a different colorway, "
        "currently OutOfStock on corsair.com); the Titan II 360 RX "
        "LCD ($239.99, a different model with a 5-inch LCD); the "
        "previous-generation Titan 360 RX RGB (CW-9061018-WW, "
        "$199.99, OutOfStock) and Titan 360 RX LCD ($219.99). "
        "Excluded: the FlexShopper $11 row (lease-to-own "
        "marketplace); the Titan 360 RX LCD + fan bundles ($309.97–"
        "$414.97); the iCUE H150i RGB Pro XT / Elite (Discontinued "
        "on corsair.com). Distinct from everything in the set — the "
        "Titan II 360 RX RGB (2026, FlowDrive 2 pump, unified "
        "RX360 II RGB fan frame, 360 mm radiator, iCUE LINK System "
        "Hub included, 6-year warranty) is Corsair's current "
        "flagship 360 mm AIO and the first CPU cooler in the set. "
        "Black is pinned.",
    ),
    EvalProduct(
        key="dell-32-plus-4k-monitor-s3225qs",
        brand="Dell",
        model="32 Plus 4K Monitor S3225QS",
        variant="Ash White (F06FR)",
        category="monitors",
        identifiers={"UPC": "884116485131", "MPN": "F06FR"},
        identifier_sources={
            "UPC": "Icecat datasheet for DELL-S3225QS (EAN "
            "5397184962374 / GTIN 0884116485131) + eBay US product "
            "catalog (GTIN 0884116485131, ePID 21080788835) agree; "
            "Amazon US also states 884116485131 but is never a "
            "corroborating source"
        },
        status="verified",
        notes="Dell direct $329.99 (sale vs $369.99 estimated value, "
        "Dell US page via search-index reads 2026-10-23/26, "
        "topsave + Windows Central; the Meta feed brand_direct row "
        "still shows the $369.99 list); Best Buy $379.99 (Model "
        "S3225QS, SKU 6619489, feed authorized_retailer row — "
        "suspected, not page-verified); Micro Center $399.99 (feed "
        "authorized_retailer row — suspected, not page-verified). "
        "Dell US page confirms Manufacturer Part Number F06FR, "
        "Ash White, 31.5-inch 4K VA 120 Hz, dual 5 W speakers. "
        "The regional MPN differs (Ireland MX17X) and was not "
        "used. Distinct from everything in the set — the S3225QS "
        "(2025, 4K 120 Hz VA, FreeSync Premium, 99% sRGB, 95% "
        "DCI-P3, built-in speakers) is Dell's current mainstream "
        "32-inch 4K monitor and the first Dell monitor in the set. "
        "Re-check the $329.99 sale price after the Early Black "
        "Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="alienware-27-qd-oled-aw2726dm",
        brand="Alienware",
        model="27 240Hz QD-OLED Gaming Monitor AW2726DM",
        variant="Black (JW05F)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="Dell direct $319.99 (sale vs $349.99 estimated value, "
        "mixed-news 2026-10-30, 'the US listing was accepting "
        "orders when checked'; Windows Central 2026-10-26 agrees "
        "at $319.99); Best Buy $349.99 (Model AW2726DM, SKU "
        "6670439, search-index JSON-LD read); Dell $349.99 (Meta "
        "feed brand_direct row — the list price). Dell US page "
        "confirms Manufacturer Part Number JW05F, Black, 26.5-inch "
        "viewable QD-OLED 2560x1440 240 Hz, 0.03 ms, FreeSync "
        "Premium. Identifiers PENDING: MPN JW05F confirmed (Dell "
        "US + CA + AU pages agree; the UK MPN N0XJ0 is regional "
        "and was not used), but no US UPC surfaced — the only code "
        "found is EAN 5397321030553 on a single Icecat datasheet "
        "(EU), so identifiers stay empty per the DualSense "
        "precedent; re-check next refresh. Not copied: the AW2724DM "
        "(different, older 180 Hz model); the AW2726DL 280 Hz IPS "
        "($229.99, different panel); the AW3226DM 32-inch ($299.99, "
        "different size). Distinct from everything in the set — "
        "the AW2726DM (April 2026, the cheapest QD-OLED gaming "
        "monitor on the market at launch, 3-year burn-in warranty) "
        "is Alienware's current budget QD-OLED monitor and the "
        "first Alienware monitor in the set. Re-check the $319.99 "
        "sale price after the Early Black Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="alienware-pro-wireless-gaming-mouse-dark-side-of-the-moon",
        brand="Alienware",
        model="Pro Wireless Gaming Mouse",
        variant="Dark Side of the Moon (PRO-MS-G-DEAM)",
        category="mice",
        identifiers={"UPC": "884116464914", "MPN": "PRO-MS-G-DEAM"},
        identifier_sources={
            "UPC": "Icecat datasheet for PRO-MS-G-DEAM (EAN "
            "5397184877548 / GTIN 0884116464914, product color "
            "Black, multiple locale PDFs of the same datasheet) + "
            "axitech.be Black listing (545-BBFP PRO-MS-G-DEAM, "
            "EANs 5397184877548 0884116464914) agree"
        },
        status="verified",
        notes="Dell direct $129.99 (sale vs $149.99 list, Dell US "
        "Dark Side of the Moon category page, Offer ID 584RN, "
        "Add to Cart, page-verified 2026-11-06; 4.5 stars, 501 "
        "reviews); Newegg $160.99 (feed authorized_retailer row — "
        "suspected; above list, color unstated, not page-verified). "
        "Dell MPN 2021Y / Dell part 570-BBGJ is the Dell-side code "
        "for the Dark Side mouse (Ubuy ties 2021Y to Dark Side of "
        "the Moon; Dell's own accessory listing ties 2021Y to the "
        "Pro Mouse). Not copied: the Lunar Light UPC 884116464945 "
        "(PRO-MS-W-DEAM, 545-BBFN, a different colorway); the "
        "AW720M Tri-Mode ($79.99) and AW620M ($86.99 sale) — "
        "different, cheaper Alienware mice. Excluded: the "
        "FlexShopper $136.99 row (lease-to-own marketplace). "
        "Distinct from the set's Logitech, Razer and Corsair mice — "
        "the Pro Wireless Mouse (Jan 2024, 4KHz wireless / 8KHz "
        "wired, <60 g, 26,000 DPI, magnetic-force keyplates, "
        "designed with 100+ esports athletes) is Alienware's "
        "flagship pro mouse and the first Alienware mouse in the "
        "set. Re-check the $129.99 sale price after the Early "
        "Black Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="alienware-pro-wireless-gaming-keyboard-dark-side-of-the-moon",
        brand="Alienware",
        model="Pro Wireless Gaming Keyboard",
        variant="Dark Side of the Moon (WR47C)",
        category="keyboards",
        identifiers={},
        status="pending",
        notes="Dell direct $174.99 (sale vs $199.99 list, Dell US "
        "Dark Side of the Moon category page, Offer ID K6YT7, Add "
        "to Cart, page-verified 2026-11-06; 4.6 stars, 448 reviews; "
        "the Dell US product page 580-BBMZ agrees at $174.99 "
        "InStock); Newegg $294.99 (feed authorized_retailer row — "
        "suspected; above list, color unstated, not page-verified). "
        "The Meta feed brand_direct row still shows the $199.99 "
        "list. MPN WR47C confirmed (Dell US page, Dell part "
        "580-BBMZ); the color mapping is by elimination — the "
        "other variant X3V4D is Lunar Light (Ubuy + ShopAbunda + "
        "Icecat PRO-KB-W-WW), so WR47C is Dark Side of the Moon. "
        "Identifiers PENDING: the only UPC found, 884116464853, "
        "belongs to the White/Lunar Light keyboard (Icecat "
        "datasheet PRO-KB-W-WW + Ubuy X3V4D agree) and was not "
        "carried across colorways; no Dark Side UPC surfaced, so "
        "identifiers stay empty per the DualSense precedent; "
        "re-check next refresh. Not copied: the AW920K Tri-Mode "
        "($159.99), AW510K Low Profile ($129.99) and AW420K TKL "
        "($99.99) — different Alienware keyboards. Distinct from "
        "the set's Logitech, Keychron, Razer and Corsair boards — "
        "the Pro Wireless Keyboard (Jan 2024, 75%, hot-swappable "
        "linear switches, tri-mode, up to 798 hours) is Alienware's "
        "flagship pro keyboard and the first Alienware keyboard in "
        "the set. Re-check the $174.99 sale price after the Early "
        "Black Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="alienware-pro-wireless-gaming-headset-dark-side-of-the-moon",
        brand="Alienware",
        model="Pro Wireless Gaming Headset",
        variant="Dark Side of the Moon",
        category="headphones",
        identifiers={},
        status="pending",
        notes="Dell direct $174.99 (sale vs $199.99 list, Dell US "
        "search-index read, Offer ID 9K2M1; techaeris Black Friday "
        "hub 2026-11-05 agrees at $174.99); Best Buy $199.99 "
        "(Dark Side of the Moon, Model BBY-AWProH-D, SKU 6605023, "
        "save $30 off comp. value $229.99, search-index page read). "
        "The Meta feed today shows $229.99 list rows for both "
        "merchants and a $199.99 Dell row (N6YJD, Dark Side slug) — "
        "the feed lags the sale, so the page reads win per the "
        "Quill precedent; re-check after the Early Black Friday "
        "event ends Nov 8. Identifiers PENDING: the only UPC "
        "candidate, 884116469728, is stated on manuals.plus alone "
        "(reproducing the manual's spec table for ASIN B0DHWH425M, "
        "color unattributed), while Amazon's Lunar Light listing "
        "states 884116469759 — two colorways, two codes, neither "
        "corroborated by a second non-Amazon source, so "
        "identifiers stay empty per the DualSense precedent; "
        "re-check next refresh. Not copied: the Lunar Light UPC "
        "884116469759; the AW725H Tri-Mode ($149.99) and AW920H "
        "($109.99) — different Alienware headsets. Distinct from "
        "the set's Sony, Bose, JBL, Razer and Corsair headsets — "
        "the Pro Wireless Headset (2024, 50 mm graphene drivers, "
        "hybrid ANC, 75-hour battery, 15-minute fast charge, "
        "detachable boom mic) is Alienware's flagship pro headset "
        "and the first Alienware headset in the set.",
    ),
]


def get_product(key: str) -> EvalProduct:
    for product in EVAL_SET:
        if product.key == key:
            return product
    raise KeyError(f"unknown eval model key: {key}")
