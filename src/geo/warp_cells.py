from src.geo.warp_lattice import WarpedLattice
from src.geo.kdtree import KDTree
from src.geo.point import Point
from src.geo.line import Line

import random


class WarpedCells(object):
    def __init__(
        self,
        artboard_size,
        grid_size,
        min_distortion,
        max_distortion,
        min_degree,
        max_degree,
    ):
        assert min_degree < max_degree

        self.warped_lattice = WarpedLattice(
            artboard_size,
            grid_size,
            min_distortion,
            max_distortion,
        )
        self.lines = set()

        kdtree = KDTree.from_list([
            (p.x, p.y)
            for p in self.warped_lattice.lattice
        ])

        def _find_point_neighbors(pt):
            nearest_neighbors = { pt }
            pt_filter = lambda x: Point(x[0], x[1]) not in nearest_neighbors
            degree = random.randint(min_degree, max_degree)

            for i in range(degree):
                _, neighbor = kdtree.find_nearest((pt.x, pt.y), pt_filter)
                nearest_neighbors.add(Point(neighbor[0], neighbor[1]))

            nearest_neighbors.remove( pt )
            return nearest_neighbors

        neighbor_map = {
            pt: _find_point_neighbors(pt)
            for pt in self.warped_lattice.lattice
        }
        print(len(neighbor_map))
        for pt, neighbors in neighbor_map.items():
            for n in neighbors:
                new_line = Line(pt, n)
                is_valid = True

                for old_line in self.lines:
                    if new_line != old_line and new_line.intersects(old_line, True):
                        is_valid = False
                        break

                if is_valid:
                    self.lines.add(new_line)


