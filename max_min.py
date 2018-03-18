import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = np.array(Image.open("/home/nikky/Downloads/50TPancard.jpg"))

h, w, d = img.shape

newImage = np.zeros((h, w, d))

for i in range(1, h-1):
    for j in range(1, w-1):
        r, g, b = img[i-1, j-1]
        listV = [r, g, b]
        maxV = max(listV)
        minV = min(listV)
        avg = np.round(np.average([maxV, minV]))
        newImage[i,j] = (avg, avg, avg)

plt.imshow(newImage)
plt.show()
