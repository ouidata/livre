import numpy as np
import cv2 as cv

#lire une image
img = cv.imread("visage.jpeg")

#changer la colorimetrie
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Mettre en noir et blanc
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#ne prendre qu'une partie de l'image en fonction d'une couleur
mask_min = np.array([30,0,0])
mask_max = np.array([50,250,250])

img_withmask = cv.inRange(img, mask_min, mask_max)

#avoir le contour
en_desous_on_ne_prend_pas = 200
au_dessus_on_prend = 400
img_contour = cv.Canny(img,en_desous_on_ne_prend_pas,au_dessus_on_prend)

#grossir un contour
kernel = np.ones((10,10), np.uint8)
img_contour_grossi = cv.dilate(img_contour, kernel, iterations=1)

#faire un flou
img_blur = cv.bilateralFilter(img, 9, 1500, 1500)

#changer une couleur par une autre : on fait une recherche dans le tableau qui correspond à une image
img[np.where((img == [0, 0, 0]).all(axis=2))] = [0, 33, 166]

# afficher en surimpression un mask sur une image
res = cv.bitwise_and(img, img, mask=img_contour_grossi)

#afficher une image
cv.imshow("mon titre", res)
cv.waitKey(0)
cv.destroyAllWindows()

