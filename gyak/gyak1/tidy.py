import os
from os import path
import sys

target = 'sample' if len(sys.argv) < 2 else sys.argv[1]
output = 'sorted' if len(sys.argv) < 3 else sys.argv[2]

if not path.exists(target) or not path.isdir(target):
    print('not a folder')
    sys.exit()

filetypes = []

cwd = os.getcwd()


def get_filetypes(dir):
    for file in os.listdir(dir):
        if path.isfile(path.join(dir, file)):
            (name, ext) = path.splitext(file)
            if ext.replace('.', '') not in filetypes:
                filetypes.append(ext.replace('.', ''))
        elif path.isdir(path.join(dir, file)):
            get_filetypes(path.join(dir, file))


get_filetypes(path.join(cwd, target))

if not path.exists(path.join(cwd, output)):
    os.mkdir(output)

for ext in filetypes:
    if not path.exists(path.join(output, ext)) and len(ext) > 0:
        os.mkdir(path.join(output, ext))


def move_files(dir):
    for file in os.listdir(dir):
        if path.isfile(path.join(dir, file)):
            (name, ext) = path.splitext(file)
            os.rename(path.join(dir, file), path.join(
                cwd, output, ext.replace('.', ''), file))
        elif path.isdir(path.join(dir, file)):
            move_files(path.join(dir, file))


move_files(path.join(cwd, target))


def delete_folder(dir):
    if path.exists(dir) and path.isdir(dir):
        for file in os.listdir(dir):
            if path.isfile(path.join(dir, file)):
                os.remove(path.join(dir, file))
            elif path.isdir(path.join(dir, file)):
                delete_folder(path.join(dir, file))
        os.rmdir(dir)


delete_folder(target)
