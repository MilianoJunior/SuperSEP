from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.view.menus.viewMenuLateral.properties import menu_lateral_properties
from libs.baseclass.view.menus.viewMenuLateral.widgets import NavegationMenu
from libs.baseclass.state_variable import StateVariable
# from desempenho import Desempenho
# from os import getpid

# s1 = Desempenho()
var =  StateVariable()


class MenuLateral(MDBoxLayout):
    '''
    Description: Layout
    -----------
        Composto por widgets
    '''
    name = None
    
    def __init__(self,name, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name = name

        
    def __call__(self):

        var.register_change(self,menu_lateral_properties)
        menu = NavegationMenu(name='navigation')()
        self.add_widget(menu)
        
        # s1.instance_time('16-MenuLateral')
        # s1.memory_size(getpid(),'MenuLateral')
        return self
            


