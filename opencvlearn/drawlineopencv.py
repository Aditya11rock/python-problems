import cv2
import numpy as np

img=cv2.imread("sudoku.png",1)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny=cv2.Canny(img,50,150,apertureSize=3)
lines=cv2.HoughLines(canny,1,np.pi/180,200)

for line in lines:
    rho,the=line[0]
    a=np.cos(the)
    b=np.sin(the)
    x0=a*rho
    y0=b*rho

    x1=int(x0 + 1000*(-b))
    y1=int(y0 + 1000*a)

    x2=int(x0 - 1000*(-b))
    y2=int(y0 - 1000*a)
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)

cv2.imshow("lines",img)
cv2.waitKey(0)
cv2.destroyAllWindows()