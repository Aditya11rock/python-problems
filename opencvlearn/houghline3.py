import cv2
from matplotlib import pylab as plt
import  numpy as np

def region(img,vertices):
    mask=np.zeros_like(img)

    match_color=(255)
    cv2.fillPoly(mask,vertices,match_color)
    masked=cv2.bitwise_and(img,mask)
    return masked

def draw_line(img,lines):
    imd=np.zeros_like(img)
    for line in lines:
        x1,y1,x2,y2=line[0]
        cv2.line(imd,(x1,y1),(x2,y2),(255,0,0),2)
    img=cv2.addWeighted(img,0.6,imd,0.8,0.0)

    return img

img=cv2.imread("road.jpg",1)
imgray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("dam",imgray)
canny=cv2.Canny(imgray,100,200)
#cv2.imshow("adi",img)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


height=img.shape[0]
width=img.shape[1]

region_of_intresr_vertices=[
    (150,height),
    (180,height/3),
    (width,height)
]



crop=region(canny,np.array([region_of_intresr_vertices],np.int32))

lines=cv2.HoughLinesP(crop,1,np.pi/80,10,minLineLength=10,maxLineGap=10)

image_final=draw_line(img,lines)

cv2.imshow("adi",canny)
plt.imshow(image_final)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()