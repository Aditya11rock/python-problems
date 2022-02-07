import cv2

img=cv2.imread("FindingContours.png")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(imgray,220,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
a=0
for count in contours:
    approx=cv2.approxPolyDP(count,0.01*cv2.arcLength(count,True),True)

    x=approx.ravel()[0]
    y=approx.ravel()[1]

    if len(approx)==3:
        cv2.putText(img,"Triangle",(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
        cv2.drawContours(img,[count],0,(0,255,0),4)
    elif len(approx)==4:
        x,y,w,h=cv2.boundingRect(count)
        n=float(w/h)
        if(n>=0.95 and n<=1.05):
            cv2.putText(img, "square", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.drawContours(img, [count], -1, (0, 255, 0), 4)
        else:
            cv2.putText(img, "Rectangle", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.drawContours(img, [count], -1, (0, 255, 0), 4)
    elif len(approx)==5:
        cv2.putText(img, "Pentagon", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.drawContours(img, [count], 0, (0, 255, 0), 4)
    elif len(approx)==6:
        cv2.putText(img, "Hexagon", (x -10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.drawContours(img, [count], 0, (0, 255, 0), 4)
    elif len(approx)==7:
        cv2.putText(img, "Heptagon", (x + 30, y+10 ), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.drawContours(img, [count], 0, (0, 255, 0), 4)
    elif len(approx)==8:
        cv2.putText(img, "octagon", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.drawContours(img, [count], 0, (0, 255, 0), 4)
    else:
        cv2.putText(img, "circle", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.drawContours(img, [count], 0, (0, 255, 0), 4)


cv2.imshow("aditya",img)
cv2.waitKey(0)
cv2.destroyAllWindows()