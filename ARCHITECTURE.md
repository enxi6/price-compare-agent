# 架构

## 一句话架构

```
用户查询 → 标识归一（UPC/MPN/SKU）→ 多商家适配器并行取价
        → 到手总价计算 → 排名（总价 → 到货 → 信誉）→ 透明账单输出
```

## 模块

| 模块 | 职责 | 当前状态 |
|---|---|---|
| `price_agent/models.py` | Offer / Product 数据模型、总价计算 | 已实现 |
| `price_agent/adapters.py` | 商家适配器接口 + 模拟商家 | 已实现（模拟） |
| `price_agent/ranking.py` | 排名：总价 → 到货天数 → 商家评分 | 已实现 |
| `price_agent/cli.py` | 命令行入口 | 已实现 |
| 真实商家适配器 | 官方 API / Feed / 目录接入 | Phase 1 |
| 价格追踪器 | 定时复查 + 降价提醒 | Phase 2 |
| 约束校验器 | 白名单 / 上限 / 预算帽，下单前强制校验 | Phase 3 |

## 数据模型（核心字段）

```python
Offer(
    merchant: str,          # 商家名
    title: str,             # 商家商品标题
    identifier: str | None, # UPC / EAN / MPN / 官方 SKU，同款主键
    price: float,           # 商品价
    shipping: float | None, # 运费；未知 = None，绝不按 0 算
    tax_estimate: float,    # 预估税费（需注明税率口径）
    coupon: float,          # 可用公开优惠（无 = 0）
    delivery_days: int | None,
    seller_rating: float | None,  # 0–5
    url: str,               # 商品页链接
    in_stock: bool,
    fetched_at: str,        # ISO 时间，价格过期判断依据
)
total = price + (shipping or 0) + tax_estimate - coupon
# 但 shipping 未知时，总价要标注“不含未知运费”，不得假装是全包价
```

## 排名公式（Phase 1，不搞黑箱分）

1. 主键：运费已知的按到手总价从低到高；运费未知的排在所有运费已知者之后
   （其总价只是下限、不可比），并标注“不含未知运费”。
2. 同价（差额 < $1）：到货天数短者优先。
3. 再同：商家评分高者优先。
4. 标识对不上的商品不进主排名，进“疑似同款”附表。

Phase 2 起，质量信号只作展示与同价 tie-break，不并入加权总分——
加权分一旦不透明，买方就没法审计 agent 到底为谁服务。

## 数据源梯队（重申 README 的合规线）

官方 API / Feed > 联盟目录 > 商家结构化数据 > 浏览器只读复核。
任何一档被屏蔽、要求登录后才能看价、或 ToS 明确禁止的，停在该档，
记入公开报告，不绕过去。

## 下单约束（Phase 3 预留，提前定死接口）

```yaml
constraints:
  allowed_merchants: []   # 空 = 不允许任何自动下单
  max_per_order: 0         # 单笔上限，0 = 关闭
  total_budget: 0          # 总预算帽
  require_confirmation: true  # 每次下单前必须用户点头
```

约束校验发生在支付之前、且独立于排名逻辑：排名说“这家最便宜”，
约束说“这单能不能付”，两把锁分开。
