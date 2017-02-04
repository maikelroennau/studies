import os

i = 0

for filename in os.listdir("."):
    if not filename.startswith("rename"):
        os.rename(filename, str(i) + os.path.splitext(filename)[1])
        i += 1
