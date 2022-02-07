import cv2
import numpy as np

img=cv2.imread("smarties.png")
cv2.resizeWindow("aditya",800,800)
output=img.copy()
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgray=cv2.medianBlur(imgray,5)
circles=cv2.HoughCircles(imgray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

detect_circle=np.uint16(np.around(circles))

for (x,y,r) in detect_circle[0,:]:
    cv2.circle(output,(x,y),r,(0,255,0),3)
    cv2.circle(output,(x,y),2,(0,255,0),2)


cv2.imshow("aditya",output)
cv2.waitKey(0)
cv2.destroyAllWindows()