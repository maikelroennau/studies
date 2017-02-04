import cv2
import numpy as np
import os

for filename in os.listdir("."):
    if not filename.startswith("resizer"):
        image = cv2.imread(filename)

        #height, width, channels = image.shape
        
        # height += h
        # width += w
        # i += 1

	#image = cv2.resize(image, (70, int((float(height) / float(width)) * 80)))

        image = cv2.resize(image, (1134, 1536))

        cv2.imwrite(filename, image)
