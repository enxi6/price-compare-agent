# Track B — 第八批草稿：DealMoon 交叉验证 + 可穿戴 / 智能家居

- 日期：2026-11-21（PT 16:00 左右扫页；DealMoon 抓取时间 2026-11-22 00:00 UTC）
- 扫页范围：DealMoon Electronics & Computers 主页（全 840 行）+ Wearable 子类页 + Smart Devices 子类页
- 对照表：`data/rework8/catalog_ref_550.tsv`（550 款）。每款均做 key / 型号名子串（双向归一化）/ MPN / UPC 四项对照，见文末核查记录。
- 规则执行：UPC 是唯一门，MPN 单独扶正为 0；无第二来源即 pending，绝不编标识；只认商家自营；只认美版货；Amazon 独家价不作价格来源；eBay、翻新、运营商分期、清仓旧款排除。
- 未动 catalog.py、DECISIONS.md、快照、站点，未提交。

## 候选清单（8 款）

### 1. harman-kardon-soundsticks-5-white
- 品牌 / 型号：Harman Kardon SoundSticks 5 2.1-Channel Bluetooth Speaker with HDMI，白色（Clear / White）
- MPN：**HKSOUNDSTK5WAM2 —— 已核实**（B&H 商品页型号；Amazon 商品页 Model Number 一致）
- UPC：**050036422468 —— 已核实**（B&H 规格页 UPC 字段；Amazon UPC 一致；PicClick 一致）
- 价格行：**B&H $279.95（原 $349.95），InStock，Add to Cart，自营**（2026-11-22 文本抓取）。DealMoon 帖 Amazon 同价 $279.95，仅作 deal 信号。
- deal-site 证据：DealMoon 主页帖「Harman Kardon SoundSticks Bluetooth Speaker System 4th Gen $199, 5th Gen $279.95」（Amazon）；**Slickdeals 未见专帖**（本次检索仅命中 Onyx Studio 9 帖）。
- 目录对照：无撞款。目录无任何 SoundSticks；仅有 harman-kardon-onyx-studio-8-black（pending），型号/MPN/UPC 均不同。
- 待定项：黑色版 MPN HKSOUNDSTK5BAM2 已确认（Staples CA / Best Buy CA），但无美国 UPC（仅 APAC 版 EAN 1200130023729，对应 BAS2 后缀），且 B&H 暂无黑色版在售，故本批只推白色版；另注意勿与新出的 SoundSticks 5 Wi-Fi 版混淆（不同型号）。

### 2. harman-kardon-onyx-studio-9-black
- 品牌 / 型号：Harman Kardon Onyx Studio 9 Portable Stereo Bluetooth Home Speaker，黑色
- MPN：**HKOS9BLKAM —— 已核实**（Harman Kardon 美国官网 Item#；Amazon / Newegg / NeweggBusiness 一致）
- UPC：**028292291104 —— 已核实**（Amazon + Newegg + NeweggBusiness 三方一致；eBay 个别 listing 亦同）
- 价格行：**Newegg $219.50**（newegg.com 品牌店页标价；加行时须核实为 Newegg 自营而非 marketplace 卖家）。Harman Kardon 官网 $299.99 但 OutOfStock。DealMoon 帖 Amazon $158.89 仅作 deal 信号（Amazon 价不作价格来源）。
- deal-site 证据：DealMoon 主页帖「Harman Kardon Onyx Studio 9 Portable Bluetooth Speaker Black $158.89 *$186.99*」（Amazon）；**Slickdeals 有帖**：f/19817025，Woot $149.95（2026-07-28，已过期，仅作交叉验证）。
- 目录对照：无撞款。目录仅有 harman-kardon-onyx-studio-8-black（pending），型号/MPN（HKOS8BLKAM）/UPC 均不同。
- 待定项：eBay / Snapklik 流传的 UPC 610214681881 与 724129192612 为 eBay 生成码 / 翻新 listing 附带码，已排除，不采用；Newegg $219.50 行的自营身份待加行时复核。

