import pyglet
from food import Food
from fish import Fish
import random
import config


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
        self.fishes = [
            Fish(
                random.randint(0, config.WIDTH),
                random.randint(0, config.HEIGHT),
                self.batch,
            )
            for n in range(config.FISH_N)
        ]

    def gen_food(self):
        self.food.append(
            Food(
                random.randint(0, config.WIDTH),
                random.randint(0, config.HEIGHT),
                self.batch,
            )
        )

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
                dist = ((fish.x - food.x) ** 2 + (fish.y - food.y) ** 2) ** 0.5
                if dist <= fish.radius + food.radius:
                    flag = False
            if flag:
                new_food.append(food)
        self.food = new_food
