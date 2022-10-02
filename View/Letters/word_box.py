from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from View.Letters.letter_box import LetterBox
from View.border_box import BorderBox

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\Letters\\kv\\word_box.kv")


class WordBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_letter_boxes()

    def add_letter_boxes(self):
        for i in range(5):
            self.add_widget(BorderBox())

