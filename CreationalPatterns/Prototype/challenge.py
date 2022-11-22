"""
Given the definitions shown in code, you are asked to implement Line.deep_copy()
to perform a deep copy of the given Line object. This method should return
a copy of a Line that contains copies of its start/end points.
"""
import copy


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"Line: [({self.start.x},{self.start.y}), " \
               f"({self.end.x},{self.end.y})])"


if __name__ == '__main__':
    l1 = Line(Point(0, 1), Point(0, 1))
    l2 = l1.deep_copy()
    l2.end = Point(42, 42)

    print(l1)
    print(l2)