import numpy as np
import timeit

# M-Pesa: one million simulated Send Money amounts in KES
rng = np.random.default_rng(42)
amounts_kes = rng.uniform(50, 5000, 1_000_000)

fee_rate = 0.01            # assumed flat 1% transaction charge
kes_per_usd = 129.0        # assumed exchange rate
mean_amount = amounts_kes.mean()

def loop_version():
    deviations = []
    for amount in amounts_kes:
        fee = amount * fee_rate
        total_usd = (amount + fee) / kes_per_usd
        deviations.append((amount - mean_amount) ** 2)
    return deviations

def vectorized_version():
    fee = amounts_kes * fee_rate
    total_usd = (amounts_kes + fee) / kes_per_usd
    return total_usd, (amounts_kes - mean_amount) ** 2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

total_usd, sq_dev = vectorized_version()

print("First five amounts (KES):", np.round(amounts_kes[:5], 2))
print("First five totals incl. fee (USD):", np.round(total_usd[:5], 2))
print(f"Total fees collected: KES {(amounts_kes * fee_rate).sum():,.2f}")
print(f"Variance of amounts: {sq_dev.mean():,.2f}")
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time/vector_time:.1f}x")