### 3. garmin-venu-x1-black
- 品牌 / 型号：Garmin Venu X1 GPS Smartwatch，Black / Slate Titanium Caseback，黑色 ComfortFit 尼龙带
- MPN：**010-02980-00 —— 已核实**（Micro Center / CompSource / Petra / Dell / Bloomingdale's 一致）
- UPC：**753759342746 —— 已核实**（Micro Center 规格表 + CompSource UPC EAN 字段 + Petra UPC + eBay GTIN 0753759342746，四方一致）
- 价格行：**Best Buy $499.99（comp $699.99），自营**；Target $499.99；DealMoon 帖 Amazon $499.99（仅作 deal 信号）。另有 Garmin 官网 / Crutchfield $499.99。
- deal-site 证据：DealMoon Wearable 页帖「Garmin Early Black Friday Deals … Venu X1 $499.99 *$799.99*」（Amazon）；**Slickdeals 未见专帖**（本次检索无 slickdeals.net 结果命中）。
- 目录对照：无撞款。目录有 Venu 3 / Venu 3S / Venu 4（45mm/41mm），无 Venu X1；MPN 010-02980-00 与 UPC 753759342746 均不在目录。
- 待定项：尺寸口径——Best Buy 与 DealMoon 标题称 51mm，Garmin 官方规格为 46mm 表壳 / 2 英寸屏；key 暂不带尺寸（garmin-venu-x1-black），加行时以 Garmin 官方为准复核；Moss 色（010-02980-01 / UPC 753759342753）Best Buy 一度 Sold Out，本批只推黑色版。

### 4. oura-ring-5-size-8-silver
- 品牌 / 型号：Oura Ring 5 Smart Ring & Fitness Tracker，Silver，Size 8（2026）
- MPN：**JZ90-61403-08 —— 已核实**（Best Buy 商品页 Model 字段；Slickdeals 前页帖同款同价引用）
- UPC/EAN：**pending**。唯一线索为 13 位 EAN 6430060156975（Harvey Norman AU），属非美 EAN，不得当作美国 UPC 使用；Best Buy 抓取的规格文本未含 UPC 字段。
- 价格行：**Best Buy $299.00（comp $399.00，Save $100），Sold by Best Buy，InStock，Add to Cart**（黑五价；5 天前抓取曾为 $399.00）。DealMoon Wearable 页帖 Amazon $299.00（仅作 deal 信号）。
- deal-site 证据：DealMoon「Oura Ring 5 … $299.00 *$399.00*」（Amazon）；**Slickdeals 有帖**：前页 f/20339559「Oura Ring 5 Smart Ring, various colors from $299」+ Sift 黑五清单 Best Buy $299。
- 目录对照：无撞款。目录仅有 samsung-galaxy-ring-size-9-titanium-black（pending），品牌/型号/MPN 均不同。
- 待定项：① UPC 待加行时在 Best Buy 规格页（See all specifications > Other）复核，或等下一轮刷新；② 会员制：首月免费，之后 $5.99/月或 $69.99/年，价格行须注明首年价不含后续会员费；③ 需 sizing kit 先测尺寸，Size 8 为本次锚定尺码。

### 5. whoop-5-0-peak-obsidian
- 品牌 / 型号：WHOOP 5.0 Peak Health and Fitness Tracker，12-Month Membership，Obsidian（2025）
- MPN：**973-004-000 —— 已核实**（Best Buy 商品页 Model 字段；pricehistory.app Amazon 款 Model Number 一致）
- UPC：**pending——两线索冲突，不选**。线索 A：810114363317（manuals.plus，明确绑定 973-004-000）；线索 B：810114363270（SB Technology 分销商帖，称 5.0 Peak Obsidian）。另 MG 款 973-002-000 → 810114363300、973-003-000 → 810114363324 均与本款无关，不得挪用。
- 价格行：**Best Buy $199.00（comp $239.00，Save $40），Sold by Best Buy，InStock，Add to Cart**。DealMoon Wearable 页帖 Amazon $199.00（12-month 会员款）/$189.00（One 款）仅作 deal 信号；WHOOP 官宣黑五价 Peak $199（11-19 至 12-01）三方一致。
- deal-site 证据：DealMoon「WHOOP 5.0 … $199」；**Slickdeals 未见专帖**（本次检索无 slickdeals.net 结果命中）。
- 目录对照：无撞款。目录无任何 WHOOP。
- 待定项：① UPC 冲突待加行时以 Best Buy 规格页复核，复核不出即保持 pending；② 价格为会员捆绑价（12 个月 Peak 会员含设备），续费 $239/年，价格行须注明；③ 勿与 One 款（$189，Jet Black CoreKnit + 有线充）及 MG/Life 款（$299，ECG）混淆，本款为 Peak 档。

