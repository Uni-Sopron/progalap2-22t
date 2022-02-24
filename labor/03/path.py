from typing import *

class Coord:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def dist_from(self, other: 'Coord') -> float:
        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5
    
    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

def distance(a: Coord, b: Coord) -> float:
    return a.dist_from(b)

class Path:
    def __init__(self) -> None:
        self.coords: List[Coord] = []
        self.length = 0.0
        self.changed = False

    def add(self, coord: Coord) -> None:
        #if self.coords:
        #    self.length += coord.dist_from(self.coords[-1])
        self.changed = True
        self.coords.append(coord)
        
    def get_length(self) -> float:
        if not self.changed:
            return self.length
        #return self.length
        total = 0.0
        for i in range(1,len(self.coords)):
            a = self.coords[i]
            b = self.coords[i-1]
            total += a.dist_from(b)
        self.length = total
        self.changed = False
        return total
    
    def print(self):
        for c in self.coords:
            #print(f'({c.x}, {c.y})')
            print(c)
            
    def __str__(self) -> str:
        #output = ''
        #for c in self.coords:
        #    output += str(c) + ' '
        #return output
        return ', '.join([str(c) for c in self.coords])

if __name__ == '__main__':
    p = Path()
    c = Coord(0,0)
    print(c.x, c.y)
    p.add(c)
    c = Coord(4,3)
    p.add(c)
    print(p.get_length())
    c = Coord(5,5)
    p.add(c)
    print(p.get_length())
    #p.print()
    print(p)
