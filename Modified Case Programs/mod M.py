import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# M-Pesa agent network growth: average daily transactions per agent, months 1 to 12
# (assumed data). Growth slows as the market saturates, so a logistic curve is tried.
months = np.arange(1, 13, dtype=float)
daily_tx = np.array([60, 105, 170, 260, 380, 500, 620, 740, 820, 880, 915, 945], dtype=float)

# Logistic model: L / (1 + exp(-k (t - t0)))
def logistic(t, L, k, t0):
    return L / (1 + np.exp(-k * (t - t0)))

# Quadratic model for comparison
def quadratic(t, a, b, c):
    return a*t**2 + b*t + c

p_log, _ = curve_fit(logistic, months, daily_tx, p0=[1000, 0.5, 6])
p_quad, _ = curve_fit(quadratic, months, daily_tx)

rmse_log = np.sqrt(np.mean((daily_tx - logistic(months, *p_log))**2))
rmse_quad = np.sqrt(np.mean((daily_tx - quadratic(months, *p_quad))**2))

L, k, t0 = p_log
print(f"Logistic fit: L = {L:.1f}, k = {k:.3f}, t0 = {t0:.2f}")
print(f"Quadratic fit: y = {p_quad[0]:.3f}t^2 + {p_quad[1]:.3f}t + {p_quad[2]:.2f}")
print(f"RMSE logistic: {rmse_log:.2f} | RMSE quadratic: {rmse_quad:.2f}")
print(f"Forecast for month 15 (logistic): {logistic(15, *p_log):.1f}")
print(f"Forecast for month 15 (quadratic): {quadratic(15, *p_quad):.1f}")

t_plot = np.linspace(1, 15, 300)
plt.scatter(months, daily_tx, label="Observed")
plt.plot(t_plot, logistic(t_plot, *p_log), label="Logistic fit")
plt.plot(t_plot, quadratic(t_plot, *p_quad), label="Quadratic fit", linestyle="--")
plt.xlabel("Month")
plt.ylabel("Average daily transactions per agent")
plt.title("M-Pesa agent growth: logistic vs quadratic")
plt.legend()
plt.grid(True)
plt.show()