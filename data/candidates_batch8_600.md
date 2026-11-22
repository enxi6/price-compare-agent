# 第八批 50 款草稿（目标 600 款）

- 草稿日期：2026-11-21（PT）；分轨核查时点均为 2026-11-21/22 抓取
- 目录状态（入批前）：**550 款、已核实 229、pending 321、排名 169、matched 186、总报价 2,399**（HEAD 3ee2b63）
- 本批：**50 款**；入批后目录 550 → **600**（已核实 229 → 253，pending 321 → 347）
- 标识 tally：**MPN 已核实 44/50、UPC 已核实 24/50**；双标识已核实 24/50；pending 26/50
  - UPC pending 细分：有 lead 15（单源或弱源一致）、无线索 7、冲突未解 4
  - MPN pending 细分：单源 5、冲突未解 1（Delta II 白：美版/亚太版后缀冲突）
- 品牌计数（26 家）：ASUS 8、Samsung 7、DJI 4、Apple 3、Lenovo 3、Insta360 3、Amazon 2、Harman Kardon 2；Shokz、Beats、Skullcandy、Nothing、Garmin、Oura、WHOOP、Google、OnePlus、LG、JBL、Hisense、Alienware、HP、Dell、GoPro、8BitDo、Microsoft 各 1
- 品类计数（18 类）：laptops 8、phones 5、action-cameras 5、headphones 4、wearables 4、speakers 3、tvs 3、monitors 3、soundbars 2、drones 2、mice 2、routers 2、controllers 2、earbuds 1、smart-home 1、tablets 1、cameras 1、keyboards 1
- 来源拆分：**deal-site 缺口 35、队列顶位 15**
  - 队列顶位 15：华硕 8（Zephyrus G14、XG27UCGR、Delta II 白、Keris 白、Scope II 96 白、BT8 3-pack、BT10 1-pack、M3 Gen II）、三星 3（M70F 43"、Tab S10 FE 256GB、Book5 360）、联想 2（Legion Pro 7、LOQ）、Alienware 1（16 Aurora）、HP 1（OMEN Transcend 14）
  - deal-site 缺口 35：其余全部（Slickdeals Tech + Black Friday Sift 当日榜、DealMoon Electronics & Computers 交叉）
- 新品类提案：**drones**（Mini 5 Pro、Neo 2 各 1）——目录尚无 drones 品类；按第七批 tvs/phones/action-cameras 的先例，新品类须用户点头才入。
- 分轨文件：`data/rework8/trackA.md`（耳机/耳塞/音箱）、`trackB.md`（DealMoon 交叉 + 可穿戴/智能家居）、`trackC.md`（手机/平板/可穿戴）、`trackD.md`（电视/音箱/显示器）、`trackE.md`（笔记本）、`trackF.md`（运动相机/相机/无人机/配件）、`trackG.md`（华硕外设队列）。
- TSV：`data/rework8/candidates_batch8_50.tsv`（50 行）；membership 脚本：`data/rework8/membership_batch8.py`。

## 方法与口径（与第七批相同）

- 选品信号：Slickdeals Tech 当日榜 + Black Friday Sift 热榜（saves 数即需求信号）为主，DealMoon Electronics & Computers 交叉验证；只作 gap-check——候选款须不在现有 550 款目录里，且须在两边榜单反复出现。
- 骨架不变：品牌官网目录仍是选品与标识核实的骨架。标识规则不放宽：UPC 是唯一门，MPN 单独扶正为 0；无第二来源就 pending，绝不编标识。
- 报价资格：只认商家自营（品牌直营或零售商直售），平台第三方卖家行排除；只认美版货（美国 MPN/UPC、美国零售商/美店在售）。
- 排除：XREAL / Meta AI 眼镜（新品类）；Amazon 独家价不作价格来源；eBay/平台卖家、翻新机、运营商分期价、清仓旧款、PC 散件/套装、智能家居安防（目录无同类先例）。
- 前提如实报：550 款之后好找的主流款已接近见底；本批已核实率 24/50（48%）、队列顶位占比 15/50（30%），均按实测写，未为凑满 50 放宽规则。

## 协调裁决（7 项，分轨结论之上）

1. **Echo Dot Max 两轨重复，只计一次**：Track A 与 Track B 各自独立推了同一款（MPN B0D6SX8VLQ）。TSV 只留一行（track 标 A+B）。价格取 B 轨的黑五价 Best Buy **$49.99**（Save $70，comp $119.99），A 轨的 $119.99 为原价，不采用。UPC：A 轨未找到；B 轨找到 4 个互斥的聚合器码，无一出自美国零售商规格页——**一个都不写**。
2. **C1/C2 的 UPC 降为 pending-lead（协调降级）**：Track C 把 Watch Ultra 3（195950484311）与 iPhone 17 Pro Max（195950638004）的 UPC 计为“已核实”，依据是 eBay 产品标识 + PayMore 实物扫描 + 盒标照片 / BarcodesInc + eBay + tekfeed 多源一致。协调按严格口径降级：链上无一家品牌/零售商规格页（eBay 是平台、PayMore 是二手连锁、BarcodesInc/tekfeed 是聚合器），不符合“品牌或零售商实页”门。两码仍写进草稿作 lead，入目录时在 Best Buy 规格页复核后可升已核实——与第七批 M70F/IdeaPad 5 的加时升级同口径。
3. **SB580 与 M70F 43" 的 UPC 维持已核实（与 C1/C2 的区分）**：SB580（050036408530）有零售商 leg（VIP Outlet 的 SKU 嵌该 UPC）+ 两家分销商一致；M70F 43"（198957005435）有分销商 DataVision + 零售商 LayawayLand + camelcamelcamel 三源一致，与第七批 M70F 32" 升级（B&H + DataVision）同形。两者与 C1/C2 的区别是有零售商/分销商规格页背书，不只是平台与聚合器。
4. **智能家居口径**：Echo Dot Max（音箱）与 Echo Time（带屏智能钟）按第七批先例收录——Echo Show 8 / Echo Hub 已在目录、smart-home 品类已存在。安防类（门锁/摄像头/门铃）仍排除，目录无同类先例（Track B 已剔除 Ring/eufy/Reolink 全系）。
5. **Alienware 16 Aurora 的 HOLD 解除**：第六批的保留条件是“AntOnline 直营行不显示型号代码”；本次实页确认 AntOnline 页已印 Manufacturer Part Number LAC16250-7469BLU-PUS，条件满足。但 tier 保留旗标：AntOnline 是小零售商，且 $2,149.99 高于 Best Buy 已售罄的 $1,707.70；入目录时决定用 AntOnline 行还是等顶级渠道行。
6. **Book5 360 出队列**：MPN 本轮新核实（Best Buy + Quill + Connection + Staples 四源）；Connection $1,695.95 与 Quill $1,702.99 两行 live 且价一致；Best Buy 的 $358.99 清仓 vs $2,187.81 冲突仍在但两行均 Unavailable，已无关。Connection/Quill 均为 B2B 偏向零售商，非三星直营/Best Buy，入目录时确认 tier。
7. **无干净直营行者不入选（第六批先例）**：T16 21QN0045US 与 T14 Gen 5 Gray 虽双标识已核实，但无 live 直营行（T16 仅 marketplace/分销商行，T14 仅 B&H 停售 + Adorama 2027-01 到货），继续留队列。Legion 5i 仍留队列：Walmart 第三次撞机器人墙，且 UPC 198155802546 新发现冲突（PSREF 绑 83LY0000US，HowManyFPS/Ubuy 绑 83DF00AQUS）。

## 候选清单（50 款）

### 1. shokz-opendots-2-black — ✅ 已核实
- 品牌 / 型号：Shokz / OpenDots 2 Open-Ear Clip-On Earbuds（Black）
- MPN：E320-ST-BK-US —— B&H 商品页 URL slug + Abt 商品页，双源一致
- UPC：810202687523 —— B&H 规格页 + Abt 商品页，双源一致。另有一条冲突线索 Snapklik 810221005445（单源、非零售商），采信 B&H + Abt
- 价格行：B&H $139.95（原价 $199.95，Holiday Savings $60），In Stock，Add to Cart
- deal-site 证据：Slickdeals Tech 当日帖（Violet 色 Amazon $119.97）；Slickdeals headphones 搜索榜亦有热度。注意与目录已有的 OpenDots Air（E210）不同款
- 待定项：无

### 2. beats-solo-4-matte-black — ✅ 已核实
- 品牌 / 型号：Beats / Solo 4 Wireless On-Ear Headphones（Matte Black）
- MPN：MUW23LL/A —— Best Buy 商品页 + B&H + Abt，三源一致
- UPC：195949121708 —— B&H 规格页 + Abt 商品页，双源一致
- 价格行：Best Buy $99.99（Black Friday Deal，原价 $199.99），InStock，Sold by Best Buy。Slickdeals 帖为 Amazon Exclusive Metallic Pink $80，Amazon 独家色价不作价格来源
- deal-site 证据：Slickdeals headphones 搜索榜 frontpage（5.3K votes）
- 待定项：无

### 3. skullcandy-crusher-anc-2-black-tan — ⏳ pending
- 品牌 / 型号：Skullcandy / Crusher ANC 2 Over-the-Ear Noise Canceling Wireless Headphones（Black/Tan）
- MPN：S6CAW-S978 —— Best Buy 商品页实页，已核实
- UPC：lead 810145320808 —— 仅 eBay 多条 listing 一致，无品牌/零售商实页第二来源，按规则 pending
- 价格行：Best Buy $119.99（Black Friday Deal，原价 $239.99），InStock，Add to Cart，Sold by Best Buy
- deal-site 证据：Slickdeals headphones 搜索榜 frontpage（$120，Best Buy，7.9K votes）；专帖 f/20309634
- 待定项：UPC 需品牌官网规格页 / Abt / B&H / Walmart 实页第二来源。注意与目录已有的 Crusher Evo（第七批）不同型号

### 4. nothing-headphone-1-pro-black — ⏳ pending
- 品牌 / 型号：Nothing / Headphone (1) Pro（Black）
- MPN：B192 —— iFixit 设备页 + Best Buy Canada + Nothing 官网产品页，三源一致，已核实
- UPC/EAN：lead 6974434229471（13 位 EAN）—— Swiftronics 加拿大 + Kogan 澳大利亚，两源一致但均为小型零售商/市场平台、非美零售商实页，按规则 pending
- 价格行：Nothing 美国官网 $399（定价）；Slickdeals 帖为 Amazon $319（原价 $399，6.5K votes），Amazon 价不作价格来源，仅作 deal 证据
- deal-site 证据：Slickdeals headphones 搜索榜 frontpage；9to5Google 黑五清单（$319，20% off）
- 待定项：EAN 需美零售商（Target / Best Buy US / B&H）或品牌实页第二来源。注意与 2025 年原版 Headphone (1)（B186）区分，Pro 为 2026-09-29 发布的新款

