import cv2
import numpy as np
img=cv2.imread("chess.jpg")
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgray=np.float32(imgray)
cv2.imshow("man",img)

corner=cv2.cornerHarris(imgray,3,5,0.04)

dst=cv2.dilate(corner,None)

img[dst >0.01 * dst.max()]=[0,0,255]
print(len(dst))


cv2.imshow("adi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()