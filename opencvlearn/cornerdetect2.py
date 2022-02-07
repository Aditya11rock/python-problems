import cv2
import numpy as np

img=cv2.imread("corner.png")
cv2.imshow("og",img)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(imgray,300,0.1,10)

corners=np.int0(corners)

for i in corners:
    x,y=i.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)

cv2.imshow("aditya",img)
cv2.waitKey(0)
cv2.destroyAllWindows()