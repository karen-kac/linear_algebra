import numpy as np
import numpy.linalg as LA
import sys

def GramSchmidt(A):
    A = np.array(A, dtype = np.float64)
    m = A.shape[0] # number of row
    n = A.shape[1] # number of column(vectors)
    # A = (a0, a1, ..., an)
    if m < n:
        print('The given ndarray cannot be a basis.')
        sys.exit()   

    a = A[:,[0]] # the first column vector a1(a0)
    basis = a/LA.norm(a) # b1(b0)

    # Gram-Schmidt orthogonalization
    for j in range(1, n):  
        a = A[:,[j]]
        for i in range(j):
            a -= np.dot(A[:,j], basis[:,i])*basis[:,[i]]

        b_i = a / LA.norm(a)
        basis = np.append(basis, b_i, axis = 1)

    return basis

A = np.array([[1, 0, 1, 0], [0, -1, 1, 1], [-1, 0, 1, -1], [0, 1, 0, 1]])
G = GramSchmidt(A)
print(G)

# the case using LA.qr
Q, R = LA.qr(A) 
print('Q=', Q)
print('R=', R)
print('QR=', Q @ R)