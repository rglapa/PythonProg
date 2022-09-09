import cv2

image = cv2.imread('/Users/ruben/Desktop/August 2022 Standard/Vi_nsfw.png')


#cv2.imshow('Original Image', image)
#cv2.waitKey(0)

Gaussian = cv2.GaussianBlur(image, (103,11), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.imwrite('/Users/ruben/Desktop/output.png',Gaussian)

#median = cv2.medianBlur(image, 17)
#cv2.imshow('Median Blurring', median)

#bilateral = cv2.bilateralFilter(image, 15, 15, 9)
#cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
