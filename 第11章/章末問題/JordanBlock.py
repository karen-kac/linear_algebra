import numpy as np
import numpy.linalg as LA

J = np.array([[2, 1, 0], [0, 2, 1], [0, 0, 2]])
print(LA.eig(J))