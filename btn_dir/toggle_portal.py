from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from common.screen_handler import ScreenHandler
from common.playmat import Playmat
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string('''
<DraggableToggleButton>:
    on_press: self.on_press_action()
    on_touch_move: self.on_touch_move_action(args[1])
''')


class DraggableToggleButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(DraggableToggleButton, self).__init__(**kwargs)
        self.button_moved = False
        self.initial_pos = None
        self.screen_handler = ScreenHandler()
        self.playmat = Playmat()                # Initialize the Playmat object

    def on_press(self):
        self.on_press_action()

    def on_press_action(self):
        self.initial_pos = self.pos
        print("Toggle Button touched")

    def on_touch_move_action(self, touch):
        if self.collide_point(*touch.pos):
            print("Toggle Button dragged")
            self.center = touch.pos             # Update button position when touched
            if self.initial_pos != touch.pos:   # Check if the button was moved
                self.button_moved = True        # Set the button_moved flag if it was
        return True

    def on_release_action(self):
        self.button_moved = False               # Reset the button_moved flag
        print("Toggle Button released")

    def toggle_state(self):
        app = App.get_running_app()
        is_game_state = app.is_game_state
        game_buttons = app.game_buttons
        menu_buttons = app.menu_buttons
        print(f"Before toggle: is_game_state: {is_game_state}")
        if self.button_moved:
            self.button_moved = False
            return
        if is_game_state:
            print(game_buttons)
            # if game state is active hide menu buttons and show game buttons
            for button in menu_buttons:
                button.opacity = 0
                button.size = (0, 0)
                button.disabled = True
            for button in game_buttons:
                button.opacity = 1
                button.size = (300, 150)
                button.disabled = False
        else:
            print(menu_buttons)
            # if menu state is active hide game buttons and show menu buttons
            for button in game_buttons:
                button.opacity = 0
                button.size = (0, 0)
                button.disabled = True
            for button in menu_buttons:
                button.opacity = 1
                button.size = (300, 150)
                button.disabled = False
        app.is_game_state = not is_game_state
        print(f"After toggle: is_game_state: {is_game_state}")
        self.button_moved = False


class MyApp(App):
    def build(self):
        return DraggableToggleButton(text="Drag or Tap")


if __name__ == '__main__':
    MyApp().run()
