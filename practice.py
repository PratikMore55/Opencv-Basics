import cv2


#img = cv2.imread("Resources/dog.jpg")
#cv2.imshow("Image", img)
#cv2.waitKey(0)

cap = cv2.VideoCapture("Resources/WhatsApp Video 2023-08-31 at 13.52.32.mp4")
while True:

    succes,img = cap.read()
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break