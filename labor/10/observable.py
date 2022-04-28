
class Observable:
    def __init__(self) -> None:
        self.__value = None
        self.__functions = set()
    
    def get(self):
        return self.__value

    def set(self, val) -> None:
        self.__value = val
        for f in self.__functions:
            f(self.__value)

    def add_trace(self, func):
        self.__functions.add(func)


number = Observable()
number.add_trace(print)
number.add_trace(print)
number.add_trace(lambda x: print(f'The new value of the variable is {x}'))
number.set(42)
number.set(23)
