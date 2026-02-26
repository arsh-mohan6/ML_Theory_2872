import numpy as np

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix row by row:")

matrix = []
for i in range(rows):
    row = list(map(float, input().split()))
    matrix.append(row)

A = np.array(matrix)

# ---- Compute SVD ----
U, S, VT = np.linalg.svd(A)

Sigma = np.zeros((rows, cols))
np.fill_diagonal(Sigma, S)

# ---- Print results ----
print("\nMatrix A =\n", A)
print("\nU =\n", U)
print("\nSigma (matrix form) =\n", Sigma)
print("\nV^T =\n", VT)