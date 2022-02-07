import cv2
import numpy as np
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,' ',y)
        font=cv2.FONT_ITALIC
        text=str(x)+", "+str(y)
        cv2.putText(img,text,(x,y),font,0.5,(255,0,0),1,cv2.LINE_AA)
        cv2.imshow("image",img)
    elif event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        font = cv2.FONT_ITALIC
        text = str(red) + ", " + str(green)+", "+str(blue)
        cv2.putText(img, text, (x, y), font, 0.5, (255, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow("image", img)


img=cv2.imread("messi5.jpg",1)
cv2.imshow("image",img)
cv2.setMouseCallback("image",click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()