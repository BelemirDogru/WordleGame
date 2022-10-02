from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from View.header_box import HeaderBox
from View.keyboard_box import KeyboardBox
from View.wordle_box import WordleBox

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\main_box.kv")


class MainBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(HeaderBox())
        self.add_widget(WordleBox())
        self.add_widget(KeyboardBox())
