import numpy as np
import numpy.linalg as LA

A = np.array([[1, 2, 2], [-3, -1, 1], [2, -3, 3]])
b = np.array([1, -1, 8])
#A = np.array([[1, 2, -3], [3, 4, -5], [-1, 3, 1]])
#b = np.array([-7, -11, -10])

r = LA.matrix_rank(A)
print('rank(A) =', r)
try:
    x = LA.solve(A, b)
    print(x)
except Exception as message:
    print(message)