import matplotlib.pyplot as plt
import numpy as np

Ranx = np.arange(-2.5, 3.5, 0.05)
Rany = np.arange(-3, 3, 0.05)
x, y = np.meshgrid(Ranx,Rany)

plt.axis([-3, 3.5, -3, 3])
plt.gca().set_aspect('equal', adjustable='box')

z = y**2 - x**3 + 3*x - 1
plt.contour(x, y, z, [0])
plt.show()