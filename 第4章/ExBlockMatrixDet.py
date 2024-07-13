import numpy as np
import numpy.linalg as LA

A = np.random.uniform(low = -10, high = 10, size = (2, 2))
B = np.random.uniform(low = -10, high = 10, size = (2, 2))
C = np.random.uniform(low = -10, high = 10, size = (2, 2))
O = np.zeros((2,2))

M = np.block([[A, C], [O, B]])

print(M, LA.det(M), LA.det(A)*LA.det(B), sep='\n')