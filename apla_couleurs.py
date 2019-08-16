# import the necessary packages
import scipy.spatial as sp
import matplotlib.pyplot as plt
import cv2
import numpy as np
print("toot")
# Stored all RGB values of main colors in a array
main_colors = [(0, 0, 0),
               (255, 255, 255),
               (255, 0, 0),
               (0, 255, 0),
               (0, 0, 255),
               (255, 255, 0),
               (0, 255, 255),
               (255, 0, 255),
               (198, 152, 126),
               ]

image = cv2.imread("visage.jpeg")
# convert BGR to RGB image
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w, bpp = np.shape(image)

# Change colors of each pixel
# reference :https://stackoverflow.com/a/48884514/9799700
for py in range(0, h):
    for px in range(0, w):
        print(py,px)
        ########################
        # Used this part to find nearest color
        # reference : https://stackoverflow.com/a/22478139/9799700
        input_color = (image[py][px][0], image[py][px][1], image[py][px][2])
        tree = sp.KDTree(main_colors)
        ditsance, result = tree.query(input_color)
        nearest_color = main_colors[result]
        ###################

        image[py][px][0] = nearest_color[0]
        image[py][px][1] = nearest_color[1]
        image[py][px][2] = nearest_color[2]

# show image
# plt.figure()
# plt.axis("off")
# plt.imshow(image)
# plt.show()
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
