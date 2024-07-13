import sympy

x, y = sympy.symbols("x y")
a, b, D = sympy.symbols("a b D")

f = x**3 + a*x + b
g = 3*x**2 + a

D = sympy.resultant(f,g,x)
print(D)