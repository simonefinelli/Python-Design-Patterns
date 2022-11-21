"""
It is quite often inconvenient to keep making object copies manually as we have
done in the prototype.py. I would be nice to package them into a factory, in
order to isolate the deep copy and the customization of the object.

"""
import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.suite = suite
        self.city = city
        self.street_address = street_address

    def __str__(self):
        return f'{self.street_address}, Suite #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", 0, "London"))  # prototype
    aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))  # prototype

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name, suite
        )


john = EmployeeFactory.new_main_office_employee("John", 42)
jane = EmployeeFactory.new_aux_office_employee("Jane", 242)
print(john)
print(jane)

