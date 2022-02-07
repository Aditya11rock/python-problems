import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,img=cap.read()

    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(imgray, 1.5, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow("aditya", img)
    k=cv2.waitKey(1)
    if k==27:
        break


cap.release()
cv2.destroyAllWindows()