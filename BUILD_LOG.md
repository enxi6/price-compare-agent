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
