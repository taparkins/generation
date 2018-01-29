import pytest

from src.geo.utils import Point
from src.geo.triangle import Triangle
from src.geo import triangle


def test_constructor_errors():
    with pytest.raises(AssertionError):
        Triangle(
            'not a point',
            Point( 0,  0),
            Point( 1,  0),
        )
    with pytest.raises(AssertionError):
        Triangle(
            Point( 0,  0),
            'not a point',
            Point( 1,  0),
        )
    with pytest.raises(AssertionError):
        Triangle(
            Point( 0,  0),
            Point( 1,  0),
            'not a point',
        )


@pytest.mark.parametrize(
    ('t', 'expected'), [

    ( Triangle(Point( 2,  0), Point( 0,  2), Point( 0,  0)),
      Point(  1,  1) ),  # right triangle at origin

    ( Triangle(Point(-1,  2), Point( 1,  2), Point( 0,  0)),
      Point( 0, 1.25) ), # acute triangle at origin

    ( Triangle(Point(-2,  1), Point( 2,  1), Point( 0,  0)),
      Point( 0, 2.5) ),  # obtuse triangle at origin

    ( Triangle(Point( 1, -3), Point(-1, -1), Point(-1, -3)),
      Point(  0, -2) ),  # right triangle translated

    ( Triangle(Point( 3,  7), Point( 5,  7), Point( 4,  5)),
      Point( 4, 6.25) ), # acute triangle translated

    ( Triangle(Point( 5,  1), Point( 9,  1), Point( 7,  0)),
      Point( 7, 2.5) ),  # obtuse triangle translated

])
def test_circumcenter(t, expected):
    assert triangle.circumcenter(t) == expected


def test_circumcenter_errors():
    with pytest.raises(AssertionError):
        triangle.circumcenter('not a triangle')

    with pytest.raises(AssertionError):
        triangle.circumcenter(Triangle(Point(0, 0), Point(1, 0), Point(2, 0)))

