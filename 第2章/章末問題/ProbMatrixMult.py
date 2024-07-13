import numpy as np

A = np.array([[1, 3, 5], [-2, 5, 1]])
B = np.array([[2, -3], [-1, 4], [5, 6]])

typeA = A.shape; typeB = B.shape
m = typeA[0]; r = typeA[1]; s = typeB[0]; n = typeB[1]
if r != s:
    print('different type')

M = np.zeros((m , n))

for i in range(m):
    for j in range(n):
        for k in range(r):
            M[i][j] += A[i][k]*B[k][j]
            
print(M)