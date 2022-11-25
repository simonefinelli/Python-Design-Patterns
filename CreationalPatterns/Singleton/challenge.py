"""
Write a function called is_singleton(). This method takes a factory method that
returns an object, and it's up to you to determine whether that object is a
singleton instance.
"""
from copy import deepcopy


def is_singleton(factory):
    x = factory()
    y = factory()
    return x is y


if __name__ == '__main__':
    l = [42] * 10
    print(is_singleton(lambda: l))  # we can se a lambda expression as a Factory
    print(is_singleton(lambda: deepcopy(l)))
