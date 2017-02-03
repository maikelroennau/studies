import os

i = 0
for filename in os.listdir("."):
    if not os.path.splitext(filename)[1] == ".py" and not os.path.splitext(filename)[1] == ".jpg": 
        os.system("convert " + filename + " " + os.path.splitext(filename)[0] + ".jpg")
        os.system("rm " + filename)
        i += 1
