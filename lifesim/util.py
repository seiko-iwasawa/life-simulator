from food import Food
from fish import Fish
import config
import random
import pyglet


def gen_food(batch: pyglet.graphics.Batch):
    return Food(
        random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT), batch
    )


def gen_fish(batch: pyglet.graphics.Batch):
    return Fish(
        random.randint(0, config.WIDTH), random.randint(0, config.HEIGHT), batch
    )


def dist(obj1: Fish | Food, obj2: Fish | Food):
    return ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5
