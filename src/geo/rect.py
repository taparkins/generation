from src.geo.point import Point

class Rect(object):
    def __init__(self, a, b):
        assert isinstance(a, Point)
        assert isinstance(b, Point)

        self.left = min(a.x, b.x)
        self.right = max(a.x, b.x)
        self.top = max(a.y, b.y)
        self.bottom = min(a.y, b.y)

    def __repr__(self):
        return f'[({self.left}, {self.top}), ({self.right}, {self.bottom})]'

    def __eq__(r1, r2):
        if not isinstance(r2, Rect):
            return False
        return (
            r1.left == r2.left and
            r1.top == r2.top and
            r1.right == r2.right and
            r1.bottom == r2.bottom
        )

    def draw(self, turtle):
        turtle.up()
        turtle.goto(self.left, self.top)
        turtle.down()
        turtle.goto(self.right, self.top)
        turtle.goto(self.right, self.bottom)
        turtle.goto(self.left, self.bottom)
        turtle.goto(self.left, self.top)
        turtle.up()
