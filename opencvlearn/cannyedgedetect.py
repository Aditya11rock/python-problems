import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

img=cv2.imread("opencv-logo.png",cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("aditya",0)
cv2.resizeWindow("aditya",512,512)
cv2.createTrackbar("min","aditya",0,255,nothing)
cv2.createTrackbar("max","aditya",0,255,nothing)
cv2.imshow("og",img)
while True:
    img = cv2.imread("opencv-logo.png", cv2.IMREAD_GRAYSCALE)
    min = int(cv2.getTrackbarPos("min", "aditya"))
    max = int(cv2.getTrackbarPos("max", "aditya"))
    canny = cv2.Canny(img, min, max)

    images = [img, canny]
    titles = ["og", "canny"]

    k=cv2.waitKey(1)

    if (k==27):
        break

    cv2.imshow("canny",canny)




cv2.destroyAllWindows()


