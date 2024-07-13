import numpy as np
import numpy.linalg as LA

def element(A, i, j):
    try:
        tmpA = np.delete(A, i, axis = 0) # delete i-th row    
        CFMatij = np.delete(tmpA, j, axis = 1) # delete j-th column
        Minorij = (-1)**(i+j)*LA.det(CFMatij) 
    except Exception as message:
        print(message)
        exit(0)
    return np.round(Minorij, decimals = 2)

def CofMat(A):
    n = np.shape(A)[0] # This is the number of rows of A.
                       # The number of columns is not checked.
    CM = np.zeros([n, n])  
    for i in range(n):
        for j in range(n):
            CM[i][j] = element(A, i, j)
    return CM.T # transpose of CM

A = np.array([[8, 3, 1], [2, -1, 3], [3, 1, 4]])

print(A)
print(CofMat(A))
print(np.round(LA.det(A), decimals = 2))