def print_matrix(matrix):
    for row in matrix:
        print(row)

def identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]

def row_operation_matrix(size, i, j, factor):
    mat = identity_matrix(size)
    mat[j][i] = factor
    return mat

def multiply_matrices(mat1, mat2):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]

def lu_decomposition(matrix):
    n = len(matrix)
    L = identity_matrix(n)
    U = [row[:] for row in matrix]

    for i in range(n):
        for j in range(i + 1, n):
            if U[i][i] == 0:
                raise ValueError("LU decomposition is not possible (zero pivot)")

            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]

    return L, U

def elementary_row_operations(matrix):
    n = len(matrix)
    elementary_matrices = []

    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][i] == 0:
                raise ValueError("Elementary row operations are not possible (zero pivot)")

            factor = matrix[j][i] / matrix[i][i]
            operation_matrix = row_operation_matrix(n, i, j, -factor)
            elementary_matrices.append(operation_matrix)
            matrix = multiply_matrices(operation_matrix, matrix)

    return elementary_matrices

# Example Usage:
A = [
    [2, -1, 1],
    [-3, 3, 0],
    [-2, 1, 2]
]

print("Original Matrix A:")
print_matrix(A)

elementary_matrices = elementary_row_operations(A)

print("\nElementary Matrices:")
for matrix in elementary_matrices:
    print_matrix(matrix)

L, U = lu_decomposition(A)

print("\nLower Triangular Matrix L:")
print_matrix(L)

print("\nUpper Triangular Matrix U:")
print_matrix(U)

# Verify A = LU
A_calculated = multiply_matrices(L, U)

print("\nVerification A = LU:")
print_matrix(A_calculated)
