class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.animals = []

    def adopt(self, animal):
        self.animals.append(animal)
        animal._adopt(self)

    def __str__(self):
        return f'My name is {self.name} and i have {len(self.animals)} animals: {self.animals}'


class Animal:
    def speak(self):
        return '*voice*'

    def __init__(self, name):
        self.name = name

    def _adopt(self, owner):
        self.owner = owner

    def __str__(self):
        return f'My name is {self.name} my owner is {self.owner.name} ({self.speak()})'

    def __repr__(self):
        return self.name


class Cat(Animal):
    def speak(self):
        return 'miau'


class OwnedCat(Cat):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner
        owner.adopt(self)

    def speak(self):
        return 'miaaaaau'


class Dog(Animal):
    def speak(self):
        return 'vau'

    def dig(self):
        print('i am digging a hole')


pisti = Person('Pisti', 12)
cat = Cat('Cat')
dog = Dog('Dog')
pisti.adopt(cat)
pisti.adopt(dog)
cat2 = OwnedCat('Cat 2', pisti)

for pet in pisti.animals:
    print(pet)
print(pisti)

dog.dig()
