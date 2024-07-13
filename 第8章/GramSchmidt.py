import sympy

A = [sympy.Matrix([1, 1, 1, -1]), 
     sympy.Matrix([-1, 0, 1, 1]), 
     sympy.Matrix([0, 2, 1, 1]), 
     sympy.Matrix([1, 1, 0, 1])]

G = sympy.GramSchmidt(A, True) 
print(G)