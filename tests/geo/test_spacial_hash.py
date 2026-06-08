import pytest

from src.geo.point import Point
from src.geo.spatial_hash import GeoMap_Point


def test_find_nearest__empty():
    geomap = GeoMap_Point(set())
    result_point, result_distance = geomap.find_nearest(Point(0, 0))

    assert result_point is None
    assert result_distance is None


def test_find_nearest__search_only_elem():
    geomap = GeoMap_Point({Point(0, 0)})
    result_point, result_distance = geomap.find_nearest(Point(0, 0))

    assert result_point is None
    assert result_distance is None


def test_find_nearest__single_elem():
    geomap = GeoMap_Point({Point(0, 0)})
    search_point = Point(1, 2)

    result_point, result_distance = geomap.find_nearest(search_point)

    assert result_point == Point(0, 0)
    assert result_distance == Point.dist(result_point, search_point)


def test_find_nearest__multi_elem():
    sample_points = {
        Point(-10, 1),
        Point(10, 15),
        Point(-5, -5),
    }
    geomap = GeoMap_Point(sample_points)
    search_point = Point(1, 2)

    result_point, result_distance = geomap.find_nearest(search_point)

    assert result_point == Point(-5, -5)
    assert result_distance == Point.dist(result_point, search_point)


@pytest.mark.skip(reason = "this should pass, but it will take a VERY long time!")
def test_find_nearest__far_search():
    sample_points = {
        Point(-10004822, 89238048),
        Point(-90128582, 19028459),
        Point( 29485820, 18347192),
    }
    geomap = GeoMap_Point(sample_points)
    search_point = Point(0, 0)

    result_point, result_distance = geomap.find_nearest(search_point)

    assert result_point == Point( 29485820, 18347192)
    assert result_distance == Point.dist(result_point, search_point)

