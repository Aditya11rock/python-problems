import cv2
from matplotlib import pyplot as plt
import numpy as np

#img=np.zeros((200,200),np.uint8)
#cv2.rectangle(img,(10,10),(100,100),(255,0,0),-1)
#cv2.rectangle(img,(50,50),(120,120),(0,127,0),-1)
img=cv2.imread("lena.jpg")

imgray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#b,g,r=cv2.split(img)
cv2.imshow("adi",img)
#cv2.imshow("adit",b)
#cv2.imshow("adiy",g)
#cv2.imshow("adia",r)

hist=cv2.calcHist([imgray],[0],None,[256],[0,256])
plt.plot(hist)
#plt.hist(b.ravel(),256,[0,256])
#plt.hist(g.ravel(),256,[0,256])
#plt.hist(r.ravel(),256,[0,256])
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()