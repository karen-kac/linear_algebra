import numpy as np

n = 6; i = 1; j = 3; k = 10
B = np.eye(n)
B[j, :] += k * B[i, :]
S = np.eye(n)
S[[i, j], :] = S[[j, i], :]
print(B, S, sep ='\n')