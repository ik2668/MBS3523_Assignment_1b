import cv2
import numpy as np

d=256
CD=2 * d

cam = cv2.VideoCapture(0)

while True:
    frame, img = cam.read()

    img1 = cv2.resize(img, (d,d))
    img2 = cv2.flip(img1, 1)
    img3 = cv2.flip(img1, 0)
    img4 = cv2.flip(img2, 0)
    mer = np.zeros((CD, CD, 3), dtype=np.uint8)
    mer[0:d, 0:d] = img1
    mer[0:d, d:CD] = img2
    mer[d:CD, 0:d] = img3
    mer[d:CD, d:CD] = img4

    cv2.imshow('img', mer)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
