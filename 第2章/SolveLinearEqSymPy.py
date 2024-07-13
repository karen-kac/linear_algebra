import sympy

x, y, z = sympy.var('x y z')
f1 = x + 2*y + 3*z - 4
f2 = -2*x + 5*y + z + 5
f3 = 4*x + 3*y + 2*z - 8
#f1 = x + 2*y + 3*z - 4
#f2 = -2*x + 5*y + z + 5
#f3 = -x + 7*y + 4*z - 1

try:
    sol = sympy.solve([f1, f2, f3], [x, y, z])
    print(sol)
except Exception as message:
    print(message)