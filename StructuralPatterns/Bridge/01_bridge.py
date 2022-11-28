"""
Suppose we have a drawing application that can drawing a different kind of
shapes (circles and squares). Each can be rendered in vector or raster form.
So we can have VectorCircle, VectorSquare, RasterCircle and RasterSquare
("Cartesian product" complexity), so the approach don't scale.

So to the concepts of shapes and renders can be split, but we have to make a
connection between them with the Bridge design patter.
"""
from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    # render_square, etc. (breaking the open-close principle,
    #                      but here it is not much that we can do)


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')


class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer  # core of the bridge design: connect an
                                  # hierarchy with another

    def draw(self): pass
    def resize(self, factor): pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(raster, 5)
    # circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
