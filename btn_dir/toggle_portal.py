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
        # TODO: Possibly related to toggle_game_state bug
        self.initial_pos = self.pos
        print("Toggle Button pressed")
        self.toggle_game_state()

    def on_touch_move_action(self, touch):
        if self.collide_point(*touch.pos):
            print("Toggle Button dragged")
            self.center = touch.pos             # Update button position when touched
            if self.initial_pos != touch.pos:   # Check if the button was moved
                self.button_moved = True        # Set the button_moved flag if it was

    def on_release_action(self):
        self.button_moved = False               # Reset the button_moved flag
        print("Toggle Button released")

    def toggle_game_state(self):
        # TODO: There is a bug here. The game state is not being toggled properly
        main_widget = self.parent
        if self.is_game_state:
            # Switching to menu state
            self.screen_handler.clear_screen(main_widget)   # Clear the main_widget
            self.create_menu_buttons(main_widget, self.playmat)
            self.playmat.draw_grid()                             # Redraw the grid
            self.is_game_state = False
        else:
            # Switching to game state
            self.screen_handler.clear_screen(main_widget)  # Clear the main_widget
            self.create_game_buttons(main_widget, self.playmat)
            self.playmat.draw_grid()                             # Redraw the grid
            self.is_game_state = True


class MyApp(App):
    def build(self):
        return DraggableToggleButton(text="Drag or Tap")


if __name__ == '__main__':
    MyApp().run()
