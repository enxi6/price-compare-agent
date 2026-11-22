# Track D — 电视 / 音箱 / 显示器（第八批草稿）

研究员：Track D · 日期：2026-11-21（PT）· 对照表：`data/rework8/catalog_ref_550.tsv`（550 款）
方法：每款先对照 catalog 查 key、型号名子串（双向归一化）、MPN、UPC，撞任何一项即剔除；标识在品牌/零售商实页核（browser.open 文本抓取、Best Buy 规格页、品牌官网规格页/公开产品 JSON、制造商规格 PDF）；UPC 是唯一门，MPN 单独扶正为 0，无第二来源就 pending，绝不编标识；只认商家自营，美版货；Amazon 独家价不作价格来源；eBay/翻新/清仓旧款排除。

## 候选清单（9 款）

### 已核实 MPN + UPC（6 款）

#### 1. samsung-s90h-65 — Samsung S90H 65" OLED
- 品牌/型号：Samsung S90H 65"（2026 OLED，QN65S90H）
- MPN：**QN65S90HAEXZA**（已核实：Crutchfield MFR #；Samsung 2026 规格表；Best Buy 页面 Model 栏）
- UPC：**198957270574**（已核实：QVC 技术规格表 PDF + manuals.plus 收录的 Samsung 规格表，两源一致指向 QN65S90H）
  - ⚠️ 冲突记录：fillion.ca（加拿大零售商）给同一型号列 198957276095，单源、疑似区域变体 UPC，不采用；加时复核须以 Best Buy 规格页 "Other" 栏为准。
- 价格行：Best Buy **$1,399.99**，Sold by Best Buy，Add to Cart，InStock（2026-11-21 抓取；Black Friday 价，comp. value $2,699.99）；Costco 同价 $1,399.99 为含 Allstate 保护计划的 bundle，不作主行；Sam's Club 55" $1,197.99（不同尺寸，仅参考）。
- deal-site 证据：Slickdeals Black Friday Sift（Costco 77" $1,899.99 / 65" $1,399.99；Sam's 55" $1,197.99 / 77" $1,997.99），Sift 排名靠前。
- 撞表检查：key、"S90H"、MPN、UPC 在 550 款中均无撞。
- 待定项：UPC 冲突项加时再核一次。

#### 2. lg-oled-evo-c6-65 — LG OLED evo C6 65"
- 品牌/型号：LG OLED evo C6 65"（2026，OLED65C6PUA；注意 LG 官网另有 OLED65C6WUA 变体，Best Buy 行用 PUA）
- MPN：**OLED65C6PUA**（已核实：Best Buy Model 栏，SKU 6673112）
- UPC：**195174137666**（已核实：B&H 产品页 + EnergyStar 认证清单（OLED65C6PU* 家族）+ Value Electronics + Amazon + Adorama，五源一致）
  - 注：EnergyStar 同时列 195174137703（PU* 家族另一后缀变体）；Visions 加拿大列 OLED65C6PUA.ACC / 195174137673，区域变体，不混用。
- 价格行：Best Buy **$1,399.99**，Sold by Best Buy，Add to Cart，InStock（2026-11-22 00:02 UTC 实页抓取；Black Friday 价，comp. value $2,699.99）；Walmart 同价 $1,399.99（Slickdeals 线索）；Sam's Club 65" $1,399.99 / 77" $1,999.99（Sift）。
- deal-site 证据：Slickdeals Sift（Sam's 65"/77"）+ Slickdeals 帖 Best Buy $1,499.99→现 $1,399.99。
- 撞表检查：key、"C6"、MPN、UPC 均无撞。
- 待定项：无。

