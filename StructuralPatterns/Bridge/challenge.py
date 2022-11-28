"""
You are given an example of an inheritance hierarchy which results in
Cartesian-product duplication.

Please refactor this hierarchy, giving the base class Shape a constructor that
takes an interface Renderer defined as

    class Renderer(ABC):
        @property
        def what_to_render_as(self):
            return None

as well as VectorRenderer and RasterRenderer classes. Each inheritor of the
Shape abstract class should have a constructor that takes a Renderer such that,
subsequently, each constructed object's __str__()  operates correctly.
For example, str(Triangle(RasterRenderer())  # returns "Drawing Triangle as
pixels".
"""

##### GIVEN CODE
#
# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'
#
# imagine VectorTriangle and RasterTriangle are here too
#
##### END GIVEN CODE

from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixel'


class Shape(ABC):
    def __init__(self, renderer, name):
        self.name = name
        self.renderer = renderer

    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}."


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')


if __name__ == '__main__':
    sq = Square(VectorRenderer())
    print(sq)
    tr = Triangle(RasterRenderer())
    print(tr)
