import numpy as np

A = np.array([[-1 + 3j, 2 + 3j, 4 + 1j], [-4 - 3j, 1 + 1j, 3 - 2j]])
B = np.array([[2 + 2j, 1j], [1-1j, 1 + 1j], [3 - 1j, 5 + 2j]])

C = np.dot(A, B)
D = np.dot(B, A)
print(C, D, sep = '\n')