#### 3. samsung-hw-q990h-black — Samsung HW-Q990H 11.1.4ch Soundbar
- 品牌/型号：Samsung Q-Series HW-Q990H（2026 旗舰，11.1.4ch + 无线低音炮 + 后置）
- MPN：**HW-Q990H/ZA**（已核实：Samsung US 官网 + Best Buy Model 栏，SKU 6670431）
- UPC：**198957269394**（已核实：Walts 零售商规格页 + Amazon 产品页，两源一致）
- 价格行：Best Buy **$1,497.99**（Sold by Best Buy）；Samsung US $1,499.99。Woot $857.99 不采用：Deal Guy 等帖指出该 listing 疑似国际版/平行货，且 Woot 价未经自营身份核实。
- deal-site 证据：Slickdeals Sound Bar 页置顶（Woot $857.99，by pennysave）+ Sift 亦有 Best Buy 行。
- 撞表检查：key、"Q990H"、MPN、UPC 均无撞（目录仅有 HW-Q990F pending，是上一代）。
- 待定项：无。

#### 4. jbl-cinema-sb580-black — JBL Cinema SB580 3.1ch Soundbar
- 品牌/型号：JBL Cinema SB580（3.1ch，Virtual Dolby Atmos，无线低音炮，440W；JBL 官网：manufactured from 2024 until now）
- MPN：**JBLSB580BLKAM**（已核实：Crowdfused、goWholesale、VIP Outlet 产品名一致）
- UPC：**050036408530**（已核实：Crowdfused 型号/UPC 表 + goWholesale "JBLSB580BLKAM - 050036408530" + VIP Outlet SKU VIP050036408530MN，三源一致）
- 价格行：Walmart **$199.00**，Sold and shipped by Walmart.com，InStock（Slickdeals + Walmart 实页；原价 $289）。
- deal-site 证据：Slickdeals Sound Bar 页（Walmart $199，31% off）。
- ⚠️ 旗标：2026-09 至 11 月多条社交帖称部分 Walmart 门店 in-store clearance 低至 $50（与线上 $199 常规价并存）；线上行目前正常，但加时须复核线上价/库存是否仍在。
- 撞表检查：key、"SB580"、MPN、UPC 均无撞。
- 待定项：加时复核 Walmart 线上价。

#### 5. samsung-smart-monitor-m70f-43-black — Samsung Smart Monitor M70F 43"
- 品牌/型号：Samsung Smart Monitor M7 M70F 43" 4K（LS43FM702UNXZA，黑色；与已入的 32" 白 LS32FM703UNXZA 不同尺寸 = 不同款）
- MPN：**LS43FM702UNXZA**（已核实：Samsung US + Best Buy Model 栏，SKU 6632216 + Abt）
- UPC：**198957005435**（已核实：camelcamelcamel ASIN B0F5VLWQY6 + DataVision + LayawayLand，三源一致）
- 价格行：Samsung US **$499.99**；Abt **$499.99** InStock。Best Buy $399.99 但挂 Clearance 标，仅作参考价、不作主行。
- ⚠️ 旗标：Best Buy 清仓 $399.99 + Amazon 清仓 $279.99 帖（2026-11-17）并存，显示该尺寸可能进入清仓通道；Samsung US/Abt 仍为常规价。加时须复核 Samsung US 价与库存。
- 队列标注：队列款，达标带入。
- 撞表检查：key、"LS43FM702UNXZA"、UPC 均无撞（目录仅有 32" M70F）。
- 待定项：加时复核是否仍为常规在售（非清仓）。

#### 6. samsung-odyssey-g73sh-32-black — Samsung Odyssey OLED G7 G73SH 32"
- 品牌/型号：Samsung Odyssey OLED G7 G73SH 32" 4K 165Hz/1080p 330Hz 双模（2026）
- MPN：**LS32HG732SNXZA**（已核实：Costco Item 2084100 Model 栏 + Samsung 促销条款 Exhibit A + Samsung US）
- UPC：**198957301674**（已核实：Micro Center + Walts + eBay + MonitorPug，四源一致）
- 价格行：Costco **$699.99** + $100 Costco Shop Card（Slickdeals 帖 by shivster1796；Costco 实页 Item 2084100）；Samsung US $1,099.99（list）。
- deal-site 证据：Slickdeals Monitor Deals 置顶（Costco $699.99 + $100 卡）。
- 撞表检查：key、"G73SH"、MPN、UPC 均无撞。
- 待定项：无（注：Costco 价含 $100 礼卡，净价口径加时再定）。

