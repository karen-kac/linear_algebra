import numpy as np
import numpy.linalg as LA

A = np.array([[1, -1, 1], [2, 3, -3], [-1, 4, 1]]) 
b = np.array([4, -2, 5]).reshape((3,1))

r = LA.matrix_rank(A) 
print('rank(A) =', r)
try:
    InvA = LA.inv(A)
    x = InvA @ b
    print(x)
except Exception as message:
    print(message)