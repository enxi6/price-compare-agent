# 公开建造日志（Build in Public）

这个文件就是“开源整个过程”的载体：每一步做了什么、为什么、结果如何，
照实记，数字不好看也记。

## 001 — 2026-10-31：立项

- 起因：读了 Stripe CEO Patrick Collison 2026-10-09 的长文（个人 agent 为买方
  比价、奖励好产品），决定动手把“比价”一环做出来。
- 今天做的事：
  - 仓库骨架搭好：README / PLAN / ARCHITECTURE / DECISIONS / LICENSE / CONTRIBUTING
  - 比价核心最小实现 + 模拟商家 + 测试，可跑通 `python3 -m price_agent.cli compare`
  - 定下五条不可妥协的原则（见 DECISIONS 001–005）
- 当前状态：骨架可跑，商家是模拟数据；真实商家接入尚未开始。
- 待定：GitHub 公开库的发布方式、第一个品类、目标市场（默认美国 + 标准化电子产品型号）。
- 下一步：Phase 1 同款标识归一 + 到手总价 + 透明账单；先定 20 个型号的评测集。

## 002 — 2026-10-31：Phase 1 开工（评测集 + 标识匹配 + 目录快照）

- 用户说“开始”，未改默认值：按 DECISIONS 005 执行（美国市场、标准化电子产品型号）。
- GitHub 公开库已建成：https://github.com/enxi6/price-compare-agent（Public），
  13 个 Phase 0 文件已通过网页上传上站；注意本地 git 历史与远程上传历史不同步，
  本次 Phase 1 先只做本地提交，推送前须先处理历史差异（见文末待定）。
- 今天做的事：
  - 20 个型号评测集（`price_agent/catalog.py`）：6 个已核实标识（UPC/MPN 以零售商或
    厂商页面为准，且按颜色/版本钉死变体——XM5 黑与银、AirPods Lightning 与 USB-C、
    MX Master 3S 各版本 UPC 各不相同，混用即错）；其余 14 个标识留空待核实，绝不编造。
  - 标识匹配模块（`price_agent/identity.py`）：仅标识匹配进主排名；GTIN-14 与 UPC-12
    归一化后可匹配；标题相似只进疑似表。
  - Tier-1 适配器（`price_agent/adapters_shopify.py`）：Shopify 店铺公开商品 JSON 接口，
    运费/税费不编造（运费未知、税费 0），被屏蔽即抛错停住；测试用桩数据，不联网。
  - 目录快照（`data/eval_snapshots.json`，Meta Catalog 2026-10-31 采集）：12 条真实报价，
    覆盖 5 个已核实型号；Buds2 Pro 白色无干净报价，是覆盖缺口不是 0 元。
    目录源不给 UPC，所以快照报价全部落在疑似表、主排名 0 家——这是规则在起作用，
    不是 bug；下一步需要返回标识的源（官方 API/Feed）才能把匹配率做上去。
  - CLI 新增 `compare --model` 与 `eval`：`eval` 现报 20 型号、6 已核实、5 有快照、
    报价 12、匹配 0、疑似 12。
  - 测试从 8 个增至 18 个，全过；另修了首个提交误把 `__pycache__` 入库的问题
    （加 .gitignore 并从索引中移除）。
  - 抓到的反作弊实例已记入快照 excluded_traps：T-Mobile 的 Bose $37.50 是月付价、
    Switch 捆绑包、翻新机、颜色错位、变体错位，都是 Phase 2 反作弊的现成用例。
- 不好看的数字照实记：匹配率 0%、快照覆盖 5/20、标识核实 6/20。
- 待定：本地提交与远程上传历史的合并方式（推送前定）；Shopify 适配器尚未接真实店铺
  （需先核实店铺域名与商品 handle，不得猜 URL）；其余 14 个型号标识待核实。

## 003 — 2026-10-31：第一波标识核实（6/7）+ 实店 CLI

- 第一波 7 个型号，核实 6 个，已核实总数从 6 升至 12：
  - WF-1000XM5 黑（WF1000XM5/B）：UPC 027242925601（Adorama + 亚马逊美 + Abt + eBay 一致；
    国际版与捆绑包 UPC 不同，已排除）。
  - AirPods 4 USB-C（MXP63LL/A）：UPC 195949688522（Adorama + B&H + 亚马逊美一致；
    印度版与 ANC 版是不同产品，已排除）。
  - Watch SE 2 40mm GPS 午夜（MXE93LL/A）：UPC 195949641756（Micro Center 单一来源，
    表带尺寸未在来源中确认，已在条目中标注；其他颜色/表带/蜂窝/年份 UPC 各不相同）。
  - Kindle Paperwhite 16GB 2024 黑（B0CFPL6CFY）：UPC 840268942847（PBTech 新澳单一卖家）。
  - MX Keys S：纠正——920-011559 是浅灰不是石墨灰（石墨灰是 920-011406），
    条目已改名并钉为浅灰，UPC 097855187857。
  - Switch Lite 绿松石（HDHSBAZAA）：UPC 045496882266（eBay + Desertcart + Ubuy 一致；
    加拿大翻新码已排除）。
  - 未核实：Keychron K8 Pro——直营店用 SKU（K8P-G1 等）而非 UPC，且 SKU 按配置分；
    K8（非 Pro）的 UPC 不得挪用，条目保持 pending 并写明原因。
- CLI 新增 `compare --model … --shopify store/handle`：跑通实店公开商品 JSON → 标识匹配
  → 排名的完整链路；被屏蔽即停住报错，不绕行。
- Keychron 实店端点验证已交浏览器只读检查（店铺 www.keychron.com，
  handle keychron-k8-pro-qmk-via-wireless-mechanical-keyboard，来自搜索结果 URL），
  结果回来后再写进日志；本提交不含未经验证的实店断言。
