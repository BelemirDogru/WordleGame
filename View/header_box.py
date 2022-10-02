from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from View.title import Title

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\header_box.kv")


class HeaderBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Title())
