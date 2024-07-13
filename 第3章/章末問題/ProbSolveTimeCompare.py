import numpy as np
import numpy.linalg as LA
import time

A = np.random.rand(2000, 2000)
b = np.random.rand(2000)

start1 = time.time()
x1 = LA.inv(A) @ b
end1 = time.time()

t1 = end1 - start1

start2 = time.time()
x2 = LA.solve(A, b)
end2 = time.time()  

t2 = end2 - start2

print(t1, t2)