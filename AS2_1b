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

# Example usage:
# Assuming A1 is already defined
lambda_1, eigenvector_1 = power_method(A1)

# Normalize eigenvector
eigenvector_hat_1 = eigenvector_1 / np.linalg.norm(eigenvector_1)

print("\nEstimated largest eigenvalue (λ1):", lambda_1)
print("Corresponding eigenvector (x1):", eigenvector_1)
print("Normalized eigenvector (x_hat1):", eigenvector_hat_1)
