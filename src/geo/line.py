from src.geo.point import Point

class Line(object):
    def __init__(self, a, b):
        assert isinstance(a, Point)
        assert isinstance(b, Point)
        assert a != b # a line cannot be defined by a duplicate point!

        if a.x < b.x or (a.x == b.x and a.y < b.y):
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a

    def __repr__(self):
        return f'<{self.a}, {self.b}>'

    def __eq__(l1, l2):
        if not isinstance(l2, Line):
            return False
        return l1.a == l2.a and l1.b == l2.b

    def __ne__(l1, l2):
        return not l1.__eq__(l2)

    def __hash__(self):
        return hash((self.a, self.b))

    def draw(self, turtle):
        turtle.up()
        turtle.goto(self.a.x, self.a.y)
        turtle.down()
        turtle.goto(self.b.x, self.b.y)
        turtle.up()

    def intersects(l1, l2, ignore_shared_vertex=False):
        # If the set has fewer than 4 points, that means
        # at least two of them were the same point.
        point_set = { l1.a, l1.b, l2.a, l2.b }
        if len(point_set) < 4:
            return not ignore_shared_vertex

        def _ccw(a, b, c):
            return (c.y-a.y) * (b.x-a.x) > (b.y - a.y) * (c.x - a.x)
        return _ccw(l1.a, l2.a, l2.b) != _ccw(l1.b, l2.a, l2.b) and _ccw(l1.a, l1.b, l2.a) != _ccw(l1.a, l1.b, l2.b)


def intersection(line_1, line_2):
    # based on the solution provided on this wikipedia article:
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
    assert isinstance(line_1, Line)
    assert isinstance(line_2, Line)

    interm_a = (line_1.a.x * line_1.b.y) - (line_1.a.y * line_1.b.x)
    interm_b = (line_2.a.x * line_2.b.y) - (line_2.a.y * line_2.b.x)

    interm_c = line_1.a.x - line_1.b.x
    interm_d = line_2.a.x - line_2.b.x
    interm_e = line_1.a.y - line_1.b.y
    interm_f = line_2.a.y - line_2.b.y

    denom = (interm_c * interm_f) - (interm_d * interm_e)
    if denom == 0:
        return None

    return Point(
        ((interm_a * interm_d) - (interm_b * interm_c)) / denom,
        ((interm_a * interm_f) - (interm_b * interm_e)) / denom,
    )

