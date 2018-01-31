from src.geo.point import Point

class Line(object):
    def __init__(self, a, b):
        assert isinstance(a, Point)
        assert isinstance(b, Point)
        assert a != b # a line cannot be defined by a duplicate point!

        self.a = a
        self.b = b

    def __repr__(self):
        return f'<{self.a}, {self.b}>'


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

