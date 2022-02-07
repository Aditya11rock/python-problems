import cv2
import datetime
img=cv2.VideoCapture(0)

while True:
    ret,frame=img.read()
    print(ret)
    fort=cv2.FONT_HERSHEY_SIMPLEX
    text="width : "+str(img.get(3))+" height : "+str(img.get(4))
    datet=str(datetime.datetime.now())+"\n"+text
    frame=cv2.putText(frame,datet,(10,50),fort,1,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow("adia",frame)
    a=cv2.waitKey(2)
    if(a==ord("q")):
        break
img.release()
cv2.destroyAllWindows()
