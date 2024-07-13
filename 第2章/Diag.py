import numpy as np

n = 4
I = np.eye(n) # identity
J = np.eye(n, k = 1)
K = np.eye(n, k = -1)
A = np.arange(n**2).reshape((n, n))
d = np.diag(A)
B = np.diag(d)
print('I=', I,'J=', J, 'K=', K, 'A=', A, sep='\n')
print('np.diag(A)=', d, 'np.diag(d)=', B, sep='\n')