import numpy as np
from decimal import Decimal

# M-Pesa agent reconciliation: float errors in money calculations

# 1. Ten deposits of KES 0.10 should total exactly KES 1.00
float_total = 0.0
for _ in range(10):
    float_total += 0.10
print("Float total of ten KES 0.10 amounts:", float_total)
print("Exact comparison with 1.00:", float_total == 1.00)
print("Tolerance comparison (np.isclose):", np.isclose(float_total, 1.00))

# 2. Accumulated error: 1,000,000 fee entries of KES 0.10 (true total = 100000.00)
n = 1_000_000
float_sum = 0.0
for _ in range(n):
    float_sum += 0.10
true_total = 100000.00
abs_err = abs(float_sum - true_total)
rel_err = abs_err / true_total
print(f"Float running total: {float_sum:.6f}")
print(f"Absolute error: {abs_err:.6f}")
print(f"Relative error: {rel_err:.3e}")

# 3. Safer approaches: whole cents (integers) and Decimal
cents_total = sum([10] * n)                 # 10 cents each, integer arithmetic
decimal_total = sum([Decimal("0.10")] * n)
print("Integer cents total (KES):", cents_total / 100)
print("Decimal total (KES):", decimal_total)