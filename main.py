from kivy.app import App
from kivy.properties import StringProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget



class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("1")
    text_input_str = StringProperty("1")
    def on_button_click(self):
        print("button clicked")
    def on_text_validate(self, widget):
        self.text_input_str = widget.text

class MainWidget(Widget):
    pass

class WaterApp(App):
    pass

WaterApp().run()