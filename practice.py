import cv2
import numpy as np
from cv2 import CascadeClassifier


#img = cv2.imread("Resources/dog.jpg")
#cv2.imshow("Image", img)
#cv2.waitKey(0)

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture("Resources/WhatsApp Video 2023-08-31 at 13.52.32.mp4")

imgGray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,16)

for (x, y, w, h) in faces:
    cv2.rectangle(cap,(x,y),(x+w,y+h),(100,100,100),2)

while True:

    succes,img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break