import pyglet
from field import Field


class Window(pyglet.window.Window):
    def __init__(self):
        super().__init__(
            800,
            800,
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
        pyglet.clock.schedule_interval(self.update, 1 / 60)
        pyglet.app.run(1 / 60)


def main():
    Window().run()


if __name__ == "__main__":
    main()
