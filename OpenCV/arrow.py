import cv2

path = r'/Users/ruben/Desktop/IMG_0014.JPG'

image = cv2.imread(path)

window_name = 'Image'

start_point = (0,0)

end_point = (500,500)

color = (0, 0, 255)

thickness = 9

image = cv2.arrowedLine(image, start_point, end_point, color, thickness, tipLength=0.5)

cv2.imshow(window_name, image)
cv2.waitKey(0)
k