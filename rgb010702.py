import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = np.array(Image.open("/home/nikky/Downloads/800px-Crew_of_STS-107,_official_photo.jpg"))

h, w, d = img.shape

newImage = np.zeros((h, w, d))

for i in range(1, h-1):
    for j in range(1, w-1):
        r, g, b = img[i-1, j-1]
        newImage[i,j] = (r*0.1, g*0.7, b*0.2)

plt.imshow(newImage)
plt.show()
