import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Open the image
img = np.array(Image.open('/home/nikky/Downloads/800px-Crew_of_STS-107,_official_photo.jpg')).astype(np.uint8)

#Now get the height, width and channel of image
h, w, d = img.shape

#Define image with 0s
newImage = np.zeros((h, w, d))

#Now take the average of 9 pixel in 3X3 square and place the value at the centre of square.

for channel in range(d):
    for i in range(1, h-2):
        for j in range(1, w-2):
            newImage1 = ((img[i-1, j-1, channel]) + (img[i-1, j, channel]) + (img[i-1, j+1, channel]) + \
                       (img[i, j-1, channel]) + (img[i, j, channel]) + (img[i, j+1, channel]) + \
                       (img[i+1, j-1, channel]) + (img[i+1, j, channel]) + (img[i+1, j+1, channel])).astype(np.int32) 
            Meanimage = np.divide(newImage1, 9)
            newImage[i, j, channel] = newImage1
            

# now add the images r g and b
rgb_edge = newImage[:,:,0] + newImage[:,:,1] + newImage[:,:,2]

plt.figure()
plt.title('Pan_image')
plt.imshow(newImage)
plt.show()
