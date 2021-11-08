import pico2d

import os
if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    from GameObject import *
    from PhysicsManager import *
    from Camera import *
else:
    from .GameObject import *
    from .PhysicsManager import *
    from .Camera import *

class Scene:
    def __init__(self, name=""):
        self.name = name
        self.root = GameObject(None)
        self.root.scene = self

        self.collisionManager = CollisionManager(self)
        self.cameras = []

        self.updateFixedTimeStep = 3.0
        self.updateTime = 0.0

        self.debug = False

    def update(self, deltaTime):
        self.updateTime += deltaTime

        while self.updateTime >= self.updateFixedTimeStep:
            self.collisionManager.Update()
            self.root.update(self.updateFixedTimeStep)

            self.updateTime -= self.updateFixedTimeStep

    def render(self):
        for camera in self.cameras:
            self.root.render(camera, self.debug)

    def addCamera(self, parent, layer, order):
        camera = Camera(parent, layer, order)

        self.cameras.append(camera)
        self.cameras.sort(key=lambda camera: camera.order)

        return camera

    def removeCamera(self, camera):
        self.cameras.remove(camera)