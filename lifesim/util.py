import food
import fish
import config
import random
import pyglet


def gen_food(batch: pyglet.graphics.Batch):
    return food.Food(
        random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT), batch
    )


def gen_fish(batch: pyglet.graphics.Batch):
    return fish.Fish(
        random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT), batch
    )


def dist(obj1: "fish.Fish | food.Food", obj2: "fish.Fish | food.Food"):
    return ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5
