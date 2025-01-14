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
        self.food: list[Food] = []
        self.fishes = [util.gen_fish(self.batch) for n in range(config.FISH_N)]

    def gen_food(self):
        self.food.append(util.gen_food(self.batch))

    def update(self, dt: float):
        for fish in self.fishes:
            fish.update(self.food, self.fishes, dt)
        if len(self.food) < config.FOOD_N:
            self.gen_food()
        self.intersect()

    def intersect(self):
        new_food: list[Food] = []
        for food in self.food:
            flag = True
            for fish in self.fishes:
                if util.dist(fish, food) <= fish.radius + food.radius:
                    flag = False
            if flag:
                new_food.append(food)
        self.food = new_food