### 5. amazon-echo-dot-max-graphite — ⏳ pending
- 品牌 / 型号：Amazon / Echo Dot Max（newest model，Graphite）
- MPN：B0D6SX8VLQ —— Best Buy 商品页 Model 栏，已核实（另有一冲突码 PBTech NZ 的 B0DKLQD97R，暂以美国零售商 Best Buy 为准）
- UPC：未找到。Best Buy 规格页实页未含 UPC；Amazon 技术参数页未列 UPC。B 轨的 4 个聚合器码（840414628809 / 840414663176 / 840414694620 / 84041466007）互斥且无一出自美国零售商规格页，**一律不写**
- 价格行：Best Buy $49.99（Black Friday Deal，Save $70，comp $119.99），Sold by Best Buy，InStock，Add to Cart。A 轨报的 $119.99 为原价，不采用
- deal-site 证据：Slickdeals Tech 当日帖（Amazon $49.99）；DealMoon 主页 + Smart Devices 页同帖；Gizmodo 当日帖亦报 $49.99（58% off）
- 待定项：UPC 待 Best Buy "See all specifications" 完整页 / B&H / Target 实页。注意 Alexa+ 需 Prime 会员或 $19.99/月订阅

### 6. harman-kardon-soundsticks-5-white — ✅ 已核实
- 品牌 / 型号：Harman Kardon / SoundSticks 5 2.1-Channel Bluetooth Speaker with HDMI（White / Clear）
- MPN：HKSOUNDSTK5WAM2 —— B&H 商品页型号 + Amazon 商品页 Model Number 一致，已核实
- UPC：050036422468 —— B&H 规格页 UPC 字段 + Amazon UPC 一致 + PicClick 一致，已核实
- 价格行：B&H $279.95（原 $349.95），InStock，Add to Cart，自营。DealMoon 帖 Amazon 同价 $279.95 仅作 deal 信号
- deal-site 证据：DealMoon 主页帖「SoundSticks 4th Gen $199, 5th Gen $279.95」；Slickdeals 未见专帖
- 待定项：黑色版 MPN HKSOUNDSTK5BAM2 已确认但无美国 UPC（仅 APAC 版 EAN），且 B&H 暂无黑色版在售，本批只推白色版；勿与新出的 SoundSticks 5 Wi-Fi 版混淆

### 7. harman-kardon-onyx-studio-9-black — ✅ 已核实
- 品牌 / 型号：Harman Kardon / Onyx Studio 9 Portable Stereo Bluetooth Home Speaker（Black）
- MPN：HKOS9BLKAM —— Harman Kardon 美国官网 Item# + Amazon / Newegg / NeweggBusiness 一致，已核实
- UPC：028292291104 —— Amazon + Newegg + NeweggBusiness 三方一致，已核实。eBay 流传的 610214681881 与 724129192612 为 eBay 生成码/翻新 listing 附带码，已排除
- 价格行：Newegg $219.50（品牌店页标价；**加行时须核实为 Newegg 自营而非 marketplace 卖家**）。Harman Kardon 官网 $299.99 但 OutOfStock。DealMoon 帖 Amazon $158.89 仅作 deal 信号
- deal-site 证据：DealMoon 主页帖（Amazon $158.89）；Slickdeals f/19817025（Woot $149.95，2026-07-28，已过期，仅交叉验证）
- 待定项：Newegg 行自营身份复核

### 8. garmin-venu-x1-black — ✅ 已核实
- 品牌 / 型号：Garmin / Venu X1 GPS Smartwatch（Black / Slate Titanium Caseback，黑色 ComfortFit 尼龙带）
- MPN：010-02980-00 —— Micro Center / CompSource / Petra / Dell / Bloomingdale's 一致，已核实
- UPC：753759342746 —— Micro Center 规格表 + CompSource UPC EAN 字段 + Petra UPC + eBay GTIN 四方一致，已核实
- 价格行：Best Buy $499.99（comp $699.99），自营；Target $499.99；Garmin 官网 / Crutchfield $499.99
- deal-site 证据：DealMoon Wearable 页帖（Amazon $499.99）；Slickdeals 未见专帖
- 待定项：尺寸口径——Best Buy 与 DealMoon 标题称 51mm，Garmin 官方规格为 46mm 表壳 / 2 英寸屏；key 暂不带尺寸，加行时以 Garmin 官方为准复核。Moss 色（010-02980-01 / UPC 753759342753）Best Buy 一度 Sold Out，本批只推黑色版

### 9. oura-ring-5-size-8-silver — ⏳ pending
- 品牌 / 型号：Oura / Ring 5 Smart Ring & Fitness Tracker（Silver，Size 8，2026）
- MPN：JZ90-61403-08 —— Best Buy 商品页 Model 字段 + Slickdeals 前页帖同款同价引用，已核实
- UPC/EAN：pending。唯一线索为 13 位 EAN 6430060156975（Harvey Norman AU），属非美 EAN，不得当作美国 UPC 使用；Best Buy 抓取的规格文本未含 UPC 字段
- 价格行：Best Buy $299.00（comp $399.00，Save $100），Sold by Best Buy，InStock，Add to Cart（黑五价）
- deal-site 证据：DealMoon Wearable 页帖（Amazon $299.00）；Slickdeals 前页 f/20339559 + Sift 黑五清单 Best Buy $299
- 待定项：① UPC 待 Best Buy 规格页（See all specifications > Other）复核；② 会员制：首月免费，之后 $5.99/月或 $69.99/年，价格行须注明首年价不含后续会员费；③ 需 sizing kit 先测尺寸，Size 8 为本次锚定尺码

### 10. whoop-5-0-peak-obsidian — ⏳ pending
- 品牌 / 型号：WHOOP / 5.0 Peak Health and Fitness Tracker，12-Month Membership（Obsidian，2025）
- MPN：973-004-000 —— Best Buy 商品页 Model 字段 + pricehistory.app Amazon 款 Model Number 一致，已核实
- UPC：pending，**两线索冲突，不选**。线索 A：810114363317（manuals.plus，明确绑定 973-004-000）；线索 B：810114363270（SB Technology 分销商帖，称 5.0 Peak Obsidian）。MG 款 973-002-000 → 810114363300、973-003-000 → 810114363324 均与本款无关，不得挪用
- 价格行：Best Buy $199.00（comp $239.00，Save $40），Sold by Best Buy，InStock，Add to Cart。WHOOP 官宣黑五价 Peak $199（11-19 至 12-01）三方一致
- deal-site 证据：DealMoon Wearable 页帖（Amazon $199.00）；Slickdeals 未见专帖
- 待定项：① UPC 冲突待 Best Buy 规格页复核，复核不出即保持 pending；② 价格为会员捆绑价（12 个月 Peak 会员含设备），续费 $239/年，价格行须注明；③ 勿与 One 款（$189）及 MG/Life 款（$299，ECG）混淆

### 11. amazon-echo-time-graphite — ⏳ pending
- 品牌 / 型号：Amazon / Echo Time（all-new / 2026 release），Customizable smart clock（Graphite）
- MPN：B0FRPDXJYC —— Best Buy Graphite 款 Model 字段，已核实（Glacier White 为 B0GFY8SZTK，Coral Pink 为 B0GG1YNSPD，各色独立编码）
- UPC：pending，**仅弱聚合器线索且自相矛盾，不选**。bestpricescanner 同页两处分别给出 840414694712（Graphite）与 840414627574（标称 B0GFY8SZTK 实为白色款），无一出自零售商规格页
- 价格行：Best Buy $199.99（原价行）；DealMoon 帖 Amazon $99.99（首次 50% off）仅作 deal 信号
- deal-site 证据：DealMoon 主页 + Smart Devices 页帖（Amazon $99.99）；Slickdeals 本次未跑专查
- 待定项：① UPC 待 Best Buy 规格页复核；② The Verge 等评测质疑 $200 定价过高，黑五 $99.99 为首降，价格波动大，加行时须重核 live 价

### 12. apple-watch-ultra-3-49mm-black-ocean-band — ⏳ pending（协调降级）
- 品牌 / 型号：Apple / Watch Ultra 3 (GPS + Cellular, 49mm)，黑色钛金属 + Black Ocean Band
- MPN：MF0J4LW/A —— Best Buy 实页（SKU 6572972）+ Slickdeals 线程 + Costco 陈列（item 1874533）三方一致，已核实
- UPC：lead 195950484311 —— eBay 产品标识（GTIN 0195950484311）× 多条、PayMore 两家分店实物扫描、零售盒照片，多源一致。**协调降级为 pending**：链上无品牌/零售商规格页（见裁决 2），入目录前须 Best Buy 规格页复核
- 价格行：Best Buy $549.00（原价 $799.00，省 $250），自营，InStock，Add to Cart（browser.open 实页验证，JSON-LD Price 549 / InStock）。另有 Costco 门店 $449.97（仅限部分门店、不可在线核实，不作行）
- deal-site 证据：Slickdeals 线程（Best Buy from $549，2026-11-07）；Sift 同款 Black Ocean Band $549.00（Live 11-18 至 11-28）及多配置 $549/$649；MacRumors 黑五汇总、9to5Mac 11-04 均报 $549
- 待定项：UPC 须 Best Buy 规格页复核；同页另有翻新行（Simple Cell $599.99）与 open-box 行，不得混用

### 13. apple-iphone-17-pro-max-256gb-cosmic-orange — ⏳ pending（协调降级）
- 品牌 / 型号：Apple / iPhone 17 Pro Max 256GB（Unlocked），Cosmic Orange
- MPN：MFXH4LL/A —— Best Buy 实页（SKU 6473213）+ PayMore 两条 listing 一致，已核实。注意与已入目录的 iPhone 17 Pro 256GB Silver（不同款）无 MPN 碰撞
- UPC：lead 195950638004 —— PayMore 两家分店实物扫描、BarcodesInc（GTIN 0195950638004）、eBay 产品标识、tekfeed 四方一致。**协调降级为 pending**：链上无品牌/零售商规格页（见裁决 2），入目录前须 Best Buy 规格页复核
- 价格行：Best Buy $1,099.99（原价 $1,199.99），自营，InStock（Sift + dealnews + Best Buy 搜索快照一致，最近 12 小时内抓取）。同页 open-box $1,011.99–$1,044.99 与翻新 $972.97+ 不得混用
- deal-site 证据：Slickdeals Hot Deals 今日线程（Cosmic Orange $1099）；Sift 同款 $1,099.99（Live 11-18 至 11-28）；dealnews 称 best-ever 解锁价
- 待定项：UPC 入目录前须 Best Buy 规格页复核；颜色只钉 Cosmic Orange（Deep Blue / Silver 为不同 MPN，不在此款内）

