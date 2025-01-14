import pyglet
import config


class Food(pyglet.shapes.Circle):
    def __init__(self, x: int, y: int, batch: pyglet.graphics.Batch):
        super().__init__(x, y, config.FOOD_SIZE, color=config.FOOD_COLOR, batch=batch)
