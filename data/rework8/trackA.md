# Track A — 第八批草稿：耳机 / 耳塞 / 音箱新缺口（Slickdeals 今日榜）

- 扫榜日期：2026-11-21（PT 当日；页面抓取时间为 2026-11-22 00:00–00:02 UTC）
- 来源 A：Slickdeals Tech 今日热门 https://slickdeals.net/deals/tech/（当日 40 条全扫）
- 来源 B：Black Friday Sift 热榜 https://slickdeals.net/sift/black-friday-deals（当日 Top 96，按 saves 排序，全扫）
- 补充：Slickdeals 站内 headphones 搜索 frontpage 榜（slickdeals.net/search/?q=headphones）——用于补齐当日耳机类热门，因 Tech 页当日音频条目过少
- 对照表：`data/rework8/catalog_ref_550.tsv`（550 款）。每款均已按 key、型号名子串（双向归一化）、MPN、UPC 四项撞库，零撞库（见文末撞库记录）。
- 规则：只认商家自营（品牌直营 / 零售商直售）；只认美版货；Amazon 独家价不作价格来源；eBay、翻新/开箱、运营商分期、清仓旧款排除；UPC 是唯一门，MPN 单独扶正为 0，无第二来源就 pending，绝不编标识。
- 未动 catalog.py、DECISIONS.md、快照、站点；未提交。

## 候选清单（8 款）

### 1. shokz-opendots-2-black — ✅ 已核实（MPN + UPC 双源一致）
- 品牌 / 型号：Shokz / OpenDots 2 Open-Ear Clip-On Earbuds（Black）
- MPN：E320-ST-BK-US —— B&H 商品页 URL slug + Abt 商品页（Model # E320-ST-BK-US），双源一致
- UPC：810202687523 —— B&H 规格页（实页抓取，L81）+ Abt 商品页（UPC # 810202687523），双源一致。另有一条冲突线索：Snapklik 给出 810221005445（单源、非零售商），与 B&H/Abt 不一致，采信 B&H + Abt，冲突已记录。
- 价格行：B&H $139.95（原价 $199.95，Holiday Savings $60），In Stock，Add to Cart（实页抓取 2026-11-22 00:01 UTC）。Slickdeals Tech 当日帖为 Violet 色 Amazon $119.97（$199.99 原价），颜色不同，Black 行以 B&H $139.95 为准。
- deal-site 证据：Tech 页当日帖（SHOKZ OpenDots 2，Violet，Amazon $119.97）；另在 Slickdeals headphones 搜索榜亦有热度。注意：OpenDots 2 并非第七批的 OpenDots Air（E210，目录已有），是 2026 年新款（Dolby Audio + Bassphere 2.0，BT 6.1）。
- 待定项：无。入选时按流程在 add time 再复核一次实页价/库存。

### 2. beats-solo-4-matte-black — ✅ 已核实（MPN + UPC 双源一致）
- 品牌 / 型号：Beats / Solo 4 Wireless On-Ear Headphones（Matte Black）
- MPN：MUW23LL/A —— Best Buy 商品页（Model: MUW23LL/A，SKU 6501020）+ B&H + Abt，三源一致
- UPC：195949121708 —— B&H 规格页 + Abt 商品页（UPC # 195949121708），双源一致
- 价格行：Best Buy $99.99（Black Friday Deal，原价 $199.99），InStock，Sold by Best Buy（Best Buy 实页，2026-11-21 抓取）。Slickdeals headphones 搜索榜 frontpage 帖为 Amazon Exclusive Metallic Pink $80——Amazon 独家色价不作价格来源，本款以标准色 Matte Black + Best Buy 行入选。
- deal-site 证据：Slickdeals headphones 搜索榜 frontpage（Beats Solo 4，Amazon Exclusive Metallic Pink，$80，5.3K votes）；Best Buy 黑五价 $99.99 为同款标准色当日价。
- 待定项：无。入选时按流程在 add time 再复核一次实页价/库存。

### 3. skullcandy-crusher-anc-2-black-tan — ⏳ pending（MPN 已核实，UPC 仅 eBay 线索）
- 品牌 / 型号：Skullcandy / Crusher ANC 2 Over-the-Ear Noise Canceling Wireless Headphones（Black/Tan）
- MPN：S6CAW-S978 —— Best Buy 商品页实页抓取（Model: S6CAW-S978，SKU 6580349），已核实
- UPC：lead 810145320808 —— 仅 eBay 多条 listing 一致给出（MPN S6CAW-S978 + UPC 810145320808），无品牌/零售商实页第二来源，按规则降级为 pending，不得当作已核实写入。
- 价格行：Best Buy $119.99（Black Friday Deal，原价 $239.99），InStock，Add to Cart，Sold by Best Buy（实页抓取 2026-11-22 00:01 UTC）。
- deal-site 证据：Slickdeals headphones 搜索榜 frontpage（$120，Best Buy，7.9K votes）；Slickdeals 专帖 f/20309634（$119.99）。
- 待定项：UPC 需在品牌官网规格页 / Abt / B&H / Walmart 实页上找到第二来源；若下次刷新仍无，维持 pending。注意与目录已有的 Crusher Evo（第七批）是不同型号，不撞库。

