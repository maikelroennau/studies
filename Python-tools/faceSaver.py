import numpy as np
import cv2

facesFound = 0

imagePath = "1.jpg"
cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

for (x, y, w, h) in faces:
    face = image[y: y + h, x: x + w]
    cv2.imwrite(str(facesFound) + ".jpg", face)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow("Faces found" ,image)
cv2.waitKey(0)