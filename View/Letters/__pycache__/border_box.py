from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\Letters\\__pycache__\\kv\\border_box.kv")


class BorderBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = 10
