import numpy as np

A1 = np.array([[1,3],[2,5]])
B1 = np.eye(2)
C1 = np.zeros((2,2))
D1 = np.array([[3,-2],[1,2]])
M1 = np.block([[A1,B1],[C1,D1]])

A2 = np.array([[-2,0],[1,3]])
B2 = np.zeros((2,2))
C2 = np.eye(2)
D2 = np.array([[1,-1],[3,2]])
M2 = np.block([[A2,B2],[C2,D2]])

M3 = M1 @ M2

print('M1=', M1, 'M2=', M2, 'M1M2=', M3, sep='\n')