##### point class and method are given
class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x


def draw_point(p):
    print('.', end='')  # simulate the drawing of the point

##### end given stuff


class Line:
    def __init__(self, start, end):
        self.end = end
        self.start = start


class Rectangle(list):
    """Represented as a list of lines."""

    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter(list):
    """Reuse the given interface (draw_point) to adapt to new interfaces
    (draw_rectangles) building an Adapter."""
    count = 0

    def __init__(self, line):
        super().__init__()
        self.count += 1
        print(f'{self.count}: Generating points for line '
              f'[{line.start.x},{line.start.y}]→'
              f'[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))


def draw_rectangles(rcs):
    print("\n\n--- Drawing Rectangles ---\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)  # reuse old interface


if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw_rectangles(rs)
    draw_rectangles(rs)

    """
    Note
    There is a problem: the problem is that the Adapter actually generates
    temporary objects, because in order to adapt a line to a point we have to
    generate lots of points.
    So, why do we have to keep doing it over and over again? (check the 
    adapter_with_caching to avoid the problem).
    """