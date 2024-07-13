import numpy as np
import numpy.linalg as LA

A = np.array([[2, 5, 3], [-1, 7, 9]])
B = np.array([[-1, 3], [2, 9], [5, -3]])

C = A @ B
print(C)
print(LA.det(C))

D = B @ A
print(D)
print(LA.det(D))