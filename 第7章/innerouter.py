import numpy as np
import numpy.linalg as LA
import sympy

# numpy
a = np.array([1, 2, -3])
b = np.array([5, -1, 4])

print('numpy: LA.norm(a)', LA.norm(a))
print('numpy: LA.norm(a, ord=2)', LA.norm(a, ord = 2))
print('numpy: np.dot(a, b)', np.dot(a, b))
print('numpy: a @ b', a @ b)
print('numpy: a.dot(b)', a.dot(b))
print('numpy: np.inner(a, b)', np.inner(a, b))
print('numpy: np.cross(a, b)', np.cross(a, b))

# sympy
a, b = sympy.symbols('a b')
a = sympy.Matrix([1, 2, -3])
b = sympy.Matrix([5, -1, 4])

print('sympy: a.norm(ord=2)', a.norm(ord=2))
print('sympy: a.dot(b)', a.dot(b))
print('sympy: a.cross(b)', a.cross(b))