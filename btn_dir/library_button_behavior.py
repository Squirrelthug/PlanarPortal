from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup

Builder.load_string('''
<DraggableButton>:
    on_press: self.on_press_action()
    on_touch_move: self.on_touch_move_action(args[1])
''')


class LibraryPopup:
    def __init__(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='lib_list(): \n\nlib\nlib'))   # Replace with actual libraries
        layout.add_widget(Button(text='Import',
                                 size_hint=(None, None),
                                 size=(100, 50)))
        self.popup = Popup(title='Libraries',
                           content=layout,
                           size_hint=(None, None),
                           size=(400, 400))

    def show(self):
        # Display the popup
        self.popup.open()


class DraggableLibraryButton(Button):
    def __init__(self, **kwargs):
        super(DraggableLibraryButton, self).__init__(**kwargs)
        self.button_moved = False
        self.initial_pos = None
        self.library_popup = LibraryPopup()

    def on_press_action(self):
        self.initial_pos = self.pos
        print("Library Button pressed")

    def on_touch_move_action(self, touch):
        if self.collide_point(*touch.pos):
            print("Library Button dragged")
            # Update button position or perform drag action
            self.center = touch.pos
            if self.initial_pos != touch.pos:
                self.button_moved = True

    def on_release_action(self):
        self.button_moved = False           # Reset the button_moved flag
        print("Library Button released")

    def lib_popup(self):
        print("button_moved status: ", self.button_moved)
        if self.button_moved:               # Check if the button was moved
            self.button_moved = False       # If it was, reset the button_moved flag
            return                          # If it was, return immediately without scheduling show_libraries
        self.library_popup.show()           # Otherwise, initiate the show_libraries method
        self.on_release_action()


class MyApp(App):
    def build(self):
        return DraggableLibraryButton(text="Drag or Tap")


if __name__ == '__main__':
    MyApp().run()
