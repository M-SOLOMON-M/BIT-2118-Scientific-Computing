import numpy as np

# Land survey: a rectangular plot in a GIS/CAD tool, corners in metres [x, y]
plot = np.array([
    [0.0,  0.0],
    [40.0, 0.0],
    [40.0, 25.0],
    [0.0,  25.0]
])

angle = np.deg2rad(30)     # rotate plot to match road alignment
scale_factor = 1.2         # enlarge layout by 20%
shift_x, shift_y = 100.0, 50.0   # move plot to its position on the site map

rotation = np.array([
    [np.cos(angle), -np.sin(angle), 0],
    [np.sin(angle),  np.cos(angle), 0],
    [0, 0, 1]
])
scaling = np.array([
    [scale_factor, 0, 0],
    [0, scale_factor, 0],
    [0, 0, 1]
])
translation = np.array([
    [1, 0, shift_x],
    [0, 1, shift_y],
    [0, 0, 1]
])

# Combined 3x3 homogeneous transformation (scale first, then rotate, then translate)
T = translation @ rotation @ scaling

# Add a column of ones so translation can be done by matrix multiplication
homogeneous = np.hstack([plot, np.ones((len(plot), 1))])
new_plot = (homogeneous @ T.T)[:, :2]

# Area: width x height before, determinant of the 2x2 linear part for the scaling
original_area = 40.0 * 25.0
area_factor = np.linalg.det(T[:2, :2])
new_area = original_area * area_factor

# Inverse transformation should bring the corners back
restored = (np.hstack([new_plot, np.ones((4, 1))]) @ np.linalg.inv(T).T)[:, :2]

print("Original corners:\n", plot)
print("Transformation matrix:\n", np.round(T, 4))
print("Transformed corners:\n", np.round(new_plot, 3))
print("Area scale factor (determinant):", round(area_factor, 4))
print(f"Original area: {original_area:.1f} m^2, new area: {new_area:.1f} m^2")
print("Inverse restores original:", np.allclose(restored, plot))