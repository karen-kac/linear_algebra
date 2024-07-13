import numpy as np
import numpy.linalg as LA
import sympy

A = np.array([[1, 2, 3, 4], [-2, 3, 1, 0], [3, 4, -1, 2], [0, 2, 5, -1]])
B = sympy.Matrix([[1, 2, 3, 4], [-2, 3, 1, 0], [3, 4, -1, 2], [0, 2, 5, -1]])

print(LA.det(A), sympy.det(B), sep = '\n')