import copy


class Address:
    def __init__(self, street_address, city, country):
        self.country = country
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'


address = Address("123 London Road", "London", "UK")
john = Person("John", address)

# jane = Person("Jane", address)
# jane.address.street_address = '321 Paris Road'  # still problems because
#                                                 # John's address info will
#                                                 # change!

jane = copy.deepcopy(john)  # to 'clone' an exiting object. Deepcopy recursively
                            # copy all of the attributes of an object into a new
                            # object that does not refere to the original
jane.name = "Jane"
jane.address.street_address = '321 Paris Road'
print(john)
print(jane)

# TIP: exists a copy() function that performs a shallow copy. If we use in our
# example, the name will change but the address not!
