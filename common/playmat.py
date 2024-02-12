from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Line, Color


class Playmat(Widget):
    def __init__(self, **kwargs):
        super(Playmat, self).__init__(**kwargs)
        self.draw_grid()
        Window.bind(on_resize=self.window_resize)

    def draw_grid(self):
        self.canvas.clear()                             # Clear the canvas to avoid overlapping lines
        with self.canvas:
            Color(0.2, 0.2, 0.2)                        # Grey color for the grid lines
            for i in range(0, Window.width, 100):       # This will draw grid lines on the canvas; adjust as needed
                Line(points=[i, 0, i, Window.height])
            for j in range(0, Window.height, 100):
                Line(points=[0, j, Window.width, j])

    def window_resize(self, instance, width, height):   # Redraw the grid whenever the window size changes

        self.draw_grid()

