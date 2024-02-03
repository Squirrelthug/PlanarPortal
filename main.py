# from WotC import Magic
# from commonsense import Nothing
# from myopinion import DGAF
# print("If you're a wizard,and you're reading this, GFY.")
# Import necessary modules
from kivy.app import App
from kivy.core.window import Window
from kivy.graphics import Line, Color
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from common.library_popup import LibraryPopup


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
        self.button_moved = False
        self.initial_pos = None

    def on_button_move(self, instance, touch):
        self.initial_pos = instance.pos
        if instance.collide_point(*touch.pos):
            instance.center = touch.pos

    def show_libraries(self, instance):     # Show the libraries popup
        self.library_popup.show()

    def timed_popup(self, instance):        # Schedule the libraries popup
        if self.button_moved:               # Check if the button was moved
            return                          # If it was, return immediately without scheduling show_libraries
        self.show_libraries(instance)       # Otherwise, initiate the show_libraries method
        self.button_moved = False           # Reset the flag to False

    def build(self):
        Window.clearcolor = (0, 0, 0, 1)    # Black background
        Window.fullscreen = 'auto'          # Fullscreen mode
        main_widget = Widget()

        playmat = Playmat()                 # Create a new playmat for grid from playmat class
        main_widget.add_widget(playmat)     # Add the playmat to the main widget

        # CREATE BUTTONS
        # Exit
        exit_button = Button(text='Exit',
                             size_hint=(None, None),
                             size=(300, 150),
                             pos=(70, Window.height - 10))

        # Refresh
        refresh_button = Button(text='Refresh',
                                size_hint=(None, None),
                                size=(100, 50),
                                pos=(20, Window.height - 100))
        # Start Game
        start_game_button = Button(text='Start Game',
                                   size_hint=(None, None),
                                   size=(300, 150),
                                   pos=(250, Window.height - 20))
        # Libraries
        libraries_button = Button(text='Libraries',
                                  size_hint=(None, None),
                                  size=(300, 150),
                                  pos=(1200, Window.height - 90))

        # Bind the buttons to their respective methods
        refresh_button.bind(on_press=lambda x: playmat.draw_grid())         # Refresh the grid
        libraries_button.bind(on_release=self.timed_popup)                  # Delayed popup
        exit_button.bind(on_press=lambda x: App.get_running_app().stop())   # Exit the app

        # Use .bind to make the buttons movable
        refresh_button.bind(on_touch_move=self.on_button_move)
        libraries_button.bind(on_touch_move=self.on_button_move)
        start_game_button.bind(on_touch_move=self.on_button_move)

        # Add the buttons to the main_widget
        main_widget.add_widget(exit_button)
        main_widget.add_widget(refresh_button)
        main_widget.add_widget(start_game_button)
        main_widget.add_widget(libraries_button)

        # Libraries popup
        self.library_popup = LibraryPopup()

        return main_widget

if __name__ == '__main__':
    PlanarPortalApp().run()
