import os

i = 0
for filename in os.listdir("."):
    os.system("convert " + str(i) + ".pgm " + str(i) + ".jpg")
    i += 1
