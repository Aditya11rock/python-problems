import cv2
import matplotlib.pyplot as plt

img=cv2.imread("prac3.jpeg")

b,g,r=cv2.split(img)
cv2.imshow("adi1",img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)
plt.hist(r.ravel(),256,[0,255])
plt.hist(b.ravel(),256,[0,255])
plt.hist(g.ravel(),256,[0,255])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()