import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('visage.jpeg')
#blur = cv2.blur(img,(100,100))
blur = cv2.bilateralFilter(img, 9, 1500, 1500)

kernel = np.ones((10,10),np.uint8)
erosion = cv2.dilate(img,kernel, iterations=1)
cv2.imshow('erosion',erosion)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()