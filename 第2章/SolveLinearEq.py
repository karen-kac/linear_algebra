import numpy as np
import numpy.linalg as LA

A = np.array([[1, 3, 5], [-2, 5, 1], [3, 2, 4]])
b = np.array([14, -6, 16])
#A = np.array([[1, 3, 2, -1], [2, -1, -5, 2], [3, 2, -3, 1], [1, -4, -7, 3]])
#b = np.array([5, -2, 3, 7])

r = LA.matrix_rank(A)
print('rank(A) =', r)
try:
    x = LA.solve(A, b)
    print(x)
except Exception as message:
    print(message)