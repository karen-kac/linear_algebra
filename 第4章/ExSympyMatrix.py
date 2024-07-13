import sympy

n = 2
A = sympy.MatrixSymbol('A', n, n)
B = sympy.MatrixSymbol('B', n, n)
C = sympy.MatrixSymbol('C', n, n)
I = sympy.Identity(n)
O = sympy.ZeroMatrix(n, n)

X = sympy.BlockMatrix([[A, I],[-I,B]])
Y = sympy.BlockMatrix([[A,O],[C,-I]])

print(sympy.block_collapse(sympy.Inverse(X)))
print(sympy.block_collapse(sympy.Inverse(X)*Y))