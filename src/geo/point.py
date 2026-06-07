import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(p1, p2):
        if not isinstance(p2, Point):
            return False
        return p1.x == p2.x and p1.y == p2.y

    def __ne__(p1, p2):
        return not p1.__eq__(p2)

    def __add__(p1, p2):
        assert isinstance(p2, Point)
        return Point(
            p1.x + p2.x,
            p1.y + p2.y,
        )

    def __sub__(p1, p2):
        assert isinstance(p2, Point)
        return Point(
            p1.x - p2.x,
            p1.y - p2.y,
        )

    def draw(self, turtle):
        turtle.up()
        turtle.goto(self.x, self.y)
        turtle.down()
        turtle.circle(3)
        turtle.up()

    @staticmethod
    def scale(p, c):
        assert isinstance(p, Point)
        assert isinstance(c, (int, float, complex))
        return Point(
            p.x * c,
            p.y * c,
        )

    @staticmethod
    def dist(p1, p2):
        assert isinstance(p1, Point)
        assert isinstance(p2, Point)

        return math.sqrt(\
            (p1.x - p2.x)**2 +\
            (p1.y - p2.y)**2\
        )

