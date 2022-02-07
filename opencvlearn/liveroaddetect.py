import cv2
import numpy as np
#determining region of interest
def region(img,vertices):
    mask=np.zeros_like(img)
    match_color=(255,)
    masked=cv2.fillPoly(mask,vertices,match_color)
    final=cv2.bitwise_and(img,masked)
    return final
#draw those detected lines
def draw_lines_on_img(img,lines):

    if lines is not None:


        for line in lines:
            x1,y1,x2,y2=line[0]
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)

        return img



imk=cv2.VideoCapture("drivingd.mp4")
ret,img=imk.read()

height = img.shape[0]
width = img.shape[1]


region_of_intrest = [(127,735),(5,571),(425,508),(544,419),(616,360),(670,358),(713,382),(826,427),(1012,501),(1340,635)

    ]


while imk.isOpened():
    ret,img=imk.read()


    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img, 10, 255)

    _,thresh=cv2.threshold(canny,100,200,cv2.THRESH_BINARY)
    dialate=cv2.dilate(thresh,(5,5),iterations=3)
    # cv2.imshow("canny",canny)
    # cv2.imshow("og",img)

    crop = region(dialate, np.array([region_of_intrest], np.int32))
    # cv2.imshow("aditya",crop)

    lines = cv2.HoughLinesP(crop,2, np.pi / 180, 10, minLineLength=10, maxLineGap=5)
    final_img = draw_lines_on_img(img, lines)

    cv2.imshow("aditya",img)
    k=cv2.waitKey(10)
    if k==27:
        break

imk.release()
cv2.destroyAllWindows()
