import cv2

FILE_NAME = '/Users/ruben/Dropbox/BlushyPixy/August HD/HD/Aqua_nsfw.png'

try:
    img = cv2.imread(FILE_NAME)

    edges = cv2.Canny(img, 100, 200)

    cv2.imwrite('/Users/ruben/Desktop/output_nedge.png', edges)
except:
    print('Error when reading file')