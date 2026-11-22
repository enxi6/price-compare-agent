# Track C — 第八批草稿：手机 / 平板 / 可穿戴（2026-11-21/22）

研究员：Track C。范围：Slickdeals Tech 今日热门 + Black Friday Sift + 第七批后备队列 3 款。
对照表：`data/rework8/catalog_ref_550.tsv`（550 款）。8 款候选的 key / 型号名子串（双向归一化）/ MPN / UPC 逐项 grep 对照，**全部无命中**（唯一子串命中是 `pro max` 撞 Anker `Soundcore Liberty 5 Pro Max`，不同品牌不同品类，不构成碰撞）。
未动 catalog.py、DECISIONS.md、快照、站点；未提交。

## 扫描结论

- Slickdeals Tech 今日前页（2026-11-22 00:00 UTC 抓取）：手机/平板/可穿戴极少。命中的只有 Apple Watch Ultra 3（Renewed，排除）、Oura Ring 5（Sam's Club，见备选）、AirTag 2nd Gen 4-pack（已入目录，排除）。其余为耳机/音箱/电视/配件。
- Black Friday Sift 前 96 条：命中的只有 Galaxy Tab A11+（已入目录，verified）和翻新 iPad 8th Gen（翻新+旧款，排除）。Sift 的 Apple Watch Ultra 3 多配置行（Best Buy $549）与 iPhone 17 Pro/Pro Max 行是本次候选的重要旁证。
- 因前页太薄，另做定向核查：Best Buy 黑五手机页（iPhone 17 Pro Max / iPhone Air / Galaxy Z Flip8 / razr ultra 2025 / Pixel 10 Pro / OnePlus 15）与 Slickdeals 站内搜索，补主流新款。

## 候选清单（8 款）

### C1. apple-watch-ultra-3-49mm-black-ocean-band
- 品牌：Apple；型号：Apple Watch Ultra 3 (GPS + Cellular, 49mm)，黑色钛金属 + Black Ocean Band。
- 新 key：`apple-watch-ultra-3-49mm-black-ocean-band`
- MPN：**已核实 MF0J4LW/A** —— Best Buy 实页（SKU 6572972，Model: MF0J4LW/A）+ Slickdeals 线程 + Costco 陈列（item 1874533）三方一致。
- UPC：**195950484311（多源一致，待加时在 Best Buy 规格页复核）** —— eBay 产品标识（GTIN 0195950484311）× 多条、PayMore 两家分店实物扫描（Derita / Spring，含序列号）、零售盒照片（盒标 UPC 1 95950 48431 1）。无品牌/零售商规格页文本可引——browser.open 的 Best Buy 文本抓取不含 UPC 字段。
- 价格行：**Best Buy $549.00（原价 $799.00，省 $250），自营，InStock，Add to Cart** —— browser.open 实页验证（2026-11-22 00:01 UTC），JSON-LD Product Offer: Price 549 USD / InStock。另有 Costco 门店 $449.97（仅限部分门店、不可在线核实，不作行）。
- deal-site 证据：Slickdeals 线程 `49mm Apple Watch Ultra 3 GPS+Cellular Titanium Case Smartwatch (Various)`（Best Buy from $549，2026-11-07）；Sift：同款 Black Ocean Band $549.00（Live 11-18 至 11-28）及多配置 $549/$649；MacRumors 黑五汇总、9to5Mac 11-04 均报 $549。
- 待定项：UPC 须在入目录前于 Best Buy 规格页（See all specifications > Other）复核；注意同页另有翻新行（Simple Cell $599.99）与 open-box 行，不得混用。