### 14. samsung-galaxy-z-flip8-256gb-graphite — ⏳ pending
- 品牌 / 型号：Samsung / Galaxy Z Flip8 256GB（Unlocked），Graphite
- MPN：SM-F776UZKAXAA —— Best Buy 实页（SKU 6681665，Model 栏），已核实。注意 Verizon 版 MPN 不同（SM-F776UZKAVZW），不得混用；Pink 版为 SM-F776ULIAXAA
- UPC：lead 0198957311260 —— 仅 shop.databitinc.com 一家列出（Part # SM-F776UZKAXAA, UPC 0198957311260）。按规则无第二来源，留 pending
- 价格行：Best Buy $999.99（原价 $1,199.99，省 $200），自营（Sold by Best Buy），InStock，Add to Cart（browser.open 实页验证，JSON-LD Price 999.99 / InStock）。同页另有 marketplace 行 $815.99–$1,239.84（open-box/第三方），只取 $999.99 自营行
- deal-site 证据：Slickdeals Hot Deals 今日线程（256GB Cream or Graphite $999.99）；Sift 未见此款，Best Buy 黑五手机页有售
- 待定项：UPC 待第二来源；Cream 色为另一 MPN，不在此款内

### 15. samsung-galaxy-tab-s10-fe-256gb-gray — ⏳ pending（队列顶位）
- 品牌 / 型号：Samsung / Galaxy Tab S10 FE 10.9" Wi-Fi 256GB（12GB RAM），Gray，含 S Pen
- 队列标注：第七批后备队列③。目录已有 `samsung-galaxy-tab-s10-fe-128gb-gray`（SM-X520NZAAXAR / UPC 887276992266，verified）；本款 MPN 与 UPC 均不同，**无碰撞**，是不同容量款
- MPN：SM-X520NZAEXAR —— Best Buy 实页（SKU 11066617 / 6618940）+ 三星官方 MSRP 价目表（多版）一致，已核实
- UPC：lead 887276992259 —— 三星美国官方 Galaxy Tablet MSRP Price List，2025-03 / 2025-06 / 2025-09 / 2025-12 / 2026-03 / 2026-05 / 2026-06 / 2026-07 共 8 版均列 `SM-X520NZAEXAR … 12+256GB (Wi-Fi) Gray … 887276992259`。按项目先例（三星 MSRP 表单独来源只算线索），留 pending。注意 eBay 一条蓝色款 UPC 887276992273 是另一颜色（SM-X520NLBEXAR），不得混用
- 价格行：Best Buy $469.99（可比价 $669.99，省 $200，Black Friday Deal），自营（Sold by Best Buy），InStock，Add to Cart（Best Buy 搜索快照，4 天前与 1 天前两次抓取一致）。**加时必复核**：同产品页另有第三方 Merchant Expo LLC 行 $874.69（SKU 11066617）与 open-box 行 $422.99–$469.99，$469.99 必须确认为全新自营行才能写；三星官网 2026-08-13 曾显示 256GB $569.99，可作交叉参考
- deal-site 证据：队列后备项（非当日 Slickdeals 热门）；smartprix 汇总同款 $469.99（Amazon 价不可作源，仅作信号）
- 待定项：UPC 第二来源；$469.99 行加时复核（全新 vs open-box）

### 16. apple-iphone-air-256gb-space-black — ⏳ pending
- 品牌 / 型号：Apple / iPhone Air 256GB（Unlocked），Space Black（eSIM only，A3260）
- MPN：MG184LL/A —— Best Buy 实页（SKU 6473225）+ 零售盒照片（MG184LL/A, Space Black, 256GB, Model A3260）一致，已核实
- UPC：lead 195950621303 —— 仅 BarcodesInc（GTIN 0195950621303）。按项目先例，条码聚合站单独不可作数，留 pending
- 价格行：Best Buy $799.99，自营，InStock（Best Buy 搜索快照，最近 1 天内两次抓取，JSON-LD Price 799.99）。**加时必复核**：同款 Light Gold 行 $999.99（3 天前抓取）、Sky Blue $919.99，颜色间价差真实存在；页面另有 $699.99 字样（疑似连网激活价），**不得写入**，只取 $799.99 裸机解锁行；dealnews 11-04 称 $999.99 已过期
- deal-site 证据：Slickdeals Hot Deals 今日线程（iPhone 17 Pro Max 1099 / iPhone 17 pro 899 / iPhone air 799，Unlocked）；dealnews 11-04 曾报 Air 256GB $999.99（已降价）
- 待定项：UPC 第二来源；$799.99 加时复核（裸机价 vs 激活价；Light Gold $999.99 是否同降）

### 17. google-pixel-10-pro-128gb-obsidian — ⏳ pending
- 品牌 / 型号：Google / Pixel 10 Pro 128GB（Unlocked），Obsidian
- MPN：GA09887-US —— Best Buy 实页（SKU 6637725 / 13188733），已核实。硬件型号 G4QUR（pcguide 称 US model）与 Best Buy 的 GA09887-US 是两套编号体系，以零售商实页的 GA09887-US 为准
- UPC：无线索。检索未见任何可信 UPC（Best Buy 文本抓取不含 UPC；无第二来源）
- 价格行：Best Buy $999.00，自营（Sold by Best Buy），InStock（Best Buy 实页，SKU 6637725）。同页另有第三方行 $869.99（Platinum Supply Group）与翻新行 $465.99–$559.00，均排除。另有信号未核实：Google Store 黑五 $749（9to5Google / etagicon 引述，25% off）与 Amazon $749（Slickdeals 线程，Amazon 价不可作源），**加时须在 Google Store 实页复核 $749 再决定写哪行**
- deal-site 证据：Slickdeals 线程（256GB Pixel 10 Pro XL $849 同帖列 Pixel 10 Pro 128GB Obsidian/Moonstone $749，Amazon）；Android Police 10-28 报 Amazon $749（$250 off）
- 待定项：UPC 无线索；$749 行须 Google Store 实页复核，否则以 Best Buy $999.00 为行

### 18. oneplus-15-12gb-256gb-infinite-black — ⏳ pending
- 品牌 / 型号：OnePlus / OnePlus 15 12GB RAM + 256GB（Unlocked），Infinite Black
- MPN：CPH2749（北美版）—— 多家北美经销商（Swiftronics / myworldphone）+ sekin.in（引 OnePlus 美国规格页）一致，已核实。注意 smartprix 列的 CPH2745 / CPH2747 / PLK110 为国际版，**不得混用**；512GB 版为另一配置
- UPC：lead 6921815630302 —— 仅 Swiftronics 一家列出（Brand New UPC 6921815630302）。无第二来源，留 pending
- 价格行：oneplus.com $799.00（原价 $899.99，码 EXTRA100 立减 $100），品牌直营。Slickdeals 线程（sd-core，链 oneplus.com/us/oneplus-15）。**加时必在官网实页复核**（码是否仍有效、是否为裸机价；Best Buy 只有 512GB Sand Storm $999.99 行，256GB 未见 Best Buy 自营行）
- deal-site 证据：同上 Slickdeals 线程；OnePlus 官方 Facebook 亦报 $799.99（$899.99 立减 $100，oneplus.com/us）
- 待定项：UPC 第二来源；官网 $799 码价加时复核；注意 OnePlus 已宣布不再在北美发新机（sekin.in 8 月更新），15 为北美最后旗舰，库存风险须留意

### 19. samsung-s90h-65 — ✅ 已核实
- 品牌 / 型号：Samsung / S90H 65" OLED（2026，QN65S90H）
- MPN：QN65S90HAEXZA —— Crutchfield MFR # + Samsung 2026 规格表 + Best Buy 页面 Model 栏，三源一致，已核实
- UPC：198957270574 —— QVC 技术规格表 PDF + manuals.plus 收录的 Samsung 规格表，两源一致指向 QN65S90H，已核实。⚠️ 冲突记录：fillion.ca（加拿大零售商）给同一型号列 198957276095，单源、疑似区域变体 UPC，不采用；加时复核须以 Best Buy 规格页 "Other" 栏为准
- 价格行：Best Buy $1,399.99，Sold by Best Buy，Add to Cart，InStock（2026-11-21 抓取；Black Friday 价，comp. value $2,699.99）；Costco 同价 $1,399.99 为含 Allstate 保护计划的 bundle，不作主行；Sam's Club 55" $1,197.99（不同尺寸，仅参考）
- deal-site 证据：Slickdeals Black Friday Sift（Costco 77" $1,899.99 / 65" $1,399.99；Sam's 55" $1,197.99 / 77" $1,997.99），Sift 排名靠前
- 待定项：UPC 冲突项加时再核一次

### 20. lg-oled-evo-c6-65 — ✅ 已核实
- 品牌 / 型号：LG / OLED evo C6 65"（2026，OLED65C6PUA；注意 LG 官网另有 OLED65C6WUA 变体，Best Buy 行用 PUA）
- MPN：OLED65C6PUA —— Best Buy Model 栏（SKU 6673112），已核实
- UPC：195174137666 —— B&H 产品页 + EnergyStar 认证清单（OLED65C6PU* 家族）+ Value Electronics + Amazon + Adorama，五源一致，已核实。注：EnergyStar 同时列 195174137703（PU* 家族另一后缀变体）；Visions 加拿大列 OLED65C6PUA.ACC / 195174137673，区域变体，不混用
- 价格行：Best Buy $1,399.99，Sold by Best Buy，Add to Cart，InStock（2026-11-22 00:02 UTC 实页抓取；Black Friday 价，comp. value $2,699.99）；Walmart 同价 $1,399.99（Slickdeals 线索）；Sam's Club 65" $1,399.99 / 77" $1,999.99（Sift）
- deal-site 证据：Slickdeals Sift（Sam's 65"/77"）+ Slickdeals 帖 Best Buy $1,499.99→现 $1,399.99
- 待定项：无

### 21. samsung-hw-q990h-black — ✅ 已核实
- 品牌 / 型号：Samsung / Q-Series HW-Q990H（2026 旗舰，11.1.4ch + 无线低音炮 + 后置）
- MPN：HW-Q990H/ZA —— Samsung US 官网 + Best Buy Model 栏（SKU 6670431），双源一致，已核实
- UPC：198957269394 —— Walts 零售商规格页 + Amazon 产品页，两源一致，已核实
- 价格行：Best Buy $1,497.99（Sold by Best Buy）；Samsung US $1,499.99。Woot $857.99 不采用：Deal Guy 等帖指出该 listing 疑似国际版/平行货，且 Woot 价未经自营身份核实
- deal-site 证据：Slickdeals Sound Bar 页置顶（Woot $857.99，by pennysave）+ Sift 亦有 Best Buy 行
- 待定项：无。注意目录仅有 HW-Q990F pending，是上一代

### 22. jbl-cinema-sb580-black — ✅ 已核实
- 品牌 / 型号：JBL / Cinema SB580（3.1ch，Virtual Dolby Atmos，无线低音炮，440W；JBL 官网：manufactured from 2024 until now）
- MPN：JBLSB580BLKAM —— Crowdfused、goWholesale、VIP Outlet 产品名一致，已核实
- UPC：050036408530 —— Crowdfused 型号/UPC 表 + goWholesale "JBLSB580BLKAM - 050036408530" + VIP Outlet SKU VIP050036408530MN，三源一致，已核实（见裁决 3）
- 价格行：Walmart $199.00，Sold and shipped by Walmart.com，InStock（Slickdeals + Walmart 实页；原价 $289）
- deal-site 证据：Slickdeals Sound Bar 页（Walmart $199，31% off）
- 待定项：⚠️ 2026-09 至 11 月多条社交帖称部分 Walmart 门店 in-store clearance 低至 $50（与线上 $199 常规价并存）；线上行目前正常，但加时须复核线上价/库存是否仍在

