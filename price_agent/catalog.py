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
                model="K8 Pro QMK", variant="unpinned", category="keyboards",
                notes="Keychron 直营用 SKU（如 K8P-G1、K8P-Q1）而非 UPC；同款须按具体配置"
                "钉死 SKU，暂不 verified；K8（非 Pro）的 UPC 不得挪用。"),
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
                notes="UPC/MPN pending verification."),
    EvalProduct(key="xbox-wireless-controller-black", brand="Microsoft",
                model="Xbox Wireless Controller", variant="Carbon Black",
                category="controllers",
                notes="UPC/MPN pending verification."),
    EvalProduct(key="meta-quest-3s-128gb", brand="Meta",
                model="Quest 3S (128GB)", variant="unpinned",
                category="vr",
                notes="UPC/MPN pending verification."),
    EvalProduct(key="anker-737-120w", brand="Anker",
                model="737 GaNPrime Charger (120W)", variant="unpinned",
                category="chargers",
                notes="UPC/MPN pending verification."),
    EvalProduct(key="apple-magic-mouse-usbc", brand="Apple",
                model="Magic Mouse (USB-C)", variant="unpinned",
                category="mice",
                notes="UPC/MPN pending verification."),
    EvalProduct(key="logitech-g-pro-x-superlight-2-black", brand="Logitech",
                model="G Pro X Superlight 2", variant="Black",
                category="mice",
                notes="UPC/MPN pending verification."),
    EvalProduct(key="google-pixel-buds-pro-2-porcelain", brand="Google",
                model="Pixel Buds Pro 2", variant="Porcelain",
                category="earbuds",
                notes="UPC/MPN pending verification."),
]


def get_product(key: str) -> EvalProduct:
    for product in EVAL_SET:
        if product.key == key:
            return product
    raise KeyError(f"unknown eval model key: {key}")
