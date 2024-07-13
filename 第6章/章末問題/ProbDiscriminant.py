import sympy

x = sympy.symbols("x")
a, b, c, D = sympy.symbols("a b c D")

f = x**4 + a*x**2 + b*x + c
g = 4*x**3 + 2*a*x + b

D = sympy.resultant(f,g,x)
print(D)