### C2. apple-iphone-17-pro-max-256gb-cosmic-orange
- 品牌：Apple；型号：iPhone 17 Pro Max 256GB（Unlocked），Cosmic Orange。
- 新 key：`apple-iphone-17-pro-max-256gb-cosmic-orange`
- MPN：**已核实 MFXH4LL/A** —— Best Buy 实页（SKU 6473213）+ PayMore 两条 listing 一致。注意与已入目录的 iPhone 17 Pro 256GB Silver（不同款）无 MPN 碰撞。
- UPC：**195950638004（多源一致，待加时在 Best Buy 规格页复核）** —— PayMore 两家分店实物扫描、BarcodesInc（GTIN 0195950638004）、eBay 产品标识、tekfeed 四方一致。BarcodesInc 单独不可作数，但此处另有两家实物扫描背书。
- 价格行：**Best Buy $1,099.99（原价 $1,199.99），自营，InStock** —— Sift + dealnews + Best Buy 搜索快照一致（最近 12 小时内抓取）。同页 open-box $1,011.99–$1,044.99 与翻新 $972.97+ 不得混用。
- deal-site 证据：Slickdeals Hot Deals 今日线程 `Apple - iPhone 17 Pro Max 256GB - Cosmic Orange (Unlocked) $1099`；Sift 同款 $1,099.99（Live 11-18 至 11-28）；dealnews 称 best-ever 解锁价。
- 待定项：UPC 入目录前须 Best Buy 规格页复核；颜色只钉 Cosmic Orange（Deep Blue / Silver 为不同 MPN，不在此款内）。

### C3. samsung-galaxy-z-flip8-256gb-graphite
- 品牌：Samsung；型号：Galaxy Z Flip8 256GB（Unlocked），Graphite。
- 新 key：`samsung-galaxy-z-flip8-256gb-graphite`
- MPN：**已核实 SM-F776UZKAXAA** —— Best Buy 实页（SKU 6681665，Model: SM-F776UZKAXAA）。注意 Verizon 版 MPN 不同（SM-F776UZKAVZW），不得混用；Pink 版为 SM-F776ULIAXAA。
- UPC：**pending，线索 0198957311260（单一经销商来源）** —— 仅 shop.databitinc.com 一家列出（Part # SM-F776UZKAXAA, UPC 0198957311260）。按规则无第二来源，留 pending；加时须在 Best Buy 规格页复核。
- 价格行：**Best Buy $999.99（原价 $1,199.99，省 $200），自营（Sold by Best Buy），InStock，Add to Cart** —— browser.open 实页验证（2026-11-22 00:01 UTC），JSON-LD Price 999.99 / InStock。同页另有 marketplace 行 $815.99–$1,239.84（open-box/第三方），只取 $999.99 自营行。
- deal-site 证据：Slickdeals Hot Deals 今日线程 `Samsung Galaxy Z Flip8 Unlocked Android Smartphone, 256GB Cream or Graphite $999.99`；Sift 未见此款，Best Buy 黑五手机页有售。
- 待定项：UPC 待第二来源；Cream 色为另一 MPN，不在此款内。

### C4. samsung-galaxy-tab-s10-fe-256gb-gray（第七批后备队列 ③）
- 品牌：Samsung；型号：Galaxy Tab S10 FE 10.9" Wi-Fi 256GB（12GB RAM），Gray，含 S Pen。
- 新 key：`samsung-galaxy-tab-s10-fe-256gb-gray`
- 碰撞检查：目录已有 `samsung-galaxy-tab-s10-fe-128gb-gray`（SM-X520NZAAXAR / UPC 887276992266，verified）；本款 MPN 与 UPC 均不同，**无碰撞**，是不同容量款。
- MPN：**已核实 SM-X520NZAEXAR** —— Best Buy 实页（SKU 11066617 / 6618940）+ 三星官方 MSRP 价目表（多版）一致。
- UPC：**pending，线索 887276992259（品牌官方价目表单一出版方）** —— 三星美国官方 Galaxy Tablet MSRP Price List，2025-03 / 2025-06 / 2025-09 / 2025-12 / 2026-03 / 2026-05 / 2026-06 / 2026-07 共 8 版均列 `SM-X520NZAEXAR … 12+256GB (Wi-Fi) Gray … 887276992259`。按项目先例（三星 MSRP 表单独来源只算线索，见 Watch7 40mm pending 注），留 pending；加时须在 Best Buy 规格页复核第二来源。注意 eBay 一条蓝色款 UPC 887276992273 是另一颜色（SM-X520NLBEXAR），不得混用。
- 价格行：**Best Buy $469.99（可比价 $669.99，省 $200，Black Friday Deal），自营（Sold by Best Buy），InStock，Add to Cart** —— Best Buy 搜索快照（SKU 6618940，4 天前与 1 天前两次抓取一致）。**加时必复核**：同产品页另有第三方 Merchant Expo LLC 行 $874.69（SKU 11066617）与 open-box 行 $422.99–$469.99，$469.99 必须确认为全新自营行才能写；三星官网 2026-08-13 曾显示 256GB $569.99，可作交叉参考。
- deal-site 证据：队列后备项（非当日 Slickdeals 热门）；smartprix 汇总同款 $469.99（Amazon 价不可作源，仅作信号）。
- 待定项：UPC 第二来源；$469.99 行加时复核（全新 vs open-box）。

