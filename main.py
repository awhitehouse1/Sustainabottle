from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget



class BoxLayoutExample(BoxLayout):
    def on_button_click(self):
        print("button clicked")

class MainWidget(Widget):
    pass

class TextInput(Widget):
    pass

class WaterApp(App):
    pass

WaterApp().run()