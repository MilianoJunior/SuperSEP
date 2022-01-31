from libs.baseclass.exception_error import Error
from libs.baseclass.view.factory.builder_layout import BuilderLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


widgets = ['gauge','button-emergency','card-power','card-temperature','card-lubrication']
           
class ViewUG01(Screen):
    '''
    Description: Layout
    -----------
        Composto por outros 3 layouts: Menu, SideBar, Footer
    '''
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.error = Error(self,'PrincipalLayout')
    def __call__(self):
        try:
            # criar o layout main
            main = MDFloatLayout()
            main.add_widget(Button(text='UG01'))
            self.add_widget(main)
            return self
            
        except Exception as e:
            self.error.msg(e)
            
        return self
