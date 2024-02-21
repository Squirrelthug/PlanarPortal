# Import necessary modules from Kivy
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder

# Load Kivy string for DraggableButton
Builder.load_string('''
<ExitButton>:
    on_press: self.on_press_action()  # Bind on_press event to on_press_action method
    on_touch_move: self.on_touch_move_action(args[1])  # Bind on_touch_move event to on_touch_move_action method
''')

# Define ExitButton class which inherits from Kivy's Button class
class ExitButton(Button):
    def __init__(self, **kwargs):
        super(ExitButton, self).__init__(**kwargs)
        self.button_moved = False  # Flag to check if button was moved
        self.initial_pos = None  # Store initial position of button

    # Method to handle on_press event
    def on_press_action(self):
        self.initial_pos = self.pos  # Store initial position when button is pressed
        print("Button pressed")

    # Method to handle on_touch_move event
    def on_touch_move_action(self, touch):
        # If touch event is within button
        if self.collide_point(*touch.pos):
            print("Button dragged")
            self.center = touch.pos  # Update button position to touch position
            # If button position is different from initial position, set button_moved flag to True
            if self.initial_pos != touch.pos:
                self.button_moved = True

    # Method to handle on_release event
    def on_release_action(self):
        self.button_moved = False  # Reset button_moved flag when button is released
        print("Button released")

    # Method to handle exit action
    def allow_exit(self):
        print("button_moved status: ", self.button_moved)
        # If button was moved, reset button_moved flag and return
        if self.button_moved:
            self.button_moved = False
            return
        # If button was not moved, stop the app
        app = App.get_running_app()
        app.stop()

# Define MyApp class which inherits from Kivy's App class
class MyApp(App):
    def build(self):
        return ExitButton(text="Drag or Tap")  # Return an instance of ExitButton as root widget

# Main function to run the app
if __name__ == '__main__':
    MyApp().run()