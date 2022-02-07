import cv2

img=cv2.VideoCapture(0)
while True:
    ret,frame=img.read()
    cv2.imshow("video",frame)
    imgray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _,thresh=cv2.threshold(imgray,127,255,0)
    contour,hirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,contour,-1,(255,0,0),3)
    cv2.imshow("adotya",frame)
    k=cv2.waitKey(5)
    if k==27:
        break


img.release()

cv2.destroyAllWindows()
