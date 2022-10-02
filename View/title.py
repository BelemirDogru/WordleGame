from kivy.uix.label import Label
from kivy.lang import Builder
Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\title.kv")


class Title(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