### C5. motorola-razr-ultra-2025-512gb-pantone-scarab
- 品牌：Motorola；型号：razr ultra 2025 512GB（Unlocked），PANTONE Scarab。
- 新 key：`motorola-razr-ultra-2025-512gb-pantone-scarab`
- MPN：**已核实 PB770019US** —— Best Buy 实页（SKU 6625234）。注意另有 MPN PB250015US / XT2551-2（eBay 国际版 listing）与 PB770020US（snapklik，疑似另一颜色），均不得混用。
- UPC：**pending，标识冲突** —— 两方各执一词：Target Plus 第三方卖家 Mobile Advance 列 UPC **840023284427**（Scarab）；eBay 国际版 listing（MPN PB250015US）列 UPC **840023270826**（Scarab）；snapklik 把 840023284427 配给 MPN PB770020US。冲突未解，按规则直接降级为 pending，**两个号都不写入**，加时以 Best Buy 规格页为准。
- 价格行：**Best Buy $699.99（原价 $1,299.99，省 $600），自营，InStock** —— Best Buy 实页（SKU 6625234，Sold by Best Buy，多次抓取一致）。同产品另有 marketplace SKU 行 $1,510.88–$1,528.14 与翻新行 $589.97–$634.97，均排除。
- deal-site 证据：dealnews Best Buy 黑五手机汇总（razr ultra 2025 512GB $699，$600 off）；Slickdeals 站内 9-16 帖亦报 Best Buy $699.99。
- 待定项：UPC 冲突待解（须 Best Buy 规格页）；只钉 Scarab 色（Cabaret / Rio Red / Mountain Trail 各有不同 MPN）。

### C6. apple-iphone-air-256gb-space-black
- 品牌：Apple；型号：iPhone Air 256GB（Unlocked），Space Black（eSIM only，A3260）。
- 新 key：`apple-iphone-air-256gb-space-black`
- MPN：**已核实 MG184LL/A** —— Best Buy 实页（SKU 6473225）+ 零售盒照片（MG184LL/A, Space Black, 256GB, Model A3260）一致。
- UPC：**pending，线索 195950621303（单一来源）** —— 仅 BarcodesInc（GTIN 0195950621303）。按项目先例，条码聚合站单独不可作数，留 pending；加时须 Best Buy 规格页复核。
- 价格行：**Best Buy $799.99，自营，InStock** —— Best Buy 搜索快照（最近 1 天内两次抓取，JSON-LD Price 799.99 USD）。**加时必复核**：同款 Light Gold 行 $999.99（3 天前抓取）、Sky Blue $919.99，颜色间价差真实存在；页面另有 $699.99 字样（疑似连网激活价），**不得写入**，只取 $799.99 裸机解锁行；dealnews 11-04 称 $999.99 已过期。
- deal-site 证据：Slickdeals Hot Deals 今日线程 `BestBuy iPhone 17 Pro Max 1099 iPhone 17 pro 899 and IPhone air 799- (Unlocked)`；dealnews 11-04 曾报 Air 256GB $999.99（已降价）。
- 待定项：UPC 第二来源；$799.99 加时复核（裸机价 vs 激活价；Light Gold $999.99 是否同降）。

### C7. google-pixel-10-pro-128gb-obsidian
- 品牌：Google；型号：Pixel 10 Pro 128GB（Unlocked），Obsidian。
- 新 key：`google-pixel-10-pro-128gb-obsidian`
- MPN：**已核实 GA09887-US** —— Best Buy 实页（SKU 6637725 / 13188733）。硬件型号 G4QUR（pcguide 称 US model）与 Best Buy 的 GA09887-US 是两套编号体系，以零售商实页的 GA09887-US 为准。
- UPC：**pending，无线索** —— 检索未见任何可信 UPC（Best Buy 文本抓取不含 UPC；无第二来源）。加时须 Best Buy 规格页核查。
- 价格行：**Best Buy $999.00，自营（Sold by Best Buy），InStock** —— Best Buy 实页（SKU 6637725）。同页另有第三方行 $869.99（Platinum Supply Group）与翻新行 $465.99–$559.00，均排除。另有信号未核实：Google Store 黑五 $749（9to5Google / etagicon 引述，25% off）与 Amazon $749（Slickdeals 线程，Amazon 价不可作源），**加时须在 Google Store 实页复核 $749 再决定写哪行**。
- deal-site 证据：Slickdeals 线程 `$849 | 256GB Google Pixel 10 Pro XL at Amazon` 同帖列 Pixel 10 Pro 128GB Obsidian/Moonstone $749（Amazon）；Android Police 10-28 报 Amazon $749（$250 off）。
- 待定项：UPC 无线索；$749 行须 Google Store 实页复核，否则以 Best Buy $999.00 为行。

