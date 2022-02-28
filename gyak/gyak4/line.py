class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def len(self):
        import math
        len = math.sqrt((self.p2.x - self.p1.x)**2 +
                        (self.p2.y - self.p1.y) ** 2)
        return len

    def __sub__(self, other):
        p1 = Point(self.p1.x - other.p1.x, self.p1.y - other.p1.y)
        p2 = Point(self.p2.x - other.p2.x, self.p2.y - other.p2.y)
        return Line(p1, p2)


p1 = Point(0, 0)
p2 = Point(1, 1)

l = Line(p1, p2)

p3 = Point(0, 0)
p4 = Point(3, 3)

l2 = Line(p3, p4)

print(l.len())
print((l2-l).len())