### 23. samsung-smart-monitor-m70f-43-black — ✅ 已核实（队列顶位）
- 品牌 / 型号：Samsung / Smart Monitor M7 M70F 43" 4K（LS43FM702UNXZA，黑色；与已入的 32" 白 LS32FM703UNXZA 不同尺寸 = 不同款）
- 队列标注：三星队列顶位。目录仅有 32" M70F
- MPN：LS43FM702UNXZA —— Samsung US + Best Buy Model 栏（SKU 6632216）+ Abt，三源一致，已核实
- UPC：198957005435 —— camelcamelcamel ASIN B0F5VLWQY6 + DataVision + LayawayLand，三源一致，已核实（见裁决 3）
- 价格行：Samsung US $499.99；Abt $499.99 InStock。Best Buy $399.99 但挂 Clearance 标，仅作参考价、不作主行
- 待定项：⚠️ Best Buy 清仓 $399.99 + Amazon 清仓 $279.99 帖（2026-11-17）并存，显示该尺寸可能进入清仓通道；Samsung US/Abt 仍为常规价。加时须复核 Samsung US 价与库存，确认仍为常规在售（非清仓）

### 24. samsung-odyssey-g73sh-32-black — ✅ 已核实
- 品牌 / 型号：Samsung / Odyssey OLED G7 G73SH 32" 4K 165Hz / 1080p 330Hz 双模（2026）
- MPN：LS32HG732SNXZA —— Costco Item 2084100 Model 栏 + Samsung 促销条款 Exhibit A + Samsung US，三源一致，已核实
- UPC：198957301674 —— Micro Center + Walts + eBay + MonitorPug，四源一致，已核实
- 价格行：Costco $699.99 + $100 Costco Shop Card（Slickdeals 帖 by shivster1796；Costco 实页 Item 2084100）；Samsung US $1,099.99（list）
- deal-site 证据：Slickdeals Monitor Deals 置顶（Costco $699.99 + $100 卡）
- 待定项：无（注：Costco 价含 $100 礼卡，净价口径加时再定）

### 25. hisense-qd7-55 — ⏳ pending
- 品牌 / 型号：Hisense / QD7 Series 55" Hi-QLED Fire TV（2026，Costco 专供型号 55QD75SFC；注意与 Best Buy 的 75QD7QF 等 2025 QD7QF 系列不同型号）
- MPN：55QD75SFC —— Costco Item 9655750 Model 栏 + Hisense 规格 PDF，双源一致，已核实
- UPC：lead 888143028279 —— 仅见于 Hisense 官方规格 PDF（Costco gdx-assets 托管），无第二来源，按规则留 pending（与 U7900H 规格表单源先例同口径）
- 价格行：Costco $269.99（价至 11/30/26；costcodrops 2026-11-21 11:50 AM PST 查核 in stock；Costco.com 一次抓取显示 OutOfStock，库存信号 mixed）；仓库价亦 $269.99
- deal-site 证据：Slickdeals Sift（Costco 55" $279.99→现 $269.99；100" $999.99）
- 待定项：UPC 第二来源、加时复核 Costco 库存

### 26. asus-rog-strix-xg27ucgr-black — ⏳ pending（队列顶位）
- 品牌 / 型号：ASUS / ROG Strix XG27UCG Gen2（XG27UCGR），27" 4K 双模（4K 162Hz / FHD 485Hz），Fast IPS
- 队列标注：华硕队列顶位。须与已入的 XG27UCG（UPC 197105564633，CompSource + Adorama）严格区分，不得借用其 UPC
- MPN：XG27UCGR —— ROG US + ASUS eShop，双源一致，已核实。ASUS 内部件号 90LM0CS0-B013B2；白色变体 XG27UCGR-W / 90LM0CS2-B013B2（$429），须区分
- UPC：无任何 UPC 线索（全网检索无结果），pending
- 价格行：ROG US / ASUS eShop $399，InStock（ROG US JSON-LD）；Staples $449 InStock；Target $425.99。Amazon $319 帖（PCGuide，11/05）为 Amazon 价，不作行
- deal-site 证据：队列款（非当日 Slickdeals 热门）
- 待定项：UPC

### 27. lenovo-legion-pro-7-gen-10-83ru0006us — ✅ 已核实（队列顶位）
- 品牌 / 型号：Lenovo / Legion Pro 7 16AFR10H，Eclipse Black，Ryzen 9 9955HX3D，RTX 5080 16GB，32GB DDR5-5600，2TB PCIe Gen5 SSD，16" WQXGA OLED 240Hz，Win 11 Pro
- 队列标注：第六批后备队列（联想）
- MPN：83RU0006US —— Best Buy model field（SKUs 12629843, 13259871）+ PSREF PDF for 16AFR10H + CompSource，三源一致，已核实
- UPC：199271660232 —— PSREF PDF（"EAN / UPC / JAN: 199271660232"，TopSeller，Announce 2025-09-13）+ CompSource 分销商 + Bonanza / SimplifiedComputers / DirectDial / PC-Canada / Venditore 一致。制造商 + 分销商 = 可接受先例，已核实
- 价格行：Adorama $4,949.00，InStock（JSON-LD），Adorama 直营（2026-11-22 00:02 UTC 实页；标题/规格确认 9955HX3D / 32GB / 2TB / RTX 5080 / Win 11 Pro）。Best Buy SKU 12629843 同价 $4,949.00 但为 "Sold & shipped by Adorama"——marketplace，**不是** Best Buy 直营行，不得用作 Best Buy 行。Newegg $4,495.62 未核卖家身份，不用
- 待定项：无。勿混用：Slickdeals/Best Buy 1TB 配置（2026-11-08 帖，$2,849.99，已过期）是另一配置、MPN 未知；同系 83RU0005US 有 RAM 争议（CompSource 称 32GB/2TB，ek.ua 称 64GB），不是钉死配置

### 28. alienware-16-aurora-lac16250-7469blu-blue — ✅ 已核实（队列顶位，HOLD 解除）
- 品牌 / 型号：Alienware / 16 Aurora，Blue，Intel Core 7 240H，RTX 5060 8GB，16GB DDR5-5600，1TB SSD，16" WQXGA 2560×1600 IPS 120Hz，Win 11 Home
- 队列标注：第六批 alternate。**HOLD 已解除**：第六批的保留条件是 AntOnline 直营行不显示型号代码；本次实页确认 AntOnline 页已印 Manufacturer Part Number LAC16250-7469BLU-PUS（见裁决 5）
- MPN：LAC16250-7469BLU-PUS —— 第六批记录（Newegg 规格页 + D&H 分销商规格表；Best Buy model field 一致），本次 AntOnline 实页再次确认，已核实
- UPC：884116430469 —— 第六批记录（D&H Consumer 规格表 + "Product Setup - New Age" 规格表，Hilltown Tech 一致），已核实。注：第七批简报曾称 Aurora 的证据在 rework7，实误——证据在 `data/rework6/trackD.md:122-128` 与 `data/candidates_batch6_500.md:594`，不在 rework7
- 价格行：AntOnline $2,149.99，JSON-LD InStock，新品（2026-11-22 00:03 UTC 实页）。AntOnline（Atlanta Network Technologies, Inc.，Atlanta GA，1995 年起营业）是美国直营线上零售商，非平台。⚠️ tier 旗标：AntOnline 是小零售商，且 $2,149.99 高于 Best Buy 已售罄的 $1,707.70；第六批的保留条件原要求 Best Buy / Newegg / dell.com 直营行，本行是 AntOnline 直营而非三者。Best Buy SKU 13279039 实页 Sold Out（JSON-LD 误报 InStock，以页文为准）；Dell.com 配置器只显示 32GB/1TB/RTX 5060 配置 $2,699.99 list，不对应零售 PUS SKU，不用
- 待定项：入目录时决定 AntOnline 行是否接受为 tier。勿混用：32GB 同系 LAC16250-7568BLU-PUS 的 $999.99 Slickdeals 帖为 2025-11-21（一年前，已过期）；Best Buy "Upgraded" PC Heaven 行（AC16250-Upgraded）为第三方改装，排除

### 29. lenovo-loq-essential-15arp11-83va001pus — ⏳ pending（队列顶位）
- 品牌 / 型号：Lenovo / LOQ Essential 15ARP11，Eclipse Black，Ryzen 7 170，RTX 5050 8GB 65W，16GB DDR5-4800，512GB PCIe 4.0 SSD，15.6" FHD 1920×1080 IPS 144Hz 100% sRGB，Win 11 Home（2026-02 发布）
- 队列标注：第六批后备队列（联想）
- MPN：83VA001PUS —— **pending（仅 Best Buy 单源）**。Best Buy model field（SKU 6673556，2026-11-22 00:01 UTC 实页）。lenovo.com / Newegg / B&H 均未命中。PSREF LOQ Essential 15ARP11 PDF 是平台规格（7 页，无逐型号 EAN/UPC 表），不列 83VA001PUS
- UPC：pending，无线索。PSREF 平台 PDF 无型号级 UPC 行；全网搜索无 UPC
- 价格行：Best Buy $1,049.99（Comp. Value $1,499.99，Save $450），Add to Cart，JSON-LD InStock，Sold by Best Buy。搜索爬虫另见黑五 $999.99 变体与 $1,299.00 PC Heaven marketplace SKU（12974439），均不用。lenovo.com US list $1,892.99（NotebookCheck/The Gadgeteer，2026-11-10）是标价，不是行
- 待定项：MPN 第二来源（lenovo.com US 产品页或 B&H）；UPC（无线索，需零售商/分销商规格页）。另：Best Buy 标题称 "2K" 但其规格面板称 1920×1080 FHD 144Hz，以规格面板 + PSREF 平台规格为准钉 FHD，标题与规格冲突已记录

### 30. asus-rog-zephyrus-g14-ga403um-r9hx4-white — ⏳ pending（队列顶位）
- 品牌 / 型号：ASUS / ROG Zephyrus G14 (2025) GA403UM，Platinum White，Ryzen 9 270，RTX 5060 8GB，16GB LPDDR5X-7500，1TB PCIe 4.0 SSD，14" 3K 2880×1800 OLED 120Hz 500-nit，Win 11 Home
- 队列标注：第六批 alternate
- MPN：GA403UM-G14.R9HX4 —— **pending（仅 Best Buy 单源）**。Best Buy model field（SKU 6629420，2026-11-22 00:02 UTC 实页）。非合格佐证：Best Buy 上 Velztorm marketplace 行印 "Model No: GA403UM-G14.R9HX4"、Smartprix 聚合器、Slickdeals 线程。B&H / Newegg / ASUS store 均未命中（ASUS ROG 站列 2026 GA403 家族、不同 CPU，非 2025 GA403UM 零售 SKU 后缀）
- UPC：pending，无线索。Best Buy 规格面板未印；全网搜索无 UPC（仅 Amazon ASINs for HIDevolution 捆绑包）
- 价格行：Best Buy $2,299.99，Sold by Best Buy，Add to cart，JSON-LD InStock，4.4 星 / 509 评价。Smartprix 称 Walmart $1,976.99（聚合器，未核实，不用）；Slickdeals open-box $1,154.99 Excellent / $1,085.99 Good / $1,015.99 Fair 均为 open-box，非新品行；Tom's Guide $1,349 为 2025-07 旧价；Velztorm "Upgraded" 行（$2,049.99–$2,149.99）为第三方改装，排除
- 待定项：MPN 第二来源（ASUS US store / B&H）；UPC（无线索）

