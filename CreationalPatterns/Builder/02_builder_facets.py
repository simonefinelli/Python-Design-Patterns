"""
Sometimes we could have an objet that is so complicated to build that we need
more than one builder to do it.
So we need to use several builders which participating in the build up of that
object.
"""


class Person:
    """A big object."""
    def __init__(self):
        print('Creating an instance of Person')
        # address info
        self.street_address = None
        self.postcode = None
        self.city = None
        # employment info
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self) -> str:
        return f'Address: {self.street_address}, {self.postcode}, ' \
               f'{self.city}\n' \
               f'Employed at {self.company_name} as a {self.position} ' \
               f'earning {self.annual_income}\n'


class PersonBuilder:
    """Concrete class."""
    # to not have extra replications
    def __init__(self, person=None):
        if person is None:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonAddressBuilder(PersonBuilder):
    """Builder for personal info."""
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


class PersonJobBuilder(PersonBuilder):
    """Builder for employment info."""
    def __init__(self, person):
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


if __name__ == '__main__':
    pb = PersonBuilder()
    p = pb \
        .lives\
        .at('42 Amazing Road') \
        .in_city('Wonderland') \
        .with_postcode('00001') \
        .works \
        .at('Teahouse') \
        .as_a('Tea Master') \
        .earning(100000000000) \
        .build()
    print(p)
    p2 = PersonBuilder().build()
    print(p2)
