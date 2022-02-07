import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("gradient.png",0)
ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret2,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret3,th3=cv2.threshold(img,100,255,cv2.THRESH_TRUNC)
ret4,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret5,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles=["og","bi","byi","tru","to","toi"]
images=[img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
#cv2.imshow("aditya",img)
#cv2.imshow("thres1",th1)
#cv2.imshow("thes2",th2)
#cv2.imshow("th3",th3)
#cv2.imshow("th4",th4)
#cv2.imshow("th5",th5)

#cv2.waitKey(0)
#cv2.destroyAllWindows()