import sympy

A = sympy.Matrix([[8, 3, 1], [2, -1, 3], [3, 1, 4]])
#A = sympy.Matrix([[1, 2, 1], [2, -1, 3], [3, 1, 4]]) # singular
#(a, b, c, d) = sympy.symbols('a b c d')
#A = sympy.Matrix([[a, b], [c, d]])

try:
    InvA = A.inv()
    print(InvA, A * InvA, sep='\n')
except Exception as message:
    print(message)