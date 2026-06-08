from src.geo.point import Point
from src.geo.grid import spiral_itr
from collections import defaultdict

import math

class GeoMap_Point(object):
    def __init__(self, points):
        assert isinstance(points, set)

        self.map = defaultdict(set)

        for point in points:
            assert isinstance(point, Point)
            adj_x = math.floor(point.x)
            adj_y = math.floor(point.y)
            self.map[Point(adj_x, adj_y)].add(point)

    def find_nearest(self, search_point):
        assert isinstance(search_point, Point)

        min_distance = None
        min_point = None
        search_center = Point(
                math.floor(search_point.x),
                math.floor(search_point.y)
        )

        # Edge case: if the map has no points, or only contains a single point
        # that matches the search_point, the loop below will iterate forever.
        # This fencepost handles those scenarios:
        if len(self.map) == 0:
            return None, None
        elif len(self.map) == 1:
            if len(self.map[search_center]) == 1:
                if list(self.map[search_center])[0] == search_point:
                    return None, None

        for check_point in spiral_itr(search_center):
            # Once we found at least one candidate for minimum, we can bound
            # our search by a box that has length/height equal to twice the
            # radius from the search point
            if min_distance is not None and check_point.x > min_distance and check_point.y > min_distance:
                break

            # check_points represent buckets of points (potentially multiple
            # within integer coordinates of one another), so check each as a
            # potential candidate:
            for candidate in self.map[check_point]:
                # We shouldn't match to ourselves, or else this would be kind
                # of trivial ;)
                if candidate != search_point:
                    check_distance = Point.dist(candidate, search_point)
                    if min_point is None or check_distance < min_distance:
                        min_point = candidate
                        min_distance = check_distance

        return min_point, min_distance
