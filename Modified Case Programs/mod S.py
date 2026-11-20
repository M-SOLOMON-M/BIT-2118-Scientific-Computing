import numpy as np
import matplotlib.pyplot as plt

# M-Pesa agent: probability of running out of cash on a day.
# Daily withdrawals: the NUMBER of customers is random (Poisson, mean 50) and each
# withdrawal AMOUNT is random (lognormal, mean about KES 2,000). (assumed values)
rng = np.random.default_rng(42)

cash_held = 120_000.0       # KES the agent starts the day with
mean_customers = 50
mu, sigma = 7.3, 0.8        # lognormal parameters of one withdrawal (KES)
days = 100_000              # number of simulated days

customers = rng.poisson(mean_customers, days)
daily_demand = np.array([rng.lognormal(mu, sigma, n).sum() for n in customers])

ran_out = daily_demand > cash_held
p = ran_out.mean()
std_error = np.sqrt(p * (1 - p) / days)

print(f"Average daily withdrawals: KES {daily_demand.mean():,.0f}")
print(f"Estimated probability of running out of cash: {p:.2%}")
print(f"Standard error: {std_error:.3%}  (95% interval {p - 1.96*std_error:.2%} to {p + 1.96*std_error:.2%})")
print(f"Days short of cash: {ran_out.sum()} out of {days}")
print(f"Cash needed to cover 95% of days: KES {np.percentile(daily_demand, 95):,.0f}")
print(f"Cash needed to cover 99% of days: KES {np.percentile(daily_demand, 99):,.0f}")

running = np.cumsum(ran_out) / np.arange(1, days + 1)
idx = np.unique(np.logspace(1, np.log10(days), 200).astype(int)) - 1

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].semilogx(idx + 1, running[idx])
ax[0].set_xlabel("Number of simulated days")
ax[0].set_ylabel("Estimated probability of running out")
ax[0].set_title("Convergence of the estimate")
ax[0].grid(True)
ax[1].hist(daily_demand, bins=60, alpha=0.8)
ax[1].axvline(cash_held, linestyle="--", color="red", label="Cash held")
ax[1].set_xlabel("Daily withdrawals (KES)")
ax[1].set_ylabel("Number of days")
ax[1].set_title("Simulated daily cash demand")
ax[1].legend()
plt.tight_layout()
plt.show()