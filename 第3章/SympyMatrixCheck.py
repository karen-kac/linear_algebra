import sympy

a = sympy.symbols('a')
X = sympy.Matrix([[1, -1, 2], [2, -1, 3], [3, a, 2-a]])
#A = sympy.Matrix([[1, 2, 1], [2, -1, 3], [3, 1, 4]]) # singular
#(a, b, c, d) = sympy.symbols('a b c d')
#A = sympy.Matrix([[a, b], [c, d]])

try:
    InvX = X.inv()
    print(InvX, X * InvX, sep='\n')
except Exception as message:
    print(message)