from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from View.Letters.word_box import WordBox

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\wordle_box.kv")


class WordleBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_word_boxes()

    def add_word_boxes(self):
        for i in range(6):
            self.add_widget(WordBox())

