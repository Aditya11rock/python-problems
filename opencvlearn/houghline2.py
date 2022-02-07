import cv2
import numpy as np

img=cv2.imread("sudoku.png",1)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(imgray,10,120,apertureSize=3)
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=10,maxLineGap=30)

for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow("aditya",edges)
cv2.imshow("adityaa",img)
cv2.waitKey(0)
cv2.destroyAllWindows()