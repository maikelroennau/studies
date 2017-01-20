import os
import sys

folder_path = sys.argv[1]

os.system("ls -d -v1 " + folder_path + "/*.* >> " + folder_path + ".txt")

print "File saved to under the name " + folder_path + ".txt"
