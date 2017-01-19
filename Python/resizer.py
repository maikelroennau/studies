import cv2
import numpy

i = 0

for i in range(0):
    image = cv2.imread(str(i) + ".jpg")

    height, width, channels = image.shape

    image = cv2.resize(image, (70, int((float(height) / float(width)) * 80)))

    cv2.imwrite(str(i) + ".jpg", image)
