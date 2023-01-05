"""
We have two classes called SingleValue and ManyValues. SingleValue stores just
one numeric value, but ManyValues can store either numeric values or
SingleValue objects.

You are asked to give both SingleValue and ManyValues a property member called
sum that returns a sum of all the values that the object contains. Please ensure
that there is only a single method that realizes the property sum, not multiple
methods.
"""


class SingleValue:
    def __init__(self, value):
        self.value = value


class ManyValues(list):

    def __init__(self):
        super().__init__()
        self._sum = 0

    @property
    def sum(self):
        return self._sum