### 31. hp-omen-transcend-14-14-fb1043dx-black — ⏳ pending（队列顶位）
- 品牌 / 型号：HP / OMEN Transcend 14 (2025)，Shadow Black，Intel Core Ultra 7 255H，RTX 5060 8GB，16GB LPDDR5x-7467，1TB PCIe Gen4 SSD，14" 3K 2880×1800 OLED 120Hz，Win 11 Home
- 队列标注：第六批 alternate
- MPN：14-fb1043dx / D8KM3UA#ABA —— Best Buy model field（SKU 6672941）+ HP 自家 datasheet PDF（"OMEN by HP Transcend 14 inch Gaming Laptop PC 14-fb1043dx"，Product number D8KM3UA#ABA），双源一致，已核实
- UPC：lead 821844495667 —— 仅 HP datasheet PDF（"UPC Code • 821844495667"）。无第二来源（搜索该 UPC 只返回 datasheet；Walmart Business 同配置 $1,330.00 但缺货且不印 UPC），按规则 pending
- 价格行：Best Buy $2,499.99，Sold by Best Buy，Add to cart，JSON-LD InStock，4.8 星 / 37 评价（2026-11-22 00:02 UTC 实页）。标价，无促销。早先片段提到的 "Win 11 Pro" 与 "+1TB Dock" 属另一（升级/marketplace）listing，钉死配置为 Win 11 Home
- 待定项：UPC 第二来源（B&H / Newegg 规格页印 821844495667）。勿混用：32GB 同系 14-fb1013dx / B94GQUA#ABA（SKU 6618922，清仓 $1,600.99 片段）已死——Best Buy 实页称 "This item is no longer available in new condition"

### 32. samsung-galaxy-book5-360-15-np750qha-ka1us-gray — ⏳ pending（队列顶位，出队列）
- 品牌 / 型号：Samsung / Galaxy Book5 360，Gray，Core Ultra 7 256V，16GB LPDDR5X，512GB SSD，15.6" FHD AMOLED touch，Win 11 Home，Copilot+ PC
- 队列标注：第七批剔除款复查——**出队列**（见裁决 6）
- MPN：NP750QHA-KA1US —— **本轮新核实**：Best Buy model field + Quill（Model #）+ Connection（MFG Part#）+ Staples（Model），四源一致，已核实
- UPC：pending，无线索。Connection 与 Quill 抓取文本均不印 UPC；samsung.com US 未找到该 MPN 的产品页
- 价格行：Connection $1,695.95，In Stock，Ships in 1–2 Business Days（2026-11-22 00:06 UTC 实页；搜索片段的 $1,315.95 已过期，实页为 $1,695.95）；Quill $1,702.99，JSON-LD InStock，delivery Nov 25–27（实页）。两行约 $1,700 价一致。Staples $1,419.69 缺货（193+ 天旧价）。Best Buy 复查：SKU 6613609 清仓 $358.99（Save $991，Comp. Value $1,349.99）**Unavailable**；SKU 13224856 $2,187.81 亦 Unavailable——$358.99 vs $2,187.81 冲突仍在但已无关，行取 Connection/Quill
- 待定项：UPC（无线索）；Samsung.com 第二 MPN/价格来源（若该型号重新上架）

### 33. lenovo-yoga-7i-2-in-1-14-83tc003xus-luna-grey — ⏳ pending
- 品牌 / 型号：Lenovo / Yoga 7i 2-in-1 Gen 11 Aura Edition 14IPH11，Luna Grey，Intel Core Ultra 7 355（Panther Lake, Series 3），24GB LPDDR5X-7467（焊死），512GB PCIe NVMe SSD，14" 1920×1200 2K OLED touch 60Hz 400-nit，Win 11 Home，Copilot+ PC
- MPN：83TC003XUS —— Best Buy model field（SKU 6671007）+ Newegg listing（Model Name 83TC003XUS，规格一致）+ NotebookCheck（2026-11-21）三源一致，已核实
- UPC：lead 199275077982 —— 仅 TekFeed 聚合器（"SKU 83TC003XUS, Model 83TC003XUS, UPC 199275077982"）。PSREF 未命中 83TC003XUS / 14IPH11，按规则 pending
- 价格行：Best Buy $999.99（Save $650，Comp. Value $1,649.99），Add to Cart，JSON-LD InStock，4.8 星 / 49 评价（2026-11-22 00:07 UTC 实页；1–2 天前爬虫确认 "Sold by Best Buy"）。Slickdeals 前页帖 2026-11-19（Dr.W）+ NotebookCheck 2026-11-21 "lowest-ever price"。open-box 行（$765.99–$812.99）与翻新（$1,199.99，IST Computers）排除；"Upgraded" marketplace 行（83TC003XUS-Upgraded，$1,629–$1,729）排除
- deal-site 证据：Slickdeals 前页 2026-11-19；NotebookCheck 2026-11-21
- 待定项：UPC 第二来源（PSREF 14IPH11 型号 PDF 或零售商规格页印 199275077982）。勿混用：与第七批的 Yoga 7i 2-in-1 16" 83JT0000US（Ultra 5 226V，16GB，16" WUXGA IPS）及双生配置 83TE0004US（Ultra 5 322，16GB，$1,649.99 list）不同尺寸/CPU/RAM = 不同款

### 34. dell-xps-13-ldx13260-5960sky-sky — ⏳ pending
- 品牌 / 型号：Dell / XPS 13 (2026) DX13260，Sky，Intel Core 5 320 (Series 3)，16GB LPDDR5X，512GB SSD，13.4" 2560×1600 (2.5K) touch 120Hz 500-nit，Intel Graphics，Win 11 Home，Wi-Fi 7
- MPN：LDX13260-5960SKY-PUS —— **pending（Best Buy + 制造商包装）**。Best Buy model field（SKU 6683772）+ 零售盒照片（Facebook，2026-10-10/11-04）显示型号代码与 Dell 包装上的一致规格。无第二零售商（"-PUS" 后缀为 Best Buy 零售 SKU；dell.com 配置器不带该 SKU）
- UPC：lead 884116652960 —— 仅 eBay listing（item 327296803592）+ picclick / myus / seekknowhow 同 listing 镜像。无零售商/分销商第二来源，按规则 pending
- 价格行：Best Buy $999.99，Sold by Best Buy，Add to cart，JSON-LD InStock，4.3 星 / 47 评价（2026-11-22 00:07 UTC 实页）。**Slickdeals 的 $699.99 已过期**（2026-11-16 帖，优惠至 Nov 18；5 天前爬虫 $699.99，1 天前爬虫 $999.99），**不得写 $699.99**。另一 Best Buy SKU 13223232 同型号 $969.00，卖家不明，不用
- deal-site 证据：Slickdeals 前页（$699.99 已过期，仅作热度信号）
- 待定项：MPN 第二零售商；UPC 第二来源（B&H / Newegg / Dell 规格表）。另：Best Buy 标题称 "3K" 但规格面板称 2560×1600 (2.5K) 120Hz，以规格面板为准。勿混用 8GB 同系 LDX13260-5953SKY-PUS（亦曾 $699.99）

### 35. dji-osmo-action-5-pro-standard-combo-black — ✅ 已核实
- 品牌 / 型号：DJI / Osmo Action 5 Pro Standard Combo，黑色
- MPN：CP.OS.00000377.01 —— B&H 商品页 URL slug（`cp_os_00000377_01`）+ Micro Center "Mfr Part #: CP.OS.00000377." 一致，已核实
- UPC：190021114616 —— B&H 规格页 + Micro Center 规格表（SKU 754903）一致，已核实
- 价格行：B&H $319.00 自营、In Stock；Micro Center $319.99
- deal-site 证据：bfcy.cameraegg DJI 黑五页点名 "Buy the Osmo Action 5 Pro at $319"；Slickdeals 同期多为 Action 6 帖，Action 5 Pro 为该站 DJI 黑五首选
- 待定项：无

### 36. dji-osmo-pocket-3-black — ✅ 已核实
- 品牌 / 型号：DJI / Osmo Pocket 3（单机，Standard），黑色
- MPN：CP.OS.00000301.01 —— B&H（BH # DJOP3）+ Crutchfield（MFR # CP.OS.00000301.01）一致，已核实；与已入 Creator Combo 的 CP.OS.00000302.01 不同
- UPC：190021094970 —— B&H 规格页 + ShopSavvy 商品页一致，已核实
- 价格行：B&H $373.00（划线 $439.00）自营、In Stock；Best Buy 同价 $373（9to5Toys 2026-11-20）；Amazon $373 仅作佐证（不作价格来源）
- deal-site 证据：Slickdeals Pocket 3 帖（2026-10-31，AliExpress $263 为全球版非美行，仅作热度信号）；9to5Toys 黑五价 $373
- 待定项：无。注意：2025 年该机美国价曾因关税涨至 $800 左右，现价已回落，不影响本次行

### 37. dji-mini-5-pro-rc-n3-gray — ✅ 已核实
- 品牌 / 型号：DJI / Mini 5 Pro（配 RC-N3 遥控器，单电池标准版），灰色
- MPN：CP.MA.00000838.03 —— B&H 商品页 URL slug（`cp_ma_00000838_03`）+ Adorama MFR CP.MA.00000838.03 一致，已核实（Adorama 后缀 K 为其捆绑包 SKU，不取）
- UPC：190021121126 —— B&H 规格页 + Target 商品页（TCIN 1012392891）一致，已核实
- 价格行：B&H $759.00 自营、In Stock；Adorama 同款单机捆绑包 $759.00（含卡/包，不同箱，不作同款行）
- deal-site 证据：Slickdeals 2026-11 月多帖 Frontpage（Mini 5 Pro RC-N3 / Fly More），但均为 AliExpress 店铺价（$508–$825），**不作价格来源**，仅作热度信号
- 待定项：无。**新品类提案**：drones（目录无此品类，须用户点头）

