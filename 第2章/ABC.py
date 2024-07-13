import numpy as np

A = np.array([[1, 2], [-1, 3]])
B = np.array([[4, 1], [2, -1]])
C = np.array([[-2, 1], [4, -5]])

ABC = A @ B @ C; BCA = B @ C @ A; CAB = C @ A @ B
ACB = A @ C @ B

print(np.trace(ABC), np.trace(BCA), np.trace(CAB))
print(np.trace(ACB))