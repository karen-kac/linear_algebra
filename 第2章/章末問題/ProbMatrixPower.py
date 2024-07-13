import numpy as np

def MatrixPower(A, k):
    bit = format(k,"b") 
    M = np.eye(len(A))
    for i in range(len(bit)):
        M = M @ M 
        if bit[i] == "1":
            M = A @ M 
    return M

# example
A = np.array([[1, 2, 3], [1, -2, 1], [-3, 5, 2]])

print(MatrixPower(A, 5))