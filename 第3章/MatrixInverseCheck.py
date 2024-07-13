import numpy as np
import numpy.linalg as LA

A = np.array([[1, 1, 0], [-2, 0, 1], [-1, 2, 2]])
#A = np.array([[1, 1, 0], [-2, 0, 1], [0, 0, 0]]) # singular
#A = np.array([[1, 2, 1], [2, -1, 3], [3, 1, 4]]) # singular

r = LA.matrix_rank(A) 
print('rank(A) =', r)
try:
    InvA = LA.inv(A)
    print(InvA, A @ InvA, sep='\n')
except Exception as message:
    print(message)