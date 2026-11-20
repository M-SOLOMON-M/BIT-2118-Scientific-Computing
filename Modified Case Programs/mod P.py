import numpy as np
import matplotlib.pyplot as plt

# Mobile-money adoption in a country (assumed values, not real data).
# N = number of active users in millions. Growth slows as the market saturates:
# dN/dt = r * N * (1 - N/K)   (logistic growth)
K = 40.0          # market capacity (million users)
r = 0.35          # growth rate per year
N0 = 2.0          # users at year 0 (millions)
end_time = 20.0   # years

def growth_rate(N):
    return r * N * (1 - N / K)

def euler(h):
    t = np.arange(0, end_time + h, h)
    N = np.zeros_like(t)
    N[0] = N0
    for i in range(len(t) - 1):
        N[i + 1] = N[i] + h * growth_rate(N[i])
    return t, N

def exact(t):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

h = 1.0
t, N = euler(h)
true = exact(t)

print(f"Step size h = {h} year")
for year in (5, 10, 15, 20):
    i = int(year / h)
    print(f"Year {year:>2}: Euler = {N[i]:6.2f} M, exact = {true[i]:6.2f} M, error = {abs(N[i] - true[i]):.3f} M")
print(f"Year when Euler first passes 20 million users: {t[np.argmax(N >= 20)]:.0f}")

print("\nEffect of step size on the error at year 10")
for step in (4.0, 2.0, 1.0, 0.5, 0.1):
    ts, Ns = euler(step)
    i = int(round(10 / step))
    print(f"h = {step:<4} Euler = {Ns[i]:6.2f} M, error = {abs(Ns[i] - exact(ts[i])):.3f} M")

plt.plot(t, N, marker="o", label="Euler (h = 1 year)")
t_fine = np.linspace(0, end_time, 300)
plt.plot(t_fine, exact(t_fine), label="Exact logistic solution")
plt.axhline(K, linestyle=":", label="Market capacity")
plt.xlabel("Year")
plt.ylabel("Active users (millions)")
plt.title("Mobile-money adoption: Euler vs exact")
plt.legend()
plt.grid(True)
plt.show()