### MPN 已核实、UPC pending（3 款）

#### 7. tcl-qm6k-pro-65 — TCL QM6K Pro 65"
- 品牌/型号：TCL QM6K Pro 65" QD-Mini LED（2025，Costco 专供变体，NFL 联名包装）
- MPN：**65QM6K Pro**（已核实：Costco Item 9565676 Model 栏）
- UPC：**pending**——冲突未解：TCL 制造商规格表（1worldsync/NFM）给 65QM6K（非 Pro）列 846042032155；Amazon/HiBid 给同一 65QM6K 列 846042043069；两者皆非 Pro 变体 UPC，Pro 自身 UPC 无线索。两码均不得写入。
- 价格行：Costco **$599.99**（价至 11/25/26；一次抓取显示 OutOfStock，另一次显示 $599.99，库存信号不稳）；Slickdeals 帖：$499.99（11/27–11/30，线上 11/26 起），75" $699.99 / 85" $899.99。
- deal-site 证据：Slickdeals Sift 113 saves（全场 TV 类最高之一）+ 专帖。
- 撞表检查：key、"QM6K"、MPN 均无撞。
- 待定项：UPC（Pro 变体）、加时复核 Costco 库存与 $499.99 是否兑现。

#### 8. hisense-qd7-55 — Hisense QD7 55"（Costco 专供）
- 品牌/型号：Hisense QD7 Series 55" Hi-QLED Fire TV（2026，Costco 专供型号 55QD75SFC；注意与 Best Buy 的 75QD7QF 等 2025 QD7QF 系列不同型号）
- MPN：**55QD75SFC**（已核实：Costco Item 9655750 Model 栏 + Hisense 规格 PDF）
- UPC：**pending**——唯一线索 888143028279 仅见于 Hisense 官方规格 PDF（Costco gdx-assets 托管），无第二来源，按规则留 pending（与 U7900H 规格表单源先例同口径）。
- 价格行：Costco **$269.99**（价至 11/30/26；costcodrops 2026-11-21 11:50 AM PST 查核 in stock；Costco.com 一次抓取显示 OutOfStock，库存信号 mixed）；仓库价亦 $269.99。
- deal-site 证据：Slickdeals Sift（Costco 55" $279.99→现 $269.99；100" $999.99）。
- 撞表检查：key、"QD7"、MPN 均无撞。
- 待定项：UPC 第二来源、加时复核 Costco 库存。

#### 9. asus-rog-strix-xg27ucgr-black — ASUS ROG Strix XG27UCG Gen2（XG27UCGR）27"
- 品牌/型号：ASUS ROG Strix XG27UCG Gen2（XG27UCGR），27" 4K 双模（4K 162Hz / FHD 485Hz），Fast IPS
- MPN：**XG27UCGR**（已核实：ROG US + ASUS eShop；ASUS 内部件号 90LM0CS0-B013B2；白色变体 XG27UCGR-W / 90LM0CS2-B013B2，$429，须区分）
- UPC：**pending**——无任何 UPC 线索（全网检索无结果）。
- 价格行：ROG US / ASUS eShop **$399**，InStock（ROG US JSON-LD）；Staples $449 InStock；Target $425.99。Amazon $319 帖（PCGuide，11/05）为 Amazon 价，不作行。
- 队列标注：队列款，达标带入（UPC pending）。
- 撞表检查：key、"XG27UCGR"、MPN 均无撞；须与已入的 XG27UCG（UPC 197105564633，CompSource + Adorama）严格区分，不得借用其 UPC。
- 待定项：UPC。

