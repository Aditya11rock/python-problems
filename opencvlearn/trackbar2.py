import cv2


def nothing(x):
    print(x)

img=cv2.imread("HappyFish.jpg")
cv2.namedWindow("aditya",1)
cv2.resizeWindow("aditya",512,512)
cv2.createTrackbar("CP","aditya",10,400,nothing)

switch='color/gray'
cv2.createTrackbar(switch,"aditya",0,1,nothing)
while(1):
    img = cv2.imread("HappyFish.jpg")
    img=cv2.imshow("aditya",img)
    pos=cv2.getTrackbarPos("CP","aditya")
    text=str(pos)
    print(text)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,text,(260,180),font,10,(255,255,0))

    k=cv2.waitKey(1)
    if(k==27):
        break
    s=cv2.getTrackbarPos(switch,"aditya")
    if(s==0):
        pass
    else:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



cv2.destroyAllWindows()
