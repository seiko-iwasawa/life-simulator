import pyglet
from food import Food
import config
import util
import math


class Fish(pyglet.shapes.Sector):
    def __init__(self, x: int, y: int, batch: pyglet.graphics.Batch):
        super().__init__(x, y, config.FISH_SIZE, color=config.FISH_COLOR, batch=batch)
        self.speed = config.FISH_SPEED
        self.mouth_angle = 0
        self.mouth_sign = +1

    def update(self, food: list[Food], fishes: list["Fish"], dt: float):
        if not food:
            return
        near_food = min(food, key=lambda f: util.dist(self, f))
        dir = util.direction(self, near_food)
        self.x += math.cos(dir) * min(util.dist(self, near_food), self.speed * dt)
        self.y += math.sin(dir) * min(util.dist(self, near_food), self.speed * dt)
        self.mouth_angle += dt * self.mouth_sign * config.FISH_MOUTH_SPEED
        if self.mouth_angle > math.pi / 2:
            self.mouth_sign = -1
            self.mouth_angle = math.pi / 2
        if self.mouth_angle < 0:
            self.mouth_sign = +1
            self.mouth_angle = 0
        self.start_angle = dir + self.mouth_angle / 2
        self.angle = math.tau - self.mouth_angle
