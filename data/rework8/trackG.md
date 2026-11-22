# Track G — 第八批草稿（外设队列顶位 + deal-site 补位）

- 日期：2026-11-21/22（PT 11-21 晚间核查；B&H/Best Buy 实页抓取时间为 2026-11-22 00:00–00:02 UTC）
- 目录对照：`data/rework8/catalog_ref_550.tsv`（550 款）。每款均已按 key、型号名子串（双向归一化）、MPN、UPC 四项对照：**8 款候选全部 0 撞号**（key 子串、全部 MPN 与 UPC 字符串在表中均为 0 命中；见文末复核记录）。
- 规则：UPC 是唯一门；MPN 单独不扶正；无第二来源 → pending；分销商第二来源按先例（零售商+分销商可接受，分销商+分销商留 pending）；只认商家自营；只认美版货；Amazon 价不作价格来源；eBay/翻新/清仓旧款排除。全部候选 UPC 已做校验位验算（见各款备注）。
- 价格说明：本次多为黑五促销价（Best Buy 标注 Ends Nov. 28），入目录时须按惯例重新验 live 价。

## 标识 tally

- 候选总数：8 款
- UPC verified：3 款（BT8 3-pack、BT10 1-pack、Xbox Forza LE）
- UPC pending：5 款（Delta II 白、Keris II Ace 白、Scope II 96 白 NX Storm、TUF M3 Gen II、SN30 Pro）
- MPN 有线索：8/8（其中 Delta II 白 MPN 美版/亚太版后缀冲突，见该款备注）

---

## 1. asus-rog-delta-ii-white

- 品牌：ASUS ／ 型号：ROG Delta II Wireless Gaming Headset，Moonlight White
- 新 key：`asus-rog-delta-ii-white`
- 队列标注：第六批后备队列；目录已有黑色款 `asus-rog-delta-ii-black`（pending、无标识），白色为不同颜色款，不撞号。
- MPN：**pending（冲突）**。美国渠道 Newegg  listing 型号栏为 `90YH03W0-BHAA10`；新加坡/欧洲渠道（Xcellent、SquareDeals、Carousell SG、Alfrensia）一致为 `90YH03W0-BHUA10`。后缀 BHAA10 vs BHUA10 疑似美版/亚太版之分，**不得二选一**，入目录时以美版实物或 Best Buy 规格页复核为准。
- UPC：**pending（线索冲突，勿选）**。
  - 线索 A：`197105907362`，与 MPN BHUA10 绑定，来源 SquareDeals（SG 零售商）、Dynacore（SG）、Carousell SG——均为非美渠道，无美国零售商规格页佐证。校验位有效。
  - 线索 B：`197105907355`，来源 Ubuy（ASIN B0DGZY13L6 附带），**已证伪**：亚马逊上 ASIN B0DGZY13L6 实为黑色款，其 UPC 为 `197105604858`（Micro Center 黑色款规格页亦为此码，校验位有效）；Ubuy 的 197105907355 属张冠李戴，**禁用**。
  - 另：`197105604858` 是黑色款 UPC，不得用于白色款。
- 价格行：Best Buy 自营（Sold by Best Buy）**$149.99**，InStock，Add to Cart，黑五价（对比价 $229.99），SKU 6637821，Model 栏 `A701 ROG DELTA II/WHT`。Best Buy 实页抓取未展开 "See all specifications"，故未从该页取到 UPC。
- 待定项：① 美版 MPN 后缀（BHAA10 vs BHUA10）；② 白色款 UPC 需美国零售商规格页第二来源；③ $149.99 为黑五促销价，入目录时重验 live 价。

## 2. asus-rog-keris-ii-ace-white

