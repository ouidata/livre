import numpy as np
import cv2

#im = cv2.imread('exemple_image_noir.png')
im = cv2.imread("adventure.jpeg")

im_hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
print(im_hsv)
print("#####")
print(im_hsv[4])
im_hsv[np.where(((im_hsv > [0, 0, 0]) & (im_hsv <= [31, 255, 255])).all(axis=2))] = [30, 50, 50]
im_hsv[np.where(((im_hsv > [32, 0, 0]) & (im_hsv <= [61, 255, 255])).all(axis=2))] = [60, 50, 50]
im_hsv[np.where(((im_hsv > [62, 0, 0]) & (im_hsv <= [91, 50, 50])).all(axis=2))] = [90, 50, 50]
im_hsv[np.where(((im_hsv > [92, 0, 0]) & (im_hsv <= [121, 255, 255])).all(axis=2))] = [120, 50, 50]
im_hsv[np.where(((im_hsv > [122, 0, 0]) & (im_hsv <= [151, 255, 255])).all(axis=2))] = [150, 50, 50]
im_hsv[np.where(((im_hsv > [152, 0, 0]) & (im_hsv <= [181, 255, 255])).all(axis=2))] = [180, 50, 50]
im_hsv[np.where(((im_hsv > [182, 0, 0]) & (im_hsv <= [211, 255, 255])).all(axis=2))] = [210, 50, 50]

im_nv = cv2.cvtColor(im_hsv, cv2.COLOR_HSV2BGR)
# print(np.where((im == [0, 0, 0])))
# im[np.where((im == [0, 0, 0]).all(axis=2))] = [0, 33, 166]
# #cv2.imwrite('output.png', im)


# M = np.array([[4,1,8],[5,2,1]])
# a = np.where((M > 2) )
# print(a)
cv2.imshow("im_hsv", im_hsv)
cv2.imshow("im_nv", im_nv)
cv2.imshow("im", im)
cv2.waitKey(0)

cv2.destroyAllWindows()