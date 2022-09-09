import cv2
import numpy as np

FILE_NAME = '/Users/ruben/Dropbox/BlushyPixy/August HD/HD/Aqua_nsfw.png'
try:
    img = cv2.imread(FILE_NAME)

    (rows, cols) = img.shape[:2]

    M = cv2.getRotationMatrix2D((cols/2, rows/2), 180, 1)
    res = cv2.warpAffine(img, M, (cols,rows))

    cv2.imwrite('/Users/ruben/Desktop/Aqua_n.png', res)
except IOError:
    print('Error when reading file')