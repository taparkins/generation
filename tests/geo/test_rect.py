import pytest

from src.geo.point import Point
from src.geo.rect import Rect


@pytest.mark.parametrize(
    ('r1', 'r2', 'expected'), [
    (Rect(Point(0, 0), Point(2, 2)), Rect(Point(2, 0), Point(0, 2)), True),
    (Rect(Point(0, 0), Point(-1, 2)), Rect(Point(-3, 1), Point(0, 2)), False),
    (Rect(Point(0, 0), Point(0, 0)), Rect(Point(0, 0), Point(0, 0)), True),
    (Rect(Point(2, 2), Point(2, 2)), Rect(Point(2, 0), Point(0, 2)), False),
    (Rect(Point(-1, 12), Point(2, 0)), None, False),
    (Rect(Point(-1, 12), Point(2, 0)), 'not a rect', False),
])
def test_rect_eq(r1, r2, expected):
    assert (r1 == r2) == expected
    assert (r2 == r1) == expected
    assert (r1 != r2) == (not expected)
    assert (r2 != r1) == (not expected)
