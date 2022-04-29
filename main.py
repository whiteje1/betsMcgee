from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from classes.loginPage import loginPage

class betsApp(App):
    def build(self):
        # print(loginPage.submit(self))
        return loginPage.buildLogin(self)

betsApp().run()
