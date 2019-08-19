import numpy as np
import cv2

#im = cv2.imread('exemple_image_noir.png')
im = cv2.imread("adventure.jpeg")
print(np.where((im == [0, 0, 0])))
im[np.where((im == [0, 0, 0]).all(axis=2))] = [0, 33, 166]
#cv2.imwrite('output.png', im)


M = np.array([[4,1,8],[5,2,1]])
a = np.where((M > 2) )
print(a)
cv2.imshow("img", im)
cv2.waitKey(0)
cv2.destroyAllWindows()