- 品牌：ASUS ／ 型号：ROG Keris II Ace Wireless Gaming Mouse，Moonlight White（P714 ROG KERIS II WL ACE/WHT）
- 新 key：`asus-rog-keris-ii-ace-white`
- 队列标注：第六批后备队列；目录已有黑色款 `asus-rog-keris-ii-ace-black`（pending、无标识），白色为不同颜色款，不撞号。
- MPN：`90MP03N0-BMUA10`（多源一致：PBTech、SquareDeals、Carousell SG；美国分销商 IPCStore 同款在售 $179）。MPN 本身不扶正，仅作线索。
- UPC：**pending（正面冲突，勿选）**。两个校验位均有效的 UPC 各执一端：
  - `197105394612`——PBTech（NZ 零售商，UPC 栏）、SquareDeals（SG）、Dynacore（SG）、Carousell SG，一致绑定 MPN BMUA10；
  - `197105394582`——美国亚马逊 ASIN B0D3CX3QMD（Desertcart 多站镜像 + Layup 均引同一亚马逊数据，实为同一源），GTIN 00197105394582。
  - 校验位验算不能区分两者（两码皆有效）。疑似美版/亚太版分包，**必须等美国零售商规格页（Best Buy/B&H/Target）定夺**，本次不采纳任一码。
- 价格行：
  - IPCStore（美国零售商，MPN 绑定 listing）**$179.00**，InStock——白色款可用价行。
  - ASUS eShop 美国直营 $94.99 起（原价 $159.99）、InStock，但页面黑白两色共用、"Starting at" 未按颜色拆分，**不能用作白色款价行**，仅作参考。
  - 排除：Best Buy 页 $182.43 的卖家是 antonline（第三方 marketplace），按规则排除；Target $129.99 缺货（OutOfStock），不用。
- 待定项：① UPC 冲突（612 vs 582）待美国零售商规格页裁决；② eShop $94.99 是否覆盖白色待入目录时按颜色复核。

## 3. asus-rog-strix-scope-ii-96-wireless-white-nx-storm

- 品牌：ASUS ／ 型号：ROG Strix Scope II 96 Wireless，Moonlight White，**ROG NX Storm（clicky）轴**——轴体已钉死
- 新 key：`asus-rog-strix-scope-ii-96-wireless-white-nx-storm`
- 队列标注：第六批后备队列；目录已有黑色款 `asus-rog-strix-scope-ii-96-wireless-black` 与 RX 无线黑色款，白色 Storm 为不同颜色+轴体款，不撞号。
- MPN：`90MP037B-BKAA30`（ASUS eShop 美国直营白 Storm 专页，Product Name `X901 SCOPE II 96 WL/WHT/NXSM/CA/PBT`）。注意 eShop 页面 Color 栏抓取显示为 "Black"（模板串色），以 Product Name 中的 /WHT/ 与 Part Number 为准。
- UPC：**pending（强线索，未达 verified）**。`197105487154`（校验位有效），三源一致指向同一型号串 `X901 SCOPE II 96 WL/WHT/NXSM/CA/PBT`：Target 规格页（UPC 栏，但该页注明 "item details provided by Target Plus Partner"，属 marketplace 供货信息，效力打折）、Newegg（Model # 栏直接填该 UPC）、Snapklik（聚合器，型号+UPC 同框）。无任何一家美国零售商规格表（Best Buy/B&H 规格页）背书，按先例（多源但无零售商规格表 → pending）留 pending。
- 价格行：ASUS eShop 美国直营 **$131.99**，InStock（Open Graph 抓取；注意同一 part 在较早抓取中为 $179.99，价格已变动，入目录时重验）。Newegg $129.99–$149.99 为 "from" 区间价、卖家不明，不作主价行。
- 待定项：① UPC 需 Best Buy 或 B&H 规格页第二来源；② **NX Snow 白色款（MPN 90MP037A-BKAA30，加拿大 eShop）未入选**：其美国 UPC 全网未找到（欧盟 EAN 4711387487082/4711387487112 非美版），本次只带 Storm 款，Snow 款留待后补；③ eShop $131.99 为促销价，入目录时重验。

## 4. asus-zenwifi-bt8-3-pack-white

