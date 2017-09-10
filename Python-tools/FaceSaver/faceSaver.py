import numpy as np
import os
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for directory in os.listdir("."):
    if directory[-3:] != ".py" and directory[-4:] != ".xml":
	print 'Processing {}'.format(directory)
        images = os.listdir(directory)

        for img in images:
            image = cv2.imread(os.path.join(directory, img))
            faces = faceCascade.detectMultiScale(
                image,
                scaleFactor=1.5,
                minNeighbors=5,
                minSize=(30, 30),
                flags = 0
            )

            for (x, y, w, h) in faces:
                face = image[y: y + h, x: x + w]
                cv2.imwrite(os.path.join(directory, img), face)
                break
            else:
                os.remove(os.path.join(directory, img))
