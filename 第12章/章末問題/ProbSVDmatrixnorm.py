import numpy as np
import numpy.linalg as LA

def MatNorm(A):
    U, S, VT = LA.svd(A, full_matrices = False)
    return S[0]

A = np.array([[1, 3], [-2, 0], [2, -12]])

print(MatNorm(A))