- 品牌：ASUS ／ 型号：ZenWiFi BT8 BE14000 Tri-Band WiFi 7 Mesh，3-pack，White
- 新 key：`asus-zenwifi-bt8-3-pack-white`
- 队列标注：第六批后备队列；目录已有 2-pack `asus-zenwifi-bt8-2-pack-white`（verified，MPN BT8(W-2-PK)，UPC 197105532045），3-pack 为独立款型（pack 规格不同款），不撞号。
- MPN：`BT8(W-3-PK)`（ASUS 美国官网 Tech Specs 三档并列：BT8(W-3-PK)/BT8(W-2-PK)/BT8(W-1-PK)；Microless 规格表同款）。
- UPC：**verified：`197105532090`**（校验位有效）。B&H 规格页（零售商）+ SHI（分销商，UPC 栏）两源一致，符合零售商+分销商先例；亚马逊同款亦为此码（仅作旁证，不作价格来源）。
- 价格行：B&H 自营 **$699.99**，InStock，Add to Cart（划线 $849.99，Holiday Savings $150）；ASUS eShop 美国直营同价 $699.99。
- 待定项：无标识待定；仅入目录时重验 live 价（黑五促销价）。

## 5. asus-zenwifi-bt10-1-pack-white

- 品牌：ASUS ／ 型号：ZenWiFi BT10 BE18000 Tri-Band WiFi 7 Mesh，1-pack，White
- 新 key：`asus-zenwifi-bt10-1-pack-white`
- 队列标注：第六批后备队列；目录已有 2-pack `asus-zenwifi-bt10-2-pack-white`（pending，线索 UPC 197105429895 仅 B&H 单源），1-pack 为独立款型，不撞号。注意 1-pack UPC 与 2-pack 线索 UPC 不同（…9833 vs …9895），不得混同。
- MPN：`BT10(W-1-PK)`（ASUS 美国官网 Tech Specs 三档并列；DirectDial 制造商件号同款）。
- UPC：**verified：`197105429833`**（校验位有效）。B&H 规格页（零售商）+ DirectDial（分销商，MFG PART BT10(W-1-PK) + UPC 同框）两源一致，符合零售商+分销商先例；另有 Snapklik/Desertcart 镜像同码（旁证）。
- 价格行：B&H 自营 **$346.00**，InStock，Add to Cart；ASUS 美国官网 $359.99，InStock。
- 待定项：无标识待定；仅入目录时重验 live 价。

## 6. asus-tuf-gaming-m3-gen-ii-black

- 品牌：ASUS ／ 型号：TUF Gaming M3 Gen II Wired Gaming Mouse，Black（P309）
- 新 key：`asus-tuf-gaming-m3-gen-ii-black`
- 队列标注：第六批后备队列；目录无 M3 Gen II（仅有 TUF M4 Air 与 TUF K3 Gen II），不撞号。
- MPN：`90MP0320-BMAA00`（美版；B&H MFR # + ASUS eShop 美国一致）。注意勿与非美版 `90MP0320-BMUA00`（EAN 4711081909118，欧洲/新加坡渠道）混同；另 eShop 美国另有一页 Part Number 为 `90MP0320-BMAA03`，性质未明（疑似替换 SKU/套装），入目录时复核 BMAA00 vs BMAA03。
- UPC：**pending**。唯一线索 `195553909112`（NationalPC 印度站单源，校验位有效），无第二来源；EAN 4711081909118 绑定的是非美版 BMUA00，不能转作美版 UPC。
- 价格行：Adorama 自营 **$25.99**，InStock（JSON-LD，标题 Black）。ASUS eShop $24.99 缺货、B&H 已停售（No Longer Available，旧价 $28.64），均不用作主价行。
- 待定项：① UPC 无第二来源；② BMAA00 vs BMAA03 待入目录时复核；③ 59g/8000 DPI 有线入门鼠，价位低但为 TUF 主流型号。

