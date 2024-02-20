def print_matrix(matrix):
    for row in matrix:
        print(row)

def gaussian_elimination(A, B):
    # Combine matrix A and vector B to form augmented matrix AB
    AB = [a + [b] for a, b in zip(A, B)]

    # Get the number of rows and columns
    m = len(AB)
    n = len(AB[0])

    # Perform Gaussian elimination
    for i in range(m):
        # Make the diagonal element in the current row equal to 1
        pivot = AB[i][i]
        if pivot == 0:
            # If the diagonal element is 0, find a non-zero row to swap with
            for j in range(i + 1, m):
                if AB[j][i] != 0:
                    AB[i], AB[j] = AB[j], AB[i]
                    break
            pivot = AB[i][i]
        
        # Divide the current row by the pivot to make the diagonal element 1
        AB[i] = [x / pivot for x in AB[i]]

        # Make the elements above and below the pivot in the current column equal to 0
        for j in range(m):
            if j != i:
                factor = AB[j][i]
                AB[j] = [a - factor * b for a, b in zip(AB[j], AB[i])] 

    print("Row Echelon Form:")
    print_matrix(AB)

# Example usage

A = [[1, -2, 2, 4, 0, 1, 2],
     [0, 0, 0, 1, -2, -4, 0],
     [0, 1, 4, 0, -2, 4, 0],
     [0, -1, -3, 2, 4, 0, -4],
     [-2, 4,  0, 0, 0, 1, -3],
     ]

B = [1, 2, -3, 3, 2]

gaussian_elimination(A, B)