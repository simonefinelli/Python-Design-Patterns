"""
This example is the same as in the 01_factory.py, but in this case we have
extrapolated the Factory.
"""
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


class PointFactory:
    """Factory"""
    @staticmethod
    def new_cartesian_point(x, y):
        """Factory Method"""
        return Point(x, y)

    # a specific object
    @staticmethod
    def new_polar_point(rho, theta):
        """Factory Method"""
        return Point(rho * sin(theta), rho * cos(theta))

    # TIP: in the factory pattern each Factory method creates an object!


if __name__ == '__main__':

    p1 = PointFactory.new_cartesian_point(1, 2)
    p2 = PointFactory.new_polar_point(1, 2)
    print(p1, p2)
