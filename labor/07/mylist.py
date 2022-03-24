import random

def fill_with_random_numbers(numbers, min, max, count):
    for _ in range(count):
        numbers.append(random.randint(min, max))

class MyList(list):
    def remove_all(self, value):
        #print('length:', len(self))
        #count = self.count(value)
        #for _ in range(count):
        #    self.remove(value)
        i = 0
        while i < len(self):
            if self[i] == value:
                self.pop(i)
            else:
                i += 1

class SortedList(MyList):
    def __init__(self, *args):
        super().__init__(*args)
        self.sort()
    
    def append(self, __object) -> None:
        super().append(__object)
        self.sort()
        
class LoggedList(SortedList):
    def append(self, __object):
        print(__object, " appended")
        super().append(__object)

    def __add__(self, x) -> "LoggedList":
        newlist = LoggedList()
        newlist += self
        newlist += x
        return newlist

my = [1, 2, 3, 1]
my = LoggedList(my)
print(my)
#my = LoggedList()
my.append(1)
my.append(2)
my.append(3)
my.append(1)
my.append(1)
print(my)
my.remove_all(1)
print(my)

#my += [9, 8, 7, 9, 9]
my = my + [9, 8, 7, 9, 9]
my.remove_all(9)
print(my)
