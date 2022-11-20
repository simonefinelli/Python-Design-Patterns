"""
You are given a class called Person. The person has two attributes: id and name.

Please implement a PersonFactory that has a non-static create_person() method
that takes a person's name and return a person initialized with this name and
an id.

The id of the person should be set as a 0-based index of the object created.
So, the first person the factory makes should have Id=0, second Id=1 and so on.
"""


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id:0>5} - {self.name}'


class PersonFactory:
    progressive_id = 0

    def create_person(self, name):
        # normally this method should be static, but now we have the progressive
        # number
        p = Person(self.progressive_id, name)
        self.progressive_id += 1
        return p


if __name__ == '__main__':
    factory = PersonFactory()
    hero1 = factory.create_person('Gandalf')
    hero2 = factory.create_person('Frodo')
    print(hero1)
    print(hero2)


