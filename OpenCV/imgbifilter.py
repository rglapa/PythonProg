import cv2

img = cv2.imread('/Users/ruben/Dropbox/BlushyPixy/August HD/HD/Qiyana_nsfw.png')

bilateral = cv2.bilateralFilter(img, 40, 100, 75)

cv2.imwrite('/Users/ruben/Desktop/output_bilat.png', img)