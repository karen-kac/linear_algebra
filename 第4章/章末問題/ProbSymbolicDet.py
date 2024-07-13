import sympy

(a, b, c) = sympy.symbols('a b c')
A = sympy.Matrix([[a, a, a], [a, b, b], [a, b, c]])

DetA = sympy.det(A)
print(DetA)
print(sympy.factor(DetA))