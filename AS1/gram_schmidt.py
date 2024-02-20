def dot_product(v1, v2):
    result = 0
    for x, y in zip(v1, v2):
        result += x * y
    return result


def scalar_multiply(scalar, vector):
    result = []
    for x in vector:
        result.append(scalar * x)
    return result

def vector_subtract(v1, v2):
    result = []
    for x, y in zip(v1, v2):
        result.append(x - y)
    return result

def vector_normalize(v):
    magnitude = 0
    for x in v:
        magnitude += x**2
    magnitude = magnitude**0.5
    result = []
    for x in v:
        result.append(x / magnitude)
    return result

def gram_schmidt(A):
    m, n = len(A), len(A[0])
    Q = [[0.0] * n for _ in range(m)]
    R = [[0.0] * n for _ in range(n)]

    for j in range(n):
        v = A[j]
        for i in range(j):
            R[i][j] = dot_product(Q[i], A[j])
            v = vector_subtract(v, scalar_multiply(R[i][j], Q[i]))

        R[j][j] = dot_product(v, v)**0.5
        Q[j] = vector_normalize(v)

    return Q, R
 
# Example usage:
m = 4
n = 3
A = [
    [1, 0, 0, 2],
    [0, 2, 0, -1],
    [0, -1, 1, 0],
    [1, -2, 0, 1]
]

Q, R = gram_schmidt(A)

# Display the result
print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix Q (orthogonal):")
for row in Q:
    print(row)

print("\nMatrix R (upper triangular):")
for row in R:
    print(row)

# Verify the decomposition
print("\nIs Q * R close to A?")
A_reconstructed = [[sum(Q[i][k] * R[k][j] for k in range(n)) for j in range(n)] for i in range(m)]
print(all(all(abs(A[i][j] - A_reconstructed[i][j]) < 1e-10 for j in range(n)) for i in range(m)))
