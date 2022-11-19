"""
Use the abstract Factory to implement a vending machine.
"""
from abc import ABC
from enum import Enum, auto


# interface
class HotDrink(ABC):
    def consume(self):  # consume the drink
        pass


# concrete implementation
class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk.')


# concrete implementation
class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious.')


###### hierarchy of factories ######
# interface
class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


# concrete implementation
class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


# concrete implementation
class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind some beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()
###### end hierarchy of factories ######


# use above elements to make a drink
class HotDrinkMachine:
    class AvailableDrink(Enum):  # violates OCP if we want to add a new drink, but ok in this case
        COFFEE = auto()
        TEA = auto()

    factories = []  # each element for a kind of drink
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for i, f in enumerate(self.factories):
            print(f'{i} - {f[0]}')

        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input(f'Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
