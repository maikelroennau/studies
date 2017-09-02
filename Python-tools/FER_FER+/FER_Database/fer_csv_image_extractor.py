import os
import sys
import csv
import numpy as np
import cv2
from PIL import Image


filename = open('fer2013.csv', 'rb')
file = csv.reader(filename)

location = 'FER'

i = 1
for row in file:
    if row[0] == 'emotion':
        continue

    image = np.fromstring(row[1], dtype=int, sep=' ').reshape(48, 48)

    if not os.path.isdir(os.path.join(location, row[2])):
        os.makedirs(os.path.join(location, row[2]))
        print(os.path.join(location, row[2]))

    cv2.imwrite(os.path.join(location, row[2]) + '/FER_' + str(i) + '.jpg', image)

    i += 1

filename.close()
