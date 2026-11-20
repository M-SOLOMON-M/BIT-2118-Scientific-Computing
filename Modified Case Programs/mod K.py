import numpy as np
from scipy.optimize import root

# Locating a phone from the distances to two cell towers (coordinates in km).
# Tower 1 at (0, 0): phone is 5 km away
# Tower 2 at (6, 2): phone is 4 km away   (assumed positions and distances)
T1, R1 = np.array([0.0, 0.0]), 5.0
T2, R2 = np.array([6.0, 2.0]), 4.0

def equations(z):
    x, y = z
    return [
        (x - T1[0])**2 + (y - T1[1])**2 - R1**2,
        (x - T2[0])**2 + (y - T2[1])**2 - R2**2
    ]

# Two circles meet in up to two points, so try more than one starting guess
for guess in ([3.0, 4.0], [5.0, -2.0]):
    solution = root(equations, guess)
    x, y = solution.x
    print("Initial guess:", guess)
    print(f"Possible phone position: ({x:.4f}, {y:.4f}) km")
    print("Residuals:", equations(solution.x))
    print("Converged:", solution.success)
    print(f"Distance to tower 1: {np.hypot(x - T1[0], y - T1[1]):.4f} km, "
          f"to tower 2: {np.hypot(x - T2[0], y - T2[1]):.4f} km")
    print()

# Polynomial check: subtracting the two circle equations gives a line,
# substituting it into circle 1 gives 160x^2 - 1176x + 2001 = 0
x_roots = np.roots([160.0, -1176.0, 2001.0])
print("Polynomial roots for x:", np.round(x_roots, 4))
print("Matching y values:", np.round((49 - 12 * x_roots) / 4, 4))