## 备选（MPN 已核实、UPC pending，未进 9 款；按需替换）

### A1. asus-rog-strix-xg27ucsr-black — ASUS ROG Strix XG27UCS Gen2（XG27UCSR）27"
- MPN **XG27UCSR**（ROG US + Best Buy Model 栏，SKU 12697071；ASUS 件号 90LM0CK0-B01171）。UPC pending：无美国 UPC 线索，仅有欧盟 EAN 4711636242929（Xcellent PC / ASUS brochure），**不得作 UPC 用**。
- 价格行：ROG US **$399** InStock；Best Buy 有 listing（JSON-LD $510.70，卖家身份不明，不作行）；Smartprix $299.99 为 Amazon 价，不作行。
- 队列标注：队列款。UPC 冲突说明：此前"冲突"实为 XG27UCG 的 UPC 197105564633（Adorama 明列于 XG27UCG 规格页）被误挂到 UCSR 名下；UCSR 自身无 UPC，不是两码打架，是零码。
- 撞表检查：key、"XG27UCSR"、MPN 均无撞。

### A2. asus-rog-strix-oled-xg27aqwmg-black — ASUS ROG Strix OLED XG27AQWMG 27"
- MPN **XG27AQWMG**（ROG US + ASUS eShop；件号 90LM0BZ0-B011B3）。UPC pending：无线索。
- 价格行：ROG US / ASUS eShop **$649** InStock；Amazon $399.99（Slickdeals 帖 by shivster1796）为 Amazon 价，不作行。
- deal-site 证据：Slickdeals Monitor Deals（Amazon $399.99）。2025-11-06 上市，MSRP $599，Tandem WOLED 280Hz。
- 撞表检查：key、"XG27AQWMG"、MPN 均无撞。

### A3. asus-tuf-gaming-vg27aq1a-black — ASUS TUF Gaming VG27AQ1A 27"
- MPN **VG27AQ1A**（ASUS US）。UPC pending：无线索。⚠️ 不得借用旧款 VG27AQ 的 UPC 192876306444（Adorama，属 VG27AQ 非 1A）。
- 价格行：ASUS US **$229** InStock；Amazon $229（vaagame  tracker）。
- 队列标注：队列款。QHD 170Hz IPS，仍在售的主流预算款。
- 撞表检查：key、"VG27AQ1A"、MPN 均无撞（目录仅有 VG27AQ3A 已核实）。

### A4. tcl-s55h-black — TCL S-Class S55H 2.1ch Soundbar
- MPN **S55H**（Best Buy Model 栏，SKU 6580778）。UPC pending：无线索。
- 价格行：Best Buy **$99.99** 新品（Black Friday 价，comp. value $159.99）；open-box $65.99–$69.99 不作行。
- deal-site 证据：Slickdeals Sound Bar 页（Best Buy $99.99）。
- 撞表检查：key、"S55H"、MPN 均无撞。

### A5. tcl-27g64-black — TCL 27G64 27" QD-Mini LED 显示器
- MPN **27G64**（TCL US + Best Buy Model 栏，SKU 6650390 + Walmart）。
- UPC：**846042043243**（MonitorPug + gamingmonitor.top 两源一致；⚠️ OnBuy UK 列 792257818483，疑似区域变体/错码，不采用；加时须以 TCL 规格表或 Best Buy 规格页再核）。
- 价格行：TCL US **$249.99**（官网直营）；Walmart $279.99（Slickdeals 帖 by Frugie）。
- deal-site 证据：Slickdeals Gaming Monitor 页（Walmart $279.99）。
- 撞表检查：key、"27G64"、MPN、UPC 均无撞。
- 未进 9 款原因：UPC 仅两家聚合站一致、有一家冲突，为稳妥列备选第一顺位。

## E6SR 50" 复查结论（第七批剔除款，重新核查 2026-11-21）

