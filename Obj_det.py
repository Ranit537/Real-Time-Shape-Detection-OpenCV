import cv2
import numpy as np
from numpy.ma.testutils import approx

frameHight = 540
frameWidth = 380

cap = cv2.VideoCapture(0)
cap.set(3,frameHight)
cap.set(4,frameWidth)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,280)
cv2.createTrackbar("Thresold1","Parameters",4,255,empty)
cv2.createTrackbar("Thresold2","Parameters",30,255,empty)
cv2.createTrackbar("Area","Parameters",5000,30000,empty)


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContuors(img,imgContuors):
    contours , hierachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaa = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaa:
            cv2.drawContours(imgContuors, contours, -1, (255, 0, 255), 7)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgContuors,(x,y),(x+w,y+h),(0,255,0),3)

            cv2.putText(imgContuors, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)
            cv2.putText(imgContuors, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)


while True:
    success , img = cap.read()
    imgContours = img.copy()

    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    thresold1 = cv2.getTrackbarPos("Thresold1","Parameters")
    thresold2 = cv2.getTrackbarPos("Thresold2","Parameters")

    imgCanny = cv2.Canny(imgGray,thresold1,thresold2)
    kernal = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny,kernal,iterations=1)


    getContuors(imgDil,imgContours)
    imgStack = stackImages(0.8, ([img, imgBlur, imgCanny],
                                 [imgDil,imgContours,imgContours]))

    cv2.imshow("WebFeed",imgStack)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break