### C8. oneplus-15-12gb-256gb-infinite-black
- 品牌：OnePlus；型号：OnePlus 15 12GB RAM + 256GB（Unlocked），Infinite Black。
- 新 key：`oneplus-15-12gb-256gb-infinite-black`
- MPN：**已核实 CPH2749（北美版）** —— 多家北美经销商（Swiftronics / myworldphone）+ sekin.in（引 OnePlus 美国规格页）一致。注意 smartprix 列的 CPH2745 / CPH2747 / PLK110 为国际版，**不得混用**；512GB 版为另一配置。
- UPC：**pending，线索 6921815630302（单一转售商来源）** —— 仅 Swiftronics 一家列出（Brand New UPC 6921815630302）。无第二来源，留 pending；加时须 Best Buy / B&H 规格页复核。
- 价格行：**oneplus.com $799.00（原价 $899.99，码 EXTRA100 立减 $100），品牌直营** —— Slickdeals 线程 `OnePlus 15 12GB RAM 256 GB ROM Infinite Black $100 off`（sd-core，链 oneplus.com/us/oneplus-15）。**加时必在官网实页复核**（码是否仍有效、是否为裸机价；Best Buy 只有 512GB Sand Storm $999.99 行，256GB 未见 Best Buy 自营行）。
- deal-site 证据：同上 Slickdeals 线程；OnePlus 官方 Facebook 亦报 $799.99（$899.99 立减 $100，oneplus.com/us）。
- 待定项：UPC 第二来源；官网 $799 码价加时复核；注意 OnePlus 已宣布不再在北美发新机（sekin.in 8 月更新），15 为北美最后旗舰，库存风险须留意。

## 第七批后备队列三款处理结果

| 队列款 | 结果 | 结论 |
|---|---|---|
| 三星 Galaxy Watch Ultra 一代（47mm LTE，Titanium Gray） | **不带入** | MPN SM-L705UDAAXAA 已核实（Best Buy 实页）；UPC 887276873039 有 Abt（0887276873039）+ Ubuy 两源。**但无干净直营新品行**：Best Buy 实页（SKU 13173677，$479.99）为第三方 YY Wireless 售卖，非 Best Buy 自营；Abt 显示“no longer available”；三星官网已换 Ultra2。另 2024 旧款走第三方清仓，属排除口径。 |
| 三星 Buds2 Pro（White） | **不带入** | MPN 白色美版 SM-R510NZWAXAR（eBay 产品标识 + esurebuy 一致）、UPC 887276668741（同两源）；另有一条盒标 SM-R510NZAAXAR 未辨颜色，留有疑问。**但无干净直营新品行**：B&H / Best Buy / 三星官网均无新品直营 listing；仅见小转售商（azorts $69.95 已售罄、amaax、nuq 全售罄）、Swappa 二手、2024 年旧 Slickdeals Amazon 帖。2022 年旧款、已被 Buds3 Pro / Buds4 Pro 迭代，属清仓旧款排除口径。 |
| 三星 Tab S10 FE 256GB（Gray） | **带入，见 C4** | MPN SM-X520NZAEXAR 已核实；UPC 线索 887276992259（三星官方价目表，pending）；Best Buy $469.99 自营行（加时复核全新 vs open-box）。与目录 128GB 款 MPN/UPC 均不同，无碰撞。 |

## 剔除 / 未入选（有名款及理由）

