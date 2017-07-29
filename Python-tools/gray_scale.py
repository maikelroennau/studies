import cv2
import os


for directory in os.listdir("."):
    if directory[-3:] != ".py":
        print "Processing " + directory
        for filename in os.listdir(directory):
            image = cv2.imread(os.path.join(directory, filename), 0)
            cv2.imwrite(os.path.join(directory, filename), image)
