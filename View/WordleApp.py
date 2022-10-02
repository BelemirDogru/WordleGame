from kivy.uix.anchorlayout import AnchorLayout
from kivy.app import App
from kivy.lang import Builder

from View.main_box import MainBox

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\wordle.kv")


class Wordle(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(MainBox())

class WordleApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return Wordle()


if __name__ == "__main__":
    WordleApp().run()
