import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix multiplication (dot product)
matmul_result = np.dot(A, B)     # or A @ B
print("\nMatrix Multiplication (A x B):\n", matmul_result)

# Transpose
A_transpose = A.T
print("\nTranspose of A:\n", A_transpose)
