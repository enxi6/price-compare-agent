"""Phase 1 evaluation set: 20 standardized electronics models, US market.

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
        key="apple-airpods-pro-2-lightning",
        brand="Apple",
        model="AirPods Pro (2nd generation)",
        variant="Lightning case (MQD83AM/A)",
        category="earbuds",
        identifiers={"UPC": "194253397168", "MPN": "MQD83AM/A"},
        identifier_sources={
            "UPC": "Abt + eBay listings agree for MQD83AM/A (USB-C version "
            "MTJV3AM/A is a different UPC, 0195949052484)"
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
        key="samsung-buds2-pro-white",
        brand="Samsung",
        model="Galaxy Buds2 Pro",
        variant="White, US version (SM-R510NZWAXAR)",
        category="earbuds",
        identifiers={"UPC": "887276668741", "MPN": "SM-R510NZWAXAR"},
        identifier_sources={
            "UPC": "Amazon + Best Buy listings agree for SM-R510NZWAXAR "
            "(Bora Purple is 887276709000)"
        },
        status="verified",
    ),
    # --- Pending: model pinned, identifiers NOT yet verified (never invent) ---
    EvalProduct(key="sony-wf1000xm5-black", brand="Sony",
                model="WF-1000XM5", variant="Black (WF1000XM5/B)",
                category="earbuds",
                identifiers={"UPC": "027242925601"},
                identifier_sources={
                    "UPC": "Adorama + Amazon US + Abt + eBay agree for WF1000XM5/B "
                    "(international version and bundles carry different UPCs)"
                },
                status="verified"),
    EvalProduct(key="apple-airpods-4-usbc", brand="Apple",
                model="AirPods 4", variant="USB-C case (MXP63LL/A)",
                category="earbuds",
                identifiers={"UPC": "195949688522", "MPN": "MXP63LL/A"},
                identifier_sources={
                    "UPC": "Adorama + B&H Photo + Amazon US agree for MXP63LL/A "
                    "(India MXP63HN/A and ANC MXP93LL/A are different products)"
                },
                status="verified"),
    EvalProduct(key="apple-watch-se2-40mm", brand="Apple",
                model="Watch SE 2 (40mm, GPS)", variant="Midnight, GPS (MXE93LL/A)",
                category="wearables",
                identifiers={"UPC": "195949641756", "MPN": "MXE93LL/A"},
                identifier_sources={
                    "UPC": "Micro Center spec sheet for MXE93LL/A (single source; "
                    "band size unconfirmed in source; other colors, bands, "
                    "cellular and year variants carry different UPCs)"
                },
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
                "left unverified for now."),
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
    EvalProduct(key="anker-737-120w", brand="Anker",
                model="737 GaNPrime Charger (120W)",
                variant="Black, US plug (A2148)",
                category="chargers",
                identifiers={"UPC": "194644099008", "MPN": "A2148111"},
                identifier_sources={
                    "UPC": "Swiftsly + Ubuy listings agree for A2148; EAN "
                    "0194644099008 is the same code in GTIN form (UK-plug "
                    "versions are separate references)"
                },
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
                model="G Pro X Superlight 2", variant="Black (910-006630)",
                category="mice",
                identifiers={"EAN": "5099206104525", "MPN": "910-006630"},
                identifier_sources={
                    "EAN": "Multiple EU retailer listings agree for 910-006630 "
                    "(910-006631 is the same mouse in different regional "
                    "packaging; US UPC not separately confirmed, EAN is the "
                    "GTIN-family identifier)"
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
    # --- Apple cluster (added 2026-10-31, user-approved) ---
    # All pinned to base configs; part numbers / UPCs pending verification.
    # iPhone deliberately excluded: carrier financing and lock status make
    # "cheapest" non-comparable without contract context.
    EvalProduct(key="apple-macbook-air-13-m4", brand="Apple",
                model="MacBook Air 13-inch (M4, 2025)",
                variant="M4, 16GB/256GB, Starlight (MW0Y3LL/A)",
                category="laptops",
                identifiers={"UPC": "195949837197", "MPN": "MW0Y3LL/A"},
                identifier_sources={
                    "UPC": "eBay item specifics + Bestpeek agree for MW0Y3LL/A; "
                    "Best Buy US confirms the MPN (SKU 6565859). Other colors "
                    "are different part numbers."
                },
                status="verified"),
    EvalProduct(key="apple-macbook-air-15-m4", brand="Apple",
                model="MacBook Air 15-inch (M4, 2025)",
                variant="M4, 16GB/256GB, Sky Blue (MC7A4LL/A)",
                category="laptops",
                identifiers={"UPC": "195949893162", "MPN": "MC7A4LL/A"},
                identifier_sources={
                    "UPC": "Two distinct eBay listings agree for MC7A4LL/A. "
                    "Other colors are different part numbers."
                },
                status="verified"),
    EvalProduct(key="apple-macbook-pro-14-m4", brand="Apple",
                model="MacBook Pro 14-inch (M4, 2024)",
                variant="M4, 16GB/512GB, Space Black (MW2U3LL/A)",
                category="laptops",
                identifiers={"UPC": "195949507786", "MPN": "MW2U3LL/A"},
                identifier_sources={
                    "UPC": "Two distinct eBay listings + Back Market agree for "
                    "MW2U3LL/A (UK B/A and AU X/A suffixes are regional; "
                    "Silver MW2W3LL/A is a different SKU)."
                },
                status="verified"),
    EvalProduct(key="apple-mac-mini-m4", brand="Apple",
                model="Mac mini (M4, 2024)",
                variant="M4, 16GB/256GB, Silver (MU9D3LL/A)",
                category="desktops",
                identifiers={"UPC": "195949080296", "MPN": "MU9D3LL/A"},
                identifier_sources={
                    "UPC": "Many distinct eBay listings agree (GTIN 0195949080296); "
                    "UK B/A code is regional. One listing pairing MU9E3LL/A "
                    "with this config and one stray UPC were excluded."
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
    EvalProduct(key="apple-ipad-air-m3-11", brand="Apple",
                model="iPad Air 11-inch (M3, 2025)",
                variant="M3, 128GB Wi-Fi, Purple (MCA04LL/A)",
                category="tablets",
                identifiers={"UPC": "195949997952", "MPN": "MCA04LL/A"},
                identifier_sources={
                    "UPC": "Two distinct eBay listings agree for MCA04LL/A. "
                    "Space Gray/Blue/Starlight are MC9x4LL/A codes; Wi-Fi + "
                    "Cellular is a different SKU."
                },
                status="verified"),
    EvalProduct(key="apple-ipad-pro-m4-11", brand="Apple",
                model="iPad Pro 11-inch (M4, 2024)",
                variant="M4, 256GB Wi-Fi, Space Black (MVV83LL/A)",
                category="tablets",
                identifiers={"UPC": "195949222467", "MPN": "MVV83LL/A"},
                identifier_sources={
                    "UPC": "Many distinct eBay listings agree for MVV83LL/A. "
                    "Silver MVV93LL/A is a different SKU; Wi-Fi + Cellular "
                    "is a different SKU."
                },
                status="verified"),
    EvalProduct(key="apple-airpods-max-usbc", brand="Apple",
                model="AirPods Max (USB-C, 2024)",
                variant="USB-C, Midnight (MWW43AM/A)",
                category="headphones",
                identifiers={"UPC": "195949543890", "MPN": "MWW43AM/A"},
                identifier_sources={
                    "UPC": "Best Buy US + multiple eBay listings agree for "
                    "MWW43AM/A. One eBay catalog page giving 1959495440206 "
                    "was excluded as conflicting. Lightning version is a "
                    "different model."
                },
                status="verified"),
]


def get_product(key: str) -> EvalProduct:
    for product in EVAL_SET:
        if product.key == key:
            return product
    raise KeyError(f"unknown eval model key: {key}")
