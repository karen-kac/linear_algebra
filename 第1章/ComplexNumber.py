import numpy as np

z1 = 2 - 3j
z2 = complex(2, -3)
z3 = 3 + 0j
print(z1, z2)
print(type(z3))

print(z1.real, z1.imag)
print(type(z1.real), type(z1.imag))
print(z1.conjugate())

A = np.array([[2 + 3j, -1 + 2j, 2 + 1j], [-3 - 1j, 3 + 4j, 2 - 1j]])
B = np.array([[1 + 1j, 2j], [-1j, 3 + 2j], [5 - 2j, 6 + 1j]])

C = A @ B
D = B @ A
print(C, D, sep = '\n')
print(np.conjugate(C.transpose()))
print(C.T)