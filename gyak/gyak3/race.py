# class Dog:
#     lab = 4
#     name = ""

#     def __init__(self, name):
#         self.name = name
#         self.tricks = []

#     def add_trick(self, trick):
#         self.tricks.append(trick)


# fido = Dog('Fido')
# buddy = Dog('Buddy')

# print(fido.tricks)
# print(buddy.tricks)
# fido.add_trick('pacsi')
# buddy.add_trick('ül')
# print(fido.tricks)
# print(buddy.tricks)


#####

class Vehicle:
    tank_size = 10

    def __init__(self, brand, model, year, type):
        self.brand = brand
        self.model = model
        self.year = year
        self.type = type
        self.tank = 0

    def drive(self):
        if self.tank == 0:
            print('üres a tank')
        else:
            self.tank -= 1
            print(f"Driving {self.brand}")

    def fuel_up(self, amount, petrol):
        if not petrol.type == self.type:
            print('ez nem megy bele')
        else:
            if self.tank + amount > self.tank_size:
                print('nem fér bele')
            else:
                self.tank += amount
                print(f'ez most {petrol.price * amount}ft volt')

    def fill_up(self, petrol):
        amount = self.tank_size - self.tank
        self.fuel_up(amount, petrol)

    def upgrade(self, amount):
        self.tank_size = amount


class Petrol:
    def __init__(self, type, price):
        self.type = type
        self.price = price


class Race:
    def __init__(self, car1, car2, laps):
        self.car1 = car1
        self.car2 = car2
        self.laps = laps

    def race(self):
        petrolType = Petrol('petrol', 0)
        electricType = Petrol('electric', 0)

        self.car1.fill_up(petrolType)
        self.car2.fill_up(electricType)
        for lap in range(0, self.laps):
            self.car1.drive()
            self.car2.drive()
            if self.car1.tank == 0:
                print(self.car2.brand, ' nyert')
                break
            if self.car2.tank == 0:
                print(self.car1.brand, ' nyert')
                break


ferrari = Vehicle('Ferrari', "California", 1994, "petrol")
tesla = Vehicle('Tesla', "Y", 2018, "electric")

# petrolType = Petrol('petrol', 479.9)
# electricType = Petrol('electric', 79.9)

# ferrari.fuel_up(9, petrolType)
# ferrari.drive()
tesla.upgrade(11)
# tesla.fuel_up(10, electricType)
# tesla.drive()

race = Race(ferrari, tesla, 10)
race.race()
