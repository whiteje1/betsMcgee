from kivy.uix.gridlayout import GridLayout


class LoginControl(GridLayout):
    _parentwidget=None

    def __init__(self, **kwargs):
        super(LoginControl,self).__init__(**kwargs)
        self.userid.text='Welcome'

    def setparent(self,parent):
        self._parentwidget=parent

    def changewidget(self,to):
        self._parentwidget.changewidget(to)

    def login_pressed(self,button):
        print(button.text)
        print(self.userid.text)
        print(self.userpw.text)
        self.changewidget('AfterLogin')

    def close_pressed(self,button):
        print(button.text)
        exit()


class AfterLogin(GridLayout):

    def __init__(self,**kwargs):
        super(AfterLogin,self).__init__(**kwargs)