### 38. dji-neo-2-drone-only-gray — ✅ 已核实
- 品牌 / 型号：DJI / Neo 2（Drone Only，无遥控器），灰色
- MPN：CP.FP.00000270.01 —— Adorama MFR + B&H URL slug（`cp_fp_00000270_01`）+ Visions CA 型号栏一致，已核实
- UPC：190021157224 —— B&H 规格页 + Target 商品页（TCIN 1015573677，Target Plus 合作方数据）+ Visions CA 一致，已核实
- 价格行：B&H $259.00 自营、In Stock；Adorama $259.00 In Stock
- deal-site 证据：Slickdeals Neo 2 帖（2026-11-14，AliExpress 单机 $212，仅热度信号）；bfcy Neo 2 页确认 B&H 单机 $259 / Fly More $349 / RC-N3 版 $429 三档价
- 待定项：无。**须标注**：Neo 2 未上 DJI 美国官网直营（UFLPA 海关原因），美国行走授权经销商（B&H、Adorama、djiusa.com）；B&H/Adorama 行仍为零售商自营，符合收录口径。**新品类提案**：drones

### 39. insta360-x5-standard-bundle-black — ✅ 已核实
- 品牌 / 型号：Insta360 / X5 Standard Bundle（基础盒：单机+电池+线+收纳包），黑色
- MPN：CINSAAHA_X501 —— B&H 商品页 URL slug（`cinsaaha_x501`）+ NFM 零售商页 Model 栏一致，已核实
- UPC：842126110955 —— B&H 规格页（实页打开确认，2026-11-22 00:01 UTC 抓取）+ NFM 零售商页一致；另 B&H Motorcycle Bundle 套装页内含件清单亦列同一 UPC。已核实
- 价格行：B&H $439.99（划线 $549.99）自营、In Stock；Insta360 官网店 $439.99（划线 $549.99）；Target $439.99
- deal-site 证据：Slickdeals 黑五相机页、the5krunner 2026-11-21（X5 $439，降 $110）；Costco X5 Bundle $549.99 为另一捆绑包，不取
- 待定项：无。**防混淆**：Best Buy / Costco 的 "X5 Bundle"（MPN CINSAAHA，UPC 842126113239，含 256GB 卡+自拍杆+备用电池）是另一捆绑 SKU，不得与本款互贴标识

### 40. insta360-x6-standard-bundle-midnight-black — ✅ 已核实
- 品牌 / 型号：Insta360 / X6 Standard Bundle，Midnight Black（2026-08-12 上市新旗舰）
- MPN：CINSABXA-X601 —— Micro Center "Mfr Part #" + Visions CA 型号栏一致，已核实；B&H URL slug `cinsabxa_x602` 对应 Arctic White 版（X602），不混用
- UPC：842126120213 —— Micro Center 规格表 + Visions CA 一致（另 eBay / PBTech NZ 同值佐证），已核实
- 价格行：B&H $699.99 自营、In Stock（上市价，无划线）；Insta360 官网公告 "from $699.99"
- deal-site 证据：DealMoon 新品帖（X6 上市，$699.99 B&H）；Slickdeals Costco X6 Bundle $629.99（2026-11 月黑五，另一捆绑包，不取）；bfcy 确认 $699.99 为上市价、尚未降价
- 待定项：无。备注：B&H 商品页另列 EAN 6942590200337（13 位，与 UPC 842126120213 编号体系不同）；本次以两家美国零售商一致的 UPC 为准，EAN 不写入

### 41. gopro-hero13-black-black — ✅ 已核实
- 品牌 / 型号：GoPro / HERO13 Black（单机），黑色
- MPN：CHDHX-131-TH —— B&H URL slug（`chdhx_131_th`）+ Filmtools MPN 栏一致，已核实
- UPC：810116381821 —— B&H 规格页 + Filmtools UPC 栏一致，已核实
- 价格行：B&H $349.99（划线 $429.99）自营、**暂时缺货，预计到货 Dec 07, 2026**；Amazon $349（the5krunner 2026-11-21）仅佐证
- deal-site 证据：Target 黑五清单 HERO13 Black $429.99；Costco HERO13 Black Bundle $339.99（Item 6094012，另一捆绑包，不取）；Slickdeals 黑五 Sift 有 Costco 款
- 待定项：**库存**——B&H 黑色单机暂缺货（预计 12-07 到货），加行时须重查库存。另 Scuba 页面另列一 CHDHX-131-RW / UPC 810116381616 变体，与本次 TH/…1821 不一致，**该 RW 线索未核实、不采用**，不贴给本款

### 42. insta360-go-3s-standard-bundle-128gb-midnight-black — ✅ 已核实
- 品牌 / 型号：Insta360 / GO 3S Standard Bundle，128GB，Midnight Black
- MPN：CINSAATA_GO3S13 —— B&H URL slug + Micro Center "Mfr Part #" + CompSource 一致，已核实
- UPC：842126106989 —— B&H 规格页 + Micro Center 规格表（SKU 721472）一致，已核实
- 价格行：B&H $299.99（划线 $379.99）自营、In Stock；Micro Center $299.99
- deal-site 证据：Target 黑五清单 GO 3S 128GB $299.99；Slickdeals 相机页有 GO 3S 帖
- 待定项：无。**防混淆**：Target 的 "GO 3S Action Bundle"（UPC 842126107641，Target Plus 合作方）与 B&H 的 Camera Only 版（CINSAATA_GO3S11，UPC 842126106965，$269.99 Special Order）均为不同箱，不取

### 43. asus-rog-delta-ii-white — ⏳ pending（队列顶位）
- 品牌 / 型号：ASUS / ROG Delta II Wireless Gaming Headset，Moonlight White
- 队列标注：第六批后备队列。目录已有黑色款 `asus-rog-delta-ii-black`（pending、无标识），白色为不同颜色款，不撞号
- MPN：**pending（冲突）**。美国渠道 Newegg listing 型号栏为 `90YH03W0-BHAA10`；新加坡/欧洲渠道（Xcellent、SquareDeals、Carousell SG、Alfrensia）一致为 `90YH03W0-BHUA10`。后缀 BHAA10 vs BHUA10 疑似美版/亚太版之分，**不得二选一**，入目录时以美版实物或 Best Buy 规格页复核为准
- UPC：**pending（线索冲突，勿选）**。线索 A：`197105907362`，与 MPN BHUA10 绑定，来源 SquareDeals（SG 零售商）、Dynacore（SG）、Carousell SG——均为非美渠道，无美国零售商规格页佐证，校验位有效。线索 B：`197105907355`，来源 Ubuy（ASIN B0DGZY13L6 附带），**已证伪**：亚马逊上 ASIN B0DGZY13L6 实为黑色款，其 UPC 为 `197105604858`（Micro Center 黑色款规格页亦为此码，校验位有效）；Ubuy 的 197105907355 属张冠李戴，**禁用**。另：`197105604858` 是黑色款 UPC，不得用于白色款
- 价格行：Best Buy 自营（Sold by Best Buy）$149.99，InStock，Add to Cart，黑五价（对比价 $229.99），SKU 6637821，Model 栏 `A701 ROG DELTA II/WHT`。Best Buy 实页抓取未展开 "See all specifications"，故未从该页取到 UPC
- 待定项：① 美版 MPN 后缀（BHAA10 vs BHUA10）；② 白色款 UPC 需美国零售商规格页第二来源；③ $149.99 为黑五促销价，入目录时重验 live 价

### 44. asus-rog-keris-ii-ace-white — ⏳ pending（队列顶位）
- 品牌 / 型号：ASUS / ROG Keris II Ace Wireless Gaming Mouse，Moonlight White（P714 ROG KERIS II WL ACE/WHT）
- 队列标注：第六批后备队列。目录已有黑色款 `asus-rog-keris-ii-ace-black`（pending、无标识），白色为不同颜色款，不撞号
- MPN：90MP03N0-BMUA10 —— PBTech、SquareDeals、Carousell SG 多源一致；美国分销商 IPCStore 同款在售 $179。MPN 本身不扶正，仅作线索
- UPC：**pending（正面冲突，勿选）**。两个校验位均有效的 UPC 各执一端：`197105394612`——PBTech（NZ 零售商，UPC 栏）、SquareDeals（SG）、Dynacore（SG）、Carousell SG，一致绑定 MPN BMUA10；`197105394582`——美国亚马逊 ASIN B0D3CX3QMD（Desertcart 多站镜像 + Layup 均引同一亚马逊数据，实为同一源），GTIN 00197105394582。校验位验算不能区分两者（两码皆有效）。疑似美版/亚太版分包，**必须等美国零售商规格页（Best Buy/B&H/Target）定夺**，本次不采纳任一码
- 价格行：IPCStore（美国零售商，MPN 绑定 listing）$179.00，InStock——白色款可用价行。ASUS eShop 美国直营 $94.99 起（原价 $159.99）、InStock，但页面黑白两色共用、"Starting at" 未按颜色拆分，**不能用作白色款价行**，仅作参考。排除：Best Buy 页 $182.43 的卖家是 antonline（第三方 marketplace），按规则排除；Target $129.99 缺货（OutOfStock），不用
- 待定项：① UPC 冲突（612 vs 582）待美国零售商规格页裁决；② eShop $94.99 是否覆盖白色待入目录时按颜色复核

### 45. asus-rog-strix-scope-ii-96-wireless-white-nx-storm — ⏳ pending（队列顶位）
- 品牌 / 型号：ASUS / ROG Strix Scope II 96 Wireless，Moonlight White，**ROG NX Storm（clicky）轴**——轴体已钉死
- 队列标注：第六批后备队列。目录已有黑色款 `asus-rog-strix-scope-ii-96-wireless-black` 与 RX 无线黑色款，白色 Storm 为不同颜色+轴体款，不撞号
- MPN：90MP037B-BKAA30 —— ASUS eShop 美国直营白 Storm 专页，Product Name `X901 SCOPE II 96 WL/WHT/NXSM/CA/PBT`。**pending（仅 eShop 单源）**。注意 eShop 页面 Color 栏抓取显示为 "Black"（模板串色），以 Product Name 中的 /WHT/ 与 Part Number 为准
- UPC：lead 197105487154（校验位有效）—— 三源一致指向同一型号串 `X901 SCOPE II 96 WL/WHT/NXSM/CA/PBT`：Target 规格页（UPC 栏，但该页注明 "item details provided by Target Plus Partner"，属 marketplace 供货信息，效力打折）、Newegg（Model # 栏直接填该 UPC）、Snapklik（聚合器，型号+UPC 同框）。无任何一家美国零售商规格表（Best Buy/B&H 规格页）背书，按先例（多源但无零售商规格表 → pending）留 pending
- 价格行：ASUS eShop 美国直营 $131.99，InStock（Open Graph 抓取；注意同一 part 在较早抓取中为 $179.99，价格已变动，入目录时重验）。Newegg $129.99–$149.99 为 "from" 区间价、卖家不明，不作主价行
- 待定项：① UPC 需 Best Buy 或 B&H 规格页第二来源；② **NX Snow 白色款（MPN 90MP037A-BKAA30，加拿大 eShop）未入选**：其美国 UPC 全网未找到（欧盟 EAN 4711387487082/4711387487112 非美版），本次只带 Storm 款，Snow 款留待后补；③ eShop $131.99 为促销价，入目录时重验

