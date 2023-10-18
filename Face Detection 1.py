import cv2
import numpy as np
from cv2 import CascadeClassifier

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/Screenshot 2023-08-31 001152.png")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,16)

for (x, y, w, h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(100,100,100),2)

cv2.imshow("Image", img)
cv2.waitKey(0)