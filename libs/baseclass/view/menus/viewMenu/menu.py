from libs.baseclass.exception_error import Error
from libs.baseclass.view.factory.builder_layout import BuilderLayout
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.view.menus.viewMenu.properties import *
from libs.baseclass.view.menus.viewMenu.methods import *
from libs.baseclass.view.menus.viewMenu.widgets.widgets import *
from libs.baseclass.state_variable import StateVariable
from libs.baseclass.utils.layout_supersep import *
from kivy.core.window import Window
# from desempenho import Desempenho
# import os

var =  StateVariable()
# s1 = Desempenho()

class Menu(BuilderLayout):
    '''
    Description: Layout
    -----------
        Composto por outros 3 layouts: Menu, SideBar, Footer
    '''
    name = None

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.error = Error(self,'MenuLayout')
        
    def __call__(self):
        try:
            # layout main
            main = MDBoxLayout(orientation='horizontal',
                               md_bg_color = cores['background'],adaptive_size= True) 
            #----------
            logo_layout = MDBoxLayout(md_bg_color = color_logo)        # 1 Logo .2
            links_layout = MDBoxLayout(md_bg_color = color_links)        # 2 Menu -. 4
            icons_layout = MDBoxLayout(md_bg_color = color_icons)       # 3 settings icons . 4
            #-----------
            logo = Logo(name='logo')()
            principal = MenuPrincipal(name='principal')()
            icons_config = CardMenu(name='icons config')()
            menu_mobile = MenuMobile(name='menu mobile')()
            #-----------
            logo_layout.add_widget(logo)
            links_layout.add_widget(principal)
            icons_layout.add_widget(icons_config)
            #-----------
            var.register_change(main,menu1_properties)    
            var.register_change(logo_layout,logo1_properties)
            var.register_change(icons_layout,icons1_properties)
            var.register_change(links_layout,links1_properties)
            var.register_remove_add(main,[logo_layout,links_layout,icons_layout],[menu_mobile], remove_logo)
            #----------
            main.add_widget(logo_layout)
            main.add_widget(links_layout)
            main.add_widget(icons_layout)
            
            # s1.instance_time('6-Menu')
            # s1.memory_size(os.getpid(),'Menu')
            return main
            
        except Exception as e:
            self.error.msg(e)
            
        return self
    def resize_screen(self,*args):
        Window.system_size = [290,620]
