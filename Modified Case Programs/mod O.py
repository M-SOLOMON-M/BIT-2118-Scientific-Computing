import numpy as np
from scipy.integrate import simpson, quad
import matplotlib.pyplot as plt

# Cell-tower data traffic: throughput in Mbps over 12 hours (06:00 to 18:00).
# Total data transferred = integral of throughput over time.
# Assumed smooth model with an afternoon peak at hour 8 (14:00):
def throughput(t):
    return 20 + 60 * np.exp(-((t - 8) / 2.5) ** 2)       # Mbps

MBPS_HOUR_TO_GB = 3600 / 8 / 1000       # 1 Mbps for 1 hour = 0.45 GB

def estimate(step):
    t = np.arange(0, 12 + step, step)
    y = throughput(t)
    trap = np.trapezoid(y, t) if hasattr(np, "trapezoid") else np.trapz(y, t)
    simp = simpson(y, x=t)
    return t, y, trap, simp

# "Exact" value from adaptive quadrature on the model
exact, _ = quad(throughput, 0, 12)

for step in (2.0, 1.0):
    t, y, trap, simp = estimate(step)
    print(f"Readings every {step:.0f} h ({len(t)} points)")
    print(f"  Trapezoidal: {trap * MBPS_HOUR_TO_GB:.3f} GB  (error {abs(trap - exact) * MBPS_HOUR_TO_GB:.4f} GB)")
    print(f"  Simpson:     {simp * MBPS_HOUR_TO_GB:.3f} GB  (error {abs(simp - exact) * MBPS_HOUR_TO_GB:.4f} GB)")
print(f"Adaptive quadrature (quad): {exact * MBPS_HOUR_TO_GB:.3f} GB")

t2, y2, _, _ = estimate(2.0)
t_fine = np.linspace(0, 12, 300)
plt.plot(t_fine, throughput(t_fine), label="Throughput model")
plt.fill_between(t2, y2, alpha=0.2, step=None, label="Trapezoids (2 h readings)")
plt.scatter(t2, y2, label="Readings every 2 h")
plt.xlabel("Hours since 06:00")
plt.ylabel("Throughput (Mbps)")
plt.title("Cell-tower traffic: area under the curve = data transferred")
plt.legend()
plt.grid(True)
plt.show()