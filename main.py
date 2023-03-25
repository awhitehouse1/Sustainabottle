from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class MyApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        t = TextInput(font_size=25,
                      size_hint_y=None,
                      height=50)
        f = FloatLayout()
        s = Scatter()

        l = Label(text="Hello !",
                  font_size=50)

        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t)
        b.add_widget(f)

        t.bind(text=l.setter('text'))

        return b
        #return Label(text = 'Hello World')



class MainWidget(Widget):
    pass

class WaterApp(App):
    pass

WaterApp().run()