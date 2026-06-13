from src.geo.mesh.warp_cells import WarpedCells
from src.geo.point import Point
from src.geo.line import Line
from src.raster.scene import RasterScene
from src.raster.point import RasterPoint
from src.raster.line import RasterLine

import random
import string

scene_size = (800, 800)
margin = 100
artboard_size = (
    scene_size[0] - (2 * margin),
    scene_size[1] - (2 * margin),
)

wc = WarpedCells(
    artboard_size,
    (20, 20),
    5, 10,
    3, 6,
)

scene = RasterScene(scene_size[0], scene_size[1])

def _make_point_model(pt):
    return RasterPoint(
        pt + Point(margin, margin),
        2,
    )

def _make_line_model(l):
    return RasterLine(
        l.translated(margin, margin),
        '#99a3f0ff',
    )

for l in wc.lines:
    scene.add_model_object(_make_line_model(l))
for pt in wc.warped_lattice.lattice:
    scene.add_model_object(_make_point_model(pt))

def _gen_filepath():
    suffix = ''.join(random.sample(string.ascii_letters, 8))
    return (f'output/test_{suffix}.png')

scene.draw()
scene.save(_gen_filepath())
