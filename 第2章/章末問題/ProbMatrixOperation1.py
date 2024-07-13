import numpy as np

n = 6; i = 3; k = 10
A = np.eye(n); A[i][i] = k
print(A, sep ='\n')