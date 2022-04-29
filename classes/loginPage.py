from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class loginPage(App):
    def buildLogin(self):
        layout = GridLayout(
            cols=1,
            pos_hint= {'top':.75, 'right':1.35}
        )
        inLayout = GridLayout(
            rows = 7,
            cols = 1,
            width = 100,
            row_default_height = 20,
            spacing = 10,
            padding = 10
        )

        title = Label(
            text="BETS WITH FRIENDS",
            font_size = 30,
            size_hint=(None, None)
        )
        title.bind(texture_size=title.setter('size'))

        prompt = Label(
            text="Login",
            font_size = 25,
            size_hint=(None, None)
        )
        prompt.bind(texture_size=prompt.setter('size'))

        usernameLabel = Label(
            text="Username",
            font_size = 20,
            size_hint=(None, None)
        )
        usernameLabel.bind(texture_size=usernameLabel.setter('size'))

        self.username = TextInput(
            size_hint =(None, None),
            height = 30,
            width = 200
        )

        passwordLabel = Label(
            text="Password",
            font_size = 20,
            size_hint=(None, None)
        )
        passwordLabel.bind(texture_size=passwordLabel.setter('size'))
        self.password = TextInput(
            size_hint =(None, None),
            height = 30,
            width = 200
        )
        submit = Button(
            text = 'Submit',
            on_press=self.submit,
            size_hint =(None, None),
            height = 30,
            width = 70
        )

        inLayout.add_widget(title)
        inLayout.add_widget(prompt)
        inLayout.add_widget(usernameLabel)
        inLayout.add_widget(self.username)
        inLayout.add_widget(passwordLabel)
        inLayout.add_widget(self.password)
        inLayout.add_widget(submit)

        layout.add_widget(inLayout)
        return layout

    def submit(self, obj):
        print('username: ' + self.username.text)
        print('password: ' + self.password.text)
