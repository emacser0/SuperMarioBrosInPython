from .Settings import *
from .Transform import *
from .GameObject import *

import math

class Camera(GameObject):
    def __init__(self, parent, layer="Default", order=1):
        super().__init__(parent)

        self.layer = layer
        self.order = order

    def translate(self, position):
        assert isinstance(position, Vector2), "Invalid parameter type: {}".format(type(position))

        cos = math.cos(math.radians(-self.transform.rotation))
        sin = math.sin(math.radians(-self.transform.rotation))

        position = position * self.transform.scale
        position = Vector2(position.x * cos - position.y * sin,
                           position.y * cos + position.x * sin)
        position += -self.transform.position

        return position

    def rotate(self, rotation):
        assert isinstance(rotation, int) or isinstance(rotation, float), "Invalid parameter type: {}".format(type(rotation))
        return rotation - self.transform.rotation

    def scale(self, scale):
        assert isinstance(scale, Vector2), "Invalid parameter type: {}".format(type(scale))

        return scale * self.transform.scale