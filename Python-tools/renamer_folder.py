import os

i = 1

for filename in os.listdir("."):
    if not filename.startswith("rename"):
        os.rename(filename, os.path.split(os.getcwd())[1] + "_" + str(i) + os.path.splitext(filename)[1])
        i += 1
