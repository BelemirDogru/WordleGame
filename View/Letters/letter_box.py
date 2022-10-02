from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\Letters\\kv\\letter_box.kv")


class LetterBox(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "BELEMİR"



