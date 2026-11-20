import numpy as np
from scipy.linalg import lu_factor, lu_solve, lu

# Three-loop resistor network (mesh-current analysis): R @ i = V
# R holds the resistances (ohms) and stays fixed.
# V holds the battery voltage (volts) in each loop and changes between tests.
R = np.array([
    [10.0, -4.0,  0.0],
    [-4.0, 12.0, -5.0],
    [ 0.0, -5.0,  9.0]
])

voltage_tests = [
    np.array([12.0, 6.0, 0.0]),
    np.array([9.0, 6.0, 3.0]),
    np.array([15.0, 0.0, 5.0])
]

# Gaussian elimination with partial pivoting (written out step by step)
def gaussian_solve(A, b):
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    n = len(b)
    for k in range(n - 1):
        p = np.argmax(np.abs(A[k:, k])) + k       # pivot row
        if p != k:
            A[[k, p]] = A[[p, k]]
            b[[k, p]] = b[[p, k]]
        for r in range(k + 1, n):
            factor = A[r, k] / A[k, k]
            A[r, k:] -= factor * A[k, k:]
            b[r] -= factor * b[k]
    x = np.zeros(n)
    for r in range(n - 1, -1, -1):                # back-substitution
        x[r] = (b[r] - A[r, r + 1:] @ x[r + 1:]) / A[r, r]
    return x

# LU factorization done once
lu_piv = lu_factor(R)
P, L, U = lu(R)
print("L =\n", np.round(L, 4))
print("U =\n", np.round(U, 4))
print("Check P @ L @ U equals R:", np.allclose(P @ L @ U, R))
print()

for i, V in enumerate(voltage_tests, start=1):
    currents = lu_solve(lu_piv, V)
    by_hand = gaussian_solve(R, V)
    residual = np.linalg.norm(V - R @ currents)
    print(f"Test {i}: voltages {V}")
    print("  Mesh currents (A):", np.round(currents, 4))
    print("  Same as Gaussian elimination:", np.allclose(currents, by_hand))
    print("  Residual norm:", residual)