**结论：仍不达标，继续留队列，不得硬塞。**

- Best Buy：无 50E6SR listing。50" Hisense 2026 在售行是 **50QD6SR**（$249.99，SKU 6684438）与 **50M7SR**（$249.99），均为不同系列型号，不得替代。
- Walmart：无 50E6SR 新品行；仅有一条 **Restored 55E6SR**（$269.95，翻新、且为 55" 不同尺寸），双重排除。
- hisense-usa.com：本次检索未出现 E6SR 产品页（无 50E6SR 官方 listing 信号）。
- MPN：仍仅 Smartprix 单一非合格源（50E6SR $247.98，2026-08 价），无品牌/零售商实页佐证。
- UPC：仍无任何线索。
- 65" E6SR（65E6SR）：不同尺寸，未作替代核查，按任务要求单独处理，留待以后。
- 后续：下次复查时顺带核 50QD6SR / 50M7SR（本次仅发现、未核标识）。

## 队列逐款结果

| 队列款 | 结果 |
|---|---|
| 三星 G6 G60SD 27"（LS27DG602SNXZA） | **剔除**。UPC 887276832579 已核实（Walts + DirectDial + DGXTech + McNain + Visions 多源一致），MPN 已核实；但 Best Buy 实页（2026-11-22 00:01 UTC 抓取）显示 "This item is no longer available in new condition"，且 2026-11-17 Deals Guy 帖称 Best Buy 清仓 $179.99（原 $899.99）。清仓 + 停售新品，无直营新品行，按清仓旧款规则排除。 |
| 三星 G8 G80SD 32"（LS32DG802SNXZA） | **剔除**。MPN 已核实（Best Buy Model 栏，SKU 6573686）；Best Buy 挂 Clearance 标 $1,169.99（comp. value $1,299.99），一次抓取显示 Unavailable；Samsung EPP $666 为 gated 价。2024 款清仓中，无常规直营行，按清仓旧款规则排除；UPC 未再追（已剔除无需）。 |
| 三星 HW-B650 旧款（HW-B650/ZA） | **剔除**。Best Buy Clearance $359.99（comp. value $399.99），Sold by Best Buy；open-box $261.99–$278.99。旧款清仓，且已被 HW-B650F（已入目录，Best Buy $199.99 Black Friday 价）取代；不得与 HW-B650F 混淆。 |
| 三星 M70F 43"（LS43FM702UNXZA） | **带入，候选 #5**（MPN + UPC 已核实；见上）。 |
| 华硕 XG27UCSR | **带入，备选 A1**（MPN 已核实，UPC pending；EU EAN 不得用）。 |
| 华硕 XG27UCG Gen2（XG27UCGR） | **带入，候选 #9**（MPN 已核实，UPC pending）。 |
| 华硕 VG27AQ1A | **带入，备选 A3**（MPN 已核实，ASUS US $229；UPC pending；不得借 VG27AQ 的 UPC）。 |
| 华硕 VG279QM5F | **留队列**。ASUS US 标 $199 但无确认的直营在库行（Smartprix：Out of Stock，仅 Amazon $199）；MPN 90LM0D81-B01171 仅埃及零售商单源；无 UPC 线索；⚠️ 不得借用旧款 VG279QM 的 UPC 192876505939（camelcamelcamel，属 2020 款 VG279QM）。 |
| 联想 ThinkVision P27u-20 | **留队列**。MPN 62CBRAR6US + UPC 195713542920 已核实（Howard + Tech-America + Bonanza + SimplifiedComputers 多源一致）；但为 2021 年款（首发 2021-08-29），多数直营/分销商处 backordered/out-of-stock，Best Buy 仅 marketplace 卖家行，无品牌直营在库行。⚠️ 另有件号 62F1RAR6US / UPC 196119196823 为另一配置，不得混用。 |

## 剔除的有名款及理由（Slickdeals 扫到的热门、未入选）

