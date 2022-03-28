import functools
from random import random


def addX(n):
    return lambda num: num + n


add5 = addX(5)
add3 = addX(3)

print(add5(4))
print(add3(4))


def increase(n, i):
    return n + i


i3 = functools.partial(increase, i=3)

print(i3(4))


def fun(x, fn): return x + fn(x)


print(fun(2, lambda x: x**2))


class Car:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Car:{self.name}, {self.age}'


c1 = Car('a', 10)
c2 = Car('b', 8)

l = [c1, c2]
l.sort(key=lambda x: x.age)
print(l)
l2 = sorted(l, key=lambda x: x.name)
print(l2)
print(l)

# filter
l = [-1, 3, 5, 1, 2]
print(list(filter(lambda x: x > 0 and x % 2 == 0, l)))
print(sorted(list(filter(lambda x: x > 0, l))))


# map
l = [1, 2, 3, 4]
print(list(map(lambda x: str(x ** 2) + ' lett az új eredeti: ' + str(x), l)))
todos = ['kenyér', 'tej', 'vaj']
print('<ul>', list(map(lambda todo: '<li>' + todo + '</li>', todos)), '</ul>')

# reduce
l = [1, 2, 3]
sum = functools.reduce(lambda prev, curr: prev + curr, l, 10)

l2 = [{'value': 1, "id": random()}, {'value': 2, "id": random()}, {
    'value': 3, "id": random()}]

sum = functools.reduce(lambda prev, curr: prev + curr['value'], l2, 0)

print(sum)


todos = [{"id": 0, "value": "kenyér"}, {
    "id": 1, "value": "tej"}, {"id": 2, "value": "vaj"}]

newList = list(
    map(lambda id: {"id": random(), "value": todos[id]["value"]}, range(len(todos))))

print(newList)

stuff = {'1': {'value': 'asd'}, '2': {'value': 'basd'}}
# ['asd', 'basd']

# TODO: get value from stuff object
print(list(map(lambda x: x, stuff.keys())))