### 46. asus-zenwifi-bt8-3-pack-white — ✅ 已核实（队列顶位）
- 品牌 / 型号：ASUS / ZenWiFi BT8 BE14000 Tri-Band WiFi 7 Mesh，3-pack，White
- 队列标注：第六批后备队列。目录已有 2-pack `asus-zenwifi-bt8-2-pack-white`（verified，MPN BT8(W-2-PK)，UPC 197105532045），3-pack 为独立款型（pack 规格不同款），不撞号
- MPN：BT8(W-3-PK) —— ASUS 美国官网 Tech Specs 三档并列（BT8(W-3-PK)/BT8(W-2-PK)/BT8(W-1-PK)）；Microless 规格表同款。已核实
- UPC：197105532090（校验位有效）—— B&H 规格页（零售商）+ SHI（分销商，UPC 栏）两源一致，符合零售商+分销商先例；亚马逊同款亦为此码（仅作旁证，不作价格来源）。已核实
- 价格行：B&H 自营 $699.99，InStock，Add to Cart（划线 $849.99，Holiday Savings $150）；ASUS eShop 美国直营同价 $699.99
- 待定项：无标识待定；仅入目录时重验 live 价（黑五促销价）

### 47. asus-zenwifi-bt10-1-pack-white — ✅ 已核实（队列顶位）
- 品牌 / 型号：ASUS / ZenWiFi BT10 BE18000 Tri-Band WiFi 7 Mesh，1-pack，White
- 队列标注：第六批后备队列。目录已有 2-pack `asus-zenwifi-bt10-2-pack-white`（pending，线索 UPC 197105429895 仅 B&H 单源），1-pack 为独立款型，不撞号。注意 1-pack UPC 与 2-pack 线索 UPC 不同（…9833 vs …9895），不得混同
- MPN：BT10(W-1-PK) —— ASUS 美国官网 Tech Specs 三档并列；DirectDial 制造商件号同款。已核实
- UPC：197105429833（校验位有效）—— B&H 规格页（零售商）+ DirectDial（分销商，MFG PART BT10(W-1-PK) + UPC 同框）两源一致，符合零售商+分销商先例；另有 Snapklik/Desertcart 镜像同码（旁证）。已核实
- 价格行：B&H 自营 $346.00，InStock，Add to Cart；ASUS 美国官网 $359.99，InStock
- 待定项：无标识待定；仅入目录时重验 live 价

### 48. asus-tuf-gaming-m3-gen-ii-black — ⏳ pending（队列顶位）
- 品牌 / 型号：ASUS / TUF Gaming M3 Gen II Wired Gaming Mouse，Black（P309）
- 队列标注：第六批后备队列。目录无 M3 Gen II（仅有 TUF M4 Air 与 TUF K3 Gen II），不撞号
- MPN：90MP0320-BMAA00（美版；B&H MFR # + ASUS eShop 美国一致），已核实。注意勿与非美版 `90MP0320-BMUA00`（EAN 4711081909118，欧洲/新加坡渠道）混同；另 eShop 美国另有一页 Part Number 为 `90MP0320-BMAA03`，性质未明（疑似替换 SKU/套装），入目录时复核 BMAA00 vs BMAA03
- UPC：lead 195553909112 —— 唯一线索 NationalPC 印度站单源（校验位有效），无第二来源；EAN 4711081909118 绑定的是非美版 BMUA00，不能转作美版 UPC。按规则 pending
- 价格行：Adorama 自营 $25.99，InStock（JSON-LD，标题 Black）。ASUS eShop $24.99 缺货、B&H 已停售（No Longer Available，旧价 $28.64），均不用作主价行
- 待定项：① UPC 无第二来源；② BMAA00 vs BMAA03 待入目录时复核；③ 59g/8000 DPI 有线入门鼠，价位低但为 TUF 主流型号

### 49. 8bitdo-sn30-pro-hall-effect-g-classic — ⏳ pending
- 品牌 / 型号：8BitDo / SN30 Pro Wireless Controller with Hall Effect Joysticks，G Classic（Model 80DJ04）
- MPN：80DJ04 —— Best Buy Model 栏（灰色款为 80DM02，不同款）。**pending（仅 Best Buy 单源）**。注意 Best Buy 存在两个 G Classic SKU（6590319 与 10189263），同为 Model 80DJ04；本次以 Sold by Best Buy 的 6590319 页为准
- UPC/EAN：lead 6922621509547（13 位 EAN，校验位有效）—— 仅 Target 规格页一源（$44.99，InStock）；B&H 未见上架该款，无第二来源。按规则 pending。Hall Effect 版与旧版（普通摇杆）同名，须以 "with Hall Effect Joysticks" + Model 80DJ04 钉死，不得与旧版混同
- 价格行：Best Buy 自营（Sold by Best Buy）$34.99，InStock，Add to Cart，黑五价（对比价 $44.99）；Target $44.99，InStock，为第二价行。注：Best Buy 价在 11-04/11-12 抓取中为 $33.99，现已变为 $34.99，入目录时重验
- deal-site 证据：Slickdeals frontpage 2026-11-04（$33.99 Best Buy）与 2026-11-12（$32.99 Amazon / $33.99 Best Buy，Amazon 价不用）；DealMoon 2026-11-13 前后 $33.99 Best Buy（Editor's Pick）；Slickdeals Threads 2026-11-13 $33 Best Buy
- 待定项：① EAN 需第二来源（B&H 无货，可试 Adorama/Newegg 规格页）；② 两个 Best Buy SKU 的关系待入目录时确认

### 50. microsoft-xbox-wireless-controller-forza-horizon-6-limited-edition — ✅ 已核实
- 品牌 / 型号：Microsoft / Xbox Wireless Controller，Forza Horizon 6 Limited Edition（半透明青 + 粉色握把，2026-05-19 上市）
- MPN：EP2-42276 —— Walmart Model 栏、GameStop Vendor Part Number、Lenovo 美国 Manufacturer PN 三源一致，已核实
- UPC：196388601059（校验位有效）—— GameStop 美国零售商规格页（UPC 栏 + Vendor PN EP2-42276）+ goWholesale（分销商，同款 UPC+MPN）两源一致，符合零售商+分销商先例；另有 eBay 产品页同码（旁证，不用）。已核实
- 价格行：Walmart 自营（sold/shipped by Walmart，Slickdeals 注明）$49.00，was $84.00；另有 Amazon $49.00（按规则不用作价格来源）
- deal-site 证据：Slickdeals frontpage 2026-11-19
- 待定项：① **LE 款定性请批示**：限量联名款但仍在 Walmart/Best Buy/GameStop 大面积有货、非清仓，是否纳入由批复定；② 入目录时重验 live 价（黑五促销价）。目录仅有黑色标准款 `xbox-wireless-controller-black`（verified，1914，196388518159），LE 为独立配色款，不撞号

## Membership 检查（协调自跑，非转述分轨数）

- 脚本：`data/rework8/membership_batch8.py`（对照 `data/rework8/catalog_ref_550.tsv`，550 行；key、型号名子串双向归一化、MPN、UPC 四项 + 批内重复）
- 结果：**raw hits: 0**——50 款全部无撞库（key/型号名/MPN/UPC 均无命中），批内无重复 key/MPN/UPC。
- 追加验证：候选全部标识字符串对 TSV 全文做原始子串 grep（含 193 个散文式 UPC 单元格，如 "UPC pending — lead …"），仍为 0 命中。
- 对照表自检：TSV 共 550 行，216 行带 MPN、417 行带 UPC，status 分布 verified 229 / pending 274 / 空 47（空的 47 条即第七批发现的缺 `status=` 字段，未动）。
- 未采纳的冲突码（不写入 TSV，故不在脚本覆盖内；由各分轨在自查时逐一对照过，0 撞库）：Echo Dot Max 的 4 个聚合器码、Echo Time 的 2 个、WHOOP 的 2 个、Delta II 白的 2 个 UPC + 2 个 MPN 后缀、Keris 白的 2 个 UPC、razr ultra 的 2 个 UPC、QM6K Pro 的 2 个 UPC、Legion 5i 的争议 UPC 198155802546。

## 协调剔除的 7 款（57 轨推 → 50 入草稿）

| 款 | 轨 | 剔除理由 |
|---|---|---|
| Echo Dot Max（重复计） | A+B | 两轨各自推了同一款（MPN B0D6SX8VLQ），只计一次；不是落选，是去重 |
| Pioneer Karved PBS2W | A | 最弱项：UPC 未找到、颜色未定（Sam's 两个 item number 对应白/黑未确认）、Sam's Club 独家款、品牌官网未列出该款；Track A 自标“入选与否请定夺” |
| CMF Headphone Pro Dark Gray | A | MPN 未找到（Nothing 官方未列 B1xx 型号码）；EAN 6974434226722 仅 Target 单源；标识 profile 最弱 |
| B&W Px7 S2e Forest Green | A | Px7 S3（FP45330，$479）已接替，S2e 有清仓尾货风险；Amazon 双 UPC 歧义（714346342617 vs 714346342631）未解；Crutchfield 行 $399 非黑五价 |
| Govee Smart Floor Lamp 3 | B | UPC 无线索；智能照明是目录无先例的新子品类（智能家居先例只到音箱/显示屏），且 Govee 为预算智能家居品牌 |
| Motorola razr ultra 2025 512GB Scarab | C | UPC 冲突未解（840023284427 vs 840023270826，两个号都不写）；按第六批 Kiyo Pro Ultra 先例，标识冲突未解即剔除 |
| TCL QM6K Pro 65" | D | UPC 冲突未解，且两码（846042032155 / 846042043069）皆属非 Pro 的 65QM6K，Pro 自身 UPC 无线索；另 Costco 库存信号不稳（一次 OutOfStock、一次 $599.99） |

## 分轨剔除的有名款（节选；完整清单见各 track 文件）

