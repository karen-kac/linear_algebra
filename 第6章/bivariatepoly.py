import sympy

x, y = sympy.symbols("x y")
a, b, R = sympy.symbols("a b R")

f = x*y - 1
g = x**2 + y**2 - 4

R = sympy.resultant(f,g,x)
print(R)