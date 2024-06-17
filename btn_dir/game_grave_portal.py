from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string('''
<GameGraveButton>:
    on_press: self.on_press_action()
    on_touch_move: self.on_touch_move_action(args[1])
''')


class GraveOptionsPopup:
    def __init__(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Graveyard Options: \n\n'
                                     'Draw (x) cards [to hand]\n'
                                     'Exile (x) cards from game'))
        layout.add_widget(Button(text='Shuffle',
                                 size_hint=(None, None),
                                 size=(100, 50)))
        self.popup = Popup(title='Graveyard Options',
                           content=layout,
                           size_hint=(None, None),
                           size=(400, 400))

    def show(self):
        # Display the popup
        self.popup.open()


class GameGraveButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(GameGraveButton, self).__init__(**kwargs)
        self.button_moved = False
        self.initial_pos = None
        self.grave_popup = GraveOptionsPopup()

    def on_press(self):
        self.on_press_action()

    def on_press_action(self):
        self.initial_pos = self.pos
        print("Grave button pressed")

    def on_touch_move_action(self, touch):
        if self.collide_point(*touch.pos):
            print("Grave Button dragged")
            # Update button position or perform drag action
            self.center = touch.pos
            if self.initial_pos != touch.pos:
                self.button_moved = True

    def on_release_action(self):
        self.button_moved = False           # Reset the button_moved flag
        print("Grave Button released")

    def grave_popup_behavior(self):
        print("grave_button_moved status: ", self.button_moved)
        if self.button_moved:               # Check if the button was moved
            self.button_moved = False       # If it was, reset the button_moved flag
            return                          # And, return immediately without triggering the popup
        self.grave_popup.show()              # Otherwise, initiate the deck options popup
        self.on_release_action()


class MyApp(App):
    def build(self):
        return GameGraveButton(text="Drag or Tap")


if __name__ == '__main__':
    MyApp().run()
