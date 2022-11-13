"""
Implement the Builder design pattern for rendering simple custom Classes.
"""


class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return 'self.%s = %s' % (self.name, self.value)


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = ['class %s:' % self.name]
        if not self.fields:
            lines.append('  pass')
        else:
            lines.append('  def __init__(self):')
            for f in self.fields:
                lines.append('    %s' % f)
        return '\n'.join(lines)


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, name, initialization):
        self.__class.fields.append(Field(name, initialization))
        return self

    def __str__(self):
        return self.__class.__str__()


cb = CodeBuilder('Person')\
    .add_field('name', 'Gandalf')\
    .add_field('age', 1000)

print(cb)
