import cv2
import numpy as np

def nothing(x):
    print(x)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("aditya",0)
cv2.resizeWindow("aditya",512,512)
cv2.createTrackbar("B","aditya",0,255,nothing)
cv2.createTrackbar("G","aditya",0,255,nothing)
cv2.createTrackbar("R","aditya",0,255,nothing)
switch='0 :OFF\n 1:ON'
cv2.createTrackbar(switch,"aditya",0,1,nothing)

while(1):
    cv2.imshow("aditya",img)
    k=cv2.waitKey(1)
    if(k==27):
        break
    b=cv2.getTrackbarPos("B","aditya")
    g = cv2.getTrackbarPos("G", "aditya")
    r = cv2.getTrackbarPos("R", "aditya")
    s = cv2.getTrackbarPos(switch, "aditya")
    if(s==0):
        img[:]=0
    else:

        img[:]=[b,g,r]

cv2.destroyAllWindows()