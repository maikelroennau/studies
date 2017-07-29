import csv 
import sys
import os

filename = open('fer2013new.csv', 'rb')
file = csv.reader(filename)

origin = 'FER'
destination = 'FER+/'
emotions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear', 'contempt', 'unknown', 'NF']

i = 1
for row in file:
    if row[0] == 'Usage':
        continue

    if not os.path.isdir(os.path.join(destination, row[0], emotions[row[1:].index(max(row[1:]))])):
        os.makedirs(os.path.join(destination, row[0], emotions[row[1:].index(max(row[1:]))]))

    origin_path = os.path.join(origin, row[0], "FER_" + str(i) + ".jpg")
    destination_path = os.path.join(destination, row[0], emotions[row[1:].index(max(row[1:]))]) + "/FER_" + str(i) + ".jpg"

    os.rename(origin_path, destination_path)
     
    i += 1

filename.close()
