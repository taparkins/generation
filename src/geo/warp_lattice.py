from src.geo.point import Point
import random
import math

class WarpedLattice(object):
    def __init__(
        self,
        artboard_size,
        grid_size,
        min_distortion,
        max_distortion,
    ):
        assert isinstance(artboard_size, tuple)
        assert len(artboard_size) == 2

        assert isinstance(grid_size, tuple)
        assert len(grid_size) == 2

        assert min_distortion <= max_distortion


        spacing = (
            artboard_size[0] / grid_size[0],
            artboard_size[1] / grid_size[1],
        )

        unwarped_lattice = [
            Point(x * spacing[0], y * spacing[1])
            for x in range(grid_size[0])
            for y in range(grid_size[1])
        ]

        def _rand_warp():
            r_range = max_distortion - min_distortion
            r = (random.random() * r_range) + min_distortion
            theta = random.random() * math.pi * 2

            return Point(math.cos(theta) * r, math.sin(theta) * r)

        self.lattice = [ lp + _rand_warp() for lp in unwarped_lattice ]
