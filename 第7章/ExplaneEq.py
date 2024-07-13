import sympy

OA, OB, OC = sympy.symbols('OA OB OC')
AB, AC = sympy.symbols('AB AC')
x, y, z = sympy.symbols('x y z')
OA = sympy.Matrix([2,-1,-2])
OB = sympy.Matrix([3, 1, 4])
OC = sympy.Matrix([1, 2, -3])
AB = OB - OA
AC = OC - OA

OP = sympy.Matrix([x, y, z])
n = AB.cross(AC) # normal vector

print(n.dot(OP - OA),'= 0')