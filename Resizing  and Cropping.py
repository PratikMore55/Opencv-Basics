import cv2
import numpy as np

img = cv2.imread("Resources/dog.jpg")
print(img.shape)

imgResize = cv2.resize(img, (1000,500))
print(imgResize.shape)

imgCropped = img[0:200,50:500]

cv2.imshow("DOG", img)
cv2.imshow("Resize Image", imgResize)
cv2.imshow("Cropped image", imgCropped)

cv2.waitKey(0)