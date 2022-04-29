from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from classes.logincodes import LoginControl
from classes.logincodes import AfterLogin

class FormControl(AnchorLayout):
    '''
    classdocs
    '''

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        super(FormControl,self).__init__(**kwargs)
        c= LoginControl()
        c.setparent(self)
        self.add_widget(c)

    def changewidget(self,to):
        if to == 'AfterLogin':
            self.clear_widgets()
            self.add_widget(AfterLogin())
