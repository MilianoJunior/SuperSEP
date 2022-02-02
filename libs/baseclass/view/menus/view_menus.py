from libs.baseclass.view.menus.viewMenu.menu import Menu
from libs.baseclass.view.menus.viewSideBar.sidebar import SideBar
from libs.baseclass.view.menus.viewMenuLateral.menu_lateral import MenuLateral
from kivymd.uix.floatlayout import MDFloatLayout
# from desempenho import Desempenho
# from os import getpid

# s2 = Desempenho()

class ViewMenus(MDFloatLayout):
    '''
    Description: Layout
    -----------
        Composto por outros 3 layouts: Menu, SideBar, Footer
    '''

    def __init__(self,name, *args,**kwargs):
        super().__init__(*args,**kwargs)

    def __call__(self):
        try:
            menu = Menu(name='Menu_SuperSEP')()
            sidebar = SideBar(name='SideBar_SuperSEP')()
            menuLateral = MenuLateral(name='Menu_Lateral_SuperSEP')()
#
            self.add_widget(menu)
            self.add_widget(sidebar)
            self.add_widget(menuLateral)

            # s2.instance_time('5-ViewMenus')
            # s2.memory_size(getpid(),'ViewMenus')
            return self

        except Exception as e:
            print('ViewMenus: ',e)

        return self

