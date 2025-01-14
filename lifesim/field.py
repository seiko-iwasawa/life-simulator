import pyglet
from food import Food
from fish import Fish
import config
import util


class Field:
    def __init__(self, batch: pyglet.graphics.Batch):
        self.batch = batch
        self.background = pyglet.shapes.Rectangle(
            0,
            0,
            config.WIDTH,
            config.HEIGHT,
            color=config.BACKGROUND_COLOR,
            batch=batch,
        )
        self.food: list[Food] = [
            util.gen_food(self.batch) for n in range(config.FOOD_N)
        ]
        self.fishes = [util.gen_fish(self.batch) for n in range(config.FISH_N)]

    def update(self, dt: float):
        for fish in self.fishes:
            fish.update(self.food, self.fishes, dt)
        while self.intersect():
            ...

    def intersect(self):
        for fish in self.fishes:
            for other in self.fishes:
                if (
                    fish != other
                    and util.dist(fish, other) <= fish.radius + other.radius
                ):
                    self.fishes.pop(self.fishes.index(other))
                    return True
        for fish in self.fishes:
            for food in self.food:
                if util.dist(fish, food) <= fish.radius + food.radius:
                    self.food.pop(self.food.index(food))
                    return True
        return False
