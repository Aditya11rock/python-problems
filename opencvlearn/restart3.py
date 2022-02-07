import cv2
import numpy as np
import matplotlib.pyplot as plt
lst=[]

def masker(im,ls):
    mask=np.zeros(im.shape,np.uint8)
    ext=np.array([ls],np.int32)
    cv2.drawContours(mask,ext,-1,(255,255,255),-1,cv2.LINE_AA)
    cv2.imshow("ron",mask)
    img2=cv2.imread("prac8.jpeg")
    h,w,_=mask.shape
    print(h,w)
    #cv2.resize(img2,(w,h))
    result=cv2.bitwise_and(img2,mask)
    cv2.imshow("result",result)
    b,g,r=cv2.split(result)
    #test=im[ls[0],ls[1]]
    #cv2.imshow("adit",test)

    plt.hist(b.ravel(),256,[0,255])
    plt.hist(g.ravel(),256,[0,255])
    plt.hist(r.ravel(),256,[0,255])
    plt.xlabel("B,G,R channels")
    plt.show()


def call_back(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        #print(x,y,sep=" ")
        lst2=[x,y]
        txt=str(x)+" "+str(y)
        cv2.putText(img,txt,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2)
        cv2.imshow("aditya",img)
        lst.append(lst2)
        #lst.insert(lst2)
        if len(lst)==4:
            lst3=list(lst)
            masker(img,lst3)



img=cv2.imread("prac8.jpeg")
cv2.imshow("aditya",img)
#img3=img.copy()
#img3[:,:,1]=0
#img3[:,:,0]=0
#cv2.imshow("adi",img3)
cv2.setMouseCallback("aditya",call_back)

cv2.waitKey(0)
cv2.destroyAllWindows()