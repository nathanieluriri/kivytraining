# step 1: create the app
# step 2: create the interface

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button

class TestApp(App):
    pass

class Interface(Widget):
    def pressed(self):
        print("enter was pressed")
#         this function will be called any time enter is pressed because of the on text validate event




TestApp().run()