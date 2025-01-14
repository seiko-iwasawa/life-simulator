import food
import fish
import config
import random
import pyglet
import math


def gen_food(batch: pyglet.graphics.Batch):
    return food.Food(
        random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT), batch
    )


def gen_fish(batch: pyglet.graphics.Batch):
    return fish.Fish(
        random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT), batch
    )


def dist(obj1: "fish.Fish | food.Food", obj2: "fish.Fish | food.Food"):
    return math.sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2)


def intersect(obj1: "fish.Fish | food.Food", obj2: "fish.Fish | food.Food"):
    return dist(obj1, obj2) <= obj1.radius + obj2.radius


def direction(fish: "fish.Fish", target: "fish.Fish | food.Food"):
    return math.atan2(target.y - fish.y, target.x - fish.x)