## 7. 8bitdo-sn30-pro-hall-effect-g-classic

- 品牌：8BitDo ／ 型号：SN30 Pro Wireless Controller with Hall Effect Joysticks，G Classic（Model 80DJ04）
- 新 key：`8bitdo-sn30-pro-hall-effect-g-classic`
- 队列标注：deal-site 补位（Slickdeals frontpage + DealMoon）；目录无任何 8BitDo 款，不撞号。
- MPN：`80DJ04`（Best Buy Model 栏；灰色款为 80DM02，不同款）。注意 Best Buy 存在两个 G Classic SKU（6590319 与 10189263），同为 Model 80DJ04；本次以 Sold by Best Buy 的 6590319 页为准。
- UPC/EAN：**pending**。`6922621509547`（13 位 EAN，校验位有效），仅 Target 规格页一源（$44.99，InStock）；B&H 未见上架该款，无第二来源。Hall Effect 版与旧版（普通摇杆）同名，须以 "with Hall Effect Joysticks" + Model 80DJ04 钉死，不得与旧版混同。
- 价格行：Best Buy 自营（Sold by Best Buy）**$34.99**，InStock，Add to Cart，黑五价（对比价 $44.99）；Target $44.99，InStock，为第二价行。注：Best Buy 价在 11-04/11-12 抓取中为 $33.99，现已变为 $34.99，入目录时重验。
- deal-site 证据：Slickdeals frontpage 2026-11-04（$33.99 Best Buy）与 2026-11-12（$32.99 Amazon / $33.99 Best Buy，Amazon 价不用）；DealMoon 2026-11-13 前后 $33.99 Best Buy（Editor's Pick）；Slickdeals Threads 2026-11-13 $33 Best Buy。
- 待定项：① EAN 需第二来源（B&H 无货，可试 Adorama/Newegg 规格页）；② 两个 Best Buy SKU 的关系待入目录时确认。

## 8. microsoft-xbox-wireless-controller-forza-horizon-6-limited-edition

- 品牌：Microsoft ／ 型号：Xbox Wireless Controller，Forza Horizon 6 Limited Edition（半透明青 + 粉色握把，2026-05-19 上市）
- 新 key：`microsoft-xbox-wireless-controller-forza-horizon-6-limited-edition`
- 队列标注：deal-site 补位（Slickdeals frontpage 2026-11-19）；目录仅有黑色标准款 `xbox-wireless-controller-black`（verified，1914，196388518159），LE 为独立配色款，不撞号。
- MPN：`EP2-42276`（Walmart Model 栏、GameStop Vendor Part Number、Lenovo 美国 Manufacturer PN 三源一致）。
- UPC：**verified：`196388601059`**（校验位有效）。GameStop 美国零售商规格页（UPC 栏 + Vendor PN EP2-42276）+ goWholesale（分销商，同款 UPC+MPN）两源一致，符合零售商+分销商先例；另有 eBay 产品页同码（旁证，不用）。
- 价格行：Walmart 自营（sold/shipped by Walmart，Slickdeals 注明）**$49.00**，was $84.00；另有 Amazon $49.00（按规则不用作价格来源）。
- 待定项：① **LE 款定性请批示**：限量联名款但仍在 Walmart/Best Buy/GameStop 大面积有货、非清仓，是否纳入由批复定；② 入目录时重验 live 价（黑五促销价）。

---

## 剔除 / 暂缓的有名款及理由

