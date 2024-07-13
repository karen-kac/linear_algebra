import numpy as np
import numpy.linalg as LA

A = np.array([[1, 9, 2], [-1, 3, 1], [3, 8, -2]])
B = np.transpose(A)

print(LA.det(A))
print(LA.det(B))