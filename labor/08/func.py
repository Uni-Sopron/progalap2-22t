numbers = [x for x in range(10)]
mapped = list(map(lambda x: x % 3, numbers))
for i in range(len(numbers)):
    numbers[i] = 0
numbers = [1 for _ in range(10)]
for x in mapped:
    print(x, end=' ')

for x in mapped:
    print(x)