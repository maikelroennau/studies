import numpy as np
import os
import cv2

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

folders = ['happy', 'angry', 'surprise', 'fear', 'neutral', 'sad', 'disgust']

if not os.path.exists('unfaced'):
    os.makedirs('unfaced')

    for folder in folders:
        os.makedirs('{}/{}'.format('unfaced', folder))

destinations = {}

for directory in os.listdir("."):
    if directory[-3:] != ".py" and directory[-4:] != ".xml" and directory != 'unfaced':
	print 'Processing {}'.format(directory)
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

            if len(faces) == 0:
                os.rename(os.path.join(directory, img), os.path.join('unfaced', directory, img))
                
                if destinations.has_key(directory):
                    destinations[directory] = destinations[directory] + 1
                else:
                    destinations[directory] = 1

print '\nMoved images:'

for key in destinations.keys():
    print '{:>10}:  \t{}'.format(key, destinations[key])