- **Apple Watch Ultra 3（Renewed，Amazon $500.46）**：翻新机，排除。**新品**同款已入选 C1。
- **Oura Ring 5 Silver Size 9**：备选未入 8 款。MPN JZ90-61403-09 已核实（Best Buy + noon + Noel Leeming + eBay 四方一致）；但 **UPC 全无线索**（eBay 标“UPC: Does Not Apply”；仅 Brushed Silver 9 号有一条液化商 POS 截图的 13 位码 6430060157224，单一弱源且颜色不同）；价格 Sam's Club $299 为会员价且另有 $40 Sam's Cash（干净价 $299 可用但须会员）；按尺码×颜色分款（6–13 号 × 多色），单款覆盖面窄。建议留作后备，待 UPC 有第二来源再议。
- **Galaxy Tab A11+ 128GB（Costco $199.99，Sift 161 saves）**：已入目录（verified，SM-X230NZAIXAR），重复，排除。
- **Apple AirTag 2nd Gen 4-pack（Walmart $69.99）**：已入目录（verified，MFEA4LL/A），重复，排除。
- **翻新 iPad 8th Gen（Newegg $117.99，Sift）**：翻新 + 2020 旧款，排除。
- **Galaxy S25 Ultra 256GB**：当日所见全为翻新行（eBay $592–$596 refurb、Woot NEW 512GB $899.99 未核实实页自营行与 MPN/UPC），无已核实的全新直营行，不入选；可作下一批 overflow。
- **Galaxy Z Fold8（Best Buy $1,600）**：dealnews 黑五汇总提及，未核实 MPN/UPC 与实页行，不入选；overflow。
- **Pixel 11 Pro（Google Store $799，25% off 信号）**：新当季旗舰，未核实 MPN/UPC，不入选；overflow（与 C7 的 Pixel 10 Pro 不冲突，不同代）。
- **iPhone 17 256GB（基础款）**：Best Buy 所见仅翻新行（$719.97–$879.99），未见已核实的全新解锁行，不入选。
- **Galaxy S25（基础款）**：未核实具体直营行与标识，不入选。
- **Shokz OpenDots 2（Amazon $119.97，Tech 前页）**：耳机类，非 Track C 核心（手机/平板/手表），且 Amazon 价不可作源；未核查。
- **Sennheiser Momentum True Wireless 4（Amazon $149.98）**：同上，耳机类；且 MTW4 已在目录处理中。
- **运营商分期价一律排除**：T-Mobile iPhone 17 / 17e（36 期账单抵扣）、AT&T iPhone 17 Pro（$31/月 + $500 礼品卡）等均不算干净行，未采纳。
- **eBay 全系**：S25 Ultra 翻新、iPhone 17 Pro 翻新等 eBay 行一律排除（平台第三方/翻新）。

## 标识 tally（8 款候选）

- MPN 已核实：**8 / 8**（全部来自 Best Buy 实页或品牌/北美经销商一致确认）。
- UPC 已核实（多源一致，含实物扫描 + eBay 产品标识 + 盒标照片；仍须加时 Best Buy 规格页复核）：**2 / 8** —— C1 Ultra 3（195950484311）、C2 Pro Max（195950638004）。
- UPC pending（有线索，单一来源）：**4 / 8** —— C3 Flip8（0198957311260，Databit 经销商单源）、C4 Tab S10 FE 256（887276992259，三星官方价目表单一出版方）、C6 iPhone Air（195950621303，BarcodesInc 单源）、C8 OnePlus 15（6921815630302，Swiftronics 单源）。
- UPC pending（标识冲突）：**1 / 8** —— C5 razr ultra（840023284427 vs 840023270826，两个号都不写）。
- UPC pending（无线索）：**1 / 8** —— C7 Pixel 10 Pro。
- 目录碰撞：**0**（key / 型号子串 / MPN / UPC 逐项 grep，全部无命中）。

## 加时复核清单（入目录前必做）

1. 全部 8 款的 UPC 在 Best Buy 规格页（See all specifications > Other）复核；C5 以规格页为准解冲突，C7 从零找。
2. C4 的 $469.99 确认为 Best Buy 全新自营行（非 open-box / 非 Merchant Expo 第三方行）。
3. C6 的 $799.99 确认为裸机解锁价（非 $699.99 连网价）；Light Gold $999.99 是否同降。
4. C7 的 Google Store $749 在官网实页复核，再定写 $749 还是 Best Buy $999.00。
5. C8 的 oneplus.com $799（码 EXTRA100）官网实页复核。
6. C1 / C2 的 UPC 虽多源一致，仍以 Best Buy 规格页为准做最终确认。
