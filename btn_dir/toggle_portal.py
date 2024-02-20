from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder

from common.screen_handler import ScreenHandler
from common.playmat import Playmat

Builder.load_string('''
<DraggableToggleButton>:
    on_press: self.on_press_action()
    on_touch_move: self.on_touch_move_action(args[1])
''')


class DraggableToggleButton(Button):
    def __init__(self, **kwargs):
        super(DraggableToggleButton, self).__init__(**kwargs)
        self.button_moved = False
        self.initial_pos = None
        self.screen_handler = ScreenHandler()
        self.playmat = Playmat()                # Initialize the Playmat object

    def on_press_action(self):
        self.initial_pos = self.pos
        print("Toggle Button touched")
        self.toggle_state()

    def on_touch_move_action(self, touch):
        if self.collide_point(*touch.pos):
            print("Toggle Button dragged")
            self.center = touch.pos             # Update button position when touched
            if self.initial_pos != touch.pos:   # Check if the button was moved
                self.button_moved = True        # Set the button_moved flag if it was

    def on_release_action(self):
        self.button_moved = False               # Reset the button_moved flag
        print("Toggle Button released")

    def toggle_state(self):
        if self.is_game_state:
            # if game state is active hide menu buttons and show game buttons
            for button in self.menu_buttons:
                button.size = (0, 0)  # Hide the button
                button.disabled = True  # Disable the button
            for button in self.game_buttons:
                button.size = (300, 150)  # Show the button
                button.disabled = False  # Enable the button
        else:
            # if menu state is active hide game buttons and show menu buttons
            for button in self.game_buttons:
                button.size = (0, 0)  # Hide the button
                button.disabled = True  # Disable the button
            for button in self.menu_buttons:
                button.size = (300, 150)  # Show the button
                button.disabled = False  # Enable the button


class MyApp(App):
    def build(self):
        return DraggableToggleButton(text="Drag or Tap")


if __name__ == '__main__':
    MyApp().run()
