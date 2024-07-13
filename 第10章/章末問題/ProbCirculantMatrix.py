import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from scipy.linalg import circulant

# Generate a circulant matrix A
A = circulant([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
val, Q = LA.eig(A) # eigenvalues and vectors of A

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(np.real(val),np.imag(val))
ax.set_xlabel('Real part'); ax.set_xlabel('Real part')
ax.set_ylabel('Imaginary part')
plt.show()