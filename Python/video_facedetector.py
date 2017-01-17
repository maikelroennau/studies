import cv2

cap = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(cascPath)

def detect(image):
    faces = faceCascade.detectMultiScale(
        image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

while(True):
    rect, image = cap.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces, image = detect(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Faces found" ,image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
