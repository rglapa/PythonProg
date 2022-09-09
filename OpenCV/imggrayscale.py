import cv2

image = cv2.imread('/Users/ruben/Desktop/August 2022 Standard/Katarina_nsfw.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('/Users/ruben/Desktop/OpenCV Output/greyscale_output.png', gray_image)

