# from WotC import Magic
# from commonsense import Nothing
# from myopinion import DGAF
# print("If you're a wizard and you're reading this, GFY.")


import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label


class PlanarPortal(App):

    def build(self):
        return Label(text='Welcome to Planar Portal')


if __name__ == '__main__':
    PlanarPortal().run()
