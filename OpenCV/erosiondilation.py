import cv2
import numpy as np

img = cv2.imread('/Users/ruben/Desktop/August 2022 Standard/Irelia_nsfw.png')

kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=5)
img_dilation = cv2.dilate(img, kernel, iterations=5)

cv2.imshow('Erosion', img_dilation)
cv2.imwrite('/Users/ruben/Desktop/ed_output.png', img=img_dilation)
cv2.waitKey(0)