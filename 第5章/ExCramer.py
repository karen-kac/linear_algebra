import sympy

A = sympy.Matrix([[1, 2, -4], [-2, 3, 1], [1, 1, 3]])
b = sympy.Matrix([[7], [-8], [3]])

D = sympy.det(A)

try:
    A.col_del(0)
    newA = A.col_insert(0, b)
    print(newA)
    Ax = sympy.det(newA)
    x = sympy.Rational(Ax, D)
    print(x)
except Exception as message:
    print(message)