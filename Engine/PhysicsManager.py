import pymunk

class PhysicsManager:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = 0, -98.1

        self.rigidBodies = []

    def add(self, rigidBody):
        self.rigidBodies.append(rigidBody)
        self.space.add(rigidBody.body, rigidBody.shape)

    def remove(self, rigidBody):
        self.rigidBodies.remove(rigidBody)
        self.space.remove(rigidBody.body, rigidBody.remove)

    def update(self, deltaTime):
        self.space.step(deltaTime)

    def sync(self):
        for rigidBody in self.rigidBodies:
            rigidBody.sync()