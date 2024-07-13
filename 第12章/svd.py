import numpy as np
import numpy.linalg as LA

A = np.array([[1, 2], [1, -1], [2, -1]])
print('A =', A, sep = '\n')
print('Rank of A =', LA.matrix_rank(A))
print('A^TA=', np.transpose(A) @ A)

print('*** Case full_matrices = False ***')
U, S, VT = LA.svd(A, full_matrices = False)
print(U.shape, S.shape, VT.shape)

print('U =',U, 'Sigma =', np.diag(S), 'V^T =', VT, sep = '\n')
# Reconstruction of matrix A
print('USV^T =', U @ np.diag(S) @ VT, sep = '\n')

print('*** Case full_matrices = True(default) ***')
U0, S0, VT0 = LA.svd(A)
print(U0.shape, S0.shape, VT0.shape)
print('U =',U0, 'Sigma =', np.diag(S0), 'V^T =', VT0, sep = '\n')

# Reconstruction of matrix A
m, n = A.shape
print(U0[:,:n] @ np.diag(S0) @ VT[:m,:])