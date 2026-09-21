import numpy as np

# Create 1D array
arr = np.arange(1, 13)  # 12 elements
print("Original 1D array:", arr)
print("Shape:", arr.shape)

# Convert into 2D using reshape()
arr_2d_a = arr.reshape(3, 4)   # 3 rows, 4 columns
print("\nReshaped to (3, 4):\n", arr_2d_a)

arr_2d_b = arr.reshape(4, 3)   # 4 rows, 3 columns
print("\nReshaped to (4, 3):\n", arr_2d_b)

arr_2d_c = arr.reshape(2, 6)   # 2 rows, 6 columns
print("\nReshaped to (2, 6):\n", arr_2d_c)

# Using -1 to let NumPy auto-calculate a dimension
arr_2d_d = arr.reshape(3, -1)
print("\nReshaped to (3, -1):\n", arr_2d_d)

# Constraint demonstration: total elements must match
try:
    invalid = arr.reshape(5, 3)   # 12 elements can't fill 15 slots
except ValueError as e:
    print("\nError when reshaping to (5, 3):", e)
