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


def copy(source, to):
    command = f'cp {source} {to}' if os.name == 'posix' else f'copy {source} {to}'
    os.system(command)


for (root, folders, files) in os.walk(target):
    for f in files:
        (name, ext) = path.splitext(f)
        out = path.join(output, ext.replace('.', ''))
        if not path.exists(out):
            os.mkdir(path.join(out))
        elif not path.isdir(out):
            print('not a folder', ext.replace('.', ''))
            sys.exit(1)
        copy(path.join(root, f), path.join(out, f))
