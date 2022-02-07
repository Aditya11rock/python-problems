import cv2
import numpy as np
lst=[]
def clicke_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255,0,0),2,cv2.LINE_AA)
        cv2.imshow("aditya",img)
        lst2=[x,y]
        lst.append(lst2)
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        lst3=np.zeros((512,512,3),np.uint8)
        lst3[:]=[blue,green,red]
        cv2.imshow("mad",lst3)
    elif event==cv2.EVENT_RBUTTONDOWN:
        for i in range(len(lst)-1):
            a=lst[i]
            b=lst[i+1]
            cv2.arrowedLine(img,(a[0],a[1]),(b[0],b[1]),(0,255,0),2,cv2.LINE_AA)
            cv2.imshow("aditya",img)
        for i in range(len(lst)-1):
            lst.pop(0)



#cv2.namedWindow("aditya",1)
#cv2.resizeWindow("aditya",512,512)

img=cv2.imread("HappyFish.jpg",1)
cv2.imshow("aditya",img)
cv2.setMouseCallback("aditya",clicke_event)

cv2.waitKey(0)
cv2.destroyAllWindows()