### 4. cmf-headphone-pro-dark-gray — ⏳ pending（EAN 仅 Target 单源，MPN 未找到）
- 品牌 / 型号：CMF by Nothing / Headphone Pro（Dark Gray）
- MPN：未找到。Nothing 官方未在公开页列出该款的 B1xx 型号码；搜索未确认，不编。
- UPC/EAN：6974434226722（13 位 EAN，697 前缀）—— Target 商品页（TCIN 1012346792，UPC 6974434226722）。单源，无第二来源，按规则 pending。注意：同款 Light Green 在 Target 为另一 EAN 6974434226746（$49，Out of Stock），各色 EAN 不同，入选必须按色区分，不得混用。
- 价格行：Target $49.00（reg $79.99），Target 直售。Amazon 同款亦为 $49（9to5Google / How-To Geek 黑五价），但 Amazon 价不作价格来源，仅作旁证。
- deal-site 证据：Slickdeals headphones 搜索榜 frontpage（CMF by Nothing Headphone Pro，$49，Amazon，13.5K votes）；Nothing 官方黑五降价（9to5Google 2026-11-13：$49，38% off）。
- 待定项：EAN 需第二来源（Amazon 商品页 / Nothing 官网 / Best Buy）；MPN 待查；Target Light Green 已缺货，Dark Gray 行以 add time 实页库存为准。

### 5. nothing-headphone-1-pro-black — ⏳ pending（MPN 已核实，EAN 两弱源一致）
- 品牌 / 型号：Nothing / Headphone (1) Pro（Black）
- MPN：B192 —— iFixit 设备页（Model number: B192）+ Best Buy Canada（Model: B192）+ Nothing 官网产品页，三源一致，已核实
- UPC/EAN：lead 6974434229471（13 位 EAN）—— Swiftronics 加拿大（Brand New UPC 6974434229471）+ Kogan 澳大利亚（TRR-N01-B192-01 / 6974434229471），两源一致但均为小型零售商/市场平台，非美零售商实页，按规则仍为 pending lead，不得当作已核实写入。
- 价格行：Nothing 美国官网 $399（定价，Digital Trends 2026-09-29）；Slickdeals headphones 搜索榜 frontpage 帖为 Amazon $319（原价 $399，6.5K votes）——Amazon 价不作价格来源，仅作 deal 证据；品牌直营行以 Nothing 官网 $399 为准，黑五价待 add time 复核。
- deal-site 证据：Slickdeals headphones 搜索榜 frontpage（$319，Amazon，6.5K votes）；9to5Google 黑五清单（Headphone (1) Pro $319，20% off）。
- 待定项：EAN 需美零售商（Target / Best Buy US / B&H）或品牌实页第二来源；注意与 2025 年原版 Headphone (1)（型号 B186）区分，Pro 为 2026-09-29 发布的新款（三单元 + xMEMS）。

### 6. bowers-wilkins-px7-s2e-forest-green — ⏳ pending（MPN 已核实，UPC 有歧义）
- 品牌 / 型号：Bowers & Wilkins / Px7 S2e（Forest Green）
- MPN：FP44555 —— Crutchfield 商品页（MFR # FP44555）+ Amazon 商品页（Model Number FP44555），双源一致，已核实
- UPC：lead 714346342617 —— Amazon 商品页列出两个 UPC（714346342617 / 714346342631），GTIN 00714346342617 对应前者，但无法确认哪一个属于 Forest Green 色，歧义未解，按规则 pending，不得二选一写入。
- 价格行：Amazon $199（原价 $399，Slickdeals 当日帖）；Crutchfield $399（定价，Add to Cart）。Amazon 价不作价格来源，Crutchfield $399 为直售行；$199 为 deal 价，仅作旁证。
- deal-site 证据：Slickdeals headphones 搜索榜 frontpage（Px7 S2e，Forest Green，$199，Amazon，11.9K votes）。
- 待定项：UPC 歧义（714346342617 vs 714346342631）需 B&H / Best Buy / B&W 官网规格页定色；另注意 B&H 已将 Px7 S2e 标注为由 Px7 S3（FP45330，$479）接替，S2e 有清仓尾货风险，入选前需确认仍在售、非停产清仓。

