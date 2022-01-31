from libs.baseclass.exception_error import Error
from libs.baseclass.view.menus.viewMenu.menu import Menu
from libs.baseclass.view.menus.viewSideBar.sidebar import SideBar
from libs.baseclass.view.menus.viewMenuLateral.menu_lateral import MenuLateral
from libs.baseclass.view.factory.builder_layout import BuilderLayout
from kivymd.uix.floatlayout import MDFloatLayout
from libs.baseclass.state_variable import StateVariable

var =  StateVariable()

widgets_ug01 = ['gauge','button-emergency','card-power','card-temperature','card-lubrication']

class BuilderUG01(BuilderLayout):
    '''
    Description: Layout
    -----------
        Composto por widgets da interface principal
    '''
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.error = Error(self,'MenuLayout')
        
    def __call__(self):
        try:
            # criar o layout main
            main = MDFloatLayout()

            return main
            
        except Exception as e:
            self.error.msg(e)
            
        return self
