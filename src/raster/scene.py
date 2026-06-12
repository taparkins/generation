from PIL import Image

class RasterScene(object):
    def __init__(
        self,
        width,
        height,
        bg_color="#000000ff",
    ):
        self.models = []
        self.image = Image.new(
            "RGBA",
            (width, height),
            bg_color,
        )

    def add_model_object(self, model):
        self.models.append(model)

    def draw(self):
        for model in self.models:
            model.draw(self.image)

    def save(self, filepath):
        self.image.save(filepath, "PNG")