- **Samsung S90H 55"/77"**：与候选 #1 同系列不同尺寸；只取 65" 为代表款，不重复加尺寸。
- **LG G6 OLED 65"**（Best Buy $1,999.99）：Sift 热门但本次未核 MPN/UPC，留作后续线索；OLED65G6WUA 待核。
- **Sony BRAVIA 6 OLED 55"**（Costco $999.99，K55A60B 疑似）：未核标识，留作后续线索。
- **Samsung QN90H 75"**（Sam's $1,497.99）、**TCL QM8L 65"**（$999.99）、**Samsung M70H 65" TV**（Costco $379.99，Mini LED 电视、与 M70F 显示器不同线）、**Samsung U8000H**（Costco $299.99）、**Hisense QD5SF 98"**（Best Buy $799.99）、**TCL 98Q5CF**（Best Buy $999.99）、**LG QNED84BUA 75"**（Best Buy $799.99）：均为 Sift 热门，本次未核标识，留作后续线索；M70H 须注意与 M70F 显示器区分。
- **Samsung HW-Q930H**：仅 Best Buy open-box $762 行，无新品直营价，排除。
- **Samsung HW-Q60CF**（Costco $299.99）：未核标识，留作后续线索。
- **JBL Bar 500MK2**（Amazon $449.95）：仅 Amazon 价，无直营行佐证，不入选。
- **Samsung HW-B400F / HW-B750F**：仅 Amazon 价，不入选。
- **Sonos Ray**（Best Buy $169）、**Sonos Era 300**（Amazon $399）、**Sonos Era 100 SL**（Amazon $149）：Ray 有 Best Buy 行但本次未核标识；Era 300/100 SL 仅 Amazon 价；留作后续线索。
- **Samsung Odyssey G61SH 27"**（$384.99）、**G50SF 27"**（Samsung EPP $288，gated）、**G80SH/G80HS**（EPP gated）：EPP/EDU 门控价不作公开直营行；G61SH 未核 UPC。
- **ASUS ROG PG32UCDM3 32"**（Amazon $999.99）：仅 Amazon 价，未核标识；目录已有 PG32UCDM（已核实），须区分。
- **Roku Pro Series 55"/65" OLED**（$699.99/$799.99，Slickdeals Hot Deals 今日帖）：2026 新线但本次未核 MPN/UPC，留作后续线索。
- **Hisense 50QD6SR / 50M7SR**（Best Buy 各 $249.99）：E6SR 复查时发现的 50" 替代系列，未核标识，留作后续线索。
- **JBL Cinema SB550**（Walmart $159）：SB580 的低配款，本次未核标识；另 SB580 本身有门店清仓旗标（见候选 #4）。

## 标识 tally

- 候选 9 款：MPN 已核实 9/9；UPC 已核实 6/9，pending 3/9（QM6K Pro 冲突、QD7 单源、XG27UCGR 零线索）。
- 备选 5 款：MPN 已核实 5/5；UPC 已核实 1/5（27G64，带一家冲突待复核），pending 4/5。
- 队列 9 款：带入 4（M70F 43"、XG27UCGR、XG27UCSR、VG27AQ1A），留队列 2（VG279QM5F、P27u-20），剔除 3（G60SD、G80SD、HW-B650）。
- 本轮新发现的 UPC 冲突 3 起：S90H 65"（198957270574 vs fillion.ca 198957276095）、QM6K Pro（846042032155 vs 846042043069，皆属非 Pro）、27G64（846042043243 vs OnBuy 792257818483）。
- 本轮明确"不得借用"的跨型号 UPC 4 起：XG27UCG→XG27UCGR/XG27UCSR；VG27AQ→VG27AQ1A；VG279QM→VG279QM5F；QD7QF 系列→QD75SFC。

## 未动项声明

未动 catalog.py、DECISIONS.md、快照、站点；未提交。仅写本 findings 文件。
