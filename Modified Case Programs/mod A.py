import numpy as np

# M-Pesa agent: 24 hourly transaction counts (00:00 to 23:00) on a normal day
transactions = np.array([
    2, 1, 0, 1, 3, 8,
    20, 45, 60, 55, 48, 52,
    70, 65, 50, 46, 58, 80,
    75, 40, 25, 15, 8, 4
])
avg_value_kes = 1850.0      # assumed average value per transaction (KES)
commission_rate = 0.004     # assumed agent commission (0.4% of value)

total_tx = np.sum(transactions)
mean_tx = np.mean(transactions)
peak_hour = np.argmax(transactions)
quiet_hour = np.argmin(transactions)

# Vectorized: value handled and commission for every hour at once
value_per_hour = transactions * avg_value_kes
commission_per_hour = value_per_hour * commission_rate

# Boolean mask: busy hours = above the daily mean
busy_hours = np.where(transactions > mean_tx)[0]

print(f"Total transactions: {total_tx}")
print(f"Mean transactions per hour: {mean_tx:.2f}")
print(f"Peak hour: {peak_hour}:00 with {transactions[peak_hour]} transactions")
print(f"Quietest hour: {quiet_hour}:00 with {transactions[quiet_hour]} transactions")
print(f"Total value handled: KES {value_per_hour.sum():,.2f}")
print(f"Total commission earned: KES {commission_per_hour.sum():,.2f}")
print("Busy hours (above mean):", busy_hours)
