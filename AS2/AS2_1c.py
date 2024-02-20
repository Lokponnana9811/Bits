import numpy as np

def power_method(A, max_iterations=1000):
    n = A.shape[0]
    
    # Initialize a random vector
    x = np.random.rand(n)
    x /= np.linalg.norm(x)  # Normalize the vector
    
    lambda_prev = 0
    
    # Print initial iterate
    print("Iterate 0: Eigenvalue estimate =", lambda_prev)
    
    # Iterate
    for i in range(1, max_iterations + 1):
        x_new = np.dot(A, x)
        lambda_ = np.dot(x_new, x)
        x_new /= np.linalg.norm(x_new)  # Normalize the vector
        
        # Print intermediate iterates
        if i <= 10:
            print(f"Iterate {i}: Eigenvalue estimate =", lambda_)
        
        lambda_prev = lambda_
        x = x_new
    
    return lambda_, x

# Construct matrix A2
A2 = A1 - np.outer(eigenvector_hat_1, eigenvector_hat_1) @ A1

# Use Power method to find eigenvalue and eigenvector of A2
lambda_2, eigenvector_2 = power_method(A2)

# Normalize eigenvector
eigenvector_hat_2 = eigenvector_2 / np.linalg.norm(eigenvector_2)

print("\nEstimated largest eigenvalue (λ2):", lambda_2)
print("Corresponding eigenvector (x2):", eigenvector_2)
print("Normalized eigenvector (x_hat2):", eigenvector_hat_2)
