import cv2
import numpy as np

img=cv2.imread("messi5.jpg",1)
imgray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
temp=cv2.imread("template.jpg",0)
w,h=temp.shape[::-1]
res=cv2.matchTemplate(imgray,temp,cv2.TM_SQDIFF)
threshold=0.7
loc=np.where(res>threshold)
for l in zip(*loc[::-1]):

    cv2.rectangle(img,(l[0],l[1]),(l[0]+w,l[1]+h),(0,0,255),4)

cv2.imshow("aditya",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
