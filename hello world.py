# step 1: create the app
# step 2: create the interface

from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button



class TestApp(App):
    pass




class Interface(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        b1 = Button(text = "nigga",size_hint =(.34,.30))

        self.add_widget(b1)


def color_coverter(x):
    y = 0.00392156863
    return x * y
def color_converter(red,green,blue):
    red=color_coverter(red)
    green=color_coverter(green)
    blue=color_coverter(blue)
    print(f"red: {red},green: {green},blue: {blue}")

# color_converter(36,34,34)
TestApp().run()
