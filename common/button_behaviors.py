from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder

Builder.load_string('''
<DraggableButton>:
    on_press: self.on_press_action()
    on_touch_move: self.on_touch_move_action(args[1])
''')


class DraggableButton(Button):
    def __init__(self, **kwargs):
        super(DraggableButton, self).__init__(**kwargs)
        self.button_moved = False
        self.initial_pos = None

    def on_press_action(self):
        self.initial_pos = self.pos
        print("Button pressed")

    def on_touch_move_action(self, touch):
        if self.collide_point(*touch.pos):
            print("Button dragged")
            # Update button position or perform drag action
            self.center = touch.pos
            if self.initial_pos != touch.pos:
                self.button_moved = True

    def on_release_action(self):
        self.button_moved = False
        print("Button released")


class MyApp(App):
    def build(self):
        return DraggableButton(text="Drag or Tap")


if __name__ == '__main__':
    MyApp().run()