- **Track A**：Harman Kardon Onyx Studio 8（已在目录）、Samsung Music Studio 5（已在目录）、Echo Show 8 2025（已在目录）、Sony ULT FIELD 3（已在目录）、Shokz OpenRun（第七批已入）、MTW4（第七批已入）、Sonos Era 100（第七批已入）、Bose QC Cypress Green（颜色变体，撞目录同款黑）、Bose QC 2nd Gen（已在目录）、Beats Solo 4 Metallic Pink（Amazon 独家色）、Shokz OpenRun Pro 一代（2022 旧款）、Monoprice Monolith AMT / DALI SONIK 5 / TALIX / Koss / HIFIMAN / Baseus（小众发烧或 AliExpress 行）、Soundcore Q20i 翻新、Fosi CD 机（非音频类）、Logitech G Yeti GX（麦克风）。
- **Track B**：Galaxy Buds3 Pro / Buds4 Pro、AirPods Pro 3 / AirPods Max 2、Watch Series 12、Watch8 Classic、Echo Show 8 / Echo Hub（均已在目录）；Garmin vívoactive 5（2023 旧款清仓）、Harman Kardon SoundSticks 4（2021 旧款清仓）；Kindle Paperwhite / Colorsoft（已在目录）；Ring / eufy / Reolink 安防全系（智能家居安防排除）；Insta360 X6 / X4 Air / GO Ultra（相机品类，转 Track F）；Galaxy Z Fold8（手机，转 Track C）；Rokid Max 2 / AR Spatial、Bee Frontier、Memoket、Casio Moflin（小众）。
- **Track C**：Watch Ultra 3 翻新（翻新排除；新品已入选 C1）、Oura Ring 5 Size 9（UPC 全无线索，留后备）、Galaxy Tab A11+（已在目录）、AirTag 2nd Gen 4-pack（已在目录）、翻新 iPad 8th Gen、Galaxy S25 Ultra（当日全为翻新行）、Galaxy Z Fold8 / Pixel 11 Pro / iPhone 17 / Galaxy S25（未核实直营行与标识，overflow）；**队列三款**：Watch Ultra 一代（无干净直营新品行——Best Buy 行为第三方 YY Wireless，Abt 已下架，三星官网已换 Ultra2）、Buds2 Pro（无干净直营新品行、2022 旧款），均不带入；Tab S10 FE 256GB 带入（C4）。
- **Track D**：三星 G6 G60SD（UPC 已核实但 Best Buy "no longer available in new condition" + 清仓 $179.99）、G8 G80SD（Best Buy 挂 Clearance $1,169.99）、HW-B650 旧款（清仓，已被 HW-B650F 取代）；Hisense E6SR 50"（复查仍不达标：Best Buy 无 listing、Walmart 仅翻新 55"、hisense-usa.com 无产品页、MPN 仅 Smartprix 单源、UPC 无线索，继续留队列）；S90H 55"/77"（同系列不同尺寸，只取 65"）；LG G6、Sony BRAVIA 6、TCL QM8L、Samsung M70H TV、U8000H、Hisense QD5SF 98"、TCL 98Q5CF、LG QNED84BUA（Sift 热门，本次未核标识，留后续线索）；HW-Q930H（仅 open-box）、JBL Bar 500MK2 / HW-B400F / HW-B750F（仅 Amazon 价）、Sonos Ray / Era 300 / Era 100 SL（未核标识或仅 Amazon 价）、Odyssey G61SH / G50SF / G80SH（EPP 门控价）、ROG PG32UCDM3（仅 Amazon 价）、Roku Pro Series（未核标识）、Hisense 50QD6SR / 50M7SR（未核标识）、JBL Cinema SB550（未核标识）。
- **Track E**：ROG Strix G16、MacBook Air M5、Legion 5a、Yoga Slim 7x（均第七批已入）；Acer Predator Helios Neo 16S（eBay 翻新）；OMEN Transcend 14 32GB 同系（Best Buy 已死）；Legion Pro 7 1TB 配置（另一配置、MPN 未知、已过期）；Alienware 32GB 同系（$999.99 帖为一年前）；**留队列**：T16 21QN0045US（双标识已核实、无 live 直营行）、T14 Gen 5 Gray（双标识已核实、B&H 停售 + Adorama 2027-01 到货）、Vivobook S 14（MPN 已核实、UPC 仅 eBay、Best Buy 已死）、Legion 5i（Walmart 第三次机器人墙 + UPC 争议）。
- **Track F**：DJI Osmo Action 6 Standard/Adventure Combo（未核实 MPN/UPC、无美零售商自营行，留队列）；Insta360 Ace Pro 2 标准版（未核实标识，留队列）；DJI Osmo Nano（未核实）、DJI Mic Mini（未核实，配件候补第一位）、DJI Osmo Pocket 4（美国不售）、DJI Neo 一代（清仓旧款）、GoPro HERO12（上一代清仓）、HERO13 Accessory Bundle（UPC 三方冲突）；X5/X6/HERO13 的 Costco/Best Buy 捆绑包（同机不同捆绑 SKU，不另立款）；**复查仍不达标**：Osmo 360 Skiing Combo（DJI 直营缺货、无 MPN、UPC 仅 Amazon 单源线索 190021996731）、TCL Q6CH（Costco.com 线上仍缺货，$199.99 仅为仓库价；Walmart 行无法核实自营身份）。
- **Track G**：Scope II 96 白色 NX Snow 款（美国 UPC 未找到，仅欧盟 EAN）、ROG Delta II-KJP 联名版（Best Buy 清仓 $188.99）、DualSense 各色翻新机、Corsair K70 CORE RGB 翻新机、Razer Basilisk V3 Pro 白色（仅聚合器单源价）、8BitDo Pro 2 Hall Effect（仅 Amazon 价源）、MSI Forge / SABLUTE 键鼠套装（廉价套装、仅 Amazon 价）、Xbox 标准款各色（黑色已在目录，其余未逐款核标识）。

## 入目录前加时复核清单（点头后另做，本草稿不做）

1. 全部 50 款重验 live 价与库存信号（多为黑五促销价，11-28 前后可能变动）。
2. C1/C2 的 UPC 在 Best Buy 规格页复核（195950484311、195950638004），复核通过可升已核实。
3. C4 的 $469.99 确认为 Best Buy 全新自营行（非 open-box / 非 Merchant Expo 第三方行）。
4. C6 的 $799.99 确认为裸机解锁价（非 $699.99 连网价）；Light Gold $999.99 是否同降。
5. C7 的 Google Store $749 在官网实页复核，再定写 $749 还是 Best Buy $999.00。
6. C8 的 oneplus.com $799（码 EXTRA100）官网实页复核。
7. B2 Onyx Studio 9 的 Newegg $219.50 核实为 Newegg 自营而非 marketplace 卖家。
8. B3 Venu X1 的尺寸口径以 Garmin 官方为准（46mm 表壳 / 2 英寸屏，Best Buy 称 51mm）。
9. E2 Alienware 16 Aurora：确认 AntOnline 行作为 tier 是否接受。
10. E6 Book5 360：确认 Connection/Quill 行作为 tier 是否接受。
11. D5 M70F 43"：复核 Samsung US $499.99 是否仍为常规在售（非清仓）。
12. D4 SB580：复核 Walmart 线上 $199.00 是否仍在（门店清仓 $50 帖并存）。
13. D1 S90H：UPC 冲突项（198957270574 vs fillion.ca 198957276095）以 Best Buy 规格页 "Other" 栏为准再核一次。
14. F7 HERO13 Black：B&H 暂缺货（预计 Dec 07 到货），加行时重查库存。
15. F4 Neo 2：确认 B&H/Adorama 行仍为自营在售（未上 DJI 美国官网）。
16. G1 Delta II 白：美版 MPN 后缀（BHAA10 vs BHUA10）以美版实物或 Best Buy 规格页复核；白色款 UPC 需美国零售商规格页第二来源。
17. G2 Keris 白：UPC 冲突（197105394612 vs 197105394582）待美国零售商规格页裁决；eShop $94.99 是否覆盖白色按颜色复核。
18. G3 Scope II 96 白 Storm：UPC 需 Best Buy 或 B&H 规格页第二来源；eShop $131.99 重验。
19. G6 M3 Gen II：复核 BMAA00 vs BMAA03。
20. G7 SN30 Pro：两个 Best Buy SKU（6590319 与 10189263）的关系确认；EAN 需第二来源。
21. G8 Forza LE：LE 款定性由批复定（限量联名但大面积有货、非清仓）。
22. E3/E4 的 MPN 第二来源（LOQ：lenovo.com US 或 B&H；Zephyrus G14：ASUS US store 或 B&H）；E8 XPS 13 的 MPN 第二零售商与 UPC 第二来源。
23. D7 剔除款 QM6K Pro 不进入加时复核，留队列；同理 razr ultra、Karved、CMF、Px7 S2e、Govee 均不进入。

## 后备队列（本次未入选，供第九批起草）

- **Track D 备选（5）**：XG27UCSR（MPN 已核实，UPC pending 无线索）、XG27AQWMG（MPN 已核实，UPC pending 无线索）、VG27AQ1A（MPN 已核实，UPC pending 无线索）、TCL S55H（MPN 已核实，UPC pending 无线索）、TCL 27G64（MPN 已核实，UPC 846042043243 两聚合站一致 + 一家冲突待复核）。
- **Track B 备选（5）**：Ray-Ban Meta Gen 3 Aviator Havana Brown Transitions（Best Buy $529.00，MPN 口径未定 SK-1002183-01 vs RW4016，UPC 未找到）、Meta Nova（Meta 直营 $322.15，未核标识）、RingConn Gen 2（Amazon $199.50，未核标识，品牌小众）、CMF Watch 3 Pro / Buds 2a / Headphone Pro / Speaker S（未核标识）、UGREEN Clipbuds Pro 2（Amazon $59.99，未核标识）。
- **Track E 未研究线索（5）**：ASUS Zenbook S14 UX5406AA（Best Buy $1,299.99）、MSI Prestige 16（Costco $1,200）、Dell 16S（Best Buy $800）、HP OmniBook X 16（Best Buy $900）、ASUS ROG Strix G18（Costco $2,000）。
- **Track C overflow（5）**：Galaxy S25 Ultra 256GB、Galaxy Z Fold8、Pixel 11 Pro、iPhone 17 256GB、Galaxy S25（均未核实直营行与标识）。
- **Track F 队列（3）**：Osmo Action 6 Standard Combo、Ace Pro 2 标准版、DJI Mic Mini（配件候补第一位）。
- **Track A 后续线索（5）**：JBL Tune 720BT、Soundcore Space One、Beats 360 Wireless、Nothing Headphone (1) 原版、Nothing Headphone (a)。
- **Track D 后续线索（9）**：LG G6 OLED 65"、Sony BRAVIA 6 OLED 55"、TCL QM8L、Samsung M70H TV、Samsung U8000H、Hisense QD5SF 98"、TCL 98Q5CF、LG QNED84BUA 75"、Roku Pro Series 55"/65"、Hisense 50QD6SR / 50M7SR、Sonos Ray / Era 300、Samsung HW-Q60CF、JBL Cinema SB550。
- **Track G 暂缓（3）**：Scope II 96 白色 NX Snow 款、Razer Basilisk V3 Pro 白色、8BitDo Pro 2 Hall Effect。
- **留队列（9）**：Legion 5i（Walmart 墙 + UPC 争议）、T16 21QN0045US（无 live 直营行）、T14 Gen 5 Gray（无 live 直营行）、Vivobook S 14（无 live 直营行）、Hisense E6SR 50"（复查仍不达标）、Osmo 360 Skiing Combo（复查仍不达标）、TCL Q6CH（无线上行）、VG279QM5F（无直营在库行）、ThinkVision P27u-20（2021 旧款、无品牌直营在库行）。
- **本次剔除款复查口径**：Karved、CMF Headphone Pro、Px7 S2e、Govee Floor Lamp 3、razr ultra、QM6K Pro 下批复查时须有新证据（新来源/新行/冲突解决）才可重推，不得原样重推。

## 未动项声明

- 本草稿只写 `data/candidates_batch8_600.md`、`data/rework8/candidates_batch8_50.tsv`、`data/rework8/membership_batch8.py` 与 `data/rework8/trackA–G.md`；未动 `price_agent/catalog.py`、`DECISIONS.md`、快照、站点。
- 本批只备草稿、等用户点头才入目录；加时复核在点头后另做。
