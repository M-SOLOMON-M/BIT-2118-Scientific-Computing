import numpy as np
import matplotlib.pyplot as plt

# Steady-state temperature of a square metal heat-sink plate.
# The plate is divided into an n x n grid of interior points.
# Left edge touches a hot component (CPU_TEMP); the other three edges are at air temperature.
n = 8
CPU_TEMP = 80.0     # C, left edge
AIR_TEMP = 25.0     # C, top, bottom and right edges

N = n * n
A = np.zeros((N, N))
b = np.zeros(N)

# Each interior point: 4*T - (four neighbours) = 0, boundary values move to b
for i in range(n):
    for j in range(n):
        k = i * n + j
        A[k, k] = 4.0
        if i > 0:     A[k, k - n] = -1.0
        else:         b[k] += AIR_TEMP      # top edge
        if i < n - 1: A[k, k + n] = -1.0
        else:         b[k] += AIR_TEMP      # bottom edge
        if j > 0:     A[k, k - 1] = -1.0
        else:         b[k] += CPU_TEMP      # left edge (hot)
        if j < n - 1: A[k, k + 1] = -1.0
        else:         b[k] += AIR_TEMP      # right edge

def jacobi(A, b, tol=1e-8, max_iter=2000):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=2000):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
x_exact = np.linalg.solve(A, b)

print("Number of equations:", N, "| non-zero entries:", np.count_nonzero(A),
      f"({np.count_nonzero(A) / N**2:.1%} of the matrix)")
print("Jacobi iterations:", len(err_j))
print("Gauss-Seidel iterations:", len(err_gs))
print("Max difference Jacobi vs direct:", np.max(np.abs(x_j - x_exact)))
print("Max difference Gauss-Seidel vs direct:", np.max(np.abs(x_gs - x_exact)))
T = x_gs.reshape(n, n)
print(f"Hottest interior point: {T.max():.2f} C, coolest: {T.min():.2f} C")
print(f"Temperature next to hot edge (middle row): {T[n // 2, 0]:.2f} C")
print(f"Temperature next to far edge (middle row): {T[n // 2, -1]:.2f} C")

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].semilogy(err_j, label="Jacobi")
ax[0].semilogy(err_gs, label="Gauss-Seidel")
ax[0].set_xlabel("Iteration")
ax[0].set_ylabel("Maximum change")
ax[0].set_title("Convergence")
ax[0].legend()
ax[0].grid(True)
im = ax[1].imshow(T, cmap="hot")
ax[1].set_title("Plate temperature (C), hot edge on the left")
fig.colorbar(im, ax=ax[1])
plt.tight_layout()
plt.show()
