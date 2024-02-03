from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class LibraryPopup:
    def __init__(self):
        # Initialize the popup
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Libraries Imported: \n\nLibrary 1\nLibrary 2'))  # Replace with actual libraries
        layout.add_widget(Button(text='Import', size_hint=(None, None), size=(100, 50)))  # This button will be linked to the import functionality
        self.popup = Popup(title='Libraries', content=layout, size_hint=(None, None), size=(400, 400))

    def show(self):
        # Display the popup
        self.popup.open()

    def update_libraries(self, libraries):
        # Update the list of libraries
        self.popup.content.children[1].text = 'Libraries Imported: \n\n' + '\n'.join(libraries)
