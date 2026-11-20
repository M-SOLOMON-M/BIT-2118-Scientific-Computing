import numpy as np
from scipy.interpolate import interp1d, CubicSpline, PchipInterpolator
import matplotlib.pyplot as plt

# M-Pesa agent: cumulative number of transactions recorded every 2 hours
# (assumed data). Estimate the count at times between the recordings.
hours = np.array([6, 8, 10, 12, 14, 16, 18, 20], dtype=float)
cumulative = np.array([0, 6, 28, 58, 98, 134, 170, 200], dtype=float)

linear = interp1d(hours, cumulative, kind="linear")
cubic = CubicSpline(hours, cumulative)
pchip = PchipInterpolator(hours, cumulative)   # shape-preserving (never decreases)

fine = np.linspace(6, 20, 281)
target = 13.0   # 13:00, midway between two recordings

print(f"Estimated transactions by 13:00 (linear): {float(linear(target)):.2f}")
print(f"Estimated transactions by 13:00 (cubic spline): {float(cubic(target)):.2f}")
print(f"Estimated transactions by 13:00 (PCHIP): {float(pchip(target)):.2f}")
print(f"Estimated transactions by 07:00 (cubic spline): {float(cubic(7.0)):.2f}")
print(f"Estimated transactions by 07:00 (PCHIP): {float(pchip(7.0)):.2f}")
print("Cubic spline never decreases:", bool(np.all(np.diff(cubic(fine)) >= 0)))
print("PCHIP never decreases:", bool(np.all(np.diff(pchip(fine)) >= 0)))
print(f"Lowest cubic spline value: {cubic(fine).min():.2f}")
print(f"Transactions between 13:00 and 14:00 (PCHIP): {float(pchip(14.0) - pchip(13.0)):.2f}")

plt.scatter(hours, cumulative, label="Recorded counts", zorder=3)
plt.plot(fine, linear(fine), label="Linear")
plt.plot(fine, cubic(fine), label="Cubic spline")
plt.plot(fine, pchip(fine), label="PCHIP", linestyle="--")
plt.xlabel("Hour of day")
plt.ylabel("Cumulative transactions")
plt.title("M-Pesa agent: estimating cumulative transactions")
plt.legend()
plt.grid(True)
plt.show()