from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from View.keyboard import Keyboard, SpaceBox

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\keyboard_box.kv")


class KeyboardBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(SpaceBox())
        self.add_widget(Keyboard())
        self.add_widget(SpaceBox())





