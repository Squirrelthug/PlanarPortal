# from WotC import Magic
# from commonsense import Nothing
# from myopinion import DGAF
# print("If you're a wizard,and you're reading this, GFY.")
# Import necessary modules
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Line, Color
from kivy.uix.widget import Widget
from btn_dir.home_libraries_portal import DraggableLibraryButton as DragLibBtn
from btn_dir.game_deck_portal import GameDeckPortal as DeckBtn
from common.button_behaviors import DraggableButton as DragBtn

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


class PlanarPortalApp(App):
    def __init__(self, **kwargs):
        super(PlanarPortalApp, self).__init__(**kwargs)

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)    # Black background
        Window.fullscreen = 'auto'          # Full screen mode
        main_widget = Widget()

        playmat = Playmat()                 # Create a new playmat for grid from playmat class
        main_widget.add_widget(playmat)     # Add the playmat to the main widget

        # Exit                              # CREATE BUTTONS
        exit_button = DragBtn(text='Exit',
                              size_hint=(None, None),
                              size=(300, 150),
                              pos=(70, Window.height - 10))

        # Refresh
        refresh_button = DragBtn(text='Refresh',
                                 size_hint=(None, None),
                                 size=(100, 50),
                                 pos=(20, Window.height - 100))
        # Start Game
        start_game_button = DragBtn(text='Start Game',
                                    size_hint=(None, None),
                                    size=(300, 150),
                                    pos=(250, Window.height - 20))
        # Deck
        deck_button = DeckBtn(text='Deck',
                                   size_hint=(None, None),
                                   size=(300, 150),
                                   pos=(1600, Window.height - 140))
        # Libraries
        libraries_button = DragLibBtn(text='Libraries',
                                   size_hint=(None, None),
                                   size=(300, 150),
                                   pos=(1200, Window.height - 90))

        # Bind the buttons to their respective methods
        refresh_button.bind(on_press=lambda x: playmat.draw_grid())         # Refresh the grid
        libraries_button.bind(on_release=DragLibBtn.lib_popup)              # Popup on release
        exit_button.bind(on_press=lambda x: App.get_running_app().stop())   # Exit the app
        deck_button.bind(on_release=DeckBtn.deck_popup_behavior)                     # Popup on release

        # Use .bind to make the buttons movable
        refresh_button.bind(on_touch_move=DragBtn.on_touch_move_action)
        libraries_button.bind(on_touch_move=DragLibBtn.on_touch_move_action)
        start_game_button.bind(on_touch_move=DragBtn.on_touch_move_action)
        deck_button.bind(on_touch_move=DeckBtn.on_touch_move_action)

        # Add the buttons to the main_widget
        main_widget.add_widget(exit_button)
        main_widget.add_widget(refresh_button)
        main_widget.add_widget(start_game_button)
        main_widget.add_widget(libraries_button)
        main_widget.add_widget(deck_button)

        return main_widget

if __name__ == '__main__':
    PlanarPortalApp().run()
