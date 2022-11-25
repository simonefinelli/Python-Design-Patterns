"""
One way to avoid the problem with constructors showed in 01_singleton_allocator
is to use a different approach to implementing a singleton.
In particular, here we build a Singleton using a decorator.
"""


def singleton(class_):
    """Singleton as decorator."""
    instances = {}  # every class instance is kept in a dictionary

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print('Loading database')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)

    # now the initializer is called only one time, in fact, we have  a single
    # print of 'Loading database'
