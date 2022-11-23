import random


class Database:
    initialized = False

    def __init__(self):
        self.id = random.randint(0, 1000)
        print('Generated an id of ', self.id)
        print('Loading database from file...')

    _instance = None

    # use the allocator to check if the instance is already created
    # this approach is good if we don't have any code in the initializer.
    # in fact in this case objects in the initializers will be instantiated more
    # than one.
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
                .__new__(cls, *args, **kwargs)

        return cls._instance


database = Database()

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()

    print(d1.id, d2.id)
    print(d1 == d2)
    print(database == d1)