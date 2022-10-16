import requests
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random

Window.size=(700,800)
Builder.load_file('animation.kv')

class MyLayout(Widget):
    pass

restaurants = ['1', '2']
picdict = {'1':'photo.jpeg', '2':'photo2.jpeg'}
textdict = {'1':'this is the first restaurant', '2':'this is the second restaurant'}

class LoopApp(App):
    test_image = StringProperty()
    test_text = StringProperty()

    yeslist = []
    nolist = []

    def info(self):
        selection = random.choice(restaurants)
        restaurants.remove(selection)
        self.test_image = picdict[selection]
        self.test_text = textdict[selection]

    def yesnextimage(self):
        selection = random.choice(restaurants)
        # yeslist.append(selection)
        restaurants.remove(selection)
        self.test_image = picdict[selection]
        self.test_text = textdict[selection]

    def nonextimage(self):
        selection = random.choice(restaurants)
        # nolist.append(selection)
        restaurants.remove(selection)
        self.test_image = picdict[selection]
        self.test_text = textdict[selection]
    
    def build(self):
        return MyLayout()

if __name__=='__main__':
    LoopApp().run()