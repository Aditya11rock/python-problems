import cv2

img=cv2.imread("lena.jpg")

cv2.imshow("og",img)
layer=img.copy()
lst=[layer]
for i in range(5):
    layer=cv2.pyrDown(layer)
    lst.append(layer)

for i in range(5,0,-1):
    gp=cv2.pyrUp(lst[i])
    lp=cv2.subtract(lst[i-1],gp)
    cv2.imshow(str(i),lp)




cv2.waitKey(0)
cv2.destroyAllWindows()