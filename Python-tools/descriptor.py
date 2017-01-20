import os
import sys

folder_path = sys.argv[1]

print "ls -d -v1 " + folder_path + "/*.* >> " + folder_path + ".txt"
