import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as SLA
from PIL import Image

# Convert a color image to a black-and-white one
imagefile = Image.open('cat.jpg')
BWimage = imagefile.convert('L')
BWimage.save('black-and-white.jpg')

# SVD
U, S, VT = SLA.svd(BWimage)

rlist = [1, 10, 20, 50, 300, 400] # rank

dict = {} # empty dictionary

# Generate images of a specified rank
for r in rlist:
    Utmp = U[:, :r] 
    Stmp = np.array(SLA.diagsvd(S[ :r], M = r, N = r)) 
    VTtmp = VT[:r, :] 
    Ar = np.array(Utmp @ Stmp @ VTtmp)
    imageuint8 = Image.fromarray(np.uint8(Ar), mode = 'L')
    filename = 'PictRank{}.jpg'.format(r)
    imageuint8.save(filename)
    dict[rlist.index(r)] = filename
   
# Display images horizontally and vertically
fig, ax = plt.subplots(3, 2, figsize=(14, 10))

for i in range(len(rlist)): 
    imagefile0 = Image.open(dict[i]) # i-th image open
    j = i % 3; k = i // 3 
    ax[j][k].imshow(imagefile0, cmap='gray')
    ax[j][k].set_title('rank = {}'.format(rlist[i]))

# Adjusting the distance between images
fig.subplots_adjust(wspace=-0.4, hspace=0.3)

plt.show()