####  color detection from picture


import cv2
import numpy as np
def empty(a):
    pass
img=cv2.imread("Resources/lambo.png")

cv2.namedWindow("track")
cv2.resizeWindow("track",420,420)
cv2.createTrackbar("h min","track",0,179,empty)
cv2.createTrackbar("h max","track",19,179,empty)
cv2.createTrackbar("s min","track",110,255,empty)
cv2.createTrackbar("s max","track",240 ,255,empty)
cv2.createTrackbar("v min","track",153,255,empty)
cv2.createTrackbar("v max","track",255,255,empty)

while(1):
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("h min","track")
    h_max=cv2.getTrackbarPos("h max", "track")
    s_min=cv2.getTrackbarPos("s min", "track")
    s_max=cv2.getTrackbarPos("s max", "track")
    v_min=cv2.getTrackbarPos("v min", "track")
    v_max=cv2.getTrackbarPos("v max", "track")
    #print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower =np.array([h_min,s_min,v_min])
    upper =np.array([h_max,s_max,v_max])


    mask =cv2.inRange(imghsv,lower,upper)
    imgres=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("orignal image",img)
    cv2.imshow("mask image ",mask)
    cv2.imshow("output",imgres)
    if cv2.waitKey(1)&0XFF==ord('q'):
        break




