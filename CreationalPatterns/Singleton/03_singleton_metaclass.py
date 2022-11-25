"""
Last way to implement a Singleton is to use metaclass which is going to
have a similar implementation as the decorator.

TIP: this is the best way to make a Singleton in Python.
"""
class Singleton(type):
    """Metaclass that creates a Singleton base type when called."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args,
                                                                 **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
