from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder

Builder.load_file("C:\\Users\\dell\\PycharmProjects\\WordleGame\\View\\kv\\keyboard.kv")


class SpaceBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (.30,.30)



class Keyboard(StackLayout):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
       self.size_hint = (1.40, 1)
       for i in range(33):
           if i == 23:
               btn = Button(text="ENTER", width=60, height=40, size_hint=(None, None))
               self.add_widget(btn)
           elif i == 32:
               btn = Button(text="DEL", width=60, height=40, size_hint=(None, None))
               self.add_widget(btn)
           elif i ==10:
               space = Label(text="  ", width=20, height=40, size_hint=(None, None))
               self.add_widget(space)
           elif i == 22:
               space = Label(text="  ", width=20, height=40, size_hint=(None, None))
               self.add_widget(space)
           elif 10 < i < 22:
               btn = Button(text="A", width=37, height=40, size_hint=(None, None))
               self.add_widget(btn)

           else:
               btn = Button(text="A", width=50, height=40, size_hint=(None, None))
               self.add_widget(btn)









