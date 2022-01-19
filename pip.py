import os 
import sys

print(str(sys.argv))
print(os.system("pip3 install {}".format(sys.argv[1])))
