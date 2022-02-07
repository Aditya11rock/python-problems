import cv2



img=cv2.imread("messi5.jpg",1)

print(img.shape)
print(img.size)
print(img.dtype)
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))
ball=img[285:340, 335:385]
img[280:335, 410:460]=ball
#cv2.imshow("adi",ball)

print(ball.dtype)
print(ball.size)
print(ball.shape)

cv2.imshow("aditya",img)


cv2.waitKey(0)
cv2.destroyAllWindows()

#328 285 401 338
#70 272 169 324

