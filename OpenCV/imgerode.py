import cv2

import numpy as np

path = r'/Users/ruben/Dropbox/BlushyPixy/August HD/HD/Irelia_nsfw.png'

image = cv2.imread(path)

window_name = "Irelia"

kernel = np.ones((6,6), np.uint8)

image = cv2.erode(image, kernel, cv2.BORDER_REFLECT)

cv2.imshow(window_name, image)
cv2.waitKey(0)