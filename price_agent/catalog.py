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
                variant="Black, 16GB (B0CFPJYX7P)",
                category="e-readers",
                identifiers={"UPC": "840268989538", "MPN": "B0CFPJYX7P"},
                identifier_sources={
                    "UPC": "NFM listing (Model B0CFPJYX7P, UPC "
                    "840268989538, SKU 67502252, $196.99) + "
                    "CamelCamelCamel product page for B0CFPJYX7P "
                    "(ASIN B0CFPJYX7P, UPC 840268989538) agree",
                    "MPN": "B0CFPJYX7P is the US amazon.com code: "
                    "confirmed by Best Buy US (Model B0CFPJYX7P, "
                    "$199.99), Dell US, TrustedReviews, "
                    "pricehistory.app, NFM and CamelCamelCamel. "
                    "Old pin B0CFPL6CFY / UPC 840268942847 was the "
                    "non-US code (PBTech NZ/AU single source); "
                    "re-pinned to the US code 2026-11-07 on user "
                    "confirmation (DECISIONS 062)."
                },
                notes="Update 2026-10-31: amazon.com refused AI-agent "
                "access (Conditions of Use wall) during the small- "
                "brands sweep (BUILD_LOG 025); official currency "
                "unverified. Entry unchanged — neither confirmed nor "
                "removed on this basis; needs live-browser takeover or "
                "a retailer currency check. Update 2026-11-07: "
                "re-pinned to the US code B0CFPJYX7P on user "
                "confirmation; the old non-US pin is retired, never "
                "reused.",
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
                identifiers={"UPC": "195951080291", "MPN": "MHWT4LL/A"},
                identifier_sources={
                    "UPC": "B&H Photo + Adorama + Micro Center listings "
                    "agree on 195951080291 for MHWT4LL/A (2026-11-07 "
                    "check; B&H $1,999.00, Adorama $1,999.00, Micro "
                    "Center $1,999.99). Best Buy (SKU 6565882) confirms "
                    "the model and price but publishes no UPC."
                },
                notes="Current generation announced 2026-10-27; in stock from launch day 2026-11-06 (Apple + Best Buy, $1,999). "
                "Part number MHWT4LL/A confirmed by "
                "iClarified order number + Best Buy pre-order page "
                "(SKU 6565882, $1,999). UPC verified 2026-11-07 "
                "(three retailers agree) and upgraded to verified on "
                "user confirmation (DECISIONS 062). User confirmed 2026-10-31 to track "
                "the M6 base over the in-stock M5 24GB/1TB (MDE34LL/A).",
                status="verified"),
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
        variant="825GB, White, all-digital (CFI-2100 model group)",
        category="consoles",
        identifiers={"UPC": "711719021483", "MPN": "1000049898"},
        identifier_sources={
            "UPC": "UPC 711719541035 returned to pending 2026-11-08 "
            "(DECISIONS 067): the code points to the 2020 launch "
            "825GB, not the Slim — GameStop's launch Digital page FAQ "
            "says 825GB, ©2020; the launch disc UPC 711719541028 "
            "pairs with CFI-1015A, so 711719541035 is its digital "
            "sequential number; Notebookcheck/GameLuster confirm "
            "CFI-1015A/B are 2020 launch 825GB. No clean source ties "
            "it to CFI-2015 (GameStop Slim Digital 1TB: UPC "
            "711719573371, CFI-2000 group; eBay CFI-2015: UPC "
            "711719548539). The currently sold 825GB Slim is the "
            "CFI-2100 group: Abt Model 1000049898 page says "
            "'(CFI-2100 group – slim)', 825GB, $599.99; Cowtown and "
            "ShopCGX agree; Best Buy same model/SKU 6646420 $599.99. "
            "Counter-evidence: Walmart's same 825GB Slim page lists "
            "Model CFI-2015, but that page is marked unverified. "
            "CFI-2100's real UPC is still unknown; no Sony official "
            "UPC-to-model page was found. Resolved 2026-11-10: Best Buy "
            "spec page (SKU 6646420, live-browser verified) shows UPC "
            "711719021483 and Model Number 1000049898 for this 825GB Slim "
            "Digital, $599.99, sold by Best Buy; 711719541035 remains the "
            "2020 launch code, not this model."
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
        variant="Neon Blue/Neon Red set (HADSKABAH; SKU 117972)",
        category="consoles",
        identifiers={"UPC": "045496883775", "MPN": "HADSKABAH"},
        identifier_sources={
            "UPC": "Nintendo US official store page itself (SKU 117972, "
            "UPC 00045496883775, $339.99 InStock) + Amazon B0BFJWCYTL "
            "(Model HADSKABAH, UPC 045496883775) + Abt (HADSKABAH, "
            "UPC 045496883775) agree. MPN corrected 2026-11-07 from "
            "HADSKABAA to HADSKABAH (DECISIONS 065): the UPC belongs "
            "to HADSKABAH per Abt, Amazon and Best Buy; the older "
            "HADSKABAA barcode 045496882174 (ASIN B07VGRJDFY, 2019 "
            "red-box listing) is a different revision and was not pinned."
        },
        notes="Nintendo direct $339.99 (JSON-LD InStock); NFM $339.99; "
        "Best Buy $334.00 (Model HADSKABAH, SKU 10951790, "
        "search-index read, below MSRP). MPN corrected 2026-11-07 "
        "(HADSKABAA -> HADSKABAH): HADSKABAA is the 2017 original "
        "revision with barcode 045496882174, a different SKU; the "
        "current neon set is HADSKABAH. Distinct from "
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
        "MHWT4LL/A, $1,999, UPC 195951080291 verified 2026-11-07) and from the Liquid Retina "
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
        identifiers={"UPC": "027242930339", "MPN": "WFC510/B"},
        identifier_sources={
            "UPC": "B&H Photo spec page (UPC 027242930339, $58.00, "
            "In Stock) + Abt listing (Model WFC510/B, UPC "
            "027242930339, $58.00) agree, 2026-11-07"
        },
        notes="Best Buy $59.99 (Model WFC510/B, SKU 6594425, JSON-LD "
        "InStock, page-verified 2026-11-06); B&H Photo $58.00 (In "
        "Stock, was $68.00, page-verified); Abt $58.00 (feed row; "
        "manufacturer rebate ends 11/08/2026, comp. value $68); "
        "Electronic Express $58.00 and Focus Camera $58.00 (feed rows, "
        "Black); Fred Meyer $69.99 (JSON-LD InStock, page-verified — "
        "the list price). MPN WFC510/B confirmed (Best Buy US Model + "
        "B&H + Sony AU Model WFC510B agree). UPC verified 2026-11-07 "
        "(B&H + Abt agree) and upgraded to verified on user "
        "confirmation (DECISIONS 064). Correction vs the 2026-10-31 candidate price $69.99: "
        "that is the list price — the current street price is $58 at "
        "B&H, Abt, Electronic Express and Focus Camera and $59.99 at "
        "Best Buy. White (UPC 027242930346), Blue and Yellow are "
        "different colorways. Distinct from the set's WF-C710N Black "
        "(WFC710N/B) and WF-1000XM5/XM6 Black — the C510 (2024) is "
        "Sony's compact everyday budget line, no noise cancelling.",
        status="verified",
    ),
    EvalProduct(
        key="sony-inzone-h5-black",
        brand="Sony",
        model="INZONE H5",
        variant="Black (WHG500/B)",
        category="headphones",
        identifiers={"UPC": "027242927919", "MPN": "WHG500/B"},
        identifier_sources={
            "UPC": "Datavision + Focus Camera public product JSON "
            "agree on UPC 027242927919 at $128.00 (identified "
            "snapshots 2026-11-07 retry/retry3, fresh from coverage "
            "round 2)"
        },
        notes="Focus Camera $128.00 (Black, $128 vs $178, page-verified "
        "2026-11-06 — the Meta Catalog feed row for the same URL was "
        "$178, so the price has dropped since the feed was cut); "
        "Datavision $128.00 (feed row, Black); Abt $128.00 "
        "(page-verified — price-only: 'Notify me when this item is "
        "available', PreOrder; manufacturer rebate ends 11/22/2026, "
        "comp. value $178). MPN WHG500/B confirmed (Best Buy US Model "
        "WHG500/B, SKU 6562125 + Crutchfield MFR # WHG500/B + Abt "
        "agree). UPC verified 2026-11-07 (Datavision + Focus Camera "
        "public product JSON agree) and upgraded to verified on user "
        "confirmation (DECISIONS 064). Correction vs the 2026-10-31 candidate price "
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
        status="verified",
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
    EvalProduct(
        key="hp-omen-27s-black",
        brand="HP",
        model="OMEN 27s 27-inch FHD 240Hz Gaming Monitor",
        variant="Black (780G5AA#ABA)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="HP direct $389.99 (InStock, hp.com/us-en page JSON-LD "
        "read 2026-11-06, Product # 780G5AA#ABA, 27-inch FHD "
        "1920x1080 IPS 240 Hz 1ms GtG, G-SYNC compatible, "
        "DisplayHDR 400); Newegg $309 (feed authorized_retailer "
        "row — suspected; color unstated, not page-verified). "
        "Identifiers PENDING: MPN 780G5AA#ABA confirmed (HP US "
        "page), but the US UPC is single-source only — the HP "
        "datasheet (1WorldSync syndication + the same document "
        "mirrored on Etilize) lists UPC/EAN (ABA) 197029615442 "
        "for P/N 780G5AA#ABA, and no second independent non-Amazon "
        "source states it (B&H lists the 780G5AA#ABA page with no "
        "UPC and marks it Discontinued at $349.99; Amazon also "
        "states 197029615442 but Amazon never corroborates), so "
        "identifiers stay empty per the strict two-source rule; "
        "re-check next refresh. Not copied: 197029615466 — that "
        "is the (ABB) regional code, not the US (ABA) code; the "
        "OMEN 27 (165 Hz, Z4D33AA) and OMEN 27q/27qs lines — "
        "different models. Distinct from the set's Dell/Alienware "
        "monitors — the OMEN 27s (2023, HP's mainstream 240 Hz "
        "FHD gaming monitor) is the first HP monitor in the set.",
    ),
    EvalProduct(
        key="hyperx-cloud-iii-black-red",
        brand="HyperX",
        model="Cloud III Gaming Headset",
        variant="Black-Red (727A9AA)",
        category="headphones",
        identifiers={},
        status="pending",
        notes="HP direct $99.99 (InStock, hp.com/us-en page JSON-LD "
        "read 2026-11-06, Product # 727A9AA, Black/Red, wired "
        "53 mm angled drivers, 10 mm mic, USB-C/USB-A/3.5 mm); "
        "Staples $104.59 (Black/Red 727A9AA, feed "
        "authorized_retailer row — suspected; not page-verified); "
        "Newegg $159.69 (feed row — suspected; color unstated, "
        "above list, not page-verified). Correction vs sweep 059: "
        "the Black-Red MPN is 727A9AA on the HP US product page — "
        "the sweep's 4P5M0AA came from a bundle listing and an "
        "OMEN desktop accessory upsell and is NOT the standalone "
        "headset's code, so 4P5M0AA was not recorded; 727A8AA is "
        "the Black colorway and BS7C1AA is White, both different "
        "colorways at the same $99.99. Identifiers PENDING: MPN "
        "727A9AA confirmed (HP US page + Staples feed row agree), "
        "but the only UPC found, 197029008237, is stated on "
        "Amazon listings only (Amazon.com/.ca/.in, ASIN "
        "B0C3BV19Q3) — and those same listings also carry a "
        "second, conflicting code 740617255522 — so identifiers "
        "stay empty per the DualSense precedent; re-check next "
        "refresh. Not copied: the Cloud III Wireless / Cloud III "
        "S Wireless (different, wireless models); the Cloud II "
        "(older model). Distinct from the set's Sony, Bose, JBL, "
        "Razer and Corsair headsets — the Cloud III (2023, "
        "HyperX's mainstream wired headset) is the first HyperX "
        "headset in the set.",
    ),
    EvalProduct(
        key="hp-920-ergonomic-vertical-mouse-black",
        brand="HP",
        model="920 Ergonomic Vertical Mouse",
        variant="Black (6H1A4AA#ABA)",
        category="mice",
        identifiers={"UPC": "197029640277", "MPN": "6H1A4AA#ABA"},
        identifier_sources={
            "UPC": "HP datasheet for the 920 Ergonomic Wireless "
            "Mouse (Product number 6H1A4AA; UPC number (ABA) "
            "197029640277) + eBay US product catalog (item "
            "156358903729, MPN 6H1A4AA#ABA, UPC 197029640277) "
            "agree"
        },
        status="verified",
        notes="HP direct $68.99 (sale vs $114.99 list, InStock, "
        "hp.com/us-en page JSON-LD read 2026-11-06, Product # "
        "6H1A4AA#ABA, Black, wireless 2.4 GHz + Bluetooth 5.3, "
        "detachable wrist rest, 6 buttons, up to 4000 dpi); Best "
        "Buy $68.99 (sale vs $114.99 list, SKU 12714516, feed "
        "authorized_retailer row — suspected; the feed title "
        "says 'Wired' but the HP US page specs the mouse as "
        "wireless, so the title is a feed mislabel, not a second "
        "variant; not page-verified). Not copied: 196548939633 "
        "— that is the (ABB) EMEA code, not the US (ABA) code "
        "(the HP datasheet lists (ABA) 197029640277, (ABB) "
        "196548939633, (ABL) 196548939640, (UUF) 196548939657); "
        "the HP 925 Ergonomic Vertical Mouse (different, business "
        "model, $114 list / $68 sale in the same feed run) and "
        "the HP 710 Rechargeable Silent Mouse ($79.99) — different "
        "mice. Distinct from the set's Logitech, Razer, Corsair "
        "and Alienware mice — the 920 (2023, Red Dot winner, HP's "
        "ergonomic vertical mouse) is the first HP mouse in the "
        "set. Re-check the $68.99 sale price after the Early "
        "Black Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="hp-omen-27q-g2-black",
        brand="HP",
        model="OMEN 27q G2 27-inch QHD 180Hz Gaming Monitor",
        variant="Black (AV4H6AA#ABA)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="HP direct $203.99 (sale vs $339.99 list, InStock, "
        "hp.com/us-en page JSON-LD read 2026-11-06, Product # "
        "AV4H6AA#ABA, 27-inch QHD 2560x1440 IPS 180 Hz 1ms GtG, "
        "AMD FreeSync, HDR 400); Newegg $218.99 (AV4H6AA in the "
        "title, feed authorized_retailer row — suspected; not "
        "page-verified). Identifiers PENDING: MPN AV4H6AA#ABA "
        "confirmed (HP US page + Harvey Norman UK + DirectDial "
        "agree), but no US UPC surfaced — the HP datasheet lists "
        "UPC codes for #A2N (198701661184), #ABB (198701661221), "
        "#ABT, #ABU, #ABV, #ACQ, #UUG and #UUZ, and the (ABA) "
        "slot is absent, so identifiers stay empty per the "
        "DualSense precedent; re-check next refresh. Not copied: "
        "198701661221 — that is the (ABB) regional code, not the "
        "US (ABA) code; the OMEN 27qs G2 280 Hz (AW3V0AA#ABA, "
        "different, faster panel) and the OMEN 27q (780H4AA, "
        "older 165 Hz model) — different monitors. Excluded: the "
        "Micro Center $169.99 shop.app row (new_item_marketplace, "
        "DECISIONS 021) and the Newegg $553.98 row (same model "
        "name at 2.7x the direct price, unconfirmed listing). "
        "Distinct from the set's Dell/Alienware/HP monitors — the "
        "27q G2 (HP's mainstream 180 Hz QHD gaming monitor) is "
        "the first HP QHD monitor in the set. Re-check the "
        "$203.99 sale price after the Early Black Friday event "
        "ends Nov 8.",
    ),
    EvalProduct(
        key="hyperx-alloy-rise-75-black",
        brand="HyperX",
        model="Alloy Rise 75 Mechanical Gaming Keyboard",
        variant="Black, US Layout, HyperX Red - Linear, wired (7G7A4AA#ABA)",
        category="keyboards",
        identifiers={},
        status="pending",
        notes="HyperX direct $84.99 (InStock, hyperx.com US store "
        "page read 2026-11-06 — the only variant listed: Black / "
        "US Layout / HyperX Red - Linear, wired, 8k polling, "
        "hot-swappable, gasket mounted); Best Buy $84.99 (sale "
        "vs $169.99 list, SKU 11006248, Black wired linear, feed "
        "authorized_retailer row — suspected; not page-verified); "
        "Target $84.99 (sale vs $169.99 list, feed row — "
        "suspected; not page-verified); Newegg $169.99 (feed row "
        "— the list price; not page-verified). Identifiers "
        "PENDING: MPN 7G7A4AA#ABA confirmed (HP US page + "
        "HyperX feed spec row agree), but the US UPC is "
        "single-source only — the HP leaflet (mirrored on "
        "expert.de) lists HP GTIN (ABA) 197192334096, and no "
        "second independent non-Amazon source states it, so "
        "identifiers stay empty per the strict two-source rule; "
        "re-check next refresh. Not copied: the Alloy Rise 75 "
        "Wireless (different, wireless model, up to 1500-hour "
        "battery) and the Alloy Rise Top Plates (accessory, "
        "$49.99) — different products. Distinct from the set's "
        "Logitech, Keychron, Razer, Corsair and Alienware boards "
        "— the Alloy Rise 75 (2024, HyperX's flagship customizable "
        "75% board) is the first HyperX keyboard in the set. "
        "Re-check the $84.99 sale price after the Early Black "
        "Friday event ends Nov 8.",
    ),
    # --- Expansion batch 22 (2026-11-06, continuous expansion per DECISIONS 027) ---
    # 130 -> 135 models. DECISIONS 044, BUILD_LOG 061.
    EvalProduct(
        key="hp-omen-27k-black",
        brand="HP",
        model="OMEN 27k 27-inch UHD 144Hz Gaming Monitor",
        variant="Black (780G8AA#ABA)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="HP direct $370.32 (InStock, hp.com/us-en page JSON-LD "
        "read 2026-11-06, Product # 780G8AA#ABA, 27-inch 4K UHD "
        "3840x2160 IPS 144 Hz 1ms GtG, G-SYNC compatible, "
        "DisplayHDR 400, built-in KVM switch). Identifiers "
        "PENDING: MPN 780G8AA#ABA confirmed (HP US page), but the "
        "HP datasheet (1WorldSync) lists UPC codes only for #ABB "
        "(197029615961) and #ABU (197029615992) — the (ABA) slot "
        "is absent, so no US UPC surfaced; identifiers stay empty "
        "per the DualSense precedent; re-check next refresh. Not "
        "copied: 197029615961 (the ABB regional code) and "
        "197029615992 (the ABU regional code); the OMEN 27qs G2 "
        "280 Hz (AW3V0AA#ABA, different, faster panel) and the "
        "OMEN 27q G2 (already in the set) — different monitors. "
        "Excluded: the Newegg $609.99 feed row (65% above the HP "
        "direct price, unconfirmed outlier, Distritech "
        "precedent). Distinct from the set's Dell/Alienware/HP "
        "monitors — the OMEN 27k (2023, HP's mainstream 4K 144 Hz "
        "gaming monitor) is the first HP 4K monitor in the set.",
    ),
    EvalProduct(
        key="hyperx-omen-oled-27q-black",
        brand="HyperX",
        model="OMEN OLED 27q 27-inch QHD 240Hz Gaming Monitor",
        variant="Black (CH0R2AA#ABA)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="HP direct $399.99 (sale vs $499.99 list, InStock, "
        "hp.com/us-en page JSON-LD read 2026-11-06, Product # "
        "CH0R2AA#ABA, 27-inch QHD 2560x1440 QD-OLED 240 Hz "
        "0.03ms GtG, G-SYNC, HyperX OLED Core Protect, factory "
        "color calibration); HyperX direct $399.99 (feed "
        "brand_direct row — suspected; not page-verified); Best "
        "Buy $379.99 (Model CH0R2AA, SKU 6669985, feed "
        "authorized_retailer row — suspected; not page-verified). "
        "Identifiers PENDING: MPN CH0R2AA#ABA confirmed (HP US "
        "page + Best Buy agree), but the UPC is conflicted — the "
        "HP datasheet (1WorldSync) states P/N CH0R2AA, UPC "
        "199642944442, while Amazon states UPC 199642944428 for "
        "CH0R2AA#ABA, and no second non-Amazon source states "
        "either code, so identifiers stay empty per the DualSense "
        "precedent; neither code was recorded; re-check next "
        "refresh. Not copied: the OMEN OLED 34 (different, "
        "34-inch WQHD 360 Hz) and the OMEN 27q G3 (different, IPS "
        "240 Hz) — different monitors. Excluded: the mydex.shop "
        "$822.69 row (seller_type other, DECISIONS 021). "
        "Distinct from the set's Dell/Alienware/HP monitors — the "
        "OMEN OLED 27q (HyperX's mainstream QD-OLED gaming "
        "monitor) is the first OLED monitor in the set. Re-check "
        "the $399.99 sale price after the Early Black Friday "
        "event ends Nov 8.",
    ),
    EvalProduct(
        key="hyperx-cloud-iii-s-wireless-black-red",
        brand="HyperX",
        model="Cloud III S Wireless Gaming Headset",
        variant="Black-Red (A59Z0AA)",
        category="headphones",
        identifiers={"UPC": "198415435569", "MPN": "A59Z0AA"},
        identifier_sources={
            "UPC": "PBTech retailer listing (Manufacturer Part No "
            "A59Z0AA, UPC 198415435569, Black-Red) + trippodo spec "
            "database (EAN13 0198415435569, the same code in "
            "GTIN-13 form, for A59Z0AA Black-Red) agree"
        },
        status="verified",
        notes="HP direct $179.99 (InStock, hp.com/us-en page JSON-LD "
        "read 2026-11-06, Product # A59Z0AA, Black-Red, wireless "
        "2.4 GHz + Bluetooth 5.3 + Instant Pair, 53 mm angled "
        "drivers, up to 120-hour battery, DTS Headphone:X); Best "
        "Buy $129.99 (Model A59Z0AA, SKU 6618287, Red/Black, Best "
        "Buy page text read via search index 2026-11-06 — sale "
        "price, below the $179.99 HP list); Target $129.99 (feed "
        "authorized_retailer row — suspected; color unstated, not "
        "page-verified); Newegg $170.99 Black-Red (feed row — "
        "suspected; not page-verified). Not copied: A59YZAA "
        "(Black), AX6G1AA (White), DF7E9AA (Black/Blue) and "
        "White/Pink — different colorways at the same $179.99; "
        "the Cloud III Wireless (different, older model, $99.99 "
        "sale) and the Cloud III wired (already in the set). "
        "Excluded: the Ayoub $145 row (overseas seller, "
        "DECISIONS 021), the buyitsolutions $165.23 row "
        "(unconfirmed reseller), the Newegg $197.99 / $250.69 / "
        "$216 rows (above list, unconfirmed), the Best Buy "
        "$179.99 Black/Sci-Fi Blue Special Edition row (different "
        "colorway) and all HyperX bundle rows. Distinct from the "
        "set's Sony, Bose, JBL, Razer, Corsair and HyperX "
        "headsets — the Cloud III S Wireless (2025, HyperX's "
        "flagship wireless headset) is the first HyperX wireless "
        "headset in the set.",
    ),
    EvalProduct(
        key="hyperx-pulsefire-haste-2-pro-slate-grey",
        brand="HyperX",
        model="Pulsefire Haste 2 Pro 4K Wireless Gaming Mouse",
        variant="Slate Grey (A1KY5AA)",
        category="mice",
        identifiers={},
        status="pending",
        notes="HP direct $119.99 (InStock, hp.com/us-en page JSON-LD "
        "read 2026-11-06, Product # A1KY5AA, Slate grey, true "
        "4 kHz wireless polling, 61 g, HyperX 26K sensor up to "
        "26000 DPI, up to 90-hour battery, Instant Pair); HyperX "
        "direct $119.99 (feed brand_direct row — suspected; not "
        "page-verified); Best Buy $99.99 (Slate Grey, SKU 6626287, "
        "feed authorized_retailer row — suspected; not "
        "page-verified). Identifiers PENDING: MPN A1KY5AA "
        "confirmed (HP US page + HyperX feed agree), but the UPC "
        "is single-source only — Currys Business UK lists EAN "
        "198122802432 for A1KY5AA, and no second independent "
        "source states it (no UPC surfaced in the HP datasheet "
        "copies read), so identifiers stay empty per the strict "
        "two-source rule; re-check next refresh. Not copied: "
        "198122802432 (single-source); the Pulsefire Haste 2 S "
        "Navy/Silver (different, S model), the Pulsefire Haste 2 "
        "Wireless Black (6N0B0AA, different, $89.99) and the "
        "Pulsefire Saga Pro (different mouse) — different mice. "
        "Excluded: the Newegg $201.98 row (above list, "
        "unconfirmed) and all HyperX bundle rows. Distinct from "
        "the set's Logitech, Razer, Corsair, Alienware and HP "
        "mice — the Haste 2 Pro (HyperX's first true-4kHz mouse) "
        "is the first HyperX mouse in the set.",
    ),
    EvalProduct(
        key="hyperx-quadcast-2-s-black",
        brand="HyperX",
        model="QuadCast 2 S USB Microphone",
        variant="Black (9A273AA)",
        category="microphones",
        identifiers={},
        status="pending",
        notes="HP direct $149.99 (sale vs $199.99 list, InStock, "
        "hp.com/us-en page JSON-LD read 2026-11-06, Product # "
        "9A273AA, Black, 32-bit/192 kHz, 100+ aRGB LEDs, "
        "tap-to-mute sensor, multifunction knob, four polar "
        "patterns); HyperX direct $149.99 (feed brand_direct row "
        "— suspected; not page-verified). Identifiers PENDING: "
        "MPN 9A273AA confirmed (HP US page), but the UPC is "
        "single-non-Amazon-source only — the HP user manual (via "
        "manuals.plus) states UPC 197961186741 for 9A273AA, and "
        "every other source stating it is Amazon (.com/.ca/.in/"
        ".ie), which never corroborates, so identifiers stay "
        "empty per the strict two-source rule; re-check next "
        "refresh. Not copied: 197961186741 (manual-only); the "
        "QuadCast 2 Black (872V1AA, different, $149.99, red-only "
        "lighting, 24-bit/96 kHz) and QuadCast 2 Frost ($129.99) "
        "— different mics; the QuadCast S (4P5P7AA, older model). "
        "Excluded: the Newegg $223.99 / $329.98 rows (above list, "
        "unconfirmed; the $223.99 row carries third-party brand "
        "Barrow) and the Mister Spex $180 drop_shipper row "
        "(DECISIONS 021), plus all HyperX bundle rows. First "
        "microphone in the set — the new category 'microphones' "
        "enters the set with this batch (category decision in "
        "DECISIONS 044; cf. the HP printer precedent in "
        "BUILD_LOG 059). Re-check the $149.99 sale price after "
        "the Early Black Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="asus-rog-swift-oled-pg27ucwm-black",
        brand="ASUS",
        model="ROG Swift OLED PG27UCWM 27-inch 4K 240Hz Gaming Monitor",
        variant="Black (single colorway)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="ROG US $1,199.00 (ROG US monitors category page read "
        "2026-11-06, Temporarily out of stock — price verified, "
        "stock out at direct; 26.5-inch Tandem RGB OLED, dual mode "
        "4K@240Hz / FHD@480Hz, TrueBlack Glossy, DP 2.1a, USB-C "
        "90W); B&H $1,199.00 (page read fresh 2026-11-06, 'New Item "
        "- Coming Soon', OutOfStock); Newegg $1,199.99 (feed "
        "authorized_retailer row — suspected; stock not confirmed "
        "on the page read). Identifiers PENDING: the UPC "
        "199291335226 is B&H-only — no second independent source "
        "states it (Scan UK lists GTIN 4711636505857 for the EU "
        "listing, a different regional code, not a corroboration), "
        "and no ASUS part number (90LM…) surfaced for the US "
        "listing, so identifiers stay empty per the strict "
        "two-source rule; re-check next refresh. Not copied: "
        "199291335226 (single-source); 4711636505857 (EU GTIN); "
        "the PG32UCWM 32-inch ($1,399) and PG27UCDM ($1,099, "
        "QD-OLED) — different monitors shown on the same B&H/ROG "
        "pages. Excluded: the rog.asus.com/ca-en $1,699 row (CAD, "
        "non-US, DECISIONS 021). Stock caveat: temporarily out of "
        "stock at ROG US and coming soon at B&H — added per the "
        "PS5 Pro precedent (batch 3: price-verified, stock not "
        "confirmed); re-check stock next refresh. Distinct from "
        "the set's Dell/Alienware/HP monitors — the PG27UCWM "
        "(ASUS's flagship Tandem RGB OLED monitor) is the first "
        "ASUS monitor in the set and the first ASUS brand entry of "
        "any kind.",
    ),
    EvalProduct(
        key="asus-rog-delta-ii-black",
        brand="ASUS",
        model="ROG Delta II Wireless Gaming Headset",
        variant="Black (90YH03W0-BHAA03)",
        category="headphones",
        identifiers={},
        status="pending",
        notes="ASUS eShop USA $185.99 (page read fresh 2026-11-06, "
        "InStock, Product Name A701 ROG DELTA II/BLK, Part Number "
        "90YH03W0-BHAA03, Color Black, tri-mode BT/2.4GHz/3.5mm, "
        "50 mm titanium-plated drivers, up to 110-hour battery, "
        "318 g); Target $199.99 Black (feed authorized_retailer "
        "row — suspected; not page-verified); ASUS shop $229.99 "
        "list (feed row for the same part, seller_type unstated "
        "— suspected; list price). Identifiers PENDING: MPN "
        "90YH03W0-BHAA03 confirmed (ASUS eShop USA page), but no "
        "US UPC surfaced — the EAN 4711387604847 stated by "
        "Overclockers UK and itworkup.co.za is for 90YH03W0-BHUA00 "
        "(the UK Black part number), not the US BHAA03, so it was "
        "not carried across regions per the strict two-source "
        "rule; re-check next refresh. Not copied: 4711387604847 "
        "(UK part); 90YH03W0-BHAA10 (Moonlight White, CA $339.99 "
        "CAD — different colorway); 90YH04C0-BHAA10 (Delta II KJP "
        "limited edition, $269.99 — different headset). Excluded: "
        "the eShop feed row at $177.99 (stale — the fresh page "
        "read shows $185.99; same staleness pattern as batch 22's "
        "QuadCast $159.99 read) and the pricehistory.app $177.99 "
        "figure (Amazon-derived; Amazon never corroborates). "
        "Distinct from the set's Sony, Bose, JBL, Razer, Corsair, "
        "HyperX and Alienware headsets — the Delta II is the first "
        "ASUS headset in the set.",
    ),
    EvalProduct(
        key="asus-rog-gladius-iv-ace-black",
        brand="ASUS",
        model="ROG Gladius IV Ace Wireless Gaming Mouse",
        variant="Black (P729 ROG GLADIUS IV ACE/BLK)",
        category="mice",
        identifiers={},
        status="pending",
        notes="Best Buy $169.99 (page read fresh 2026-11-06, "
        "InStock, Model P729 ROG GLADIUS IV ACE/BLK, SKU 6690126, "
        "Sold by Best Buy, 56 g, AimPoint Pro 65K sensor, "
        "SpeedNova 8K Gen II, customizable weight); ASUS $169.99 "
        "(ROG US product page JSON-LD read 2026-11-06 — price "
        "verified, Availability OutOfStock at direct). "
        "Identifiers PENDING: no MPN in 90MP… form and no UPC "
        "surfaced for this model in any source read (launched "
        "2026-10-30; B&H carries no listing yet), so identifiers "
        "stay empty per the strict two-source rule; re-check next "
        "refresh. Not copied: nothing — no candidate code "
        "surfaced. Not the Gladius III (different mouse) or the "
        "Harpe II Ace ($150.99, different mouse). Excluded: the "
        "AliExpress $271.08 row (overseas marketplace, DECISIONS "
        "021). Distinct from the set's Logitech, Razer, Corsair, "
        "Alienware, HP and HyperX mice — the Gladius IV Ace is the "
        "first ASUS mouse in the set.",
    ),
    EvalProduct(
        key="asus-rog-azoth-96-he-black",
        brand="ASUS",
        model="ROG Azoth 96 HE Wireless Gaming Keyboard",
        variant="Black (90MP040H-BKAA20)",
        category="keyboards",
        identifiers={},
        status="pending",
        notes="ASUS eShop USA $359.99 (InStock, Open Graph read "
        "2026-11-06, Product Name M901 ROG AZOTH 96 HE/BLK/HFXV2/"
        "CA/PBT, Part Number 90MP040H-BKAA20, HFX V2 magnetic "
        "switches, SpeedNova 8K, OLED touchscreen); Newegg "
        "$359.99 (feed authorized_retailer row — suspected; not "
        "page-verified); Target $339.99 sale (feed "
        "authorized_retailer row — suspected; Target's $399.99 "
        "reg conflicts with the ASUS $359.99 list). Identifiers "
        "PENDING: MPN 90MP040H-BKAA20 confirmed (ASUS eShop USA "
        "page), but the only UPC surfaced, 199291008571, is "
        "stated on Amazon only (for M901 ROG AZOTH 96 "
        "HE/BLK/HFXV2/CA/ABS — note ABS keycaps vs the eShop's "
        "PBT), and Amazon never corroborates, so identifiers stay "
        "empty per the strict two-source rule; re-check next "
        "refresh. Not copied: 199291008571 (Amazon-only); "
        "4711636009126 (EAN for 90MP040H-BKDA20, the QWERTZ EU "
        "part) and 4711636009201 (barcode for 90MP040H-BKUA20, "
        "the UK part) — different regional parts. Not the Azoth "
        "96 HE Lite (90MP048H-BKAA00, different keyboard, also "
        "$359.99) or the Azoth Extreme ($499.99). Correction vs "
        "sweep 059: the sweep's $308.99 is superseded — the fresh "
        "eShop read, the feed and Newegg all agree on $359.99 "
        "(the $305.99 sale row on a rog.asus.com helpdesk page is "
        "stale/unclear and was not used). Distinct from the set's "
        "Logitech, Razer, Corsair, Alienware, HP, HyperX and "
        "Keychron keyboards — the Azoth 96 HE is the first ASUS "
        "keyboard in the set.",
    ),
    EvalProduct(
        key="asus-rog-cetra-open-wireless-black",
        brand="ASUS",
        model="ROG Cetra Open Wireless Gaming Earbuds",
        variant="Black (90YH0450-BTAA00)",
        category="earbuds",
        identifiers={},
        status="pending",
        notes="ASUS eShop USA $229.99 (page read via search index "
        "2026-11-06, Product Name O701 ROG CETRA OPEN "
        "WIRELESS/BLK, Part Number 90YH0450-BTAA00, dual-mode BT "
        "+ SpeedNova 2.4 GHz, 14.2 mm DLC drivers, open-ear, "
        "16-hour battery + 48-hour case); Best Buy $229.99 (feed "
        "authorized_retailer row + page text read via search "
        "index 2026-11-06, Model O701 ROG CETRA OPEN WRLS/BLK, "
        "SKU 6668329, Sold by Best Buy — suspected; not freshly "
        "page-verified). Identifiers PENDING: the UPC is a "
        "genuine conflict, not a verification — PBTech (NZ "
        "retailer) and the LittleBit datasheet agree on UPC "
        "199291232747 for 90YH0450-BTUA00 (the non-US part), "
        "while Amazon states UPC 199291232754 for the same US "
        "model name (O701 ROG CETRA OPEN WIRELESS/BLK); neither "
        "code was recorded, per the DualSense precedent and the "
        "strict two-source rule (no US source ties a UPC to the "
        "US part BTAA00); re-check next refresh. Not copied: "
        "199291232747 (non-US part) or 199291232754 (Amazon-only, "
        "conflicting); 90YH0450-BTUA00 (non-US part). Not the "
        "Cetra True Wireless SpeedNova (different earbuds, "
        "$199.99). Excluded: the Walmart $229.99 feed row "
        "(sold-by unconfirmed — marketplace risk, DECISIONS 021), "
        "the Newegg WUQ $390.99 row (third-party brand, above "
        "list), the 961souq $325/$399 rows (overseas), the "
        "rog.asus.com/ca-en $339.99 CAD row (non-US). Distinct "
        "from the set's Sony, Bose, JBL, Google, Samsung and "
        "other earbuds — the Cetra Open Wireless is the first "
        "ASUS earbuds entry in the set.",
    ),
    EvalProduct(
        key="dell-27-plus-4k-monitor-s2725qs",
        brand="Dell",
        model="27 Plus 4K Monitor S2725QS",
        variant="Ash White (T4CNF)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="Dell direct $299.99 (Meta Catalog feed brand_direct "
        "row 2026-11-06 — suspected; not page-verified, Dell US "
        "page text carries no price); Newegg $299.99 (feed "
        "authorized_retailer row — suspected; page read fresh "
        "2026-11-06 confirms the exact model but carries no "
        "price); ThinkEdu $284.99 (feed authorized_retailer row "
        "— suspected; not page-verified). Dell US page confirms "
        "Manufacturer Part Number T4CNF, Ash White, 27-inch 4K "
        "UHD IPS 120 Hz, FreeSync Premium, 99% sRGB, dual 5 W "
        "speakers (page read fresh 2026-11-06). Identifiers "
        "PENDING: MPN T4CNF confirmed (Dell US + CA pages agree; "
        "the AU MPN 8PRJ8, IE/UK MPN V424D and SG/MY MPN 2M7P9 "
        "are regional and were not used), but the only UPC "
        "surfaced, 884116485117, is stated on Amazon only "
        "(alongside a second code, 738060953201), and Amazon "
        "never corroborates; the Icecat EAN 5397184962350 is a "
        "single-source EU datasheet, so identifiers stay empty "
        "per the DualSense precedent; re-check next refresh. Not "
        "copied: 884116485117 (Amazon-only); 738060953201 "
        "(Amazon-only, second code on the same listing); "
        "5397184962350 (Icecat-only EAN); 8PRJ8 / V424D / 2M7P9 "
        "(regional MPNs). Not the S2725QC (USB-C sibling, "
        "$349.99) or the S2721QS (older 60 Hz model, $299.99). "
        "The sweep's ~$279.99 is superseded for Dell direct — "
        "the $279.99 figures traced this round are Amazon prices "
        "(BetterBuyBase, Gadget Review), excluded per the "
        "no-Amazon rule; the Dell feed row and Newegg both say "
        "$299.99. Distinct from everything in the set — the "
        "S2725QS (2025, Dell's mainstream 27-inch 4K 120 Hz "
        "monitor) is the second Dell monitor in the set. "
        "Re-check the $299.99 price after the Early Black Friday "
        "event ends Nov 8.",
    ),
    EvalProduct(
        key="dell-ultrasharp-32-4k-thunderbolt-hub-monitor-u3225qe",
        brand="Dell",
        model="UltraSharp 32 4K Thunderbolt Hub Monitor U3225QE",
        variant="Silver (3PVPJ)",
        category="monitors",
        identifiers={"UPC": "884116484561", "MPN": "3PVPJ"},
        identifier_sources={
            "UPC": "B&H Photo spec page (UPC 884116484561, MFR # "
            "U3225QE) + CompTechDirect Icecat-derived listing "
            "(EAN/UPC code 5397184923399 0884116484561, MFG # "
            "DELL-U3225QE) agree; Amazon also states the code "
            "but is never a corroborating source"
        },
        status="verified",
        notes="Dell direct $1,029.99 (Meta Catalog feed "
        "brand_direct row 2026-11-06 — suspected; not "
        "page-verified, Dell US page text carries no price); "
        "Target $799.99 (InStock, search-index JSON-LD read "
        "2026-11-06, listing A-1004931139); Adorama $799.00 "
        "(InStock, search-index JSON-LD read 2026-11-06); CDW "
        "$949.99 (feed authorized_retailer row — suspected; not "
        "page-verified); Newegg $1,099.99 (feed "
        "authorized_retailer row — suspected; the list price). "
        "Dell US page confirms Manufacturer Part Number 3PVPJ, "
        "Silver, 31.5-inch 4K UHD IPS Black 120 Hz, Thunderbolt "
        "4 hub, 140 W PD, 2.5GbE, KVM (page read fresh "
        "2026-11-06). The sweep's $1,099.99 is the list price, "
        "not the current Dell price — the feed brand_direct row "
        "says $1,029.99 and Target/Adorama are at ~$799. Not "
        "copied: the UK MPN FPG3K (regional, Dell UK page) and "
        "the EAN 5397184923399 on its own (the GTIN-12 form "
        "0884116484561 is the recorded UPC). Not the U3223QE "
        "(previous generation, $1,116.99) or the U3226Q QD-OLED "
        "($2,599.99) or the P3225QE (100 Hz, standard IPS, "
        "$559-$643.99). Excluded: the Target 2-pack bundle "
        "$1,699 (different product), the second Target feed row "
        "$1,028.97 (listing A-1006296976, conflicts with the "
        "$799.99 Target listing — not used), the BuyItSolutions "
        "$1,034.83 row (unconfirmed reseller), the K-Rauta rows "
        "(Estonia, non-US). Distinct from everything in the "
        "set — the U3225QE (Feb 2025, the world's first enhanced "
        "IPS Black monitor, Dell's flagship 32-inch 4K hub "
        "monitor) is the first UltraSharp in the set. Re-check "
        "the $1,029.99 Dell price and the ~$799 street price "
        "after the Early Black Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="alienware-32-curved-gaming-monitor-aw3225dm",
        brand="Alienware",
        model="32 Curved Gaming Monitor AW3225DM",
        variant="Dark Blue (VX89X)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="Dell direct $249.99 (sale vs $299.99 list; Windows "
        "Central 2026-10-26 'Alienware 32 (AW3225DM) for $249.99 "
        "(was $299.99)' at Dell + topsave.org 2026-10-23 'Dell "
        "has the Alienware 32 Curved Gaming Monitor (AW3225DM) "
        "for $249.99, sold by Dell' + the BUILD_LOG 058 Dell US "
        "sweep 2026-11-06); Best Buy $319.99 (InStock, page read "
        "fresh 2026-11-06, Model AW3225DM, SKU 6619487, Sold by "
        "Best Buy, 4.8 stars, 954 reviews); Newegg $370.30 "
        "(feed authorized_retailer row — suspected; above list, "
        "not page-verified). Dell US page confirms Manufacturer "
        "Part Number VX89X, Dark Blue, 31.5-inch QHD VA 180 Hz "
        "1500R curved, FreeSync Premium, DisplayHDR 400 (page "
        "read fresh 2026-11-06); Best Buy calls the same "
        "colorway Interstellar Indigo. Identifiers PENDING: MPN "
        "VX89X confirmed (Dell US + CA pages agree), but no US "
        "UPC surfaced — the only code found is EAN 5397184962725 "
        "on a single Icecat datasheet (mirrored by startech24, "
        "e-misija and manua.ls, all the same source family), so "
        "identifiers stay empty per the DualSense precedent; "
        "re-check next refresh. Not copied: 5397184962725 "
        "(Icecat-only EAN). Not the AW3225QF (4K QD-OLED, "
        "$999.99), the AW2725DM (27-inch, $269.99) or the "
        "AW2726DM (27-inch QD-OLED, $319.99-$349.99, already in "
        "the set). Excluded: the Sigmatiendas $507.99 sale row "
        "(overseas). Distinct from everything in the set — the "
        "AW3225DM (2025, Alienware's budget 32-inch curved QHD "
        "gaming monitor) is the second Alienware monitor in the "
        "set. Re-check the $249.99 sale price after the Early "
        "Black Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="alienware-tri-mode-wireless-gaming-keyboard-aw920k-dark-side-of-the-moon",
        brand="Alienware",
        model="Tri-Mode Wireless Gaming Keyboard AW920K",
        variant="Dark Side of the Moon (6R87M)",
        category="keyboards",
        identifiers={},
        status="pending",
        notes="Dell direct $159.99 (Meta Catalog feed brand_direct "
        "row 2026-11-06 for the 6R87M Dark Side of the Moon slug "
        "— suspected; not page-verified, Dell US page text "
        "carries no price). Dell US page (6R87M slug, read fresh "
        "2026-11-06) confirms the Dark Side of the Moon "
        "colorway (slug + /dsotm/ image paths), CHERRY MX Red "
        "switches, tri-mode 2.4 GHz / BT 5.1 / USB-C, magnetic "
        "snap-on charging, 4.3/5 (326 ratings, 230 reviews). "
        "Identifiers PENDING: no Dark Side UPC surfaced — the "
        "only UPC found, 884116448686, is stated on a single "
        "Icecat datasheet for AW920K-W-WW (the Lunar Light / "
        "White colorway) and was not carried across colorways; "
        "identifiers stay empty per the DualSense precedent; "
        "re-check next refresh. Not copied: 884116448686 "
        "(Lunar Light only, Icecat-only); EAN 5397184790397 "
        "(same Icecat datasheet, Lunar Light). Not the AW920K "
        "Lunar Light (different colorway, same $159.99) or the "
        "Alienware Pro Wireless Keyboard (different keyboard, "
        "$174.99, already in the set) or the AW510K ($129.99) "
        "and AW420K ($99.99). Excluded: the Fnac $218.02 row "
        "(overseas marketplace) and the second Dell feed row "
        "$149.99 sale vs $159.99 list on the generic 520-bbcg "
        "accessories path (colorway unstated — not attributed "
        "to the pinned variant). Distinct from the set's "
        "Logitech, Keychron, Razer, Corsair, HP and ASUS boards "
        "— the AW920K (Dec 2023, Alienware's first tri-mode "
        "wireless keyboard) is the second Alienware keyboard in "
        "the set. Re-check the $159.99 price after the Early "
        "Black Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="dell-pro-7-webcam-4k-wb726",
        brand="Dell",
        model="Pro 7 Webcam 4K WB726",
        variant="Black (G4MYM)",
        category="webcams",
        identifiers={},
        status="pending",
        notes="Dell direct $199.99 (Dell US webcams category "
        "pages, Offer ID V813W, Add to Cart, crawled 3 hours to "
        "3 days ago 2026-11-06; the Dell US product page "
        "search-index read agrees at $199.99, Manufacturer part "
        "V813W, Dell part v813w). Dell US page confirms "
        "Manufacturer Part Number G4MYM, 4K UHD 3840x2160 at "
        "60 fps, Sony STARVIS CMOS sensor, 90-degree field of "
        "view, Windows Hello, gesture control, presence sensing "
        "(page read via search index 2026-11-06). Single "
        "colorway (Black). Identifiers PENDING: MPN G4MYM "
        "confirmed (Dell US page), but no US UPC surfaced — the "
        "only code found is EAN 5397321028925 on Icecat "
        "datasheets for WB726-EMEA (the EMEA part, mirrored by "
        "several EU resellers, one source family), so "
        "identifiers stay empty per the DualSense precedent; "
        "re-check next refresh. Not copied: 5397321028925 "
        "(Icecat-only EAN, EMEA part). Not the Pro 5 Webcam 2K "
        "WB526 ($119.99, different webcam) or the WB7022 (older "
        "model). Excluded: the silarius $209.99 sale row "
        "(mislabeled brand_direct in the feed — unconfirmed "
        "reseller, not Dell) and the shop.app $174 marketplace "
        "row (DECISIONS 021). The $189.99 figure in Lifewire's "
        "September 10 report is stale — Dell's current listing "
        "is $199.99. Distinct from everything in the set — the "
        "WB726 (June 2026, Dell's flagship AI webcam) is the "
        "first webcam in the set and opens the new 'webcams' "
        "category (precedent: 'microphones' opened the same "
        "way). Re-check the $199.99 price after the Early Black "
        "Friday event ends Nov 8.",
    ),
    EvalProduct(
        key="asus-rog-swift-oled-pg32ucwm-black",
        brand="ASUS",
        model="ROG Swift OLED PG32UCWM 32-inch 4K 240Hz Gaming Monitor",
        variant="Black (90LM0DN0-B019B1)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="ASUS $1,399.00 (ROG US product page JSON-LD read "
        "fresh 2026-11-06, InStock; 31.5-inch 4K Tandem RGB "
        "OLED, dual mode 4K@240Hz / FHD@480Hz, TrueBlack "
        "Glossy, DP 2.1a, USB-C 90W, 3-year warranty); B&H "
        "$1,399.00 (page read fresh 2026-11-06, InStock, UPC "
        "199291571570); Newegg $1,399.99 (feed "
        "authorized_retailer row — suspected; not "
        "page-verified). Identifiers PENDING: the UPC "
        "199291571570 is B&H-only — no second independent "
        "source states it (Scan UK lists GTIN 4711636571531 "
        "for the EU listing, a different regional code, not a "
        "corroboration), and the MPN 90LM0DN0-B019B1 is ASUS "
        "eShop USA only, so identifiers stay empty per the "
        "strict two-source rule; re-check next refresh. Not "
        "copied: 199291571570 (single-source); 4711636571531 "
        "(EU GTIN); 90LM0DN0-B019B2 (PG32UCDMR part, different "
        "monitor). Excluded: the silarius $1,427.99 row "
        "(mislabeled brand_direct in the feed — unconfirmed "
        "reseller, not ASUS; same pattern as batch 24's "
        "WB726). Distinct from the set's Dell, Alienware, HP "
        "and ASUS PG27UCWM monitors — the PG32UCWM (ASUS's "
        "32-inch Tandem RGB OLED flagship) is the second ASUS "
        "monitor in the set.",
    ),
    EvalProduct(
        key="asus-rog-swift-oled-pg27aqdpr-black",
        brand="ASUS",
        model="ROG Swift OLED PG27AQDPR 27-inch QHD 500Hz Gaming Monitor",
        variant="Black (single colorway)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="ASUS $729.00 sale vs $899.00 list (ROG US monitors "
        "category page, search-index read crawled 2026-11-03, "
        "Temporarily out of stock at direct; 27-inch QHD "
        "QD-OLED, 500Hz, OLED Anti-Flicker 2.0, OLED Care Pro, "
        "DisplayHDR 500 True Black); Best Buy $999.99 (page "
        "read fresh 2026-11-06, InStock, Model PG27AQDPR, SKU "
        "6685336, Sold by Best Buy). Identifiers PENDING: no "
        "UPC and no ASUS part number (90LM...) surfaced for "
        "this model in any source read, so identifiers stay "
        "empty per the strict two-source rule; re-check next "
        "refresh. Not copied: nothing — no candidate code "
        "surfaced. Not the PG27AQDP (480Hz WOLED, $799/$679 — "
        "different monitor) or the PG27AQWP-W (540Hz "
        "dual-mode, $1,099). Correction vs sweep 059: the "
        "sweep's $899.00 'sale, save $170' misreads the "
        "category page — $899.00 is the LIST and $729.00 is "
        "the sale (save $170.00); the feed's $599.00 ROG row "
        "is a category-page misassociation (that price belongs "
        "to another monitor on the same page — the ROG US "
        "product page carries no offer block on the fresh "
        "read) and was not used. Stock caveat: temporarily out "
        "of stock at ROG US — added per the PS5 Pro precedent "
        "(batch 3: price-verified, stock not confirmed); Best "
        "Buy has stock. Re-check the $729.00 sale price after "
        "the Early Black Friday event ends Nov 8. Distinct "
        "from the set's other monitors — the PG27AQDPR is the "
        "third ASUS monitor in the set and ASUS's 500Hz "
        "QD-OLED monitor.",
    ),
    EvalProduct(
        key="asus-rog-delta-usb-c-black",
        brand="ASUS",
        model="ROG Delta USB-C Gaming Headset",
        variant="Black (90YH01D1-B2UA00)",
        category="headphones",
        identifiers={},
        status="pending",
        notes="ASUS $149.99 (ROG US product page JSON-LD + ASUS "
        "eShop USA page read fresh 2026-11-06, OutOfStock at "
        "direct; ESS 9218 Quad-DAC, USB-C + USB 2.0 adapter, "
        "Aura Sync RGB, 387 g); Newegg $102.78 (feed "
        "authorized_retailer row — suspected; 'ASUS ROG DELTA "
        "USB Connector Circumaural Headset', not "
        "page-verified). Identifiers PENDING: MPN "
        "90YH01D1-B2UA00 confirmed (ASUS eShop USA page, "
        "Product Name ROG DELTA/SR/UBW/ACI, Color Black), but "
        "no US UPC surfaced in any source read, so "
        "identifiers stay empty per the strict two-source "
        "rule; re-check next refresh. Not copied: "
        "90YH00Z1-B2UA00 (UK part, different regional part); "
        "90YH02K0-B2UA00 (Delta S, different headset). Not the "
        "Delta II (different headset, $185.99) or the Delta "
        "White Edition (different colorway/model). Excluded: "
        "the 961souq $203/$250 rows (overseas). Stock caveat: "
        "out of stock at ASUS direct — added per the PS5 Pro "
        "precedent (batch 3: price-verified, stock not "
        "confirmed); re-check stock next refresh. Distinct "
        "from the set's Sony, Bose, JBL, Razer, Corsair, "
        "HyperX, Alienware and ASUS Delta II headsets — the "
        "Delta (2018, the original ESS Quad-DAC ROG headset) "
        "is the second ASUS headset in the set.",
    ),
    EvalProduct(
        key="asus-rog-harpe-mini-core-black",
        brand="ASUS",
        model="ROG Harpe Mini Core Gaming Mouse",
        variant="Black (90MP04D0-BMAA02)",
        category="mice",
        identifiers={},
        status="pending",
        notes="ASUS $44.99 (ROG US product page JSON-LD + ASUS "
        "eShop USA read fresh 2026-11-06, InStock; 52 g wired, "
        "12,000 DPI, ROG Micro Switch II, Push-Fit sockets, "
        "Paracord, P524 ROG HARPE MINI CORE); B&H $29.99 (page "
        "read fresh 2026-11-06, InStock, UPC 199291014046); "
        "Newegg $32.00 sale vs $44.99 (feed "
        "authorized_retailer row — suspected; not "
        "page-verified). Identifiers PENDING: the UPC "
        "199291014046 is B&H-only — no second independent "
        "source states it — and the MPN 90MP04D0-BMAA02 is ASUS "
        "eShop USA only (the JP part is 90MP04D0-BMUA00, also "
        "listed by PB Tech NZ), so identifiers stay empty per "
        "the strict two-source rule; re-check next refresh. "
        "Not copied: 199291014046 (single-source); "
        "90MP04D0-BMUA00 (JP/non-US part). Not the Harpe Ace "
        "Mini (wireless, $81.99-$129.99, different mouse). "
        "Correction vs sweep 059: the sweep's $69.99 is the "
        "list — the current ASUS price is $44.99 sale (was "
        "$59.99). Excluded: the MercadoLibre $55 marketplace "
        "row (DECISIONS 021) and the JP 8,980 yen row "
        "(non-US). Re-check the $44.99 sale price after the "
        "Early Black Friday event ends Nov 8. Distinct from "
        "the set's Logitech, Razer, Corsair, Alienware, HP, "
        "HyperX and ASUS Gladius IV Ace mice — the Harpe Mini "
        "Core is the second ASUS mouse in the set.",
    ),
    EvalProduct(
        key="asus-rog-pelta-black",
        brand="ASUS",
        model="ROG Pelta Gaming Headset",
        variant="Black (90YH0410-BHAA00)",
        category="headphones",
        identifiers={},
        status="pending",
        notes="ASUS $104.99 sale vs $129.99 list (ASUS eShop USA "
        "BHAA00 page read fresh 2026-11-06, InStock, Product "
        "Name A501 ROG PELTA/BLK, Color Black; ROG US product "
        "page JSON-LD agrees at $104.99; tri-mode BT/2.4GHz/"
        "USB-C, 50 mm titanium drivers, 309 g, up to 70-hour "
        "battery). Identifiers PENDING: MPN 90YH0410-BHAA00 "
        "confirmed (ASUS eShop USA), but no US UPC surfaced "
        "— the only UPC found, 199291069725, is stated on a "
        "single ASUS datasheet for 90YH0410-BHUA10 (the White "
        "non-US part, EAN 4711636069724), so identifiers stay "
        "empty per the strict two-source rule; re-check next "
        "refresh. Not copied: 199291069725 (non-US White part, "
        "single datasheet); 90YH0410-BHAA10 (White, $104.99 — "
        "different colorway); 90YH0410-BHUA00 (non-US Black "
        "part). Not the Pelta Core (wired, $119.99, different "
        "headset). Correction vs sweep 059: the sweep's 'from "
        "$84.99' is not corroborated — no $84.99 price appears "
        "on any fresh read (ROG US $104.99/$129.99, eShop "
        "$104.99 both colorways); the $114.99 feed row for "
        "BHAA00 is stale (fresh eShop read $104.99) and was "
        "not used. Excluded: the Walmart $104.99 feed row "
        "(sold-by unconfirmed — marketplace risk, DECISIONS "
        "021, same as batch 23's Cetra). Re-check the $104.99 "
        "sale price after the Early Black Friday event ends "
        "Nov 8. Distinct from the set's other headsets — the "
        "Pelta is the third ASUS headset in the set (after "
        "Delta II and Delta, batches 23/25).",
    ),
    EvalProduct(
        key="lenovo-legion-tab-gen-3-eclipse-black",
        brand="Lenovo",
        model="Legion Tab Gen 3 8.8-inch Gaming Tablet",
        variant="Eclipse Black (ZAEF0068US)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Lenovo $549.99 (US product page JSON-LD read fresh "
        "2026-11-06 21:08 UTC, InStock; 8.8-inch 2.5K 165Hz, "
        "Snapdragon 8 Gen 3, 12GB LPDDR5X / 256GB UFS 4.0, "
        "Eclipse Black single colorway, Android 14 with 3 OS "
        "upgrades). Identifiers PENDING: no UPC surfaced for "
        "ZAEF0068US in any source read, so identifiers stay "
        "empty per the strict two-source rule; re-check next "
        "refresh. Not copied: nothing — no candidate code "
        "surfaced. Not the Legion Tab Gen 3 FIFA World Cup 26 "
        "Edition (ZAEF0096US, White, $569.99 — different, "
        "limited-edition tablet) or the Legion Tab Gen 5 (8.8-"
        "inch Snapdragon, $899.99 list / $699.99 sale — "
        "different, newer tablet). Excluded: the feed's dbrand "
        "skin and m2skins rows (accessories, not the tablet); "
        "the Meta Catalog feed for this query carried no direct "
        "tablet row at all. Distinct from the set's six Apple "
        "iPads — the Legion Tab Gen 3 is the first Lenovo tablet "
        "in the set and its first Android gaming tablet; Lenovo "
        "is a new brand in the set.",
    ),
    EvalProduct(
        key="lenovo-tab-plus-gen-2-celestial-white",
        brand="Lenovo",
        model="Tab Plus Gen 2 12.1-inch Tablet",
        variant="Celestial White (ZAHT0078US)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Lenovo $469.99 (US product page JSON-LD read fresh "
        "2026-11-06 21:08 UTC, InStock; feed brand_direct row "
        "agrees at $469.99; 12.1-inch 2.5K 120Hz, MediaTek "
        "Dimensity 7400, 8GB LPDDR5 / 128GB UFS 3.1, JBL 9-unit "
        "Pro speaker system, Celestial White); Newegg $299.99 "
        "(feed authorized_retailer row — suspected; not "
        "page-verified; 8GB/128GB, part ZAHT0078US). "
        "Identifiers PENDING: no UPC surfaced for ZAHT0078US in "
        "any source read, so identifiers stay empty per the "
        "strict two-source rule; re-check next refresh. Not "
        "copied: nothing — no candidate code surfaced. Not the "
        "Best Buy ZAHT0043US (8GB/256GB, $449.99 sale $379 — "
        "different storage config, different part) or the "
        "original Tab Plus (11.5-inch, 2024, different tablet). "
        "Correction vs earlier sale reports: the $269.99 sale "
        "(Slickdeals, Sep 29) and $289.99/$299.99 October sale "
        "prices are stale — the current Lenovo direct price is "
        "$469.99 on two agreeing reads (fresh page + feed), a "
        "sharp rise consistent with Lenovo's October US price "
        "hikes (PhoneArena, Oct 13); re-check the $469.99 price "
        "next refresh. Distinct from the set's iPads — the Tab "
        "Plus Gen 2 is the second Lenovo tablet in the set and "
        "its entertainment/speaker-first tablet.",
    ),
    EvalProduct(
        key="lenovo-idea-tab-pro-gen-2-cloud-grey",
        brand="Lenovo",
        model="Idea Tab Pro Gen 2 13-inch Tablet",
        variant="Cloud Grey (ZAHD0826US)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Lenovo $399.99 sale vs $549.99 list (US product page "
        "JSON-LD read fresh 2026-11-06 21:08 UTC, InStock; feed "
        "brand_direct row agrees at price $549.99 / sale "
        "$399.99; 13-inch 3.5K 144Hz, Snapdragon 8s Gen 4, 8GB / "
        "128GB, Cloud Grey); Newegg $527.99 sale vs $549.99 "
        "(feed authorized_retailer row — suspected; not "
        "page-verified; TB390FU, 8GB/128GB, part number not "
        "stated in the feed row). Identifiers PENDING: no UPC "
        "surfaced for ZAHD0826US in any source read, so "
        "identifiers stay empty per the strict two-source rule; "
        "re-check next refresh. Not copied: nothing — no "
        "candidate code surfaced. Not the Best Buy ZAHD0863US "
        "($529.99, with Tab Pen Plus — different part/bundle) "
        "or the CDW ZAHC 256GB ($606.99 — different storage "
        "config) or the Idea Tab Pro Gen 1 (12.7-inch 3K, "
        "Dimensity 8300, different tablet). Bundle conflict "
        "recorded: the feed description for ZAHD0826US says "
        "'Folio case and Pen included' while droidgadgets (Oct "
        "23) says this part ships without pen or keyboard — the "
        "pin is the part number, not the bundle claim; re-check "
        "bundle contents next refresh. Re-check the $399.99 sale "
        "price after the Early Black Friday event ends Nov 8. "
        "Distinct from the set's iPads — the Idea Tab Pro Gen 2 "
        "is the third Lenovo tablet in the set and its "
        "large-screen study tablet.",
    ),
    EvalProduct(
        key="lenovo-tab-one-luna-grey",
        brand="Lenovo",
        model="Tab One 8.7-inch Tablet",
        variant="Luna Grey (ZAF00008US)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Lenovo $149.99 sale vs $199.99 est. value (US product "
        "page JSON-LD read fresh 2026-11-06 21:08 UTC, InStock; "
        "feed brand_direct row agrees at price $199.99 / sale "
        "$149.99; 8.7-inch HD, MediaTek Helio G85, 4GB / 64GB "
        "eMMC, Luna Grey, Android 14 upgradable to 15). "
        "Identifiers PENDING: no UPC surfaced for ZAF00008US in "
        "any source read, so identifiers stay empty per the "
        "strict two-source rule; re-check next refresh. Not "
        "copied: nothing — no candidate code surfaced. Not the "
        "Best Buy ZAF00067US (SKU 6621480, $99.99 Holiday Deal — "
        "a Best Buy-specific part number for the same 4GB/64GB "
        "Luna Grey specs, not the Lenovo-direct part; the "
        "$99.99 price was NOT used) or the Staples ZAF00043US "
        "($209.99 — different part) or the Tab One LTE 128GB "
        "(different storage/connectivity). Re-check the $149.99 "
        "sale price after the Early Black Friday event ends Nov "
        "8. Distinct from the set's iPads — the Tab One is the "
        "fourth Lenovo tablet in the set and its entry-level "
        "compact tablet.",
    ),
    EvalProduct(
        key="lenovo-yoga-tab-plus-gen-2-cosmic-blue",
        brand="Lenovo",
        model="Yoga Tab Plus Gen 2 13-inch Tablet",
        variant="Cosmic Blue (ZAHX0159US)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Lenovo $799.99 sale vs $999.99 list (US product page "
        "JSON-LD read fresh 2026-11-06 21:08 UTC, InStock; feed "
        "brand_direct row agrees at price $999.99 / sale "
        "$799.99; Notebookcheck confirms the first discount, "
        "$999.99 to $799.99; 13-inch 4K PureSight Pro 144Hz, "
        "Snapdragon 8 Elite, 12GB LPDDR5X / 256GB UFS 4.0, "
        "Cosmic Blue, clamshell keyboard + Tab Pen Pro 2 "
        "included, Android 17 with 7 OS upgrades). Identifiers "
        "PENDING: no UPC surfaced for ZAHX0159US in any source "
        "read, so identifiers stay empty per the strict "
        "two-source rule; re-check next refresh. Not copied: "
        "nothing — no candidate code surfaced. Not the Yoga Tab "
        "Plus Gen 1 (12.7-inch, Snapdragon 8 Gen 3, 16GB/256GB, "
        "different tablet) or the Yoga Tab Gen 2 (11.1-inch, "
        "$729.99, different tablet) or the 'Yoga Tab Plus (Gen "
        "2) + Earbud' bundle ($1,069.98 feed row — a bundle, "
        "excluded). Re-check the $799.99 sale price after the "
        "Early Black Friday event ends Nov 8. Distinct from the "
        "set's iPads — the Yoga Tab Plus Gen 2 is the fifth "
        "Lenovo tablet in the set and its flagship creator "
        "tablet.",
    ),
    # --- Expansion batch 27 (2026-11-06, DECISIONS 049) ---
    # 155 -> 160 models. DECISIONS 049, BUILD_LOG 066.
    EvalProduct(
        key="xbox-series-x-1tb-black",
        brand="Microsoft",
        model="Xbox Series X",
        variant="1TB Disc Edition, Black (RRT-00001)",
        category="consoles",
        identifiers={"UPC": "889842640724", "MPN": "RRT-00001"},
        identifier_sources={
            "UPC": "Micro Center US spec (SKU 191429, Mfr Part # "
            "RRT-00001, UPC 889842640724, HDR Blu-ray drive) + "
            "marknet auction listing (UPC 889842640724, Brand "
            "Microsoft, Model RRT-00001) agree on the exact pair; "
            "Amazon's RRT-00001 listing corroborates the code "
            "(GTIN 00889842640724 among its listed UPCs)"
        },
        notes="Microsoft direct $799.99 (US store page JSON-LD read "
        "fresh 2026-11-06 21:13 UTC: $749.99 to $799.99 — the "
        "$749.99 end is the 1TB Digital Edition in White, the "
        "$799.99 end is the Disc Edition in Black pinned here; "
        "stock not stated in the page text). ShopCGX $799.99 "
        "(Model RRT-00001, OutOfStock) agrees on price. Stock "
        "caveat: Micro Center and ShopCGX both show RRT-00001 "
        "OutOfStock, and gamegpu (Nov 1) reports US shortages "
        "after the Digital Edition was discounted to $599.99 at "
        "Amazon/Target — re-check stock next refresh. Price "
        "history: Microsoft raised US Xbox prices Aug 1, 2026 "
        "(Series X disc $649.99 to $799.99, Digital $599.99 to "
        "$749.99; Xbox Wire Jun 25, 2026 via Push Square/Pure "
        "Xbox), so the $799.99 is the current list, not a sale. "
        "Not the 1TB Digital Edition in White ($749.99, no disc "
        "drive), the 2TB Galaxy Black Special Edition (sunset "
        "Aug 2026) or the Xbox Series X25 Limited Edition "
        "($899.99, launches Nov 13). The set's first Xbox "
        "console and its first current-gen disc console; "
        "distinct from the set's PS5 lines and Switch lines.",
        status="verified",
    ),
    EvalProduct(
        key="xbox-series-s-512gb-robot-white",
        brand="Microsoft",
        model="Xbox Series S",
        variant="512GB All-Digital, Robot White",
        category="consoles",
        identifiers={},
        status="pending",
        notes="Microsoft direct $499.99 (US store page JSON-LD read "
        "fresh 2026-11-06, $499.99 to $599.99 — the $499.99 end "
        "is the 512GB Robot White pinned here, the $599.99 end "
        "is the 1TB Robot White; stock not stated in the page "
        "text). Feed rows at $499.99 for the 512GB Digital "
        "console agree (suspected; not page-verified). Price "
        "history: the 512GB was $399.99 before Microsoft's Aug "
        "1, 2026 US increase to $499.99 (Xbox Wire Jun 25, 2026 "
        "via Pure Xbox). Identifiers PENDING: the part-number "
        "picture is conflicted and no code has two agreeing US "
        "sources — Micro Center lists the current 512GB console "
        "as Mfr Part # EP2-10050, UPC 196388421343 (single "
        "source); eBay lists the original part RRS-00001, UPC "
        "0889842651317 (single source); Amazon's Series X "
        "listing lumps 889842640731 among five unattributed "
        "UPCs; PBTech NZ lists EP2-10071, UPC 196388421541 "
        "(regional). Nothing was copied; re-check next refresh. "
        "Not the 1TB Robot White ($599.99) or the 1TB Carbon "
        "Black (different color/storage). The set's second Xbox "
        "console; distinct from the Series X (native 4K, disc "
        "drive) — the Series S is the all-digital 1440p entry "
        "console.",
    ),
    EvalProduct(
        key="xbox-wireless-headset-2024-black",
        brand="Microsoft",
        model="Xbox Wireless Headset (2024 refresh)",
        variant="Black (2024 refresh)",
        category="headphones",
        identifiers={},
        status="pending",
        notes="Microsoft direct $110.99 (US store page JSON-LD, two "
        "fresh crawls agree — 2 hours ago and 7 days ago — "
        "2026-11-06; stock not stated in the page text). Feed "
        "Microsoft row agrees at $110.99 (authorized_retailer). "
        "This is the October 2024 refresh, not the 2021 "
        "original: Dolby Atmos included, Bluetooth 5.3 (was "
        "4.2), 20-hour battery (was 15), upgraded mic with "
        "auto-mute/voice isolation, green ear-cup accents "
        "removed (Xbox Wire Oct 22, 2024; Notebookcheck). "
        "Launch price was $109.99 — the current $110.99 is $1 "
        "above launch; re-check next refresh. The feed's "
        "Microsoft $99.99 row is the stale 2021-model price and "
        "was not used. Identifiers PENDING: no MPN or UPC "
        "surfaced for the 2024 refresh in any source read — the "
        "2021 model's TLL-00001 code was not copied across, "
        "since a refresh may carry a different code; re-check "
        "next refresh. Not the Starfield Limited Edition "
        "($250.79 feed row) or the Forza Horizon 6 Limited "
        "Edition ($134.99 feed row). Distinct from the set's "
        "Xbox Stereo Headset (wired, $59.99) and from the "
        "PULSE Elite/Explore lines.",
    ),
    EvalProduct(
        key="xbox-stereo-headset-black",
        brand="Microsoft",
        model="Xbox Stereo Headset",
        variant="Black (8LI-00001)",
        category="headphones",
        identifiers={"UPC": "889842748031", "MPN": "8LI-00001"},
        identifier_sources={
            "UPC": "Ubuy listing (Model 8LI-00001, UPC "
            "889842748031) + eBay US product identifiers (MPN "
            "8LI00001, UPC 0889842748031) agree. A second eBay "
            "listing's 499007320363 is unattributed/conflicting "
            "and was excluded. MPN 8LI-00001 corroborated by "
            "Verizon + Best Buy US (Model 8LI-00001, SKU "
            "6474763) + manuals.plus"
        },
        notes="Microsoft direct $59.99 (US store page JSON-LD read "
        "fresh 2026-11-06; stock not stated in the page text). "
        "Verizon $59.99 (Model 8LI-00001/Black) agrees. The "
        "feed's Microsoft $79.99 and $74.99 rows are above the "
        "Microsoft direct price and were not used (third-party "
        "inflated rows). Wired 3.5 mm headset, single colorway, "
        "launched Sep 2021 at $59.99 (Notebookcheck) — the "
        "price is unchanged five years on. Not the 20th "
        "Anniversary Special Edition (feed rows $99.99–"
        "$119.99, different headset). Distinct from the set's "
        "Xbox Wireless Headset (2024 refresh, $110.99, "
        "wireless) — the Stereo is the wired entry headset.",
        status="verified",
    ),
    EvalProduct(
        key="microsoft-surface-laptop-13-8-8th-edition-platinum",
        brand="Microsoft",
        model="Surface Laptop, 13.8-inch (8th Edition)",
        variant="Snapdragon X2 Plus 10-core, 16GB/512GB, Platinum (EP2-59028)",
        category="laptops",
        identifiers={},
        status="pending",
        notes="Microsoft direct $1,299.99 sale vs $1,599.99 list "
        "(US store configure page, two fresh crawls 2026-11-06 "
        "agree: X2 Plus (10 Core) 'From $1,299.99' with 'Save "
        "$300.00' on the Platinum 16GB/512GB config; the "
        "$1,599.99 list is the per-config price on the 5-day-"
        "old crawl and pcdepo's 'starts at around $1,600'). "
        "Best Buy $1,199.99 sale (reg $1,600) for the same X2 "
        "Plus/16GB/512GB config, reported by 9to5Toys Nov 2 "
        "(early Black Friday) — reported, not page-verified. "
        "Base config pinned cleanly: the 13.8-inch 8th Edition "
        "introduced Jun 16, 2026 (Snapdragon X2, 120 Hz HDR "
        "PixelSense Flow, haptic touchpad, up to 20-hour "
        "battery); the US base is X2 Plus 10-core / 16GB / "
        "512GB / Platinum (pcdepo confirms the entry config; "
        "storage is 512GB minimum — the 256GB EP2-77788 is the "
        "smaller 13-inch Surface Laptop, a different model). "
        "Identifiers PENDING: MPN EP2-59028 is stated only by "
        "TheGoodGuys AU for this exact config (single non-US "
        "source), and no UPC surfaced — the MPN lives in the "
        "variant string only, per the Lenovo batch precedent; "
        "re-check next refresh. Not the X2 Elite 12-core "
        "configs, the 32GB/64GB or 1TB configs, the 15-inch "
        "8th Edition, or the 7th Edition (feed row $1,799.99, "
        "different laptop). Re-check the $1,299.99 sale price "
        "after Black Friday (Nov 27). The set's first Surface "
        "and first Microsoft laptop; distinct from the set's "
        "MacBook lines.",
    ),
    EvalProduct(
        key="garmin-vivoactive-6-slate-black",
        brand="Garmin",
        model="vívoactive 6",
        variant="Slate with Black silicone band (010-02985-00)",
        category="wearables",
        identifiers={"UPC": "753759342807", "MPN": "010-02985-00"},
        identifier_sources={
            "UPC": "Petra US (Vendor SKU 010-02985-00, UPC "
            "753759342807) + HeartRateMonitorsUSA MPN/UPC table "
            "(Slate/Black 010-02985-00 / 753759342807) agree. "
            "MPN 010-02985-00 corroborated by Dell US (Mfr Part # "
            "010-02985-00) + Best Buy US (Model 010-02985-00, SKU "
            "6628683)"
        },
        notes="Garmin direct $299.99 (US store page JSON-LD read "
        "fresh 2026-11-06; the page shows the Lunar Gold variant "
        "but the price is uniform $299.99 across all four colors). "
        "Dell $299.99 (Mfr Part # 010-02985-00) agrees but shows "
        "Temporarily Out of Stock; Best Buy $299.99 (Model "
        "010-02985-00) agrees. 42.2 mm AMOLED fitness smartwatch, "
        "up to 11 days battery, launched 2025. Not the Lunar Gold "
        "/ Bone (010-02985-01, UPC 753759342814), Metallic Jasper "
        "Green (010-02985-02, UPC 753759342821) or Pink Dawn "
        "(010-02985-03, UPC 753759342838) colorways, and not the "
        "vívoactive 5 (previous generation). The set's first "
        "Garmin entry; distinct from the set's Apple Watch lines.",
        status="verified",
    ),
    EvalProduct(
        key="garmin-venu-4-45mm-silver-gray",
        brand="Garmin",
        model="Venu 4",
        variant="45mm, Silver stainless steel bezel with Silver Gray silicone band (010-03014-01)",
        category="wearables",
        identifiers={"UPC": "753759342883", "MPN": "010-03014-01"},
        identifier_sources={
            "UPC": "Petra US (Vendor SKU 010-03014-01, UPC "
            "753759342883, GTIN 00753759342883) + "
            "HeartRateMonitorsUSA MPN/UPC table (45mm Silver / "
            "Silver Gray 010-03014-01 / 753759342883) agree. MPN "
            "corroborated by Abt US (Model 010-03014-01) + the "
            "Garmin US store URL itself (pn/010-03014-01)"
        },
        notes="Garmin direct $549.99 (US store page JSON-LD read "
        "fresh 2026-11-06 — the page description is the pinned "
        "variant exactly, Silver with Silver Gray Silicone Band). "
        "Dell feed row shows $499.99 sale vs $549.99 list for "
        "this exact variant (early Black Friday pricing, "
        "suspected — not page-verified). Launched Sep 22, 2025 "
        "at $549.99 (Garmin press release); 45 mm AMOLED, "
        "stainless steel bezel, ECG app, LED flashlight, up to "
        "12 days battery. Not the 41 mm Venu 4 (different size, "
        "same $549.99), the Slate/Black silicone 010-03014-00 "
        "(UPC 753759342876), the Silver/Citron 010-03014-02, or "
        "the Slate/Black + Brown leather 010-03014-03 ($599.99). "
        "The set's first Venu; distinct from the set's "
        "vívoactive 6 (entry fitness watch, $299.99).",
        status="verified",
    ),
    EvalProduct(
        key="garmin-forerunner-570-42mm-raspberry",
        brand="Garmin",
        model="Forerunner 570",
        variant="42mm, Raspberry Aluminum with Translucent Bone/Mango band (010-02970-02)",
        category="wearables",
        identifiers={"UPC": "753759349820", "MPN": "010-02970-02"},
        identifier_sources={
            "UPC": "Target US (TCIN 94760143, UPC 753759349820, "
            "$549.99, In Stock) + Selenal.lv (part code "
            "010-02970-02, Barcode 753759349820) agree; "
            "CycleSuperStore.ie barcode list confirms the "
            "-00/-01/-02 mapping (753759349806 / 753759349813 / "
            "753759349820). MPN corroborated by the Garmin US "
            "store URL (pn/010-02970-02) + Meta Catalog feed row "
            "for this exact variant"
        },
        notes="Garmin direct $549.99 (US store page JSON-LD read "
        "fresh 2026-11-06 — the 42 mm page shows the Slate Gray "
        "variant but the price is uniform $549.99 across sizes "
        "and colors; the Meta Catalog feed carries a $549.99 "
        "Garmin row for this exact Raspberry variant, "
        "pn/010-02970-02). Target $549.99 In Stock agrees. "
        "Launched May 21, 2025 at $549.99 alongside the "
        "Forerunner 970; 42 mm AMOLED, multi-band GPS, speaker "
        "and mic, up to 10 days battery — no offline maps and no "
        "ECG, which stay exclusive to the 970. Not the 47 mm "
        "570 (different size, same $549.99), the Slate Gray "
        "010-02970-00 or Cloud Blue 010-02970-01 colorways, or "
        "the Forerunner 970 ($749.99, titanium/sapphire/maps). "
        "The set's first Forerunner.",
        status="verified",
    ),
    EvalProduct(
        key="garmin-edge-1050",
        brand="Garmin",
        model="Edge 1050",
        variant="Device only, Black (010-02890-00)",
        category="cycling-computers",
        identifiers={"UPC": "753759336288", "MPN": "010-02890-00"},
        identifier_sources={
            "UPC": "HeartRateMonitorsUSA (010-02890-00 / "
            "753759336288) + 6ave (UPC 753759336288, MPN "
            "010-02890-00) + The Pro's Closet (mpn 010-02890-00, "
            "upc 753759336288) + SunnySports (MFR 010-02890-00, "
            "UPC 753759336288) agree; the Meta Catalog feed row "
            "for this device carries GTIN 753759336288. The "
            "010-02890-01 bundle's EAN 0753759336295 is a "
            "different code and was excluded"
        },
        notes="Garmin direct $699.99 (US store page JSON-LD read "
        "fresh 2026-11-06). Best Buy feed row $699.99 sale "
        "(list $704.95) agrees; BikeTiresDirect $699.99 (Mfg "
        "PartNum 010-02890-00) agrees. Launched Jun 2024 at "
        "$699.99; 3.5-inch 480x800 touchscreen, 64 GB, speaker "
        "and bike bell, Garmin Pay, up to 20 hours demanding "
        "use / 60 hours battery saver. The Edge 1060 launched "
        "Oct 20, 2026 at $799.99 and replaces the 1050 as "
        "Garmin's premium computer, but the 1050 is still "
        "listed and sold at $699.99 at Garmin direct and "
        "multiple US bike shops on 2026-11-06 — not "
        "discontinued. Not the 010-02890-01 sensor bundle "
        "(different MPN/EAN) or the Edge 1040 Solar ($699.99, "
        "previous generation). The set's first cycling computer "
        "and first entry in the new \"cycling-computers\" "
        "category.",
        status="verified",
    ),
    EvalProduct(
        key="garmin-fenix-9-47mm-titanium-pebble-gray",
        brand="Garmin",
        model="fēnix 9",
        variant="47mm, Titanium with Pebble Gray silicone band (010-04762-00)",
        category="wearables",
        identifiers={},
        status="pending",
        notes="Garmin direct $999.99 (US store page JSON-LD read "
        "fresh 2026-11-06 — the page description is the pinned "
        "variant exactly, Titanium with Pebble Gray Silicone "
        "Band). Abt $999.99 (Model 010-04762-00, InStock) and "
        "NFM $999.99 agree; the Meta Catalog feed carries five "
        "$999.99 rows naming MPN 010-04762-00. Announced Aug 25, "
        "2026, orderable Aug 28; 47 mm AMOLED (twice as bright "
        "as fēnix 8), titanium bezel, sapphire lens, leakproof "
        "metal buttons, LED flashlight, 64 GB, up to 16 days "
        "battery. Identifiers PENDING: MPN 010-04762-00 is "
        "confirmed by Garmin US + Abt + RA Cycles, but no UPC "
        "surfaced in any source read — the fēnix 9 is ten weeks "
        "old and retailer UPC fields are still blank; the MPN "
        "lives in the variant string only, per the Surface "
        "Laptop (batch 27) precedent; re-check next refresh. "
        "Not the 43 mm or 51 mm fēnix 9 ($999.99 / $1,099.99), "
        "the Carbon Gray DLC Titanium 010-04762-10 ($1,049.99), "
        "or any fēnix 9 Pro line ($1,099.99+, full titanium case "
        "and/or inReach/solar). The set's first fēnix; distinct "
        "from the set's Venu 4 and Forerunner 570.",
    ),
    # --- Expansion batch 29 (2026-11-06, DECISIONS 051) ---
    # 165 -> 170 models. DECISIONS 051, BUILD_LOG 068.
    EvalProduct(
        key="lenovo-legion-tab-gen-5-eclipse-black",
        brand="Lenovo",
        model="Legion Tab Gen 5 8.8-inch Gaming Tablet",
        variant="Eclipse Black (ZAH20126US)",
        category="tablets",
        identifiers={"UPC": "199275342448", "MPN": "ZAH20126US"},
        identifier_sources={
            "UPC": "B&H Photo US (Model ZAH20126US, UPC "
            "199275342448, page read fresh 2026-11-06) + "
            "TempDeals/edealinfo (tags ZAH20126US | "
            "199275342448; deal URL "
            "edealinfo.com/d/00199275342448) agree. MPN "
            "ZAH20126US corroborated by Lenovo US (page title), "
            "Slickdeals (ZAH20126US, Oct 31) and the Meta "
            "Catalog feed brand_direct row URL "
            "(/zah20126us)"
        },
        status="verified",
        notes="Lenovo $699.99 sale vs $899.99 list (US product page "
        "JSON-LD read fresh 2026-11-06 21:26 UTC, InStock; feed "
        "brand_direct row agrees at price $899.99 / sale "
        "$699.99; 8.8-inch 3K 165Hz, Snapdragon 8 Elite Gen 5, "
        "12GB LPDDR5T / 256GB UFS 4.1, Eclipse Black single US "
        "colorway, folio case + 68W charger included, Android "
        "16); B&H $799.99 sale vs $899.99 list (page read fresh "
        "2026-11-06 21:27 UTC, InStock — a different, smaller "
        "discount than Lenovo direct). Re-check the $699.99 sale "
        "price after the Early Black Friday event ends Nov 8. "
        "Not the FIFA World Cup 26 Edition (ZAEF0096US, White, "
        "$569.99 — different, limited-edition tablet), the "
        "Glacier White or Surge green colorways (not sold in "
        "the US — Notebookcheck: single Eclipse Black US "
        "colorway) or the Legion Tab Gen 3 (ZAEF0068US, "
        "Snapdragon 8 Gen 3, $549.99 — previous generation, "
        "already in the set). Excluded: the $598.49 Slickdeals "
        "price (Oct 31 — requires stacking two eCoupons, "
        "DEALDAYSLIVE + EXTRAFIVE, at checkout, not a clean "
        "sale price) and the $680/$679.99 September sale prices "
        "(stale — the list rose $849.99 to $899.99 in October, "
        "PhoneArena Oct 13). Distinct from the set's Legion Tab "
        "Gen 3 — the Gen 5 is the sixth Lenovo tablet in the "
        "set and its flagship gaming tablet.",
    ),
    EvalProduct(
        key="lenovo-yoga-tab-gen-2-cosmic-blue",
        brand="Lenovo",
        model="Yoga Tab Gen 2 11.1-inch Tablet",
        variant="Cosmic Blue (ZAJ00250US)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Lenovo $599.99 sale vs $729.99 list (US product page "
        "JSON-LD read fresh 2026-11-06 21:26 UTC, InStock; feed "
        "brand_direct row agrees at price $729.99 / sale "
        "$599.99; 11.1-inch 4K PureSight Pro 144Hz, MediaTek "
        "Dimensity 9500s, 8GB LPDDR5X / 256GB UFS 4.1, Cosmic "
        "Blue, Tab Pen Pro 2 + 2-in-1 Keyboard Pack included, "
        "Android 17 with 7 OS upgrades, 11,000mAh). "
        "Identifiers PENDING: no UPC surfaced for ZAJ00250US in "
        "any source read, so identifiers stay empty per the "
        "strict two-source rule; re-check next refresh. Not "
        "copied: nothing — no candidate code surfaced. The "
        "model number is TB711FU (GSMArena / PSREF). Not the "
        "Yoga Tab Plus Gen 2 (13-inch, Snapdragon 8 Elite, "
        "$799.99 sale — already in the set) or the Yoga Tab "
        "Gen 1 (11.1-inch, Snapdragon 8 Gen 3, $659.99 — "
        "previous generation, superseded, not added per the "
        "batch 28 Fenix 8 precedent) or the 'Yoga Tab (Gen 2) "
        "+ Earbud' bundle ($639.98 feed row — a bundle, "
        "excluded). The ~$582 Notebookcheck price (Oct 24, 20% "
        "off) is stale vs the current $599.99. Lenovo-only in "
        "the US — no second retailer quote exists (no retailer "
        "row in the feed). Re-check the $599.99 sale price "
        "after the Early Black Friday event ends Nov 8. "
        "Distinct from the set's Yoga Tab Plus Gen 2 — the "
        "Yoga Tab Gen 2 is the seventh Lenovo tablet in the "
        "set and its mid-size creator tablet.",
    ),
    EvalProduct(
        key="lenovo-idea-tab-luna-grey",
        brand="Lenovo",
        model="Idea Tab 11-inch Tablet",
        variant="Luna Grey (ZAFR0923US)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Lenovo $269.99 (US product page JSON-LD read fresh "
        "2026-11-06 21:26 UTC, InStock; feed brand_direct row "
        "agrees at $269.99; 11-inch 2.5K 90Hz, MediaTek "
        "Dimensity 6300, 4GB / 128GB, Luna Grey, Android 15 "
        "with 2 OS upgrades; Tab Pen Plus sold separately). "
        "Identifiers PENDING: no UPC surfaced for ZAFR0923US in "
        "any source read, so identifiers stay empty per the "
        "strict two-source rule; re-check next refresh. Not "
        "copied: nothing for this part — the Amazon UPCs "
        "199271882283 (ZAFR0920US, 8GB/256GB with pen + folio), "
        "199271888728 (ZAFR0928US, 8GB/128GB with pen) and "
        "199271882306 (ZAFR0925US, 4GB/128GB with pen + folio) "
        "are all different parts and were NOT copied onto "
        "ZAFR0923US. The 4GB tier is $269.99 and the 8GB tier "
        "$339.99 (PhoneArena, Oct 26 — the Idea Tab rose from "
        "$239.99/$309.99 to $269.99/$339.99); the 8GB part is "
        "ZAFR0928US at $339.99 (feed brand_direct row), a "
        "different part. Not the Staples ZAFR0912US ($269.99 — "
        "a different part, TB336FU 128GB) or the Idea Tab Pro "
        "Gen 2 (13-inch, Snapdragon 8s Gen 4 — already in the "
        "set) or the Tab K11 Gen 2 (the Idea Tab's business-"
        "channel twin, TB336FU — same hardware family under a "
        "different channel name, not added separately). "
        "Lenovo-only in the US — no second retailer quote "
        "exists for this part. Re-check the $269.99 price next "
        "refresh (third price rise for this tablet in 2026). "
        "Distinct from the set's Idea Tab Pro Gen 2 — the Idea "
        "Tab is the eighth Lenovo tablet in the set and its "
        "entry-level student tablet.",
    ),
    EvalProduct(
        key="lenovo-idea-tab-plus-cloud-grey",
        brand="Lenovo",
        model="Idea Tab Plus 12.1-inch Tablet",
        variant="Cloud Grey (ZAG71084US)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Lenovo $369.99 (US product page JSON-LD read fresh "
        "2026-11-06 21:26 UTC, InStock; feed brand_direct row "
        "agrees at $369.99; 12.1-inch 2.5K 90Hz, MediaTek "
        "Dimensity 6400, 6GB / 128GB, Cloud Grey, Android 15); "
        "Newegg $279.00 (feed authorized_retailer row — "
        "suspected; not page-verified; part ZAG71084US stated "
        "in the listing, 6GB/128GB). Identifiers PENDING: no "
        "UPC surfaced for ZAG71084US in any source read, so "
        "identifiers stay empty per the strict two-source rule; "
        "re-check next refresh. Not copied: nothing — no "
        "candidate code surfaced. Correction vs earlier "
        "reports: the $339.99 PhoneArena figure (Oct 13) was "
        "the 8GB config — the current Lenovo-direct part is "
        "the 6GB ZAG71084US at $369.99. Not the 8GB/128GB "
        "ZAG70917US (Luna Grey, pen + folio — $279-$294 at "
        "retailers) or the Best Buy ZAG70921US (8GB/128GB, "
        "$279.99 sale vs $369.99 comp value) or the 12GB/256GB "
        "ZAG70922US — all different parts/configs — or the Tab "
        "Plus Gen 2 (12.1-inch, Dimensity 7400, JBL 9-unit "
        "speakers — already in the set) or the Idea Tab Pro "
        "Gen 2 (13-inch — already in the set). Re-check the "
        "$369.99 price next refresh. Distinct from the set's "
        "Tab Plus Gen 2 and Idea Tab Pro Gen 2 — the Idea Tab "
        "Plus is the ninth Lenovo tablet in the set and its "
        "lightweight large-screen student tablet.",
    ),
    EvalProduct(
        key="asus-rog-swift-oled-pg27ucdm-black",
        brand="ASUS",
        model="ROG Swift OLED PG27UCDM 27-inch 4K 240Hz Gaming Monitor",
        variant="Black (90LM0B30-B019B2)",
        category="monitors",
        identifiers={},
        status="pending",
        notes="ASUS $1,099.00 (eShop USA page read fresh "
        "2026-11-06 21:29 UTC, InStock; feed brand_direct rows "
        "agree at $1,099 — eShop row + ROG US page row; "
        "26.5-inch 4K Tandem QD-OLED, 240Hz, 0.03ms, DP 2.1a "
        "UHBR20, USB-C 90W, Dolby Vision, DisplayHDR 400 True "
        "Black, 99% DCI-P3, 3-year warranty incl. burn-in); "
        "Newegg $1,099.00 sale vs $1,199.99 list (feed "
        "authorized_retailer row — suspected; not "
        "page-verified; agrees with ASUS eShop). Identifiers "
        "PENDING: the candidate UPC 197105815193 is not tied "
        "to the US part 90LM0B30-B019B2 by a second US source — "
        "it appears in the ASUS brochure PDF (with EAN "
        "4711387815236) for the EU part 90LM0B30-B01971 and on "
        "Tanotis/eBay/Ubuy listings for PG27UCDM generally, "
        "but no source states it for the B019B2 part "
        "specifically, so identifiers stay empty per the "
        "strict two-source rule (same call as batch 25's "
        "PG32UCWM, whose B&H-only UPC stayed unrecorded); "
        "re-check next refresh. Not copied: 197105815193 "
        "(candidate UPC, part tie unconfirmed); 4711387815236 "
        "(EU EAN for the B01971 part). Not the PG27UCWM "
        "(27-inch 4K 240Hz Tandem RGB OLED, $1,699 — already "
        "in the set), the PG32UCWM (32-inch, $1,399 — already "
        "in the set), the PG27UCDMR ($1,299, Out of Stock — "
        "different monitor) or the PG27AQDM-R (QHD, $599 sale "
        "— different monitor). Excluded: the $949 ROG row and "
        "the $1,199 shop.asus.com row (stale / other storefront "
        "vs the $1,099 eShop + ROG page + Newegg agreement), "
        "the AirVision M1 bundle ($100 add-on), and the CDW "
        "$1,199 / Macy's $1,124.99 sale rows (not used). "
        "Distinct from the set's other ASUS monitors — the "
        "PG27UCDM is the third ASUS monitor in the set and its "
        "27-inch 4K Tandem QD-OLED flagship.",
    ),
    EvalProduct(
        key="samsung-galaxy-watch9-40mm-graphite",
        brand="Samsung",
        model="Galaxy Watch9",
        variant="Graphite, 40mm, Bluetooth (SM-L340NZKAXAA)",
        category="wearables",
        identifiers={},
        status="pending",
        notes="Samsung $379.99 (US buy page JSON-LD read fresh "
        "2026-11-06 21:35 UTC, InStock; feed brand_direct row "
        "agrees at $379.99; 40mm, Snapdragon Wear Elite, 390mAh, "
        "Sport Band S/M, Wear OS 7, 3,000-nit display); Best Buy "
        "$379.99 (page read fresh 2026-11-06 21:35 UTC, InStock, "
        "Sold by Best Buy, SKU 6684173, Model SM-L340NZKAXAA); "
        "Abt $379.99 (search-index read, SM-L340NZKAXAA). "
        "Identifiers PENDING: the candidate UPC 198957310546 "
        "appears only in Samsung's own Wearables MSRP Price "
        "List (July 2026) — no second independent source was "
        "found (the Best Buy page text states no UPC; web "
        "search returns nothing else for the code), so "
        "identifiers stay empty per the strict two-source rule "
        "(same call as batch 2's Watch Ultra 4). Not copied: "
        "198957310546 (single-source candidate). Not the 44mm "
        "Graphite SM-L350NZKAXAA ($409.99), the 40mm LTE "
        "SM-L345UZKAXAA ($429.99), or the Cream SM-L340NZEAXAA "
        "(UPC 198957310430, different color). The $299.99 / "
        "$349.99 figures in older coverage are Watch8 prices, "
        "not Watch9 (Watch9 launched Aug 7, 2026 at $379.99). "
        "Re-check the UPC next refresh. Distinct from the set's "
        "Apple, Google and Garmin watches — the Galaxy Watch9 "
        "is the first Samsung wearable in the set and its "
        "current mainstream smartwatch.",
    ),
    EvalProduct(
        key="samsung-galaxy-watch8-classic-46mm-black",
        brand="Samsung",
        model="Galaxy Watch8 Classic",
        variant="Black, 46mm, Wi-Fi/Bluetooth (SM-L500NZKAXAA)",
        category="wearables",
        identifiers={"UPC": "198957093562", "MPN": "SM-L500NZKAXAA"},
        identifier_sources={
            "UPC": "Samsung Wearables MSRP Price Lists (Sep 2025, "
            "Dec 2025, Mar 2026 and Jun 2026 editions all agree "
            "for SM-L500NZKAXAA, Galaxy Watch8 Classic BT - "
            "Black, $499.99, UPC 198957093562) + eBay product "
            "identifiers (GTIN 0198957093562, the same code) "
            "agree"
        },
        notes="Samsung $499.99 (US buy page JSON-LD read fresh "
        "2026-11-06 21:35 UTC, InStock; feed brand_direct row "
        "agrees at $499.99; 46mm, rotating bezel, Exynos W1000, "
        "445mAh, 64GB, stainless steel); Best Buy $499.99 "
        "(search-index page read, new-unit page SKU 13170487, "
        "Model SM-L500NZKAXAA). Note: memeburn reported $419.99 "
        "at Samsung on Sep 24, 2026 — the fresh page read today "
        "says $499.99, so $419.99 looks like an ended sale; "
        "re-check next refresh. Not the LTE SM-L505UZKAXAA "
        "($549.99, UPC 198957093579) or the White SM-L500NZWAXAA "
        "(UPC 198957106224). There is no Watch9 Classic "
        "(Samsung confirmed no Classic in the 2026 lineup), so "
        "the Watch8 Classic stays the current Classic. Distinct "
        "from the set's Galaxy Watch9 — the Watch8 Classic is "
        "the first Samsung Classic watch in the set and its "
        "rotating-bezel flagship.",
        status="verified",
    ),
    EvalProduct(
        key="samsung-galaxy-watch-ultra2-47mm-titanium-silver",
        brand="Samsung",
        model="Galaxy Watch Ultra2",
        variant="Titanium Silver, 47mm, LTE (SM-L715UZSAXAA)",
        category="wearables",
        identifiers={"UPC": "198957393730", "MPN": "SM-L715UZSAXAA"},
        identifier_sources={
            "UPC": "Samsung Wearables MSRP Price List (July 2026) "
            "states UPC 198957393730 for SM-L715UZSAXAA, Galaxy "
            "Watch Ultra 2 - Titanium Silver, $699.99 + "
            "T-Mobile for Business product URL carries the same "
            "code as its sku (product_default_group...198957393730)"
            " — the same URL-sku pattern as the Buds4 Pro "
            "precedent (DECISIONS 009)"
        },
        notes="Samsung $699.99 (US buy page JSON-LD read fresh "
        "2026-11-06 21:35 UTC, InStock; feed brand_direct row "
        "agrees at $699.99; 47mm titanium, 800mAh, 5,000-nit "
        "display, Snapdragon Wear Elite, Marine Band, IP69K / "
        "10 ATM); Best Buy $699.99 (search-index page read, "
        "SKU 6684221, Model SM-L715UZSAXAA — the feed's $737.52 "
        "row conflicts and was excluded as stale); Abt $699.99 "
        "(search-index read, SM-L715UZSAXAA). Not the Titanium "
        "Gray SM-L715UZKAXAA (UPC 198957393792, $699.99) or the "
        "original Galaxy Watch Ultra SM-L705 (2024, $649.99 list, "
        "now $449.99 sale — previous generation). Distinct from "
        "the set's Galaxy Watch9 and Watch8 Classic — the Watch "
        "Ultra2 is the first Samsung Ultra watch in the set and "
        "its rugged flagship.",
        status="verified",
    ),
    EvalProduct(
        key="samsung-galaxy-tab-s11-128gb-gray",
        brand="Samsung",
        model="Galaxy Tab S11",
        variant="Gray, 11-inch, 128GB, Wi-Fi (SM-X730NZAAXAR)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Samsung $999.99 (US buy page JSON-LD read fresh "
        "2026-11-06 21:35 UTC, InStock — the page read was the "
        "Silver variant at $999.99; Gray matches at Best Buy and "
        "NFM; 11-inch Dynamic AMOLED 2X 120Hz, Dimensity 9400+, "
        "12GB/128GB, S Pen included, IP68); Best Buy $999.99 "
        "(page read fresh 2026-11-06 21:35 UTC, InStock, Sold by "
        "Best Buy, SKU 6641206, Model SM-X730NZAAXAR); NFM "
        "$999.99 (feed authorized_retailer row); Macy's $899.99 "
        "(feed authorized_retailer row — suspected; not "
        "page-verified). Identifiers PENDING: no UPC surfaced "
        "for SM-X730NZAAXAR in any source read — Samsung's April "
        "2026 tablet MSRP PDF lists the Enterprise 128GB "
        "(SM-X730NZAAN20, UPC 198957257360) and the 256GB Gray "
        "(SM-X730NZAEXAR, UPC 198957230189) but not the consumer "
        "128GB Gray — so identifiers stay empty per the strict "
        "two-source rule. Not copied: 198957230189 (256GB) or "
        "198957257360 (Enterprise); the 810210911580 / "
        "810210913805 UPCs belong to Best Buy bundle listings for "
        "the Canada part SM-X730NZAAXAC with an SD card, a "
        "different part. The $799.99 launch price rose to "
        "$899.99 (Apr 2026) and $999.99 now; the $659 sale price "
        "is an Amazon-only deal (excluded, no Amazon touch). Not "
        "the 256GB ($1,099.99) or 512GB ($1,299.99) or the Tab "
        "S11 Ultra ($1,199.99+). Re-check the UPC next refresh. "
        "Distinct from the set's Lenovo tablets — the Galaxy Tab "
        "S11 is the first Samsung tablet in the set and its "
        "flagship 11-inch tablet.",
    ),
    EvalProduct(
        key="samsung-galaxy-tab-s10-fe-128gb-gray",
        brand="Samsung",
        model="Galaxy Tab S10 FE",
        variant="Gray, 10.9-inch, 128GB, Wi-Fi (SM-X520NZAAXAR)",
        category="tablets",
        identifiers={"UPC": "887276992266", "MPN": "SM-X520NZAAXAR"},
        identifier_sources={
            "UPC": "Samsung Galaxy Tablet MSRP Price Lists (Mar, "
            "Jun, Sep, Dec 2025 and Mar, Apr 2026 editions all "
            "agree: SM-X520NZAAXAR, Galaxy Tab S10 FE 8+128GB "
            "(Wi-Fi) Gray, UPC 887276992266) + manuals.plus "
            "mirror of Samsung's June 2025 list (same code)"
        },
        notes="Samsung $549.99 (US buy page JSON-LD, search-index "
        "read 2026-11-06, InStock; 10.9-inch WUXGA+ 90Hz, Exynos "
        "1580, 8GB/128GB, S Pen included, IP68); Best Buy "
        "$549.99 (page read fresh 2026-11-06 21:36 UTC, InStock, "
        "Sold by Best Buy, SKU 6618942, Model SM-X520NZAAXAR); "
        "BJ's $529.99 (feed authorized_retailer row). Note: "
        "Samsung's MSRP list still shows $499.99 (May 2026) but "
        "the current Samsung US and Best Buy price is $549.99 — "
        "the list price rose; re-check next refresh. Excluded: "
        "Target's $449.99 / $394.99 'Global Model' row (non-US, "
        "DECISIONS 021) and the 5G SM-X528UZAA ($685.99) and "
        "256GB SM-X520NZAEXAR ($589.99 MSRP) — different "
        "configs. Not the Tab S10 FE+ 13.1-inch (SM-X620NZAAXAR, "
        "$649.99 MSRP). Distinct from the set's Galaxy Tab S11 — "
        "the Tab S10 FE is the second Samsung tablet in the set "
        "and its mid-range FE tablet.",
        status="verified",
    ),
    # --- Expansion batch 31 (added 2026-11-06, continuous expansion
    # per DECISIONS 027, no per-batch approval). 175 -> 180 models.
    # DECISIONS 053, BUILD_LOG 070.
    EvalProduct(
        key="samsung-galaxy-tab-s11-ultra-256gb-gray",
        brand="Samsung",
        model="Galaxy Tab S11 Ultra",
        variant="Gray, 14.6-inch, 256GB, Wi-Fi (SM-X930NZAAXAR)",
        category="tablets",
        identifiers={},
        status="pending",
        notes="Samsung $1,299.99 (US buy page JSON-LD read fresh "
        "2026-11-06 21:42 UTC, InStock; 14.6-inch Dynamic AMOLED 2X, "
        "Dimensity 9400+, 12GB/256GB, S Pen included, IP68, 11,600mAh, "
        "up to 23 hours video); Best Buy $1,299.99 (page read fresh "
        "2026-11-06 21:42 UTC, InStock, Sold by Best Buy, SKU 6641197, "
        "Model SM-X930NZAAXAR); Quill $1,320.99 (page read fresh "
        "2026-11-06 21:44 UTC, Out of stock, Model SM-X930NZAAXAR). "
        "Identifiers PENDING: the candidate UPC 198957230080 appears "
        "only in Samsung's own Galaxy Tablet MSRP Price Lists (Sep, Dec "
        "2025 and Mar, May 2026 editions all agree: SM-X930NZAAXAR, "
        "Galaxy Tab S11 Ultra 12+256GB (Wi-Fi) Gray, UPC 198957230080) "
        "— no second independent source was found (the Quill page "
        "states no UPC; web search returns nothing else for the code), "
        "so identifiers stay empty per the strict two-source rule — "
        "same call as batch 30's Watch9. Not copied: 198957230080 "
        "(single-source candidate). Note: the $1,199.99 MSRP (Samsung's "
        "May 2026 list) is stale vs the current $1,299.99 at Samsung US "
        "and Best Buy — the list price rose; re-check next refresh. "
        "Excluded: the feed's Quill $1,281.99 row (stale vs the fresh "
        "$1,320.99 page read) and the Newegg $1,129.99 / $1,944.52 rows "
        "(unverified marketplace-style listings). Not the 512GB Gray "
        "(SM-X930NZAEXAR, UPC 198957230066, $1,399.99 MSRP) or the 1TB "
        "Silver (SM-X930NZSIXAR, $1,899.99). Distinct from the set's "
        "Galaxy Tab S11 — the Tab S11 Ultra is Samsung's flagship "
        "14.6-inch tablet.",
    ),
    EvalProduct(
        key="samsung-galaxy-tab-a11-plus-128gb-gray",
        brand="Samsung",
        model="Galaxy Tab A11+",
        variant="Gray, 11-inch, 128GB, Wi-Fi (SM-X230NZAIXAR)",
        category="tablets",
        identifiers={"UPC": "198957270390", "MPN": "SM-X230NZAIXAR"},
        identifier_sources={
            "UPC": "Samsung Galaxy Tablet MSRP Price Lists (Dec 2025 "
            "and May 2026 editions agree: SM-X230NZAIXAR, Galaxy Tab "
            "A11+ 6+128GB (Wi-Fi) Gray, UPC 198957270390) + eBay "
            "product identifiers (MPN SM-X230NZAIXAR, UPC 198957270390, "
            "Gray, 128GB) agree"
        },
        notes="Samsung $299.99 (US buy page JSON-LD read fresh "
        "2026-11-06 21:42 UTC, InStock; 11-inch WUXGA 90Hz, MediaTek "
        "Dimensity 7300, 6GB/128GB, microSD to 2TB, quad speakers, "
        "Android 16); Best Buy $299.99 (page read fresh 2026-11-06 "
        "21:43 UTC, InStock, Sold by Best Buy, SKU 6665037, Model "
        "SM-X230NZAIXAR); Walmart $299.99 (feed authorized_retailer "
        "row — suspected; not page-verified). Note: the $249.99 MSRP "
        "(Samsung's Dec 2025 / May 2026 lists; NotebookCheck's Jan "
        "2026 launch coverage) is stale vs the current $299.99 at "
        "Samsung US and Best Buy — the list price rose; re-check next "
        "refresh. Not the 256GB Gray (SM-X230NZATXAR, UPC 198957270383, "
        "$329.99 MSRP) or the 5G Unlocked (SM-X238UZAAXAA, $279.99 "
        "MSRP) or the Silver (SM-X230NZSIXAR). Distinct from the set's "
        "Galaxy Tab S11 / S10 FE lines — the Tab A11+ is Samsung's "
        "entry-level 11-inch tablet.",
        status="verified",
    ),
    EvalProduct(
        key="samsung-galaxy-tab-s10-fe-plus-128gb-gray",
        brand="Samsung",
        model="Galaxy Tab S10 FE+",
        variant="Gray, 13.1-inch, 128GB, Wi-Fi (SM-X620NZAAXAR)",
        category="tablets",
        identifiers={"UPC": "887276992563", "MPN": "SM-X620NZAAXAR"},
        identifier_sources={
            "UPC": "Samsung Galaxy Tablet MSRP Price Lists (Mar, Jun, "
            "Sep, Dec 2025 and Mar, Apr, May 2026 editions all agree: "
            "SM-X620NZAAXAR, Galaxy Tab S10 FE+ 8+128GB (Wi-Fi) Gray, "
            "UPC 887276992563) + manuals.plus mirror of Samsung's June "
            "2025 list (same code)"
        },
        notes="Samsung $699.99 (US buy page JSON-LD read fresh "
        "2026-11-06 21:42 UTC, InStock; 13.1-inch WQXGA 90Hz, Exynos "
        "1580, 8GB/128GB, S Pen included, IP68); Best Buy $699.99 "
        "(search-index page read, InStock, Sold by Best Buy, SKU "
        "6618945, Model SM-X620NZAAXAR); bkstr $699.99 (feed "
        "authorized_retailer row — suspected; not page-verified). "
        "Note: the $649.99 MSRP (Samsung's May 2026 list) is stale vs "
        "the current $699.99 at Samsung US and Best Buy — the list "
        "price rose; re-check next refresh. Excluded: the antonline "
        "marketplace rows ($549.99 / $705.41, Best Buy marketplace "
        "seller, DECISIONS 021) and the shopabunda $540 'International "
        "Model' row (non-US, DECISIONS 021). Not the 256GB Gray "
        "(SM-X620NZAEXAR, UPC 887276992556, $819.99) or the Blue "
        "(SM-X620NLBAXAR) or Silver (SM-X620NZSAXAR). Distinct from "
        "the set's Galaxy Tab S10 FE — the FE+ is the 13.1-inch big-screen "
        "FE tablet.",
        status="verified",
    ),
    EvalProduct(
        key="garmin-forerunner-165-black-slate-gray",
        brand="Garmin",
        model="Forerunner 165",
        variant="Black with Slate Gray band, non-Music (010-02863-20)",
        category="wearables",
        identifiers={"UPC": "753759326593", "MPN": "010-02863-20"},
        identifier_sources={
            "UPC": "Snapklik (Model 010-02863-20, UPC 753759326593) + "
            "Cycle Superstore barcodes (753759326593) + Evolution Bikes "
            "(SKU 010-02863-20, EAN 753759326593) agree"
        },
        notes="Garmin direct $249.99 (US store page JSON-LD read fresh "
        "2026-11-06 21:44 UTC; the page read states no availability — "
        "stock unconfirmed at Garmin direct); Crutchfield $249.99 "
        "(search-index page read, InStock, Black with Slate Gray band); "
        "Running Warehouse $249.99 (search-index page read, In Stock "
        "4+, Stock # 010-02863-20). 43mm AMOLED GPS running watch, "
        "1.2-inch display, up to 11 days smartwatch battery, launched "
        "Feb 2024. Not the Music edition (010-02863-30, $299.99) or "
        "the Mist Gray (010-02863-21) — different SKUs. Distinct from "
        "the set's Forerunner 570 — the 165 is Garmin's entry-level "
        "AMOLED running watch.",
        status="verified",
    ),
    EvalProduct(
        key="garmin-edge-850",
        brand="Garmin",
        model="Edge 850",
        variant="Device only, Black (010-03023-00)",
        category="cycling-computers",
        identifiers={"UPC": "753759356644", "MPN": "010-03023-00"},
        identifier_sources={
            "UPC": "HeartRateMonitorsUSA MPN/UPC table (Edge 850, "
            "010-03023-00, UPC 753759356644, $599.99) + The Pro's "
            "Closet (mpn 010-03023-00, upc 753759356644) agree. MPN "
            "010-03023-00 corroborated by Garmin US (product URL "
            "pn/010-03023-00) + Best Buy US (Model 010-03023-00, SKU "
            "6665042) + BikeTiresDirect (Mfg PartNum 010-03023-00)"
        },
        notes="Garmin direct $599.99 (US store page JSON-LD read fresh "
        "2026-11-06 21:44 UTC; the page read states no availability — "
        "stock unconfirmed at Garmin direct); Best Buy $599.99 "
        "(search-index page read, InStock, Sold by Best Buy, SKU "
        "6665042, Model 010-03023-00); BikeTiresDirect $599.99 "
        "(search-index page read, JSON-LD InStock, Mfg PartNum "
        "010-03023-00); Sun & Ski $599.99 (feed authorized_retailer "
        "row — suspected; not page-verified). Compact GPS cycling "
        "computer, 2.7-inch color touchscreen + buttons, Garmin Pay, "
        "speaker / bike bell, up to 12 hours demanding / 36 hours "
        "battery saver, launched Sep 9, 2025. Single SKU — no color "
        "or size variants. Distinct from the set's Edge 1050 — the "
        "850 is the compact mid-tier Edge.",
        status="verified",
    ),
    EvalProduct(
        key="garmin-instinct-3-amoled-45mm-black",
        brand="Garmin",
        model="Instinct 3",
        variant="AMOLED 45mm, Black with Black Band (010-02936-00)",
        category="wearables",
        identifiers={"UPC": "753759339487", "MPN": "010-02936-00"},
        identifier_sources={
            "UPC": "Distributor row in the Meta Catalog feed (Mfg. "
            "Number 010-02936-00, UPC 753759339487) + DID Electrical "
            "(EAN 0753759339487 — the EAN-13 form of the same code) "
            "agree"
        },
        notes="Garmin direct $349.99 (US store page JSON-LD read fresh "
        "2026-11-06 21:48 UTC; the page read states no availability — "
        "stock unconfirmed at Garmin direct); Abt $332.99 (page read "
        "fresh 2026-11-06 21:50 UTC, JSON-LD InStock, Comp. Value "
        "$349.99, Model 010-02936-00); The GPS Store $349.99 (feed "
        "authorized_retailer row — suspected; not page-verified). "
        "45mm AMOLED GPS smartwatch, 1.2-inch display, built-in LED "
        "flashlight, up to 18 days smartwatch battery, launched Jan "
        "2025. The feed's $199.99 brand_direct row is a UK shop "
        "(zenithwellness.co.uk) — non-US, excluded (DECISIONS 021); "
        "the Kohl's $349.99 Neotropic row is a different colorway. "
        "Not the Solar 45mm Black (010-02934-00, $349.99) or the "
        "AMOLED 50mm Black (010-03020-00, $399.99) or the Solar 50mm "
        "Black (010-02935-00, $399.99) — different SKUs. Distinct "
        "from the set's Forerunner 165 and Forerunner 570 — the "
        "Instinct 3 is Garmin's rugged outdoor watch, not a running "
        "watch.",
        status="verified",
    ),
    EvalProduct(
        key="bose-soundlink-flex-2nd-gen-black",
        brand="Bose",
        model="SoundLink Flex (2nd Gen)",
        variant="Black (887612-0100)",
        category="speakers",
        identifiers={"UPC": "017817852470", "MPN": "887612-0100"},
        identifier_sources={
            "UPC": "B&H Photo (887612-0100, Black, UPC 017817852470, "
            "$159.00 InStock, page read 2026-11-06 21:52 UTC) + "
            "Volza Peru import records (Bose 887612-0100, SPKR "
            "SOUNDLINK FLEX BLACK, ITEM NUMBER 017817852470, "
            "filings Dec 2024–Mar 2025) agree. An Amazon US listing "
            "agreeing on the same code was read but not cited and "
            "not used (no-Amazon rule)."
        },
        notes="Bose direct $159.00 (feed brand_direct rows — "
        "suspected; the bose.com page text read 2026-11-06 21:49 UTC "
        "shows no price); Abt $159.00 (page read fresh 2026-11-06 "
        "21:50 UTC, JSON-LD InStock, Model 887612-0100); B&H $159.00 "
        "(page read fresh 2026-11-06 21:52 UTC, JSON-LD InStock). "
        "Portable Bluetooth speaker, IP67, Bluetooth 5.3, up to 12 "
        "hours battery, PositionIQ, launched Sep 2024. Not the Blue "
        "Dusk (887612-0200, UPC 017817852487) or the Sandstone "
        "(887612-0300, UPC 017817852616) or the Alpine Sage "
        "(887612-0400, UPC 017817852494) — different SKUs. Distinct "
        "from the set's Bose headphones and earbuds — the Flex is "
        "Bose's portable speaker line, and the first Bose speaker in "
        "the set.",
        status="verified",
    ),
    EvalProduct(
        key="bose-soundlink-plus-black",
        brand="Bose",
        model="SoundLink Plus",
        variant="Black (894040-0100)",
        category="speakers",
        identifiers={"UPC": "017817857932", "MPN": "894040-0100"},
        identifier_sources={
            "UPC": "B&H Photo (894040-0100, Bose Black, UPC "
            "017817857932, page read 2026-11-06 21:52 UTC) + "
            "manuals.plus spec table (Model Number 894040-0100, "
            "UPC 017817857932) agree. An Amazon US listing agreeing "
            "on the same code was read but not cited and not used "
            "(no-Amazon rule)."
        },
        notes="Bose direct $269.00 (feed brand_direct row — suspected; "
        "not page-read this round); B&H $179.00 (page read fresh "
        "2026-11-06 21:52 UTC, JSON-LD InStock, Holiday Savings "
        "$90 off $269.00); Abt $179.00 (page read fresh 2026-11-06 "
        "21:52 UTC, JSON-LD InStock, manufacturer rebate ends "
        "11/08/2026, Comp. Value $269.00). Note: the $179.00 is a "
        "sale/rebate price ending Nov 8 — re-check next refresh. "
        "Portable Bluetooth speaker, IP67, Bluetooth 5.4, up to 20 "
        "hours battery, USB-C power-bank output, launched Jun 2025. "
        "Not the Blue Dusk or Sunset Peach — different SKUs. "
        "Distinct from the set's SoundLink Flex (2nd Gen) — the "
        "Plus sits between the Flex and the Max (bigger driver, "
        "20-hour battery, power-bank function).",
        status="verified",
    ),
    EvalProduct(
        key="keychron-k2-he-special-black",
        brand="Keychron",
        model="K2 HE",
        variant="Special Edition, Black, Gateron Double-Rail Magnetic "
        "Nebula Switch Version 1 (K2H-F1)",
        category="keyboards",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING — EAN conflict, no tiebreak: the "
        "Keychron official store public product JSON "
        "(browser-verified 2026-11-06) gives the Special Edition / "
        "Black / Nebula Switch V1 variant (SKU K2H-F1, price "
        "$139.99, available: true) barcode 4895248889175, while B&H "
        "Photo lists the same SKU K2H-F1 with EAN 4895248889199. No "
        "third source surfaced for either code, and neither code "
        "appears in the other's source, so identifiers stay empty "
        "per the strict two-source rule — re-check next refresh. "
        "Not copied: 4895248889175 or 4895248889199 (conflicted "
        "candidates). Quotes (3): Keychron direct $139.99 (official "
        "store JSON, available: true; 75% ANSI, QMK, Hall Effect, "
        "2.4 GHz / Bluetooth 5.2 / USB-C, 4000 mAh, up to 110 "
        "hours); B&H $139.99 (search-index page read, Temporarily "
        "Out of Stock, expected 7–14 business days); Best Buy "
        "$129.99 (feed authorized_retailer row — suspected; the "
        "listing title names no edition or switch version and is "
        "most likely the Standard version, a different variant). "
        "Excluded: the Best Buy $199.99 Concrete Edition row and "
        "the feed's Newegg $255.82 / $272.75 rows (third-party "
        "inflated prices). Not the Standard Version Black "
        "(K2H-J1, $129.99, currently unavailable at Keychron) or "
        "the Special Edition White (K2H-Q1) or the Resin Edition "
        "($199.99) — different variants. Distinct from the set's K8 "
        "HE Special (K8H-F1) — the K2 HE is the 75% Hall Effect "
        "board; and from the set's K8 lines and Q1 — the K2 HE won "
        "a 2025 CES Innovation Award.",
        status="pending",
    ),
    EvalProduct(
        key="dell-ultrasharp-27-4k-thunderbolt-hub-monitor-u2725qe",
        brand="Dell",
        model="UltraSharp 27 4K Thunderbolt Hub Monitor",
        variant="Silver (U2725QE, MPN 95WRG)",
        category="monitors",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: the candidate UPC 884116484578 "
        "appears only at B&H Photo (U2725QE spec page, $649.99 "
        "InStock) — the only other hit, Tanotis, reproduces B&H's "
        "spec text verbatim (same data lineage, not independent), "
        "and no second independent source surfaced, so identifiers "
        "stay empty per the strict two-source rule — same call as "
        "batch 30's Watch9 and batch 31's Tab S11 Ultra. Not "
        "copied: 884116484578 (single-source candidate). MPN 95WRG "
        "confirmed by the Dell US page (Manufacturer Part Number "
        "95WRG); SHI lists Mfr Part # DELL-U2725QE. Quotes (3): "
        "Dell direct $849.99 (feed row — suspected; the dell.com "
        "page read 2026-11-06 21:50 UTC confirms the model and "
        "specs but shows no price in text); B&H $649.99 (page read "
        "fresh 2026-11-06 21:52 UTC, JSON-LD InStock, was $799.99); "
        "Adorama $649.99 (search-index page read, BackOrder). Note "
        "the wide spread: Dell direct $849.99 vs street $649.99 — "
        "re-check the Dell direct price next refresh. 27-inch 4K "
        "UHD IPS Black, 120Hz, Thunderbolt 4 hub with up to 140W "
        "power delivery, 99% DCI-P3, DisplayHDR 600, KVM, launched "
        "early 2025 (MSRP $749 per trade coverage; SHI lists MSRP "
        "$1,062.49). Distinct from the set's UltraSharp 32 4K "
        "U3225QE — the U2725QE is the 27-inch sibling; and from the "
        "set's Dell 27 Plus 4K S2725QS — the UltraSharp is the "
        "Thunderbolt-hub pro line.",
        status="pending",
    ),
    EvalProduct(
        key="bose-soundlink-max-black",
        brand="Bose",
        model="SoundLink Max",
        variant="Black (883848-0100)",
        category="speakers",
        identifiers={"UPC": "017817848817", "MPN": "883848-0100"},
        identifier_sources={
            "UPC": "Adorama spec table (MFR 883848-0100, Black "
            "Speaker UPC 017817848817, Blue Dusk 017817848824, "
            "speaker-with-case codes 192223266810/803 are different "
            "SKUs) + Layup (Model 883848-0100, UPC 017817848817) "
            "agree. Amazon US and eBay listings agreeing on the "
            "same code were read but not cited and not used "
            "(no-Amazon rule)."
        },
        notes="Bose direct $399.00 list / $329.00 sale (feed "
        "brand_direct rows — suspected; the bose.com page text "
        "shows no price, same as batch 32's Flex); Adorama "
        "$399.00 (page read fresh 2026-11-06 21:58 UTC, SKU "
        "BO8838480100, MFR 883848-0100, 4.7/5 from 912 reviews); "
        "Abt $399.00 (search-index read, JSON-LD InStock, Model "
        "883848-0100). Portable Bluetooth speaker, IP67, Bluetooth "
        "5.3, up to 20 hours battery, USB-C power-bank output, "
        "removable rope handle, launched May 2024. Not the Blue "
        "Dusk (017817848824) — different SKU. Distinct from the "
        "set's SoundLink Flex (2nd Gen) and SoundLink Plus — the "
        "Max is the largest portable in the line (bigger stereo "
        "drivers, 20-hour battery).",
        status="verified",
    ),
    EvalProduct(
        key="bose-quietcomfort-headphones-black",
        brand="Bose",
        model="QuietComfort Headphones",
        variant="Black (884367-0100)",
        category="headphones",
        identifiers={"UPC": "017817848961", "MPN": "884367-0100"},
        identifier_sources={
            "UPC": "Best Buy US specs (Model 884367-0100, UPC "
            "017817848961) + Reverb bundle row (MPN 884367-0100-1K, "
            "UPC 17817848961 — the same code without its leading "
            "zero) + BuyAdvanced GTIN 00017817848961 agree; VIP "
            "Outlet's SKU VIP017817848961MN embeds the same code. "
            "An Amazon US listing agreeing on the same code was "
            "read but not cited and not used (no-Amazon rule). "
            "Not the manuals.plus 732262048246 (a -cr suffixed "
            "listing, different SKU)."
        },
        notes="Bose direct $359.00 list / $169.00 sale (feed "
        "brand_direct rows — suspected; the bose.com page read "
        "fresh 2026-11-06 21:59 UTC confirms the model — successor "
        "to the QuietComfort 45 — but shows no price; DealNews "
        "2026-11-04, verified 2026-11-05, reports $169 matched at "
        "Target and Bose direct); Crutchfield $359.00 "
        "(search-index read, In stock, Item # 018QCHPBK, MFR # "
        "884367-0100). Excluded: the Best Buy $225.00 JSON-LD row "
        "(page read fresh 2026-11-06 21:58 UTC) — sold & shipped "
        "by GD Electronics, a marketplace seller (DECISIONS 021). "
        "The $169.00 is a Black Friday sale — re-check after the "
        "sale ends Nov 8. Over-ear wireless noise-cancelling "
        "headphones, up to 24 hours battery, Quiet/Aware modes, "
        "launched Sep 2023. Not the QuietComfort Headphones (2nd "
        "Gen, launched 2025, $359.00) or the QuietComfort SC "
        "(884367-0900, soft case, Costco/Best Buy only) or the "
        "QuietComfort Ultra (880066-0100) — different models. "
        "Distinct from the set's QuietComfort Ultra Headphones "
        "(2nd Gen) — these are the standard QC line, Bose's "
        "mainstream over-ear.",
        status="verified",
    ),
    EvalProduct(
        key="keychron-k2-max-black-rgb-aluminum-banana",
        brand="Keychron",
        model="K2 Max",
        variant="Black, RGB Backlight Aluminum Frame (Hot-Swappable), "
        "Keychron Super Banana (K2M-C4)",
        category="keyboards",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: the Keychron official store "
        "public product JSON (read fresh 2026-11-06 22:00 UTC) "
        "gives variant 41767535870041 (Black / RGB Backlight "
        "Aluminum Frame / Keychron Super Banana, SKU K2M-C4, "
        "$114.99, available: true) barcode 4895248880271, but no "
        "second independent source states that barcode — the "
        "B&H search surfaced no US row for K2M-C4, and the "
        "datagate.ee row is K2M-J3 (a different RGB/Black "
        "variant) — so identifiers stay empty per the strict "
        "two-source rule, same call as batch 32's K2 HE. Not "
        "copied: 4895248880271 (single-source candidate). MPN "
        "K2M-C4 is Keychron-store-only, so it is not recorded "
        "either (0 MPN-only entries in the set). Quotes (1): "
        "Keychron direct $114.99 (official store JSON, "
        "available: true; 75% ANSI, QMK, 2.4 GHz / Bluetooth 5.1 "
        "/ USB-C, 1000 Hz polling, hot-swappable, 4000 mAh, up to "
        "190 hours, double-shot PBT keycaps). No second US "
        "retailer row surfaced for the exact K2M-C4 variant — "
        "Zenox HK (929 HKD) and PCCaseGear AU are non-US, and "
        "the feed's $124.99 ISO Layout Collection row is a "
        "different layout — so this entry carries a single quote; "
        "re-check for a second retailer quote next refresh. Not "
        "the K2M-A1 (White Backlight Banana, Amazon B0DXBM2TQM) "
        "or the K2M-J3 (RGB/Black) or the K2 Pro or the K2 "
        "Version 3 ($109.99 ISO) — different variants/models. "
        "Distinct from the set's K2 HE Special (K2H-F1) — the K2 "
        "Max is the QMK wireless 75% board with MX-style "
        "switches, not Hall Effect; and from the set's K8 lines "
        "and Q1 — the K2 Max is the 75% QMK Max board.",
        status="pending",
    ),
    EvalProduct(
        key="asus-proart-display-pa279crv",
        brand="ASUS",
        model="ProArt Display PA279CRV",
        variant="Black (PA279CRV, 90LM08E0-B01KB2)",
        category="monitors",
        identifiers={"UPC": "195553951531", "MPN": "PA279CRV"},
        identifier_sources={
            "UPC": "B&H Photo (PA279CRV, UPC 195553951531, $429.00 "
            "InStock, page read fresh 2026-11-06 21:57 UTC) + EPA "
            "ENERGY STAR registry (PA279CRV family, UPC Codes "
            "195553951531) + EPEAT registry (PA279CRV, UPCs "
            "including 195553951531) agree. EPEAT lists several "
            "UPCs for the family (195553951500, ...517, ...531, "
            "197105747869, 199291205994) — the B&H listing ties "
            "...531 to the standalone US monitor, so ...531 is "
            "the recorded code; the others are not copied."
        },
        notes="ASUS eShop $429.00 (feed brand_direct row, "
        "shop.asus.com/us/90lm08e0-b01kb2); B&H $429.00 (page "
        "read fresh 2026-11-06 21:57 UTC, JSON-LD InStock); ASUS "
        "US product page $429.00 (feed brand_direct row — "
        "suspected; not page-read this round). This is the retry "
        "of the batch 32 hold: the hold reason is gone — the feed "
        "now carries ASUS-direct rows at $429.00 and B&H confirms "
        "the same price in stock, so the street rows are no "
        "longer thin. 27-inch 4K UHD IPS, 99% DCI-P3 / 99% Adobe "
        "RGB, Delta E <2 Calman Verified, USB-C 96W PD, "
        "DisplayHDR 400, daisy-chain DisplayPort out, launched "
        "2023. Not the PA279CRV-P ($469.00 at B&H, different "
        "variant with a different stand) or the PA279CV ($399.00, "
        "the older model) — different models. Distinct from the "
        "set's ROG Swift monitors — the PA279CRV is ASUS's ProArt "
        "creator line, the first ProArt monitor in the set.",
        status="verified",
    ),
    EvalProduct(
        key="hyperx-cloud-iii-black",
        brand="HyperX",
        model="Cloud III Gaming Headset",
        variant="Black (727A8AA)",
        category="headphones",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: MPN 727A8AA is corroborated "
        "(HP US product page, Product # 727A8AA + Best Buy, Model "
        "727A8AA, SKU 6542541 + HyperX ROW atom feed, SKU "
        "727A8AA, Black), but the only UPC found, 197029008220, "
        "is stated on Amazon-lineage listings only (Amazon US, "
        "UPC 197029008220, GTIN 00197029008220; BuyAdvanced "
        "repeats the same Amazon-derived code) — and the set's "
        "Black-Red Cloud III (727A9AA) was left pending on "
        "exactly the same call, so identifiers stay empty per "
        "the strict two-source rule; re-check next refresh. Not "
        "copied: 197029008220 (single-lineage candidate). MPN "
        "727A8AA is not recorded either (0 MPN-only entries in "
        "the set). Quotes (3): HP direct $99.99 (search-index "
        "read, $99.99 USD, Product # 727A8AA); Best Buy $69.99 "
        "Holiday Deal (page read fresh 2026-11-06 21:58 UTC, "
        "JSON-LD InStock, Sold by Best Buy, Comp. Value $99.99); "
        "CompSource $120.22 (search-index read, JSON-LD InStock, "
        "authorized HP dealer). The $69.99 is a Holiday Deal — "
        "re-check after the Early Black Friday event ends Nov 8. "
        "Wired gaming headset, 53mm angled drivers, DTS "
        "Headphone:X, 10mm detachable mic, USB-C/USB-A/3.5mm, "
        "launched 2023. Not the Black-Red (727A9AA, UPC "
        "197029008237 — already in the set as "
        "hyperx-cloud-iii-black-red) or the Cloud III Wireless "
        "(77Z45AA, $149.99 list / $99.99 sale at HP) or the Cloud "
        "III S Wireless ($179.99) — different SKUs/models. "
        "Distinct from the set's Black-Red Cloud III — this is "
        "the all-Black colorway at the same $99.99 list.",
        status="pending",
    ),
    EvalProduct(
        key="jbl-charge-6-black",
        brand="JBL",
        model="Charge 6",
        variant="Black (JBLCHARGE6BLKAM)",
        category="speakers",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: MPN JBLCHARGE6BLKAM is corroborated "
        "(Best Buy US Model JBLCHARGE6BLKAM, SKU 10736029, page read "
        "fresh 2026-11-06 22:05 UTC + Canex CA + Amazon US agree), but "
        "the only UPC found, 050036407441, is stated on Amazon US "
        "(Model JBLCHARGE6BLKAM, UPC 050036407441) + Canex CA (SKU "
        "050036407441 for JBLCHARGE6BLKAM) + an eBay refurbished "
        "listing (MPN JBLCHARGE6BLKAM-Z, UPC 050036407441) — no second "
        "US non-Amazon source states it for the exact JBLCHARGE6BLKAM "
        "variant, so identifiers stay empty per the strict two-source "
        "rule, same call as batch 33's K2 Max and Cloud III. Not "
        "copied: 050036407441 (single-lineage candidate). MPN "
        "JBLCHARGE6BLKAM is not recorded either (0 MPN-only entries in "
        "the set). Quotes (5): JBL direct $199.95 list / $149.95 sale "
        "(feed brand_direct rows — suspected; the jbl.com page was not "
        "page-read this round); T-Mobile $199.99 (feed brand_direct "
        "row); Dell $199.95 (feed brand_direct row); Sweetwater "
        "$199.95 list / $149.95 sale (feed authorized_retailer row); "
        "Crutchfield $149.95 (feed authorized_retailer row). The "
        "$149.95 is an Early Black Friday sale — re-check after the "
        "event ends Nov 8. Portable Bluetooth speaker, JBL Pro Sound "
        "with AI Sound Boost, up to 28 hours playtime (24h + 4h "
        "Playtime Boost), IP68 waterproof/dustproof/drop-proof (1 m "
        "onto concrete), Auracast multi-speaker, built-in powerbank, "
        "USB-C lossless audio, launched Apr 2025. Excluded: the Best "
        "Buy $149.95 JSON-LD row (page read fresh 2026-11-06 22:05 "
        "UTC) — sold & shipped by Electronic Express, a marketplace "
        "seller (DECISIONS 021); the Best Buy $157.45 rows (speaker + "
        "carrying case bundles); the $24,998 feed rows (bad data); "
        "the Woot $119.95 deal reported by SamMobile 2026-10-30 (not "
        "a feed row, not counted). Not the Flip 7 (already in the set) "
        "or the Charge 5 — different models. Distinct from the set's "
        "Flip 7, PartyBox Stage 320 and Tour One M3 — the Charge 6 is "
        "JBL's mainstream portable speaker with a built-in powerbank.",
        status="pending",
    ),
    EvalProduct(
        key="razer-deathadder-v4-pro-black",
        brand="Razer",
        model="DeathAdder V4 Pro",
        variant="Black (RZ01-05330100-R3U1)",
        category="mice",
        identifiers={"UPC": "840272920718", "MPN": "RZ01-05330100-R3U1"},
        identifier_sources={
            "UPC": "Amazon US (Model RZ01-05330100-R3U1, UPC "
            "840272920718) + Layup (Model RZ01-05330100-R3U1, UPC "
            "840272920718) agree; Best Buy US confirms the MPN "
            "(Model RZ01-05330100-R3U1, SKU 6621764, page read fresh "
            "2026-11-06 22:05 UTC)"
        },
        notes="Quotes (5): Razer direct $169.99 (feed brand_direct "
        "row); Newegg $169.99 (feed authorized_retailer row); Abt "
        "$169.99 (feed authorized_retailer row); NFM $166.99 (feed "
        "authorized_retailer row); Best Buy $169.99 (page read fresh "
        "2026-11-06 22:05 UTC, SKU 6621764, 4.8/5 from 252 reviews). "
        "Ultra-lightweight wireless esports mouse, 56 g, Focus Pro 45K "
        "Optical Sensor Gen-2 (45,000 DPI), HyperSpeed Wireless Gen-2, "
        "first optical scroll wheel, Gen-4 optical switches, 8,000 Hz "
        "polling, up to 150 hours battery, launched Jul 2025. Not the "
        "White (RZ01-05330200-R3U1, $169.99) or the Esports Green "
        "Edition ($152.99 sale) or the NiKo Edition (RZ01-05330300-"
        "R3U1, $189.99) or the DeathAdder V3 Pro ($139.99 sale) or the "
        "DeathAdder Essential ($29.99) — different SKUs/models. "
        "Distinct from the set's Viper V4 Pro — the DeathAdder V4 Pro "
        "is Razer's ergonomic flagship, the Viper is the symmetrical "
        "line.",
        status="verified",
    ),
    EvalProduct(
        key="anker-soundcore-boom-2-black",
        brand="Anker",
        model="Soundcore Boom 2",
        variant="Phantom Black (A3138)",
        category="speakers",
        identifiers={"UPC": "194644188276"},
        identifier_sources={
            "UPC": "B&H Photo (A3138011, Phantom Black, UPC "
            "194644188276) + Romanian importer label (r-c.ro, Boom 2, "
            "UPC 194644188276) agree; Amazon US (AnkerDirect, UPC "
            "194644188276) states the same code but is not used for "
            "corroboration"
        },
        notes="MPN NOT recorded: B&H states A3138011 for the US Phantom "
        "Black while Target US (A-95002904) and the r-c.ro label state "
        "A3138012 — the two US sources disagree on the suffix, so no "
        "MPN is pinned (the UPC is shared across both suffixes). "
        "Quotes (3): soundcore direct $129.99 (soundcore.com page read "
        "fresh 2026-11-06 22:06 UTC, 'Buy Now for $129.99' — this "
        "supersedes the feed's stale $139.99 anker.com / us.anker.com "
        "rows); Target $99.99 (feed authorized_retailer row, sale vs "
        "the $139.99 list); Newegg $139.99 (feed authorized_retailer "
        "row). Portable Bluetooth speaker, 80W max (60W + BassUp 2.0), "
        "50W racetrack subwoofer + dual 15W tweeters, 24-hour playtime, "
        "IPX7 waterproof and floatable, beat-synced RGB light show, "
        "PartyCast 2.0, built-in power bank, Bluetooth 5.3, USB-C, "
        "launched 2024. B&H lists it Temporarily Out of Stock. Not "
        "the Boom 2 Plus (140W, A3134, $250 list) or the Boom 2 Pro or "
        "the Soundcore 2 ($44.99) or the Motion Boom — different "
        "models. The first Anker/Soundcore speaker in the set — Anker "
        "previously entered only with chargers, hubs and a power bank.",
        status="verified",
    ),
    EvalProduct(
        key="garmin-venu-3-black",
        brand="Garmin",
        model="Venu 3",
        variant="Black — Slate Stainless Steel Bezel, Black Case/Band "
        "(010-02784-01)",
        category="wearables",
        identifiers={"UPC": "753759314743", "MPN": "010-02784-01"},
        identifier_sources={
            "UPC": "Petra US distributor (Vendor SKU 010-02784-01, UPC "
            "753759314743) + PB Tech NZ (MPN 010-02784-01, UPC "
            "753759314743) + HeartRateMonitorsUSA MPN/UPC table "
            "(010-02784-01, 753759314743) agree"
        },
        notes="Quotes (4): Dell $449.99 list / $299.99 sale (feed "
        "brand_direct row — the $299.99 is a Dell sale, re-check next "
        "refresh); Kohl's $449.99 (feed authorized_retailer row, Black "
        "Case & Silicone Band); Best Buy $449.99 (feed "
        "authorized_retailer row, Stainless Steel and Black); "
        "Cabela's $449.99 (feed authorized_retailer row, Black 45mm). "
        "45mm AMOLED smartwatch, 1.4-inch display, up to 14 days "
        "battery, 30+ sports apps, calls from the wrist, 5 ATM, "
        "launched Sep 2023. Not the Whitestone (010-02784-00, UPC "
        "753759314736) or the Venu 3S (41mm) or the Venu 4 (already in "
        "the set) — different SKUs/models. Distinct from the set's "
        "Venu 4 — the Venu 3 is the previous-generation 45mm AMOLED "
        "health watch at the same $449.99 list.",
        status="verified",
    ),
    EvalProduct(
        key="keychron-q1-max-carbon-black",
        brand="Keychron",
        model="Q1 Max",
        variant="Carbon Black, Fully Assembled Knob, Gateron Jupiter "
        "Brown (Q1M-M3)",
        category="keyboards",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: the Keychron official store public "
        "product JSON (read fresh 2026-11-06 22:07 UTC) gives variant "
        "40707102802009 (Fully Assembled Knob / Carbon Black / Gateron "
        "Jupiter Brown, SKU Q1M-M3, $229.99) barcode 4895248870609, "
        "but no second independent source states that barcode — PB "
        "Tech lists UPC '-' for Q1M-M3, and the barcode search "
        "surfaced no second source — so identifiers stay empty per "
        "the strict two-source rule, same call as batch 33's K2 Max "
        "and K2 HE. Not copied: 4895248870609 (single-source "
        "candidate). MPN Q1M-M3 is corroborated (Keychron JSON + Best "
        "Buy Canada Model Q1M-M3 + PB Tech Manufacturer Part No "
        "Q1M-M3) but is not recorded either (0 MPN-only entries in "
        "the set). Quotes (3): Keychron direct $229.99 (feed "
        "brand_direct row); Best Buy $229.99 (page read fresh "
        "2026-11-06 22:06 UTC, SKU 12683717, JSON-LD InStock, sold & "
        "shipped by Keychron — the brand itself); Newegg $317.29 "
        "(feed authorized_retailer row — higher than the $229.99 "
        "direct price, noted not used as the reference). This is the "
        "retry of the batch 33 hold: the hold reason is gone — the "
        "feed now carries Keychron-direct + Best Buy rows at $229.99, "
        "same pattern as the batch 33 PA279CRV retry. 75% ANSI "
        "full-metal QMK/VIA board, CNC aluminum, 2.4 GHz / Bluetooth "
        "5.1 / USB-C, 1000 Hz polling, hot-swappable Gateron Jupiter, "
        "4000 mAh, KSA double-shot PBT keycaps, knob. Not the Q1M-M1 "
        "(Red, barcode 4895248870593) or the Q1M-M4 (Banana, "
        "4895248870616) or the Q1M-M3-UK (ISO) or the Q1M-M3-SW "
        "(Swiss, EAN 7640156523034) or the barebone Q1M-B1 ($209.99) "
        "or the Q1 HE ($239.99) or the Q1 Pro ($149.99) or the Q1 "
        "Ultra 8K — different SKUs/models. Distinct from the set's Q1 "
        "Knob (the base Q1 V2) — the Q1 Max is the full-metal "
        "wireless QMK/VIA board with 2.4 GHz.",
        status="pending",
    ),
    EvalProduct(
        key="jbl-xtreme-4-black",
        brand="JBL",
        model="Xtreme 4",
        variant="Black (JBLXTREME4BLKAM)",
        category="speakers",
        identifiers={"UPC": "050036398190", "MPN": "JBLXTREME4BLKAM"},
        identifier_sources={
            "UPC": "Amazon US (ASIN B0CTP191Z3, Model JBLXTREME4BLKAM, "
            "UPC 050036398190, GTIN 11200130008129) + Ubuy (Model "
            "JBLXTREME4BLKAM, UPC 050036398190, GTIN 11200130008129, "
            "imported from US) agree; Best Buy US confirms the MPN, "
            "Model JBLXTREME4BLKAM, SKU 6582050"
        },
        notes="Portable Bluetooth speaker, 100W RMS (60W woofer + 40W "
        "tweeters), up to 24 hours playtime + 6 hours Playtime Boost, "
        "IP67 waterproof/dustproof, Auracast multi-speaker, built-in "
        "powerbank, replaceable battery, USB-C, launched Feb 2024. "
        "Conflicting code rejected: manuals.plus lists UPC 094148673325 "
        "for JBLXTREME4BLKAM (single source, same pattern as the XM6 "
        "094148746326 rejection in batch 1) — not used. Camo is "
        "050036398213 (Amazon US + Target US agree) and is a different "
        "color, not carried over. Quotes (3): JBL direct $379.95 list / "
        "$309.95 sale (feed brand_direct row); Target $379.99 (page "
        "read fresh 2026-11-06 22:12 UTC, OutOfStock); Rock & Soul "
        "$379.99 (feed authorized_retailer row). Excluded: the feed's "
        "Best Buy $299.99 row — page read fresh 2026-11-06 22:13 UTC "
        "shows SKU 12829838 sold & shipped by Simple Cell, Inc, a "
        "marketplace seller (DECISIONS 021); the Macy's $398.95 / "
        "$325.45 row (speaker + hard-shell case bundle); the $29,998 "
        "feed row (bad data). Not the Xtreme 3 or the Xtreme 5 — "
        "different models.",
        status="verified",
    ),
    EvalProduct(
        key="razer-basilisk-v3-pro-35k-black",
        brand="Razer",
        model="Basilisk V3 Pro 35K",
        variant="Black (RZ01-05240100-R3U1)",
        category="mice",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: MPN RZ01-05240100-R3U1 is corroborated "
        "(Razer US direct URL + Amazon US ASIN B0DG837JYP + Best Buy US "
        "Model RZ01-05240100-R3U1 + manuals.plus agree) but no US UPC "
        "was found for the R3U1 Black — the EAN 8886419334606 (startech24 "
        "datasheet) and the White R3G1 GTIN 8886419334644 (Scan UK) are "
        "EU/regional codes and were not used. MPN is not recorded either "
        "(0 MPN-only entries in the set). Quotes (4): Razer direct "
        "$159.99 (feed brand_direct row); Macy's $159.99 list / $99.99 "
        "sale (feed authorized_retailer row); CDW $167.99 (feed "
        "authorized_retailer row); ShopMyExchange $127.00 (feed "
        "authorized_retailer row). Ergonomic wireless gaming mouse, "
        "Focus Pro 35K Optical Sensor Gen-2 (35,000 DPI), HyperScroll "
        "Tilt Wheel, 13-zone Chroma RGB with full underglow, HyperSpeed "
        "Wireless + Bluetooth + USB-C, up to 140 hours battery, launched "
        "Oct 2024. Not the White (RZ01-05240200-R3U1) or the Phantom "
        "Green/White editions or the Xbox 25 Anniversary Edition "
        "($179.99) or the original 30K Basilisk V3 Pro (RZ01-04620100-"
        "R3U1, $99 sale) — different SKUs/models. Distinct from the "
        "set's Viper V4 Pro and DeathAdder V4 Pro — the Basilisk is "
        "Razer's ergonomic flagship line.",
        status="pending",
    ),
    EvalProduct(
        key="garmin-forerunner-265-black",
        brand="Garmin",
        model="Forerunner 265",
        variant="Black Bezel and Case with Black/Powder Gray Silicone Band, 46mm (010-02810-00)",
        category="wearables",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: MPN 010-02810-00 is corroborated "
        "(Abt US Model 010-02810-00 + Best Buy US Model 010-02810-00, "
        "SKU 6544440 + BikeTiresDirect Mfg PartNum 010-02810-00 agree) "
        "but no UPC was found for the -00 suffix — the only UPC "
        "circulating, 753759313715 (EAN 0753759313715), belongs to the "
        "-10 suffix (DID.ie + dbykstore) and was not carried over; "
        "753759313661 is the Whitestone -01 and 753759313678 is the "
        "Aqua -02 (Abt US spec tables). MPN is not recorded either (0 "
        "MPN-only entries in the set). Quotes (5): Abt $449.99 (page "
        "read fresh 2026-11-06 22:12 UTC, JSON-LD InStock); Kohl's "
        "$449.99 (feed authorized_retailer row); BikeTiresDirect $449.99 "
        "(feed authorized_retailer row); BuyDig $449.99 (feed "
        "authorized_retailer row, SKU GRFR265BKPG); Sportsman's $449.99 "
        "(feed authorized_retailer row). 46mm AMOLED GPS running "
        "smartwatch, 1.3-inch touchscreen, up to 13 days smartwatch "
        "mode / 20 hours GPS, 30+ sports apps, Garmin Pay, 5 ATM, "
        "launched Mar 2023. Excluded: the Best Buy $459.99 Aqua/Black "
        "row (different color variant). Not the Whitestone (010-02810-"
        "01) or the Aqua (010-02810-02) or the 42mm Forerunner 265S or "
        "the Forerunner 570 (already in the set) — different SKUs/models.",
        status="pending",
    ),
    EvalProduct(
        key="corsair-k70-core-rgb-black",
        brand="Corsair",
        model="K70 CORE RGB",
        variant="Black, no palm rest (CH-910971E-NA)",
        category="keyboards",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: MPN CH-910971E-NA is corroborated "
        "(Corsair US direct page SKU CH-910971E-NA + Amazon US Model "
        "CH-910971E-NA + pricehistory.app Model CH-910971E-NA agree) "
        "but no UPC was found for the no-palm-rest Black — the palm-"
        "rest variant's UPC 840006665762 (Amazon US, CH-910981E-NA) "
        "and the TKL's UPC 840006678786 (Amazon IN, CH-911911E-NA) are "
        "different SKUs and were not used. MPN is not recorded either "
        "(0 MPN-only entries in the set). Quotes (1): Corsair direct "
        "$99.99 list / $79.99 sale (feed brand_direct row + Corsair US "
        "page read via search index fresh 2026-11-06, InStock; the "
        "$79.99 is a current sale — umatechnology.org confirms both "
        "Black and Steel Gray at $79.99 vs $99.99 list). Only one clean "
        "quote this round: the feed's Newegg $99.99 / $79.99 row is the "
        "Steel Gray (CH-910991E-NA, confirmed by page read fresh "
        "2026-11-06 22:12 UTC) and was excluded as the wrong color; no "
        "Best Buy row surfaced for the Black. Full-size wired mechanical "
        "keyboard, pre-lubed MLX Red linear switches, SOCD, ABS "
        "double-shot keycaps, sound dampening, media control dial, 1000 "
        "Hz polling, 104 keys, QWERTY NA. Not the Steel Gray "
        "(CH-910991E-NA) or the with-palm-rest Black (CH-910981E-NA, "
        "$109.99) or the K70 CORE TKL (CH-911911E-NA) or the K70 CORE "
        "SE — different SKUs/models.",
        status="pending",
    ),
    EvalProduct(
        key="asus-rog-keris-ii-ace-black",
        brand="ASUS",
        model="ROG Keris II Ace",
        variant="Black (90MP03N0-BMAA00)",
        category="mice",
        identifiers={},
        identifier_sources={},
        notes="Identifiers PENDING: MPN 90MP03N0-BMAA00 is corroborated "
        "(ASUS eShop US + shop.asus.com CA, Product Name P714 ROG KERIS "
        "II WL ACE/BLK, Part Number 90MP03N0-BMAA00, agree) but no US "
        "UPC was found — the EAN 4711387394571 (Icecat + Direct "
        "Computers UK) belongs to the EU part 90MP03N0-BMUA00 and was "
        "not used. The White is 90MP03N0-BMAA10 (P714 ROG KERIS II WL "
        "ACE/WHT), a different SKU. MPN is not recorded either (0 "
        "MPN-only entries in the set). Quotes (2): ASUS eShop US $109.99 "
        "(feed brand_direct row, BMAA00 — a sale vs the $159.99 list; "
        "MicroCenter lists $159.99 list / $118.99 sale); MicroCenter "
        "$159.99 list / $118.99 sale (feed authorized_retailer row, "
        "poor quality). This is the retry of the batch 34 hold: the hold "
        "reason is gone — the feed now carries a clean ASUS-direct Black "
        "row at $109.99, same pattern as the batch 33 PA279CRV and "
        "batch 34 Q1 Max retries. Ultralight 54 g ergonomic wireless "
        "gaming mouse, 42,000-dpi ROG AimPoint Pro sensor, ROG Optical "
        "Micro Switches, SpeedNova wireless, Polling Rate Booster up to "
        "4,000 Hz wireless / 8,000 Hz wired. Not the Moonlight White "
        "(90MP03N0-BMAA10) or the Keris II Origin or the Keris Wireless "
        "AimPoint — different SKUs/models. Distinct from the set's ROG "
        "Gladius IV Ace and Harpe Mini Core — the Keris II Ace is the "
        "ultralight ergonomic line.",
        status="pending",
    ),
    # --- Expansion batch 32 (added 2026-11-09, user-approved, DECISIONS 070).
    # 200 -> 250 models. Source: data/candidates_batch1_250.md.
    # DECISIONS 070, BUILD_LOG 102.
    EvalProduct(
        key="sony-wh-ch520-black",
        brand="Sony",
        model="WH-CH520",
        variant="Black (WHCH520/B)",
        category="headphones",
        identifiers={"UPC": "027242925205", "MPN": "WHCH520/B"},
        identifier_sources={
            "UPC": "Batch-1 candidate verification 2026-11-09 (data/candidates_batch1_250.md, A-group "
            "report; single source)",
        },
        status="verified",
        notes="Sony entry-level on-ear Bluetooth headset, 50-hour battery; current mainstream model, "
        "sold new in the US.",
    ),
    EvalProduct(
        key="sony-ult-field-1-black",
        brand="Sony",
        model="ULT FIELD 1",
        variant="Black",
        category="speakers",
        identifiers={"UPC": "027242928923"},
        identifier_sources={
            "UPC": "Batch-1 candidate verification 2026-11-09 (data/candidates_batch1_250.md, A-group "
            "report)",
        },
        status="verified",
        notes="Sony ULT-series portable Bluetooth speaker (IP67, current generation); mainstream, sold "
        "new in the US. MPN pending — do not use SRS-XB100, the predecessor model.",
    ),
    EvalProduct(
        key="sony-inzone-h9-white",
        brand="Sony",
        model="INZONE H9",
        variant="White (WH-G900)",
        category="headphones",
        identifiers={"UPC": "027242923522"},
        identifier_sources={
            "UPC": "UPC 027242923522 verified 2026-11-12 (white only; "
            "black is a different code 027242928343, kept separate): "
            "ListenUp Shopify public product JSON (barcode 027242923522, "
            "SKU SON-WH-G900N-WHI, $178.00) + Best Buy US spec page (UPC "
            "027242923522, Model WHG900N/W, SKU 6510363) + Kawartha TV "
            "JSON-LD + Amazon white ASIN B0B1TDHLPT + Tanotis/Volza "
            "(WH-G900N-WZ) agree. Upgraded to verified on user approval "
            "2026-11-12 (DECISIONS 074).",
        },
        status="verified",
        notes="Sony INZONE flagship gaming headset (ANC, 360 Spatial Sound); previous generation — H9 "
        "II has launched — but still sold new in the US at ~$178. MPN WH-G900. Flag: previous- "
        "generation model; watch for clearance drift at add time.",
    ),
    EvalProduct(
        key="bose-smart-soundbar-600-black",
        brand="Bose",
        model="Smart Soundbar 600",
        variant="Black (873973-1100)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found in batch-1 verification 2026-11-09 "
            "(data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Bose compact Dolby Atmos soundbar; current mainstream model, live at Best Buy (SKU "
        "6517621). MPN 873973-1100.",
    ),
    EvalProduct(
        key="jbl-go-4-black",
        brand="JBL",
        model="Go 4",
        variant="Black",
        category="speakers",
        identifiers={"UPC": "050036399289"},
        identifier_sources={
            "UPC": "Batch-1 candidate verification 2026-11-09 (data/candidates_batch1_250.md, A-group "
            "report)",
        },
        status="verified",
        notes="JBL IP67 mini portable speaker, current generation; mainstream, sold new in the US. MPN "
        "pending — not recorded.",
    ),
    EvalProduct(
        key="jbl-clip-5-black",
        brand="JBL",
        model="Clip 5",
        variant="Black",
        category="speakers",
        identifiers={"UPC": "050036400077"},
        identifier_sources={
            "UPC": "Batch-1 candidate verification 2026-11-09 (data/candidates_batch1_250.md, A-group "
            "report)",
        },
        status="verified",
        notes="JBL ultra-portable carabiner speaker (IP67, Auracast), current generation; mainstream, "
        "sold new in the US. MPN pending — not recorded.",
    ),
    EvalProduct(
        key="jbl-tune-770nc-black",
        brand="JBL",
        model="Tune 770NC",
        variant="Black (JBLT770NCBLKAM)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — conflicting leads 050036395960 vs 050036396042, unresolved; do not pick "
            "one (batch-1 verification 2026-11-09, data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="JBL over-ear ANC headphones, 70-hour battery; mainstream, sold new in the US "
        "(Crutchfield MFR # JBLT770NCBLKAM). MPN JBLT770NCBLKAM.",
    ),
    EvalProduct(
        key="logitech-g502-x-black",
        brand="Logitech",
        model="G502 X",
        variant="Black, wired, HERO 25K (910-006136)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855166876 (3 independent sources, none a retailer spec table; "
            "batch-1 verification 2026-11-09). Do not use as verified.",
        },
        status="pending",
        notes="Current Logitech gaming mouse; Best Buy sold-by-Best-Buy $79.99 in stock; also Newegg "
        "sold-by-Newegg $79.99. Distinct from G502 X PLUS already in the catalog. MPN 910-006136 "
        "— the brief's 910-006178 is the G502 X LIGHTSPEED wireless, a different model.",
    ),
    EvalProduct(
        key="logitech-k380-dark-grey",
        brand="Logitech",
        model="K380",
        variant="Dark Grey (920-007558)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855117618 (batch-1 verification 2026-11-09, "
            "data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Logitech multi-device Bluetooth keyboard; Best Buy sold-by-Best-Buy $29.99 in stock, "
        "4.7/5, 4,041 reviews. MPN 920-007558 — the brief's alternative 920-011755 was not "
        "verified as this product. Logitech calls it 'Dark Grey' ('Gray' at Best Buy); not "
        "'Graphite' for K380. Flag: B&H has delisted it; Best Buy is the single live major "
        "retailer.",
    ),
    EvalProduct(
        key="logitech-mx-brio-graphite",
        brand="Logitech",
        model="MX Brio",
        variant="Graphite (960-001545)",
        category="webcams",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855187307 (batch-1 verification 2026-11-09, "
            "data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Logitech flagship 4K webcam, still a current product (~$199.99 list; $169.99 at Best Buy "
        "per Windows Central, Dec 2025). MPN 960-001545 — the brief's 960-001544 is the EU pack; "
        "960-001548 is AU/NZ graphite; not the MX Brio 705 for Business (960-001529). Flag: "
        "patchy US retail — Best Buy's current listing is the business 705 variant and B&H's "
        "consumer listing is Pale Gray; no live B&H/Best Buy consumer-graphite page found. Verify "
        "the live US seller before adding.",
    ),
    EvalProduct(
        key="logitech-signature-m650-graphite",
        brand="Logitech",
        model="Signature M650",
        variant="Regular size (small-to-medium hands), Graphite (910-006250)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855167637 (batch-1 verification 2026-11-09, "
            "data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Logitech silent-clicks wireless mouse; Best Buy sold-by-Best-Buy $39.99 in stock, 4.8/5. "
        "Regular size — NOT the L (910-006231) or Left (910-006234). MPN 910-006250 — 910-006262 "
        "on PB Tech is a non-US pack, do not use.",
    ),
    EvalProduct(
        key="razer-blackwidow-v4-x-green",
        brand="Razer",
        model="BlackWidow V4 X",
        variant="Full-size wired, Green clicky switches, Black (RZ03-04700200-R3U1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272903391 (batch-1 verification 2026-11-09, "
            "data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Current Razer mechanical gaming keyboard; Best Buy sold-by-Best-Buy $99.99 list in "
        "stock. MPN RZ03-04700200-R3U1 — the brief's RZ03-05200100 is wrong; special editions "
        "carry different MPNs (Fortnite RZ03-04703600-R3M1, Minecraft RZ03-04704100-R3M1, Pokémon "
        "RZ03-04704200-R3M1) — pin the standard edition.",
    ),
    EvalProduct(
        key="razer-huntsman-v3-pro-black",
        brand="Razer",
        model="Huntsman V3 Pro",
        variant="Full-size wired, Analog Optical Gen-2, Black (RZ03-04970200-R3U1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272909362 (batch-1 verification 2026-11-09, "
            "data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Current Razer analog-optical flagship keyboard; Best Buy sold-by-Best-Buy $209.99 (list "
        "$249.99) in stock. Standard 1KHz model — the newer Huntsman V3 Pro 8KHz "
        "(RZ03-05530200-R3U1, $249.99) is a separate model. MPN RZ03-04970200-R3U1 — the brief's "
        "RZ03-04970100 is the non-US -R3M1 part.",
    ),
    EvalProduct(
        key="razer-cobra-pro-black",
        brand="Razer",
        model="Cobra Pro",
        variant="Black, wireless (RZ01-04660100-R3U1)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found in batch-1 verification 2026-11-09 "
            "(data/candidates_batch1_250.md); the white version's UPC 840272913772 was not "
            "transferred to black.",
        },
        status="pending",
        notes="Current Razer wireless gaming mouse (HyperSpeed + Bluetooth + wired USB-C); Best Buy "
        "sold-by-Best-Buy $129.99 in stock; B&H in stock at $89.99 sale. MPN RZ01-04660100-R3U1 — "
        "the brief's RZ01-04630100 is the DeathAdder V3 Pro; the wired-only Cobra is "
        "RZ01-04650100-R3U1, a different model.",
    ),
    EvalProduct(
        key="razer-seiren-v3-chroma-black",
        brand="Razer",
        model="Seiren V3 Chroma",
        variant="Black (RZ19-05060100-R3U1)",
        category="microphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272911389 (batch-1 verification 2026-11-09, "
            "data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Current Razer streaming microphone; MPN RZ19-05060100-R3U1 (confirmed at Best Buy), list $129.99; Razer still "
        "sells it direct. Flag: Best Buy's own SKU shows a 'Clearance' tag and 'Unavailable' "
        "($116.99); the in-stock Best Buy listing is a marketplace seller (SpaceBound, $104.99). "
        "Confirm a live brand/retailer channel before adding.",
    ),
    EvalProduct(
        key="hyperx-cloud-alpha-black-red",
        brand="HyperX",
        model="Cloud Alpha",
        variant="Black-Red, wired (4P5L1AA#ABL)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — two values circulate: 196188048030 (HP-era, current) vs 740617268324 "
            "(Kingston-era); no spec-page confirmation (batch-1 verification 2026-11-09, "
            "data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Long-running HyperX wired gaming headset, still sold new (~$69.99). Distinct from Cloud "
        "Alpha Wireless (different model) and from Cloud III in the catalog. MPN 4P5L1AA#ABL "
        "(also shown as HX-HSCA-RD/AM). Flag: Best Buy lists it at $69.99 but 'Sold & shipped by "
        "HP Inc' (marketplace fulfillment, not Best Buy itself); the old Best Buy-sold SKU is no "
        "longer available new. HP is the brand owner, so this is brand-direct via marketplace — "
        "confirm the channel reading at add time.",
    ),
    EvalProduct(
        key="hyperx-alloy-origins-65-aqua",
        brand="HyperX",
        model="Alloy Origins 65",
        variant="Black, US layout, Aqua tactile switches (56R64AA#ABA)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 196337181342; conflicting 895829513446 from an India listing is "
            "likely a regional code, do not use (batch-1 verification 2026-11-09, "
            "data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="HyperX 65% gaming keyboard; HyperX US direct $79.99, available. Distinct from Alloy Rise "
        "75 in the catalog. MPN 56R64AA#ABA — the brief's 4P5N6AA is wrong; 4P5D6AA is the Red- "
        "switch version (B&H spec confirms Red: 4P5D6AA, UPC 196188046074, which is the Red, not "
        "the Aqua). Flag: B&H lists only the Red version; Aqua's live channels are HyperX/HP "
        "direct and Best Buy.",
    ),
    EvalProduct(
        key="hyperx-pulsefire-haste-2-black",
        brand="HyperX",
        model="Pulsefire Haste 2",
        variant="Black, wired, 53 g (6N0A7AA)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found in batch-1 verification 2026-11-09 "
            "(data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Current HyperX lightweight wired gaming mouse; Best Buy sold-by-Best-Buy $59.99 in "
        "stock; HP.com direct $59.99 in stock. Distinct from Haste 2 Pro (wireless) already in "
        "the catalog. MPN 6N0A7AA.",
    ),
    EvalProduct(
        key="apple-magic-keyboard-usb-c-white",
        brand="Apple",
        model="Magic Keyboard (USB-C)",
        variant="US English, White keys, no Touch ID, no numeric keypad (MJLX4LL/A)",
        category="keyboards",
        identifiers={"UPC": "195951258386", "MPN": "MJLX4LL/A"},
        identifier_sources={
            "UPC": "Apple.com manufacturer page, Part Number section (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Apple current keyboard; apple.com $99 in stock; also Best Buy ($79.99 on sale "
        "2026-11-02). Distinct from the Touch ID + Numeric Keypad model in the catalog "
        "(MJM64LL/A). MPN MJLX4LL/A — the brief's 'likely MJK83LL/A' does not exist; MXK83LL/A is "
        "the Touch ID + Numeric Keypad model in Black Keys.",
    ),
    EvalProduct(
        key="samsung-galaxy-watch8-40mm-graphite",
        brand="Samsung",
        model="Galaxy Watch8",
        variant="Graphite, 40mm, Bluetooth (SM-L320NDAAXAA)",
        category="wearables",
        identifiers={"UPC": "198957101786", "MPN": "SM-L320NDAAXAA"},
        identifier_sources={
            "UPC": "Samsung official US MSRP price list, Sept 2026 (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Samsung current smartwatch; Best Buy $299.99; Samsung US Business lists Graphite 40mm BT "
        "$299.99. Distinct from Watch8 Classic 46mm and Watch9 40mm in the catalog. MPN "
        "SM-L320NDAAXAA — Graphite = DAA code; the brief's SM-L320NZKAXAA is not a Watch8 code.",
    ),
    EvalProduct(
        key="samsung-galaxy-tab-s10-lite-128gb-gray",
        brand="Samsung",
        model="Galaxy Tab S10 Lite",
        variant="Gray, 10.9-inch, 128GB / 6GB RAM, Wi-Fi, with S Pen (SM-X400NZAAXAR)",
        category="tablets",
        identifiers={"UPC": "198957219764", "MPN": "SM-X400NZAAXAR"},
        identifier_sources={
            "UPC": "DataVision retailer listing, MFR SM-X400NZAAXAR, new, $399.99; corroborated by three "
            "eBay listings for Gray 128GB Wi-Fi (batch-1 verification 2026-11-09)",
        },
        status="verified",
        notes="Samsung current budget tablet (launched Sept 2025); Samsung US $399.99; Best Buy also "
        "lists it (SKU 6639132). Distinct from Tab S10 FE / FE+ / S11 family in the catalog. Best "
        "Buy calls the color 'Lite Gray', Samsung US calls it 'Gray' — same SKU. Conflicting UPC "
        "198957233845 comes from a used/resale shop listing — ignored.",
    ),
    EvalProduct(
        key="nintendo-switch-2-gamecube-controller",
        brand="Nintendo",
        model="Switch 2 GameCube Controller",
        variant="Indigo, wireless (BEE-021)",
        category="controllers",
        identifiers={"UPC": "045496884796", "MPN": "BEE-021"},
        identifier_sources={
            "UPC": "nintendo.com official store page (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Nintendo current first-party controller; Nintendo US Store $69.99 in stock. Distinct "
        "from Switch 2 Pro Controller (BEE-008) and N64 Controller in the catalog. MPN BEE-021 — "
        "the brief's BEE-010 is the Joy-Con 2 Charging Grip. Nintendo Store purchase requires a "
        "paid Nintendo Switch Online membership; no Best Buy/Target listing found — effectively "
        "brand-direct-only and membership-gated.",
    ),
    EvalProduct(
        key="garmin-forerunner-965-black",
        brand="Garmin",
        model="Forerunner 965",
        variant="Black case / Black-Powder Gray silicone band, 47mm (010-02809-00)",
        category="wearables",
        identifiers={"UPC": "753759313838", "MPN": "010-02809-00"},
        identifier_sources={
            "UPC": "Abt retailer spec page (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Garmin premium running watch; Best Buy (model 010-02809-00) $599.99 in stock. 2023 "
        "model; the Forerunner 970 successor exists, but the 965 is still sold new at Best "
        "Buy/Garmin. Distinct from Forerunner 570/165/265 in the catalog.",
    ),
    EvalProduct(
        key="garmin-lily-2-cream-gold",
        brand="Garmin",
        model="Lily 2",
        variant="Cream Gold case with Coconut silicone band, Sport edition, 35mm (010-02839-00)",
        category="wearables",
        identifiers={"UPC": "753759324711", "MPN": "010-02839-00"},
        identifier_sources={
            "UPC": "Visions Electronics Canada retailer spec; corroborated by eBay and OnBuy, EAN "
            "0753759324711 (batch-1 verification 2026-11-09)",
        },
        status="verified",
        notes="Garmin current women's smartwatch; Garmin US $249.99; also Target $249.99. No Lily model "
        "in the catalog. Conflicting UPC 753759342531 belongs to the Lily 2 Active — do not use.",
    ),
    EvalProduct(
        key="garmin-vivosmart-5-black-sm",
        brand="Garmin",
        model="Vivosmart 5",
        variant="Black, S/M (010-02645-00)",
        category="wearables",
        identifiers={"UPC": "753759279776", "MPN": "010-02645-00"},
        identifier_sources={
            "UPC": "heartratemonitorsusa.com retailer MPN/UPC table, corroborated by that seller's eBay "
            "description (batch-1 verification 2026-11-09)",
        },
        status="verified",
        notes="Garmin current fitness band; Garmin US $149.99; GPS Nation and Cabela's list it in stock "
        "new at $149.99. 2022 model, still sold new. Conflicting code 753759295066 belongs to the "
        "Large size (010-02645-04) — do not use for S/M.",
    ),
    EvalProduct(
        key="garmin-edge-540",
        brand="Garmin",
        model="Edge 540",
        variant="Device only, Black (010-02694-00)",
        category="cycling-computers",
        identifiers={"UPC": "753759299804", "MPN": "010-02694-00"},
        identifier_sources={
            "UPC": "Visions and Abt retailer specs (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Garmin current GPS bike computer; Garmin US $349.99, available to ship. Device only "
        "(Standard Edition) — not the sensor bundle (010-02694-10, $449.99) or Solar. Distinct "
        "from Edge 1050 and Edge 850 in the catalog.",
    ),
    EvalProduct(
        key="keychron-q3-max",
        brand="Keychron",
        model="Q3 Max",
        variant="Carbon Black, Fully Assembled Knob, Gateron Jupiter Red (Q3M-M1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC on keychron.com and no retailer spec found (batch-1 verification "
            "2026-11-09); consistent with all existing Keychron catalog entries, all pending.",
        },
        status="pending",
        notes="Keychron current QMK/VIA wireless custom keyboard; keychron.com US $229.99. Distinct "
        "from Q1 Max (Q1M-M3) in the catalog. MPN Q3M-M1 (page SKU). Fully Assembled Knob, Carbon "
        "Black, Gateron Jupiter Red — first-listed/default variant on keychron.com.",
    ),
    EvalProduct(
        key="keychron-v1-max",
        brand="Keychron",
        model="V1 Max",
        variant="Carbon Black, Fully Assembled Knob, Gateron Jupiter Red (V1M-D3)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found (batch-1 verification 2026-11-09); same as all other Keychron "
            "entries.",
        },
        status="pending",
        notes="Keychron current QMK/VIA wireless custom keyboard; keychron.com US $114.99. Distinct "
        "from K2 Max / Q1 Max in the catalog. MPN V1M-D3 (page SKU); only color is Carbon Black. "
        "Flag: the default Red-switch variant is currently out of stock on keychron.com US; Brown "
        "and Banana are in stock at the same $114.99. Previous generation — keychron.com pushes "
        "the newer V1 8K / V1 Ultra 8K — but the V1 Max is still listed and sold. Re-check stock "
        "at add time.",
    ),
    EvalProduct(
        key="keychron-k3-max",
        brand="Keychron",
        model="K3 Max",
        variant="Black, Fully Assembled (Hot-Swappable), RGB Backlight, Low Profile Gateron Mechanical Red (K3M-H1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found (batch-1 verification 2026-11-09); same as all other Keychron "
            "entries.",
        },
        status="pending",
        notes="Keychron current low-profile QMK/VIA wireless keyboard; keychron.com US $109.99. "
        "Distinct from K2 Max in the catalog. MPN K3M-H1 (page SKU). Flag: exact-variant stock on "
        "keychron.com US could not be cleanly read; mechanicalkeyboards.com lists K3M-H1 Red as "
        "sold out on their own stock. Previous generation — keychron.com pushes the newer K3 HE / "
        "K3 Ultra 8K — but the K3 Max is still listed and sold. The K3 Max also comes in non-hot- "
        "swap and white-backlight versions at lower prices; the pinned variant is the hot-swap "
        "RGB one.",
    ),
    EvalProduct(
        key="microsoft-surface-pro-12-2025-platinum",
        brand="Microsoft",
        model="Surface Pro, 12-inch (2025)",
        variant="Snapdragon X Plus (8-core), 16GB/256GB UFS, Platinum, device only (EP2-33670)",
        category="laptops",
        identifiers={"UPC": "196388550555", "MPN": "EP2-33670"},
        identifier_sources={
            "UPC": "Electronic Express retailer spec (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Microsoft current Copilot+ PC; Best Buy $989 (list $1,049.99), device only. Distinct "
        "from Surface Laptop 13.8-inch in the catalog. MPN EP2-33670 — ZGK codes are bundle SKUs, "
        "not this device. Best Buy now also sells a newer Surface Pro 12-inch with the same "
        "16GB/256GB/Platinum spec but Snapdragon X2 Plus (6-core), model EP2-75907, $1,149.99 — "
        "pin EP2-33670 explicitly as the 2025 Snapdragon X Plus model.",
    ),
    EvalProduct(
        key="lenovo-legion-go-s-steamos",
        brand="Lenovo",
        model="Legion Go S",
        variant="Powered by SteamOS, Nebula (black), Ryzen Z2 Go, 16GB / 512GB SSD, 8-inch 120Hz (83L30030US)",
        category="handheld-consoles",
        identifiers={"UPC": "198157044982", "MPN": "83L30030US"},
        identifier_sources={
            "UPC": "eBay and 12Sell, MPN 83L30030US (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Lenovo current handheld gaming PC; Best Buy $989.99 in stock, sold by Best Buy; Lenovo "
        "US also lists part 83L30030US. Distinct from Legion Tab models in the catalog. The same "
        "UPC appears on the white Windows version's listings too — the UPC seems shared across "
        "the Z2 Go 16/512 family; pin 83L30030US / SteamOS only. Keep separate from the higher- "
        "tier SteamOS Z1 Extreme 32GB/1TB model (~$1,099.99). Conflicting code 198157044999 is a "
        "ShopAbunda bundle SKU, not the base unit.",
    ),
    EvalProduct(
        key="anker-liberty-4-pro-glossy-black",
        brand="Anker",
        model="Soundcore Liberty 4 Pro",
        variant="Glossy Black (A3954ZF1)",
        category="earbuds",
        identifiers={"UPC": "194644297237", "MPN": "A3954ZF1"},
        identifier_sources={
            "UPC": "Abt retailer spec (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Anker flagship ANC earbuds (ACAA dual driver, smart case with display); Best Buy $109.99 "
        "live listing. Distinct from Liberty 5 (also in this batch) and Liberty 5 Pro (D1203) / "
        "Pro Max (D1204). MPN A3954ZF1 — B&H's A3954Z11 is the Matte Black finish, a different "
        "variant. Abt has since delisted it ('no longer available'); Best Buy is the live "
        "channel.",
    ),
    EvalProduct(
        key="alienware-aw3425dw",
        brand="Alienware",
        model="AW3425DW",
        variant="34-inch QD-OLED 240Hz (63HN0)",
        category="monitors",
        identifiers={"UPC": "884116493655", "MPN": "63HN0"},
        identifier_sources={
            "UPC": "Batch-1 candidate verification 2026-11-09 (data/candidates_batch1_250.md, D-group "
            "report)",
        },
        status="verified",
        notes="Alienware current 34-inch QD-OLED curved gaming monitor (launched Apr 2025); Dell USA "
        "direct. MPN 63HN0 (Dell USA; regional MPNs differ — AU KG7KH).",
    ),
    EvalProduct(
        key="hp-omen-32x-black",
        brand="HP",
        model="OMEN 32x",
        variant="Black, 32-inch (99Z68AA#ABA)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found in batch-1 verification 2026-11-09 "
            "(data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="HP current OMEN gaming monitor; sold new in the US. MPN 99Z68AA#ABA — the brief's "
        "guessed 780G9AA#ABA is wrong.",
    ),
    EvalProduct(
        key="google-pixel-watch-4-41mm-matte-black",
        brand="Google",
        model="Pixel Watch 4",
        variant="41mm, Matte Black case / Obsidian band, Wi-Fi (GA09958-US)",
        category="wearables",
        identifiers={"UPC": "840353931503", "MPN": "GA09958-US"},
        identifier_sources={
            "UPC": "Batch-1 candidate verification 2026-11-09 (data/candidates_batch1_250.md, D-group "
            "report)",
        },
        status="verified",
        notes="Google current smartwatch; Best Buy (SKU 6637235) lists GA09958-US. Distinct from the "
        "45mm size (also in this batch). MPN GA09958-US — the brief's GA05832-US is wrong.",
    ),
    EvalProduct(
        key="amazon-kindle-scribe-16gb-tungsten",
        brand="Amazon",
        model="Kindle Scribe (16GB, 2024)",
        variant="Tungsten, 16GB (B0CZ9VFQ2P)",
        category="e-readers",
        identifiers={"UPC": "840414615816", "MPN": "B0CZ9VFQ2P"},
        identifier_sources={
            "UPC": "Batch-1 candidate verification 2026-11-09 (data/candidates_batch1_250.md, D-group "
            "report)",
        },
        status="verified",
        notes="Amazon current pen e-reader (2024 release, 1st-gen Scribe refresh with AI notebook "
        "tools); sold new in the US. MPN B0CZ9VFQ2P is the ASIN retail code, consistent with the catalog's "
        "Paperwhite practice; device model C4A6T4.",
    ),
    EvalProduct(
        key="amazon-kindle-colorsoft-16gb-black",
        brand="Amazon",
        model="Kindle Colorsoft (16GB, 2025)",
        variant="Black, 16GB (B0FJBNPJ9P)",
        category="e-readers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found in batch-1 verification 2026-11-09 "
            "(data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Amazon current color E Ink reader (2025 release, standard Colorsoft — no wireless "
        "charging, unlike the Signature Edition); sold new in the US. MPN B0FJBNPJ9P is the ASIN retail "
        "code; device model SA58CB.",
    ),
    EvalProduct(
        key="anker-prime-charger-140w",
        brand="Anker",
        model="Prime Charger (140W)",
        variant="140W, 4-port, PD 3.1 (A2697)",
        category="chargers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — conflicting leads 194644290955 vs 194644212087, unresolved (batch-1 "
            "verification 2026-11-09, data/candidates_batch1_250.md).",
        },
        status="pending",
        notes="Anker current flagship GaN charger (140W single-port, touchscreen); Anker US direct, in "
        "sale. MPN A2697 — B2697 is the with-USB-C-cable bundle, a different SKU.",
    ),
    EvalProduct(
        key="bose-soundlink-micro-2nd-gen-black",
        brand="Bose",
        model="SoundLink Micro (2nd Gen)",
        variant="Black (895098-0100)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 017817859226 (check digit validates; Amazon listing only — no second "
            "non-Amazon source surfaced; batch-1 verification 2026-11-09). Do not use as verified.",
        },
        status="pending",
        notes="Bose current-generation micro portable speaker (launched Sept 10, 2025); Bose.com US "
        "live, Best Buy $129.00, Target $129.99 in stock, Abt $129.00 in stock. Replaces the "
        "discontinued 1st-gen Micro. Distinct from SoundLink Flex (2nd Gen), Plus, Max in the "
        "catalog. MPN 895098-0100. Do not confuse with the discontinued 1st-gen Micro "
        "(783342-0100, UPC 017817768429).",
    ),
    EvalProduct(
        key="alienware-aw2524hf",
        brand="Alienware",
        model="AW2524HF",
        variant="Dark Gray, 24.5-inch 500Hz Fast IPS (XM0CN)",
        category="monitors",
        identifiers={"UPC": "884116451860", "MPN": "XM0CN"},
        identifier_sources={
            "UPC": "Dell's own product datasheet, EAN 0884116451860 (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Alienware current 24.5-inch 500Hz Fast IPS gaming monitor; Dell USA direct, $449.99 sale "
        "/ $549.99 list. Successor to the AW2524H (cheaper FreeSync model, not the same monitor). "
        "Distinct from AW2726DM and AW3225DM in the catalog. MPN XM0CN (Dell USA tech specs; Dell "
        "config code 210-BJPH).",
    ),
    EvalProduct(
        key="dell-s3425dw-ash-white",
        brand="Dell",
        model="S3425DW",
        variant="Ash White, 34-inch 3440x1440 VA curved 120Hz, 65W USB-C (FRVJ3)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 884116485148 (single weak source: Ubuy import listing mirroring the "
            "US ASIN; no US retailer spec page confirms it; batch-1 verification 2026-11-09). Do not "
            "use as verified.",
        },
        status="pending",
        notes="Dell current 34-inch curved monitor (launched Mar 14, 2025); Dell USA direct, ~$399.99 "
        "street / $419.99 list. Distinct from S3225QS, S2725QS, U3225QE, U2725QE in the catalog. "
        "MPN FRVJ3 (US; regional MPNs differ — Ireland J7WG8, AU 31XKP). The brief's 'S3425QSA' "
        "model does not exist; S3425DW is the real model. The Best Buy listing calling it 'Black' "
        "is a third-party (6ave Electronics) 2-pack bundle mislabel — do not pin Black. "
        "Dell.com's own price was not exposed in the page crawl; confirm price on refresh.",
    ),
    EvalProduct(
        key="hyperx-solocast-2-black",
        brand="HyperX",
        model="SoloCast 2",
        variant="Black (AR0A0AA)",
        category="microphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 198701525790 (Amazon listings only; manuals.plus mirrors the Amazon "
            "ASIN and does not count as a second source; batch-1 verification 2026-11-09). Do not use "
            "as verified.",
        },
        status="pending",
        notes="HyperX current USB microphone (launched Aug 2025); HP.com US $59.99 in stock. MPN AR0A0AA. Successor "
        "to the discontinued SoloCast. Distinct from QuadCast 2 S in the catalog. List price is "
        "$59.99 — the brief's ~$44.99 was a ShopAbunda/Amazon-fulfilled holiday deal (excluded "
        "channel). Do not confuse with SoloCast 2 Pro (C96GRAA, $89.99), a different model.",
    ),
    EvalProduct(
        key="corsair-m75-air-wireless-black",
        brand="Corsair",
        model="M75 AIR Wireless",
        variant="Black (CH-931D100-NA)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no reliable lead in batch-1 verification 2026-11-09 "
            "(data/candidates_batch1_250.md); do not use 840006678403 (garbled Amazon Renewed listing "
            "that lists Manufacturer as 'Razer'); do not use 840006669128 (the White CH-931D101-NA "
            "SKU).",
        },
        status="pending",
        notes="Corsair current ultra-lightweight (60g, no-RGB) FPS wireless mouse; Corsair.com US in "
        "stock $99.99; Best Buy also lists it. Distinct from the discontinued M75 Wireless "
        "(CH-931D010-NA, RGB, 89g) and from M65 RGB Ultra in the catalog. MPN CH-931D100-NA — "
        "White is CH-931D101-NA, a different SKU. A Revival Series refurbished version exists "
        "(CH-931D100-NA-RV, $44.99) — pin the standard NA SKU only. One Best Buy review mentions "
        "a clearance purchase, so watch for clearance drift.",
    ),
    EvalProduct(
        key="anker-liberty-5-black",
        brand="Anker",
        model="Soundcore Liberty 5",
        variant="Black (A3957Z11)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC surfaced on Abt/Best Buy/B&H pages in batch-1 verification "
            "2026-11-09 (data/candidates_batch1_250.md); B&H lists the White A3957Z21. The only UPC "
            "found, 194644293482, belongs to the EU A3957G31 variant — not used as a lead for the US "
            "Black.",
        },
        status="pending",
        notes="Anker 2025 flagship earbuds (launched at $129.99); Best Buy sold-by-Best-Buy $89.99 (SKU "
        "6644915, model A3957Z11); Abt same model $89.99 in stock; Soundcore US direct $129.99. "
        "Distinct from Liberty 4 Pro (also in this batch) and Liberty 5 Pro (D1203) / Pro Max "
        "(D1204). MPN A3957Z11 (US suffix Z11; H11/G11 are other regions). Flag: Abt's $89.99 is "
        "flagged as including a manufacturer rebate ending 11/15/2026.",
    ),
    EvalProduct(
        key="samsung-galaxy-watch8-44mm-graphite",
        brand="Samsung",
        model="Galaxy Watch8",
        variant="Graphite, 44mm, Bluetooth (SM-L330NDAAXAA)",
        category="wearables",
        identifiers={"UPC": "198957098482", "MPN": "SM-L330NDAAXAA"},
        identifier_sources={
            "UPC": "Samsung official Wearables MSRP Price List, June and March 2026 editions (batch-1 "
            "verification 2026-11-09)",
        },
        status="verified",
        notes="Samsung current smartwatch, larger size of the Watch8; Best Buy sold-by-Best-Buy $329.99 "
        "in stock (SKU 6635080, model SM-L330NDAAXAA). Distinct from the 40mm Watch8 (also in "
        "this batch) — different size, different MPN/UPC.",
    ),
    EvalProduct(
        key="jbl-live-beam-3-black",
        brand="JBL",
        model="Live Beam 3",
        variant="Black (JBLLIVEBEAM3BLKAM)",
        category="earbuds",
        identifiers={"UPC": "050036401210", "MPN": "JBLLIVEBEAM3BLKAM"},
        identifier_sources={
            "UPC": "B&H spec page (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="JBL current true-wireless earbuds; B&H in stock $229.99; Crutchfield in stock $129.95 "
        "(sale, was $229.95). MPN JBLLIVEBEAM3BLKAM (B&H + Crutchfield agree). The Blue variant's "
        "UPC is different (050036401234) — do not mix.",
    ),
    EvalProduct(
        key="anker-space-one-pro-black",
        brand="Anker",
        model="Space One Pro",
        variant="Jet Black (A3062Z11)",
        category="headphones",
        identifiers={"UPC": "194644042479", "MPN": "A3062Z11"},
        identifier_sources={
            "UPC": "B&H spec page (batch-1 verification 2026-11-09) "
        },
        status="verified",
        notes="Anker 2024 flagship over-ear headphones, still current; B&H in stock $169.99 (was "
        "$199.99); Abt $169.99 in stock. MPN A3062Z11 (B&H, Abt, Crutchfield agree). A different "
        "code, 194644042448, appears on a non-US listing for a Cream White variant — not the "
        "Black.",
    ),
    EvalProduct(
        key="google-pixel-watch-4-45mm-matte-black",
        brand="Google",
        model="Pixel Watch 4",
        variant="45mm, Matte Black case / Obsidian band, Wi-Fi (GA09962-US)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found for GA09962-US in batch-1 verification 2026-11-09 "
            "(data/candidates_batch1_250.md); the Porcelain variant's UPC 840353931459 is Amazon-only "
            "and not transferable to Black.",
        },
        status="pending",
        notes="Google current smartwatch, larger size of the Pixel Watch 4; Google Store lists 41/45mm "
        "(brand direct); Target also lists the 45mm Matte Black/Obsidian. Distinct from the 41mm "
        "(also in this batch) — different size, different MPN. MPN GA09962-US — do not use "
        "GA09307-US (45mm LTE Black) or GA10850-US (45mm Moonstone, sold out at Best Buy). Flag: "
        "Best Buy's product page repeatedly showed 'Unavailable' next to the $399.99 price in "
        "crawls from the last 2–4 days, while its JSON-LD simultaneously said InStock — "
        "conflicting signals. Looks like a Best Buy stock/fulfilment gap (possibly Black Friday "
        "sell-through), not discontinuation — but re-check stock at add time. Porcelain "
        "(GA09308-US) has no standalone Best Buy US page, which is why Black was pinned.",
    ),
    EvalProduct(
        key="jbl-live-680nc-black",
        brand="JBL",
        model="Live 680NC",
        variant="Black (JBLLIVE680NCBLKAM)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 050036417365 (Amazon listing only; no retailer/manufacturer spec page "
            "publishes a US UPC — the UK page's EAN 1200130033186 belongs to the UK variant "
            "JBLLIVE680NCBLK, do not use; batch-1 verification 2026-11-09). Do not use as verified.",
        },
        status="pending",
        notes="JBL current Live-series on-ear ANC model (launched Mar 12, 2026), successor to the "
        "discontinued Live 670NC; JBL US in stock $159.95; Best Buy (Blue variant, sold by Best "
        "Buy) in stock $159.95; Abt lists the Black variant. MPN JBLLIVE680NCBLKAM. List price is $159.95 — the brief's "
        "~$129.95 was the old Live 670NC's price. Abt crawls conflict ($79.95 sale vs $159.95), "
        "so the street price may currently be promo-discounted.",
    ),
    EvalProduct(
        key="bose-soundlink-home-cool-gray",
        brand="Bose",
        model="SoundLink Home",
        variant="Cool Gray (892399-0020)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 017817856553 (Amazon listing + Snapklik mirror only; no "
            "retailer/manufacturer spec page publishes it; batch-1 verification 2026-11-09). Do not "
            "use as verified.",
        },
        status="pending",
        notes="Bose current portable home speaker (launched Oct 1, 2024, no successor); Bose US product "
        "page live; Target in stock $229.99; Sweetwater $229.00. MPN 892399-0020 — Light Silver "
        "is 892399-0010, not pinned. There is no Black variant — US colors are Cool Gray and "
        "Light Silver only (Warm Wood exists in Australia only). Model is ~2 years old but still "
        "current with no successor — acceptable as a mainstream current model, not clearance "
        "stock. Not waterproof, no Bose app support — product limitations, not catalog-rule "
        "issues.",
    ),
]

def get_product(key: str) -> EvalProduct:
    for product in EVAL_SET:
        if product.key == key:
            return product
    raise KeyError(f"unknown eval model key: {key}")
