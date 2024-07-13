import numpy as np

A = np.array([[1, 3, -5], [-4, 6, 2]])
B = np.array([[2, -3], [-1, 4], [5, 6]])

AT = A.T; BT = B.T
C = A @ B; CT = C.T
#AT = A.transpose(); BT = B.transpose()
#C = A @ B; CT = C.transpose()
print(CT, BT @ AT, sep = '\n')