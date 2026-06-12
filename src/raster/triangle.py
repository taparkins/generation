from src.geo.triangle import Triangle
from PIL import ImageColor, ImageDraw, Image

class RasterPoint(object):
    def __init__(
        self,
        model,
        fill_color=ImageColor.getrgb('#ffffffff'),
        stroke_color=ImageColor.getrgb('#ffffffff'),
        stroke_width=1,
    ):
        assert isinstance(model, Triangle)
        assert fill_color is not None or stroke_color is not None

        self.model = model
        self.fill_color = color
        self.stroke_color = color
        self.stroke_width = stroke_width

    def draw(self, image):
        assert isinstance(image, Image.Image)

        points = [
            (self.model.a.x, self.model.a.y),
            (self.model.b.x, self.model.b.y),
            (self.model.c.x, self.model.c.y),
        ]

        d = ImageDraw.Draw(image)
        d.polygon(
            points,
            self.fill_color,
            self.stroke_color,
            self.stroke_width,
        )