### 7. amazon-echo-dot-max-graphite — ⏳ pending（MPN 已核实，UPC 未找到）
- 品牌 / 型号：Amazon / Echo Dot Max（newest model，Graphite）
- MPN：B0D6SX8VLQ（Amazon ASIN 式型号码）—— Best Buy 商品页（Model: B0D6SX8VLQ，SKU 6642849），已核实
- UPC：未找到。Best Buy 规格页实页抓取未含 UPC；Amazon 技术参数页未列 UPC；定向搜索无结果。按规则 pending，不编。
- 价格行：Best Buy $119.99，InStock，Sold by Best Buy（Best Buy 实页，2026-11-21 抓取）。Slickdeals Tech 当日帖为 Amazon $49.99（原价 $119.99）——Amazon 独家价不作价格来源，仅作 deal 证据。
- deal-site 证据：Slickdeals Tech 当日帖（Echo Dot Max newest model，Amazon $49.99）；Gizmodo 当日 FB 帖亦报 $49.99（58% off）。
- 待定项：UPC 待查（Best Buy "See all specifications" 完整页 / B&H / Target 实页）。注意与目录已有的 Echo Show 8 (2025)、Echo Hub 不同款，不撞库。

### 8. pioneer-karved-pbs2w — ⏳ pending（MPN 已核实，UPC 未找到，颜色未定）
- 品牌 / 型号：Pioneer / Karved Series Portable Bluetooth Speaker（型号 PBS2W）
- MPN：PBS2W —— Sam's Club 商品页（Model #: PBS2W），已核实
- UPC：未找到。Sam's Club 商品页实页抓取被机器人验证拦截；定向搜索无 UPC 线索。按规则 pending，不编。
- 价格行：Sam's Club $49.88（原价 $99.88，50% off），Sam's Club 直售（会员仓储店）。
- deal-site 证据：Black Friday Sift 热榜当日（Pioneer Karved Portable Bluetooth Speaker，Sam's Club，$49.88，35 saves，Live Nov 12–Nov 24）。
- 待定项：① UPC 待查；② 颜色未定——Sam's 有两个 item number（990557708 / 990557719），店内陈列有白、黑两色，颜色与 item number 对应关系未确认，故 key 暂不带颜色后缀；③ Sam's Club 独家款（"Sam's Club Exclusive"），无其他零售商行，品牌官网亦未列出该款，属渠道独家而非全渠道主流款，入选与否请用户定夺。

## 标识 tally

| 款 | MPN | UPC/EAN | 状态 |
|---|---|---|---|
| Shokz OpenDots 2 Black | E320-ST-BK-US ✅双源 | 810202687523 ✅双源（B&H+Abt） | 已核实 |
| Beats Solo 4 Matte Black | MUW23LL/A ✅多源 | 195949121708 ✅双源（B&H+Abt） | 已核实 |
| Skullcandy Crusher ANC 2 Black/Tan | S6CAW-S978 ✅Best Buy | lead 810145320808（仅 eBay） | pending |
| CMF Headphone Pro Dark Gray | 未找到 | 6974434226722（仅 Target） | pending |
| Nothing Headphone (1) Pro Black | B192 ✅多源 | lead 6974434229471（两弱源一致） | pending |
| B&W Px7 S2e Forest Green | FP44555 ✅双源 | lead 714346342617（Amazon 双 UPC 歧义） | pending |
| Echo Dot Max Graphite | B0D6SX8VLQ ✅Best Buy | 未找到 | pending |
| Pioneer Karved PBS2W | PBS2W ✅Sam's | 未找到 | pending |

- 已核实：2 款（OpenDots 2、Solo 4）
- pending：6 款（其中 Crusher ANC 2、CMF、Nothing Pro、Px7 S2e 有 lead，Echo Dot Max、Karved 无 lead）
- MPN 已核实 7/8（仅 CMF 未找到）；UPC/EAN 已核实 2/8

## 撞库记录（对照 catalog_ref_550.tsv，550 款）

逐款查 key、型号名子串（双向归一化）、MPN、UPC 四项，全部零命中：
- `opendots-2` / E320-ST-BK-US / 810202687523：0 命中（目录仅有 OpenDots Air E210，型号不同）
- `solo-4` / MUW23LL/A / 195949121708：0 命中（目录仅有 Solo Buds、Studio Buds+，型号不同）
- `crusher-anc-2` / S6CAW-S978 / 810145320808：0 命中（目录仅有 Crusher Evo，型号不同）
- `cmf-headphone-pro` / 6974434226722：0 命中（目录无 Nothing / CMF 行）
- `headphone-1-pro` / B192 / 6974434229471：0 命中（目录无 Nothing 行）
- `px7-s2e` / FP44555 / 714346342617：0 命中（目录无 Bowers & Wilkins 行）
- `echo-dot-max` / B0D6SX8VLQ：0 命中（目录仅有 Echo Show 8 (2025)、Echo Hub，型号不同）
- `karved` / PBS2W：0 命中（目录无 Pioneer 行）

