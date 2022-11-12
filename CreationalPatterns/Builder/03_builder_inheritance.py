"""
In the builder_facets we can notice that combining the 2 builder we directly
violate the open closed principle: whenever we have a new sub-builder we have to
add it to the builder.

There is an alternative approach using inheritance to avoid that.
"""


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'Name: {self.name} Position: {self.position} ' \
               f'Birth: {self.date_of_birth}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


# add works_as_a without modify only Person class
class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


# add works_as_a without modify only Person class
class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


# add works_as_a without modify only Person class
class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    p = pb\
        .called('Frodo')\
        .works_as_a('traveler')\
        .born('1/1/1970')\
        .build()  # this does NOT work in C#/C++/Java/...

    print(p)
