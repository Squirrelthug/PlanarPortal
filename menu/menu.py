from kivy.uix.popup import Popup
from kivy.uix.label import Label

class Menu:
    def __init__(self):
        # Initialize the menu
        self.popup = Popup(title='Menu', content=Label(text='Menu Content'), size_hint=(None, None), size=(400, 400))

    def show(self):
        # Display the menu
        self.popup.open()