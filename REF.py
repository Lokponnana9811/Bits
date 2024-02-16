def print_matrix(matrix):
    for row in matrix:
        print(row)

def perform_ref(matrix):
    m = len(matrix)
    n = len(matrix[0])

    pivot_row = 0
    for col in range(n):
        # Find the first non-zero entry in the current column
        pivot_found = False
        for row in range(pivot_row, m):
            if matrix[row][col] != 0:
                pivot_found = True
                break

        # If a non-zero entry is found, perform row operations to make the pivot 1 and clear below
        if pivot_found:
            # Swap rows to bring the pivot to the top
            matrix[pivot_row], matrix[row] = matrix[row], matrix[pivot_row]

            # Make the pivot 1
            pivot_value = matrix[pivot_row][col]
            for i in range(col, n):
                matrix[pivot_row][i] /= pivot_value

            # Eliminate below the pivot
            for i in range(pivot_row + 1, m):
                factor = matrix[i][col]
                for j in range(col, n):
                    matrix[i][j] -= factor * matrix[pivot_row][j]

            # Move to the next pivot row
            pivot_row += 1

    return matrix    

def construct_augmented_matrix(A, B):
    return [a + [b] for a, b in zip(A, B)]

# Example usage
A = [[1, -2, 2, 4, 0, 1, 2],
     [0, 0, 0, 1, -2, -4, 0],
     [0, 1, 4, 0, -2, 4, 0],
     [0, -1, -3, 2, 4, 0, -4],
     [-2, 4,  0, 0, 0, 1, -3],
     ]

B = [1, 2, -3, 3, 2]

augmented_matrix = construct_augmented_matrix(A, B)
ref_matrix = perform_ref(augmented_matrix)

print("Original Augmented Matrix:")
print_matrix(augmented_matrix)

print("\nMatrix in Row Echelon Form:")
print_matrix(ref_matrix)