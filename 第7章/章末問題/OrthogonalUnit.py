import sympy

a = sympy.Matrix([1, -3, 2])
b = sympy.Matrix([2, 2, -1])
n = a.cross(b)

print(n/n.norm(ord=2))