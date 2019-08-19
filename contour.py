import cv2 as cv
import numpy as np

# img = cv2.imread("visage.jpeg")
# imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(imgray,127,255,0)
# im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

im = cv.imread('visage.jpeg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#cnt = contours[4]
cv.drawContours(im, contours, -1, (0,0,0), 3)
#cv.drawContours(im, contours, -1, (0,255,0), 3)

cv.imshow("img", thresh)
cv.waitKey(0)
cv.destroyAllWindows()

