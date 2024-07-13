import numpy as np
import numpy.linalg as LA

A = np.array([[4, 1, -1], [1, 2, -1], [-1, -1, 2]])
t = np.pi/4
R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
print(A)
print(LA.eig(A))

print(R)
print(LA.eig(R))