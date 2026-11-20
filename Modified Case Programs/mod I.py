import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

# M-Pesa agent break-even point.
# n = number of transactions per day.
# Revenue: KES 30 average commission per transaction.
# Cost:    KES 1200 fixed (rent + attendant) + KES 8 per transaction
#          + 40*sqrt(n) for float handling and queue costs (grows with volume).
# Break-even: profit(n) = 0
FIXED = 1200.0

def profit(n):
    return 30*n - (FIXED + 8*n + 40*np.sqrt(n))

# Bisection: profit is negative at 10 transactions and positive at 200
solution = root_scalar(profit, bracket=[10, 200], method="bisect", xtol=1e-10)

# Fixed-point form: n = (FIXED + 40*sqrt(n)) / 22
def g(n):
    return (FIXED + 40*np.sqrt(n)) / 22

n = 100.0
history = [n]
for _ in range(100):
    n_new = g(n)
    history.append(n_new)
    if abs(n_new - n) < 1e-10:
        break
    n = n_new

print(f"Bisection break-even: {solution.root:.4f} transactions per day")
print(f"Fixed-point break-even: {history[-1]:.4f} transactions per day")
print("Bisection iterations:", solution.iterations)
print("Fixed-point iterations:", len(history) - 1)
print(f"Profit at the root: {profit(solution.root):.2e} KES")
print(f"Profit at 50 transactions: {profit(50):.2f} KES")
print(f"Profit at 120 transactions: {profit(120):.2f} KES")

counts = np.linspace(10, 200, 300)
plt.plot(counts, profit(counts))
plt.axhline(0, linewidth=0.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Transactions per day")
plt.ylabel("Daily profit (KES)")
plt.title("M-Pesa agent break-even point")
plt.grid(True)
plt.show()