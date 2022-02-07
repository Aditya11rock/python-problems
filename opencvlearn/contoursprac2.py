import cv2

img=cv2.VideoCapture("vtest.avi")

ret,frame1=img.read()
ret,frame2=img.read()

while img.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    imgray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(imgray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,220,cv2.THRESH_BINARY)
    dilate=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for count in contours:
        x,y,w,h=cv2.boundingRect(count)
        if cv2.contourArea(count)<700:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Status: {}".format("Movement"),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)


    cv2.imshow("aditya",frame1)
    frame1=frame2
    ret,frame2=img.read()
    if cv2.waitKey(40)==27:
        break

img.release()
cv2.destroyAllWindows()