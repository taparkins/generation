import pytest

from src.geo.point import Point
from src.geo.grid import *

@pytest.mark.parametrize(
    ('center', 'init_dir', 'turn_cw', 'count', 'expected'), [
    ( Point(0, 0),
      Point(0, 1),
      True,
      1,
      [ Point(0, 0) ]), # First point is origin, standard
    ( Point(-1, 10),
      Point(0, 1),
      True,
      1,
      [ Point(-1, 10) ]), # First point is origin, offset
    ( Point(0, 0),
      Point(0, 1),
      True,
      9,
      [ Point(0, 0),
        Point(0, 1),
        Point(1, 1),
        Point(1, 0),
        Point(1, -1),
        Point(0, -1),
        Point(-1, -1),
        Point(-1, 0),
        Point(-1, 1)]), # Two layers, cw, start up
    ( Point(0, 0),
      Point(1, 0),
      True,
      9,
      [ Point(0, 0),
        Point(1, 0),
        Point(1, -1),
        Point(0, -1),
        Point(-1, -1),
        Point(-1, 0),
        Point(-1, 1),
        Point(0, 1),
        Point(1, 1)]), # Two layers, cw, start right
    ( Point(0, 0),
      Point(0, -1),
      False,
      9,
      [ Point(0, 0),
        Point(0, -1),
        Point(1, -1),
        Point(1, 0),
        Point(1, 1),
        Point(0, 1),
        Point(-1, 1),
        Point(-1, 0),
        Point(-1, -1)]), # Two layers, ccw, start down
    ( Point(-10, 69),
      Point(-1, 0),
      True,
      25,
      [ Point(-10, 69),
        Point(-11, 69),
        Point(-11, 70),
        Point(-10, 70),
        Point(-9, 70),
        Point(-9, 69),
        Point(-9, 68),
        Point(-10, 68),
        Point(-11, 68),
        Point(-12, 68),
        Point(-12, 69),
        Point(-12, 70),
        Point(-12, 71),
        Point(-11, 71),
        Point(-10, 71),
        Point(-9, 71),
        Point(-8, 71),
        Point(-8, 70),
        Point(-8, 69),
        Point(-8, 68)]), # 3 layers, cw, start left, offset
])
def test_spiral_itr(center, init_dir, turn_cw, count, expected):
    results = []
    i = 0
    for result in spiral_itr(center, init_dir, turn_cw):
        i += 1
        results.append(result)

        if i > count:
            break

    assert all([
        a == b
        for a, b in zip(expected, results)
    ])
