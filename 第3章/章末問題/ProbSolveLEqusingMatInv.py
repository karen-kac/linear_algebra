import numpy as np
import numpy.linalg as LA
import sympy

A = np.array([[1, 6, -2], [-1, 5, 7], [1, 3, 3]])
B = sympy.Matrix([[1, 6, -2], [-1, 5, 7], [1, 3, 3]])

u = np.array([1, 5, 3]).reshape(3,1)
v = sympy.Matrix([1, 5, 3]).reshape(3,1)

r = LA.matrix_rank(A) 
print('rank(A) =', r)
try:
    InvA = LA.inv(A)
    InvB = B.inv()
    print('NumPy:', np.dot(InvA, u), 'SymPy:', np.dot(InvB, v), sep = '\n')
except Exception as message:
    print(message)