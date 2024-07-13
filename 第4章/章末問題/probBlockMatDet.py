import numpy as np
import numpy.linalg as LA

A = np.random.uniform(low = -10, high = 10, size = (2, 2))
B = np.random.uniform(low = -10, high = 10, size = (2, 2))

M = np.block([[A, B], [B, A]])

d = LA.det(A+B)*LA.det(A-B)

s = LA.det(A**2 - B**2)
t = LA.det(A)**2 - LA.det(B)**2

print('M=', M, '|M|=', LA.det(M), '|A+B||A-B|=', d, '|A**2-B**2|=', s, '|A|**2-|B|**2=', t, sep='\n')