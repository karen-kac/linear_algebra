import numpy as np
import numpy.linalg as LA
import random
import matplotlib.pyplot as plt

# Generate a random real symmetric matrix A
n = 12 # size of matrices
R = np.array([random.uniform(-1,1) for i in range(n**2)], dtype = np.complex).reshape(n, n) 
U = np.triu(R, k = 0) # upper triangular matrix
L = U.transpose() # L = U^T
D = np.diag(np.diag(U), k = 0) # diagonal part of U
A = U + L - D # real symmetric case
val, Q = LA.eig(A) # eigenvalues and vectors of A
# Q can be regarded as a random orthogonal matrix
val2, vect = LA.eig(Q) # eigenvalues and vectors of Q

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.scatter(np.real(val),np.imag(val))
ax2.scatter(np.real(val2),np.imag(val2))
ax2.set_aspect('equal', adjustable='box')
ax1.set_xlabel('Real part'); ax2.set_xlabel('Real part')
ax1.set_ylabel('Imaginary part')
plt.show()