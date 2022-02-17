import os
from os import path
import sys

target = 'sample' if len(sys.argv) < 2 else sys.argv[1]
output = 'sorted' if len(sys.argv) < 3 else sys.argv[2]

if not path.exists(target) or not path.isdir(target):
    print('not a folder')
    sys.exit()

if not path.exists(output):
    os.mkdir(output)

cwd = os.getcwd()

for file in os.scandir(target):
    print(file.name, file.is_dir(), file.is_file())
