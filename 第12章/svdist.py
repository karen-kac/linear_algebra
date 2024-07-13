import matplotlib.pyplot as plt
from scipy import linalg as SLA
from PIL import Image

# Convert a color image to a black-and-white one
imagefile = Image.open('cat.jpg')
BWimage = imagefile.convert('L')
BWimage.save('black-and-white.jpg')
print('size=', BWimage.size, 'mode=', BWimage.mode)

# SVD
U, S, VT = SLA.svd(BWimage)

fig, ax = plt.subplots(1, 1)

ax.plot(range(len(S)), S)
ax.set_yscale('log')
ax.set_xlabel('rank')
ax.set_ylabel('singular value(logarithmic scale)')
plt.show()