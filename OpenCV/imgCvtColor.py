import cv2

path = r'/Users/ruben/Dropbox/BlushyPixy/August HD/HD/Qiyana_nsfw.png'

src = cv2.imread(path)

window_name = 'Image'

image = cv2.cvtColor(src, cv2.COLOR_BGR2HLS)

cv2.imwrite('/Users/ruben/Desktop/invert_output.png', image)