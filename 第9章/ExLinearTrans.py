import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-np.pi, np.pi, 0.01)

##### box
x = 2*np.ceil(np.cos(t + np.pi/4))-1
y = 2*np.ceil(np.sin(t + np.pi/4))-1
#####

###### curves
#p = 2; q = 0; r = 0; s = 1 # ellipse
#p = 1; q = 1/2; r = 1/4; s = 1 # flower
#x = p*np.cos(t)+ q*np.cos(6*t) + r*np.sin(14*t)
#y = s*np.sin(t)+ q*np.sin(6*t) + r*np.cos(14*t)
######

##### sample matrix
a = 3; b = -1
c = 1; d = 2

##### rotation matrix
#theta = np.pi/4 # angle of rotation
#a = np.cos(theta); b = -np.sin(theta)
#c = np.sin(theta); d = np.cos(theta)

X = a*x + b*y
Y = c*x + d*y

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(x, y)
plt.plot(X, Y, linestyle="dashed")
ax.set_aspect('equal', adjustable='box')
ax.grid()

plt.xlabel("x")
plt.ylabel("y")
plt.savefig('box.png')
plt.show()