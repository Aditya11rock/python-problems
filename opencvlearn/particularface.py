import cv2
import numpy as np

cascade_face=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("aditya.png")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face1=cascade_face.detectMultiScale(imgray,1.5,4)

cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,frame=cap.read()
    frame_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face2=cascade_face.detectMultiScale(frame,1.5,4)

    for fic in face2:
        if fic in face1:
            x,y,w,h=fic
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,"SuperHero",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        elif fic not in face1:
            x, y, w, h = fic
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Donkey", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)


    cv2.imshow("aditya", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()