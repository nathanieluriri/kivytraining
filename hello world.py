# step 1: create the app
# step 2: create the interface

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button



class TestApp(App):
    pass




class Interface(GridLayout):
    pass


def color_coverter(x):
    y = 0.00392156863
    return x * y
def color_converter(red,green,blue):
    red=color_coverter(red)
    green=color_coverter(green)
    blue=color_coverter(blue)
    print(f"red: {red},green: {green},blue: {blue}")
TestApp().run()
