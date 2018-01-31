import pytest

from src.geo.point import Point
from src.geo.line import Line
from src.geo import line


def test_constructor_errors():
    with pytest.raises(AssertionError):
        Line('not a point', Point(1, 0))

    with pytest.raises(AssertionError):
        Line(Point(0, 0), 'not a point')

    with pytest.raises(AssertionError):
        Line(Point(1, 0), Point(1, 0))


def test_intersection_errors():
    with pytest.raises(AssertionError):
        line.intersection(
            'not a line',
            Line(Point(0, 0), Point(1, 0)),
        )

    with pytest.raises(AssertionError):
        line.intersection(
            Line(Point(0, 0), Point(1, 0)),
            'not a line',
        )


@pytest.mark.parametrize(
    ('line_1', 'line_2', 'expected'), [

    ( Line(Point( 2,  0), Point( 1,  0)),
      Line(Point(-1, -1), Point(-2, -2)),
      Point( 0,  0) ), # intersect; horizontal x diagonal

    ( Line(Point( 0,  2), Point( 0,  1)),
      Line(Point(-1, -1), Point(-2, -2)),
      Point( 0,  0) ), # intersect; vertical x diagonal

    ( Line(Point( 1,  1), Point( 2,  2)),
      Line(Point( 1, -1), Point( 2, -2)),
      Point( 0,  0) ), # intersect; diagonal x diagonal 1

    ( Line(Point( 0,  0), Point( 6, 10)),
      Line(Point( 0,  2), Point(-3, -1)),
      Point( 3,  5) ), # intersect; diagonal x diagonal 2

    ( Line(Point( 1,  1), Point( 2,  2)),
      Line(Point( 3,  1), Point( 4,  2)),
      None ), # parallel; diagonal

    ( Line(Point( 0,  1), Point( 1,  1)),
      Line(Point( 0,  3), Point( 1,  3)),
      None ), # parallel; horizontal

    ( Line(Point( 1,  1), Point( 1,  2)),
      Line(Point( 3,  1), Point( 3,  2)),
      None ), # parallel; vertical

    ( Line(Point( 0,  1), Point( 0,  2)),
      Line(Point( 0,  3), Point( 0,  4)),
      None ), # coinciding lines
])
def test_intersection(line_1, line_2, expected):
    assert line.intersection(line_1, line_2) == expected

