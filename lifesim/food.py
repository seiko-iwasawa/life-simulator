import pyglet

class Food(pyglet.shapes.Circle):
    def __init__(self, x: int, y: int, batch: pyglet.graphics.Batch):
        super().__init__(x, y, 3, color=(0, 255, 0), batch=batch)