## 剔除的有名款及理由

当日两榜音频类帖子中被剔除者：
- Harman Kardon Onyx Studio 8（Tech 页，eBay $99.99）——已在目录（harman-kardon-onyx-studio-8-black，pending）；且当日唯一行是 eBay，按规则本就排除。
- Samsung Music Studio 5 HW-LS50H（Tech 页，Woot $214.99）——已在目录（samsung-music-studio-5-black，已核实 HW-LS50H/ZA，UPC 198957266393）。
- Amazon Echo Show 8 (2025)（Tech 页，Amazon $99.99）——已在目录（amazon-echo-show-8-2025-glacier-white，pending）。
- Sony ULT FIELD 3（Tech 页，Amazon $128）——已在目录（sony-ult-field-3-black，已核实）。
- Shokz OpenRun（Tech 页，Shokz 官网 $64.95）——第七批已入（shokz-openrun-gray-standard，已核实）。
- Shokz OpenDots 2 之外的 Shokz 帖：OpenRun Pro 2（Tech 页，Best Buy $85）——开箱价（Open-Box），按规则排除；且 OpenRun Pro 2 为旧款迭代，非新缺口。
- Sennheiser Momentum True Wireless 4（Tech 页，Amazon $149.98）——第七批已入。
- Sonos Era 100（Sift，Costco 2 件装 $329.99，38 saves）——第七批已入。
- Bose QuietComfort Cypress Green（headphones 搜索榜，Walmart $169）——颜色变体，撞目录 bose-quietcomfort-headphones-black（同款不同色），剔除。
- Bose QuietComfort Headphones (2nd Gen) / QC 2nd Gen 各色（搜索榜多帖）——已在目录（bose-qc-headphones-2nd-gen-black，已核实）。
- Bose QuietComfort SC Noise-Cancelling Headphones (2nd Gen)（搜索榜，Costco $180）——Costco 渠道变体，与目录 QC Headphones (2nd Gen) 型号名撞库嫌疑，未能确认其为独立 MPN 的 distinct 型号，按型号名子串撞库口径剔除，未深入核 MPN。
- Shokz OpenRun Pro 一代（搜索榜，Best Buy $90）——2022 年旧款，已被 Pro 2 取代，非新款，剔除。
- Beats Solo 4 Amazon Exclusive Metallic Pink（搜索榜，Amazon $80）——Amazon 独家色，未单独入选；同款以标准色 Matte Black + Best Buy 行入选（见候选 2）。
- Monoprice Monolith AMT（Tech 页，Amazon $506.38）——小众发烧耳机，非主流款，剔除。
- DALI SONIK 5 落地箱（Tech 页，Crutchfield $1,299/对）——小众 Hi-Fi，非主流款，剔除。
- TALIX AuraHalo G1 开放式耳夹耳机（Tech 页，Amazon $15.99）——无名品牌，剔除。
- Koss A550 / HIFIMAN Ananda Stealth / HIFIMAN SUNDARA / Baseus BH1 / Baseus Bowie MH1（搜索榜）——小众发烧或 AliExpress 行，按规则剔除。
- Soundcore Q20i 翻新（搜索榜，eBay $20）——翻新机，剔除。
- Fosi Audio Merak CD 机（Tech 页）——CD 播放器，不属耳机/耳塞/音箱类，剔除。
- Logitech G Yeti GX（Tech 页，Amazon $89.99）——麦克风，不属本类，剔除。
- Apple Watch Ultra 3 翻新（Tech 页）——翻新机且非音频，剔除。

## 未深入核实的后续线索（本次未入选，供下一轮参考）

- JBL Tune 720BT（搜索榜，Amazon $49.95，2.2K votes）——目录无此款，UPC 未核；Amazon 单一价源，需 B&H/Best Buy 行。
- Soundcore Space One（搜索榜，Costco 会员 $55，6.7K votes）——目录仅有 Space One Pro / Space 2 Pro，Space One 本体未入；UPC 未核。
- Pioneer Karved A70W 头戴耳机（Sam's Club 黑五 $129，原价 $199）——与 Karved PBS2W 同系列陈列，Sam's 独家，UPC 未核。
- Beats 360 Wireless Over-Ear（搜索榜，Amazon $249.95，1.3K votes）——型号真实性未核实（疑似 2026 新款，需确认），未入选。
- Nothing Headphone (1) 原版（搜索榜，$169）与 Nothing Headphone (a)（$109）——黑五降价热帖，但目录尚无 Nothing 品牌行；如 Track A 要补 Nothing 品牌线，这两款与 Headphone (1) Pro 可成组核，但本次只按 deal-site 新款口径推了 Pro。
