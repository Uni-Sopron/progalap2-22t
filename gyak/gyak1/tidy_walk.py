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

for (root, folders, files) in os.walk(target):
    for f in files:
        (name, ext) = path.splitext(f)
        out = path.join(output, ext.replace('.', ''))
        if not path.exists(out):
            os.mkdir(path.join(out))
        elif not path.isdir(out):
            print('not a folder', ext.replace('.', ''))
            sys.exit(1)
        os.rename(path.join(root, f), path.join(out, f))


def delete_folder(dir):
    if path.exists(dir) and path.isdir(dir):
        for file in os.listdir(dir):
            if path.isfile(path.join(dir, file)):
                os.remove(path.join(dir, file))
            elif path.isdir(path.join(dir, file)):
                delete_folder(path.join(dir, file))
        os.rmdir(dir)


delete_folder(target)
