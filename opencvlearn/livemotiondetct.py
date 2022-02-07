import cv2

cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
ret,frame2=cap.read()


while cap.isOpened():
    img=cv2.absdiff(frame1,frame2)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(img,(5,5),0)
    _,thresh=cv2.threshold(blur,100,255,cv2.THRESH_BINARY)
    dialate=cv2.dilate(thresh,None,iterations=3)
    countours,hirarchy=cv2.findContours(dialate,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for count in countours:
        x,y,w,h=cv2.boundingRect(count)
        if cv2.contourArea(count)>400:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame1,"status: {}".format("movement"),(10,40),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)

    cv2.imshow("frame",frame1)
    frame1=frame2
    ret,frame2=cap.read()

    k=cv2.waitKey(1)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()