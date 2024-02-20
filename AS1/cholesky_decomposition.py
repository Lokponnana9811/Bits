def cholesky_decomposition(A):
    n = len(A)
    L = []
    for i in range(n):
        L.append([0.0] * n)


    for i in range(n):
        for j in range(i + 1):
            sum_val = 0.0
            for k in range(j):
                sum_val += L[i][k] * L[j][k]
            
            if i == j:
                L[i][j] = (A[i][i] - sum_val) ** 0.5
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - sum_val))

    return L

# Example usage:
A = [
    [4, 12, -16],
    [12, 37, -43],
    [-16, -43, 98]
]

L = cholesky_decomposition(A)

# Display the result
print("Original matrix A:")
for row in A:
    print(row)

print("\nCholesky decomposition L:")
for row in L:
    print(row)