### 6. amazon-echo-dot-max-graphite
- 品牌 / 型号：Amazon Echo Dot Max（newest model / 2025），Alexa speaker，Graphite
- MPN：**B0D6SX8VLQ —— 已核实（Best Buy 美国页 Model 字段；另有一冲突码，见待定项）**
- UPC：**pending——多线索冲突，不选**。线索：840414628809（PBTech NZ，Graphite）、840414663176（Target，经 shoplooks 链接）、840414694620（PBTech NZ，White）、84041466007（Fred Meyer，White）。四码互斥，无一出自美国零售商规格页。
- 价格行：**Best Buy $49.99（Black Friday Deal，Save $70，comp $119.99），Sold by Best Buy，InStock，Add to Cart**——非 Amazon 直营行成立。DealMoon 帖 Amazon $49.99 仅作 deal 信号。
- deal-site 证据：DealMoon 主页 + Smart Devices 页帖「Echo Dot Max (Newest Model) $49.99 *$119.99*」（Amazon）；**Slickdeals 有帖**：f/19181425，Echo Dot Max $49.99（2026-02-06，select accounts，已过期，仅作交叉验证）。
- 目录对照：无撞款。目录有 amazon-echo-show-8-2025-glacier-white 与 amazon-echo-hub-white（第七批），型号名/MPN 均不同。
- 待定项：① MPN 冲突：PBTech NZ 将 Graphite 标为 B0DKLQD97R，与 Best Buy 的 B0D6SX8VLQ 不一致，暂以 Best Buy（美国零售商）为准，加行时复核；② UPC 待 Best Buy 规格页复核；③ 口径旗标：本款为智能音箱，Track B 括号称“智能家居（音箱/显示屏/门锁除外）”——若该除外指音箱类整体，则本款应剔除；本稿按“耳机/音箱类”重点收录，提请 parent 定夺。另注意 Alexa+ 需 Prime 会员或 $19.99/月订阅。

### 7. govee-smart-floor-lamp-3-black
- 品牌 / 型号：Govee Smart Floor Lamp 3（旗舰智能落地灯，LuminBlend+，2100 流明，Matter），黑色
- MPN：**H16B0 —— 已核实**（Govee 美国官网 Description 栏「Model: H16B0 (Black)」；Best Buy 商品页 Model: H16B0 一致）
- UPC：**pending，无线索**。Govee 不公开 UPC；Best Buy 抓取文本未含 UPC 字段；本次检索无任何 UPC 线索。不得用旧款 H6079（Floor Lamp Pro）冒充——H6079 是另一款灯。
- 价格行：**Govee 官网直营 $118.99（原 $169.99，黑五价）**，DealMoon 帖即引 Govee 直营；Best Buy $169.99（原价行）。Govee 官网另有翻新款 $144.49，已排除（翻新不入选）。
- deal-site 证据：DealMoon 主页 + Smart Devices 页帖「Govee Black Friday Sale … Floor Lamp 3rd Gen $118」（Govee 直营）；**Slickdeals 本次未跑专查**，无交叉结论。
- 目录对照：无撞款。目录无任何 Govee；无智能照明品类先例——本款为目录首款智能家居照明。
- 待定项：① UPC 待加行时在 Best Buy 规格页复核，复核不出即保持 pending；② 颜色口径：Govee 称 Black，Best Buy 称 Charcoal Gray，同为 H16B0，key 暂用 black；③ 勿与 Floor Lamp 3 Lite / Lantern Floor Lamp（均为 $129.99 新品）及旧款 Floor Lamp Pro H6079 / Floor Lamp 2 H607C 混淆。

