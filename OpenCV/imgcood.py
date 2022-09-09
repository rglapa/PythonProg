import numpy as np
import cv2

font = cv2.FONT_HERSHEY_COMPLEX
img2 = cv2.imread('/Users/ruben/Desktop/shapes.jpg',cv2.IMREAD_COLOR)

img = cv2.imread('/Users/ruben/Desktop/shapes.jpg',cv2.IMREAD_GRAYSCALE)

_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

contours, _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)

    cv2.drawContours(img2, [approx], 0, (0,0,255), 5)

    n = approx.ravel()
    i = 0

    for j in n:
        if i % 2 == 0:
            x = n[i]
            y = n[i+1]

            string = str(x) + " " + str(y)

            if i == 0:
                cv2.putText(img2, "Arrow tip", (x,y), font, 0.5, (255,0,0))

            else:
                cv2.putText(img2, string, (x,y), font, 0.5, (0,255,0))
        i = i+1

cv2.imshow('image2',img2)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
