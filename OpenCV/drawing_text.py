import cv2

path = r'/Users/ruben/Dropbox/BlushyPixy/August HD/HD/Vi_nsfw.png'

image = cv2.imread(path)

window_name = "image"

font = cv2.FONT_HERSHEY_SIMPLEX

org = (50,50)
font_scale = 1

color = (255, 0, 0)

thickness = 2

image = cv2.putText(image, 'OpenCV', org, font, font_scale, color, thickness, cv2.LINE_AA)

cv2.imwrite('/Users/ruben/Desktop/OpenCV Output/imgtextoutput.png', image)