import cv2
import numpy as np
from cv2 import CascadeClassifier

# img = cv2.imread("Resources/img_1.png")
# cv2.imshow("IMAGE", img)
# cv2.waitKey(0)

# vid = cv2.VideoCapture("Resources/WhatsApp Video 2023-08-31 at 13.52.32.mp4")
# while True:
#     success,img = vid.read()
#     cv2.imshow("Video", img)
#
#     if cv2.waitKey(1) & 0xFF ==ord('p'):
#         break




#img = cv2.imread("Resources/dog.jpg")
#cv2.imshow("Image", img)
#cv2.waitKey(0)

# faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
# cap = cv2.VideoCapture("Resources/WhatsApp Video 2023-08-31 at 13.52.32.mp4")
#
# imgGray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray,1.1,16)
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(cap,(x,y),(x+w,y+h),(100,100,100),2)
#
# while True:
#
#     succes,img = cap.read()
#     cv2.imshow("Video", img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#
#         break

# img = cv2.imread("Resources/dog.jpg")
# cv2.line(img, (0,50),(0,100), (0,0,255), thickness=5, lineType=cv2.LINE_AA)
# cv2.circle(img, (50,50), radius=10, color=(255,0,255), thickness=5, lineType=cv2.LINE_AA)
# cv2.rectangle(img, (20,30), (50,10), color=(255,255,0), thickness=-3, lineType=cv2.LINE_AA)
# cv2.imshow("Image" ,img)
# imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("Gray Image", imGray)
# cv2.imshow("Pata nahi", imgBlur)
# cv2.waitKey(0)

# img = cv2.imread("Resources/416156.jpg")
#
# matrix1 = np.ones(img) * .8
# matrix2 = np.ones(img) * 1.2
#
# cv2.imshow("Lower Contrast", matrix1)
# cv2.imshow("Higher Contrast", matrix2)q
#
# cv2.imshow("Original", img)
# cv2.waitKey(0)