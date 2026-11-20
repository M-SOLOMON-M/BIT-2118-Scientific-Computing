import numpy as np
import matplotlib.pyplot as plt

# M-Pesa agent: cumulative transactions recorded every hour (06:00 to 20:00).
# The derivative of the cumulative count is the transaction RATE (per hour).
# For testing accuracy, the counts come from a known logistic model
# C(t) = L / (1 + exp(-k (t - t0))), so the exact rate is known too. (assumed model)
L, k, t0 = 2000.0, 0.6, 13.0

def C(t):
    return L / (1 + np.exp(-k * (t - t0)))

def exact_rate(t):
    c = C(t)
    return k * c * (1 - c / L)

hours = np.arange(6, 21, dtype=float)
cumulative = np.round(C(hours))          # whole transactions, as an agent would record
# cumulative[7] += 30                    # (parameter change: uncomment a recording error)

rate = np.zeros_like(cumulative)
rate[0] = (cumulative[1] - cumulative[0]) / (hours[1] - hours[0])            # forward
for i in range(1, len(hours) - 1):                                           # central
    rate[i] = (cumulative[i + 1] - cumulative[i - 1]) / (hours[i + 1] - hours[i - 1])
rate[-1] = (cumulative[-1] - cumulative[-2]) / (hours[-1] - hours[-2])       # backward

peak = np.argmax(rate)
print("Hour  Cumulative  Estimated rate  Exact rate")
for i in (0, 4, 6, 7, 8, 10, 14):
    print(f"{hours[i]:>4.0f}  {cumulative[i]:>10.0f}  {rate[i]:>14.1f}  {exact_rate(hours[i]):>10.1f}")
print(f"Peak estimated rate: {rate[peak]:.1f} transactions/hour at {hours[peak]:.0f}:00")
print("np.gradient agrees:", np.allclose(rate, np.gradient(cumulative, hours)))

# Effect of step size h at t = 10:00 (exact rate known)
print("\nStep-size study at 10:00")
true = exact_rate(10.0)
for h in (2.0, 1.0, 0.5, 0.25):
    fwd = (C(10.0 + h) - C(10.0)) / h
    cen = (C(10.0 + h) - C(10.0 - h)) / (2 * h)
    print(f"h={h:<5} forward error={abs(fwd - true):.4f}  central error={abs(cen - true):.4f}")

plt.plot(hours, rate, marker="o", label="Estimated rate (differences)")
t_fine = np.linspace(6, 20, 200)
plt.plot(t_fine, exact_rate(t_fine), linestyle="--", label="Exact rate")
plt.xlabel("Hour of day")
plt.ylabel("Transactions per hour")
plt.title("M-Pesa agent: transaction rate from cumulative counts")
plt.legend()
plt.grid(True)
plt.show()