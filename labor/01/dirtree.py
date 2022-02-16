""" Ez a program képes felderíteni egy könyvtár szerkezetét, és azt exportálni
    egy JSON fájlba. Vagy fordítva, egy JSON fájl alapján létrehozza a benne
    található könyvtárstruktúrát.
    
    Ha parancssori argumentumként egy könyvtárat kap, akkor azt térképezze fel,
    és a könyvtáron belül egy directories.json fájlba exportálja a struktúrát.
    Ha a fájl létezik, írja felül.
    
    Ha nincs megadva argumentum, akkor az aktuális könyvtárból induljon.
    
    Ha egy JSON fájl van megadva argumentumként, akkor az alapján hozza létre a
    könyvtárszerkezetet, a fájl könyvtárán belül. Ne okozzon hibát, ha egy
    létrehozandó könyvtár már létezik.
    
    JSON struktúra:
    Minden könyvtár egy object, amiben a kulcsok az alkönyvtárak nevei.
"""

import json
import os
import sys

def dirtree(path: str) -> dict:
    tree = {}
    for elem in os.listdir(path):
        #print(' ', elem)
        if os.path.isdir(path+'/'+elem):
            #print(elem)
            tree[elem] = dirtree(path+'/'+elem)
    return tree

if __name__ == "__main__":
    print('Running', sys.argv[0])
    path = '.' if len(sys.argv) < 2 else sys.argv[1]
    tree = dirtree(path)
    #print(tree)
    with open(path + '/directories.json', 'w') as f:
        json.dump(tree, f, indent=4)
