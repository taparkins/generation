from src.geo.line import Line
from PIL import ImageColor, ImageDraw, Image

class RasterLine(object):
    def __init__(
        self,
        model,
        color=ImageColor.getrgb('#ffffffff'),
    ):
        assert isinstance(model, Line)

        self.model = model
        self.color = color

    def draw(self, image):
        assert isinstance(image, Image.Image)
        d = ImageDraw.Draw(image)
        d.line(
            [
                (self.model.a.x, self.model.a.y),
                (self.model.b.x, self.model.b.y),
            ],
            self.color,
        )
