import numpy as np

# M-Pesa agent, end-of-day totals. Unknowns:
# d = number of deposits, w = number of withdrawals, a = number of airtime sales
#
# Equation 1: total number of transactions        d + w + a = 120
# Equation 2: total commission (KES)              25d + 40w + 5a = 3000
# Equation 3: total value handled (KES)           1500d + 2000w + 100a = 158000
#
# (commission per transaction and average amounts are assumed values)

A = np.array([
    [1.0,    1.0,    1.0],
    [25.0,   40.0,   5.0],
    [1500.0, 2000.0, 100.0]
])
b = np.array([120.0, 3000.0, 158000.0])

solution = np.linalg.solve(A, b)
residual = b - A @ solution

print(f"Deposits: {solution[0]:.0f}")
print(f"Withdrawals: {solution[1]:.0f}")
print(f"Airtime sales: {solution[2]:.0f}")
print("Verification A @ solution:", A @ solution)
print("Residual:", residual)
print("Residual norm:", np.linalg.norm(residual))
print("Determinant of A:", round(np.linalg.det(A), 2))