from src.geo.point import Point
from PIL import ImageColor, ImageDraw, Image

class RasterPoint(object):
    def __init__(
        self,
        model,
        radius=1,
        color=ImageColor.getrgb('#ffffffff'),
    ):
        assert isinstance(model, Point)

        self.model = model
        self.radius = radius
        self.color = color

    def draw(self, image):
        assert isinstance(image, Image.Image)
        d = ImageDraw.Draw(image)
        d.circle(
            (self.model.x, self.model.y),
            self.radius,
            self.color,
        )
