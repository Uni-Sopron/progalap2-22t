import sys
import os
import os.path
import matplotlib.pyplot as plt

def dirsize(path: str) -> int:
    total = 0
    for elem in os.listdir(path):
        if not os.path.isdir(path+'/'+elem):
            total += os.path.getsize(path+'/'+elem)
        else:
            total += dirsize(path+'/'+elem)
    return total

def dirsize2(path: str) ->int:
    total = 0
    for dirpath, dirs, files in os.walk(path):
        for f in files:
            total += os.path.getsize(dirpath+'/'+f)
    return total

def plotsizes(path: str) -> None:
    # make data:
    x = [elem for elem in os.listdir(path)]
    y = []
    for elem in os.listdir(path):
        if os.path.isdir(path+'/'+elem):
            y.append(dirsize(path+'/'+elem))
        else:
            y += [os.path.getsize(path+'/'+elem)]

    # plot
    fig, ax = plt.subplots()
    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)
    plt.show()

if __name__ == '__main__':
    path = '.' if len(sys.argv) < 2 else sys.argv[1]
    print('size of', path, end=': ')
    print(dirsize(path))
    plotsizes(path)