- 测试仍 18 个，全过；eval 现报 20 型号、12 已核实、5 有快照、报价 12、匹配 0、疑似 12。
- 待定：第二波 7 个型号标识；Keychron 端点验证结果；本地与远程历史合并方式。

## 004 — 2026-10-31：第二波标识核实（6/7），评测集 18/20

- 第二波 7 个型号，核实 6 个，已核实总数从 12 升至 18：
  - Xbox 手柄碳黑 Series X|S（1914）：UPC 196388518159（PayMore + eBay 一致；
    老款 QAT-00001 码与另一 PayMore 码已排除为不同版本）。
  - Quest 3S 128GB（SK-1000926-01）：UPC 815820025825（B&H + 亚马逊美 + PayMore 一致；
    新加坡、新西兰、翻新版 SKU 各不相同）。
  - Anker 737 120W 美版插头（A2148）：UPC 194644099008（Swiftsly + Ubuy 一致，
    EAN 0194644099008 为同一码的 GTIN 形式；英版插头是另一参考）。
  - Magic Mouse USB-C 白（MXK53AM/A）：UPC 195949655883（苹果官网；
    新西兰码与黑色版已排除）。
  - G Pro X Superlight 2 黑（910-006630）：EAN 5099206104525（多家欧洲零售商一致；
    美版 UPC 未单独确认，以 GTIN 族的 EAN 为准；910-006631 仅包装地区不同）。
  - Pixel Buds Pro 2 瓷白美版（GA05760-US）：UPC 840244604448（B&H + DirectDial 一致；
    840244604516 组与澳洲码为其他地区版）。
  - 未核实：DualSense 白——UPC 三方冲突（亚马逊美 711719574293、新澳 PBTech
    711719575856、其他 711719541080），无干净一致口径，宁可空着等美版厂商页二次确认。
- 评测集剩余 pending 仅 2 个：Keychron K8 Pro（SKU 制）与 DualSense 白（UPC 冲突）。
- 测试仍 18 个，全过；eval 现报 20 型号、18 已核实（快照报价仍 12 条、匹配仍 0，
  因新核实型号暂无快照报价——标识齐了，下一步是给它们补报价源）。
- Keychron 端点浏览器验证结果尚未返回，仍 blocked，不催、不重复派发。

## 005 — 2026-10-31：Keychron 实店端点验证通过，评测集 19/20

- 浏览器只读验证（未加购、未登录、未购买）：Keychron 官网公开商品 JSON
  （keychron-k8-pro-qmk-via-wireless-mechanical-keyboard）可正常加载、无屏蔽，
  标题 Keychron K8 Pro QMK/VIA Wireless Mechanical Keyboard，共 31 个变体。
- 关键纠正：上一条说“Keychron 用 SKU 而非 UPC”是错的——JSON 里每个变体都有 barcode，
  如 K8P-G1（黑、全组装热插拔、白光、Gateron G Pro 红）barcode 4895248806837，
  K8P-G2 为 4895248806844。K8 Pro 条目已按 K8P-G1 配置钉死并升为 verified，
  评测集已核实总数升至 19/20，仅剩 DualSense 白（UPC 冲突）。
- 真 bug 一个：该端点的变体对象不含 available 字段；旧适配器逻辑会把缺字段
  当成缺货，导致全部变体沉底。已修复：缺字段 = 库存未断言（视为已上架），
  并在 CLI 实店路径打印库存须到商品页核实的说明；另加回归测试。
- 测试从 18 个增至 19 个，全过。
- 待定：DualSense 白 UPC 冲突的二次确认；本地与远程历史合并方式。

## 007 — 2026-10-31：Apple 型号组加入评测集（8/8 核实）

- 用户批准后新增 8 个 Apple 型号，全部按基础配置 + 颜色钉死 part number，
  评测集从 20 扩至 28，已核实从 19 升至 27，仅剩 DualSense 白 pending：
  - MacBook Air 13 M4 星光色（MW0Y3LL/A）：UPC 195949837197
    （eBay + Bestpeek 一致，Best Buy 美国确认 MPN）。
  - MacBook Air 15 M4 天蓝色（MC7A4LL/A）：UPC 195949893162（两条不同 eBay 刊登一致）。
  - MacBook Pro 14 M4 深空黑（MW2U3LL/A）：UPC 195949507786
    （两条不同 eBay 刊登 + Back Market 一致；英/澳后缀为地区版）。
  - Mac mini M4（MU9D3LL/A）：UPC 195949080296（多条不同刊登一致）。
  - iPad A16 银色（MD3Y4LL/A）：UPC 195950086232（Best Buy 捆绑页 + eBay 一致）。
  - iPad Air M3 紫色（MCA04LL/A）：UPC 195949997952（两条不同刊登一致）。
  - iPad Pro M4 深空黑（MVV83LL/A）：UPC 195949222467（多条不同刊登一致）。
  - AirPods Max USB-C 午夜色（MWW43AM/A）：UPC 195949543890
    （Best Buy 美国 + 多条 eBay 刊登一致；eBay 目录页给出的另一码已排除）。
- 本轮教训：Apple 的颜色 = 不同 part number，条目必须钉颜色；Wi-Fi + 蜂窝版、
  Lightning 版、地区后缀版一律是不同 SKU，已在来源注记中排除。
- iPhone 仍排除在外（运营商分期/锁网使“最便宜”不可比），Apple 专场页面
  待 Phase 4 再议；下一步是给 Apple 组补报价源（Apple 官网与 Amazon/Best Buy
  均非 Shopify，需新适配器）。
