from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_string('''
<GameDeckButton>:
    on_press: self.on_press_action()
    on_touch_move: self.on_touch_move_action(args[1])
''')


class DeckOptionsPopup:
    def __init__(self):
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Deck Options: \n\n'
                                     'Draw (x) cards [to hand]\n'
                                     'Discard (x) cards to graveyard\n'
                                     'Draw (x) cards to board [default facedown]'))
        layout.add_widget(Button(text='Import',
                                 size_hint=(None, None),
                                 size=(100, 50)))
        self.popup = Popup(title='Deck Options',
                           content=layout,
                           size_hint=(None, None),
                           size=(400, 400))

    def show(self):
        # Display the popup
        self.popup.open()


class GameDeckButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(GameDeckButton, self).__init__(**kwargs)
        self.button_moved = False
        self.initial_pos = None
        self.deck_popup = DeckOptionsPopup()

    def on_press(self):
        self.on_press_action()

    def on_press_action(self):
        self.initial_pos = self.pos
        print("Deck button pressed")

    def on_touch_move_action(self, touch):
        if self.collide_point(*touch.pos):
            print("Deck Button dragged")
            # Update button position or perform drag action
            self.center = touch.pos
            if self.initial_pos != touch.pos:
                self.button_moved = True

    def on_release_action(self):
        self.button_moved = False           # Reset the button_moved flag
        print("Deck Button released")

    def deck_popup_behavior(self):
        print("deck_button_moved status: ", self.button_moved)
        if self.button_moved:               # Check if the button was moved
            self.button_moved = False       # If it was, reset the button_moved flag
            return                          # And, return immediately without triggering the popup
        self.deck_popup.show()              # Otherwise, initiate the deck options popup
        self.on_release_action()


class MyApp(App):
    def build(self):
        return GameDeckButton(text="Drag or Tap")


if __name__ == '__main__':
    MyApp().run()
