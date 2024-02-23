# Import necessary modules
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from btn_dir.home_libraries_portal import DraggableLibraryButton as DragLibBtn
from btn_dir.game_deck_portal import GameDeckButton as DeckBtn
from btn_dir.game_grave_portal import GameGraveButton as GraveBtn
from btn_dir.exit_portal import ExitButton as DragBtn
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


        return main_widget

    def create_buttons(self, main_widget, playmat):
        # Create menu buttons here
        # Exit
        exit_button = DragBtn(source='data/images/exit_portal.png',
                              size_hint=(None, None),
                              size=(600, 600),
                              pos=(Window.center[0] - 550, Window.center[1] - 65))

        # Libraries
        libraries_button = DragLibBtn(source='data/images/libraries_portal.png',
                                      size_hint=(None, None),
                                      size=(300, 300),
                                      pos=(Window.center[0] - 200, Window.center[1] + 395))
        # Toggle Game State
        toggle_game_button = ToggleBtn(source='data/images/toggle_portal.png',
                                     size_hint=(None, None),
                                     size=(300, 300),
                                     pos=(Window.center[0] + 250, Window.center[1] + 65))
        # Deck
        deck_button = DeckBtn(source='data/images/deck_portal.png',
                              size_hint=(None, None),
                              size=(300, 300),
                              pos=(Window.center[0] - 250, Window.center[1] + 35))

        # Grave
        grave_button = GraveBtn(source='data/images/grave_portal.png',
                              size_hint=(None, None),
                              size=(300, 300),
                              pos=(Window.center[0] - 450, Window.center[1] + 95))

        # Bind the buttons to their respective methods
        exit_button.bind(on_release=DragBtn.allow_exit)  # Exit the app
        toggle_game_button.bind(on_release=ToggleBtn.toggle_state)  # Switch to game state
        libraries_button.bind(on_release=DragLibBtn.lib_popup)  # Popup on release
        deck_button.bind(on_release=DeckBtn.deck_popup_behavior)  # Popup on release
        grave_button.bind(on_release=GraveBtn.grave_popup_behavior)  # Popup on release

        # Use .bind to make the buttons movable
        exit_button.bind(on_touch_move=DragBtn.on_touch_move_action)
        toggle_game_button.bind(on_touch_move=ToggleBtn.on_touch_move_action)
        libraries_button.bind(on_touch_move=DragLibBtn.on_touch_move_action)
        deck_button.bind(on_touch_move=DeckBtn.on_touch_move_action)
        grave_button.bind(on_touch_move=GraveBtn.on_touch_move_action)

        # Add the buttons to the main_widget
        main_widget.add_widget(exit_button)
        main_widget.add_widget(toggle_game_button)
        main_widget.add_widget(libraries_button)
        main_widget.add_widget(deck_button)
        main_widget.add_widget(grave_button)

        self.menu_buttons = [exit_button, toggle_game_button, libraries_button]
        self.game_buttons = [toggle_game_button, deck_button, grave_button]

        # Call toggle_state to show/hide appropriate buttons for given state
        toggle_game_button.toggle_state()


if __name__ == '__main__':
    PlanarPortalApp().run()
