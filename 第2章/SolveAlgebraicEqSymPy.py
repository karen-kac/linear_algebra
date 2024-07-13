import sympy

x, y = sympy.var('x y')
f1 = x**2 + y**2 - 25
f2 = x + y - 2

try:
    sol = sympy.solve([f1, f2], [x, y])
    print(sol)
except Exception as message:
    print(message)