import cv2
import numpy as np
def nothing(x):
    pass

cam = cv2.VideoCapture(0)

frame = np.zeros((512, 512, 3), np.uint8)

while True:
    ret, img = cam.read()

    cv2.imshow("original", img)

    blur = cv2.GaussianBlur(img,(5,5),0)
    cv2.imshow("GaussianBlur", blur)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV color space", hsv)

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    GB = cv2.GaussianBlur(grey,(5,5),0)
    canny = cv2.Canny(GB, 100, 200)
    cv2.imshow("Canny edges", canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
