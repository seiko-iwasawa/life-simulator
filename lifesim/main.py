import pyglet
from field import Field
import config


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(
            config.WIDTH,
            config.HEIGHT,
            "Life Simulator",
            config=pyglet.gl.Config(sample_buffers=1, samples=4),  # anti-aliasing
        )
        self.batch = pyglet.graphics.Batch()
        self.field = Field(self.batch)

    def on_draw(self):
        self.clear()
        self.batch.draw()
        pyglet.gl.glFlush()

    def update(self, dt: float):
        self.field.update(dt)

    def run(self):
        pyglet.clock.schedule_interval(self.update, 1 / config.FPS)
        pyglet.app.run(1 / config.FPS)


def main():
    Window().run()


if __name__ == "__main__":
    main()
