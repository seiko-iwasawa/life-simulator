import pyglet
from food import Food
import config
import util


class Fish(pyglet.shapes.Circle):
    def __init__(self, x: int, y: int, batch: pyglet.graphics.Batch):
        super().__init__(x, y, config.FISH_SIZE, color=config.FISH_COLOR, batch=batch)
        self.speed = config.FISH_SPEED

    def update(self, food: list[Food], fishes: list["Fish"], dt: float):
        if not food:
            return
        near_food = min(food, key=lambda f: util.dist(self, f))
        vec = (near_food.x - self.x, near_food.y - self.y)
        dist = util.dist(self, near_food)
        self.x += vec[0] / dist * self.speed * dt
        self.y += vec[1] / dist * self.speed * dt
