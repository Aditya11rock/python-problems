import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("aditya",1)
cv2.createTrackbar("LH","aditya",0,255,nothing)
cv2.createTrackbar("LS","aditya",0,255,nothing)
cv2.createTrackbar("LV","aditya",0,255,nothing)
cv2.createTrackbar("UH","aditya",255,255,nothing)
cv2.createTrackbar("US","aditya",255,255,nothing)
cv2.createTrackbar("UV","aditya",255,255,nothing)

while True:
    ret,img=cap.read()
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("LH","aditya")
    l_s=cv2.getTrackbarPos("LS","aditya")
    l_v=cv2.getTrackbarPos("LV","aditya")

    u_h=cv2.getTrackbarPos("UH","aditya")
    u_s=cv2.getTrackbarPos("US","aditya")
    u_v=cv2.getTrackbarPos("UV","aditya")


    l_b=np.array([l_h,l_s,l_v])
    u_b=np.array([u_h,u_s,u_v])

    mask=cv2.inRange((hsv),l_b,u_b)

    res=cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("img",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    k=cv2.waitKey(1)
    if(k==27):
        break

cap.release()
cv2.destroyAllWindows()