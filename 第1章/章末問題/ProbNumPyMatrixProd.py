import numpy as np

A = np.array([[3, 5], [-2, 1]])
B = np.array([[1, 0, -2], [3, -1, 2]])
C = np.array([[1, 2], [-1, 9], [3, -4]])
D = np.array([[3, 8, 2], [0, 2, 1]])

E = np.dot(A, B)
F = np.dot(C, D)
print(C, D, sep='\n')