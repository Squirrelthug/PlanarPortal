# Import necessary modules
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from btn_dir.home_libraries_portal import DraggableLibraryButton as DragLibBtn
from btn_dir.game_deck_portal import GameDeckPortal as DeckBtn
from common.button_behaviors import DraggableButton as DragBtn
from common.screen_handler import ScreenHandler
from btn_dir.toggle_portal import DraggableToggleButton as ToggleBtn
from common.playmat import Playmat


class PlanarPortalApp(App):
    def __init__(self, **kwargs):
        super(PlanarPortalApp, self).__init__(**kwargs)
        self.is_game_state = False
        self.screen_handler = ScreenHandler()
        self.playmat = Playmat()            # Store a reference to the Playmat object
        self.menu_buttons = []              # Store a reference to the menu buttons
        self.game_buttons = []              # Store a reference to the game buttons

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)    # Black background
        Window.fullscreen = 'auto'          # Full screen mode
        main_widget = Widget()              # Create a main widget
        main_widget.add_widget(self.playmat)    # Add the playmat to the main widget
        self.create_buttons(main_widget, self.playmat)  # Create the menu buttons
        ToggleBtn.toggle_state()            # Initialize appropriate game state buttons

        return main_widget

    def create_buttons(self, main_widget, playmat):
        # Create menu buttons here
        # Exit
        exit_button = DragBtn(text='Exit',
                              size_hint=(None, None),
                              size=(300, 150),
                              pos=(Window.center[0] - 150, Window.center[1] - 175))

        # Refresh
        refresh_button = DragBtn(text='Refresh',
                                 size_hint=(None, None),
                                 size=(300, 150),
                                 pos=(Window.center[0] - 0, Window.center[1] + 0))
        # Libraries
        libraries_button = DragLibBtn(text='Libraries',
                                      size_hint=(None, None),
                                      size=(300, 150),
                                      pos=(Window.center[0] - 200, Window.center[1] + 395))
        # Toggle Game State
        toggle_game_button = ToggleBtn(text='Start Game',
                                     size_hint=(None, None),
                                     size=(300, 150),
                                     pos=(Window.center[0] + 250, Window.center[1] + 65))
        # Deck
        deck_button = DeckBtn(text='Deck',
                              size_hint=(None, None),
                              size=(300, 150),
                              pos=(Window.center[0] - 250, Window.center[1] + 35))

        # Bind the buttons to their respective methods
        exit_button.bind(on_press=lambda x: App.get_running_app().stop())  # Exit the app
        refresh_button.bind(on_press=lambda x: playmat.draw_grid())  # Refresh the grid
        toggle_game_button.bind(on_release=ToggleBtn.toggle_state)  # Switch to game state
        libraries_button.bind(on_release=DragLibBtn.lib_popup)  # Popup on release
        deck_button.bind(on_release=DeckBtn.deck_popup_behavior)  # Popup on release

        # Use .bind to make the buttons movable
        exit_button.bind(on_touch_move=DragBtn.on_touch_move_action)
        refresh_button.bind(on_touch_move=DragBtn.on_touch_move_action)
        toggle_game_button.bind(on_touch_move=ToggleBtn.on_touch_move_action)
        libraries_button.bind(on_touch_move=DragLibBtn.on_touch_move_action)
        deck_button.bind(on_touch_move=DeckBtn.on_touch_move_action)

        # Add the buttons to the main_widget
        main_widget.add_widget(exit_button)
        main_widget.add_widget(refresh_button)
        main_widget.add_widget(toggle_game_button)
        main_widget.add_widget(libraries_button)
        main_widget.add_widget(deck_button)

        self.menu_buttons = [exit_button, refresh_button, toggle_game_button, libraries_button]
        self.game_buttons = [toggle_game_button, deck_button]

    def on_window_resize(self, window, width, height):
        # This method is called whenever the window size changes
        main_widget = self.root
        if self.is_game_state:
            # If the menu state is active, update the pos of the game buttons
            self.create_game_buttons(main_widget, main_widget.children[0])
        else:
            # If the menu state is active, update the pos of the menu buttons
            self.create_game_buttons(main_widget, main_widget.children[0])

if __name__ == '__main__':
    PlanarPortalApp().run()