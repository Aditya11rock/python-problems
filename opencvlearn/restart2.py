import cv2
import datetime
import numpy as np

def call_back(event,x,y,flags,param):

    if event==cv2.EVENT_LBUTTONDOWN:
        txt=str(x)+" "+str(y)
        cv2.putText(img,txt,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv2.imshow("adita",img)
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,255,0),2)
        cv2.imshow("adita",img)
img=cv2.imread("lena.jpg")

cv2.line(img,(10,10),(300,100),(25,25,0),5)
cv2.arrowedLine(img,(10,10),(100,500),(255,0,0),4)
cv2.circle(img,(300,300),100,(0,255,0),6)
cv2.rectangle(img,(200,200),(400,400),(0,0,0),6)
t=datetime.datetime.now()
ans=str(t)
cv2.putText(img,"I love lena",(130,130),fontFace=cv2.FONT_ITALIC,fontScale=2,color=(0,0,255),thickness=5)
cv2.putText(img,ans,(10,30),fontFace=cv2.FONT_ITALIC,fontScale=1,color=(0,255,255),thickness=3)

mask=np.zeros(img.shape,np.uint8)



#cv2.setMouseCallback("aditya",call_back)

ext=np.array([[[190,190],[400,190],[400,400],[190,400]]],np.int32)
#cv2.fillPoly(img,ext,(0,0,0))
cv2.drawContours(mask,ext,-1,(255,255,255),-1,cv2.LINE_AA)
result=cv2.bitwise_and(img,mask)
cv2.imshow("result",result)
cv2.imshow("adity",mask)
cv2.imshow("aditya",img)

cv2.waitKey(0)
cv2.destroyAllWindows()