# step 1: create the app
# step 2: create the interface


from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import random


class FLoating(FloatLayout):
    pass

class Relative_Practice(FloatLayout):
    pass
class TestApp(App):
    pass

class Scroller():
    pass


class StackInterface(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for i in range(500):
            a = random.random()+.2
            b=random.random()-.2
            c=random.random()+.2
            d=random.random()+.2
            b1 = Button(text= f'{i}', size_hint= (None,None),background_normal='',background_color=(a,b,c,d), size =(100,100))
            self.add_widget(b1)






class Interface(AnchorLayout):
    pass


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
