import sympy

x, y, z = sympy.var('x y z')
f1 = x**2 + y**2 + z**2 - 50
f2 = x - y + z - 2
f3 = x + 2*y + z - 1

try:
    sol = sympy.solve([f1, f2, f3], [x, y, z])
    print(sol)
except Exception as message:
    print(message)