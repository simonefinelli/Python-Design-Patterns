from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * sin(b)
    #         self.y = a * cos(b)
    #
    #     # if we want to add a new system:
    #     # 1. write the new system in CoordinateSystem class
    #     # 2. update the constructor
    #     # but this breaks the open-close principle!!!

    # to avoid above situation we can use factory pattern

    class Factory:
        """Factory"""
        def new_cartesian_point(self, x, y):
            """Factory Method"""
            return Point(x, y)

        # a specific object
        def new_polar_point(self, rho, theta):
            """Factory Method"""
            return Point(rho * sin(theta), rho * cos(theta))

        # TIP: in the factory pattern each Factory method creates an object!

    factory = Factory()


if __name__ == '__main__':
    p1 = Point.factory.new_cartesian_point(1, 2)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p1, p2)
