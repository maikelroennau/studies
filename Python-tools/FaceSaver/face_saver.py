import numpy as np
import os
import cv2
from multiprocessing import Process

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

def process_directory(directory):
    print 'Processing {}: started'.format(directory)
    images = os.listdir(directory)

    for img in images:
        image = cv2.imread(os.path.join(directory, img))
        faces = faceCascade.detectMultiScale(
            image,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(16, 16),
            flags = 0
        )

        for (x, y, w, h) in faces:
            y = int(y * 1.0)
            x = int(x * 1.0)
            face = image[ y: y + int(h * 1.0), x: x + int(w * 1.0) ]
            cv2.imwrite(os.path.join(directory, img), face)
            break
        else:
            os.remove(os.path.join(directory, img))

    print 'Processing {}: done'.format(directory)


for directory in os.listdir("."):
    if directory[-3:] != ".py" and directory[-4:] != ".xml" and directory[-4:] != ".png":
        process = Process(target=process_directory, args=(directory,))
        process.start()
