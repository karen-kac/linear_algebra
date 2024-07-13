import numpy as np
import numpy.linalg as LA

A = np.array([[3, 1], [1, 3]])
B = np.array([[3, 2], [1, 4]])
C = np.array([[1, -1], [-1, 2]])

print(LA.eig(A), LA.eig(B), LA.eig(C), sep='\n')