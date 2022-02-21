# usage = []

# for i in range(12):
#     usage.append({"minutes": 0, "messages": 0})

# for i in range(12):
#     usage[i]['minutes'] = int(input('Mennyi perc? '))
#     usage[i]['messages'] = int(input('Mennyi sms? '))

########

# usage = []


# class Usage:
#     minutes = 0
#     messages = 0


# for i in range(12):
#     usage.append(Usage())

# for i in range(12):
#     usage[i].minutes = int(input('Mennyi perc? '))
#     usage[i].messages = int(input('Mennyi sms? '))


########

usages = []


class Usage:
    minutes = 0
    messages = 0
    data = 0

    def input(self):
        self.minutes = int(input('Mennyi perc? '))
        self.messages = int(input('Mennyi sms? '))
        self.data = int(input('Mennyi Mb? '))


class Tariff:
    _base_price = 0
    _minute_cost = 0
    _message_cost = 0
    _data_cost = 0
    _name = ""

    # def __init__(self):
    #     self.input()

    def __str__(self):
        return f"Tariff ({self._name}) basic cost is {self._base_price}"

    def __init__(self, name, base_price, minute_cost, message_cost, data_cost):
        self._name = name
        self._base_price = base_price
        self._minute_cost = minute_cost
        self._message_cost = message_cost
        self._data_cost = data_cost
        self._users = []

    def input(self):
        self._base_price = int(input('Mennyi az alap? '))
        self._minute_cost = int(input('Mennyi 1 perc? '))
        self._message_cost = int(input('Mennyi 1 sms? '))
        self._data_cost = int(input('Mennyi 1 Mb? '))

    def payment(self, usage):
        cost = usage.messages * self._message_cost + usage.minutes * \
            self._minute_cost + usage.data * self._data_cost
        if cost < self._base_price:
            cost = self._base_price
        return cost


january = Usage()
tariff = Tariff("Egyik", 20, 1, 1, 1)
print(tariff)
tariff2 = Tariff("Másik", 10, 1, 1, 1)
print(tariff2)
