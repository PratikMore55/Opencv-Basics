import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[:] = 0,255,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
cv2.rectangle(img,(0,0),(100,200),(255,0,0),cv2.FILLED)
cv2.circle(img,(250,50),30,(0,255,0),cv2.FILLED)

cv2.putText(img,"OPENCV", (300,100), cv2.FONT_HERSHEY_SIMPLEX,1, (140,0,140),3)

cv2.imshow("Image", img)


cv2.waitKey(0)