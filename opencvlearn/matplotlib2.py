import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread("bina1.png",cv2.IMREAD_GRAYSCALE)
_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal=np.ones((2,2),np.uint8)
dialation=cv2.dilate(mask,kernal,iterations=2)
erosion=cv2.erode(mask,kernal,iterations=2)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)
cloaing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)
grad=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)
th=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)

title=["images","mask","dialate","erode","open","close","tophat","grad"]
images=[img,mask,dialation,erosion,opening,cloaing,grad,th]
for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],"gray")
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()