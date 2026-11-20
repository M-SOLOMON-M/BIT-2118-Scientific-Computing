import numpy as np
from scipy.optimize import minimize

# M-Pesa agent: how to split working capital between e-float and cash
# to maximise daily commission. (all figures assumed; amounts in KES thousands)
#
# e = e-float (serves deposits), c = cash (serves withdrawals)
# Deposits:    commission 0.8% per KES, e-float turns over 2 times a day -> 16 per thousand per day
# Withdrawals: commission 1.2% per KES, cash turns over 1.5 times a day  -> 18 per thousand per day
# Daily deposit demand is limited to 250 (so e <= 125), withdrawal demand to 180 (so c <= 120)
# At least 40 must be kept as cash for walk-in withdrawals.
capital = 200.0

def negative_profit(z):
    e, c = z
    return -(16*e + 18*c)           # minimise the negative to maximise profit

def capital_constraint(z):
    e, c = z
    return capital - e - c          # must be >= 0

constraints = {"type": "ineq", "fun": capital_constraint}
bounds = [(0, 125), (40, 120)]

solution = minimize(
    negative_profit,
    x0=[50, 50],
    method="SLSQP",
    bounds=bounds,
    constraints=constraints
)

e, c = solution.x
print("Optimization success:", solution.success)
print(f"E-float: KES {e * 1000:,.0f}")
print(f"Cash:    KES {c * 1000:,.0f}")
print(f"Capital used: KES {(e + c) * 1000:,.0f} of {capital * 1000:,.0f}")
print(f"Maximum daily commission: KES {-solution.fun:,.2f}")

# Check against a simple brute-force search in steps of KES 5,000
best = None
for e_try in np.arange(0, 125.1, 5):
    for c_try in np.arange(40, 120.1, 5):
        if e_try + c_try <= capital:
            profit = 16*e_try + 18*c_try
            if best is None or profit > best[0]:
                best = (profit, e_try * 1000, c_try * 1000)
print("Brute-force best (profit, e-float, cash):", best)