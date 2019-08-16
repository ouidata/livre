import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    min_mask = np.array([0, 0, 200])
    max_mask = np.array([255, 255, 255])

    # White has an HSV value of 0-255, 0-255, 255
    # Black has an HSV value of 0-255, 0-255,0.

    mask = cv2.inRange(hsv, min_mask, max_mask)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)



    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()