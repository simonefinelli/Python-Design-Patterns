##### point class and method are given
class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x


def draw_point(p):
    print('.', end='')

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


class LineToPointAdapter:
    # to avoid excess generation of temporary information we use a cache.
    # Also, using the cache, we got rid of List inheritance of
    # LineToPointAdapter class.
    cache = {}

    def __init__(self, line):
        self.h = hash(line)  # calculate the hash code of a particular line
        if self.h in self.cache:  # check if the line is already processed
            return

        super().__init__()
        print(f'Generating points for line ' +
              f'[{line.start.x},{line.start.y}]→[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []
        if right - left == 0:
            for y in range(top, bottom):
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                points.append(Point(x, top))

        self.cache[self.h] = points

    # the class did not inherit from List, so we have to override __iter__
    # to iterate on cache dict
    def __iter__(self):
        return iter(self.cache[self.h])


def draw_rectangles(rcs):
    print("\n\n--- Drawing Rectangles ---\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
    print('\n')


if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    draw_rectangles(rs)
    draw_rectangles(rs)
