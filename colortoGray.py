import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = np.array(Image.open("/home/nikky/Downloads/50TPancard.jpg"))

h, w, d = img.shape

newImage = np.zeros((h, w, d))

for i in range(1, h):
    for j in range(1, w):
        r, g, b = img[i-1, j-1]
        avg = np.round(np.average([r, g, b]))
        newImage[i,j] = (avg, avg, avg)

plt.imshow(newImage)
plt.show()        
