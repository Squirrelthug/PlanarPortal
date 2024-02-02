# from WotC import Magic
# from commonsense import Nothing
# from myopinion import DGAF
# print("If you're a wizard,and you're reading this, GFY.")


# Import necessary modules
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# Define the main application class
# class PlanarPortal(App):
#     def build(self):
#         # Create a grid layout with two columns
#         layout = GridLayout(cols=2)
#
#         # Create a button and add it to the layout
#         button = Button(text='Import Card Library')
#         layout.add_widget(button)
#
#         # Create a label and add it to the layout
#         label = Label(text='Welcome to Planar Portal')
#         layout.add_widget(label)
#
#         # Return the layout
#         return layout

class PlanarPortal(App):
    def build(self):
        # Initialize the game board and add the menu button
        menu_button = Button(text='Menu')
        menu_button.bind(on_release=self.show_menu)

        return menu_button

    def show_menu(self, instance):
        # Create an instance of the Menu class and display the menu
        menu = Menu()
        menu.show()

# Run the application
if __name__ == '__main__':
    PlanarPortal().run()
