from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from View.Letters.letter_box import LetterBox

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\border_color_box.kv")


class BorderColorBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(LetterBox())
