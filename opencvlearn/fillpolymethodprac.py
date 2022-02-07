import cv2
import numpy as np

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        st=str(x)+" "+str(y)
        cv2.putText(img,st,(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
        print(st)
        cv2.imshow("aditya",img)


img=cv2.imread("useroad.png",1)
cv2.resizeWindow("aditya",768,1366)
cv2.imshow("aditya",img)
cv2.setMouseCallback("aditya",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()