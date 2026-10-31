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
