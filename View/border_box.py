from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from View.border_color_box import BorderColorBox

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\border_box.kv")


class BorderBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(BorderColorBox())
