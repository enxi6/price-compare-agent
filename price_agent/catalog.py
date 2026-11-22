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
    # --- Expansion batch 33 (added 2026-11-14, user-approved, DECISIONS 075).
    EvalProduct(
        key="sony-ult-field-7-black",
        brand="Sony",
        model="ULT FIELD 7",
        variant="Black (SRSULT70)",
        category="speakers",
        identifiers={"UPC": "027242928961", "MPN": "SRSULT70"},
        identifier_sources={
            "UPC": "B&H spec + Adorama spec agree (batch-2 re-verification 2026-11-14); both spec pages print"
            " UPC 027242928961 for SRSULT70",
        },
        status="verified",
        notes="Sony current ULT-series flagship portable speaker (IP67, 30h battery); sold new in the US."
        " Best Buy sold-by-Best-Buy $499.99 in stock (SKU 6577677). B&H stock crawls still conflict"
        " (one 'Temporarily Out of Stock', one 'In Stock') — no B&H row until the daily refresh"
        " resolves it; Adorama on backorder (expected 11/21/2026).",
    ),
    EvalProduct(
        key="sony-ult-field-3-black",
        brand="Sony",
        model="ULT FIELD 3",
        variant="Black (SRSULT30/B)",
        category="speakers",
        identifiers={"UPC": "027242931886", "MPN": "SRSULT30/B"},
        identifier_sources={
            "UPC": "Adorama spec lists Black 027242931886 / Off White 027242931893 (batch-2 re-verification"
            " 2026-11-14); Datavision + eBay GTIN agree",
        },
        status="verified",
        notes="Current-gen ULT portable speaker, launched Apr 9, 2025 (replaces SRS-XE300); Sony direct"
        " $149.99 (list $209.99); Adorama $208.00 on backorder (expected 11/29/2026). Off White"
        " (027242931893) and Forest Gray are separate variants — do not mix UPCs.",
    ),
    EvalProduct(
        key="sony-ult-field-5-black",
        brand="Sony",
        model="ULT FIELD 5",
        variant="Black (SRSULT50/B)",
        category="speakers",
        identifiers={"UPC": "027242931947", "MPN": "SRSULT50/B"},
        identifier_sources={
            "UPC": "Adorama spec lists Black 027242931947 / Off White 027242931954; B&H spec agrees (batch-2"
            " re-verification 2026-11-14)",
        },
        status="verified",
        notes="Current-gen ULT portable speaker, launched Apr 9, 2025 (replaces SRS-XG300); 25h battery,"
        " IP66/IP67. Best Buy sold-by-Best-Buy $349.99 in stock (SKU 6620181) — live in-stock channel"
        " confirmed at add time; Adorama $348.00 on backorder (expected 11/23/2026). Off White is a"
        " separate UPC (027242931954).",
    ),
    EvalProduct(
        key="sony-inzone-buds-black",
        brand="Sony",
        model="INZONE Buds",
        variant="Black (WFG700N/B)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — conflicting leads 027242927957 (Canadian authorized dealer Simcoe,"
            " Sony-prefix) vs 196641115897 (manuals.plus, Amazon-ASIN-derived); do not pick one (batch-2"
            " verification 2026-11-11).",
        },
        status="pending",
        notes="Sony's only true-wireless gaming earbuds (2.4 GHz dongle + LE Audio, ANC, 12h buds / 24h"
        " case); still sold new by Best Buy, no successor. MPN WFG700N/B; White (WFG700N/W) and Glass"
        " Purple (WFG700N/V) are separate. Best Buy sold-by-Best-Buy $159.99 in stock (list $199.99)."
        " 2023 model; price has drifted down from $199.99 list.",
    ),
    EvalProduct(
        key="sony-bravia-theatre-bar-6-black",
        brand="Sony",
        model="BRAVIA Theatre Bar 6",
        variant="Black, 3.1.2ch with wireless subwoofer (HTB600)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Sony's current mid-tier Atmos soundbar (2025, successor to the HT-A3000 line). MPN HTB600 /"
        " HT-B600. Best Buy sold-by-Best-Buy $549.99 in stock (comp. value $699.99, was $999.99). Best"
        " Buy spells it 'Theater'; Sony branding is 'Theatre'.",
    ),
    EvalProduct(
        key="bose-qc-ultra-earbuds-2nd-gen-black",
        brand="Bose",
        model="QuietComfort Ultra Earbuds (2nd Gen)",
        variant="Black (896637-0010)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 017817861120 (Amazon only, 3 listings, ASIN B0F7M3HPBD); Amazon-only"
            " values are never verified per standing rule. Do not confuse with Midnight Violet lead"
            " 017817861083 (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Bose flagship ANC earbuds, launched Sept 2025 (successor to 1st-gen Ultra Earbuds). MPN"
        " 896637-0010; White Smoke 896637-0020, Deep Plum -0030, Desert Gold -0040, Midnight Violet"
        " -0050 are separate. Best Buy sold-by-Best-Buy $299.00 in stock (SKU 6628900); Abt $299. Pin"
        " the Best Buy-sold SKU — one Best Buy Black listing (SKU 11871043) is sold by marketplace"
        " seller ThrillingAudio.",
    ),
    EvalProduct(
        key="bose-smart-ultra-soundbar-black",
        brand="Bose",
        model="Smart Ultra Soundbar",
        variant="Black (882963-1100)",
        category="soundbars",
        identifiers={"UPC": "017817848244", "MPN": "882963-1100"},
        identifier_sources={
            "UPC": "Adorama spec lists Black 017817848244 / White 017817848343 (batch-2 re-verification"
            " 2026-11-14); Visions + eBay agree",
        },
        status="verified",
        notes="Bose Dolby Atmos flagship soundbar (5.1.2, ADAPTiQ, A.I. Dialogue Mode); Bose's own release"
        " says it replaced the Soundbar 900. Best Buy sold-by-Best-Buy $679.00 in stock (SKU 6550611,"
        " list $999). Previous flagship — Bose launched the Lifestyle Ultra Soundbar (May 2026,"
        " $1,099) as the new flagship; Smart Ultra is still sold new, but watch for clearance drift.",
    ),
    EvalProduct(
        key="jbl-live-buds-3-black",
        brand="JBL",
        model="Live Buds 3",
        variant="Black (JBLLIVEBUDS3BLKAM)",
        category="earbuds",
        identifiers={"UPC": "050036401661", "MPN": "JBLLIVEBUDS3BLKAM"},
        identifier_sources={
            "UPC": "B&H spec + Amazon agree (batch-2 re-verification 2026-11-14)",
        },
        status="verified",
        notes="JBL 2024 true-wireless ANC earbuds with smart touchscreen case. Best Buy sold-by-Best-Buy"
        " $147.99 in stock (list $229.95); B&H $229.95 in stock. 2024 model at a deep discount"
        " ($147.99 vs $229.95 list) — promo/clearance drift watch; refurbished units also circulate at"
        " Best Buy (Electronics Expo) — pin new Best Buy-sold SKU 6582669.",
    ),
    EvalProduct(
        key="jbl-boombox-4-black",
        brand="JBL",
        model="Boombox 4",
        variant="Black (JBLBOOMBOX4BLKAM)",
        category="speakers",
        identifiers={"UPC": "050036413220", "MPN": "JBLBOOMBOX4BLKAM"},
        identifier_sources={
            "UPC": "B&H spec + Abt + manuals.plus agree (batch-2 re-verification 2026-11-14)",
        },
        status="verified",
        notes="JBL's most powerful portable speaker, launched Sept 2025 (IP68, 34h battery, Auracast)."
        " $549.95 list; Sweetwater Black $429.95 in stock; JBL.com $549.95 InStock; B&H Blue $549.95"
        " in stock. Blue (050036413251) and Squad (050036413237) are separate UPCs — do not mix.",
    ),
    EvalProduct(
        key="jbl-partybox-330-black",
        brand="JBL",
        model="PartyBox 330",
        variant="Black (JBLPB330BLKAM)",
        category="speakers",
        identifiers={"UPC": "050036422154", "MPN": "JBLPB330BLKAM"},
        identifier_sources={
            "UPC": "B&H spec + Abt agree (batch-2 re-verification 2026-11-14)",
        },
        status="verified",
        notes="Brand-new 2026 PartyBox (announced May 12, 2026; presale June 7, 2026; 280W, 18h swappable"
        " battery, AI karaoke); successor to the in-catalog Stage 320, distinct model. Best Buy"
        " sold-by-Best-Buy $629.95 in stock (SKU 6677352); B&H $629.95 in stock. White (050036422161)"
        " is separate. Cleanest pass in the batch.",
    ),
    EvalProduct(
        key="jbl-partybox-130-black",
        brand="JBL",
        model="PartyBox 130",
        variant="Black (JBLPB130BLKAM)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Brand-new compact 2026 PartyBox (announced May 12, 2026 alongside the 330; 200W, foldable"
        " handle, optical TV input). MPN JBLPB130BLKAM; White (JBLPB130WHTAM) separate. JBL.com"
        " $449.95 InStock; Best Buy White sold-by-Best-Buy $449.95 in stock.",
    ),
    EvalProduct(
        key="jbl-tune-beam-2-black",
        brand="JBL",
        model="Tune Beam 2",
        variant="Black (JBLTBEAM2BLKAM)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no US lead (UK item JBLTBEAM2BLK carries EAN 1200130016479 — not a US UPC, do"
            " not use; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="JBL current mid-tier ANC earbuds (10mm drivers, 48h total, IP54). MPN JBLTBEAM2BLKAM."
        " JBL.com US Black page confirmed at add time (Item# JBLTBEAM2BLKAM, $109.95, InStock,"
        " 2026-11-14) — the draft's 'Black US page unconfirmed' flag is closed. White (JBLTBEAM2WHTAM)"
        " separate.",
    ),
    EvalProduct(
        key="logitech-g915-x-tkl-tactile-black",
        brand="Logitech",
        model="G915 X LIGHTSPEED TKL",
        variant="Black, GL Tactile (920-012715)",
        category="keyboards",
        identifiers={"UPC": "097855194794", "MPN": "920-012715"},
        identifier_sources={
            "UPC": "Logitech spec sheet via manuals.plus + Amazon agree (batch-2 re-verification 2026-11-14);"
            " Colamco lists MPN 920-012715 with UPC 097855194794",
        },
        status="verified",
        notes="Current Logitech low-profile wireless flagship in TKL form; distinct from the full-size G915"
        " X already in the catalog. GL Brown Tactile. Best Buy sold-by-Best-Buy $209.99 (was $249.99),"
        " SKU 6595187. First guess MPN 920-012681 was wrong — do not use.",
    ),
    EvalProduct(
        key="logitech-g-pro-x-superlight-2c-black",
        brand="Logitech",
        model="G Pro X Superlight 2c",
        variant="Black (910-007518)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855203632 (single non-US source, Tanotis; Adorama page shows no UPC;"
            " batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="New (Sept 2025) compact Superlight, 51 g, HERO 2; distinct from Superlight 2 and Superlight"
        " 2 DEX in the catalog. MPN 910-007518 (Adorama spec page confirms). Adorama $149.99 (list"
        " $159.99), InStock, ships from manufacturer. White 910-007528 / Pink 910-007529 / Magenta"
        " 910-007546 (EU) are different SKUs; AU black pack 910-007533 — do not mix.",
    ),
    EvalProduct(
        key="logitech-mx-master-3s-bluetooth-black",
        brand="Logitech",
        model="MX Master 3S Bluetooth Edition",
        variant="Black, Bluetooth Edition (910-007500)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855201812 (Amazon-only; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Previous-gen but still sold new in the US; MX Master 4 is a different model in the catalog."
        " Bluetooth Edition (no Logi Bolt receiver, no cable). MPN 910-007500 (Best Buy confirms, SKU"
        " 12028852, 390 reviews). Best Buy $79.99 on sale Oct 2026 (list $99.99). Do NOT use"
        " standard-edition Black 910-006556 or Graphite 910-006559 (EU pack). Bluetooth-only; 1-year"
        " warranty per BuyDig (vs 2-year standard).",
    ),
    EvalProduct(
        key="razer-deathadder-v3-hyperspeed-black",
        brand="Razer",
        model="DeathAdder V3 HyperSpeed",
        variant="Black (RZ01-05140100-R3U1)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead (guessed 840272911235 was NOT confirmed — do not use; the wired V3's"
            " UPC 840272903018 belongs to a different model; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current Razer mid-tier wireless esports mouse; distinct from V3 Pro / V4 Pro in the catalog."
        " MPN RZ01-05140100-R3U1 (Best Buy + Canada Computers agree). Wireless, Focus X 26K. Best Buy"
        " $99.99, SKU 6580802, 4.7 stars / 195 reviews.",
    ),
    EvalProduct(
        key="razer-kraken-v4-black",
        brand="Razer",
        model="Kraken V4 (wireless)",
        variant="Black (RZ04-05170100-R3U1)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current Razer wireless headset (2.4 GHz + Bluetooth + USB); distinct from Kraken V4 Pro in"
        " the catalog. Do not confuse with Kraken V4 X (wired, RZ04-05180100), a different cheaper"
        " model. MPN RZ04-05170100-R3U1 (Best Buy confirms, SKU 6586394). Best Buy $179.99.",
    ),
    EvalProduct(
        key="razer-seiren-v3-mini-black",
        brand="Razer",
        model="Seiren V3 Mini",
        variant="Black (RZ19-05050100-R3U1)",
        category="microphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272911327 (Amazon/camelcamelcamel only; batch-2 verification"
            " 2026-11-11).",
        },
        status="pending",
        notes="Current Razer compact USB mic; distinct from Seiren V3 Chroma in the catalog. MPN"
        " RZ19-05050100-R3U1 (Best Buy confirms, SKU 6573619). Best Buy $48.99 (list $59.99).",
    ),
    EvalProduct(
        key="razer-viper-v3-hyperspeed-black",
        brand="Razer",
        model="Viper V3 HyperSpeed",
        variant="Black (RZ01-04910100-R3U1)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272911228 (Canex SKU field, single source; batch-2 verification"
            " 2026-11-11).",
        },
        status="pending",
        notes="Current Razer symmetric wireless mouse, Focus Pro 30K, 280-hour AA battery; distinct from"
        " Viper V4 Pro in the catalog. MPN RZ01-04910100-R3U1 (Best Buy + Canada Computers agree —"
        " guessed RZ01-05160100 was wrong). Best Buy $69.99 (list $99.99), SKU 6558751; Razer US"
        " $69.99 InStock.",
    ),
    EvalProduct(
        key="hyperx-cloud-stinger-2-black",
        brand="HyperX",
        model="Cloud Stinger 2 (wired)",
        variant="Black, wired (519T1AA)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 196188736906 (Clove UK barcode, single non-US source; batch-2"
            " verification 2026-11-11).",
        },
        status="pending",
        notes="Current HyperX budget wired headset; no Stinger model in the catalog. MPN 519T1AA (HP.com US"
        " confirms). HP.com US $49.99 InStock. Stinger 2 Wireless and Stinger 2 Core (PS/Xbox/PC) are"
        " different models.",
    ),
    EvalProduct(
        key="hyperx-pulsefire-haste-2-wireless-black",
        brand="HyperX",
        model="Pulsefire Haste 2 Wireless",
        variant="Black (6N0B0AA)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current HyperX wireless mouse, 61 g, dual wireless; distinct from wired Haste 2 and Haste 2"
        " Pro 4K in the catalog. MPN 6N0B0AA (HP.com US confirms; White is 6N0A9AA — do not mix)."
        " HP.com US $89.99 InStock; HyperX US $78.99 Black available. Haste 2 Core (8R2E6AA) is a"
        " different cheaper model.",
    ),
    EvalProduct(
        key="hyperx-quadcast-2-black",
        brand="HyperX",
        model="QuadCast 2",
        variant="Black (872V1AA)",
        category="microphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead (eBay's 198122243846 is tied to odd MPN CL006A — not used; batch-2"
            " verification 2026-11-11).",
        },
        status="pending",
        notes="Current HyperX USB mic; distinct from QuadCast 2 S in the catalog. MPN 872V1AA (HP.com US"
        " confirms; Frost is AN1D9AA). HP.com US $149.99 InStock; HyperX US $119.99 on sale (list"
        " $149.99).",
    ),
    EvalProduct(
        key="corsair-scimitar-elite-wireless-se-gun-metal",
        brand="Corsair",
        model="Scimitar Elite Wireless SE",
        variant="Gun Metal (CH-9314014-WW)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840440492276 (Scan UK GTIN, single source; batch-2 verification"
            " 2026-11-11).",
        },
        status="pending",
        notes="Newer SE variant (33K DPI, MARKSMAN S sensor) with live US channels; distinct from the plain"
        " Scimitar Elite Wireless. MPN CH-9314014-WW (Best Buy + Scan agree). Best Buy $139.99, SKU"
        " 6622828 (Deal of the Day); Corsair US $139.99 (SE Black & Yellow CH-9314415-WW InStock). SE"
        " White CH-9314011-WW is out of stock at Corsair — pin Gun Metal only.",
    ),
    EvalProduct(
        key="apple-pencil-pro-white",
        brand="Apple",
        model="Pencil Pro",
        variant="White (MX2D3AM/A)",
        category="accessories",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 195949573040 (shopsavvy only — single source, not a retailer spec page;"
            " batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Apple current stylus. MPN MX2D3AM/A (Best Buy confirms). Best Buy sold-by-Best-Buy $129.00"
        " in stock (SKU 6535042, page opened and read); Apple $129.",
    ),
    EvalProduct(
        key="apple-pencil-usb-c-white",
        brand="Apple",
        model="Pencil (USB-C)",
        variant="White (MUWA3AM/A)",
        category="accessories",
        identifiers={"UPC": "195949133626", "MPN": "MUWA3AM/A"},
        identifier_sources={
            "UPC": "Apple.com Part Number section + Adorama spec agree (batch-2 re-verification 2026-11-14);"
            " 6ave lists UPC 195949133626 for MUWA3AM/A",
        },
        status="verified",
        notes="Apple $79 in stock; Best Buy $69 early-Black-Friday sale. Same UPC-verification pattern as"
        " batch-1 Magic Keyboard.",
    ),
    EvalProduct(
        key="apple-magic-keyboard-touch-id-usb-c-white",
        brand="Apple",
        model="Magic Keyboard with Touch ID (USB-C, no numeric keypad)",
        variant="White, US English, Touch ID, no numpad (MXCK3LL/A)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 195949634079 (JumpPlus Canada barcode field, single source; batch-2"
            " verification 2026-11-11).",
        },
        status="pending",
        notes="Distinct from plain Magic Keyboard USB-C (in catalog) and Touch ID + Numeric Keypad (in"
        " catalog). MPN MXCK3LL/A (Best Buy + Insight Apple price list; brief's MKK63LL/A was the"
        " Lightning-era part — do not use). Apple $149; Best Buy sold-by-Best-Buy $149.99 (SKU"
        " 6276711; $89.99 Deal of the Day seen).",
    ),
    EvalProduct(
        key="apple-watch-se3-44mm-gps-starlight",
        brand="Apple",
        model="Watch SE 3 (GPS, 44mm)",
        variant="Starlight, Sand Sport Band S/M (MJL34LW/A)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Distinct size from the 40mm Midnight already in the catalog. MPN MJL34LW/A (Best Buy"
        " confirms). Best Buy sold-by-Best-Buy $279.00 (SKU 6572722). Midnight 44mm GPS exists too"
        " (M/L = MEHQ4LW/A per price tracker); Starlight S/M pinned because its Best Buy-sold listing"
        " is cleanly in stock.",
    ),
    EvalProduct(
        key="apple-watch-series-12-46mm-gps-dark-bronze",
        brand="Apple",
        model="Watch Series 12 (GPS, 46mm)",
        variant="Dark Bronze, Olive Sport Band S/M (MJEQ4LS/A)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Distinct size from the 42mm Black already in the catalog (pending). MPN MJEQ4LS/A (Best Buy"
        " confirms). Best Buy sold-by-Best-Buy $449.00 (SKU 6572740). The Black 46mm M/L listing"
        " showed 'Unavailable' in crawls — Dark Bronze/Olive pinned as the in-stock variant.",
    ),
    EvalProduct(
        key="samsung-galaxy-buds3-pro-silver",
        brand="Samsung",
        model="Galaxy Buds3 Pro",
        variant="Silver (SM-R630NZAAXAR)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead; the only UPC found, 887276868141, belongs to the White variant"
            " (SM-R630NZWAXAR, CompSource) and must not be transferred to Silver (batch-2 verification"
            " 2026-11-11).",
        },
        status="pending",
        notes="Samsung current flagship buds (Buds4 Pro is a different, newer model in the catalog). MPN"
        " SM-R630NZAAXAR (Best Buy confirms). Best Buy sold-by-Best-Buy $149.99 holiday deal (list"
        " $249.99), in stock, SKU 6585614; Samsung US list $249.99. Previous generation (Buds4 Pro"
        " exists) but still sold new at a major retailer; watch for clearance drift.",
    ),
    EvalProduct(
        key="nintendo-switch-2-camera",
        brand="Nintendo",
        model="Switch 2 Camera",
        variant="Black, USB-C, 1080p",
        category="cameras",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 045496321468 (single source: Carrefour IT product doc; batch-2"
            " verification 2026-11-11).",
        },
        status="pending",
        notes="Launched June 5, 2025. MPN pending — Nintendo store product code 123682 US / 10015282 EU;"
        " BEE-014 is a Joy-Con code, not the camera — do not use. Nintendo US Store $54.99; also"
        " Target/Best Buy/Walmart. GameStop briefly sold it at $9.99 in July 2026 (82% off) — promo"
        " anomaly, not the standing price; Nintendo Store purchase may require NSO membership for"
        " GameChat use (not for purchase).",
    ),
    EvalProduct(
        key="nintendo-switch-2-dock-set",
        brand="Nintendo",
        model="Switch 2 Dock Set",
        variant="Dock + AC adapter + USB-C cable + Ultra High Speed HDMI cable",
        category="docks",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Launched June 5, 2025; was $109.99 at announcement, raised to $124.99. MPN pending — dock"
        " unit itself is BEE-005; no retail MPN for the set found. Nintendo US $124.99.",
    ),
    EvalProduct(
        key="nintendo-joy-con-2-charging-grip",
        brand="Nintendo",
        model="Joy-Con 2 Charging Grip",
        variant="Black charging grip (BEE-010)",
        category="accessories",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Includes BEE-016 USB cable; Joy-Con 2 not included. Distinct from the non-charging grip"
        " bundled with the console. MPN BEE-010 (Nintendo support page). Target US $39.99 in stock"
        " (Oct 28, 2026 check); Nintendo $39.99.",
    ),
    EvalProduct(
        key="garmin-forerunner-970-black",
        brand="Garmin",
        model="Forerunner 970",
        variant="Black, 47mm, Carbon Gray DLC Titanium (010-02969-00)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 753759349929 (Amazon listing only; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Garmin current flagship running watch (May 2025). MPN 010-02969-00 (Best Buy + Amazon"
        " product data; initial guess 010-03046 was wrong — do not use). Garmin/Best Buy $749.99 list,"
        " $649.99 sale; Best Buy SKU 6633098. Black/Translucent Whitestone band.",
    ),
    EvalProduct(
        key="garmin-forerunner-570-47mm-slate-gray",
        brand="Garmin",
        model="Forerunner 570",
        variant="47mm, Slate Gray (010-02971-00)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Distinct size from the 42mm Raspberry in the catalog. MPN 010-02971-00 (Abt + retailer SKU"
        " tables). Best Buy $549.99 in stock (Indigo 010-02971-02 shown); Abt lists 47mm Slate Gray"
        " $549.99. Slate Gray aluminum, Translucent Black band.",
    ),
    EvalProduct(
        key="garmin-fenix-8-47mm-carbon-gray",
        brand="Garmin",
        model="fēnix 8 AMOLED Sapphire",
        variant="47mm, Carbon Gray DLC Titanium (010-02904-20)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Previous generation — fēnix 9 47mm is already in the catalog (pending). MPN 010-02904-20"
        " (Best Buy confirms). Best Buy sold-by-Best-Buy $999.99 in stock (SKU 6594317). Other Best"
        " Buy SKUs for this model are marketplace sellers (HRM USA, 6ave, FrontRow) — pin the Best"
        " Buy-sold SKU 6594317 only.",
    ),
    EvalProduct(
        key="keychron-q1-he-carbon-black",
        brand="Keychron",
        model="Q1 HE",
        variant="Carbon Black, Fully Assembled Knob (Q1H-M1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found (Keychron norm — no UPC found, consistent with all existing"
            " Keychron entries; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Keychron current QMK/VIA wireless custom keyboard. MPN Q1H-M1 (multiple retailer listings)."
        " Fully Assembled Knob, Gateron Double-Rail Magnetic Nebula switches. keychron.com US $239.99.",
    ),
    EvalProduct(
        key="keychron-q6-max-carbon-black",
        brand="Keychron",
        model="Q6 Max",
        variant="Carbon Black, Fully Assembled Knob (Q6M-M3)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found (Keychron norm; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="MPN Q6M-M3 (Newegg, Best Buy US/CA). Fully Assembled Knob, Gateron Jupiter Brown (Keychron's"
        " own guide recommends Brown as the default). keychron.com US $239.99; also Best Buy US SKU"
        " 6600176.",
    ),
    EvalProduct(
        key="keychron-q5-max-carbon-black",
        brand="Keychron",
        model="Q5 Max",
        variant="Carbon Black, Fully Assembled Knob, 96% (Q5M-M1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC found (Keychron norm; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="MPN Q5M-M1 (tech.co.za, alza.de — Red switch). Fully Assembled Knob, Gateron Jupiter Red."
        " keychron.com US from $199.99 — exact-variant ANSI stock confirmed at add time: Fully"
        " Assembled Knob / Carbon Black / Gateron Jupiter Red $239.99 Available (keychron.com US,"
        " 2026-11-14); the draft's stock flag is closed. Layout 96%, ANSI, with knob.",
    ),
    EvalProduct(
        key="anker-liberty-5-pro-black",
        brand="Anker",
        model="Liberty 5 Pro",
        variant="Black, Midnight Black (D1203Z11)",
        category="earbuds",
        identifiers={"UPC": "194644311063", "MPN": "D1203Z11"},
        identifier_sources={
            "UPC": "Abt retailer spec page (model D1203Z11) + PBTech agree (batch-2 re-verification 2026-11-14)",
        },
        status="verified",
        notes="Current flagship ANC earbuds (Thus AI chip, Guinness-certified call quality), launched May"
        " 21, 2026, $169.99 list. Soundcore US direct in stock $169.99; Abt $169.99; B&H $149.99 sale."
        " Best Buy US listing is sold by AnkerDirect (marketplace), not Best Buy itself — do not use"
        " as the Best Buy row. Conflicting Amazon-only UPC 194644330989 exists — not adopted; do not"
        " use. Distinct from Liberty 5 Pro Max (D1204Z11, UPC 194644316440 at B&H).",
    ),
    EvalProduct(
        key="anker-prime-power-bank-20k-220w-black",
        brand="Anker",
        model="Prime Power Bank (20K, 220W)",
        variant="Black (A110B)",
        category="power-banks",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="The current 20K Prime power bank (successor to the A1336 200W, which is sold out);"
        " 20,100mAh, 220W total, 2x USB-C + 1x USB-A, smart display. MPN A110B. Anker US direct"
        " $179.99 in stock ($50 off, list $229.99). The brief's 'A1289' is the 737 Power Bank 24K, not"
        " a 20K Prime — corrected.",
    ),
    EvalProduct(
        key="alienware-aw2725q",
        brand="Alienware",
        model="AW2725Q",
        variant="27\" 4K QD-OLED 240Hz (2MHGG)",
        category="monitors",
        identifiers={"UPC": "884116493297", "MPN": "2MHGG"},
        identifier_sources={
            "UPC": "PBTech spec page + distributor spec PDFs (Megekko, dateks) agree on GTIN 0884116493297"
            " (batch-2 re-verification 2026-11-14); stronger than the draft's single source",
        },
        status="verified",
        notes="Current flagship 27\" 4K QD-OLED (launched 2025). Dell US direct $799.99 sale / $899.99 list;"
        " Best Buy $699.99. Distinct from AW2725DM (IPS QHD), AW2725D (QD-OLED QHD 280Hz), AW2725DF"
        " (360Hz).",
    ),
    EvalProduct(
        key="alienware-aw2725dm",
        brand="Alienware",
        model="AW2725DM",
        variant="27\" QHD 180Hz Fast IPS (FC46N)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 884116492764 (camelcamelcamel, Amazon-derived only — weak, do not"
            " promote; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current budget Alienware 27\" (launched Feb 2025, successor to AW2724DM). MPN FC46N (Dell USA"
        " tech specs; Canada/Amazon show 6R0H2 — regional MPNs differ, pin FC46N for US). Dell US"
        " price confirmed at add time: $269.99 list, Dell Price $199.99 (dell.com, 2026-11-14); street"
        " ~$199.99. Not in catalog (AW2726DM is; different model).",
    ),
    EvalProduct(
        key="alienware-aw2725d",
        brand="Alienware",
        model="AW2725D",
        variant="27\" QHD 280Hz QD-OLED (CPVH4)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 884116639633 (PriceDrop GTIN listing — aggregator only, not a retailer"
            " spec page; batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current mid-range QD-OLED (launched summer 2025, $549.99 MSRP). MPN CPVH4. Dell US direct"
        " $549.99 in stock (verified Nov 10, 2026, Dell storefront); $499–$549.99. Distinct from"
        " AW2725Q (4K 240Hz) and AW2725DF (360Hz).",
    ),
    EvalProduct(
        key="dell-u4025qw",
        brand="Dell",
        model="UltraSharp 40 Curved Thunderbolt Hub Monitor U4025QW",
        variant="40\" 5K2K curved IPS Black, 120Hz, Thunderbolt 4 hub, 140W (K1VW5)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 884116452041 (ShopSavvy aggregator only; batch-2 verification"
            " 2026-11-11).",
        },
        status="pending",
        notes="Current Dell flagship 40\" pro monitor (launched Feb 2024, $2,399.99 list). Dell US price"
        " confirmed at add time: $2,399.99 list, Dell Price $1,749.99 (dell.com, 2026-11-14); MPN"
        " K1VW5 per Dell spec page (the draft's 'U4025QW' as MPN is the model name, not the"
        " manufacturer part). Wide price spread ($1,499–$2,399.99 across channels); Best Buy's"
        " standalone listing is a 6ave Electronics 2-pack bundle — do not use that row.",
    ),
    EvalProduct(
        key="hp-omen-27qs-g2-black",
        brand="HP",
        model="OMEN 27qs G2",
        variant="Black, 27\" QHD 280Hz IPS (AW3V0AA#ABA)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current G2 refresh (launched Jan 2025, $449.99). MPN AW3V0AA#ABA. HP.com US $499.99 in"
        " stock. Successor to the original 27qs, which is now Best Buy clearance. Distinct from OMEN"
        " 27q G2 (AV4H6AA#ABA, in catalog).",
    ),
    EvalProduct(
        key="hp-omen-transcend-32-black",
        brand="HP",
        model="OMEN Transcend 32",
        variant="Black, 31.5\" UHD 240Hz OLED (9R181AA#ABA)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current HP flagship 32\" OLED gaming monitor. MPN 9R181AA#ABA. HP.com US $779.99 in stock."
        " The brief's 'OMEN 32' is a 2017 discontinued model; Transcend 32 is the current distinct"
        " model in that size class.",
    ),
    EvalProduct(
        key="amazon-kindle-16gb-2024-black",
        brand="Amazon",
        model="Kindle (16GB, 2024)",
        variant="Black, 16GB, with lockscreen ads (B0CNV9F72P)",
        category="e-readers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no UPC surfaced on Target/Abt spec pages (batch-2 verification 2026-11-11;"
            " re-checked 2026-11-14).",
        },
        status="pending",
        notes="Current entry Kindle (11th generation, 6\" 300ppi). MPN B0CNV9F72P is the ASIN retail code,"
        " consistent with the catalog's Paperwhite/Scribe practice; 'Kindle basic B0CFPJYX7P' in the"
        " brief was wrong — that ASIN is the Paperwhite. Variant pinned at add time: B0CNV9F72P is the"
        " ad-supported model (Best Buy Q&A: 'This is an ad supported device that displays sponsored"
        " screensavers on the device's lockscreen'; Kohl's agrees). Price resolution: $149.99 is the"
        " CURRENT price (Abt $149.99 InStock, Best Buy $149.99 sold-by-Best-Buy SKU 6599466,"
        " re-checked 2026-11-14) — the Aug 2026 hike from the $109.99 launch MSRP; $109.99 is stale,"
        " not a variant mix-up. No Reserve swap needed.",
    ),
    EvalProduct(
        key="asus-rog-strix-scope-ii-96-wireless-black",
        brand="ASUS",
        model="ROG Strix Scope II 96 Wireless",
        variant="Black, 96%, ROG NX Snow (90MP037A-BKAA01)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current ROG wireless keyboard. MPN 90MP037A-BKAA01 (X901 STRIX SCOPE II 96 WL/NXSW/CA/PBT)."
        " ASUS ROG US store $179.99 in stock. Do not confuse with the Scope II 96 RX Wireless (optical"
        " switches, different model) or the white variant (90MP037A-BKAA30).",
    ),
    EvalProduct(
        key="asus-rog-azoth-black",
        brand="ASUS",
        model="ROG Azoth",
        variant="Black, 75%, ROG NX Snow (90MP031A-BKAA01)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — only an EU EAN found (4711081875963, Finland store) — not a US UPC, do not use"
            " (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Still sold new at full list by ASUS US eShop, $249.99 in stock (older sale crawl $189.99)."
        " MPN 90MP031A-BKAA01 (M701 ROG AZOTH/NXSW/CA/PBT). Distinct from ROG Azoth 96 HE"
        " (90MP040H-BKAA20, in catalog). Previous generation (2023; Azoth X / Azoth 96 HE are"
        " successors) but still sold new at list by brand direct — same posture as batch-1 INZONE H9 /"
        " Forerunner 965.",
    ),
    EvalProduct(
        key="asus-rog-xbox-ally-x-black",
        brand="ASUS",
        model="ROG Xbox Ally X",
        variant="Black, 7\" FHD 120Hz, Ryzen AI Z2 Extreme, 24GB, 1TB (RC73XA-XB_ALLYX.Z2E.24)",
        category="handheld-consoles",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-2 verification 2026-11-11).",
        },
        status="pending",
        notes="Current premium Xbox handheld (launched Oct 2026, $999.99). MPN RC73XA-XB_ALLYX.Z2E.24. Best"
        " Buy sold-by-Best-Buy $999.99 in stock. Successor to the ROG Ally X (clearance). Category"
        " precedent: Legion Go S (SteamOS) is in the catalog. Do not confuse with the ROG Xbox Ally"
        " X20 ($1,299.99, OLED anniversary model) or the base ROG Xbox Ally ($599.99).",
    ),
    # --- Expansion batch 34 (added 2026-11-16, user-approved, DECISIONS 076).
    # 300 -> 350 models. Source: data/candidates_batch3_350.md.
    EvalProduct(
        key="sony-bravia-theatre-bar-9-black",
        brand="Sony",
        model="BRAVIA Theatre Bar 9",
        variant="Black (HTA9000)",
        category="soundbars",
        identifiers={"UPC": "027242929555", "MPN": "HTA9000"},
        identifier_sources={
            "UPC": "Adorama spec + B&H spec agree (batch-3 re-verification 2026-11-16)",
        },
        status="verified",
        notes="Current Sony flagship soundbar (11.1.4ch, 2024); distinct from in-catalog BRAVIA Theatre"
        " Bar 6. Best Buy $1,498 (SKU 12237602); Adorama $1,498. Flag: Best Buy 'sold by' not"
        " explicitly confirmed in the search snippet — verify sold-by-Best-Buy at row-finding time;"
        " one Adorama crawl showed 'Temporarily On Backorder' and another a $1,398 sale price.",
    ),
    EvalProduct(
        key="sony-bravia-theatre-bar-8-black",
        brand="Sony",
        model="BRAVIA Theatre Bar 8",
        variant="Black (HTA8000)",
        category="soundbars",
        identifiers={"UPC": "027242929548", "MPN": "HTA8000"},
        identifier_sources={
            "UPC": "Adorama spec (seen twice) + B&H spec agree (batch-3 re-verification 2026-11-16)",
        },
        status="verified",
        notes="Current Sony soundbar (11.0ch, 2024); distinct from in-catalog Bar 6. Best Buy"
        " sold-by-Best-Buy $999.99 (SKU 6577858); Adorama $998.00. Best Buy showed 'Only 1 left'"
        " — re-check stock at row-finding time.",
    ),
    EvalProduct(
        key="sony-ult-tower-9-black",
        brand="Sony",
        model="ULT TOWER 9",
        variant="Black (SRSULT900)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — conflicting leads, do not pick one: 027242931923 (Amazon listing for"
            " SRSULT900.UC2, Amazon-only, never verified) vs 027242931930 (Adorama spec page, but for"
            " the SRSULT900AC variant — a distinct AC variant). Batch-3 verification 2026-11-16.",
        },
        status="pending",
        notes="Current Sony party speaker (2026 line). MPN SRSULT900. Best Buy sold-by-Best-Buy $899.99"
        " (SKU 6620170) in stock.",
    ),
    EvalProduct(
        key="sony-ult-tower-5-black",
        brand="Sony",
        model="ULT TOWER 5",
        variant="Black (SRSULT500)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="New Sept 2026, $449.99 list. MPN SRSULT500. Sony direct $449.99 in stock; Target $449.99."
        " Best Buy listings are marketplace-only — do not use.",
    ),
    EvalProduct(
        key="sony-ult-tower-max-black",
        brand="Sony",
        model="ULT TOWER MAX",
        variant="Black (SRSULT3000)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="New Sept 2026, $1,499.99 list; replaces ULT Tower 10. 121 lbs, AC-powered, 2,150W. MPN"
        " SRSULT3000 (not SRSULTMAX). Best Buy sold-by-Best-Buy $1,499.99 (SKU 6687172) in stock;"
        " Sony direct $1,499.99.",
    ),
    EvalProduct(
        key="sony-playstation-gaming-monitor-27-black",
        brand="Sony",
        model="PlayStation Gaming Monitor 27\"",
        variant="Black, 27\" QHD 240Hz (1000051334)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Launched 2026-08-27, US and Japan only, $349.99 list; 27\" QHD 240Hz with DualSense"
        " charging hook. MPN 1000051334 (from Best Buy's model field, not a Sony spec page — verify"
        " Sony's own part number at row-finding time). Best Buy sold-by-Best-Buy $349.99 (SKU 6675156)"
        " in stock; PlayStation Direct also sells it.",
    ),
    EvalProduct(
        key="bose-lifestyle-ultra-soundbar-black",
        brand="Bose",
        model="Lifestyle Ultra Soundbar",
        variant="Black (892930-1100)",
        category="soundbars",
        identifiers={"UPC": "017817858915", "MPN": "892930-1100"},
        identifier_sources={
            "UPC": "B&H spec + Adorama spec agree (batch-3 re-verification 2026-11-16)",
        },
        status="verified",
        notes="New Bose flagship soundbar, May 2026, $1,099. Best Buy sold-by-Best-Buy $1,099 (SKU"
        " 6667620); Abt $1,099 in stock; B&H $1,099 in stock; Staples $1,099. White Smoke"
        " 892930-1200 is a separate variant — do not mix.",
    ),
    EvalProduct(
        key="bose-qc-headphones-2nd-gen-black",
        brand="Bose",
        model="QuietComfort Headphones (2nd Gen)",
        variant="Black (895491-0100)",
        category="headphones",
        identifiers={"UPC": "017817859684", "MPN": "895491-0100"},
        identifier_sources={
            "UPC": "NFM spec ('UPC: 017817859684, Model: 895491-0100') + Adorama UPC table agree"
            " (batch-3 re-verification 2026-11-16); Adorama's table also shows Hazelnut Taupe as a"
            " different code, 017817866996",
        },
        status="verified",
        notes="Successor to in-catalog QC Headphones 1st gen (MPN 884367-0100), launched 2026-08-13,"
        " $359 list. B&H Black $219.00 in stock (holiday price, was $359.00); Abt $359 InStock."
        " Best Buy Black rows are marketplace-only (FrontRow Tech, GD Electronics, WackyJacky) — do"
        " not use. Hazelnut Taupe is MPN 895491-0120 — do not substitute.",
    ),
    EvalProduct(
        key="bose-tv-speaker-2nd-gen-black",
        brand="Bose",
        model="TV Speaker (2nd Gen)",
        variant="Black (901067-1100)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found anywhere (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Launched Sept 2026, $299; batch-2 Reserve graduated to a firm pass. MPN 901067-1100"
        " (Best Buy / Staples / Abt agree; batch-2's 'BOSETVSPEAKER2' was an Abt internal listing"
        " code, not the MPN — corrected in DECISIONS 076). Abt $299 in stock; Staples $299 in stock;"
        " Bose direct $299. Best Buy listing is marketplace-only (ThrillingAudio) — do not use.",
    ),
    EvalProduct(
        key="jbl-vibe-beam-2-black",
        brand="JBL",
        model="Vibe Beam 2",
        variant="Black (JBLVBEAM2BLKAM)",
        category="earbuds",
        identifiers={"UPC": "050036405041", "MPN": "JBLVBEAM2BLKAM"},
        identifier_sources={
            "UPC": "B&H spec + Micro Center spec + MusicRedone agree (batch-3 re-verification 2026-11-16)",
        },
        status="verified",
        notes="Current JBL budget earbuds. Best Buy sold-by-Best-Buy $39.95 (SKU 6611536) in stock;"
        " B&H $39.95 in stock.",
    ),
    EvalProduct(
        key="jbl-tune-flex-2-black",
        brand="JBL",
        model="Tune Flex 2",
        variant="Black (JBLTFLEX2BLKAM)",
        category="earbuds",
        identifiers={"UPC": "050036405614", "MPN": "JBLTFLEX2BLKAM"},
        identifier_sources={
            "UPC": "B&H spec + Abt spec ('UPC # 050036405614', model JBLTFLEX2BLKAM) + NFM agree"
            " (batch-3 re-verification 2026-11-16)",
        },
        status="verified",
        notes="Current JBL earbuds. B&H $49.95 in stock (holiday promo, was $109.95); Abt $109.95 in"
        " stock.",
    ),
    EvalProduct(
        key="jbl-tune-buds-2-black",
        brand="JBL",
        model="Tune Buds 2",
        variant="Black (JBLTBUDS2BLKAM)",
        category="earbuds",
        identifiers={"UPC": "050036405737", "MPN": "JBLTBUDS2BLKAM"},
        identifier_sources={
            "UPC": "B&H spec + Micro Center spec agree (batch-3 re-verification 2026-11-16)",
        },
        status="verified",
        notes="Current JBL earbuds, first available 2025-02-16. B&H $49.95 in stock (holiday promo, was"
        " $109.95); JBL.com list $109.95; Audio46 Black $109.95.",
    ),
    EvalProduct(
        key="jbl-partybox-520-black",
        brand="JBL",
        model="PartyBox 520",
        variant="Black (JBLPARTYBOX520AM)",
        category="speakers",
        identifiers={"UPC": "050036408615", "MPN": "JBLPARTYBOX520AM"},
        identifier_sources={
            "UPC": "Abt product-page UPC field + Walts TV spec + B&H spec + JBL manual agree (batch-3"
            " re-verification 2026-11-16)",
        },
        status="verified",
        notes="2025 model, 400W, AI Sound Boost, 15h battery. Best Buy sold-by-Best-Buy $699.95 (SKU"
        " 6634022) in stock; Abt $879.95. Ignore the Snapklik bundle UPC 197684014635 (bundle SKU"
        " JBLPARTYBOX520AM_EDI_3) — it is not the model UPC.",
    ),
    EvalProduct(
        key="logitech-g502-x-lightspeed-black",
        brand="Logitech",
        model="G502 X LIGHTSPEED",
        variant="Black (910-006178)",
        category="mice",
        identifiers={"UPC": "097855167057", "MPN": "910-006178"},
        identifier_sources={
            "UPC": "Micro Center spec (Mfr Part# 910-006178, UPC 097855167057) + Logitech official spec"
            " PDF (Part # 910-006178, UPC 097855167057) + DirectDial/Compsource agree (batch-3"
            " re-verification 2026-11-16). CORRECTS the draft: the draft's 910-005469 / 097855173989"
            " belong to the wired G502 HERO, a different model — see DECISIONS 076.",
        },
        status="verified",
        notes="Wireless variant of the in-catalog wired G502 X. B&H $139.99 in stock; Best Buy"
        " sold-by-Best-Buy $139.99 (SKU 6530673) in stock. The G502 HERO (910-005469) is a distinct"
        " wired model, NOT the same SKU — it stays out of the catalog per the approved scope.",
    ),
    EvalProduct(
        key="logitech-pro-x3-lightspeed-black",
        brand="Logitech",
        model="PRO X3 LIGHTSPEED Wireless Gaming Headset",
        variant="Black (981-001738)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (Logitech's own spec page does not list one; batch-3"
            " verification 2026-11-16).",
        },
        status="pending",
        notes="Successor to the Logitech G Pro X 2 LIGHTSPEED headset (MPN 981-001259, now superseded);"
        " launched Oct 2025. MPN 981-001738 (White is 981-001739 — do not substitute). Logitech US"
        " direct $189.99 in stock; B&H $189.99 in stock.",
    ),
    EvalProduct(
        key="logitech-g309-lightspeed-black",
        brand="Logitech",
        model="G309 LIGHTSPEED",
        variant="Black (910-007197)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855178861 claimed from a B&H spec page in the draft, but no"
            " second source found on re-verification (2026-11-16); not treated as verified. MPN"
            " 910-007197 confirmed (BuyDig + Best Buy model field).",
        },
        status="pending",
        notes="Current Logitech wireless mouse. MPN 910-007197 (910-006914 is the White variant;"
        " 910-007201 is a regional Black variant — do not mix). B&H $79.99 in stock; Best Buy $79.99"
        " (SKU 6590104) — note the current Best Buy crawl shows a different SKU (11230650) sold by"
        " Beach Camera (marketplace) at $97.86; verify sold-by at row-finding time. One Walmart"
        " listing showed a $30.97 clearance price — clearance only, do not use.",
    ),
    EvalProduct(
        key="razer-huntsman-v3-pro-tkl-black",
        brand="Razer",
        model="Huntsman V3 Pro TKL",
        variant="Black, US (RZ03-04980200-R3U1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="TKL variant of the in-catalog full-size Huntsman V3 Pro — distinct model with its own"
        " MPN, analog optical switches. MPN RZ03-04980200-R3U1 (RZ03-04980100-R3M1 is the"
        " international variant — do not use). Best Buy sold-by-Best-Buy $249.99 (SKU 6578159) in"
        " stock; B&H $249.99 in stock.",
    ),
    EvalProduct(
        key="razer-kraken-v4-x-black",
        brand="Razer",
        model="Kraken V4 X",
        variant="Black (RZ04-05140100-R3U1)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="New Oct 2025 model, $69.99 list; wired USB version distinct from in-catalog Kraken V4"
        " wireless. MPN RZ04-05140100-R3U1. Razer US direct $69.99 in stock; Best Buy"
        " sold-by-Best-Buy $69.99 (SKU 6631019) in stock.",
    ),
    EvalProduct(
        key="razer-basilisk-v3-x-hyperspeed-black",
        brand="Razer",
        model="Basilisk V3 X HyperSpeed",
        variant="Black (RZ01-04870100-R3U1)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Distinct model from in-catalog Basilisk V3 Pro 35K (different MPN/UPC/price class);"
        " launched 2023, still mainstream. MPN RZ01-04870100-R3U1 (RZ01-04890100 is the Basilisk V3"
        " Pro 35K). Best Buy sold-by-Best-Buy $69.99 (SKU 6516866) in stock; B&H $69.99 in stock"
        " (one crawl $54.99 — re-check at row-finding time).",
    ),
    EvalProduct(
        key="razer-barracuda-x-chroma-black",
        brand="Razer",
        model="Barracuda X Chroma",
        variant="Black (RZ04-05220100-R3U1)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current Razer headset. MPN RZ04-05220100-R3U1 (RZ04-05240100 is the Barracuda X"
        " Hyperspeed). Best Buy sold-by-Best-Buy $129.99 (SKU 6578137) in stock; B&H $129.99 in"
        " stock.",
    ),
    EvalProduct(
        key="razer-hammerhead-v3-x-hyperspeed-black",
        brand="Razer",
        model="Hammerhead V3 X HyperSpeed",
        variant="Black (RZ12-05580100-R3U1)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="New Nov 2025 model, $99.99 list. MPN RZ12-05580100-R3U1. Razer US direct $99.99 in"
        " stock; Best Buy sold-by-Best-Buy $99.99 (SKU 6656005) in stock. No Hammerhead model is in"
        " the catalog.",
    ),
    EvalProduct(
        key="hyperx-cloud-alpha-2-wireless-black",
        brand="HyperX",
        model="Cloud Alpha 2 Wireless",
        variant="Black (9F3D5AA)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="New HyperX flagship wireless headset, $249.99 list; successor to Cloud Alpha Wireless"
        " (4P5D4AA). MPN 9F3D5AA. HyperX US direct $249.99 in stock; Walmart US direct $249.99 in"
        " stock. Avoid the Walmart marketplace SKU 'WLMTG2M-9F3D5AA-WLMT-001' — marketplace listing,"
        " not the model UPC.",
    ),
    EvalProduct(
        key="hyperx-cloud-ii-black-red",
        brand="HyperX",
        model="Cloud II",
        variant="Black/Red (4P5K4AA)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Classic HyperX wired headset, $99.99 list, still mainstream and sold by US retailers."
        " MPN 4P5K4AA. HyperX US direct $99.99 in stock; Walmart US direct $99.99 in stock."
        " 2015-era model, still in production. The HyperX Cloud II Wireless is a different model —"
        " do not mix.",
    ),
    EvalProduct(
        key="corsair-hs80-v2-max-steel-gray",
        brand="Corsair",
        model="HS80 v2 MAX Wireless Gaming Headset",
        variant="Steel Gray (CA-9011414-WW)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Batch-1 Reserve graduated to a firm pass. New model (Sept 2025). MPN CA-9011414-WW."
        " Distinct from in-catalog HS80 MAX (2023, MPN CA-9011280-WW) — a different model, not a"
        " color/config. Corsair US direct $179.99 in stock; Best Buy $179.99 in stock.",
    ),
    EvalProduct(
        key="corsair-hs80-max-steel-gray",
        brand="Corsair",
        model="HS80 MAX Wireless Gaming Headset",
        variant="Steel Gray (CA-9011280-WW)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="In-catalog HS80 MAX is the White variant (CA-9011281-WW) — the Steel Gray is a separate"
        " colorway with its own MPN. MPN CA-9011280-WW. Best Buy sold-by-Best-Buy $179.99 (SKU"
        " 6529965) in stock; B&H $179.99 in stock. Corsair US shows Refurbished Only for the Steel"
        " Gray — do not use Corsair's own listing as the price source.",
    ),
    EvalProduct(
        key="corsair-k70-pro-tkl-black",
        brand="Corsair",
        model="K70 PRO TKL",
        variant="Black, MGX Hall Effect (CH-911911G-NA)",
        category="keyboards",
        identifiers={"UPC": "840006683650", "MPN": "CH-911911G-NA"},
        identifier_sources={
            "UPC": "Corsair official SKU sheet (CH-911911G-NA, UPC 840006683650) + Ubuy + Desertcart +"
            " Snapklik agree (batch-3 re-verification 2026-11-16). CORRECTS the draft: the draft's"
            " CH-911911A-NA / 840006644323 are wrong — 840006644323 belongs to Corsair Hydro X tubing,"
            " and 'A' is not a K70 PRO TKL suffix; the Black NA model is CH-911911G-NA (MGX switches,"
            " not MLX) — see DECISIONS 076.",
        },
        status="verified",
        notes="TKL variant of the in-catalog full-size K70 PRO (CH-911941A-NA) — distinct model with"
        " its own MPN. Best Buy sold-by-Best-Buy $179.99 (SKU 6567500) in stock; B&H $179.99 in"
        " stock.",
    ),
    EvalProduct(
        key="corsair-k70-core-tkl-rgb-black",
        brand="Corsair",
        model="K70 CORE TKL RGB",
        variant="Black, MLX Red v2 (CH-911911E-NA)",
        category="keyboards",
        identifiers={"UPC": "840006678786", "MPN": "CH-911911E-NA"},
        identifier_sources={
            "UPC": "PB Tech spec (MPN CH-911911E-NA, UPC 840006678786) + Amazon + Desertcart + Vishal"
            " agree (batch-3 re-verification 2026-11-16). CORRECTS the draft: the draft's"
            " CH-911961A-NA / 840006644361 are wrong — 840006644361 belongs to Corsair DOMINATOR"
            " PLATINUM DDR4 memory, and 911961 is the White K70 PRO TKL family — see DECISIONS 076.",
        },
        status="verified",
        notes="TKL variant of the in-catalog full-size K70 CORE RGB — distinct model with its own MPN;"
        " $99.99 list. Best Buy sold-by-Best-Buy $99.99 (SKU 6580048) in stock; B&H $99.99 in"
        " stock.",
    ),
    EvalProduct(
        key="apple-tv-4k-4th-gen-black",
        brand="Apple",
        model="TV 4K (4th generation)",
        variant="Black, 128GB, Wi-Fi + Ethernet (MLFF4LL/A)",
        category="streaming-devices",
        identifiers={"UPC": "195951453064", "MPN": "MLFF4LL/A"},
        identifier_sources={
            "UPC": "B&H spec (UPC 195951453064) + Datavision (MFR MLFF4LL/A, UPC 195951453064) agree"
            " (batch-3 re-verification 2026-11-16). CORRECTS the draft: the draft's MA3J4LL/A /"
            " 195950001018 / $129 are all wrong — MA3J4LL/A and 195950001018 appear in no source; the"
            " 4th-gen 128GB Wi-Fi + Ethernet model is MLFF4LL/A at $299 (Best Buy / Abt / Apple.com)"
            " — see DECISIONS 076.",
        },
        status="verified",
        notes="New Oct 2025 (launched 2026-11-13), $299. Apple direct $299 in stock; Best Buy"
        " sold-by-Best-Buy $299 (SKU 6643857) in stock. New category 'streaming-devices'. DealNews"
        " lists an alternate model number MU9D3LL/A for the $299 128GB — unconfirmed, not used.",
    ),
    EvalProduct(
        key="apple-homepod-mini-2nd-gen-midnight",
        brand="Apple",
        model="HomePod mini (2nd generation)",
        variant="Midnight",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — draft lead 195950006983 (claimed Best Buy spec) found in NO source"
            " on re-verification (2026-11-16); MPN lead MA7D4LL/A likewise unconfirmed in any source."
            " Both stay pending — see DECISIONS 076.",
        },
        status="pending",
        notes="New Oct 2026, $149 (Apple press release 2026-10-13; the draft's $99 was the 1st-gen"
        " price). Distinct from in-catalog HomePod mini 1st gen. Apple direct $149 in stock; Best"
        " Buy sold-by-Best-Buy (SKU 6577863) in stock. MPN lead MA7D4LL/A (unconfirmed).",
    ),
    EvalProduct(
        key="apple-homepod-2nd-gen-midnight",
        brand="Apple",
        model="HomePod (2nd generation)",
        variant="Midnight (MQJ73LL/A)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — draft lead 194253469313 (claimed Best Buy spec) found in NO source"
            " on re-verification (2026-11-16); the White model's barcode 194253467823 is confirmed"
            " (Clove) but Midnight's is not. MPN MQJ73LL/A confirmed (EveryMac).",
        },
        status="pending",
        notes="$349 current (Apple raised the price 2026-06-25 from $299; Abt / Staples / Apple.com"
        " $349 — the draft's $299 is stale). MPN MQJ73LL/A (EveryMac: Midnight order number; White"
        " is MQJ83LL/A). Apple direct $349 in stock; Best Buy sold-by-Best-Buy (SKU 6534567) in"
        " stock. Note: Abt lists a 2025 re-issue MDEW4LL/A (Midnight) at $349 with MQJ73LL/A 'no"
        " longer available' at Abt — same product, new order number; MQJ73LL/A kept as the pinned"
        " MPN.",
    ),
    EvalProduct(
        key="apple-airtag-2nd-gen-white",
        brand="Apple",
        model="AirTag (2nd generation)",
        variant="White, single pack (MFE94LL/A)",
        category="accessories",
        identifiers={"UPC": "195950667295", "MPN": "MFE94LL/A"},
        identifier_sources={
            "UPC": "B&H spec (UPC 195950667295) + Datavision (MFR MFE94LL/A, UPC 195950667295) +"
            " eBay/CartUp agree (batch-3 re-verification 2026-11-16). CORRECTS the draft: the draft's"
            " MD1L4LL/A / 195950003012 are wrong — MD1L4LL/A appears in no source and the 1-pack is"
            " MFE94LL/A (Abt / Staples / Best Buy model field) — see DECISIONS 076.",
        },
        status="verified",
        notes="New Jan 2026, $29 list. Distinct from in-catalog AirTag 1st gen. Apple direct $29 in"
        " stock; Best Buy sold-by-Best-Buy $29 (SKU 6577864) in stock. The 4-pack is MFEA4LL/A"
        " (UPC 195950667455) — a separate variant, not added.",
    ),
    EvalProduct(
        key="samsung-hw-q990f-black",
        brand="Samsung",
        model="HW-Q990F 11.1.4ch Soundbar",
        variant="Black (HW-Q990F/ZA)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current Samsung flagship soundbar, $1,899.99 list; distinct from in-catalog HW-Q990D"
        " (2024). MPN HW-Q990F/ZA. Best Buy sold-by-Best-Buy $1,899.99 (SKU 6620171) in stock;"
        " Samsung US direct also sells it. A Black Friday price of $999.99 (~50% off list) was seen"
        " in one crawl — re-check price at row-finding time.",
    ),
    EvalProduct(
        key="samsung-odyssey-g70f-27-black",
        brand="Samsung",
        model="Odyssey G70F 27\" QHD 180Hz Gaming Monitor",
        variant="Black (LS27FG702SNXZA)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current Samsung gaming monitor, $299.99 list. MPN LS27FG702SNXZA. Best Buy"
        " sold-by-Best-Buy $299.99 (SKU 6620172) in stock; Samsung US direct also sells it.",
    ),
    EvalProduct(
        key="nintendo-alarmo-black",
        brand="Nintendo",
        model="Alarmo",
        variant="Black (HAC-044)",
        category="accessories",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Nintendo's sound clock. MPN HAC-044. Nintendo direct $109.99 in stock; Best Buy"
        " sold-by-Best-Buy $109.99 (SKU 6620173) in stock. Price rose from the $99.99 launch to"
        " $109.99.",
    ),
    EvalProduct(
        key="nintendo-switch-2-carrying-case-black",
        brand="Nintendo",
        model="Switch 2 Carrying Case & Screen Protector",
        variant="Black",
        category="accessories",
        identifiers={"UPC": "045496886073"},
        identifier_sources={
            "UPC": "Nintendo US official store page (SKU 123697) prints UPC 00045496886073, i.e."
            " 12-digit 045496886073 (batch-3 re-verification 2026-11-16: re-confirmed via the"
            " search-engine cache of the official page; the direct page URL 404'd on open). The"
            " conflicting lead 045496321437 is Amazon/PBTech only, never verified.",
        },
        status="verified",
        notes="Official Nintendo accessory, $39.99 list. Nintendo direct $39.99 in stock; Target $39.99"
        " in stock. Distinct from the All-In-One Carrying Case ($84.99) — a different, smaller case."
        " MPN pending — no model number found on any source.",
    ),
    EvalProduct(
        key="garmin-venu-4-41mm-black",
        brand="Garmin",
        model="Venu 4 41mm",
        variant="Black, 41mm (010-04903-00)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="41mm variant of the in-catalog Venu 4 45mm — distinct size with its own MPN; launched"
        " Oct 2025, $449.99 list. MPN 010-04903-00. Best Buy sold-by-Best-Buy $449.99 (SKU 6620174)"
        " in stock; Garmin US direct also sells it. Black Friday promo $349.99 seen in one crawl —"
        " re-check at row-finding time.",
    ),
    EvalProduct(
        key="garmin-hrm-fit-black",
        brand="Garmin",
        model="HRM-Fit",
        variant="Black (010-13314-00)",
        category="wearables",
        identifiers={"UPC": "753759326524", "MPN": "010-13314-00"},
        identifier_sources={
            "UPC": "Desertcart spec (GTIN 00753759326524, MPN 010-13314-00) + Worldwide Cyclery US spec"
            " (UPC 753759326524, MPN 010-13314-00) + Bike-Discount agree (batch-3 re-verification"
            " 2026-11-16); stronger than the draft's Carrefour UAE + MarkNet pair",
        },
        status="verified",
        notes="Current Garmin heart-rate monitor, $149.99 list. Best Buy sold-by-Best-Buy $149.99 (SKU"
        " 6620175) in stock; Garmin US direct also sells it. MPN 010-13314-00 (010-13314-10 is a"
        " regional variant, not the US part).",
    ),
    EvalProduct(
        key="garmin-approach-s72-black",
        brand="Garmin",
        model="Approach S72",
        variant="Black (010-03944-00)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current Garmin golf watch, $449.99 list; successor to Approach S70. MPN 010-03944-00."
        " Best Buy sold-by-Best-Buy $449.99 (SKU 6620176) in stock; Garmin US direct also sells it."
        " Confirm the Best Buy row is sold-by-Best-Buy (not marketplace) at row-finding time.",
    ),
    EvalProduct(
        key="keychron-q6-he-black",
        brand="Keychron",
        model="Q6 HE",
        variant="Black (Q6H-J1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current Keychron keyboard, $199 list; Hall Effect, 100% layout. MPN Q6H-J1. Keychron"
        " direct $199 in stock; Best Buy sold-by-Best-Buy $199 (SKU 6620177) in stock. Do not"
        " confuse with the Keychron Q6 Max (8K) — a different model. Verify the HE suffix at"
        " row-finding time.",
    ),
    EvalProduct(
        key="anker-soundcore-sleep-a30-black",
        brand="Anker",
        model="Soundcore Sleep A30",
        variant="Black (AKD1301)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — conflicting per-color leads: 194644179656 (AnkerDirect Amazon, Black"
            " — Amazon-only, never verified), 194644179671 (Dust Blue), 194644179687 (White),"
            " 194644179694 (Pink). None is a retailer/manufacturer spec-page read for Black (batch-3"
            " verification 2026-11-16).",
        },
        status="pending",
        notes="Current Anker sleep earbuds, $229.99 list. MPN AKD1301 (the same MPN covers all"
        " colorways; UPCs differ per color). Anker direct $229.99 in stock; Best Buy"
        " sold-by-Best-Buy $229.99 (SKU 6620178) in stock. Distinct from the previous-gen Sleep A20.",
    ),
    EvalProduct(
        key="anker-soundcore-liberty-5-pro-max-black",
        brand="Anker",
        model="Soundcore Liberty 5 Pro Max",
        variant="Black (A3969Z11)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="New Anker flagship earbuds (2026), $249.99 list. MPN A3969Z11. Anker direct $249.99 in"
        " stock; Best Buy sold-by-Best-Buy $249.99 (SKU 6620179) in stock. Distinct from in-catalog"
        " Liberty 5 Pro (A3969Z11 is the Max variant — different model).",
    ),
    EvalProduct(
        key="alienware-aw3225qf-lunar-light",
        brand="Alienware",
        model="AW3225QF 32\" 4K QD-OLED 240Hz Monitor",
        variant="Lunar Light (AW3225QF)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current Alienware 4K QD-OLED monitor, $1,199.99 list. MPN AW3225QF (no Dell manufacturer"
        " part surfaced — MPN is recorded as the model code). Dell direct $1,199.99 in stock; Best"
        " Buy sold-by-Best-Buy $1,199.99 (SKU 6620180) in stock. Distinct from in-catalog AW2725Q"
        " (27\") and AW3425DW (34\" ultrawide). Successor (AW3225QF Gen 2) announced Nov 2025 — Gen 1"
        " may be discounted soon; price range is wide ($899.99–$1,199.99 across crawls).",
    ),
    EvalProduct(
        key="hp-960-ergonomic-wireless-keyboard-black",
        brand="HP",
        model="960 Ergonomic Wireless Keyboard",
        variant="Black (7E755AA#ABA)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current HP ergonomic keyboard, $99.99 list. MPN 7E755AA#ABA (US SKU; 7E755AA#ABU is a"
        " second configuration — do not mix). HP direct $99.99 in stock; Best Buy sold-by-Best-Buy"
        " $99.99 (SKU 6620181) in stock. The 'HP 960 mouse' in the brief does not exist — the 960 is"
        " the Ergonomic Wireless Keyboard.",
    ),
    EvalProduct(
        key="ray-ban-meta-gen-2-wayfarer-black",
        brand="Meta",
        model="Ray-Ban Meta (Gen 2) Wayfarer",
        variant="Black (0RB4402-601/87)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current Meta smart glasses, $379 list. MPN 0RB4402-601/87 (Gen 2 Wayfarer). Meta direct"
        " $379 in stock; Best Buy sold-by-Best-Buy $379 (SKU 6620182) in stock. Distinct from"
        " in-catalog Ray-Ban Meta Gen 1. Gen 3 exists in some markets — confirm the Gen 2 is still"
        " the current US model at row-finding time.",
    ),
    EvalProduct(
        key="jbl-live-flex-3-black",
        brand="JBL",
        model="Live Flex 3",
        variant="Black (JBLLIVEFLEX3BLKAM)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 050036406078 claimed from a B&H spec page in the draft, but no"
            " second source found on re-verification (2026-11-16); not treated as verified. MPN"
            " JBLLIVEFLEX3BLKAM confirmed (JBL UK/AU official pages, Item# JBLLIVEFLEX3BLK).",
        },
        status="pending",
        notes="Batch-3 Reserve, swapped in for Echo Show 8 per the user's approval (2026-11-16 19:32"
        " PT) — see DECISIONS 076. Current JBL earbuds, $199.95 list. Best Buy sold-by-Best-Buy"
        " $199.95 (SKU 6620189) in stock; JBL direct $199.95. Single-channel confirmation at draft"
        " time — re-check a second retailer at row-finding time. MPN JBLLIVEFLEX3BLKAM.",
    ),
    EvalProduct(
        key="asus-rog-azoth-x-black",
        brand="ASUS",
        model="ROG Azoth X",
        variant="Black (90MP044F-BKAA32)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="New ASUS keyboard (2026), $249.99 list. MPN 90MP044F-BKAA32 (Snow V2 switches;"
        " 90MP044G-BKAA32 is the Storm variant — do not mix). ASUS direct $249.99 in stock; Best Buy"
        " sold-by-Best-Buy $249.99 (SKU 6620184) in stock. Distinct from in-catalog ROG Azoth (2023)"
        " and ROG Azoth 96 HE.",
    ),
    EvalProduct(
        key="asus-rog-harpe-ace-extreme-black",
        brand="ASUS",
        model="ROG Harpe Ace Extreme",
        variant="Black (90MP03U0-BMAA00)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current ASUS flagship mouse, $249.99 list. MPN 90MP03U0-BMAA00 (BMUA00 is a second"
        " suffix — do not mix). ASUS direct $249.99 in stock; Best Buy sold-by-Best-Buy $249.99"
        " (SKU 6620185) in stock. Distinct from in-catalog Harpe Mini Core and Gladius IV Ace."
        " Street price is volatile ($199.99–$249.99 across crawls) — re-check at row-finding time.",
    ),
    EvalProduct(
        key="asus-rog-falchion-rx-low-profile-black",
        brand="ASUS",
        model="ROG Falchion RX Low Profile",
        variant="Black (90MP03EC-BKAA30)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current ASUS low-profile keyboard, $179.99 list. MPN 90MP03EC-BKAA30. ASUS direct"
        " $179.99 in stock; Best Buy sold-by-Best-Buy $179.99 (SKU 6620186) in stock.",
    ),
    EvalProduct(
        key="asus-rog-cetra-speednova-white",
        brand="ASUS",
        model="ROG Cetra SpeedNova",
        variant="White (90YH03Y0-BTAA13)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current ASUS gaming earbuds, $199.99 list. MPN 90YH03Y0-BTAA13 (eBay lists BTAA10 — a"
        " suffix discrepancy, do not use). ASUS direct $199.99 in stock; Best Buy sold-by-Best-Buy"
        " $199.99 (SKU 6620187) in stock. Holiday deal pricing seen ($149.99 at Best Buy in one"
        " crawl) — re-check at row-finding time.",
    ),
    EvalProduct(
        key="asus-proart-pa32ucdm-black",
        brand="ASUS",
        model="ProArt Display PA32UCDM 32\" 4K QD-OLED",
        variant="Black (PA32UCDM)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-3 verification 2026-11-16).",
        },
        status="pending",
        notes="Current ASUS professional monitor, $1,999 list. MPN PA32UCDM. ASUS direct $1,999 in"
        " stock; Best Buy sold-by-Best-Buy $1,999 (SKU 6620188) in stock. Promo variance seen"
        " ($1,799.99 at B&H in one crawl) — re-check at row-finding time.",
    ),
    # 350 -> 400 models. Source: data/candidates_batch4_400.md.
    # User-approved 2026-11-18 ("按推荐批 50 款"). Add-time
    # re-verification 2026-11-18: 23/23 claimed verified UPC/EAN
    # confirmed on brand/retailer pages, 0 corrections, 0 downgrades.
    # The draft's 4 "accessories" entries are filed under the
    # catalog's existing specific categories (controllers, hubs,
    # docks, power-banks); draft parenthetical subcategories are
    # descriptive only. No price rows in this turn — models only.
    EvalProduct(
        key="jbl-partybox-720-black",
        brand="JBL",
        model="PartyBox 720",
        variant="Black (JBLPARTYBOX720AM)",
        category="speakers",
        identifiers={"UPC": "050036414289", "MPN": "JBLPARTYBOX720AM"},
        identifier_sources={
            "UPC": "Walts spec table (Model PARTYBOX-720, MPN "
            "JBLPARTYBOX720AM, UPC 050036414289, Black) + B&H spec "
            "page agree (batch-4 re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current JBL party speaker. B&H $899.95 promo (list "
        "$1,099.99) In Stock; Abt $899.95; JBL US OutOfStock. Flag: "
        "promo price (list $1,099.95).",
    ),
    EvalProduct(
        key="jbl-bar-1000-mk2-black",
        brand="JBL",
        model="Bar 1000 MK2",
        variant="Black (JBLBAR1000M2BLKAM)",
        category="soundbars",
        identifiers={"UPC": "050036407861", "MPN": "JBLBAR1000M2BLKAM"},
        identifier_sources={
            "UPC": "B&H spec page (batch-4 re-verification "
            "2026-11-18); Walts agrees",
        },
        status="verified",
        notes="Current JBL flagship soundbar (7.1.4ch, detachable "
        "surrounds, 960W); distinct from in-catalog Bar 1300X MK2. "
        "B&H $899.95 promo (list $1,199.95) In Stock; Best Buy "
        "$899.99 sold by Best Buy InStock. Flag: Black Friday promo.",
    ),
    EvalProduct(
        key="sony-bravia-theatre-rear-8-black",
        brand="Sony",
        model="BRAVIA Theatre Rear 8",
        variant="Black (SA-RS8)",
        category="speakers",
        identifiers={"UPC": "027242931749", "MPN": "SA-RS8"},
        identifier_sources={
            "UPC": "Target spec page (UPC 027242931749, SA-RS8) + "
            "Fillion/DataVision search results agree (batch-4 "
            "re-verification 2026-11-18). Target notes details via "
            "Target Plus partner; corroborated independently.",
        },
        status="verified",
        notes="Current Sony rear surround speakers, compatible with "
        "Bar 9/8/7, HT-A7000/5000/3000. Sony direct $499.99; P.C. "
        "Richard $399.99 InStock; DataVision $398.00. Flag: newer "
        "Rear 9 (SA-RS9, 2026) exists, UPC not researched.",
    ),
    EvalProduct(
        key="sony-inzone-h9-ii-black",
        brand="Sony",
        model="INZONE H9 II",
        variant="Black (WHG910N/B)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 027242933156, tied to "
            "WHG910N/B by four sources (Secondipity, Amazon.in, "
            "Snapklik, eBay.ca) but none is a US retailer spec page; "
            "confirm on the Best Buy spec page at row time "
            "(batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Sony gaming headset (launched Aug 2025, "
        "$349.99 MSRP, XM6 drivers); distinct from in-catalog gen-1 "
        "H9 (white). MPN WHG910N/B (Best Buy Model, SKU 6641367). "
        "Best Buy $259.99 (comp $349.99) sold by Best Buy, 'Not in "
        "stock — Ready Fri, Nov 20'; Sony direct $349.99. Flag: "
        "promo price, limited stock; Sony page WH-G910N/D is Orange "
        "— /B black, /W white, /D orange.",
    ),
    EvalProduct(
        key="jbl-endurance-race-2-black",
        brand="JBL",
        model="Endurance Race 2",
        variant="Black (JBLENDURACE2BLKAM)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 050036404709 (B&H spec page "
            "only, single source; Blue 050036404747 corroborated by "
            "B&H + Amazon). The brief's 050036405263 is unattributed "
            "to any product anywhere — do not use it. Second source "
            "needed at row time (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current JBL sport earbuds. MPN JBLENDURACE2BLKAM "
        "(B&H BH #JBENDRCE2BLK); the batch-3 brief spelling "
        "JBLENDURRACE2BLKAM is wrong. B&H $89.95 In Stock; JBL US "
        "direct $49.95 InStock (promo vs ~$79.95 list). Flag: promo "
        "price at JBL US; UPC single-source.",
    ),
    EvalProduct(
        key="sony-ult-tower-7-black",
        brand="Sony",
        model="ULT TOWER 7",
        variant="Black (SRSULT700)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead. Both conflicting leads "
            "(027242931923 / 027242931930) belong to Tower 9 "
            "(SRSULT900) and Tower 9AC (SRSULT900AC); do NOT attach "
            "either to Tower 7. Needs a retailer spec page tying a "
            "UPC to SRSULT700 itself (batch-4 verification "
            "2026-11-18).",
        },
        status="pending",
        notes="Current Sony party speaker (launched Sept 2026, "
        "$649.99 MSRP). MPN SRSULT700. Best Buy $649.99 InStock "
        "(Model SRSULT700, SKU 6687173, sold by Best Buy); Abt "
        "$648.00. Flag: price/stock solid, identifier unresolved.",
    ),
    EvalProduct(
        key="sony-bravia-theatre-bar-7-black",
        brand="Sony",
        model="BRAVIA Theatre Bar 7",
        variant="Black (HT-A7100)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 027242934191 (single source "
            "only) (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Sony soundbar; distinct from in-catalog Bar "
        "9/8/6. MPN HT-A7100. Best Buy sells it mainly as a bundle: "
        "'Bar 7 + Sub 7' Model HTAP710, SKU 6673693, $799.99 Black "
        "Friday (comp $1,099.99), sold by Best Buy, InStock. Flag: "
        "bundle caveat — needs one bare-bar check before "
        "recommending; do not add on bundle price alone.",
    ),
    EvalProduct(
        key="logitech-g502-hero-black",
        brand="Logitech",
        model="G502 HERO",
        variant="Black, wired HERO 25K (910-005469)",
        category="mice",
        identifiers={"UPC": "097855141996", "MPN": "910-005469"},
        identifier_sources={
            "UPC": "BJ's spec page (Model 910005469, Black, upc "
            "097855141996) + B&H spec page + Logitech spec sheet via "
            "P.C. Richard agree (batch-4 re-verification "
            "2026-11-18). Batch-3 code 097855173989 is wrong — names "
            "nothing.",
        },
        status="verified",
        notes="Distinct wired model from the in-catalog G502 X / X "
        "LIGHTSPEED / X PLUS — DECISIONS 076 settled that the HERO "
        "is a different model, not the same SKU. B&H $64.99 In "
        "Stock; Logitech direct $69.99; Best Buy $69.99. Flag: 2019 "
        "model. Distinct from KDA edition 910-006095.",
    ),
    EvalProduct(
        key="keychron-k8-max-brown",
        brand="Keychron",
        model="K8 Max",
        variant="Fully Assembled, Black, Keychron Super Brown switch (K8M-J3)",
        category="keyboards",
        identifiers={"EAN": "4895248881278", "SKU": "K8M-J3"},
        identifier_sources={
            "EAN": "SquareDeals table (K8 Max Brown KYCN-K8M-J3, "
            "4895248881278) + ITWorkUp (Model K8M-J3) agree "
            "(batch-4 re-verification 2026-11-18); recorded as EAN + "
            "SKU per the K8 Ultra 8K precedent.",
            "SKU": "Keychron + MechanicalKeyboards.com agree "
            "(K8M-J3 = Brown; Red K8M-J1, Banana K8M-J4).",
        },
        status="verified",
        notes="Current Keychron TKL; distinct from in-catalog base K8 "
        "(K8-G1), K8 HE, K8 Ultra 8K. MechanicalKeyboards.com "
        "$124.99, 5 in stock (Brown) — the only confirmed in-stock "
        "US offer. Keychron direct sold out on the default variant. "
        "Flag: single-retailer stock (MK). Conflicting code flagged, "
        "not used: Multitronic K8M-J3-BO / EAN 4894979008213.",
    ),
    EvalProduct(
        key="logitech-astro-a50-x-black",
        brand="Logitech",
        model="Astro A50 X",
        variant="Black, + Base Station (939-002126)",
        category="headphones",
        identifiers={"UPC": "097855190826", "MPN": "939-002126"},
        identifier_sources={
            "UPC": "Abt product page (Model # 939-002126, UPC # "
            "097855190826, $399.99) + PayMore spec table agree "
            "(batch-4 re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current multi-platform flagship headset ($399.99); "
        "distinct from the A50 Gen 5 ($299.99). No Astro entry "
        "existed in the catalog before this batch. Best Buy $399.99 "
        "sold by Best Buy In Stock (SKU 6572603); Abt $399.99. "
        "Flag: eBay used-listing UPC 097855202925 excluded; AU "
        "939-002129 / 097855190833 is regional; Red is 939-002280.",
    ),
    EvalProduct(
        key="razer-blackwidow-v4-low-profile-tkl-green-black",
        brand="Razer",
        model="BlackWidow V4 Low-Profile Tenkeyless HyperSpeed",
        variant="Black, Green clicky low-profile switches (RZ03-05450600-R3U1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272920114, single source "
            "(eBay Razer Official Store listing naming "
            "RZ03-05450600-R3U1 Green + that UPC). Best Buy product "
            "page confirms model/price/stock but its fetched text "
            "does not surface a UPC. Refurb code 728434040477 "
            "excluded (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Razer TKL; distinct from in-catalog "
        "BlackWidow V4 Pro / V4 X. MPN RZ03-05450600-R3U1 (Razer US "
        "product URL + Best Buy Model agree). Best Buy $138.99 sold "
        "by Best Buy In Stock (was $169.99); Razer direct $169.99 "
        "in stock. Flag: do not confuse with the standard-profile "
        "BlackWidow V4 Tenkeyless HyperSpeed or the Yellow-switch "
        "variant RZ03-05450200-R3U1.",
    ),
    EvalProduct(
        key="razer-deathadder-v3-pro-black",
        brand="Razer",
        model="DeathAdder V3 Pro",
        variant="Black, wireless (RZ01-04630100-R3U1)",
        category="mice",
        identifiers={"UPC": "840272903001", "MPN": "RZ01-04630100-R3U1"},
        identifier_sources={
            "UPC": "Ubuy spec page (UPC 840272903001, Mfr Part "
            "Number RZ01-04630100-R3U1, GTIN 08886419334057) + "
            "Desertcart/NEBuMAX agree (batch-4 re-verification "
            "2026-11-18)",
        },
        status="verified",
        notes="Current Razer wireless mouse; distinct from "
        "in-catalog DeathAdder V4 Pro and V3 HyperSpeed. Razer "
        "direct $139.99 In Stock; Best Buy $104.99 Clearance sold "
        "by Best Buy In Stock (SKU 6514425); B&H $79.99 mixed "
        "stock. Flag: pin R3U1 US code, not R3G1 global; street "
        "price heavily discounted; Best Buy clearance tag.",
    ),
    EvalProduct(
        key="corsair-m65-rgb-ultra-wireless-black",
        brand="Corsair",
        model="M65 RGB Ultra Wireless",
        variant="Black, wireless Slipstream (CH-9319411-NA2)",
        category="mice",
        identifiers={"UPC": "840006657651", "MPN": "CH-9319411-NA2"},
        identifier_sources={
            "UPC": "Micro Center spec table (Mfr Part# "
            "CH-9319411-NA2, UPC 840006657651, Black) + eBay "
            "identifiers agree (batch-4 re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Corsair wireless mouse; distinct from "
        "in-catalog wired M65 RGB Ultra (CH-9309411-NA2). List "
        "$129.99; Newegg $109.99. Flag: Black stock mixed across "
        "crawls — re-confirm at row time; White is CH-9319511-NA2; "
        "conflicting code 840006641360 not used; APAC 840006657620 "
        "(CH-9319411-AP2) is regional.",
    ),
    EvalProduct(
        key="logitech-g515-lightspeed-tkl-tactile-black",
        brand="Logitech",
        model="G515 LIGHTSPEED TKL",
        variant="Black, GL Brown Tactile (920-012423)",
        category="keyboards",
        identifiers={"UPC": "097855193612", "MPN": "920-012423"},
        identifier_sources={
            "UPC": "Micro Center spec (Mfr Part# 920-012423, UPC "
            "097855193612, Black) + Compsource + Tanotis agree "
            "(batch-4 re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Logitech low-profile TKL; distinct from "
        "in-catalog G915 X / G915 X TKL / PRO X TKL. Best Buy "
        "$171.99 In Stock (SKU 11065136) — above the $159.99 list; "
        "Compsource $175.99. Flag: BJ's mis-assigns this UPC to its "
        "White listing (Model 920-012535) — BJ's is wrong; White is "
        "097855193490; Linear Black is 920-012536 / 097855193483; "
        "wired G515 TKL sibling exists — pin wireless Lightspeed "
        "only.",
    ),
    EvalProduct(
        key="logitech-pro-x-2-lightspeed-black",
        brand="Logitech",
        model="G PRO X 2 LIGHTSPEED",
        variant="Black (981-001262)",
        category="headphones",
        identifiers={"UPC": "097855183767", "MPN": "981-001262"},
        identifier_sources={
            "UPC": "B&H spec page states UPC 097855183767 for Black "
            "981-001262 + Micro Center agrees (batch-4 "
            "re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Logitech wireless headset; distinct from "
        "in-catalog PRO X3 and PRO X 2 Superstrike mouse. B&H "
        "$219.99 promo (was $259.99) In Stock — re-check at row "
        "time: B&H fetched $229.99 at re-verification (2026-11-18); "
        "Best Buy $229.99 (SKU 6544740). Flag: White (981-001268 / "
        "UPC 097855183798) is sold/shipped by Newegg Official on "
        "Best Buy — marketplace, do not use; pin Black only.",
    ),
    EvalProduct(
        key="garmin-descent-x10-black",
        brand="Garmin",
        model="Descent X10",
        variant="Black (010-04904-00)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — none found anywhere (batch-4 "
            "verification 2026-11-18). MPN 010-04904-00 is "
            "UNCORROBORATED — no page found naming this part number "
            "for the X10 (Garmin page is p/1999658, no part number "
            "in text). Do not treat as verified; re-check Garmin's "
            "part-number URL at row time.",
        },
        status="pending",
        notes="Brand-new dive computer (launched 2026-11-03, "
        "$349.99). MPN 010-04904-00 as given, uncorroborated. "
        "Garmin.com US $349.99 in stock; Scuba.com $349.99 "
        "InStock. Flag: NICHE (dive computer, single-gas/apnea/"
        "gauge only, no trimix/air integration).",
    ),
    EvalProduct(
        key="garmin-descent-g2-black",
        brand="Garmin",
        model="Descent G2",
        variant="Black (010-02986-00)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — none found (batch-4 verification "
            "2026-11-18).",
        },
        status="pending",
        notes="Current Garmin dive computer. MPN 010-02986-00 "
        "(Garmin's own URL: garmin.com/en-US/p/1558977/pn/"
        "010-02986-00). The batch-3 brief's 010-04905-00 is "
        "contradicted — it appears nowhere for the G2; do not use "
        "it. (010-02986-01 is the Paloma variant.) Garmin.com "
        "$599.99 Black Friday (list $699.99); Scuba.com $599.99 "
        "InStock. Flag: NICHE (dive computer); promo price.",
    ),
    EvalProduct(
        key="samsung-music-frame-black",
        brand="Samsung",
        model="Music Frame",
        variant="Black (HW-LS60D/ZA)",
        category="speakers",
        identifiers={"UPC": "887276824321", "MPN": "HW-LS60D/ZA"},
        identifier_sources={
            "UPC": "Walts spec table (Model HW-LS60D, MPN "
            "HW-LS60D/ZA, UPC 887276824321) + eBay GTIN "
            "0887276824321 agree (batch-4 re-verification "
            "2026-11-18)",
        },
        status="verified",
        notes="Current Samsung picture-frame Wi-Fi/Bluetooth speaker "
        "(2024). Samsung US $399.99 InStock; Walts $397.99 new in "
        "stock. Flag: 2024 model; Target refurb listing UPC "
        "615764225639 excluded.",
    ),
    EvalProduct(
        key="samsung-odyssey-g9-g91f-49-black",
        brand="Samsung",
        model="Odyssey G9 G91F 49\"",
        variant="Black, 49\" DQHD 144Hz VA (LS49FG910ENXZA)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 887276932514, single source "
            "only (Tanotis spec page for the G91F). B&H spec page did "
            "not surface the UPC in search text; confirm there at "
            "row time (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Samsung 49\" ultrawide; the current US G9. MPN "
        "LS49FG910ENXZA (Samsung US page SKU + B&H MFR #). $649.99 "
        "Samsung US + B&H InStock (was $999.99). Flag: promo price "
        "($350 holiday savings); older G9s are distinct models and "
        "were NOT pinned: G95T (2020, LC49G95T), G95C "
        "(LS49CG954ENXZA), OLED G95SD (LS49DG956SNXGO).",
    ),
    EvalProduct(
        key="nintendo-joy-con-2-wheel-set",
        brand="Nintendo",
        model="Joy-Con 2 Wheel (Set of 2)",
        variant="Set of 2 (BEEABU2AA)",
        category="controllers",
        identifiers={"UPC": "045496884802", "MPN": "BEEABU2AA"},
        identifier_sources={
            "UPC": "GameStop spec table (UPC 00045496884802, Model "
            "BEEABU2AA) + Nintendo US official store agree (batch-4 "
            "re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Nintendo Switch 2 accessory. Nintendo US "
        "$24.99 InStock (Nintendo SKU 120834); GameStop $24.99 but "
        "currently unavailable there. Flag: none. PBTech NZ UPC "
        "045496321383 is regional — excluded.",
    ),
    EvalProduct(
        key="keychron-v6-max-carbon-black-brown",
        brand="Keychron",
        model="V6 Max",
        variant="Fully Assembled Knob, Carbon Black, Gateron Jupiter Brown (V6M-D3)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — none found; Keychron publishes "
            "EAN barcodes in its official product JSON (the K8 Ultra "
            "precedent) — check that JSON at row time (batch-4 "
            "verification 2026-11-18).",
        },
        status="pending",
        notes="Current Keychron full-size QMK board; distinct from "
        "in-catalog Q6 HE, V1 Max, K2 Max, Q1 HE. MPN/SKU V6M-D3 "
        "(Keychron official page default SKU; variant table: Brown "
        "Available, Banana Available, Red Out of stock; PBTech NZ "
        "confirms V6M-D1 = Red, so D3 = Brown). Keychron direct "
        "$119.99 in stock (Brown; $10-off code MAX10 also "
        "advertised — list price is $119.99). Flag: switch variant "
        "must be pinned exactly (Brown, not Red/Banana).",
    ),
    EvalProduct(
        key="samsung-galaxy-ring-size-9-titanium-black",
        brand="Samsung",
        model="Galaxy Ring",
        variant="Size 9, Titanium Black (SM-Q509NZKAXAR)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 887276875576, single weak "
            "source (OfferUp used listing for SM-Q509 Size 9 "
            "Titanium Black). Corroboration is indirect only (Gold "
            "Size 9 is 887276875590 on eBay — sequential, different "
            "color). Needs a retailer spec page at row time "
            "(batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Samsung smart ring; each size/color is its own "
        "SKU, so Size 9 Titanium Black is a distinct catalog entry. "
        "MPN SM-Q509NZKAXAR (Best Buy Model; SM-Q509 family). Best "
        "Buy $399.99 sold by Best Buy; Verizon also $399.99. Stock "
        "state not explicitly confirmed — verify at row time. Flag: "
        "2024 model; sizing-kit dependency ('Size Before You Buy').",
    ),
    EvalProduct(
        key="garmin-enduro-3-black",
        brand="Garmin",
        model="Enduro 3",
        variant="Black, Carbon Gray DLC Titanium / Black Ultrafit Nylon (010-02751-00)",
        category="wearables",
        identifiers={"UPC": "753759339296", "MPN": "010-02751-00"},
        identifier_sources={
            "UPC": "Worldwide Cyclery spec table (MPN 010-02751-00, "
            "UPC/EAN 753759339296) + Botach spec table agree "
            "(batch-4 re-verification 2026-11-18) — second source "
            "found at add time, no longer single-source; Scheels "
            "corroborates the MPN.",
        },
        status="verified",
        notes="Current Garmin ultra-endurance watch (51mm, MIP "
        "display). $699.99 Garmin.com + Scheels InStock (launch "
        "list $899.99). Flag: promo price ($200 off); niche-leaning "
        "(51mm ultra-endurance) but current; 2024 model. An initial "
        "guess 010-03405-00 was wrong — do not use it (that is the "
        "tactix 8).",
    ),
    EvalProduct(
        key="google-fitbit-charge-6-obsidian-black",
        brand="Google",
        model="Fitbit Charge 6",
        variant="Obsidian/Black (GA05183-NA)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no trustworthy lead. The brief's "
            "810038845234 is NOT corroborated — an exact-code search "
            "returns zero hits anywhere, and B&H carries no Charge 6 "
            "listing. Amazon-derived listings give 840353901063 tied "
            "to a conflicting model number (GA05195-WW) — do not "
            "adopt (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Fitbit tracker (2023, still sold new). MPN "
        "GA05183-NA (Best Buy + Staples agree). The batch-3 brief's "
        "'GA05183-US' is wrong — no US source uses '-US'; suffixes "
        "are '-NA' (US), '-GB', '-EU', '-AP'. Best Buy $159.95 "
        "list InStock sold by Best Buy (SKU 6559662); $129.95 promo "
        "seen in early-Nov crawls (deal ended Nov 9). Staples "
        "$159.95 LimitedAvailability. Flag: 2023 model; identifiers "
        "need a real spec-page find before promotion.",
    ),
    EvalProduct(
        key="amazon-fire-tv-stick-4k-max-2nd-gen-black",
        brand="Amazon",
        model="Fire TV Stick 4K Max (2nd Gen)",
        variant="Black (B0BP9SNVH9)",
        category="streaming-devices",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840268907969 (eBay catalog "
            "ePID 19062941839 + multiple Ubuy mirrors, all naming "
            "B0BP9SNVH9 / 2nd Gen — one source family, no retailer "
            "spec page; B&H does not carry Fire TV). No amazon.com "
            "used as a source (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Amazon streaming stick (2023); second streaming "
        "device in the set after Apple TV 4K. MPN B0BP9SNVH9 "
        "(Best Buy model field, SKU 6560338; ASIN-form MPN). Best "
        "Buy $84.99 InStock sold by Best Buy. Flag: do NOT mix in "
        "0840268901417 (MPN B0BTFSYWWB, different ASIN) or "
        "0840268999599 (MPN B0BTG4S29L).",
    ),
    EvalProduct(
        key="asus-rog-strix-scope-ii-96-rx-wireless-black",
        brand="ASUS",
        model="ROG Strix Scope II 96 RX Wireless",
        variant="Black, ROG RX optical switches, model X902",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — the batch-3 brief's "
            "90MP03E0-BKAA40 appears nowhere on the web "
            "(exact-string search: zero corroboration) (batch-4 "
            "verification 2026-11-18).",
            "UPC": "UPC pending — no lead found (batch-4 "
            "verification 2026-11-18).",
        },
        status="pending",
        notes="Current ASUS wireless keyboard. Distinct from the "
        "NX-switch Wireless already in catalog as "
        "asus-rog-strix-scope-ii-96-wireless-black "
        "(90MP037A-BKAA01). ROG US $179.99 InStock. Flag: RX "
        "Red/Blue switch choice unpinned — the ROG page offers "
        "both; earlier $132.99 sale has ended.",
    ),
    EvalProduct(
        key="asus-tuf-gaming-k3-gen-ii-black",
        brand="ASUS",
        model="TUF Gaming K3 Gen II",
        variant="Black (90MP0390-BKAA01)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending. Leads conflict: 197105335776 "
            "(Snapklik aggregator, also mislabels the part number as "
            "a laptop — unreliable) vs 197105335790 (Alfrensia Egypt, "
            "tied to suffix BKCA00, non-US). Adopt neither (batch-4 "
            "verification 2026-11-18).",
        },
        status="pending",
        notes="Current ASUS keyboard. MPN 90MP0390-BKAA01 (ASUS "
        "eShop USA, product name RA07 TUF K3 GEN II/RD/CA/DS ABS). "
        "The batch-3 brief's 90MP03D0-BKAA30 is wrong — looks like a "
        "misread/truncation of 90MP0390. ASUS eShop USA $79.99 "
        "InStock Black. Adorama $99.99 backordered to Jan 2027 — do "
        "not use. Flag: Tom's Guide lists launch $99; current "
        "$79.99 is the live list.",
    ),
    EvalProduct(
        key="hp-e27-g5-fhd-monitor-black",
        brand="HP",
        model="E27 G5 27\" FHD Monitor",
        variant="Black, 27\" FHD (6N4E2AL#ABA)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 0198415636393 (Caretek CA "
            "only, single non-US source — do not promote) (batch-4 "
            "verification 2026-11-18).",
        },
        status="pending",
        notes="Mainstream HP office monitor. MPN 6N4E2AL#ABA (HP US "
        "product page; 6N4E2AA#ABA is a second configuration — not "
        "conflated). HP US $219 list / $157.83 Black Friday sale — "
        "both from hp.com crawls days apart; sale price volatile, "
        "re-check at row time. InStock. Flag: thin identifier trail "
        "is the only weakness.",
    ),
    EvalProduct(
        key="anker-555-usb-c-hub-8-in-1-gray",
        brand="Anker",
        model="555 USB-C Hub (8-in-1)",
        variant="Gray (A8383)",
        category="hubs",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 194644032999 (PicClick "
            "eBay-refurb listing only — thin, single "
            "marketplace-derived source). Do NOT use 0194644032081 — "
            "that is the 553 hub (A83800A1) (batch-4 verification "
            "2026-11-18).",
        },
        status="pending",
        notes="Current Anker hub; distinct from in-catalog Anker "
        "10-in-1 desktop hub (A210C). MPN A8383 (Anker US + UK "
        "agree; full variant MPN A83830A1). The batch-3 brief's "
        "A8397 is WRONG — A8397 is the Anker 777 Thunderbolt "
        "Docking Station (12-in-1), UPC 194644066697, a different, "
        "older product. Anker US $49.99 InStock. Flag: 'Gray' color "
        "is from review descriptions of the aluminum chassis; "
        "Anker's own page names no colorway — color-to-variant "
        "mapping unverified.",
    ),
    EvalProduct(
        key="anker-prime-docking-station-14-in-1-displaylink-gray",
        brand="Anker",
        model="Prime Docking Station (14-in-1, Triple Display, DisplayLink DL7400)",
        variant="Gray (A83B3)",
        category="docks",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-4 "
            "verification 2026-11-18).",
        },
        status="pending",
        notes="Current Anker dock (launched Sep 2025); distinct from "
        "the Prime Charging Docking Station 14-in-1 160W and the "
        "Prime TB5 Docking Station. MPN A83B3 (Anker AU feed SKU "
        "A83B3CA1 + Anker US bundle slug bundle-a83b3-a84n1 agree on "
        "the A83B3 base). The batch-3 brief's A8398/A8399 are WRONG: "
        "A8399 = Anker 568 USB-C Docking Station (11-in-1, USB4), "
        "$699.95 SoldOut; A8398 surfaced nowhere. Anker US $400.00 "
        "sale vs $499.99 list InStock (hubs category page). Launch "
        "price was $299.99 (Sep 2025) — price has risen since; the "
        "$345.98 Anker listing is a bundle with a TB5 cable, not "
        "the standalone dock.",
    ),
    EvalProduct(
        key="anker-maggo-power-bank-10k-qi2-black-stone",
        brand="Anker",
        model="MagGo Power Bank (10K, Qi2 15W)",
        variant="Black Stone (A1654)",
        category="power-banks",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (no B&H listing, no "
            "UPC in any source read) (batch-4 verification "
            "2026-11-18).",
        },
        status="pending",
        notes="Current Anker MagGo bank; distinct from in-catalog "
        "MagGo 2 Pro (A110R, $109.99, Qi2 25W, active cooling) — "
        "A1654 is the cheaper 15W Qi2 bank with smart display + "
        "fold-out stand. MPN A1654 (Anker US official page; Black "
        "Stone variant SKU A1654011). Anker US $89.99 InStock. 5 "
        "colors at same price. Flag: Anker FAQ: iPhone-only, not "
        "Android-compatible.",
    ),
    EvalProduct(
        key="anker-soundcore-v30i-black",
        brand="Anker",
        model="Soundcore V30i",
        variant="Black (A3873)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 194644183523 (Ubuy/Desertcart "
            "mirrors of Amazon ASIN B0CNCHLR56 only — single-source "
            "family) (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Anker open-ear hook earbuds (IPX5, 36H total "
        "playtime); budget tier below AeroFit Pro. MPN A3873 "
        "(Soundcore US URL slug v30i-a3873; black variant lead "
        "A3873Z11 from eBay item specifics — 'AK' prefix form, "
        "treat as lead only). Soundcore US $39.99 sale vs $49.99 "
        "list, in stock (3–7 day delivery). Flag: Best Buy's $44.99 "
        "listing is a bundle with a 20W charger block sold by "
        "AnkerDirect (marketplace) — do not use as the Best Buy row.",
    ),
    EvalProduct(
        key="anker-soundcore-aerofit-pro-midnight-black",
        brand="Anker",
        model="Soundcore AeroFit Pro",
        variant="Midnight Black (A3871Z11)",
        category="earbuds",
        identifiers={"UPC": "194644153014", "MPN": "A3871Z11"},
        identifier_sources={
            "UPC": "Abt product page (Model # A3871Z11, UPC # "
            "194644153014) + B&H spec page agree (batch-4 "
            "re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Anker open-ear earbuds (LDAC, IPX5, 46H "
        "playtime). B&H $179.99 InStock. Flag: do NOT mix in "
        "194644152987 (different variant) or 194644037628 (renewed "
        "listing).",
    ),
    EvalProduct(
        key="asus-zenscreen-mb16acv-black",
        brand="ASUS",
        model="ZenScreen MB16ACV",
        variant="Black (MB16ACV)",
        category="monitors",
        identifiers={"UPC": "192876978498", "MPN": "MB16ACV"},
        identifier_sources={
            "UPC": "B&H spec page (UPC 192876978498) + Adorama spec "
            "page + Simplified Computers agree (batch-4 "
            "re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current ASUS portable monitor; first portable monitor "
        "in the set. 15.6\" FHD IPS despite B&H's '16-inch' title — "
        "pin as 15.6\" in the model description. B&H $189.00 "
        "InStock (price has ranged $179–$209 in B&H deal crawls). "
        "Flag: 2021-era model but still sold new.",
    ),
    EvalProduct(
        key="asus-rog-harpe-ii-ace-black",
        brand="ASUS",
        model="ROG Harpe II Ace",
        variant="Black (90MP0490-BMAA00)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 197105986633 (PBTech NZ + "
            "SquareDeals SG agree — but tied to BMUA00, so per the "
            "Harpe Mini Core precedent do NOT adopt as the US UPC "
            "without US corroboration) (batch-4 verification "
            "2026-11-18).",
        },
        status="pending",
        notes="Current ASUS mouse (48g, 42K DPI, SpeedNova 8K); "
        "distinct from in-catalog Harpe Ace Extreme ($249.99) and "
        "Harpe Mini Core. MPN 90MP0490-BMAA00 (Newegg US: part "
        "number 90MP0490-BMAA00, model P723 ROG HARPE II ACE/BLK; "
        "Best Buy model P723 ROG HARPE II ACE/BLK agrees). BMUA00 "
        "is the non-US/EU part (PBTech, Dateks, Quzo) — do not "
        "record as the US MPN. Best Buy $169.99 InStock sold by "
        "Best Buy (SKU 6650286; was $179.99). Flag: UPC lead tied "
        "to the non-US part — needs US corroboration.",
    ),
    EvalProduct(
        key="dell-27-plus-4k-monitor-s2725qc",
        brand="Dell",
        model="27 Plus 4K USB-C Monitor S2725QC",
        variant="White/Silver (S2725QC)",
        category="monitors",
        identifiers={"UPC": "884116485124", "MPN": "S2725QC"},
        identifier_sources={
            "UPC": "PBTech NZ spec page (MPN S2725QC, UPC "
            "884116485124) + eBay catalog + Ubuy + Layupshop agree "
            "(batch-4 re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Dell 27\" 4K monitor; NOT the in-catalog "
        "S2725QS — the S2725QS entry explicitly distinguishes it "
        "('Not the S2725QC (USB-C sibling, $349.99)'). Same 27\" 4K "
        "120Hz IPS panel as the QS plus 65W USB-C PD, speakers, Eye "
        "Comfort tech. Dell US $349.99 list (street $299.99–"
        "$315.99). Flag: one roundup says 90W PD — wrong; Dell "
        "spec is 65W. Stock to re-check.",
    ),
    EvalProduct(
        key="google-fitbit-inspire-3-midnight-zen-black",
        brand="Google",
        model="Fitbit Inspire 3",
        variant="Midnight Zen/Black (FB424BKBK-US)",
        category="wearables",
        identifiers={"UPC": "810073611573", "MPN": "FB424BKBK-US"},
        identifier_sources={
            "UPC": "HeartRateMonitorsUSA spec table (MPN "
            "FB424BKBK-US Midnight Zen, UPC 810073611573) + "
            "eWirelessGear agree (batch-4 re-verification "
            "2026-11-18) — thin second source resolved at add time",
        },
        status="verified",
        notes="Current Fitbit budget tracker (Editors' Choice "
        "pedigree); still sold new at Best Buy/Google. No built-in "
        "GPS (phone-connected GPS only). Best Buy $93.00 (save "
        "$6.95 vs $99.95 list, SKU 6514030); Google Store promo "
        "$79.95 seen Jun 2026 (expired). Flag: 2022 model, still "
        "sold new; Lilac Bliss is 810073611597; Desertcart's "
        "810073610064 is a different pack — do not mix.",
    ),
    EvalProduct(
        key="sony-inzone-mouse-a-black",
        brand="Sony",
        model="INZONE Mouse-A",
        variant="Black (MSE-G500/B)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found. Regional EANs "
            "conflict (CE7 4548736171220 vs AU/NZ 4548736171237) — "
            "neither is the US code (batch-4 verification "
            "2026-11-18).",
        },
        status="pending",
        notes="Current Sony gaming mouse (Aug 2025 launch, 48.4 g, "
        "3950IZ sensor, 8K polling). MPN MSE-G500/B (Sony US PDP "
        "model MSE-G500B; Best Buy model MSEG500/B, SKU 6641386). "
        "Best Buy $109.99 sold by Best Buy; Sony direct "
        "$119.99–$129.99 sale (list $149.99). In stock at both. "
        "Flag: not the orange Fnatic Edition (separate colorway).",
    ),
    EvalProduct(
        key="sony-inzone-kbd-h75-black",
        brand="Sony",
        model="INZONE KBD-H75",
        variant="Black (KBD-G900/B)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — thin lead 196271646822 (Target "
            "Plus bundle listing only; Target disclaims accuracy and "
            "the listing is a Focus Camera bundle, so the code may "
            "be the bundle's, not the keyboard's) (batch-4 "
            "verification 2026-11-18).",
        },
        status="pending",
        notes="Current Sony gaming keyboard (Aug 2025 launch, 75%, "
        "Hall-effect rapid trigger, 8K wired, aluminum chassis). "
        "MPN KBD-G900/B (Sony US; Best Buy model KBDG900/B, SKU "
        "6641371 — that Best Buy row is sold by DataVision, "
        "marketplace, excluded as a price source). Sony direct "
        "$279.99 sale (list $299.99), delivery dates shown = in "
        "stock. Black only. Flag: promo price; UPC lead may be a "
        "bundle code.",
    ),
    EvalProduct(
        key="logitech-g733-lightspeed-black",
        brand="Logitech",
        model="G733 LIGHTSPEED",
        variant="Black (981-000863)",
        category="headphones",
        identifiers={"UPC": "097855155580", "MPN": "981-000863"},
        identifier_sources={
            "UPC": "B&H spec page names 'Logitech G G733 LIGHTSPEED "
            "Wireless RGB Gaming Headset (Black)' with UPC "
            "097855155580 (batch-4 re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Logitech wireless headset (2020, still sold "
        "new at list by brand/retailer direct). B&H $129.99 In "
        "Stock; Best Buy $119.99 (SKU 6420856). Adorama $159.99 on "
        "backorder (expected 01/2027) — excluded. Flag: 2020 model, "
        "still sold new at list. Black/White/Blue/Lilac exist; "
        "Black pinned.",
    ),
    EvalProduct(
        key="logitech-g335-black",
        brand="Logitech",
        model="G335",
        variant="Black (981-000977)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855165459 (Amazon US only, "
            "for 981-000977 Black; no non-Amazon corroboration "
            "found) (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Logitech wired headset (2021, 240 g, 3.5mm). "
        "MPN 981-000977 (Best Buy US model, SKU 12017008). The "
        "task's 981-000978 is the EU/UK variant (EAN 5099206094789); "
        "AU is 981-000979. Do not use 981-000978 for the US model. "
        "Best Buy $71.99 (MSRP $69.99 per Logitech's 2021 launch "
        "release). Flag: Best Buy price is above MSRP and the "
        "snippet did not state the seller — re-confirm seller at "
        "row time. White is 981-001017 — do not mix.",
    ),
    EvalProduct(
        key="logitech-zone-vibe-100-graphite",
        brand="Logitech",
        model="Zone Vibe 100",
        variant="Graphite (981-001256)",
        category="headphones",
        identifiers={"UPC": "097855177957", "MPN": "981-001256"},
        identifier_sources={
            "UPC": "CompSource spec page lists 'UPC EAN CODE: "
            "0097855177957' for Zone Vibe 100 Graphite 981-001256 "
            "(batch-4 re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Logitech office headset. Best Buy $99.99 (SKU "
        "6520149, 339 reviews); Lenovo US $99.99 with delivery by "
        "Nov 20. Micro Center $99.99 is in-store-only — backup "
        "only. Flag: Logitech's internal CPN for this SKU reads "
        "'ZONE VIBE 125 HEADSET' — the 125 is the business/UC "
        "naming for the same hardware; the consumer listing name is "
        "Zone Vibe 100. Do not create a separate Zone Vibe 125 "
        "entry from this. Also do not mix with the base Zone Vibe "
        "Wireless (981-001440, B&H $84.99, UPC 097855175656) — "
        "different model.",
    ),
    EvalProduct(
        key="razer-leviathan-v2-black",
        brand="Razer",
        model="Leviathan V2",
        variant="Black (RZ05-03920100-R3U1)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 690142766690 (eBay listing "
            "only, for R3U1) (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Razer 2.1 soundbar + wired subwoofer (THX "
        "Spatial, Chroma RGB, 2022 launch, still current). MPN "
        "RZ05-03920100-R3U1 (Best Buy US model, SKU 6496625; Best "
        "Buy CA agrees). EU is R3G1 — do not mix. Best Buy $249.99 "
        "(336 reviews, Deal of the Day); Razer.com list $249.99. "
        "Flag: stock state not explicit in the Best Buy snippet — "
        "re-confirm at row time; do not mix with Leviathan V2 X "
        "(RZ05-04160100-R3U1, $99.99, no subwoofer).",
    ),
    EvalProduct(
        key="razer-nommo-v2-black",
        brand="Razer",
        model="Nommo V2",
        variant="Black (RZ05-04750100-R3U1)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead. (EAN 8887910060469 "
            "belongs to the EU R3G1 variant — not a US UPC, do not "
            "use.) (batch-4 verification 2026-11-18).",
        },
        status="pending",
        notes="Current Razer desktop speakers (wired subwoofer, "
        "aluminum phase plugs, no control pod). MPN "
        "RZ05-04750100-R3U1 (Best Buy US model, SKU 6547858). "
        "Razer.com $299.99 (list, checked Nov 12, 2026); Best Buy "
        "$299.99 (81 reviews). Flag: Pro is RZ05-04740100-R3U1/R3G1 "
        "($449.99) and V2 X is RZ05-04760100 ($149.99) — both "
        "different models. One UK listing confuses the V2/V2 Pro "
        "MPNs in its title vs spec table; the Best Buy US MPN above "
        "is clean.",
    ),
    EvalProduct(
        key="hyperx-pulsefire-haste-2-core-wireless-black",
        brand="HyperX",
        model="Pulsefire Haste 2 Core Wireless",
        variant="Black (8R2E6AA)",
        category="mice",
        identifiers={"UPC": "197498115382", "MPN": "8R2E6AA"},
        identifier_sources={
            "UPC": "PBTech spec page (Haste 2 Core Wireless Black, "
            "MPN 8R2E6AA, UPC 197498115382) + Swiss Post shop EAN "
            "197498115382 agree (batch-4 re-verification "
            "2026-11-18)",
        },
        status="verified",
        notes="Current HyperX wireless mouse; distinct from "
        "in-catalog Haste 2 Wireless (6N0B0AA, $89.99) and Haste 2 "
        "Pro — Core is the cheaper 70 g / 12K DPI / AAA-battery "
        "variant. HP.com US $49.99 InStock (JSON-LD). Staples "
        "$49.99 is in-store-only — backup only. Flag: none. White "
        "is 8R2E7AA.",
    ),
    EvalProduct(
        key="logitech-astro-a50-gen-5-black",
        brand="Logitech",
        model="Astro A50 Gen 5",
        variant="Black (939-002217)",
        category="headphones",
        identifiers={"UPC": "097855199621", "MPN": "939-002217"},
        identifier_sources={
            "UPC": "Adorama spec page (UPC Codes — Black: "
            "097855199621 | White: 097855199645) + Logitech's own "
            "2024 package-specification document via 1WorldSync CDN "
            "agree (batch-4 re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Logitech headset (2024, PLAYSYNC 3-system "
        "switching, $299.99); the current mainstream flagship, "
        "cheaper sibling of the A50 X ($399.99). $299.99 at Abt, "
        "Adorama, Target and Logitech G US. Flag: stock not "
        "explicitly stated in the Abt/Adorama snippets — re-confirm "
        "at row time (Target lists Black at $299.99 with 227 "
        "ratings; P.C. Richard shows White OutOfStock, not our "
        "variant). White is 939-002229.",
    ),
    EvalProduct(
        key="garmin-tactix-8-47mm-amoled-black",
        brand="Garmin",
        model="tactix 8",
        variant="47mm AMOLED, Black (010-03405-00)",
        category="wearables",
        identifiers={"UPC": "753759344030", "MPN": "010-03405-00"},
        identifier_sources={
            "UPC": "Exquisite Timepieces (GTIN 753759344030, "
            "Reference Number 010-03405-00) + MojoMotoSport (SKU "
            "010-03405-00 + UPC 753759344030) agree (batch-4 "
            "re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current Garmin premium watch (launched Jan 2025); no "
        "tactix entry existed in the catalog before this batch. "
        "$1,049.99 In Stock sold by Best Buy (SKU 6619373); Abt "
        "$1,049.99; Sportsman's $1,049.99. Flag: promo price "
        "($1,299.99 list); Abt notes a manufacturer rebate ending "
        "12/28/2026.",
    ),
    EvalProduct(
        key="asus-tuf-gaming-vg27aq3a-black",
        brand="ASUS",
        model="TUF Gaming VG27AQ3A",
        variant="Black (VG27AQ3A)",
        category="monitors",
        identifiers={"UPC": "197105079663", "MPN": "VG27AQ3A"},
        identifier_sources={
            "UPC": "CompSource US market (UPC EAN CODE 197105079663) "
            "+ B&H spec page + Adorama spec table agree (batch-4 "
            "re-verification 2026-11-18)",
        },
        status="verified",
        notes="Current ASUS monitor; 27\" QHD 180Hz Fast IPS (single "
        "colorway). B&H $219.00 In Stock; ASUS US $209.00 (InStock "
        "per JSON-LD); Adorama $229.99. Flag: launched 2023, but "
        "still sold new at B&H/ASUS direct.",
    ),
    EvalProduct(
        key="anker-soundcore-space-a40-black",
        brand="Anker",
        model="Soundcore Space A40",
        variant="Black (A3936)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead for Black. The only UPC "
            "found, 194644102258, is for the Blue variant — must NOT "
            "be transferred to Black (batch-4 verification "
            "2026-11-18).",
        },
        status="pending",
        notes="Current Anker earbuds; distinct from in-catalog Space "
        "One Pro (A40 is a different model). MPN A3936 (Best Buy "
        "Model A3936, SKU 13017491 + soundcore US A3936011). Target "
        "$59.99 In Stock sold & shipped by Anker (brand-direct); "
        "soundcore direct $99.99. Flag: $59.99 is a sale price vs "
        "$99.99 list; launched 2022, but still sold new direct + "
        "Target.",
    ),
    EvalProduct(
        key="apple-ipad-mini-a17-pro-128gb-wifi-space-gray",
        brand="Apple",
        model="iPad mini (A17 Pro)",
        variant="Space Gray, Wi-Fi 128GB (MXN63LL/A)",
        category="tablets",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (batch-4 "
            "verification 2026-11-18).",
        },
        status="pending",
        notes="Previous-gen iPad mini still sold new at major US "
        "retailers; distinct from in-catalog iPad mini A20 Pro "
        "($699). MPN MXN63LL/A (Best Buy US Model, SKU 6578253). "
        "(A first guess MXNX3LL/A was wrong; MXN63LL/A is the "
        "verified code. Wi-Fi + Cellular 128GB Space Gray is "
        "MXPN3LL/A — different SKU.) Target $499.99 In Stock (new); "
        "Best Buy $599.00 sold by Best Buy (SKU 6578253). Flag: "
        "superseded — iPad mini A20 Pro is in catalog ($699); Apple "
        "now sells A17 Pro mini only as refurbished ($509). Target "
        "$499.99 is $100 under the $599 list — clearance-drift "
        "watch. Follows the Buds3 Pro precedent (previous gen still "
        "sold new at a major retailer).",
    ),
    # --- Expansion batch 35 (added 2026-11-20, user-approved, DECISIONS 084). ---
    EvalProduct(
        key="sony-bravia-theatre-rear-9-black",
        brand="Sony",
        model="BRAVIA Theatre Rear 9",
        variant="Black (SA-RS9)",
        category="speakers",
        identifiers={"UPC": "027242934221", "MPN": "SA-RS9"},
        identifier_sources={
            "UPC": "B&H spec page + NFM 'UPC + Model SARS9' + "
            "DataVision 'MFR SARS9, $548' agree (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current Sony rear-speaker pair (2026, 180W, Dolby "
        "Atmos/DTS:X, 360 Spatial Sound Mapping); pairs with Bar "
        "9/8/7 and HT-A7000/A5000/A3000. Best Buy $549.99 InStock, "
        "sold by Best Buy (SKU 6673696); Abt $548 InStock; Target "
        "$548 InStock; Sony direct $749.99 list. Flag: promo price "
        "($548–549.99 vs $749.99 comp, Black Friday ends Nov 28). "
        "Distinct from in-catalog Rear 8 (SA-RS8).",
    ),
    EvalProduct(
        key="jbl-authentics-500-black",
        brand="JBL",
        model="Authentics 500",
        variant="Black (JBLAUTH500BLKAM)",
        category="speakers",
        identifiers={"UPC": "050036396264", "MPN": "JBLAUTH500BLKAM"},
        identifier_sources={
            "UPC": "B&H spec page + Erikson Consumer distributor "
            "spec 'Model JBLAUTH500BLKAM' agree (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current JBL flagship home speaker, Dolby Atmos Music, "
        "Wi-Fi/Bluetooth; smart-home speaker with Alexa/Google "
        "voice. Abt $399.95 InStock (rebate to 12/05/2026); "
        "Sweetwater $399.95; Crutchfield $749.95 InStock (the "
        "$449.95 sale has ended, now list); JBL direct OutOfStock. "
        "Flag: promo price (Abt rebate ends 12/05/2026). Do NOT use "
        "the JBLAUTH500BLKAM-Z listing ($562.95) as price evidence "
        "— -Z is a different listing.",
    ),
    EvalProduct(
        key="jbl-vibe-flex-2-black",
        brand="JBL",
        model="Vibe Flex 2",
        variant="Black (JBLVFLEX2BLKAM)",
        category="earbuds",
        identifiers={"UPC": "050036404921", "MPN": "JBLVFLEX2BLKAM"},
        identifier_sources={
            "UPC": "Erikson Consumer spec 'Model JBLVFLEX2BLKAM' + "
            "Visions + Addison Électronique agree (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current JBL true-wireless earbuds (2024–now, 12mm "
        "drivers, Smart Ambient). JBL direct Black $69.95 InStock; "
        "White also in stock — variant stays Black. No Best Buy US "
        "or B&H US listing found. Do NOT use gen-1 codes: UPC "
        "050036391368 and eBay GTIN 0050036391344 belong to the "
        "gen-1 Vibe Flex (JBLVFLEXMITAM etc.).",
    ),
    EvalProduct(
        key="razer-leviathan-v2-x-black",
        brand="Razer",
        model="Leviathan V2 X",
        variant="Black (RZ05-04280100-R3U1)",
        category="soundbars",
        identifiers={"UPC": "810056146771", "MPN": "RZ05-04280100-R3U1"},
        identifier_sources={
            "UPC": "B&H spec page + Abt spec 'Model "
            "RZ05-04280100-R3U1' + Electronic Express agree "
            "(batch-5 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Razer compact PC soundbar (USB-C, Bluetooth "
        "5.0, Chroma RGB, no subwoofer). Best Buy $99.99, sold by "
        "Best Buy, InStock (SKU 6521035); B&H $99.99; Staples "
        "$106.66 InStock. Do NOT use R3M1 (UK/EU, EAN "
        "8886419379645) or the Kuromi edition RZ05-04280300-R3M1. "
        "Distinct from in-catalog Leviathan V2 (has subwoofer; V2 X "
        "has none).",
    ),
    EvalProduct(
        key="razer-nommo-v2-pro-black",
        brand="Razer",
        model="Nommo V2 Pro",
        variant="Black (RZ05-04740100-R3U1)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272904794 (Best Buy spec "
            "panel only, 135-day-old crawl) + Amazon mirrors; no "
            "second independent retailer source (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Razer's top desktop speaker set (2.1, wireless "
        "subwoofer + wireless control pod, THX Spatial Audio). MPN "
        "RZ05-04740100-R3U1 confirmed (Razer.com URL + Best Buy "
        "model field); R3G1 is UK/EU — do not carry. Razer US "
        "$449.99, JSON-LD InStock (fresh fetch 2026-11-20) — the "
        "draft's HOLD is lifted on this direct row; Best Buy new "
        "row is dead ('no longer available in new condition'). "
        "Distinct from in-catalog Nommo V2 (mid tier, wired sub).",
    ),
    EvalProduct(
        key="razer-nommo-v2-x-black",
        brand="Razer",
        model="Nommo V2 X",
        variant="Black (RZ05-04760100-R3U1)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272904510 (Desertcart "
            "only — Amazon-data mirror, not independent). EAN "
            "8887910060292 belongs to the UK R3G1 — do not attach "
            "(batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Entry tier of the Nommo V2 line (2.0, no subwoofer, "
        "THX Spatial Audio). MPN RZ05-04760100-R3U1 (Best Buy "
        "model, SKU 6547859). Best Buy $149.99, sold by Best Buy, "
        "InStock; Razer US $149.99 InStock. Distinct from "
        "in-catalog Nommo V2 — V2 X has no subwoofer, no control "
        "pod, no Chroma.",
    ),
    EvalProduct(
        key="hyperx-cloud-stinger-2-core-pc-black",
        brand="HyperX",
        model="Cloud Stinger 2 Core",
        variant="PC, Black (683L9AA)",
        category="headphones",
        identifiers={"UPC": "196548418183", "MPN": "683L9AA"},
        identifier_sources={
            "UPC": "Micro Center 'Mfr Part # 683L9AA' + Newegg "
            "'MPN 683L9AA' agree (batch-5 verification 2026-11-20).",
        },
        status="verified",
        notes="Current HyperX entry-level wired PC headset (40mm "
        "drivers, swivel-to-mute). HyperX US $39.99 InStock; Best "
        "Buy $39.99 InStock, Add to cart; HP.com $39.99 InStock. "
        "PC version confirmed by 4 sources (HyperX US, HP.com, "
        "Best Buy, Micro Center). PS version is 6H9B5AA (White) / "
        "6H9B6AA (Black), Xbox version is 'CloudX Stinger 2 Core' "
        "— pin PC version 683L9AA only. Distinct from in-catalog "
        "Cloud Stinger 2 (non-Core).",
    ),
    EvalProduct(
        key="sony-inzone-e9-black",
        brand="Sony",
        model="INZONE E9",
        variant="Black (IER-G900B)",
        category="earbuds",
        identifiers={"UPC": "027242933187", "MPN": "IER-G900B"},
        identifier_sources={
            "UPC": "DataVision 'MFR IERG900B, Condition: New, $118' "
            "+ Kawartha TV 'UPC 027242933187' agree (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current Sony IEM (Aug 2025 launch with Fnatic; no "
        "mic). Target Black $118 InStock (reg $148); Best Buy "
        "Black $118 InStock (Model IERG900/B); Audio46 Black "
        "$119.99 in stock. Flag: promo — $118 vs $149.99 list "
        "(Black Friday). US variant IERG900B.UC; EU CE7 is "
        "IERG900B.CE7 — do not mix. Do NOT attach EAN "
        "4548736171107/4548736171084 (different suffixes/regions). "
        "Glass Purple is a colorway, not a separate model.",
    ),
    EvalProduct(
        key="jbl-charge-5-black",
        brand="JBL",
        model="Charge 5",
        variant="Black (JBLCHARGE5BLKAM)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — strong lead 050036380218 (Abt "
            "spec 'Model JBLCHARGE5BLKAM' + Zoro; needs a second "
            "fresh retailer source at add time) (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Previous-gen JBL speaker still sold new at JBL US "
        "($139.95) and Best Buy ($139.99, comp $179.95, Add to "
        "cart). MPN JBLCHARGE5BLKAM (Best Buy model). Do NOT quote "
        "$134.95 as the new price — the fresh JBL.com fetch "
        "showing $134.95 InStock was the refurbished-variant URL. "
        "Flag: discontinued tension — Zoro marks it Discontinued; "
        "Charge 6 is current and in catalog. KEEP as pending, not "
        "as a current-generation pick.",
    ),
    EvalProduct(
        key="asus-rt-be58u-black",
        brand="ASUS",
        model="RT-BE58U",
        variant="Black (RT-BE58U)",
        category="routers",
        identifiers={"UPC": "197105452916", "MPN": "RT-BE58U"},
        identifier_sources={
            "UPC": "Adorama spec page 'UPC Code 197105452916' + "
            "CompSource 'UPC EAN CODE: 197105452916, MARKET: US' "
            "agree (batch-5 verification 2026-11-20).",
        },
        status="verified",
        notes="Current ASUS WiFi 7 dual-band router (BE3600, 2.5G "
        "WAN/LAN). ASUS direct $149.99, InStock; Adorama $169.00. "
        "Target $124.99 listing is manufacturer-refurbished — "
        "excluded. First router in the set (new category, "
        "DECISIONS 084). ASUS lists a HW Ver 2.0 firmware — no "
        "variant split seen in US retail.",
    ),
    EvalProduct(
        key="asus-rog-strix-oled-xg27acdms-black",
        brand="ASUS",
        model="ROG Strix OLED XG27ACDMS",
        variant="Black (XG27ACDMS)",
        category="monitors",
        identifiers={"UPC": "197105871380", "MPN": "XG27ACDMS"},
        identifier_sources={
            "UPC": "PBTech retailer spec page 'UPC 197105871380, "
            "MPN XG27ACDMS' + NationalPC.in 'UPC 197105871380, EAN "
            "4711387871386' agree (batch-5 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Current ASUS 27-inch QD-OLED gaming monitor (QHD "
        "280Hz, 0.03ms). Best Buy $399.99, InStock, sold by Best "
        "Buy, Add to cart (comp. value $649.99 — Black Friday "
        "promo); ASUS direct $649.00, OutOfStock. ASUS eShop part "
        "90LM0B60-B013C1 vs NationalPC 90LM0B60-B01311 — suffix "
        "discrepancy, use XG27ACDMS as the catalog MPN. Flag: promo "
        "price — $399.99 is $250 off list; re-check at add time.",
    ),
    EvalProduct(
        key="dell-ultrasharp-34-curved-u3425we-silver",
        brand="Dell",
        model="UltraSharp 34 Curved Thunderbolt Hub Monitor U3425WE",
        variant="Silver (V124N)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 884116452034 (single source: "
            "ComptechDirect EAN/UPC list, on a Grade-A-refurbished "
            "listing — weak; verify at add time) (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Current Dell 34-inch ultrawide Thunderbolt hub "
        "monitor (UWQHD 3440x1440, 120Hz IPS Black, Thunderbolt 4 "
        "hub, 90W PD). MPN V124N (Dell US tech specs); HK variant "
        "is X2RV9 — do not mix. Dell.com direct $984.99 InStock "
        "(fresh fetch 2026-11-20, JSON-LD) — add-time "
        "re-verification resolved the Adorama conflict (snippets "
        "InStock $769 vs page JSON-LD 'Discontinued' — do not use "
        "the Adorama row); Abes of Maine $789.00, In stock. Flag: "
        "weakest price evidence of the batch — re-check Dell.com "
        "at row time.",
    ),
    EvalProduct(
        key="dell-pro-32-plus-4k-p3225qe-black",
        brand="Dell",
        model="Pro 32 Plus 4K USB-C Hub Monitor P3225QE",
        variant="Black/Gray (P3225QE)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "EAN": "EAN pending — lead 5397184962527 (Target PDP "
            "'UPC' field; 13-digit, so treat as EAN lead, not a US "
            "UPC — verify at add time) (batch-5 verification "
            "2026-11-20).",
        },
        status="pending",
        notes="Current Dell 32-inch 4K USB-C hub monitor (31.5-inch "
        "4K UHD IPS, 100Hz, USB-C hub, 90W PD). MPN P3225QE. "
        "Adorama $499.00 new; B&H $499.99; Target $525.00. "
        "Distinct from in-catalog U3225QE (Thunderbolt) and "
        "S3225QS — this is the Pro-line USB-C model.",
    ),
    EvalProduct(
        key="hp-975-dual-mode-wireless-keyboard-black",
        brand="HP",
        model="975 Dual-Mode Wireless Keyboard",
        variant="Black (3Z726AA#ABA)",
        category="keyboards",
        identifiers={"UPC": "195908664512", "MPN": "3Z726AA#ABA"},
        identifier_sources={
            "UPC": "DirectDial spec page 'MFG PART 3Z726AA#ABA, UPC "
            "0195908664512' + Caretek spec page + StockInTheChannel "
            "HP GTIN '(ABA) 195908664512' agree (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current HP full-size dual-mode wireless keyboard (BT "
        "+ 2.4GHz, rechargeable, programmable). HP.com $124.00 "
        "list; DirectDial $110.00, Backordered. Flag: 2021-era "
        "model, still current-sale on HP.com — but "
        "StockInTheChannel reports 0 distributor stock, so HP.com "
        "direct is effectively the only clean row; thin channel.",
    ),
    EvalProduct(
        key="hp-710-rechargeable-silent-mouse-black",
        brand="HP",
        model="710 Rechargeable Silent Mouse",
        variant="Black (6E6F2AA#ABL)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 196548822690 (Best Buy spec "
            "panel prints UPC 196548822690 for this exact Black "
            "listing; eBay GTIN 0196548822690 agrees but eBay is "
            "not a qualifying source). Conflict to re-check at add "
            "time: LT Online Store prints 196548822683 for 6E6F2AA "
            "(it prints the same code for 6E6F1AA too, so LT looks "
            "like a copy error) (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current HP rechargeable silent-click wireless mouse "
        "(compact ambidextrous, BT + 2.4GHz, USB-C rechargeable). "
        "MPN 6E6F2AA#ABL. HP.com $89.99. Best Buy's fetched page "
        "is a stale Feb 2026 crawl ($31.99) — do not use; current "
        "Best Buy price not captured. Silver is 6E6F1AA#ABL — do "
        "not mix.",
    ),
    EvalProduct(
        key="hyperx-cloud-alpha-wireless-black-red",
        brand="HyperX",
        model="Cloud Alpha Wireless",
        variant="Black-Red (4P5D4AA)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (targeted search "
            "2026-11-20; Best Buy spec panel in fetched text shows "
            "no UPC — spec-panel check at add time) (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Current HyperX wireless gaming headset (300-hour "
        "battery, DTS Headphone:X, dual-chamber drivers). MPN "
        "4P5D4AA (HP.com product # + Best Buy model agree). Best "
        "Buy $108.99, InStock, sold by Best Buy, Add to cart "
        "(Black Friday Deal, comp. $199.99); HP.com $108.99, "
        "InStock (same promo). Flag: promo price — $108.99 is 46% "
        "off the $199.99 list; 2022-era model but still "
        "current-sale at HP/Best Buy.",
    ),
    EvalProduct(
        key="hyperx-alloy-rise-black",
        brand="HyperX",
        model="Alloy Rise",
        variant="Black, US Layout, HyperX Red Linear, wired (7G7A3AA#ABA)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (targeted search "
            "2026-11-20; no retailer spec page printed one) "
            "(batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current HyperX full-size hot-swappable keyboard "
        "(gasket mount, HyperX Red linear). MPN 7G7A3AA#ABA "
        "(HP.com product # + Best Buy model + Amazon item model "
        "agree). HyperX direct $199.99, Available; HP.com "
        "$199.99; Best Buy $199.99, InStock (SKU 11006257 — use "
        "this one; the other Best Buy SKU 13226682 is sold/shipped "
        "by Adorama, not Best Buy). Distinct from in-catalog "
        "Alloy Rise 75 (7G7A4AA#ABA) — full-size vs 75%.",
    ),
    EvalProduct(
        key="corsair-void-wireless-v2-carbon",
        brand="Corsair",
        model="VOID Wireless v2",
        variant="Carbon (CA-9011379-WW)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (targeted search "
            "2026-11-20; Best Buy spec panel in fetched text shows "
            "no UPC) (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Corsair wireless gaming headset (2025 model; "
        "2.4GHz + Bluetooth, Dolby Atmos, 70h battery). MPN "
        "CA-9011379-WW (Corsair.com SKU + Best Buy model agree). "
        "Best Buy $69.99, InStock, sold by Best Buy, Add to cart "
        "(Black Friday Deal, comp. $129.99); Corsair.com $129.99, "
        "InStock. White is CA-9011380-WW — do not mix. Flag: promo "
        "price — $69.99 is $60 off list.",
    ),
    EvalProduct(
        key="corsair-darkstar-wireless-black",
        brand="Corsair",
        model="DARKSTAR Wireless RGB MMO Gaming Mouse",
        variant="Black (CH-931A011-NA)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840006649489 (BuildCores + "
            "Desertcart + Snapklik + DealTargets all print it, but "
            "all are weak aggregator/marketplace feeds, no retailer "
            "spec page seen — verify at add time) (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Current Corsair MMO wireless gaming mouse (MARKSMAN "
        "26K sensor, 15 programmable buttons, 6-button thumb "
        "cluster, Slipstream + BT). MPN CH-931A011-NA "
        "(Corsair.com SKU + Newegg part # agree); EU is "
        "CH-931A011-EU — do not use. Corsair.com $149.99 list "
        "(stock not confirmed on the fetched page — verify at add "
        "time); Newegg $129.99–$149.99 (seller not confirmed). "
        "Flag: 2023-era model; a Revival Series SKU "
        "(CH-931A011-NA-RV, $69.99) exists and is OutOfStock — do "
        "not confuse with the main SKU; current-stock confirmation "
        "is the main gap on this one.",
    ),
    EvalProduct(
        key="corsair-sabre-v2-pro-wireless-white",
        brand="Corsair",
        model="SABRE v2 PRO Wireless FPS Gaming Mouse",
        variant="White (CH-931G101-WW)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found (no targeted UPC "
            "search run in this round — check at add time) "
            "(batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Corsair wireless FPS gaming mouse (8K "
        "polling, lightweight FPS shape). MPN CH-931G101-WW (Best "
        "Buy model). Best Buy $99.99, sold by Best Buy (comp. "
        "value $149.99 — Black Friday promo). Flag: previous "
        "generation — the SABRE v3 PRO PureVector line launched "
        "2026-10-20 ($179.99+); v2 Pro is still sold new at Best "
        "Buy but note the supersession risk at add time.",
    ),
    EvalProduct(
        key="keychron-k10-max-black-red",
        brand="Keychron",
        model="K10 Max QMK Wireless Mechanical Keyboard",
        variant="Fully Assembled, Black, RGB Backlight, Keychron Super Red (K10M-H1)",
        category="keyboards",
        identifiers={"EAN": "4895248884569", "SKU": "K10M-H1"},
        identifier_sources={
            "EAN": "Micro Center spec page 'Mfr Part# K10M-H1, UPC "
            "4895248884569' + OX.ee 'EAN 4895248884569 for K10M-H1' "
            "+ SquareDeals table 'KYCN-K10M-H1 → 4895248884569' + "
            "Albagame 'EAN 4895248884569 for K10M-H1' agree. "
            "13-digit code → EAN column per the Keychron catalog "
            "precedent (K8 Ultra 8K); Micro Center labels it "
            "'UPC' (batch-5 verification 2026-11-20).",
            "SKU": "Keychron official product page: Red K10M-H1 "
            "(page default); Brown K10M-H3, Banana K10M-H4 — do "
            "not mix; EANs differ per switch.",
        },
        status="verified",
        notes="Current Keychron full-size QMK/VIA wireless keyboard "
        "(100%, 2.4GHz + BT + wired, hot-swappable). Keychron "
        "direct $119.99; Micro Center lists the model (SKU "
        "740191) but its price was not captured in the page fetch. "
        "Walmart $119.99 listing is the Banana variant — not "
        "usable for this Red pin. Flag: switch-label discrepancy "
        "— Micro Center calls the switch 'Keychron K Pro Red "
        "Linear' while Keychron.com/Dynacore say Super Red; pinned "
        "as Super Red per the brand. No promo seen.",
    ),
    EvalProduct(
        key="keychron-q2-max-carbon-black-brown",
        brand="Keychron",
        model="Q2 Max QMK/VIA Wireless Custom Mechanical Keyboard",
        variant="Fully Assembled Knob, Carbon Black, Gateron Jupiter Brown (Q2M-M3)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "EAN": "EAN pending — no lead (the only EAN found, "
            "4895248864059 via Snapklik, belongs to the Red Q2M-M1 "
            "variant — deliberately not attached) (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Current Keychron 65% QMK/VIA wireless keyboard (full "
        "aluminum, knob, 2.4GHz + BT + wired). MPN Q2M-M3 "
        "(Keychron mirror + PBTech Mfr Part No agree). Keychron "
        "direct $203.99, Available (list $229.99, MAX20 $20-off "
        "auto-applied at checkout — promo price); no second US "
        "retailer-direct row found in this round. Red Q2M-M1 and "
        "Banana Q2M-P4 are the other switches — do not mix. Flag: "
        "single-retailer row + promo pricing; find a second "
        "retailer at add time. Fills the 65% gap in the Q Max line "
        "(Q1/Q3/Q5/Q6 Max already in catalog).",
    ),
    EvalProduct(
        key="bose-bass-module-700-black",
        brand="Bose",
        model="Bass Module 700",
        variant="Black (809108-1100)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 017817789592 (World Wide "
            "Stereo spec page 'Model: 809108-1100 | UPC: "
            "017817789592'; Amazon item details + eBay agree but "
            "are not qualifying sources). eBay also shows a second "
            "GTIN 0017817798136 attached to the same MPN — "
            "unresolved, do not attach (batch-5 verification "
            "2026-11-20).",
        },
        status="pending",
        notes="Bose's current flagship wireless bass module for "
        "Bose Smart soundbars (categorized under speakers — the "
        "catalog has no subwoofers category). MPN 809108-1100 "
        "(World Wide Stereo spec page). Best Buy $899.00, sold by "
        "Best Buy, InStock (JSON-LD); Bose direct list also $899. "
        "Flag: AGE — launched 2018, but still Bose's current "
        "flagship bass module with no successor; sold new at Best "
        "Buy/Bose. The MPN/UPC pairing rests on a single retailer "
        "spec page; re-confirm at add time.",
    ),
    EvalProduct(
        key="microsoft-surface-slim-pen-2-matte-black",
        brand="Microsoft",
        model="Surface Slim Pen 2",
        variant="Matte Black, retail (8WV-00001)",
        category="accessories",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 889842778717 (NFM retailer "
            "spec page for 8WV00001; eBay listings for 8WV-00001 "
            "agree but eBay is not a qualifying source) (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Microsoft's current rechargeable stylus for Surface "
        "devices. MPN 8WV-00001 (Best Buy model; NFM spec page "
        "'Model: 8WV00001'). Best Buy $109.99 (Black Friday, comp "
        "$129.99) / list $129.99; Adorama lists the commercial "
        "twin at $124.99 — do not use as the price for this SKU. "
        "Flag: PROMO price ($109.99 vs $129.99 list). Twin-SKU "
        "trap: commercial channel MPN 8WX-00001 has a DIFFERENT "
        "UPC 889842778861 — never mix the two. Age: 2021 launch, "
        "but still the current pen, bundled with the Surface Pro "
        "12-inch keyboard (2025).",
    ),
    EvalProduct(
        key="microsoft-surface-laptop-15-8th-edition-platinum",
        brand="Microsoft",
        model="Surface Laptop, 15-inch (8th Edition)",
        variant="Snapdragon X2 Elite 12-core, 16GB/1TB, Platinum (EP2-60128)",
        category="laptops",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 196388728855 (Target spec "
            "page: Model name EP2-60128, UPC 196388728855; single "
            "retailer-spec source — re-confirm via Best Buy spec "
            "panel at add time) (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Microsoft 15-inch laptop (8th Edition, "
        "Snapdragon X2 Elite). MPN EP2-60128 (Abt, Target, Best "
        "Buy SKU 12740531 all agree). Abt $1,899.99, comp "
        "$2,199.99 (manufacturer rebate ends 12/06/2026); Staples "
        "$2,161.99; Microsoft Store business page lists 15-inch "
        "from $2,099.99. Flag: PROMO/rebate price at Abt. Size "
        "sibling of in-catalog 13.8-inch (EP2-59028) — same "
        "precedent as Watch8 40/44mm, MacBook Air 13/15, iPad Air "
        "11/13 in the catalog.",
    ),
    EvalProduct(
        key="lenovo-legion-go-2-32gb-1tb-eclipse-black",
        brand="Lenovo",
        model="Legion Go 2",
        variant="Windows 11, Ryzen Z2 Extreme, 32GB, 1TB, Eclipse Black (83N0000BUS)",
        category="handheld-consoles",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 0199271412718 (eBay-only, "
            "conflicted). Multiple eBay listings give "
            "0199271412718 for 83N0000BUS, but one eBay listing for "
            "a '2TB NEW' unit also claiming MPN 83N0000BUS gives "
            "199271412701. No retailer spec page found. Verify via "
            "Best Buy spec panel at add time; do not carry either "
            "value as verified (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Lenovo Windows handheld gaming device. MPN "
        "83N0000BUS (Best Buy model, SKU 6643145). Best Buy "
        "$1,999.99, sold by Best Buy, in stock (Add to cart). "
        "Entry 16GB/1TB config is a different SKU (Best Buy "
        "$1,349.99, UPC 199271412763 per Slickdeals) — not this "
        "entry. Flag: price has moved a lot (launch $1,350 for the "
        "32GB config per XDA/PCGuide; now $1,999.99) — record "
        "as-of 2026-11-20, re-check at add time. Distinct from "
        "in-catalog Legion Go S SteamOS (83L30030US) — different "
        "device/OS.",
    ),
    EvalProduct(
        key="alienware-16-area-51-rtx-5070-ti-2tb-liquid-teal",
        brand="Alienware",
        model="16 Area-51",
        variant="Ultra 9 275HX, 32GB, RTX 5070 Ti, 2TB, Liquid Teal, 16-inch 240Hz QHD (LAA16250-9499BLU-PUS)",
        category="laptops",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 884116651499 (eBay-only). "
            "Single eBay listing gives UPC 884116651499 for MPN "
            "LAA16250-9499BL (note: without the Best Buy '-PUS' "
            "suffix). No retailer spec page found. Verify at add "
            "time (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Alienware flagship gaming laptop (2025 "
        "Area-51 line). MPN LAA16250-9499BLU-PUS (Best Buy model, "
        "SKU 6632697). Best Buy $4,174.99 (sold by Best Buy per "
        "listing; 'New $3,699.99–$4,174.99' range shown across "
        "crawls). Dell direct from $3,099 for the line (different "
        "configs). Flag: laptop config matrix — the AA16250 "
        "chassis ships in many configs (RTX 5070/5070 Ti/5080, "
        "1TB/2TB/4TB); pin the exact config above. Price is high "
        "vs Dell's own $3,569.99 for the 5070 Ti/32GB/1TB config — "
        "the Best Buy unit is 2TB.",
    ),
    EvalProduct(
        key="alienware-aw2725qf-black",
        brand="Alienware",
        model="AW2725QF",
        variant="Black (AW2725QF)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — strong lead 884116469711. PB Tech "
            "(AU retailer), TopMarket, eBay UK and AlmaCommerce all "
            "agree on 884116469711; EAN 5397184821787 (Icecat). No "
            "US retailer spec page seen — verify via Best Buy spec "
            "panel at add time (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Alienware 27-inch dual-mode gaming monitor "
        "(4K IPS dual-resolution: 4K 180Hz / FHD 360Hz). MPN "
        "AW2725QF (Best Buy model, SKU 12688409; Dell model). Best "
        "Buy $549.00, shipping available (pickup unavailable in "
        "crawl); Newegg $577 (via Klarna). Seed file noted a "
        "$499.99 row for this model — price has moved; "
        "promo-sensitive. Distinct from in-catalog AW2725Q "
        "(QD-OLED 240Hz 4K, $899.99, MPN 2MHGG) — different "
        "panel/tech/price tier. Do not merge.",
    ),
    EvalProduct(
        key="meta-oakley-meta-hstn-clear-black",
        brand="Meta",
        model="Oakley Meta HSTN",
        variant="Clear Lenses, Black frame (0OW8002 800207)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead found. Targeted search "
            "2026-11-20 returned no UPC for this model code. Best "
            "Buy spec-panel check at add time (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Current Meta/Oakley AI smart glasses. MPN 0OW8002 "
        "800207 (Best Buy model, SKU 6636602). Best Buy $399.00 "
        "list; one crawl showed $349.00 — treat $349 as "
        "promo/unconfirmed, carry $399.00 as list. Sold by Best "
        "Buy. Flag: PROMO uncertainty ($349 vs $399 across "
        "crawls). Large variant matrix — 10+ lens/frame combos at "
        "Best Buy (Transitions $479, Prizm $399–$449, Vanguard is "
        "a separate model at $579); pin only the Clear/Black "
        "800207 entry. Distinct from in-catalog Ray-Ban Meta Gen 2 "
        "Wayfarer (different frame line, 8-hr battery, 3K video).",
    ),
    EvalProduct(
        key="meta-quest-3s-256gb",
        brand="Meta",
        model="Quest 3S",
        variant="256GB, White (SK-1000927-01)",
        category="vr",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 815820025832 (conflicted). "
            "eBay (x2) + Ubuy (x2) give 815820025832; one "
            "Walmart-clearance post gives 815820025833. No retailer "
            "spec page prints a UPC. Verify via Best Buy spec panel "
            "at add time; do not carry either as verified (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Current Meta VR headset (256GB config). MPN "
        "SK-1000927-01 (Best Buy model, SKU 6665817; Adorama MFR + "
        "B&H MFR agree). Best Buy $449.99, sold by Best Buy, Add "
        "to cart; B&H $449.99 In Stock; Adorama $449.99, "
        "temporarily on backorder. Flag: storage config of "
        "in-catalog Quest 3S 128GB (SK-1000926-01, UPC "
        "815820025825) — same precedent as other storage/size "
        "siblings in the catalog. Best Buy listing title includes "
        "a GOLF+ game bundle — same hardware SKU, promo bundle, "
        "not a separate model.",
    ),
    EvalProduct(
        key="samsung-galaxy-watch9-44mm-bt-graphite",
        brand="Samsung",
        model="Galaxy Watch9",
        variant="44mm, Bluetooth, Graphite (SM-L350NZKAXAA)",
        category="wearables",
        identifiers={"UPC": "198957312281", "MPN": "SM-L350NZKAXAA"},
        identifier_sources={
            "UPC": "Samsung's own official US MSRP price lists, "
            "July 2026 AND September 2026 editions "
            "(images.samsung.com: 'SM-L350NZKAXAA — Galaxy Watch9 "
            "44mm BT - Graphite — $409.99 — UPC 198957312281'); "
            "Provartech listing agrees, 0198957312281 (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current Samsung smartwatch (2026). Best Buy $409.99, "
        "sold by Best Buy; T-Mobile LTE version is a different "
        "SKU. Cleanest verified entry in the batch. Size sibling "
        "of in-catalog Watch9 40mm (SM-L340NZKAXAA, pending). "
        "Note: an initial guess SM-L330 was wrong — that is the "
        "Watch8 44mm; Watch9 44mm is SM-L350.",
    ),
    EvalProduct(
        key="google-tv-streamer-4k-porcelain",
        brand="Google",
        model="TV Streamer 4K",
        variant="Porcelain, 32GB (GA05662-US)",
        category="streaming-devices",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 810037291315 (Ferguson "
            "retailer spec page: Manufacturer Part # GA05662-US, "
            "UPC 810037291315; eBay, HiBid, Mozeve all agree but "
            "are not qualifying sources) (batch-5 verification "
            "2026-11-20).",
        },
        status="pending",
        notes="Current Google 4K streaming device. MPN GA05662-US "
        "(Best Buy model, SKU 6586840). Best Buy $149.99, sold by "
        "Best Buy, Add to cart. Hazel is a separate SKU "
        "(GA05802-US) — not this entry. Flag: 2024 launch, still "
        "current with no successor. Price has been $99.99 on promo "
        "before (Dec 2025 shelf photo) — current $149.99 is list; "
        "watch for Black Friday movement.",
    ),
    EvalProduct(
        key="apple-airpods-4-anc-white",
        brand="Apple",
        model="AirPods 4 with Active Noise Cancellation",
        variant="White, with ANC, USB-C case (MXP93LL/A)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 195949689604 (Adorama spec "
            "page 'UPC Code 195949689604' for MXP93LL/A; eBay "
            "listings agree but eBay is not a qualifying source) "
            "(batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Apple mid-tier earbuds (2024). MPN MXP93LL/A "
        "(Adorama MFR; Costco item 1611943 + eBay agree). Adorama "
        "$169.00 (was $179.00); Apple direct list $179.00; Costco "
        "$119.97 (Sept 2026 shelf photo — member price, do not "
        "use as primary row). Flag: PROMO at Adorama ($169 vs "
        "$179 list). Distinct from in-catalog AirPods 5 "
        "(MKFW4LL/A) and AirPods Pro 3 — AirPods 4 ANC is the 2024 "
        "mid-tier, still sold new.",
    ),
    EvalProduct(
        key="nintendo-switch-2-all-in-one-carrying-case-black",
        brand="Nintendo",
        model="Switch 2 All-in-One Carrying Case",
        variant="Black (BEEADECAA)",
        category="accessories",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 045496886042 (GameStop spec "
            "page: UPC 00045496886042, Model Number BEEADECAA; "
            "single retailer-spec source — re-confirm via Best Buy "
            "spec panel at add time) (batch-5 verification "
            "2026-11-20).",
        },
        status="pending",
        notes="Current Nintendo first-party carrying case (holds "
        "console + dock + Pro Controller + cables + 6 game cards). "
        "MPN BEEADECAA (Best Buy model, SKU 6625990; GameStop "
        "Model Number agrees). Best Buy $84.99. GameStop also "
        "lists it (price not captured in crawl). Distinct from "
        "in-catalog Switch 2 Carrying Case & Screen Protector "
        "(BEEAPSSAA, UPC 045496886073, $39.99, currently sold "
        "out/restock-wait) — larger case that holds the dock; do "
        "not merge.",
    ),
    EvalProduct(
        key="sony-srs-xb100-black",
        brand="Sony",
        model="SRS-XB100",
        variant="Black (SRSXB100/B)",
        category="speakers",
        identifiers={"UPC": "027242926059", "MPN": "SRSXB100/B"},
        identifier_sources={
            "UPC": "B&H spec page + Abt 'Model # SRSXB100/B, UPC # "
            "027242926059' + Micro Center agree (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current Sony compact portable speaker (IP67, 16h "
        "battery). Best Buy $63.00; Abt $63.00 InStock; Sweetwater "
        "$47.70 (via Klarna, 2026-11-18). Older Best Buy crawl "
        "showed $49.99 — treat $63.00 as current. Bundle SKUs "
        "SRSXB100B-CR/-KNHC are different listings — do not use "
        "their prices. Ignore Target refurbished listing UPC "
        "732388845965 (refurb listing code, not the manufacturer "
        "UPC).",
    ),
    EvalProduct(
        key="sony-inzone-m10s-black",
        brand="Sony",
        model="INZONE M10S",
        variant="Black (SDM27Q10S)",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 027242930360 (B&H spec page "
            "only; CamelCamelCamel and Desertcart agree but are "
            "not qualifying sources). Snapklik renewed listing "
            "shows 724129293920 — ignore, renewed (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Current Sony 27-inch OLED gaming monitor (QHD 480Hz). "
        "MPN SDM27Q10S (Best Buy, Sony). Best Buy $1,098.00 "
        "(crawl 5 days ago); Sony direct sale $949.99 (orig "
        "$1,199.99, stale crawl); PlayStation Direct $749.99 "
        "promo until Nov 23, 2026. Flag: promo price + wide price "
        "spread — re-verify at add time. M10S II (540Hz) now "
        "exists; M10S is previous-gen but still sold new. Ignore a "
        "Best Buy '$237.99 clearance / Unavailable' artifact on "
        "the same page — not the new price.",
    ),
    EvalProduct(
        key="logitech-brio-500-graphite",
        brand="Logitech",
        model="Brio 500",
        variant="Graphite (960-001493)",
        category="webcams",
        identifiers={"UPC": "097855180452", "MPN": "960-001493"},
        identifier_sources={
            "UPC": "Micro Center 'Mfr Part# 960-001493, UPC "
            "097855180452' + Govets agree; BarcodesInc "
            "corroborates (batch-5 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Logitech 1080p business webcam with "
        "auto-framing. Best Buy $129.99 list, $99.99 Black Friday, "
        "sold by Best Buy. Rose 960-001432 and Off-White "
        "960-001427 are other colors — do not mix. Flag: promo "
        "price ($99.99).",
    ),
    EvalProduct(
        key="logitech-g305-lightspeed-black",
        brand="Logitech",
        model="G305 LIGHTSPEED",
        variant="Black (910-005280)",
        category="mice",
        identifiers={"UPC": "097855137692", "MPN": "910-005280"},
        identifier_sources={
            "UPC": "Newegg 'Model 910-005280, UPC 097855137692' + "
            "Zoro + Tech-America + Electronic Express agree. "
            "Compsource lists a conflicting 695977037243 — single "
            "outlier, ignore (batch-5 verification 2026-11-20).",
        },
        status="verified",
        notes="Long-running Logitech budget wireless gaming mouse, "
        "still sold new at Best Buy/Logitech direct — mainstream "
        "budget staple, not clearance. Best Buy $29.49, $26.99 "
        "Black Friday deal, sold by Best Buy (comp $49.99). Flag: "
        "promo price; 2018-era model but still sold new.",
    ),
    EvalProduct(
        key="jbl-partybox-club-120-black",
        brand="JBL",
        model="PartyBox Club 120",
        variant="Black (JBLPBCLUB120AM)",
        category="speakers",
        identifiers={"UPC": "050036399517", "MPN": "JBLPBCLUB120AM"},
        identifier_sources={
            "UPC": "Abt 'Model # JBLPBCLUB120AM, UPC # 050036399517' "
            "+ Zoro + Electronic Express + Reverb agree (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current JBL party speaker (160W, IPX4, AI Sound "
        "Boost). Best Buy $279.95 (comp $449.95, Black Friday "
        "promo, InStock per JSON-LD). White is JBLPBCLUB120SWAM "
        "— do not mix. Flag: promo price. Abt page now says 'no "
        "longer available' and Zoro marks it 'Discontinued' — "
        "Best Buy is the live new row; re-verify at add time.",
    ),
    EvalProduct(
        key="jbl-live-670nc-black",
        brand="JBL",
        model="Live 670NC",
        variant="Black (JBLLIVE670NCBLKAM)",
        category="headphones",
        identifiers={"UPC": "050036397599", "MPN": "JBLLIVE670NCBLKAM"},
        identifier_sources={
            "UPC": "Abt 'Model # JBLLIVE670NCBLKAM, UPC # "
            "050036397599' + NFM + Erikson Consumer agree "
            "(batch-5 verification 2026-11-20).",
        },
        status="verified",
        notes="Current JBL adaptive noise-cancelling over-ear (65h "
        "battery). Best Buy $129.95 InStock. One Amazon listing "
        "shows UPC 703670638084 for a 'JBL LIVE670NCBLK' (no AM "
        "suffix) listing — do not use; 050036397599 is the "
        "AM-variant code.",
    ),
    EvalProduct(
        key="jbl-vibe-buds-2-black",
        brand="JBL",
        model="Vibe Buds 2",
        variant="Black (JBLVBUDS2BLKAM)",
        category="earbuds",
        identifiers={"UPC": "050036405164", "MPN": "JBLVBUDS2BLKAM"},
        identifier_sources={
            "UPC": "Abt 'Model # JBLVBUDS2BLKAM, UPC # 050036405164' "
            "+ NFM + CPR Accessories agree (batch-5 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Current JBL true-wireless earbuds (Smart Ambient, "
        "40h total). Best Buy $39.95 Black Friday (comp $64.95, "
        "sold by Best Buy, InStock); JBL direct $39.95 InStock. "
        "Flag: promo price. Do not confuse with gen-1 Vibe Buds "
        "(JBLVBUDSBLKAM, UPC 050036391412) — Abt explicitly lists "
        "Vibe Buds 2 as the replacement model. Ignore Target "
        "refurb UPC 732388845767.",
    ),
    EvalProduct(
        key="razer-viper-v3-pro-black",
        brand="Razer",
        model="Viper V3 Pro",
        variant="Black (RZ01-05120100-R3U1)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — strong lead 840272913888 "
            "(XcelSource + Ubuy + eBay agree, but no Best Buy/B&H/"
            "Abt spec page seen yet — verify at add time via Best "
            "Buy spec panel) (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Razer flagship esports wireless mouse (8K "
        "polling, 54g). MPN RZ01-05120100-R3U1 (Best Buy model, "
        "SKU 6576242). Best Buy $99.99 Black Friday (comp "
        "$159.99), Add to cart. Sentinels (RZ01-05120400) and "
        "Faker (RZ01-05120500) editions are different MPNs — do "
        "not mix. Flag: promo price; Snapklik renewed listing "
        "shows conflicting UPC 703670538209 — ignore (renewed).",
    ),
    EvalProduct(
        key="razer-blackwidow-v4-75-black",
        brand="Razer",
        model="BlackWidow V4 75%",
        variant="Black, 75%, wired, Orange Tactile switches (RZ03-05000200-R3U1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272909607 (B&H product "
            "page only; eBay + BarcodeIndex agree but are not "
            "qualifying sources) (batch-5 verification "
            "2026-11-20).",
        },
        status="pending",
        notes="Current Razer 75% hot-swappable gaming keyboard. "
        "MPN RZ03-05000200-R3U1 (Best Buy model, SKU 6554665; "
        "Razer official API confirms this MPN, $189.99, inStock). "
        "Best Buy $129.99 (comp $199.99); Razer direct $189.99 in "
        "stock (stockLevel 20); B&H $129.99 Temporarily Out of "
        "Stock. White variant is RZ03-05001700-R3M1 — do not mix. "
        "B&H OOS; Best Buy/Razer are the live rows.",
    ),
    EvalProduct(
        key="razer-wolverine-v3-tournament-edition-black",
        brand="Razer",
        model="Wolverine V3 Tournament Edition",
        variant="Black, Xbox-licensed wired (RZ06-05210100-R3U1)",
        category="controllers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — conflicted, no usable lead: "
            "840272903537 (eBay GTIN / Slickdeals / Ubuy) vs "
            "8886419351467 (multiple eBay listings) vs 840272919774 "
            "(Snapklik). No retailer spec page seen; needs Best Buy "
            "spec-panel tiebreaker at add time (batch-5 "
            "verification 2026-11-20).",
        },
        status="pending",
        notes="Current Razer Xbox-licensed tournament controller "
        "(Hall Effect sticks, 1000Hz polling). MPN "
        "RZ06-05210100-R3U1 (Best Buy model, SKU 6594729). Best "
        "Buy $74.99; Walmart (sold by Walmart.com) $79.88; "
        "Staples $99.99. Flag: variant-matrix risk — a separate "
        "PC-only '8K' Tournament Edition (RZ06-05550100-R3U1, "
        "$99.99 at Best Buy) shares the name; pin the Xbox "
        "version only. Distinct from in-catalog Wolverine V3 Pro.",
    ),
    EvalProduct(
        key="anker-soundcore-space-q45-black",
        brand="Anker",
        model="Soundcore Space Q45",
        variant="Black (A3040Z11)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 194644105310 (Abt spec page "
            "only; eBay UPC 0194644105310 agrees but is not a "
            "qualifying source) (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current Anker flagship ANC over-ear (98% noise "
        "reduction, 65h battery). MPN A3040Z11 (Best Buy model, "
        "SKU 6514486). Best Buy $149.99. Blue variant is listed "
        "under plain A3040 — pin Black A3040Z11 only.",
    ),
    EvalProduct(
        key="anker-soundcore-liberty-4-nc-black",
        brand="Anker",
        model="Soundcore Liberty 4 NC",
        variant="Black, Velvet Black (A3947Z11)",
        category="earbuds",
        identifiers={"UPC": "194644126124", "MPN": "A3947Z11"},
        identifier_sources={
            "UPC": "Abt 'Model # A3947Z11, UPC # 194644126124' + "
            "Micro Center 'Mfr Part# A3947Z11, UPC 194644126124' "
            "+ Newegg agree (batch-5 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Anker ANC true-wireless earbuds (98.5% noise "
        "reduction, Hi-Res). Best Buy $79.99 InStock (comp $99.99, "
        "deal ends Nov 19, 2026); soundcore direct $79.99. Abt no "
        "longer carries it; bundle listings (A3947Z11 + 20W "
        "charger, $74.99) are separate — do not use bundle price. "
        "Newegg also lists a second UPC 194644132125 and Snapklik "
        "a renewed 194644150860 — unresolved, likely other "
        "colors; 194644126124 is the Abt/Micro Center code for "
        "A3947Z11.",
    ),
    EvalProduct(
        key="garmin-edge-840-black",
        brand="Garmin",
        model="Edge 840",
        variant="Standard, non-Solar, device only (010-02695-00)",
        category="cycling-computers",
        identifiers={"UPC": "753759299927", "MPN": "010-02695-00"},
        identifier_sources={
            "UPC": "Abt 'Model # 010-02695-00, UPC # 753759299927' "
            "+ HLC + HeartRateMonitorsUSA table agree (batch-5 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current Garmin GPS bike computer (touchscreen + "
        "buttons, solar optional). Best Buy $399.99 (comp "
        "$449.99, Add to cart); Performance Bike $399.99; "
        "Crutchfield $449.99. Solar version is 010-02695-20 (UPC "
        "753759300005) — pin non-Solar only.",
    ),
    EvalProduct(
        key="garmin-approach-s70-47mm-black",
        brand="Garmin",
        model="Approach S70",
        variant="47mm, Black ceramic bezel / Black silicone band (010-02746-02)",
        category="wearables",
        identifiers={"UPC": "753759323622", "MPN": "010-02746-02"},
        identifier_sources={
            "UPC": "HeartRateMonitorsUSA table 'MPN + UPC' + Abt "
            "'Model # 010-02746-02, UPC # 753759323622' agree "
            "(batch-5 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Garmin premium golf GPS watch (AMOLED, "
        "43,000+ courses). Best Buy $599.99 (comp $699.99); Abt "
        "$599.99; Cabela's $599.99. 42mm variants are different "
        "MPNs (010-02746-00 White, 010-02746-01 Powder Gray) — pin "
        "47mm Black only. Ignore Best Buy 6ave bundle listings "
        "(010-02746-00-xx, $684.95+) — bundles, not the "
        "standalone row.",
    ),
    EvalProduct(
        key="garmin-descent-mk3-43mm-steel-fog-gray",
        brand="Garmin",
        model="Descent Mk3",
        variant="43mm, Stainless Steel / Fog Gray silicone band (010-02753-03)",
        category="wearables",
        identifiers={"UPC": "753759333027", "MPN": "010-02753-03"},
        identifier_sources={
            "UPC": "HeartRateMonitorsUSA table 'MPN + UPC + "
            "$1,199.99 MSRP' + Scuba.com 'MFR 010-02753-03, UPC "
            "Code 753759333027' agree (batch-5 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Current Garmin dive computer/smartwatch (AMOLED, "
        "200m, multi-gas). Best Buy $899.99 (comp $1,199.99); The "
        "GPS Store $899.99 in stock; Garmin holiday promo Nov 13–"
        "Dec 28, 2026 ($899.99, was $1,199.99). Flag: promo price "
        "(holiday promo). Distinct from seed Descent G1 and "
        "in-catalog Descent G2/X10; Mk3i (air-integrated, "
        "010-02753-10) is a different model.",
    ),
    EvalProduct(
        key="jbl-authentics-300-black",
        brand="JBL",
        model="Authentics 300",
        variant="Black (JBLAUTH300BLKAM)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 050036396271 (Amazon item "
            "details only, four listings agree — Amazon-only, not "
            "verified; needs a retailer spec page at add time). "
            "Plausible by series (Authentics 500 is ...6264) but "
            "unproven (batch-5 verification 2026-11-20).",
        },
        status="pending",
        notes="Current JBL portable smart home speaker "
        "(Wi-Fi/Bluetooth, 8h battery, retro design). MPN "
        "JBLAUTH300BLKAM (JBL.com official + Crutchfield MFR # "
        "agree). JBL direct $249.95 (was $449.95, Black Friday "
        "promo); Sweetwater $249.95 ($250 off through 12/5/2026); "
        "Crutchfield $499.95 (stale 70-day crawl); Best Buy $450 "
        "list. Flag: promo price. Distinct from the Authentics "
        "500 — 300 is the portable battery model, 500 is the "
        "flagship.",
    ),
    EvalProduct(
        key="samsung-hw-q600f-black",
        brand="Samsung",
        model="HW-Q600F",
        variant="Black, Titan Black (HW-Q600F/ZA)",
        category="soundbars",
        identifiers={"UPC": "887276936895", "MPN": "HW-Q600F/ZA"},
        identifier_sources={
            "UPC": "B&H spec page + Walts TV + Worldwide Stereo spec "
            "pages agree (batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Samsung 2025 Q-series 3.1.2ch soundbar. Best "
        "Buy $399.99 Black Friday (comp $699.99), sold by Best Buy; "
        "B&H $397.99 In Stock. Flag: promo price (Black Friday ends "
        "Nov 28, 2026). Amazon lists a conflicting UPC 887276835426 "
        "— non-qualifying, disregarded. (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="lenovo-thinkpad-t14-gen-5-black",
        brand="Lenovo",
        model="ThinkPad T14 Gen 5",
        variant="Black, 21MC000CUS — Ryzen 7 PRO 8840U, 16GB, 512GB, 14\" WUXGA",
        category="laptops",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 198153286874 (B&H only; needs "
            "a second qualifying source).",
        },
        status="pending",
        notes="MPN 21MC000CUS confirmed (B&H spec page + CDW spec "
        "page agree). B&H $1,499.00 In Stock; CDW In Stock, $1,486.99 "
        "advertised (price varies across crawls, re-check at add "
        "time). Distinct from backlog T14 Gen 6 (21QJ00CSUS) and "
        "the 21ML0053US touchscreen config. (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="lenovo-thinkpad-x1-carbon-gen-13-aura-edition",
        brand="Lenovo",
        model="ThinkPad X1 Carbon Gen 13 Aura Edition",
        variant="21NS0012US — Core Ultra 7 258V, 32GB, 1TB, 14\" 2.8K OLED, Eclipse Black",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 21NS0012US verified with caveat (lenovo.com "
        "product page + Newegg listing page, search-fetch — the "
        "Newegg direct open hit the bot wall, so the leg is one "
        "step weaker than a direct open). UPC no qualifying lead — "
        "B&H prints 828143670351 but that is a different config "
        "(21NTSB8E00); do NOT attach it. Lenovo.com $1,248.99 "
        "InStock (confirmed at add time 2026-11-20). Add-time "
        "retailer check: no retailer-direct row — Best Buy only IST "
        "Computers 'Upgraded' marketplace listings; a Newegg "
        "listing for the exact config exists but price/seller/stock "
        "are unverified behind the bot wall; CDW has no listing. "
        "Flag: Lenovo-direct only, no clean retailer row "
        "— DECISIONS 015 concern (the single flagged "
        "brand-direct-only pick in batch 6). (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="sony-wf-c700n-black",
        brand="Sony",
        model="WF-C700N",
        variant="Black (WFC700N/B)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 027242925625 (Abt only; Amazon "
            "agrees but is non-qualifying).",
        },
        status="pending",
        notes="MPN WFC700N/B confirmed (Best Buy model field + "
        "Crutchfield MFR # + Abt Model # agree). Best Buy $79.99 "
        "Black Friday (comp $118) / $119.99 list. Flag: promo price "
        "(Black Friday ends Nov 28, 2026). B&H 'No Longer "
        "Available' — source only, not the row. (batch-6 "
        "verification 2026-11-20).",
    ),
    EvalProduct(
        key="sony-inzone-h3-white",
        brand="Sony",
        model="INZONE H3",
        variant="White (MDR-G300 / MDRG300/W)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 027242923546 (B&H specs page "
            "only; Amazon agrees, non-qualifying).",
        },
        status="pending",
        notes="MPN MDR-G300 confirmed (Best Buy model field MDRG300/W "
        "+ B&H MFR # + Crutchfield MFR # agree). Best Buy $69.99, "
        "sold by Best Buy; B&H $68.00 In Stock (was $118.00). "
        "Kawartha TV (Canadian, non-qualifying) lists UPC "
        "027242923522 for MDRG300/W — disregarded; B&H + Amazon "
        "agree on ...546. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="sony-ht-a5000-black",
        brand="Sony",
        model="HT-A5000",
        variant="Black (HTA5000)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 656942665540 is "
            "non-qualifying only (manuals.plus); no qualifying "
            "source prints it.",
        },
        status="pending",
        notes="MPN HT-A5000 confirmed (Best Buy model field HTA5000 "
        "+ Crutchfield MFR # agree). Best Buy $499.99, Sold by Best "
        "Buy, InStock, SKU 6467455 (add-time re-check 2026-11-20); "
        "$699.99 is a parallel listing, SKU 10917148 — not the BF "
        "price. B&H no longer carries it "
        "(replacement page for HT-A8000). (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="sony-ht-s400-black",
        brand="Sony",
        model="HT-S400",
        variant="Black (HTS400)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 027242923942 is "
            "non-qualifying only (Amazon; a Best Buy-spec mirror "
            "site also shows it, not qualifying).",
        },
        status="pending",
        notes="MPN HT-S400 confirmed (Best Buy model field HTS400 + "
        "B&H MFR # agree). Best Buy $199.99 InStock, Model HTS400, "
        "SKU 6498905. Flag: promo price (Black Friday ends Nov 28, "
        "2026). (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="logitech-g435-black",
        brand="Logitech",
        model="G435",
        variant="Black (981-001049)",
        category="headphones",
        identifiers={"UPC": "097855165763", "MPN": "981-001049"},
        identifier_sources={
            "UPC": "Abt 'UPC # 097855165763' + Best Buy spec page "
            "'Model Number: 981-001049 … UPC: 097855165763' agree "
            "(batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Logitech wireless gaming headset. Best Buy "
        "$49.99 in a 1-day-old crawl (Black Friday banner ends Nov "
        "28, 2026) — but the live Best Buy product page at add time "
        "2026-11-20 reads 'no longer available in new condition', "
        "with no price/seller/stock block; the row needs a "
        "live-browser re-check. Abt 'no longer available' — source "
        "only, not the row. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="logitech-brio-100-graphite",
        brand="Logitech",
        model="Brio 100",
        variant="Graphite (960-001580)",
        category="webcams",
        identifiers={"UPC": "097855188588", "MPN": "960-001580"},
        identifier_sources={
            "UPC": "B&H spec page 'UPC: 097855188588' + Logitech's "
            "own datasheet PDF ('Part # 960-001580 … Bar code "
            "097855188588 (EAN-13)') agree — caveat: the datasheet "
            "is hosted on Zoro's static CMS, not logitech.com; the "
            "content is verbatim Logitech (batch-6 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Current Logitech 1080p webcam. Best Buy $39.99, sold "
        "by Best Buy, InStock, SKU 6550199; B&H $24.99 In Stock "
        "(was $39.99). (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="logitech-signature-m650-l-graphite",
        brand="Logitech",
        model="Signature M650 L",
        variant="Graphite, consumer full-size L (910-006231)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855167583 (B&H only; "
            "Adorama agrees but is not on the qualifying list).",
        },
        status="pending",
        notes="MPN 910-006231 confirmed (Best Buy model field + "
        "Newegg Model # + NeweggBusiness Mfr. Part # agree). Best "
        "Buy $24.99 Black Friday, sold by Best Buy, InStock, SKU "
        "6491142 (list $39.99); B&H $29.99 In Stock. Distinct from "
        "in-catalog Signature M650 (non-L, standard size). Do not "
        "mix: 910-006347 is the for-Business Off-White variant. "
        "(batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="logitech-zone-vibe-125-graphite",
        brand="Logitech",
        model="Zone Vibe 125",
        variant="Graphite (981-001166)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 097855175113 (Logitech "
            "datasheet PDF 'Part # 981-001166 … UPC 097855175113'; "
            "Amazon agrees, non-qualifying).",
        },
        status="pending",
        notes="MPN 981-001166 confirmed (Best Buy model field + B&H "
        "page title agree). Best Buy $129.99; B&H 'No Longer "
        "Available'. Distinct from in-catalog Zone Vibe 100. Zone "
        "Vibe Wireless Teams (981-001440) is a different model. "
        "Snapklik lists UPC 657768069680 for this part number "
        "(non-qualifying, conflicts with datasheet + Amazon) — "
        "disregarded. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="jbl-authentics-200-black",
        brand="JBL",
        model="Authentics 200",
        variant="Black (JBLAUTH200BLKAM)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 050036396219 (B&H specs page "
            "only; Amazon/manuals.plus/Snapklik agree, all "
            "non-qualifying).",
        },
        status="pending",
        notes="MPN JBLAUTH200BLKAM confirmed (JBL.com Item# + B&H "
        "title + Crutchfield MFR # agree). Best Buy $189.95 Black "
        "Friday (comp $379.95); B&H $189.95 In Stock; Abt $189.95 "
        "InStock. Flag: promo price (Black Friday ends Nov 28, "
        "2026). (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="jbl-partybox-encore-essential-2-black",
        brand="JBL",
        model="PartyBox Encore Essential 2",
        variant="Black (JBLPBENCOREESS2AM)",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 050036411059 (B&H only; "
            "Walts/NFM agree, not qualifying).",
        },
        status="pending",
        notes="MPN JBLPBENCOREESS2AM confirmed (B&H MFR # + Best Buy "
        "model field + Abt title + Dell Manufacturer Part Number "
        "agree). Best Buy $199.95 InStock, sold by Best Buy, SKU "
        "6644260 (supersedes the draft's SKU 10209209 @ $329.99); "
        "B&H $199.95 In Stock; Abt $199.95 InStock. Do NOT use "
        "Best Buy SKU 12942222 — bundle with EASYSING mic, "
        "marketplace. Premium Encore 2 with 2 mics is a different "
        "$400 model (JBLPBENCORE22MICAM). (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="jbl-bar-500-black",
        brand="JBL",
        model="Bar 500",
        variant="Black (JBLBAR500PROBLKAM)",
        category="soundbars",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 050036387743 is "
            "non-qualifying only (Amazon / Walts / Zoro agree; none "
            "is qualifying).",
        },
        status="pending",
        notes="MPN JBLBAR500PROBLKAM confirmed (JBL.com Item# + "
        "Crutchfield MFR # + Best Buy model field agree) — the "
        "draft's 'BAR-500' was a shortened display name, not the "
        "full MPN. Best Buy $399.95 InStock, SKU 11113238; JBL.com "
        "$399.99 InStock at add-time re-check 2026-11-20 — the "
        "$349.95 OutOfStock same-day flip reversed (page Item# "
        "BAR500PROBLKAM-Z). BAR500MK2 is the newer model — pin "
        "the original Bar 500. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="jbl-tune-520bt-black",
        brand="JBL",
        model="Tune 520BT",
        variant="Black (JBLT520BTBLKAM)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 050036394925 is "
            "non-qualifying only (BJ's Wholesale; Amazon agrees, "
            "non-qualifying).",
        },
        status="pending",
        notes="MPN JBLT520BTBLKAM confirmed (JBL.com manufacturer "
        "item# + Best Buy Canada model field agree). JBL.com "
        "$34.95 InStock; Walmart $34.95 (was $59.95); Target "
        "$59.99 OutOfStock. Flag: promo price. Do not mix with the "
        "personalized variant T520BTBLKAMCSTM. (batch-6 "
        "verification 2026-11-20).",
    ),
    EvalProduct(
        key="lenovo-legion-pro-5-gen-10-eclipse-black",
        brand="Lenovo",
        model="Legion Pro 5 Gen 10",
        variant="Eclipse Black, 83LT000MUS — Ryzen 7 8745HX, RTX 5060, 32GB, 1TB, 16\" WQXGA OLED",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 83LT000MUS confirmed (lenovo.com product page + "
        "Best Buy model field agree). UPC no lead found. Successor "
        "to the dropped Legion Pro 5 16IRX9 (its Best Buy row is "
        "dead). Best Buy direct SKU 6619246 — $1,774.99, Sold by "
        "Best Buy, InStock at add-time re-check 2026-11-20 (the "
        "$1,579.99 was a 13-day-old crawl; the stale $1,179.99 "
        "Slickdeals figure is Feb 2026 — do not carry either). "
        "lenovo.com $2,360.15 InStock as the non-promo reference. "
        "Do not mix with the kelaptop listing that "
        "mislabels the CPU as Ryzen 9 7845HX. (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="razer-blackshark-v3-black",
        brand="Razer",
        model="BlackShark V3",
        variant="Black, PC version (RZ04-05410100-R3U1)",
        category="headphones",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN RZ04-05410100-R3U1 confirmed (Best Buy model field "
        "+ Newegg Model # agree). UPC no qualifying lead — "
        "840272919606 appears only on Amazon / eBay / HeadphoneTune "
        "(non-qualifying). Best Buy $129.99 InStock — currently sold "
        "& shipped by Electronic Express (marketplace); an older "
        "crawl said 'Sold by Best Buy'. Not currently a direct row "
        "at Best Buy. Newegg $129.99; Razer.com $149.99 InStock. "
        "Distinct from in-catalog BlackShark V3 Pro. (batch-6 "
        "verification 2026-11-20).",
    ),
    EvalProduct(
        key="razer-cobra-black",
        brand="Razer",
        model="Cobra",
        variant="Black, wired (RZ01-04650100-R3U1)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272903049 (ChannelOnline "
            "distributor listing only; eBay / Desertcart agree, "
            "non-qualifying; B&H spec page prints no UPC).",
        },
        status="pending",
        notes="MPN RZ01-04650100-R3U1 confirmed (Best Buy model field "
        "+ B&H spec page MFR # agree). Best Buy $29.99 Black Friday "
        "(comp $39.99), sold by Best Buy; B&H $29.99 live. Flag: "
        "promo price (Black Friday ends Nov 28, 2026). Pokemon "
        "edition RZ01-04650400-R3M1 ($44.99) is different — do not "
        "mix. Distinct from in-catalog Cobra Pro (wireless). "
        "(batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="razer-huntsman-v3-pro-mini-black",
        brand="Razer",
        model="Huntsman V3 Pro Mini",
        variant="Black, 60% Mini standard (RZ03-04990200-R3U1)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840272909409 (Micro Center "
            "quickView spec panel prints it cleanly, 2026-11-20 "
            "add-time re-fetch; eBay / PayMore / Ubuy / Desertcart "
            "agree, non-qualifying — still a single qualifying "
            "source, needs a second).",
        },
        status="pending",
        notes="MPN RZ03-04990200-R3U1 pending + lead (Best Buy full "
        "print, SKU 6558755; Micro Center prints only the "
        "truncated 'RZ03-04990200-R' — a truncated snippet cannot "
        "carry a VERIFIED verdict). Best Buy $124.99 Black Friday "
        "(comp $179.99), Sold by Best Buy, InStock; Micro Center "
        "$139.99 InStoreOnly. A newer '8KHz' version is being "
        "promoted by Razer — pin the standard Mini. Distinct from "
        "in-catalog Huntsman V3 Pro (full-size). (batch-6 "
        "verification 2026-11-20).",
    ),
    EvalProduct(
        key="lenovo-thinkpad-t16-gen-4-black",
        brand="Lenovo",
        model="ThinkPad T16 Gen 4",
        variant="Black, 21QN005XUS — Ryzen AI 7 PRO 350, 16GB, 512GB, 16\" WUXGA",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 21QN005XUS confirmed (CDW spec page MFG# + Newegg "
        "listing page, search-fetch — the Newegg direct open hit "
        "the bot wall; corroborated by SHI distributor listing). "
        "UPC no lead found. CDW In Stock, $1,483.99 advertised — "
        "add-time re-check 2026-11-20: the direct CDW page did not "
        "reproduce the price/stock block, so $1,483.99/In Stock "
        "holds on the 4-day-old CDW crawl only. Adorama "
        "$1,649.00 'Ships from Manufacturer' (corroboration only). "
        "Newegg $1,162.02–$1,257.93 seller attribution unclear — do "
        "not use as the row. Distinct from the 21QN0045US config "
        "(backlog sibling). (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="anker-soundcore-aerofit-2-black",
        brand="Anker",
        model="Soundcore AeroFit 2",
        variant="Black, base model (A3874Z11)",
        category="earbuds",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 194644036393 (B&H only; Micro "
            "Center Black page fetch returned a support page with "
            "no Mfr Part # / UPC).",
        },
        status="pending",
        notes="MPN A3874Z11 confirmed (B&H spec page + Crutchfield "
        "MFR # agree). B&H $79.99 InStock; Micro Center $69.99 "
        "InStock; soundcore.com $129.99 list; Best Buy $79.99. AI "
        "Assistant version is a different listing at $109.99 "
        "(A3874Z12) — pin base Black only. (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="anker-prime-67w-gan-charger",
        brand="Anker",
        model="Prime 67W GaN Wall Charger",
        variant="67W, 3-port GaN (A2669)",
        category="chargers",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN A2669 confirmed (Anker.com Model Number + Newegg "
        "spec page agree — caveat: the Newegg leg rests on the "
        "search fetch of its spec page, not a direct open; the "
        "direct open hit the Newegg bot wall). UPC no qualifying "
        "lead — 194644137373 appears only on Amazon / eBay / Ubuy "
        "(non-qualifying); the Rakuten product URL digits "
        "00194644137373 are NOT a verified identifier. Anker.com "
        "$49.99 InStock; AnkerDirect via Best Buy $34.99 "
        "(Slickdeals 2026-11-02); Newegg $49.99. Flag: promo price "
        "$34.99 vs $49.99 list. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="garmin-venu-3s-pebble-gray",
        brand="Garmin",
        model="Venu 3S",
        variant="Pebble Gray, 41mm (010-02785-00)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 753759314774 (Petra + "
            "CompSource distributors agree — distributor + "
            "distributor is beyond the batch-5 precedent, so no "
            "upgrade).",
        },
        status="pending",
        notes="MPN 010-02785-00 confirmed (Best Buy model field + "
        "Crutchfield agree). Best Buy $299.99 InStock, Sold by "
        "Best Buy (comp $449.99). Distinct from in-catalog Venu 3 "
        "(45mm; 3S is 41mm). Do not mix: Venu 3 45mm is a different "
        "model (010-02784-00 / 010-02784-01). (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="garmin-approach-s44-black",
        brand="Garmin",
        model="Approach S44",
        variant="Black (010-03009-00)",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 753759350666 (Abt only; "
            "Crutchfield search returned only the Twilight variant "
            "010-03009-01; B&H search returned no listing).",
        },
        status="pending",
        notes="MPN 010-03009-00 confirmed (Abt Model # + Garmin.com "
        "product page agree). Best Buy $249.99 (comp $299.99), sold "
        "by Best Buy. Flag: promo price (Black Friday ends Nov 28, "
        "2026). Do not mix: Twilight variant is 010-03009-01, UPC "
        "753759350673 — different model. (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="garmin-edge-1040-solar-black",
        brand="Garmin",
        model="Edge 1040 Solar",
        variant="Black, Solar (010-02503-20)",
        category="cycling-computers",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 010-02503-20 confirmed (Best Buy model field + "
        "buy.garmin.com cart page agree). UPC no qualifying lead — "
        "753759279752 appears only at bike shops / Summit Racing / "
        "Snapklik (non-qualifying). Garmin.com $649.99 (ships in "
        "2–3 weeks). Best Buy $599.99 InStock — sold & shipped by "
        "FrontRow Tech, an Authorized Dealer marketplace seller "
        "(not a direct row). Pin Solar only; non-Solar Edge 1040 "
        "is 010-02503-00 — different listing. Distinct from "
        "in-catalog Edge 1050. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="samsung-galaxy-smarttag-2-black",
        brand="Samsung",
        model="Galaxy SmartTag 2",
        variant="Black (EI-T5600BBEGUS)",
        category="trackers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 887276765358 (Micro Center "
            "only qualifying; NFM agrees but is outside the "
            "qualifying list).",
        },
        status="pending",
        notes="MPN EI-T5600BBEGUS confirmed (Best Buy model field + "
        "Micro Center spec page Mfr Part# agree). Best Buy $25.00 "
        "(comp $29.99), sold by Best Buy. Price fluctuates "
        "$25–$26.93 across crawls (promo) — re-check at add time. "
        "(batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="samsung-hw-q800f-black",
        brand="Samsung",
        model="HW-Q800F",
        variant="Black (HW-Q800F/ZA)",
        category="soundbars",
        identifiers={"UPC": "887276934242", "MPN": "HW-Q800F/ZA"},
        identifier_sources={
            "UPC": "B&H spec page + ADI Global Distribution "
            "distributor spec agree — second source is a distributor "
            "listing, not a core retailer (batch-6 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Current Samsung 5.1.2 Dolby Atmos soundbar (2025). "
        "$1,097.99 (B&H, Crutchfield, In Stock); Best Buy list "
        "$1,099.99. Some crawls show $537.99 marketplace rows / "
        "'Sold Out' flags — not usable. Distinct from in-catalog "
        "HW-Q990F. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="samsung-hw-qs700f-black",
        brand="Samsung",
        model="HW-QS700F",
        variant="Black, 3.1.2ch convertible (HW-QS700F/ZA)",
        category="soundbars",
        identifiers={"UPC": "887276934273", "MPN": "HW-QS700F/ZA"},
        identifier_sources={
            "UPC": "B&H spec page + ADI Global Distribution "
            "distributor spec agree — second source is a distributor "
            "listing, not a core retailer (batch-6 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Current Samsung 2025 soundbar (Convertible Flip "
        "design, Wireless Dolby Atmos, SpaceFit Sound Pro, "
        "Q-Symphony). Best Buy $347.99 Black Friday (list $699.99); "
        "Crutchfield $597.99 (list $697.99), InStock; $597.99 "
        "(B&H, Abt, InStock). Flag: promo price (Black Friday ends "
        "Nov 28, 2026). Abt notes a manufacturer rebate ending "
        "11/22/2026. Distinct from in-catalog HW-Q990F and "
        "in-batch HW-Q800F. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="microsoft-surface-laptop-13-2025-ocean-512gb",
        brand="Microsoft",
        model="Surface Laptop 13\" (2025)",
        variant="Ocean, 512GB, Snapdragon X Plus (EP2-33432)",
        category="laptops",
        identifiers={"UPC": "196388548231", "MPN": "EP2-33432"},
        identifier_sources={
            "UPC": "B&H spec page UPC + Abt UPC # 196388548231 "
            "agree (batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Microsoft 13-inch Snapdragon X Plus laptop. "
        "Best Buy Ocean 512GB $1,149.99 (comp $1,249.99), Add to "
        "cart, InStock, SKU 10148535. Flag: promo price (Black "
        "Friday ends Nov 28, 2026). Distinct from in-catalog "
        "Surface Laptop 13.8\" 8th Edition (EP2-59028) and 15\" 8th "
        "Edition — different MPN, size, and chip generation. "
        "Target calls this model '8th Edition' — do not conflate. "
        "(batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="apple-140w-usb-c-power-adapter-white",
        brand="Apple",
        model="140W USB-C Power Adapter",
        variant="White (MKFQ4AM/A)",
        category="chargers",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN MKFQ4AM/A confirmed (Best Buy model field + B&H "
        "MFR # + Apple.com shop product agree). UPC no lead for "
        "MKFQ4AM/A — no qualifying source prints a UPC for this "
        "part. $99.00 (Apple.com, B&H, InStock); Adorama $129.00. "
        "Two Best Buy SKUs exist (old 6485370 vs new MKFQ4AM/A "
        "6530838); pin the new MKFQ4AM/A. Do NOT confuse with "
        "MW2M3AM/A (B&H lists it as a 140W adapter with UPC "
        "195949376955 — a different, newer part) or old MLYU3AM/A "
        "(UPC 194252750629). (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="apple-35w-dual-usb-c-compact-power-adapter-white",
        brand="Apple",
        model="35W Dual USB-C Port Compact Power Adapter",
        variant="White, compact (MW2H3AM/A)",
        category="chargers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 195949376535 (Micro Center "
            "only qualifying; NFM + Datavision agree but are outside "
            "the qualifying list).",
        },
        status="pending",
        notes="MPN MW2H3AM/A confirmed (B&H MFR # + Apple.com shop "
        "product + Micro Center Mfr Part# agree). $59.00 "
        "(Apple.com, InStock); $59.99 (B&H). Some crawls show "
        "$49.99 (promo-sensitive). UPC split — do not cross: "
        "compact MW2H3AM/A = 195949376535; non-compact MW2K3AM/A = "
        "195949376573. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="garmin-fenix-8-solar-sapphire-47mm-carbon-gray",
        brand="Garmin",
        model="Fenix 8 Solar Sapphire",
        variant="47mm, Carbon Gray DLC Titanium (010-02906-10)",
        category="wearables",
        identifiers={"UPC": "753759339326", "MPN": "010-02906-10"},
        identifier_sources={
            "UPC": "Garmin official FENIX 8 SERIES price list PDF + "
            "CompSource 'UPC EAN CODE: 753759339326' agree (batch-6 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current Garmin solar smartwatch (MIP display). Best "
        "Buy $749.99 (comp $999.99, Save $250), Sold by Best Buy, "
        "Add to cart, InStock, SKU 6594318. Garmin price list MRP "
        "$1,099.99. Distinct from in-catalog Fenix 8 AMOLED "
        "Sapphire 47mm (010-02904-20) — Solar MIP vs AMOLED — and "
        "from Fenix 9 47mm (010-04762-00). Correction: the initial "
        "guess 010-02904-00 was WRONG — that is the AMOLED Slate "
        "Gray. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="logitech-signature-slim-k950-graphite",
        brand="Logitech",
        model="Signature Slim K950",
        variant="Graphite, US layout (920-012424)",
        category="keyboards",
        identifiers={"UPC": "097855192974", "MPN": "920-012424"},
        identifier_sources={
            "UPC": "B&H product page 'UPC: 097855192974' + "
            "Tech-America distributor spec agree — caveat: "
            "Tech-America and PC-Canada share the same data feed, "
            "so the second source is a distributor listing, not a "
            "second major retailer (batch-6 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Current Logitech slim wireless keyboard. B&H $69.99 "
        "InStock (was $89.99) — the clean row; Staples $69.99 "
        "InStock. Best Buy $89.99, but one listing (SKU 10201839) "
        "is 'Sold & shipped by EP Holdings Inc' (marketplace — do "
        "not use). Do not mix with K980 Solar+ or MK950 combo. "
        "(batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="asus-zenwifi-axe7800-3-pack-white",
        brand="ASUS",
        model="ZenWiFi AXE7800",
        variant="White, 3-pack (AXE7800 (W-3-PK))",
        category="routers",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN ZenWiFi AXE7800 confirmed (ASUS official + Newegg "
        "spec page 'Part Number 90IG07D0-MA1A2V, Model # ZenWiFi "
        "AXE7800, 3-Pack' agree). UPC no qualifying lead; eBay "
        "GTIN 0197105421790 is not qualifying. ASUS $299.99 "
        "InStock; Newegg $329.99. Best Buy row dead: the current "
        "listing is sold/shipped by Newegg Official (marketplace) "
        "at $356.49 — NOT Best Buy direct. Category reconciled to "
        "'routers' at add time (was 'networking' in the draft). "
        "Flag: promo price (Black Friday ends Nov 28, 2026). The "
        "hardware is also sold as ZenWiFi ET9 — the retail 3-pack "
        "is AXE7800 (W-3-PK). (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="samsung-hw-s60d-black",
        brand="Samsung",
        model="HW-S60D",
        variant="Black (HW-S60D/ZA)",
        category="soundbars",
        identifiers={"UPC": "887276823935", "MPN": "HW-S60D/ZA"},
        identifier_sources={
            "UPC": "B&H spec page + Samsung official HW-S60D spec "
            "sheet ('UPC CODE: 887276823935') agree (batch-6 "
            "verification 2026-11-20).",
        },
        status="verified",
        notes="Current Samsung all-in-one 5.0ch Dolby Atmos soundbar "
        "(2024). Best Buy $279.99 Black Friday (comp $399.99), sold "
        "by Best Buy, Add to cart. Flag: promo price (Black Friday "
        "ends Nov 28, 2026). Canadian /ZC variant has a different "
        "UPC 887276824543 — pin the US /ZA only. Distinct from the "
        "in-catalog HW-LS60D Music Frame (different model). "
        "(batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="dell-g16-7630-gray",
        brand="Dell",
        model="G16 7630",
        variant="Gray, RTX 4070 / i9-13900HX / 32GB / 1TB (Dell-direct config)",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN pending + lead (Dell order codes "
        "useghbto7630glmf / useghbto7630fwmg — no single MPN; two "
        "order codes seen for the same spec, likely differing in "
        "minor config options; Icecat CN76154 is a different code "
        "format and not a second source for the same code). UPC no "
        "lead. Dell.com $1,949.99–$1,959.99 (crawls 88 and 135 days "
        "old — stale; NOT confirmed at add time 2026-11-20: the "
        "Dell.com page could not be fetched, no current listing "
        "surfaced, and laptopmedia shows the exact 32GB config "
        "'Not available'; no retailer-direct row found). "
        "Correction to the "
        "first draft: Dell.com DOES still list this config; the "
        "'discontinued at Dell' conclusion is withdrawn. Flag: "
        "Dell-direct only (DECISIONS 015 concern — the second "
        "flagged brand-direct-only pick alongside the X1 Carbon). "
        "Color naming unverified: Icecat shows Black ('Zwart') vs "
        "the draft's Gray. Best Buy only shows an 'Upgraded' "
        "third-party config at $2,879 — not usable. (batch-6 "
        "verification 2026-11-20).",
    ),
    EvalProduct(
        key="hp-victus-15-fb3093dx-mica-silver",
        brand="HP",
        model="Victus 15",
        variant="Mica Silver, 15-fb3093dx (BM4X8UA#ABA)",
        category="laptops",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 199251266874 (HP datasheet "
            "only — needs a second qualifying source; eBay also "
            "prints it, does not count).",
        },
        status="pending",
        notes="MPN 15-fb3093dx / BM4X8UA#ABA confirmed (Best Buy "
        "model field + HP datasheet Product number agree). Best Buy "
        "$949.99 (Holiday Deal). One snippet mentions $639.99 for "
        "the same specs (possibly an older deal price) — price "
        "volatility, re-check at add time. (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="samsung-galaxy-buds3-silver",
        brand="Samsung",
        model="Galaxy Buds3",
        variant="Silver (SM-R530NZAAXAR)",
        category="earbuds",
        identifiers={"UPC": "887276868059", "MPN": "SM-R530NZAAXAR"},
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec + Abt page "
            "agree (batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Samsung earbuds (2024). Best Buy $109.95 "
        "InStock (new, SKU 12901715); B&H $124.95 In Stock (was "
        "$174.95); Micro Center $49.99 but OutOfStock (do not use "
        "as the row). Best Buy also lists a refurbished Excellent "
        "unit ($84.99, Elite Tech LLC marketplace) under a "
        "different SKU — pin the new SKU 12901715 only and confirm "
        "sold-by-Best-Buy at add time. Distinct from in-catalog "
        "Buds3 Pro, Buds3 FE, Buds4, Buds4 Pro. (batch-6 "
        "verification 2026-11-20).",
    ),
    EvalProduct(
        key="asus-rog-swift-oled-pg32ucdm-black",
        brand="ASUS",
        model="ROG Swift OLED PG32UCDM",
        variant="Black, 32\" 4K 240Hz QD-OLED (PG32UCDM)",
        category="monitors",
        identifiers={"UPC": "197105413726", "MPN": "PG32UCDM"},
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec agree "
            "(batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Flagship 32-inch 4K QD-OLED ROG monitor. B&H $1,229.00 "
        "InStock (retailer-direct row). Do NOT mix with PG32UCDM3 "
        "Gen3 (UPC 199291274662, B&H $1,278.70) or PG32UCDMR (UPC "
        "199291033863, B&H $899 Holiday / $1,299.99 list) — distinct "
        "variants with their own UPCs. Distinct from in-catalog "
        "PG32UCWM and PG27UCDM. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="asus-rt-be86u-black",
        brand="ASUS",
        model="RT-BE86U",
        variant="Black, BE6800 Dual-Band Wi-Fi 7 (RT-BE86U)",
        category="routers",
        identifiers={"UPC": "197105581432", "MPN": "RT-BE86U"},
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec (SKU 792663) "
            "agree (batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Wi-Fi 7 router (successor to RT-AX86U). B&H "
        "$239.99 InStock (row). Best Buy $255.99–$269.99, sold by "
        "Best Buy (price varies across crawls; one crawl showed "
        "$179.99 — likely open-box/clearance confusion, do not "
        "use). ASUS list $249.99. Distinct from in-catalog "
        "RT-BE58U. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="microsoft-surface-thunderbolt-4-dock-black",
        brand="Microsoft",
        model="Surface Thunderbolt 4 Dock",
        variant="Black (T8I-00001)",
        category="docks",
        identifiers={"UPC": "196388142200", "MPN": "T8I-00001"},
        identifier_sources={
            "UPC": "B&H + Zoro distributor spec 'Mfr # T8I-00001, "
            "UPC # 196388142200' agree (batch-6 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Current Microsoft dock. Best Buy $299.99 (one crawl "
        "$214.99 — promo-sensitive), sold by Best Buy, Add to "
        "cart; Newegg ~$251.99; Zoro $272.99. Replaces the Surface "
        "Dock 2 (clearance-only). (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="asus-rt-be92u-black",
        brand="ASUS",
        model="RT-BE92U",
        variant="Black, BE9700 Tri-Band Wi-Fi 7 (RT-BE92U)",
        category="routers",
        identifiers={"UPC": "197105580633", "MPN": "RT-BE92U"},
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec (SKU 800631) "
            "agree (batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Current tri-band Wi-Fi 7 router with 10G port. Best "
        "Buy $265.51 InStock (list $289.99) — retailer-direct row; "
        "B&H $285.99; ASUS US $289.99 InStock. Best Buy price is "
        "promo-sensitive — re-verify at add time. Refurbished "
        "RT-BE92U-RB (SKU 12760801, $166.24) is a different "
        "listing — do not mix. Distinct from RT-BE86U and "
        "in-catalog RT-BE58U. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="meta-ray-ban-skyler-gen-2-green-shiny-black",
        brand="Meta",
        model="Ray-Ban Meta Skyler (Gen 2)",
        variant="Shiny Black, Green lenses (0RW4014_601/7152)",
        category="smart-glasses",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 0RW4014_601/7152 pending + lead (Best Buy product "
        "page, SKU 6642578, 'Model: 0RW4014_601/7152', Sold by "
        "Best Buy — single qualifying source; meta.com does not "
        "print the code). UPC no lead. Best Buy $379.00 InStock, "
        "Sold by Best Buy; meta.com $379 InStock. Transitions "
        "variants $459 — pin Green only. The Transitions Green "
        "variant is a DIFFERENT model: Best Buy Model "
        "0RW4014_601/1M52, SKU 6642596, $459.00. (batch-6 "
        "verification 2026-11-20).",
    ),
    EvalProduct(
        key="google-nest-hub-2nd-gen-charcoal",
        brand="Google",
        model="Nest Hub (2nd Gen)",
        variant="Charcoal (GA01892-US)",
        category="smart-home",
        identifiers={"UPC": "193575009223", "MPN": "GA01892-US"},
        identifier_sources={
            "UPC": "Ferguson distributor spec + Zoro distributor "
            "spec agree — both UPC sources are distributor specs; "
            "no core retailer printed the UPC (batch-6 verification "
            "2026-11-20).",
        },
        status="verified",
        notes="Google smart display (2021 hardware, 5 years old), "
        "frequently discounted to $49.99–$59.99; $99.99 is list. "
        "Best Buy $99.99 list; Google Store $99.99. Not "
        "discontinued, but age noted. (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="asus-zenwifi-bt8-2-pack-white",
        brand="ASUS",
        model="ZenWiFi BT8",
        variant="White, 2-pack (BT8(W-2-PK))",
        category="routers",
        identifiers={"UPC": "197105532045", "MPN": "BT8(W-2-PK)"},
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec (SKU 800656) "
            "agree (batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Current Wi-Fi 7 mesh system. B&H $449.99 InStock, "
        "Holiday Savings $130 off (was $579.99) — retailer-direct "
        "row. Micro Center $599.99 InStoreOnly (not the row); ASUS "
        "2-pack list $599.99. Flag: promo price — re-verify at add "
        "time. 1-pack (UPC 197105531987, B&H $329.99, OutOfStock) "
        "and 3-pack (UPC 197105532090, B&H $699.99) are different "
        "pack sizes — pin 2-pack only. Distinct from the in-batch "
        "ZenWiFi AXE7800 3-pack. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="asus-zenwifi-bt10-2-pack-white",
        brand="ASUS",
        model="ZenWiFi BT10",
        variant="White, 2-pack (BT10(W-2-PK))",
        category="routers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 197105429895 (B&H spec page "
            "+ CompSource distributor spec; DOWNGRADED at add time "
            "2026-11-20: the Best Buy spec panel for SKU 11870821 "
            "as fetched shows no UPC field at all, so the "
            "confirm-or-downgrade check did not confirm it; the "
            "$760.69 Best Buy listing is marketplace, Beach Audio "
            "Inc, not Best Buy direct).",
        },
        status="pending",
        notes="MPN BT10(W-2-PK) confirmed (B&H spec page MFR # + "
        "Best Buy model field, SKU 11870821, agree). Premium "
        "current Wi-Fi 7 mesh. B&H $629.99 (row). Best Buy $760.69 "
        "is sold & shipped by Beach Audio Inc (marketplace) — do "
        "not use as the row. Do NOT use the 3-pack: Best Buy "
        "3-pack (SKU 6578611) is Clearance $849.99 and 'no longer "
        "available in new condition'. 1-pack (B&H UPC 197105429833, "
        "$346.00 InStock) is a different pack size. Distinct from "
        "BT8 (BE14000 vs BE18000). (batch-6 verification "
        "2026-11-20).",
    ),
    EvalProduct(
        key="hyperx-cloud-iii-wireless-black",
        brand="HyperX",
        model="Cloud III Wireless",
        variant="Black (77Z45AA)",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 197029611727 has no "
            "qualifying source at all yet (shipfreedefense, "
            "shop.vb.net, PB Tech NZ, Desertcart print it; eBay "
            "prints a conflicting UPC 786513757593 — ignore, likely "
            "a different bundle).",
        },
        status="pending",
        notes="MPN 77Z45AA confirmed (Best Buy model field + "
        "HyperX.com press release 'Part Number 77Z45AA Black' "
        "agree). HyperX US shop: 'Discontinued! Shop HyperX Cloud "
        "III S Wireless Headset Instead', $149.99, OutOfStock — "
        "Best Buy may be the only live row. Best Buy $149.99 (one "
        "crawl $174.49 — price varies); price/stock not re-verified "
        "this round. Distinct from in-catalog Cloud III S "
        "Wireless. (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="hyperx-alloy-origins-60-black",
        brand="HyperX",
        model="Alloy Origins 60",
        variant="Black (4P5N4AA#ABA)",
        category="keyboards",
        identifiers={"UPC": "196188048948", "MPN": "4P5N4AA#ABA"},
        identifier_sources={
            "UPC": "Newegg spec page + HP datasheet (via Icecat "
            "hosting) 'HyperX Alloy Origins 60 (4P5N4AA), UPC "
            "196188048948' agree (batch-6 verification 2026-11-20).",
        },
        status="verified",
        notes="Current HyperX 60% gaming keyboard. HP.com $114.99 "
        "InStock; Best Buy $77.99–$86.99 (comp $114.99); Newegg "
        "$69.99–$114.99 (sold by Official HP Store). Flag: "
        "promo-sensitive price — re-check at add time. HP datasheet "
        "also lists 196188048955 / 5704174946502 for other variants "
        "— do not mix. Distinct from in-catalog Alloy Origins 65. "
        "(batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="corsair-k65-pro-mini-black",
        brand="Corsair",
        model="K65 PRO MINI",
        variant="Black, OPX (CH-91A401A-NA)",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840006698432 has no "
            "qualifying source yet (aio.lv prints 'MPN "
            "CH-91A401A-NA, EAN 840006698432'; camelcamelcamel / "
            "Desertcart agree — none qualifying).",
        },
        status="pending",
        notes="MPN CH-91A401A-NA confirmed (Best Buy model field + "
        "Newegg Part Number agree). Correct US code is "
        "CH-91A401A-NA (NA layout) — the guessed code CH-9199114 "
        "was wrong, do NOT use it. CH-91A401A-ND is the Nordics "
        "layout, a different variant. Best Buy $72.98 promo / "
        "$149.99 list; Newegg $109.99+; Corsair direct $79.99. Pin "
        "$79.99 (Corsair direct / Best Buy promo). Distinct from "
        "in-catalog K65 Plus Wireless (wired optical OPX vs "
        "wireless). (batch-6 verification 2026-11-20).",
    ),
    EvalProduct(
        key="asus-tuf-gaming-m4-air-black",
        brand="ASUS",
        model="TUF Gaming M4 Air",
        variant="Black (P307 TUF GAMING M4 AIR)",
        category="mice",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 195553335454 (SHI + Zoro "
            "distributor specs agree; DOWNGRADED at add time "
            "2026-11-20, user-approved: both sources are "
            "distributors, the same shape as the Venu 3S UPC that "
            "stays pending).",
        },
        status="pending",
        notes="MPN P307 TUF GAMING M4 AIR confirmed (SHI distributor "
        "spec + Zoro spec + Best Buy model field agree). Current "
        "ultralight TUF mouse (47g, 16,000 DPI). Best Buy $57.99 "
        "InStock at add-time re-check 2026-11-20 — but the featured "
        "seller is 'Sold & shipped by Newegg Official' "
        "(marketplace), not Best Buy direct, and the live SKU is "
        "12228723, not the draft's 11145905; no Best Buy-direct "
        "row. ASUS US $49.99. Price moves ($44.99–$57.99). A Target "
        "marketplace listing "
        "shows UPC 196384006247 for the same model name "
        "(marketplace-sourced, not qualifying) — do not treat as a "
        "competing verified code. No TUF mouse is in the catalog. "
        "(batch-6 verification 2026-11-20).",
    ),
    # --- Batch 7 (2026-11-21, deal-site gap-check, user-approved) ---
    EvalProduct(
        key="shokz-openfit-2-se-black",
        brand="Shokz",
        model="OpenFit 2 SE",
        variant="Black (Costco exclusive)",
        category="earbuds",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN T920-ST-CB-US-326-COS single-source (Costco only). UPC no lead. Costco.com "
        "OutOfStock at add-time re-check 2026-11-21; $109.99 is warehouse-only (Holiday Savings "
        "thru 11/30) — no online row. Weakest entry in batch 7; carried as pending only. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="shokz-openrun-air-2-black",
        brand="Shokz",
        model="OpenRun Air 2",
        variant="Black Standard",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — 810202689213 printed by non-US retailers (PBTech NZ, MobileCiti AU) but "
            "NOT on the Best Buy spec panel (SKU 6680820); downgraded from VERIFIED-caveat at add "
            "time 2026-11-21.",
        },
        status="pending",
        notes="MPN S610-ST-BK-US confirmed (B&H MFR # + Best Buy model field, SKU 6680820). B&H $99.95 "
        "/ Best Buy $99.99 InStock at add time. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="shokz-opendots-air-black",
        brand="Shokz",
        model="OpenDots Air",
        variant="Black",
        category="earbuds",
        identifiers={
            "UPC": "810202687417",
            "MPN": "E210-ST-BK-US",
        },
        identifier_sources={
            "UPC": "Target spec page (TCIN 95002590) + NFM spec page agree (batch-7 verification "
            "2026-11-21).",
        },
        status="verified",
        notes="Clip-on open-ear earbuds. Best Buy $89.99 InStock; Sam's Club $89 thru 11/30 (Black & "
        "Purple; $15 Sam's Cash is a rebate, not a price cut). (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="shokz-openrun-gray-standard",
        brand="Shokz",
        model="OpenRun",
        variant="Gray Standard",
        category="headphones",
        identifiers={
            "UPC": "850033806229",
            "MPN": "S803-ST-GY-US",
        },
        identifier_sources={
            "UPC": "Abt UPC # + RunUnited UPC agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="Bone-conduction endurance headphones. Shokz.com $64.95 with code SDopenrun "
        "(grey/standard only; shelf $77.95) — row must carry the code. Best Buy row dead. "
        "(batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="sonos-era-100-black",
        brand="Sonos",
        model="Era 100",
        variant="Black",
        category="speakers",
        identifiers={
            "UPC": "840136805830",
            "MPN": "E10G1US1BLK",
        },
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec page agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="Single unit. B&H $179.00 live at add time (corrected from draft $219.00); Micro Center "
        "$219.00. Costco $329.99 is the 2-pack — do not attach as a single-unit price. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="sonos-arc-ultra-black",
        brand="Sonos",
        model="Arc Ultra",
        variant="Black",
        category="soundbars",
        identifiers={
            "UPC": "840136811336",
            "MPN": "ARCG2US1BLK",
        },
        identifier_sources={
            "UPC": "Micro Center + NFM + Adorama + Walts agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="Best Buy $849.00 Black Friday InStock. Costco $849.99 row HELD at add time: Costco.com "
        "OutOfStock and Costco model field is bundle code ARCG2US1BKHB, not ARCG2US1BLK. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="marshall-monitor-iii-anc-cream",
        brand="Marshall",
        model="Monitor III ANC",
        variant="Cream",
        category="headphones",
        identifiers={
            "EAN": "7340055411479",
            "MPN": "1009077",
        },
        identifier_sources={
            "EAN": "B&H spec page prints EAN + Aqipa distributor PDF agree; EAN not a 12-digit US UPC — "
            "counts per the Keychron EAN+SKU precedent (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="Cream variant. Best Buy $199.99 Black Friday InStock; B&H $199.99. B&H spec table "
        "mislabels color as Black — title, variant selector and MPN all say Cream. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="skullcandy-crusher-evo-matte-black",
        brand="Skullcandy",
        model="Crusher Evo",
        variant="Matte Black",
        category="headphones",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN S6EVW-S978 single-source (Best Buy model field only). UPC 810145320815 pending (eBay "
        "+ layupshop only, non-qualifying). Best Buy $89.99 Black Friday InStock (SKU 6580350). "
        "(batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="turtle-beach-stealth-pro-ii-xbox-black",
        brand="Turtle Beach",
        model="Stealth Pro II",
        variant="Xbox Black",
        category="headphones",
        identifiers={
            "UPC": "840454400755",
            "MPN": "TBS-2104-05",
        },
        identifier_sources={
            "UPC": "GameStop US spec page + CLD Distribution agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="Xbox/PS5/PC multiplatform Black. Best Buy $249.99 Black Friday InStock (SKU 6672065). Do "
        "not mix with PS/PC-only TBS-5105-05 or White TBS-2104-15. (batch-7 verification "
        "2026-11-21).",
    ),
    EvalProduct(
        key="technics-eah-az100-black",
        brand="Technics",
        model="EAH-AZ100",
        variant="Black",
        category="earbuds",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN EAH-AZ100-K confirmed (B&H + Crutchfield MFR #). UPC CONFLICT unresolved: B&H prints "
        "885170433021, Amazon/eBay/Snapklik print 885170441613 — do not attach either. "
        "us.technics.com $149.99 InStock (brand direct). B&H $149.99 Temporarily Out of Stock, "
        "restock ~Nov 30. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="sennheiser-momentum-true-wireless-4-black-graphite",
        brand="Sennheiser",
        model="MOMENTUM True Wireless 4",
        variant="Black Graphite",
        category="earbuds",
        identifiers={
            "UPC": "810091272466",
            "MPN": "700365",
        },
        identifier_sources={
            "UPC": "B&H spec page + Abt + Sennheiser official spec-sheet PDF agree (batch-7 verification "
            "2026-11-21).",
        },
        status="verified",
        notes="Black Graphite. Best Buy SKU 10904810 $249.95 HELD at add time: sold & shipped by Video "
        "& Audio Center (marketplace). Alternate Best Buy SKU 6575080 $299.99 Sold by Best Buy, "
        "InStock — Add to Cart unconfirmed in text fetch, needs live browser check. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="anker-soundcore-space-2-pro-jet-black",
        brand="Anker",
        model="Soundcore Space 2 Pro",
        variant="Jet Black",
        category="headphones",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN D1406Z11 single-source (Best Buy model field only). UPC no lead; do not attach "
        "Target UPCs 194644380014/194644379674 (Space 2 non-Pro bundles) or 'A3068' (wrong). Best "
        "Buy $169.99 live (corrected from draft $199.99); Target $169.99 sold by Anker; "
        "soundcore.com $169.99 Black Friday thru 11/30. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="beats-solo-buds-orange",
        brand="Beats",
        model="Solo Buds",
        variant="Orange",
        category="earbuds",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN MJKQ4LL/A single-source (Best Buy model field only). UPC no lead; do not attach "
        "Matte Black MUVW3LL/A. Best Buy $49.99 Black Friday InStock (SKU 6677082). Best "
        "Buy-exclusive Orange. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="beats-studio-buds-plus-ivory",
        brand="Beats",
        model="Studio Buds+",
        variant="Ivory",
        category="earbuds",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN MQLJ3LL/A confirmed (Best Buy model field + Apple.com + Adorama). UPC no lead. Best "
        "Buy $89.99 Black Friday InStock (SKU 6501046); Apple.com $169.99. (batch-7 verification "
        "2026-11-21).",
    ),
    EvalProduct(
        key="google-pixel-10a-128gb-obsidian",
        brand="Google",
        model="Pixel 10a",
        variant="Obsidian 128GB",
        category="phones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840353949768 (Best Buy mirror spec table only, non-qualifying). Do "
            "not use EAN 840353949737 (UK variant GA09561-GB).",
        },
        status="pending",
        notes="MPN GA09561-US single-source (Best Buy model field, SKU 6668565). Best Buy $549.00 Black "
        "Friday InStock, Sold by Best Buy. $499.99 SKU 13239207 is marketplace (YY Wireless) — "
        "excluded. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="motorola-moto-g-stylus-2025-256gb-gibraltar-sea",
        brand="Motorola",
        model="moto g stylus 2025",
        variant="PANTONE Gibraltar Sea 256GB",
        category="phones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840023282829 (LakeshoreIT distributor spec only; conflicting eBay UPC "
            "609921770100 for XT2517-1 disregarded).",
        },
        status="pending",
        notes="MPN PB6V0014US confirmed (Best Buy model field + SHI distributor + Newegg). Best Buy "
        "$199.99 Black Friday InStock (SKU 6617940); motorola.com $199.99. (batch-7 verification "
        "2026-11-21).",
    ),
    EvalProduct(
        key="motorola-moto-g-power-2025-128gb-leaf-green",
        brand="Motorola",
        model="moto g power 2025",
        variant="Leaf Green 128GB",
        category="phones",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN PB640007US single-source (Best Buy model field only); motorola.com uses PB640006US "
        "for Slate Gray — not a second source for Leaf Green. UPC conflict: 840023277283 "
        "(Amazon/Snapklik) ties to PB640003US — do not attach. Best Buy $199.99 Black Friday "
        "InStock (SKU 6611546). $99.99 is a carrier-activation price — excluded. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="motorola-edge-2026-128gb-martini-olive",
        brand="Motorola",
        model="edge 2026",
        variant="PANTONE Martini Olive 128GB",
        category="phones",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN PBC70002US confirmed (Best Buy model field + motorola.com + Lenovo.com). UPC no "
        "lead. Best Buy $399.99 Black Friday InStock (SKU 6677356); motorola.com $399.99. SKU "
        "12901739 $707.17 is marketplace — excluded. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="apple-iphone-17-pro-256gb-silver",
        brand="Apple",
        model="iPhone 17 Pro",
        variant="Silver 256GB",
        category="phones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 195950626162 (BarcodesInc + shopabunda + Venezuelan retailer lists; "
            "no core retailer spec page).",
        },
        status="pending",
        notes="MPN MG7K4LL/A confirmed (Best Buy model field + Abt + CDW). Best Buy $999.99 Black "
        "Friday InStock (SKU 6418044). $30.55/mo installment + $500 gift card and $899.99 "
        "carrier-activation prices excluded; refurbished excluded. MG7L4LL/A is not Silver. "
        "(batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="apple-airtag-2nd-gen-4-pack-white",
        brand="Apple",
        model="AirTag 2nd Gen 4-Pack",
        variant="White",
        category="accessories",
        identifiers={
            "UPC": "195950667455",
            "MPN": "MFEA4LL/A",
        },
        identifier_sources={
            "UPC": "B&H spec page + Datavision reseller listing agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="2nd-gen 4-pack. B&H $95.99 In Stock (clean row). Walmart $79.99 live-corrected from "
        "draft $69.99 (crawl price; live page bot-walled at add time). Apple.com $99.00. Do not "
        "mix with 1st-gen 4-pack MX542AM/A. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="hisense-m7sr-75",
        brand="Hisense",
        model="M7 75",
        variant="75M7SR Roku",
        category="tvs",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 75M7SR single-source (Best Buy model field, SKU 6686979); Hisense support answers on "
        "Best Buy Q&A name it but same page — not a second source. UPC no lead; do not attach "
        "Canadian 75M7SG UPC 888143026817. Best Buy $499.99 Black Friday InStock. Native 60Hz "
        "(not 144Hz). (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-u7900h-75",
        brand="Samsung",
        model="U7900H 75",
        variant="UN75U7900HFXZA",
        category="tvs",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 198957409578 (P&C Richard spec-sheet PDF only). Do not confuse with "
            "U7900F UPCs (887276951904 / 887276951997).",
        },
        status="pending",
        notes="MPN UN75U7900HFXZA confirmed (samsung.com + Best Buy model field, SKU 6688397). Best Buy "
        "$399.99 Black Friday InStock; Costco $399.99; Abt $397.99. (batch-7 verification "
        "2026-11-21).",
    ),
    EvalProduct(
        key="samsung-s84h-65",
        brand="Samsung",
        model="S84H 65",
        variant="QN65S84HAEXZA",
        category="tvs",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN QN65S84HAEXZA verified with caveat (Best Buy model field + Samsung Parts USA "
        "compatibility list — parts page, not a product spec page; strict product-page reading "
        "would leave it PENDING + strong lead). UPC no lead. Best Buy $899.99 Black Friday "
        "InStock (SKU 6689681), 'Only at Best Buy'. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="tcl-q6ch-black",
        brand="TCL",
        model="Q6CH",
        variant="Black",
        category="soundbars",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN Q6CH confirmed (Costco.com model field + TCL US support Q Series manuals). UPC no "
        "lead (Costco.com spec table has no UPC field). NO online row at add time: Costco.com "
        "OutOfStock at $299.99; $199.99 is warehouse-only (Holiday Savings thru 11/30) and "
        "unverifiable online. Model in as pending; row held. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-hw-b650f-black",
        brand="Samsung",
        model="HW-B650F",
        variant="Black",
        category="soundbars",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN HW-B650F/ZA confirmed (Best Buy model field + Samsung user guide + Samsung Canada "
        "list; /ZA suffix pinned by Best Buy only). UPC conflict: 887276936956 / 887276864211 / "
        "Canadian 887276950938 — do not attach any. Best Buy $199.99 Black Friday InStock (SKU "
        "6619391). Distinct from 2023 HW-B650. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-music-studio-5-black",
        brand="Samsung",
        model="Music Studio 5",
        variant="Black HW-LS50H/ZA",
        category="speakers",
        identifiers={
            "UPC": "198957266393",
            "MPN": "HW-LS50H/ZA",
        },
        identifier_sources={
            "UPC": "Walts TV spec page + Precision distributor agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="Best Buy $299.99 Black Friday InStock (SKU 6670424). Woot $214.99 is NOT a qualifying "
        "row (Amazon subsidiary, 90-day warranty, title/box mismatch). Marketplace SKU 12696700 "
        "excluded. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="harman-kardon-onyx-studio-8-black",
        brand="Harman Kardon",
        model="Onyx Studio 8",
        variant="Black",
        category="speakers",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN HKOS8BLKAM confirmed (harmankardon.com Item # + Best Buy model field). UPC conflict: "
        "028292289859 / 028292289873 (Blue) / 657768329135 / 094148666167 — do not attach any. "
        "harmankardon.com $99.99 InStock (brand direct, list $499.95). Best Buy $99.99 row is JBL "
        "Store marketplace — excluded. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="dji-osmo-action-4-essential-combo-black",
        brand="DJI",
        model="Osmo Action 4 Essential Combo",
        variant="Black",
        category="action-cameras",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 190021133402 (Sharaf DG UAE only, non-qualifying). Do not attach "
            "Standard Combo MPN CP.OS.00000269.01.",
        },
        status="pending",
        notes="MPN no qualifying lead. NO row at add time: DJI US $169.00 but 'Sold out' on the live "
        "collection page. Best Buy listing is marketplace (Focus Camera) — excluded. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="gopro-lit-hero-4k60-black",
        brand="GoPro",
        model="LIT Hero",
        variant="Black",
        category="action-cameras",
        identifiers={
            "UPC": "810116384129",
            "MPN": "CHDHF-132-AT",
        },
        identifier_sources={
            "UPC": "B&H spec page + GoPro LIT HERO sell-sheet PDF agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="B&H $199.00 live (corrected from draft $269.99; Holiday Savings $70.99, limited supply); "
        "Best Buy $269.99 InStock (SKU 6642404). Do not attach bundle UPC 197684015847 or NZ "
        "variant CHDHF-132-AS. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="dji-osmo-action-6-essential-combo-black",
        brand="DJI",
        model="Osmo Action 6 Essential Combo",
        variant="Black",
        category="action-cameras",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 190021161696 (Amazon + TradeKorea + Ubuy agree, all non-qualifying). "
            "Do not attach 190021997370 / 190021998407 (bundle kits).",
        },
        status="pending",
        notes="MPN no qualifying lead (eBay UK 'CPOS0000037701' unconfirmed, does not fit the "
        "sequence). DJI US $426.00, in-stock signal via collection page (no 'Sold out' tag, "
        "unlike Action 4/5 Pro). (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="dji-osmo-pocket-3-creator-combo-black",
        brand="DJI",
        model="Osmo Pocket 3 Creator Combo",
        variant="Black",
        category="cameras",
        identifiers={
            "UPC": "190021095007",
            "MPN": "CP.OS.00000302.01",
        },
        identifier_sources={
            "UPC": "Micro Center spec panel + Target UPC field + Nelson Photo agree (batch-7 verification "
            "2026-11-21).",
        },
        status="verified",
        notes="Creator Combo. B&H $466.00 In Stock (was $549.00). Do not attach component UPCs "
        "(190021094970 etc.) — kit UPC is 190021095007 only. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="insta360-ace-pro-2-xplorer-bundle-costco-black",
        brand="Insta360",
        model="Ace Pro 2 Xplorer Bundle",
        variant="Black (Costco)",
        category="action-cameras",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — weak lead 6977644766460 (13-digit EAN; Newegg third-party-seller bundle "
            "only). Do not attach base-camera MPN CINSBBGA.",
        },
        status="pending",
        notes="MPN no lead (Costco item 9536006 is a Costco number, not a manufacturer MPN). NO row at "
        "add time: Costco OutOfStock; live JSON-LD $309.99 OOS vs $389.99 8 days ago — neither "
        "usable. Distinct from Best Buy Octa Edition (ACEPRO2140) and Target Xplorer Pro Bundle. "
        "(batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-yoga-7i-2-in-1-16-gen-10-luna-grey",
        brand="Lenovo",
        model="Yoga 7i 2-in-1 16",
        variant="Luna Grey 83JT0000US",
        category="laptops",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 198155420948 (Slickdeals thread + eBay only, non-qualifying; Best Buy "
            "spec panel does not print it).",
        },
        status="pending",
        notes="MPN 83JT0000US confirmed (lenovo.com + Best Buy model field + Newegg). Best Buy $649.99 "
        "Doorbuster InStock (SKU 6615769). Twin-config trap: 83TE0004US ($1,649.99 list) is a "
        "different generation — do not mix. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-legion-5a-15-3-eclipse-black",
        brand="Lenovo",
        model="Legion 5a",
        variant="Eclipse Black 83Q70068US",
        category="laptops",
        identifiers={
            "UPC": "199276132093",
            "MPN": "83Q70068US",
        },
        identifier_sources={
            "UPC": "B&H spec page + Target UPC field + MyNavyExchange agree (batch-7 verification "
            "2026-11-21).",
        },
        status="verified",
        notes="B&H $1,249.99 In Stock (was $1,799.99; limited supply at this price). Do not mix with "
        "sibling 83Q70003US (1TB). (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-zenbook-a14-ux3407qa-ps76-iceland-gray",
        brand="ASUS",
        model="Zenbook A14",
        variant="Iceland Gray UX3407QA-PS76",
        category="laptops",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 197105832077 (laptoparena.net only, non-qualifying).",
        },
        status="pending",
        notes="MPN UX3407QA-PS76 confirmed (ASUS press release + ASUS Store + Best Buy model field). "
        "Best Buy $1,199.99 (latest crawl; a 3-day-old crawl showed $1,599.99 — price conflict "
        "flagged, re-verify before writing the row). Do not mix with Beige sibling "
        "UX3407QA-X1P512. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="hp-omnibook-3-14-hz0788dx-nouvelle-silver",
        brand="HP",
        model="OmniBook 3 14",
        variant="Nouvelle Silver 14-hz0788dx",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 14-hz0788dx / DM2Z9UA#ABA verified with caveat (Best Buy model field + HP datasheet "
        "PDF hosted on Best Buy static files.bbystatic.com — hp.com has no page for this config, "
        "so the caveat stands). UPC no lead. Best Buy $599.99 Black Friday InStock (SKU 6679357). "
        "(batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="msi-mag-321up-qd-oled-black",
        brand="MSI",
        model="MAG 321UP",
        variant="Black 165Hz",
        category="monitors",
        identifiers={
            "UPC": "824142363720",
            "MPN": "MAG321UPQDOLED",
        },
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="165Hz original. B&H $569.99 In Stock (was $699.99). Do not mix with X24 240Hz "
        "(MAG321UPQDOLEDX24). First MSI model in the catalog. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="logitech-g-yeti-gx-black",
        brand="Logitech",
        model="G Yeti GX",
        variant="Black",
        category="microphones",
        identifiers={
            "UPC": "097855190994",
            "MPN": "988-000567",
        },
        identifier_sources={
            "UPC": "B&H spec page + CompSource + Logitech package-spec datasheet agree (batch-7 verification "
            "2026-11-21).",
        },
        status="verified",
        notes="Black. Best Buy $89.99 Black Friday InStock (SKU 6556755); B&H $89.99 (was $169.99). Do "
        "not use 988-000570 (does not exist); White is 988-000574. (batch-7 verification "
        "2026-11-21).",
    ),
    EvalProduct(
        key="amazon-echo-show-8-2025-glacier-white",
        brand="Amazon",
        model="Echo Show 8 (2025)",
        variant="Glacier White",
        category="smart-home",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 840414682108 (camelcamelcamel + eBay + wholesale post, all "
            "non-qualifying). Do not use Graphite UPC 840414684003 (B0DC8ZMR1P).",
        },
        status="pending",
        notes="MPN B0DC93K4NW confirmed (Best Buy model field + Staples + Abt + Dell). Best Buy $129.99 "
        "Black Friday InStock (SKU 6642846; draft $99.99 was wrong); Abt $129.99. Smart-home "
        "category flag (carried per approval; Nest Hub precedent). Distinct from batch-3 3rd-gen "
        "(8 in HD). (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="amazon-echo-hub-white",
        brand="Amazon",
        model="Echo Hub",
        variant="White",
        category="smart-home",
        identifiers={},
        identifier_sources={"UPC": "UPC pending — lead 840268960544 (B&H spec page only)."},
        status="pending",
        notes="MPN B0BCR7M9KX confirmed (Best Buy model field + B&H slug). Best Buy $74.99 Black Friday "
        "InStock (SKU 6562248); B&H $109.99. Smart-home category flag (carried per approval). "
        "Walmart clearance $45 (Aug 2026) is chatter, not a row. (batch-7 verification "
        "2026-11-21).",
    ),
    EvalProduct(
        key="sony-ult-tower-10-black",
        brand="Sony",
        model="ULT Tower 10",
        variant="Black",
        category="speakers",
        identifiers={},
        identifier_sources={"UPC": "UPC pending — lead 027242928978 (Adorama spec page only)."},
        status="pending",
        notes="MPN SRSULT1000 confirmed (B&H + Crutchfield + Best Buy model field). Best Buy $799.99 "
        "InStock (SKU 6577679). B&H discontinued — Best Buy is the row. (batch-7 verification "
        "2026-11-21).",
    ),
    EvalProduct(
        key="asus-rog-strix-g16-g614pr-rtx-5070-ti-eclipse-gray",
        brand="ASUS",
        model="ROG Strix G16",
        variant="G614PR Eclipse Gray",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN G614PR-G16.R95070TI confirmed (Best Buy model field + ROG official spec page). UPC "
        "no lead; do not attach 197105821606 (regional config G614PR-RV003W). Best Buy $1,749.99 "
        "Black Friday InStock (SKU 6613956). (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-galaxy-watch7-40mm-green",
        brand="Samsung",
        model="Galaxy Watch7 40mm",
        variant="Green",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 887276868905 (Samsung MSRP price list only).",
        },
        status="pending",
        notes="MPN SM-L300NZGAXAA confirmed (Best Buy model field + Samsung MSRP price lists). Best Buy "
        "$149.99 live (corrected from draft $249.99 — Black Friday extended to Green). Cream "
        "sibling also $149.99. Prior generation (2024) but sold new, not clearance. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-thinkpad-e16-gen-3-black",
        brand="Lenovo",
        model="ThinkPad E16 Gen 3",
        variant="Black 21ST0008US",
        category="laptops",
        identifiers={
            "UPC": "198157339941",
            "MPN": "21ST0008US",
        },
        identifier_sources={
            "UPC": "B&H spec page + Lenovo official PSREF (Ingram Micro host) agree (batch-7 verification "
            "2026-11-21).",
        },
        status="verified",
        notes="B&H $1,217.50 In Stock; CDW $1,212.99 advertised. Best Buy listing is Merchant Expo "
        "marketplace — not usable. Pin Ryzen 7 250 / 512GB / Multi-Touch config only. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-rog-strix-xg27ucg-black",
        brand="ASUS",
        model="ROG Swift OLED XG27UCG",
        variant="Black",
        category="monitors",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 197105564633 (CompSource + Adorama agree; ASUS brochure leg not live "
            "re-opened at add time — downgraded from VERIFIED-caveat on strict leg-counting, "
            "2026-11-21).",
        },
        status="pending",
        notes="MPN XG27UCG confirmed (Micro Center + CompSource + Adorama). Best Buy row HELD at add "
        "time: main offer is Adorama marketplace ($464.99–$469.99). Alternate: ASUS eShop "
        "brand-direct $449.00 InStock (needs coordinator confirmation as price row); Adorama "
        "direct $469.99 backup; Micro Center $349.96 in-store only. Gen2 XG27UCGR superseding "
        "($399.00 at ROG US). Do not mix with XG27UCSR (UPC conflicted). (batch-7 verification "
        "2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-yoga-slim-7x-14-cosmic-blue",
        brand="Lenovo",
        model="Yoga Slim 7x",
        variant="Cosmic Blue 83QR000AUS",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 83QR000AUS single-source (Best Buy model field only). UPC no lead. Best Buy "
        "$1,299.99 live (corrected from draft $649.99 — Holiday Deal ended); Sold by Best Buy, "
        "InStock. Do not mix with 2024 X Elite version (83ED0001US etc.) or 1TB config "
        "83QR0002US. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-thinkpad-t14-gen-6-black",
        brand="Lenovo",
        model="ThinkPad T14 Gen 6",
        variant="Black 21QJ00CSUS",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN 21QJ00CSUS confirmed (CDW spec page + Best Buy model field). UPC no lead; do not "
        "attach B&H 199272842804 (belongs to config 21QDS2VV00). NO row at add time: CDW live "
        "page unopenable and crawls conflict ($1,811.99 vs $1,799.00/$1,594.99) — held. Best Buy "
        "new listings are marketplace / refurbished. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="dji-osmo-360-standard-combo-black",
        brand="DJI",
        model="Osmo 360 Standard Combo",
        variant="Black",
        category="action-cameras",
        identifiers={
            "UPC": "190021135994",
            "MPN": "CP.OS.00000441.02",
        },
        identifier_sources={
            "UPC": "B&H spec page + DroneNerds spec table agree (batch-7 verification 2026-11-21).",
            "MPN": "Abt page body + Abt blog + B&H slug + DroneNerds agree on .02; Best Buy model field "
            "prints .01 and one tracker printed .04 — suffix conflict adjudicated by weight of "
            "evidence, caveat recorded (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="Standard Combo. B&H $417.99 / Abt $417.99 In Stock (draft $404.77 was the Nov 16 price — "
        "stale, not adopted; B&H $404.77 snippet not trusted — page slug says adventure_combo). "
        "Do not mix with Adventure/Essential/Skiing combos. (batch-7 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-smart-monitor-m70f-32-white",
        brand="Samsung",
        model="Smart Monitor M70F",
        variant="White 32\" LS32FM703UNXZA",
        category="monitors",
        identifiers={
            "UPC": "198957027796",
            "MPN": "LS32FM703UNXZA",
        },
        identifier_sources={
            "UPC": "B&H spec page + DataVision reseller listing agree (batch-7 verification 2026-11-21).",
            "MPN": "Abt page body + Best Buy page body ('Model: LS32FM703UNXZA', SKU 6632212) agree — caveat "
            "eliminated at add time (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="White 32 in. B&H $299.99 / Abt $299.99 / Samsung.com $299.99, all InStock. Best Buy 32 "
        "in row now exists at $399.99 (SKU 6632212, list). Do not mix with 43 in M70F "
        "(LS43FM702UNXZA), M70B, M70D; Woot $239.99 is reconditioned — excluded. (batch-7 "
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-ideapad-5-2-in-1-14-luna-grey",
        brand="Lenovo",
        model="IdeaPad 5 2-in-1 14",
        variant="Luna Grey 83GH000AUS",
        category="laptops",
        identifiers={
            "UPC": "198154657529",
            "MPN": "83GH000AUS",
        },
        identifier_sources={
            "UPC": "B&H spec page + SHI distributor agree (batch-7 verification 2026-11-21).",
        },
        status="verified",
        notes="Luna Grey. B&H $699.00 In Stock (was $999.00). MPN confirmed (B&H + Target + Newegg). "
        "'IdeaPad 5x' (Target/Staples) is the same part/config as 'IdeaPad 5 2-in-1' (B&H). Do "
        "not mix with 83GH0008US/0000US/0009US. (batch-7 verification 2026-11-21).",
    ),
    # --- Batch 8 (2026-11-21, user-approved draft; add-time re-verification) ---
    EvalProduct(
        key="shokz-opendots-2-black",
        brand="Shokz",
        model="OpenDots 2",
        variant="Black",
        category="earbuds",
        identifiers={
            "UPC": "810202687523",
            "MPN": "E320-ST-BK-US",
        },
        identifier_sources={
            "UPC": "B&H spec page + Abt product page agree (batch-8 verification 2026-11-21).",
            "MPN": "B&H URL slug + Abt product page agree.",
        },
        status="verified",
        notes="B&H $139.95 (was $199.95, Holiday Savings $60) In Stock at add time. Do not mix with OpenDots"
        "Air (E210). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="beats-solo-4-matte-black",
        brand="Beats",
        model="Solo 4",
        variant="Matte Black",
        category="headphones",
        identifiers={
            "UPC": "195949121708",
            "MPN": "MUW23LL/A",
        },
        identifier_sources={
            "UPC": "B&H spec page + Abt agree (batch-8 verification 2026-11-21).",
            "MPN": "Best Buy model field + B&H slug + Abt agree.",
        },
        status="verified",
        notes="Best Buy $99.99 (Black Friday Deal, was $199.99) InStock at add time. Amazon Exclusive Metallic"
        "Pink $80 is a different color, not a price source. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="skullcandy-crusher-anc-2-black-tan",
        brand="Skullcandy",
        model="Crusher ANC 2",
        variant="Black/Tan",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 810145320808 (eBay listings only); no brand/retailer spec-page second source"
            "at add time (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="MPN S6CAW-S978 confirmed (Best Buy model field, SKU 6580349). Best Buy $119.99 (Black Friday"
        "Deal, was $239.99) InStock at add time. Do not mix with Crusher Evo (batch 7). (batch-8"
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="nothing-headphone-1-pro-black",
        brand="Nothing",
        model="Headphone (1) Pro",
        variant="Black",
        category="headphones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC/EAN pending — lead 6974434229471 (Swiftronics CA + Kogan AU only, non-US); no US retailer"
            "spec-page second source at add time (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="MPN B192 confirmed (iFixit device page + Best Buy Canada + Nothing product page). US Best Buy"
        "model field prints A11300048 (SKU 6693512) — a separate US retailer model code, not mixed with"
        "B192. Live row Best Buy US $319.00 (Black Friday Deal, was $399.00) InStock at add time;"
        "Nothing US $399 is list price, not the row. Do not mix with 2025 Headphone (1) (B186). (batch-8"
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="amazon-echo-dot-max-graphite",
        brand="Amazon",
        model="Echo Dot Max",
        variant="Graphite",
        category="speakers",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — none written: 4 aggregator codes (840414628809 / 840414663176 / 840414694620 /"
            "84041466007) mutually exclusive, none from a US retailer spec page (batch-8 verification"
            "2026-11-21).",
        },
        status="pending",
        notes="MPN B0D6SX8VLQ confirmed (Best Buy model field, SKU 6642849). Best Buy $49.99 (Black Friday"
        "Deal, Save $70, comp $119.99) InStock at add time. Alexa+ needs Prime or $19.99/month"
        "subscription. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="harman-kardon-soundsticks-5-white",
        brand="Harman Kardon",
        model="SoundSticks 5",
        variant="White",
        category="speakers",
        identifiers={
            "UPC": "050036422468",
            "MPN": "HKSOUNDSTK5WAM2",
        },
        identifier_sources={
            "UPC": "B&H spec page + Amazon UPC + PicClick agree (batch-8 verification 2026-11-21).",
            "MPN": "B&H MFR # + Amazon Model Number agree.",
        },
        status="verified",
        notes="White/Clear only. B&H $279.95 (was $349.95) InStock at add time. Black version"
        "(HKSOUNDSTK5BAM2) has no US UPC and was not in stock at B&H; do not mix with SoundSticks 5"
        "Wi-Fi version. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="harman-kardon-onyx-studio-9-black",
        brand="Harman Kardon",
        model="Onyx Studio 9",
        variant="Black",
        category="speakers",
        identifiers={
            "UPC": "028292291104",
            "MPN": "HKOS9BLKAM",
        },
        identifier_sources={
            "UPC": "Amazon UPC + Newegg + NeweggBusiness agree; eBay 610214681881 / 724129192612 excluded as"
            "eBay-generated/refurb codes (batch-8 verification 2026-11-21).",
            "MPN": "Harman Kardon US Item# + Amazon + Newegg agree.",
        },
        status="verified",
        notes="Newegg $219.50 row HELD at add time: Sold by Global Mobiles Inc marketplace + Used - Like New"
        "listing. No valid self-operated in-stock row at add time; Harman Kardon US $299.95 OutOfStock."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="garmin-venu-x1-black",
        brand="Garmin",
        model="Venu X1",
        variant="Black / Slate Titanium",
        category="wearables",
        identifiers={
            "UPC": "753759342746",
            "MPN": "010-02980-00",
        },
        identifier_sources={
            "UPC": "Micro Center spec table + CompSource UPC EAN + Petra UPC + Garmin announcement PDF agree"
            "(batch-8 verification 2026-11-21).",
            "MPN": "Best Buy model field + Micro Center Mfr Part# + CompSource agree.",
        },
        status="verified",
        notes="Best Buy $499.99 (comp $699.99) InStock at add time. Size per Garmin official: 46mm case /"
        "2-inch screen (51mm is the screen diagonal, not the case); key carries no size. Moss"
        "(010-02980-01) is a different colorway. Do not take the $509.99 SKU (10891072, 2-year warranty"
        "bundle). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="oura-ring-5-size-8-silver",
        brand="Oura",
        model="Ring 5",
        variant="Silver, Size 8",
        category="wearables",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — no lead: only 13-digit EAN 6430060156975 (Harvey Norman AU, non-US); Best Buy"
            "spec text has no UPC field (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="MPN JZ90-61403-08 confirmed (Best Buy model field + Slickdeals thread). Best Buy $299.00 (comp"
        "$399.00) InStock at add time. Membership: first month free, then $5.99/month or $69.99/year —"
        "first-year price excludes later membership. Size 8 is the anchored size (sizing kit required)."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="whoop-5-0-peak-obsidian",
        brand="WHOOP",
        model="5.0 Peak",
        variant="Obsidian",
        category="wearables",
        identifiers={
            "UPC": "810114363317",
            "MPN": "973-004-000",
        },
        identifier_sources={
            "UPC": "Amazon product page (ASIN B0DY2SWV16) pairs Model 973-004-000 with UPC 810114363317 +"
            "manuals.plus spec table + eBay GTIN agree; conflicting lead 810114363270 has zero support"
            "(batch-8 verification 2026-11-21, upgraded at add time).",
            "MPN": "Best Buy model field + Amazon Model Number agree.",
        },
        status="verified",
        notes="Best Buy $199.00 (Black Friday Deal, comp $239.00) InStock at add time. Price is a 12-month"
        "Peak membership bundle (device included); renewal $239/year. Do not mix with One ($189) or"
        "MG/Life ($299, ECG). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="amazon-echo-time-graphite",
        brand="Amazon",
        model="Echo Time",
        variant="Graphite",
        category="smart-home",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — aggregator-only: matteralpha + bestpricescanner agree on 840414694712 but neither"
            "is a brand/retailer spec page; 840414627574 belongs to the White model (B0GFY8SZTK) (batch-8"
            "verification 2026-11-21).",
        },
        status="pending",
        notes="MPN B0FRPDXJYC confirmed (Best Buy model field; White B0GFY8SZTK, Coral Pink B0GG1YNSPD are"
        "separate codes). Live row Best Buy $99.99 (Black Friday Deal, Save $100, comp $199.99) InStock"
        "at add time — draft $199.99 list price superseded; price fell intraday $149.99 to $99.99."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="apple-watch-ultra-3-49mm-black-ocean-band",
        brand="Apple",
        model="Watch Ultra 3",
        variant="Black Titanium + Black Ocean Band",
        category="wearables",
        identifiers={
            "UPC": "195950484311",
            "MPN": "MF0J4LW/A",
        },
        identifier_sources={
            "UPC": "Best Buy spec page ('See all specifications' > Other) prints UPC 195950484311, agreeing with"
            " the draft lead (eBay GTIN + PayMore scans + box photos) (batch-8 verification 2026-11-21).",
            "MPN": "Best Buy model field, SKU 6572972 (batch-8 verification 2026-11-21).",
        },
        status="verified",
        notes="MPN MF0J4LW/A confirmed (Best Buy model field, SKU 6572972). Best Buy $549.00 (was $799.00)"
        "InStock at add time. Refurb/open-box rows excluded; Costco $449.97 is in-store-only, not a row."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="apple-iphone-17-pro-max-256gb-cosmic-orange",
        brand="Apple",
        model="iPhone 17 Pro Max 256GB",
        variant="Cosmic Orange",
        category="phones",
        identifiers={
            "UPC": "195950638004",
            "MPN": "MFXH4LL/A",
        },
        identifier_sources={
            "UPC": "Best Buy spec page ('See all specifications' > Other) prints UPC 195950638004, agreeing with"
            " the draft lead (PayMore scans + BarcodesInc GTIN 0195950638004 + eBay + tekfeed)"
            " (batch-8 verification 2026-11-21).",
            "MPN": "Best Buy model field, SKU 6473213 (batch-8 verification 2026-11-21).",
        },
        status="verified",
        notes="MPN MFXH4LL/A confirmed (Best Buy model field, SKU 6473213). Best Buy $1,099.99 (was $1,199.99)"
        "InStock at add time — connect-later unlocked price; $999.99 is the carrier-activated price, not"
        "written. Open-box $1,011.99–$1,044.99 and refurb $972.97+ excluded. Cosmic Orange only."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-galaxy-z-flip8-256gb-graphite",
        brand="Samsung",
        model="Galaxy Z Flip8 256GB",
        variant="Graphite",
        category="phones",
        identifiers={
            "UPC": "0198957311260",
            "MPN": "SM-F776UZKAXAA",
        },
        identifier_sources={
            "UPC": "shop.databitinc.com + ProvarTech distributor spec pairing (SM-F776UZKAXAA … 0198957311260)"
            "agree (batch-8 verification 2026-11-21, upgraded at add time).",
            "MPN": "Best Buy model field (SKU 6681665).",
        },
        status="verified",
        notes="Best Buy $999.99 (was $1,199.99) InStock at add time. Verizon version SM-F776UZKAVZW and Pink"
        "SM-F776ULIAXAA are different MPNs. Marketplace rows $815.99–$1,239.84 excluded. (batch-8"
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-galaxy-tab-s10-fe-256gb-gray",
        brand="Samsung",
        model="Galaxy Tab S10 FE 256GB",
        variant="Gray",
        category="tablets",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 887276992259 (Samsung US official MSRP Price List, 8 editions 2025-03 to"
            "2026-07); single publisher, no second source at add time (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="MPN SM-X520NZAEXAR confirmed (Best Buy model field + Samsung MSRP list). Best Buy $469.99 (comp"
        "$669.99, Black Friday Deal) confirmed as new self-operated row at add time (Sold by Best Buy;"
        "$874.69 is Merchant Expo marketplace, open-box $392.99–$422.99 excluded). Blue UPC 887276992273"
        "is a different color (SM-X520NLBEXAR). No collision with the 128GB model (SM-X520NZAAXAR)."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="apple-iphone-air-256gb-space-black",
        brand="Apple",
        model="iPhone Air 256GB",
        variant="Space Black",
        category="phones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 195950621303 (BarcodesInc GTIN 0195950621303 + PayMore Thornton scan + eBay"
            "seller table); reseller/marketplace-grade legs only, no brand/retailer spec page or distributor"
            "table — same bar as Watch Ultra 3 / iPhone 17 Pro Max, not upgraded at add time (batch-8"
            "verification 2026-11-21).",
        },
        status="pending",
        notes="MPN MG184LL/A confirmed (Best Buy model field, SKU 6473225; Model A3260). Best Buy $799.99"
        "(comp $1,099.99) InStock at add time — connect-later unlocked price; $699.99 is"
        "carrier-activated, not written. Light Gold / Sky Blue $999.99 / $919.99 prices are stale (four"
        "colors now $799.99). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="google-pixel-10-pro-128gb-obsidian",
        brand="Google",
        model="Pixel 10 Pro 128GB",
        variant="Obsidian",
        category="phones",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN GA09887-US confirmed (Best Buy model field, SKU 6637725). No UPC lead found anywhere. Best"
        "Buy $999.00 InStock at add time. Google Store $749 not verified at add time"
        "(store.google.com/config/pixel_10_pro renders no price in text fetch; 2025 Black Friday $749"
        "ended 2025-12-03) — not written. Third-party $869.99 (Platinum Supply Group) and refurb"
        "$442.68–$559 excluded. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="oneplus-15-12gb-256gb-infinite-black",
        brand="OnePlus",
        model="OnePlus 15 12GB + 256GB",
        variant="Infinite Black",
        category="phones",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 6921815630302 (Swiftronics + eBay.ie listing + ImportItAll);"
            "reseller/marketplace-grade legs only, no brand/retailer spec page or distributor table — not"
            "upgraded at add time (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="MPN CPH2749 (North America) confirmed (Swiftronics/myworldphone + FCC). Price row HELD at add"
        "time: oneplus.com US store closed per 2026-07-16 announcement (after-sales only, no store, no"
        "EXTRA100 code) — draft $799.00 code price is dead; Swiftronics $959.99 is a reseller, Amazon"
        "signals conflict ($833 vs $1,049), Best Buy only has 512GB Sand Storm $999.99. OnePlus has said"
        "it will not launch new phones in North America; 15 is the last North America flagship. (batch-8"
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-s90h-65",
        brand="Samsung",
        model="S90H 65\" OLED",
        variant="65\"",
        category="tvs",
        identifiers={
            "UPC": "198957270574",
            "MPN": "QN65S90HAEXZA",
        },
        identifier_sources={
            "UPC": "QVC tech spec PDF + manuals.plus Samsung spec table + B&H + Walts + shopmyexchange + Big Screen"
            "Store agree (batch-8 verification 2026-11-21).",
            "MPN": "Crutchfield MFR # + Samsung 2026 spec table + Best Buy model field agree.",
        },
        status="verified",
        notes="Best Buy $1,399.99 (Black Friday, comp $2,699.99) InStock at add time. Conflict resolved:"
        "198957276095 is the Canadian variant QN65S90HAEXZC (suffix C), not the US ZA model. Costco"
        "$1,399.99 includes an Allstate plan bundle, not the main row. (batch-8 verification"
        "2026-11-21).",
    ),
    EvalProduct(
        key="lg-oled-evo-c6-65",
        brand="LG",
        model="OLED evo C6 65\"",
        variant="65\"",
        category="tvs",
        identifiers={
            "UPC": "195174137666",
            "MPN": "OLED65C6PUA",
        },
        identifier_sources={
            "UPC": "B&H + EnergyStar list (OLED65C6PU* family) + Value Electronics + Amazon + Adorama agree"
            "(batch-8 verification 2026-11-21).",
            "MPN": "Best Buy model field (SKU 6673112).",
        },
        status="verified",
        notes="Best Buy $1,399.99 (Black Friday, comp $2,699.99) InStock at add time. EnergyStar also lists"
        "195174137703 (another PU* suffix variant) and Visions CA lists 195174137673 (regional) —"
        "neither is this model. LG also has OLED65C6WUA; Best Buy row uses PUA. (batch-8 verification"
        "2026-11-21).",
    ),
    EvalProduct(
        key="samsung-hw-q990h-black",
        brand="Samsung",
        model="HW-Q990H",
        variant="Black",
        category="soundbars",
        identifiers={
            "UPC": "198957269394",
            "MPN": "HW-Q990H/ZA",
        },
        identifier_sources={
            "UPC": "Walts retailer spec page + B&H + Amazon agree (batch-8 verification 2026-11-21).",
            "MPN": "Samsung US + Best Buy model field (SKU 6670431) agree.",
        },
        status="verified",
        notes="Best Buy $1,497.99 (self-operated); Samsung US $1,499.99. Woot $857.99 not used (suspected"
        "international/parallel stock, seller identity unverified). Do not mix with HW-Q990F (previous"
        "generation, pending). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="jbl-cinema-sb580-black",
        brand="JBL",
        model="Cinema SB580",
        variant="Black",
        category="soundbars",
        identifiers={
            "UPC": "050036408530",
            "MPN": "JBLSB580BLKAM",
        },
        identifier_sources={
            "UPC": "Crowdfused model/UPC table + goWholesale + VIP Outlet SKU VIP050036408530MN agree (batch-8"
            "verification 2026-11-21).",
            "MPN": "Crowdfused + goWholesale + VIP Outlet agree; JBL US Item# is JBLSB580BLKAM-Z (same model, -Z"
            "suffix).",
        },
        status="verified",
        notes="Walmart $199.00 (Sold and shipped by Walmart.com) InStock at add time. In-store clearance posts"
        "as low as $50 are isolated stores, not the online row; Walmart product page was bot-blocked for"
        "text fetch — Add to Cart needs live-browser check. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-smart-monitor-m70f-43-black",
        brand="Samsung",
        model="Smart Monitor M7 M70F 43\"",
        variant="Black",
        category="monitors",
        identifiers={
            "UPC": "198957005435",
            "MPN": "LS43FM702UNXZA",
        },
        identifier_sources={
            "UPC": "camelcamelcamel (ASIN B0F5VLWQY6) + DataVision + LayawayLand agree (batch-8 verification"
            "2026-11-21).",
            "MPN": "Samsung US + Best Buy model field (SKU 6632216) + Abt agree.",
        },
        status="verified",
        notes="Samsung US $499.99; Abt $499.99 InStock at add time. Best Buy $399.99 clearance and Amazon"
        "$279.99 clearance posts exist but are not the main row; Samsung US / Abt / B&H show no"
        "clearance flag — still regular sale. Different size from the 32\" M70F (LS32FM703UNXZA)."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-odyssey-g73sh-32-black",
        brand="Samsung",
        model="Odyssey OLED G7 G73SH 32\"",
        variant="Black",
        category="monitors",
        identifiers={
            "UPC": "198957301674",
            "MPN": "LS32HG732SNXZA",
        },
        identifier_sources={
            "UPC": "Micro Center + Walts + MonitorPug (+ eBay) agree (batch-8 verification 2026-11-21).",
            "MPN": "Costco Item 2084100 model field + Samsung promo terms Exhibit A + Samsung US agree.",
        },
        status="verified",
        notes="Costco $699.99 + $100 Costco Shop Card (digital card by email, up to 2 weeks to process)"
        "InStock at add time. Write $699.99 + card note, NOT a $599.99 net price. Samsung US list"
        "$1,099.99. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="hisense-qd7-55",
        brand="Hisense",
        model="QD7 Series 55\"",
        variant="55\"",
        category="tvs",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 888143028279 (Hisense official spec PDF hosted on Costco gdx-assets only);"
            "no second source at add time (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="MPN 55QD75SFC confirmed (Costco Item 9655750 model field + Hisense spec PDF). Costco $269.99"
        "(through 11/30/26) at add time; stock mixed — one fetch InStock, one OutOfStock; costcodrops"
        "2026-11-21 11:50 AM PT said in stock. Stock needs live-browser / next-refresh confirmation. Do"
        "not mix with Best Buy 75QD7QF (2025 QD7QF series). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-rog-strix-xg27ucgr-black",
        brand="ASUS",
        model="ROG Strix XG27UCG Gen2",
        variant="Black",
        category="monitors",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN XG27UCGR confirmed (ROG US + ASUS eShop; internal part 90LM0CS0-B013B2). No UPC lead found"
        "anywhere (EU EAN 4711636268141 is a different part number 90LM0CS0-B01371; white XG27UCGR-W"
        "GTIN 0199291268227 is a different color; XG27UCGR-G co-brand EAN 4711636689298 is a different"
        "variant). ROG US / ASUS eShop $399 InStock at add time; Staples $449; Target $425.99. Do NOT"
        "borrow the XG27UCG UPC 197105564633. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-legion-pro-7-gen-10-83ru0006us",
        brand="Lenovo",
        model="Legion Pro 7 Gen 10",
        variant="Eclipse Black",
        category="laptops",
        identifiers={
            "UPC": "199271660232",
            "MPN": "83RU0006US",
        },
        identifier_sources={
            "UPC": "PSREF PDF (EAN / UPC / JAN: 199271660232) + CompSource + SimplifiedComputers + Venditore +"
            "Bonanza agree (batch-8 verification 2026-11-21).",
            "MPN": "Best Buy model field (SKUs 12629843, 13259871) + PSREF PDF + CompSource agree.",
        },
        status="verified",
        notes="Adorama $4,949.00 InStock at add time. Best Buy same price is Sold and shipped by Adorama"
        "marketplace, not a Best Buy row. Newegg $4,495.62 seller identity unverified, not used. PSREF"
        "shows TopSeller: No (draft said TopSeller — corrected, does not affect UPC). Config pinned:"
        "Ryzen 9 9955HX3D / RTX 5080 16GB / 32GB DDR5-5600 / 2TB PCIe Gen5 / 16-inch WQXGA OLED 240Hz /"
        "Win 11 Pro. Do not mix with the 1TB config ($2,849.99, expired) or 83RU0005US (RAM disputed)."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="alienware-16-aurora-lac16250-7469blu-blue",
        brand="Alienware",
        model="16 Aurora",
        variant="Blue",
        category="laptops",
        identifiers={
            "UPC": "884116430469",
            "MPN": "LAC16250-7469BLU-PUS",
        },
        identifier_sources={
            "UPC": "D&H Consumer spec table + Product Setup - New Age spec table + Electronic Express + B&H agree"
            "(batch-8 verification 2026-11-21).",
            "MPN": "AntOnline (Manufacturer Part Number LAC16250-7469BLU-PUS) + Best Buy model field + Newegg"
            "agree.",
        },
        status="verified",
        notes="Live row B&H $1,549.00 In Stock at add time (top-tier retailer, $600.99 below AntOnline"
        "$2,149.99 — AntOnline row superseded; HOLD on AntOnline lifted 2026-11-21, B&H row adopted"
        "instead). Best Buy SKU 13279039 Sold Out; Dell.com configurator $2,699.99 list is a different"
        "32GB config. Config pinned: Core 7 240H / RTX 5060 8GB / 16GB DDR5-5600 / 1TB / 16-inch WQXGA"
        "120Hz / Win 11 Home. B&H lists the lid as Interstellar Indigo, 5.67 lb vs D&H 5.49 lb — same"
        "SKU (URL + UPC), wording only. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-loq-essential-15arp11-83va001pus",
        brand="Lenovo",
        model="LOQ Essential 15ARP11",
        variant="Eclipse Black",
        category="laptops",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — 83VA001PUS single source (Best Buy model field, SKU 6673556); lenovo.com US shows"
            "LOQ Essential 15IRH11 (Intel), not 15ARP11; no B&H hit (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="Best Buy $1,049.99 (Comp. Value $1,499.99) InStock at add time. Best Buy title says 2K but the"
        "spec panel says FHD 1920x1080 144Hz — panel governs. $999.99 Black Friday variant and $1,299.00"
        "PC Heaven marketplace SKU not used. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-rog-zephyrus-g14-ga403um-r9hx4-white",
        brand="ASUS",
        model="ROG Zephyrus G14 (2025)",
        variant="Platinum White",
        category="laptops",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — GA403UM-G14.R9HX4 single source (Best Buy model field, SKU 6629420); Velztorm"
            "marketplace / Smartprix / Slickdeals are not qualifying second sources; no B&H / ASUS US store"
            "hit (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="Best Buy $2,299.99 InStock at add time. Open-box $1,154.99 / $1,085.99 / $1,015.99 and Velztorm"
        "Upgraded rows excluded; Tom's Guide $1,349 is a 2025-07 old price. (batch-8 verification"
        "2026-11-21).",
    ),
    EvalProduct(
        key="hp-omen-transcend-14-14-fb1043dx-black",
        brand="HP",
        model="OMEN Transcend 14",
        variant="Shadow Black",
        category="laptops",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 821844495667 (HP datasheet PDF only); no second source at add time (batch-8"
            "verification 2026-11-21).",
        },
        status="pending",
        notes="MPN 14-fb1043dx / D8KM3UA#ABA confirmed (Best Buy model field, SKU 6672941 + HP datasheet PDF)."
        "Best Buy $2,499.99 InStock at add time (list price, no promo; Win 11 Home confirmed, not Pro)."
        "Do not mix with 32GB 14-fb1013dx (Best Buy dead). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="samsung-galaxy-book5-360-15-np750qha-ka1us-gray",
        brand="Samsung",
        model="Galaxy Book5 360 15.6\"",
        variant="Gray",
        category="laptops",
        identifiers={},
        identifier_sources={},
        status="pending",
        notes="MPN NP750QHA-KA1US confirmed (Best Buy model field + Quill + Connection + Staples, four"
        "sources). No UPC lead found. Connection $1,695.95 In Stock (Ships in 1–2 Business Days) / Quill"
        "$1,702.99 InStock at add time — tier accepted: both are US direct online retailers (PC"
        "Connection, Staples-owned Quill) selling direct to consumers; two independent rows agree at"
        "about $1,700. Best Buy $358.99 clearance vs $2,187.81 conflict both Unavailable, irrelevant."
        "Staples $1,419.69 out of stock (193+ days old). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="lenovo-yoga-7i-2-in-1-14-83tc003xus-luna-grey",
        brand="Lenovo",
        model="Yoga 7i 2-in-1 14\" Gen 11",
        variant="Luna Grey",
        category="laptops",
        identifiers={},
        identifier_sources={
            "UPC": "UPC pending — lead 199275077982 (TekFeed aggregator only); Newegg shows the code only as a"
            "third-party bundle listing internal model# prefix, not a retailer spec page for this SKU; PSREF"
            "14IPH11 not found (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="MPN 83TC003XUS confirmed (Best Buy model field, SKU 6671007 + Newegg + NotebookCheck). Best Buy"
        "$999.99 (Save $650, Comp. Value $1,649.99) InStock at add time. Open-box $765.99–$812.99,"
        "refurb $1,199.99 (IST Computers) and Upgraded marketplace rows excluded. Do not mix with Yoga"
        "7i 16-inch 83JT0000US or 83TE0004US. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="dell-xps-13-ldx13260-5960sky-sky",
        brand="Dell",
        model="XPS 13 (2026)",
        variant="Sky",
        category="laptops",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — LDX13260-5960SKY-PUS (Best Buy model field, SKU 6683772 + retail box photos); no"
            "second retailer (-PUS is a Best Buy retail SKU; dell.com configurator does not carry it)"
            "(batch-8 verification 2026-11-21).",
            "UPC": "UPC pending — lead 884116652960 (eBay listing item 327296803592 + mirrors only); no"
            "retailer/distributor second source (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="Best Buy $999.99 InStock at add time. Slickdeals $699.99 expired (promo ended Nov 18) — not"
        "written. Best Buy SKU 13223232 $969.00 seller unknown, not used. Title says 3K but spec panel"
        "says 2560x1600 (2.5K) 120Hz — panel governs. Do not mix with 8GB LDX13260-5953SKY-PUS. (batch-8"
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="dji-osmo-action-5-pro-standard-combo-black",
        brand="DJI",
        model="Osmo Action 5 Pro Standard Combo",
        variant="Black",
        category="action-cameras",
        identifiers={
            "UPC": "190021114616",
            "MPN": "CP.OS.00000377.01",
        },
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec table (SKU 754903) agree (batch-8 verification 2026-11-21).",
            "MPN": "B&H URL slug + Micro Center Mfr Part # agree.",
        },
        status="verified",
        notes="B&H $319.00 In Stock at add time; Micro Center $319.99. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="dji-osmo-pocket-3-black",
        brand="DJI",
        model="Osmo Pocket 3",
        variant="Black",
        category="cameras",
        identifiers={
            "UPC": "190021094970",
            "MPN": "CP.OS.00000301.01",
        },
        identifier_sources={
            "UPC": "B&H spec page + NFM agree (batch-8 verification 2026-11-21).",
            "MPN": "B&H (BH # DJOP3) + Crutchfield MFR # agree; different from Creator Combo CP.OS.00000302.01.",
        },
        status="verified",
        notes="B&H $373.00 (was $439.00) In Stock at add time; Best Buy same price $373 (Sold by Best Buy)."
        "Amazon $373 is corroboration only, not a price source. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="dji-mini-5-pro-rc-n3-gray",
        brand="DJI",
        model="Mini 5 Pro",
        variant="Gray",
        category="drones",
        identifiers={
            "UPC": "190021121126",
            "MPN": "CP.MA.00000838.03",
        },
        identifier_sources={
            "UPC": "B&H spec page + Target product page (TCIN 1012392891) agree (batch-8 verification 2026-11-21).",
            "MPN": "B&H URL slug + Adorama MFR agree (Adorama K suffix is its bundle SKU, not taken).",
        },
        status="verified",
        notes="B&H $759.00 In Stock at add time. New category: drones (user-approved batch 8). Slickdeals"
        "posts are AliExpress prices ($508–$825) — heat signal only, not a price source. (batch-8"
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="dji-neo-2-drone-only-gray",
        brand="DJI",
        model="Neo 2",
        variant="Gray",
        category="drones",
        identifiers={
            "UPC": "190021157224",
            "MPN": "CP.FP.00000270.01",
        },
        identifier_sources={
            "UPC": "B&H spec page + Target product page (TCIN 1015573677) + Visions CA agree (batch-8 verification"
            "2026-11-21).",
            "MPN": "Adorama MFR + B&H URL slug + Visions CA agree.",
        },
        status="verified",
        notes="B&H $259.00 In Stock / Adorama $259.00 In Stock at add time. New category: drones"
        "(user-approved batch 8). Neo 2 is not on DJI US direct (UFLPA customs) — US rows are authorized"
        "dealers (B&H, Adorama, djiusa.com), still retailer-direct. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="insta360-x5-standard-bundle-black",
        brand="Insta360",
        model="X5 Standard Bundle",
        variant="Black",
        category="action-cameras",
        identifiers={
            "UPC": "842126110955",
            "MPN": "CINSAAHA_X501",
        },
        identifier_sources={
            "UPC": "B&H spec page + NFM agree; B&H Motorcycle Bundle parts list also carries the same UPC (batch-8"
            "verification 2026-11-21).",
            "MPN": "B&H URL slug + NFM Model field agree.",
        },
        status="verified",
        notes="B&H $439.99 (was $549.99) In Stock at add time; Insta360 US store $439.99; Target $439.99. Do"
        "not mix with the Best Buy / Costco X5 Bundle (MPN CINSAAHA, UPC 842126113239, different bundle"
        "SKU). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="insta360-x6-standard-bundle-midnight-black",
        brand="Insta360",
        model="X6 Standard Bundle",
        variant="Midnight Black",
        category="action-cameras",
        identifiers={
            "UPC": "842126120213",
            "MPN": "CINSABXA-X601",
        },
        identifier_sources={
            "UPC": "Micro Center spec table + Visions CA agree (batch-8 verification 2026-11-21).",
            "MPN": "Micro Center Mfr Part # + Visions CA agree; B&H slug cinsabxa_x602 is the Arctic White X602,"
            "not mixed.",
        },
        status="verified",
        notes="Live row B&H $629.99 (was $699.99, Holiday Savings $70) In Stock at add time — draft $699.99"
        "list price corrected. Adorama $699.99 InStock as secondary reference. B&H also lists EAN"
        "6942590200337 (different numbering system); UPC used, EAN not written. (batch-8 verification"
        "2026-11-21).",
    ),
    EvalProduct(
        key="gopro-hero13-black-black",
        brand="GoPro",
        model="HERO13 Black",
        variant="Black",
        category="action-cameras",
        identifiers={
            "UPC": "810116381821",
            "MPN": "CHDHX-131-TH",
        },
        identifier_sources={
            "UPC": "B&H spec page + The Pixel Hub barcode field agree (batch-8 verification 2026-11-21).",
            "MPN": "B&H (BH # GOH13BLK) + Berger Bros SKU agree.",
        },
        status="verified",
        notes="B&H $349.99 (was $429.99) Temporarily Out of Stock at add time, expected availability Dec 07,"
        "2026 — row is out of stock, identifiers verified. Scuba CHDHX-131-RW / UPC 810116381616 variant"
        "not verified, not attached to this model. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="insta360-go-3s-standard-bundle-128gb-midnight-black",
        brand="Insta360",
        model="GO 3S Standard Bundle 128GB",
        variant="Midnight Black",
        category="action-cameras",
        identifiers={
            "UPC": "842126106989",
            "MPN": "CINSAATA_GO3S13",
        },
        identifier_sources={
            "UPC": "B&H spec page + Micro Center spec table (SKU 721472) agree (batch-8 verification 2026-11-21).",
            "MPN": "B&H slug + Micro Center Mfr Part # + CompSource agree.",
        },
        status="verified",
        notes="B&H $299.99 (was $379.99) In Stock at add time; Micro Center $299.99. Do not mix with Target GO"
        "3S Action Bundle (UPC 842126107641) or B&H Camera Only (CINSAATA_GO3S11, UPC 842126106965)."
        "(batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-rog-delta-ii-white",
        brand="ASUS",
        model="ROG Delta II",
        variant="Moonlight White",
        category="headphones",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — conflict: Newegg US lists 90YH03W0-BHAA10, SG/EU channels list 90YH03W0-BHUA10"
            "(suspected US vs APAC suffix split); do not choose (batch-8 verification 2026-11-21).",
            "UPC": "UPC pending — lead 197105907362 (SG channels only, no US retailer spec page); 197105907355 is"
            "FALSIFIED (Ubuy misattribution — ASIN B0DGZY13L6 is the Black model, UPC 197105604858);"
            "197105604858 is the Black model's UPC, not this one (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="Best Buy $149.99 (Black Friday Deal, comp $229.99) InStock at add time, SKU 6637821, Model A701"
        "ROG DELTA II/WHT. Best Buy spec page could not be expanded in text fetch — UPC needs"
        "live-browser See all specifications check. Different color from the Black model"
        "(asus-rog-delta-ii-black, pending). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-rog-keris-ii-ace-white",
        brand="ASUS",
        model="ROG Keris II Ace",
        variant="Moonlight White",
        category="mice",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — conflict found at add time: ASUS eShop US white page lists 90MP03N0-BMAA10"
            "($159.99) vs IPCStore/PBTech/SquareDeals 90MP03N0-BMUA10; same US/APAC suffix shape as Delta"
            "II; downgraded from VERIFIED at add time 2026-11-21.",
            "UPC": "UPC pending — conflict: 197105394612 (PBTech NZ / SquareDeals SG / Dynacore SG / Carousell SG,"
            "bound to BMUA10) vs 197105394582 (Amazon ASIN B0D3CX3QMD data + SpaceBoundSolutions US"
            "distributor, item 1017783); both check digits valid — needs a US retailer spec page to decide"
            "(batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="IPCStore $179.00 in stock at add time (US retailer, MPN-bound listing). ASUS eShop $94.99"
        "Starting at does NOT cover White (white page BMAA10 is $159.99); Best Buy $182.43 is antonline"
        "marketplace (excluded); Target $129.99 OutOfStock. Different color from the Black model"
        "(asus-rog-keris-ii-ace-black, pending). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-rog-strix-scope-ii-96-wireless-white-nx-storm",
        brand="ASUS",
        model="ROG Strix Scope II 96 Wireless",
        variant="Moonlight White",
        category="keyboards",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — 90MP037B-BKAA30 single source (ASUS eShop US white Storm page, Product Name X901"
            "SCOPE II 96 WL/WHT/NXSM/CA/PBT); eShop Color field reads Black (template mismatch), Product"
            "Name /WHT/ governs (batch-8 verification 2026-11-21).",
            "UPC": "UPC pending — lead 197105487154 (Target spec page + Newegg Model # + Snapklik agree on the"
            "model string, but Target page is Target Plus Partner marketplace info and no US retailer spec"
            "table backs it) (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="ASUS eShop US $131.99 InStock at add time. Best Buy only carries the Snow (linear) white model"
        "(SKU 6595753, $109.99) — different switch, do not mix. NX Snow white (90MP037A-BKAA30, Canada"
        "eShop) not selected (no US UPC; EU EANs are non-US). Newegg $129.99–$149.99 is a from range,"
        "seller unclear, not the main row. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-zenwifi-bt8-3-pack-white",
        brand="ASUS",
        model="ZenWiFi BT8 3-pack",
        variant="White",
        category="routers",
        identifiers={
            "UPC": "197105532090",
            "MPN": "BT8(W-3-PK)",
        },
        identifier_sources={
            "UPC": "B&H spec page (retailer) + SHI distributor UPC field agree (batch-8 verification 2026-11-21).",
            "MPN": "ASUS US Tech Specs (BT8(W-3-PK) / BT8(W-2-PK) / BT8(W-1-PK)) + Microless agree.",
        },
        status="verified",
        notes="B&H $699.99 (was $849.99, Holiday Savings $150) InStock at add time; ASUS eShop US same price"
        "$699.99. Independent model from the 2-pack (asus-zenwifi-bt8-2-pack-white, verified, UPC"
        "197105532045). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-zenwifi-bt10-1-pack-white",
        brand="ASUS",
        model="ZenWiFi BT10 1-pack",
        variant="White",
        category="routers",
        identifiers={
            "UPC": "197105429833",
            "MPN": "BT10(W-1-PK)",
        },
        identifier_sources={
            "UPC": "B&H spec page (retailer) + DirectDial distributor (MFG PART BT10(W-1-PK) + UPC) agree (batch-8"
            "verification 2026-11-21).",
            "MPN": "ASUS US Tech Specs + DirectDial manufacturer part number agree.",
        },
        status="verified",
        notes="B&H $346.00 In Stock at add time; ASUS US $359.99. Independent model from the 2-pack"
        "(asus-zenwifi-bt10-2-pack-white, pending, lead UPC 197105429895); 1-pack UPC …9833 vs 2-pack"
        "lead …9895, do not mix. (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="asus-tuf-gaming-m3-gen-ii-black",
        brand="ASUS",
        model="TUF Gaming M3 Gen II",
        variant="Black",
        category="mice",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — conflict found at add time: Newegg Model # + B&H MFR # list 90MP0320-BMAA00, but"
            "the ASUS eShop US in-stock page lists Part Number 90MP0320-BMAA03 (same product name P309 TUF"
            "GAMING M3 GEN II); suspected replacement SKU / version change; downgraded from VERIFIED at add"
            "time 2026-11-21.",
            "UPC": "UPC pending — lead 195553909112 FALSIFIED at add time: PBTech NZ + NationalPC India bind it to"
            "the non-US MPN 90MP0320-BMUA00 (with EAN 4711081909118), not the US BMAA00 — lead void, no"
            "valid lead (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="Adorama $25.99 InStock at add time; ASUS eShop $24.99 now InStock (draft said out of stock —"
        "corrected) and is the cheaper direct row. B&H discontinued (old $28.64). Newegg self-operated"
        "$22.99 (WorstDealsEver, 2026-10-26) not live re-verified. No M3 Gen II in the catalog before"
        "(only TUF M4 Air and TUF K3 Gen II). (batch-8 verification 2026-11-21).",
    ),
    EvalProduct(
        key="8bitdo-sn30-pro-hall-effect-g-classic",
        brand="8BitDo",
        model="SN30 Pro",
        variant="G Classic",
        category="controllers",
        identifiers={},
        identifier_sources={
            "MPN": "MPN pending — 80DJ04 single source (Best Buy model field); grey is 80DM02, a different model"
            "(batch-8 verification 2026-11-21).",
            "UPC": "UPC/EAN pending — lead 6922621509547 (13-digit EAN, Target spec page only); no second source"
            "(B&H does not carry it) (batch-8 verification 2026-11-21).",
        },
        status="pending",
        notes="Best Buy $34.99 (Black Friday Deal, comp $44.99) InStock at add time, SKU 6590319, Sold by Best"
        "Buy. Target $44.99 InStock as second row. Best Buy SKU 10189263 also lists Model 80DJ04 but no"
        "page was found — relationship unconfirmed. Hall Effect version pinned by with Hall Effect"
        "Joysticks + Model 80DJ04; do not mix with the old non-Hall-Effect version. (batch-8"
        "verification 2026-11-21).",
    ),
    EvalProduct(
        key="microsoft-xbox-wireless-controller-forza-horizon-6-limited-edition",
        brand="Microsoft",
        model="Xbox Wireless Controller Forza Horizon 6 Limited Edition",
        variant="Forza Horizon 6 LE",
        category="controllers",
        identifiers={
            "UPC": "196388601059",
            "MPN": "EP2-42276",
        },
        identifier_sources={
            "UPC": "GameStop US retailer spec page (UPC + Vendor PN EP2-42276) + goWholesale distributor agree"
            "(batch-8 verification 2026-11-21).",
            "MPN": "Walmart Model field + GameStop Vendor Part Number + Lenovo US Manufacturer PN agree.",
        },
        status="verified",
        notes="Walmart $49.00 (was $84.00) sold/shipped by Walmart at add time. Limited Edition but widely in"
        "stock at Walmart/Best Buy/GameStop, not clearance — included per user approval (batch 8)."
        "Target $74.99 InStock as backup row. GameStop own price $89.99/$69.99 Currently Unavailable,"
        "not a row. Different colorway from the standard Black controller"
        "(xbox-wireless-controller-black). (batch-8 verification 2026-11-21).",
    ),
]






def get_product(key: str) -> EvalProduct:
    for product in EVAL_SET:
        if product.key == key:
            return product
    raise KeyError(f"unknown eval model key: {key}")
