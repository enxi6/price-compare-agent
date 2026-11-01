"""Phase 1 evaluation set: 28 standardized electronics models, US market.

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
        key="logitech-mx-master-3s-graphite",
        brand="Logitech",
        model="MX Master 3S",
        variant="Graphite, standard edition (910-006557)",
        category="mice",
        identifiers={"UPC": "097855174789", "MPN": "910-006557"},
        identifier_sources={
            "UPC": "Amazon listing for 910-006557 (For Mac / Business / "
            "Bluetooth editions carry different UPCs)"
        },
        notes="Update 2026-10-31: Logitech official-catalog sweep "
        "(BUILD_LOG 024) finds no plain consumer MX Master 3S in "
        "the 65-product Mice catalog; the line's current flagship "
        "is MX Master 4. Related variants still sold (different "
        "products, not equivalents): MX Master 3S Bluetooth "
        "Edition 910-007499 ($79.99) and MX Master 3S for Business "
        "($109.99). Replacement decision pending user.",
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
    EvalProduct(key="keychron-k8-pro", brand="Keychron",
                model="K8 Pro QMK",
                variant="Black, Fully Assembled (Hot-Swappable), White Backlight, "
                "Gateron G Pro Red (K8P-G1)",
                category="keyboards",
                identifiers={"EAN": "4895248806837", "SKU": "K8P-G1"},
                identifier_sources={
                    "EAN": "Keychron official store public product JSON, "
                    "browser-verified 2026-10-31 (31 variants; K8P-G1 barcode "
                    "4895248806837, K8P-G2 4895248806844). Earlier assumption "
                    "that Keychron uses SKUs only was wrong: the JSON carries "
                    "barcodes per variant."
                },
                notes="Update 2026-10-31: small-brands sweep (BUILD_LOG "
                "025) finds K8P-G1 still listed on keychron.com but "
                "Sold out (0 in stock; sale $74.99, reg $99.99). Page "
                "points to successors K8 HE & K8 Ultra 8K. Listed-but- "
                "sold-out is not the same as discontinued; handling "
                "(keep / replace with successor) pending user decision.",
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
                notes="Current generation announced 2026-10-27; pre-order, "
                "ships 2026-11-06. Part number MHWT4LL/A confirmed by "
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
]


def get_product(key: str) -> EvalProduct:
    for product in EVAL_SET:
        if product.key == key:
            return product
    raise KeyError(f"unknown eval model key: {key}")
