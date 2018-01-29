# coding=utf-8

from src.geo.utils import Point
from src.geo.line import Line
from src.geo import line


class Triangle(object):
    def __init__(self, a, b, c):
        assert isinstance(a, Point)
        assert isinstance(b, Point)
        assert isinstance(c, Point)

        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f'∆<{self.a}, {self.b}, {self.c}'


def circumcenter(triangle):
    assert isinstance(triangle, Triangle)

    # translate to origin
    t_a = triangle.a - triangle.c
    t_b = triangle.b - triangle.c

    # compute points on perpendicular bisectors
    pb_a_1 = Point.scale(t_a, 0.5)
    pb_a_2 = pb_a_1 + Point(t_a.y, -t_a.x)
    pb_b_1 = Point.scale(t_b, 0.5)
    pb_b_2 = pb_b_1 + Point(t_b.y, -t_b.x)

    # find intersection of bisectors
    trans_circumcenter = line.intersection(
        Line(pb_a_1, pb_a_2),
        Line(pb_b_1, pb_b_2),
    )

    # if intersection not found, that indicates the triangle was degenerate
    assert trans_circumcenter is not None

    # un-translate result
    return trans_circumcenter + triangle.c