### 8. amazon-echo-time-graphite
- 品牌 / 型号：Amazon Echo Time（all-new / 2026 release），Customizable smart clock，Graphite
- MPN：**B0FRPDXJYC —— 已核实**（Best Buy Graphite 款 Model 字段；Glacier White 为 B0GFY8SZTK，Coral Pink 为 B0GG1YNSPD，各色独立编码）
- UPC：**pending——仅弱聚合器线索且自相矛盾，不选**。bestpricescanner 同页两处分别给出 840414694712（Graphite）与 840414627574（标称 B0GFY8SZTK 实为白色款），无一出自零售商规格页。
- 价格行：**Best Buy $199.99（原价行）**；DealMoon 帖 Amazon $99.99（首次 50% off）仅作 deal 信号。
- deal-site 证据：DealMoon 主页 + Smart Devices 页帖「Echo Time (All-New) $99.99 *$199.99*」（Amazon）；**Slickdeals 本次未跑专查**，无交叉结论。
- 目录对照：无撞款。目录无 Echo Time；与 Echo Show 8 / Echo Hub 型号不同。
- 待定项：① UPC 待 Best Buy 规格页复核；② 口径旗标：本款带圆形显示屏，若 Track B“显示屏除外”按字面执行则应剔除；本稿按 Echo Show 8 / Echo Hub 已在第七批的同类先例收录，提请 parent 定夺；③ The Verge 等评测质疑 $200 定价过高，黑五 $99.99 为首降，价格波动大，加行时须重核 live 价。

## 标识 tally
- 候选 8 款；MPN 已核实 8/8，pending 0。
- UPC 已核实 3/8（SoundSticks 5 白、Onyx Studio 9 黑、Venu X1 黑）；pending 5/8（Oura Ring 5、WHOOP 5.0 Peak、Echo Dot Max、Govee Floor Lamp 3、Echo Time）。
- UPC pending 原因分布：冲突线索 3 款（WHOOP、Echo Dot Max、Echo Time）、仅非美 EAN 1 款（Oura Ring 5）、无线索 1 款（Govee Floor Lamp 3）。

## 备选（未入 8 款主清单，需 parent 定夺或下轮再核）
- **ray-ban-meta-gen-3-aviator-havana-brown-transitions**：DealMoon 主页帖 $529.00（Amazon）。Best Buy 有售：Model SK-1002183-01，$529.00，Sold by Best Buy；镜框型号 RW4016（盒标）。UPC 未找到；Slickdeals 本次未跑专查。目录对照：目录有 ray-ban-meta-gen-2-wayfarer-black（pending）、meta-ray-ban-skyler-gen-2-green-shiny-black（pending）、meta-oakley-meta-hstn-clear-black（pending），Gen 3 Aviator 与之型号名互不为子串，MPN SK-1002183-01 / RW4016 均不在目录，无撞款。未入主清单理由：MPN 口径未定（应取 Meta SKU SK-1002183-01 还是 Ray-Ban 框型 RW4016），且 UPC 全无，留作第一备选。
- **meta-nova-smart-glasses-honey-tortoise**：DealMoon Wearable 页帖，Meta 直营 $322.15（原 $479.00）。Meta 2026 新款智能眼镜，目录无 Nova。未核 MPN/UPC，留作备选。
- **ringconn-gen-2-smart-ring-size-8-rose-gold**：DealMoon Wearable 页帖 Amazon $199.50（原 $399.00），无订阅费智能戒。目录无 RingConn。未核 MPN/UPC；品牌小众，留作观察。
- **cmf-by-nothing-watch-3-pro / buds-2a / headphone-pro / speaker-s**：DealMoon Wearable 页帖，CMF BY Nothing 黑五最高 49% off（Watch 3 Pro、Buds 2a $19.99、Headphone Pro $49、Speaker S $39）。目录无 CMF。未核 MPN/UPC，预算品牌，留作观察。
- **ugreen-clipbuds-pro-2**：DealMoon 主页帖 Amazon $59.99（原 $99.99），开放式 AI 翻译耳机。目录无 UGREEN。未核 MPN/UPC，留作观察。