- **ROG Strix Scope II 96 Wireless 白色 NX Snow 款（MPN 90MP037A-BKAA30）**：暂缓。美国 UPC 全网未找到（仅欧盟 EAN 4711387487082/4711387487112，绑定欧版件号 BKNA30/BKEA30），且与 Storm 白款（已带入）同色不同轴，须分开处理，不得把 Snow 的 EAN 当 UPC 用。
- **ROG Delta II-KJP（Kojima Productions 联名版，A703）**：剔除（非本次队列款）。与标准白款是不同型号（MPN 90YH04C0-BHUA10），Best Buy 挂 Clearance $188.99；不得与标准白款混同。
- **DualSense 各色翻新机（Slickdeals frontpage 2026-11-16，PlayStation Direct Certified Refurb $44 起）**：剔除，翻新机按规则排除；且白色标准款已在目录（sony-dualsense-white，pending）。
- **Corsair K70 CORE RGB 翻新机（Best Buy Refurbished Excellent $39.37）**：剔除，翻新机排除；且 K70 CORE RGB 黑色款已在目录（pending）。
- **Razer Basilisk V3 Pro 白色（Kart Deals  aggregator $39.99）**：暂缓。仅聚合器单源价格，无零售商实页佐证；且目录已有 Basilisk V3 Pro 35K 黑色款（pending），V3 Pro 非 35K 白款需另行核标识，未达本次带入标准。
- **8BitDo Pro 2 Hall Effect（Slickdeals frontpage $38，Amazon）**：暂缓。价格来源仅 Amazon（按规则不能作价格来源），未核到 Best Buy/B&H 自营价行与 UPC；SN30 Pro 已覆盖 8BitDo 缺口，Pro 2 留待后补。
- **MSI Forge GK110 + GM320 键鼠套装（Slickdeals $24.99，Amazon）**、**SABLUTE 键鼠套装（$16.79，Amazon）**：剔除。廉价套装、非主流单品，且价格来源仅 Amazon。
- **Xbox 标准款各色 $49（Walmart，Slickdeals 同帖）**：不单独立项。黑色标准款已在目录（verified）；其余标准配色未逐款核标识，不顺带带入。

## 目录撞号复核记录（2026-11-21）

- 方法：对 `catalog_ref_550.tsv` 全表 grep（key 子串 + 全部 MPN/UPC 字符串精确匹配）。
- 结果：8 个候选 key 子串（delta-ii-white、keris-ii-ace-white、scope-ii-96-wireless-white、bt8-3-pack、bt10-1-pack、m3-gen-ii、sn30-pro、forza-horizon-6）命中 0 行；19 个标识字符串（197105907362、197105907355、90YH03W0-BHAA10、90YH03W0-BHUA10、197105394612、197105394582、90MP03N0-BMUA10、197105487154、90MP037B-BKAA30、197105532090、BT8(W-3-PK)、197105429833、BT10(W-1-PK)、195553909112、90MP0320-BMAA00、6922621509547、80DJ04、196388601059、EP2-42276）命中均为 0。
- 同名黑色款对照（颜色不同款，不构成撞号）：Delta II 黑（pending，无标识）、Keris II Ace 黑（pending，无标识）、Scope II 96 无线黑（pending，无标识）、Scope II 96 RX 无线黑（pending）、BT8 2-pack（verified，UPC 197105532045）、BT10 2-pack（pending，线索 UPC 197105429895 单源）、Xbox 无线手柄黑（verified，UPC 196388518159）。
- 第七批已入款未重复：G305、G733、G915 X、G502 X 系列、Signature Slim K950、MX Master 4 各色、Huntsman V3 Pro Mini、Kiyo 系列已入款、BT8/BT10 2-pack——本次 8 款均不在其中。

## 待办（入目录时）

1. 5 款 pending UPC 按各款备注复核（Delta II 白美版 MPN/UPC、Keris 白 612 vs 582、Scope 白 Storm 需 Best Buy/B&H 规格页、M3 Gen II 需第二来源、SN30 Pro EAN 需第二来源）；冲突码一律不得二选一。
2. 全部 8 款重验 live 价与库存信号（多为黑五促销价，Delta II 白 $149.99、Scope 白 Storm $131.99、SN30 Pro $34.99、Forza LE $49.00 均可能变动）。
3. M3 Gen II 复核 BMAA00 vs BMAA03；Keris 白复核 eShop $94.99 是否覆盖白色。
