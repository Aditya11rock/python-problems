import cv2
import numpy as np

apple=cv2.imread("apple.jpg",1)
orange=cv2.imread("orange.jpg",1)

half=np.hstack((apple[:,:256],orange[:,256:]))

#Gaussian pyramid
applei=apple.copy()
gpa=[applei]
for i in range(6):
    applei=cv2.pyrDown(applei)
    gpa.append(applei)

orangei=orange.copy()
gpo=[orangei]
for i in range(6):
    orangei=cv2.pyrDown(orangei)
    gpo.append(orangei)

#laplacian pyramid
applei=gpa[5]
lpa=[applei]
for i in range(5,0,-1):
    gex=cv2.pyrUp(gpa[i])
    laplacian=cv2.subtract(gpa[i-1],gex)
    lpa.append(laplacian)

orangei=gpo[5]
lpo=[orangei]
for i in range(5,0,-1):
    gex=cv2.pyrUp(gpo[i])
    laplacian=cv2.subtract(gpo[i-1],gex)
    lpo.append(laplacian)

#add
both=[]
n=0
for ap,oora in zip(lpa,lpo):
    n=n+1
    col,row,ch=ap.shape
    laplacian=np.hstack((ap[:,0:int(col/2)],oora[:,int(col/2):]))
    both.append(laplacian)

#reconstruct
aporre=both[0]
for i in range(1,6):
    aporre=cv2.pyrUp(aporre)
    aporre=cv2.add(both[i],aporre)

cv2.imshow("blended",aporre)

cv2.imshow("half",half)
cv2.imshow("apple",apple)
cv2.imshow("orange",orange)

cv2.waitKey(0)
cv2.destroyAllWindows()