## 剔除的有名款及理由（均已对照 catalog_ref_550.tsv）
- **Samsung Galaxy Buds3 Pro（$99.99，DealMoon）**：型号名撞目录 samsung-galaxy-buds3-pro-silver（pending）——“Galaxy Buds3 Pro”子串命中，按规则剔除。另注：目录备注称唯一 UPC 887276868141 属白色版，不可挪用。
- **Shokz OpenDots 2（$132.95）/ OpenFit 2+（$132.95）**：Shokz 全系已在第七批，剔除。
- **Beats Solo 4（$79.99）/ Beats 360（$249.00）/ Beats Studio Pro（$139）**：Beats 已在第七批，剔除。
- **Apple Watch Series 12 GPS 42mm（$329.99）**：撞目录 apple-watch-series-12-42mm-gps-black（pending），剔除。
- **Samsung Galaxy Watch8 Classic 46mm（$349.99）**：撞目录 samsung-galaxy-watch8-classic-46mm-black（verified），剔除。
- **Amazon Echo Show 8（2025，$99.99）/ Echo Hub**：第七批已入，剔除。
- **Apple AirPods Pro 3 / AirPods Max 2（Starlight $419）**：撞目录 apple-airpods-pro-3（verified）/ apple-airpods-max-2（verified），剔除。
- **Samsung Galaxy Buds4 Pro（$169.99–$179.99）**：撞目录 samsung-buds4-pro-white（verified），剔除。
- **Garmin vívoactive 5（$168.00–$168.95）**：2023 旧款清仓价，目录已有 vívoactive 6（verified）；清仓旧款排除。
- **Harman Kardon SoundSticks 4（$199）**：2021 旧款（CES 2021），现为清仓价；现款为 SoundSticks 5。虽白版 UPC 028292287442 经 Best Buy 规格页核实，仍按清仓旧款剔除。
- **DJI Osmo Action 6 Essential Combo（$376）/ Action 4（$155.35–$199）**：撞目录 dji-osmo-action-6-essential-combo-black / dji-osmo-action-4-essential-combo-black（均为 pending），剔除；且相机不在 Track B 重点内。
- **Kindle Paperwhite 16GB Bundle（$139.99）/ Kindle Colorsoft（$169.99）**：撞目录 kindle-paperwhite-16gb-2024（verified）/ amazon-kindle-colorsoft-16gb-black（pending），剔除。
- **Ring Battery Doorbell / Indoor Cam、eufy C220 智能锁 / C31 / C37 摄像头、Reolink 门铃 / 摄像头**：智能家居安防不入选；目录无安防同类先例，全部剔除。
- **Insta360 X6（$629.99）/ X4 Air（$299.99）/ GO Ultra（$479.99）**：相机品类，不在 Track B 三大重点（可穿戴 / 智能家居 / 耳机音箱）内，未纳入；建议转其他 track。
- **Samsung Galaxy Z Fold8（$1,549.99 起）**：手机，不在 Track B 范围内，剔除。
- **Rokid Max 2（$179）/ AR Spatial（$359）**：小众 AR 眼镜，非主流，剔除。
- **Bee Frontier Wearable AI Device / Memoket Gem AI 录音手环（$159）**：小众 AI 穿戴，品牌与标识均弱，剔除。
- **Casio Moflin AI 宠物机器人（$343.20）**：非 Track B 品类，剔除。

## 方法与局限
- DealMoon 三页均于 2026-11-21 扫完；价格均为黑五促销价，加行时必须重核 live 价与库存信号。
- Best Buy 规格页文本抓取未返回 UPC 字段（Oura / WHOOP / Echo Dot Max / Echo Time / Govee 五款），UPC 均按 pending 处理；SoundSticks 5 白与 Onyx Studio 9 的 UPC 由 B&H / Newegg / Amazon 多方交叉核实，不依赖 Best Buy 抓取。
- Slickdeals 交叉：Onyx Studio 9、Oura Ring 5、Echo Dot Max 有帖；SoundSticks 5、Venu X1、WHOOP 5.0 Peak 未见专帖；Govee Floor Lamp 3、Echo Time、Ray-Ban Gen 3 本次未跑专查（见各款标注）。
