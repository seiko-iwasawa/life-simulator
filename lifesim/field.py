import pyglet
from food import Food
import random


class Field:
    def __init__(self, batch: pyglet.graphics.Batch):
        self.batch = batch
        self.background = pyglet.shapes.Rectangle(
            0, 0, 800, 800, color=(0, 0, 255), batch=batch
        )
        self.food: list[Food] = []

    def gen_food(self):
        self.food.append(
            Food(random.randint(0, 800), random.randint(0, 800), self.batch)
        )

    def update(self, dt: float):
        if len(self.food) < 100:
            self.gen_food()
        print(len(self.food))
