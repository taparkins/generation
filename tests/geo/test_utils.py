import pytest

from src.geo.utils import Point


@pytest.mark.parametrize(
    ('p1', 'p2', 'expected'), [
    (Point( 0,  0), Point( 0,  0), True),
    (Point( 1,  0), Point( 1,  0), True),
    (Point( 0,  1), Point( 0,  1), True),
    (Point( 1,  1), Point( 1,  1), True),
    (Point( 5,  3), Point( 5,  3), True),
    (Point(-5, -3), Point(-5, -3), True),

    (Point( 1,  0), Point( 0,  0), False),
    (Point( 0,  1), Point( 0,  0), False),
    (Point( 0,  0), Point( 1,  0), False),
    (Point( 0,  0), Point( 0,  1), False),
    (Point( 5,  0), Point( 3,  0), False),
    (Point( 0,  5), Point( 0,  3), False),
    (Point( 1,  0), Point(-1,  0), False),
    (Point( 0,  1), Point( 0, -1), False),

    (Point( 0,  0), 'Not a point', False),
])
def test_point_eq(p1, p2, expected):
    assert (p1 == p2) == expected
    assert (p2 == p1) == expected
    assert (p1 != p2) == (not expected)
    assert (p2 != p1) == (not expected)


@pytest.mark.parametrize(
    ('p1', 'p2', 'expected'), [
    (Point( 0,  0), Point( 0,  0), Point( 0,  0)),
    (Point( 1,  0), Point( 0,  0), Point( 1,  0)),
    (Point( 0,  1), Point( 0,  0), Point( 0,  1)),
    (Point( 0,  1), Point( 1,  0), Point( 1,  1)),
    (Point( 1,  1), Point( 0,  0), Point( 1,  1)),
    (Point( 5,  0), Point( 3,  0), Point( 8,  0)),
    (Point( 0,  5), Point( 0,  3), Point( 0,  8)),
    (Point( 3,  5), Point( 5,  3), Point( 8,  8)),
    (Point( 3,  5), Point(-5, -3), Point(-2,  2)),
])
def test_point_add(p1, p2, expected):
    assert (p1 + p2) == expected
    assert (p2 + p1) == expected


def test_add_type_match():
    with pytest.raises(AssertionError):
        Point(0, 0) + 'not a point'


@pytest.mark.parametrize(
    ('p1', 'p2', 'expected'), [
    (Point( 0,  0), Point( 0,  0), Point( 0,  0)),
    (Point( 1,  0), Point( 0,  0), Point( 1,  0)),
    (Point( 0,  0), Point( 1,  0), Point(-1,  0)),
    (Point( 0,  1), Point( 0,  0), Point( 0,  1)),
    (Point( 0,  1), Point( 1,  0), Point(-1,  1)),
    (Point( 1,  1), Point( 0,  0), Point( 1,  1)),
    (Point( 0,  0), Point( 1,  1), Point(-1, -1)),
    (Point( 5,  0), Point( 3,  0), Point( 2,  0)),
    (Point( 3,  0), Point( 5,  0), Point(-2,  0)),
    (Point( 0,  5), Point( 0,  3), Point( 0,  2)),
    (Point( 0,  3), Point( 0,  5), Point( 0, -2)),
    (Point( 3,  5), Point( 5,  3), Point(-2,  2)),
    (Point( 3,  5), Point(-5, -3), Point( 8,  8)),
])
def test_point_sub(p1, p2, expected):
    assert (p1 - p2) == expected


def test_sub_type_match():
    with pytest.raises(AssertionError):
        Point(0, 0) - 'not a point'


@pytest.mark.parametrize(
    ('p', 'c', 'expected'), [
    (Point( 0,  0),  2, Point( 0,  0)),
    (Point( 1,  0),  2, Point( 2,  0)),
    (Point( 0,  1),  2, Point( 0,  2)),
    (Point( 1,  0), -2, Point(-2,  0)),
    (Point( 0,  1), -2, Point( 0, -2)),
    (Point(-1,  0),  2, Point(-2,  0)),
    (Point( 0, -1),  2, Point( 0, -2)),
    (Point(-1,  0), -2, Point( 2,  0)),
    (Point( 0, -1), -2, Point( 0,  2)),
    (Point( 1,  1),  2, Point( 2,  2)),
    (Point( 3,  0),  2, Point( 6,  0)),
    (Point( 0,  3),  2, Point( 0,  6)),
    (Point( 3,  4),  2, Point( 6,  8)),
    (Point(-3, -4),  2, Point(-6, -8)),
])
def test_point_scale(p, c, expected):
    assert Point.scale(p, c) == expected

