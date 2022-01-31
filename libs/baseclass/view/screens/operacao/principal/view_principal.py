from libs.baseclass.view.screens.operacao.principal.UG_01.builder_ug1 import BuilderUG01
from libs.baseclass.view.screens.operacao.principal.UG_02.builder_ug2 import BuilderUG02
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.splitter import Splitter
# from libs.baseclass.assets.color import *
# from desempenho import Desempenho

# s1 = Desempenho()
widgets_ug02 = ['gauge','button-emergency','card-power','card-temperature','card-lubrication']
           
class ViewPrincipal(Screen):
    '''
    Description: Layout
    -----------
        Composto por outros 3 layouts: Menu, SideBar, Footer
    '''
    
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        # self.error = Error(self,'PrincipalLayout')
    def __call__(self):
        try:
            # criar o layout main--
            main = MDBoxLayout(orientation='vertical',spacing=2)
            splitter = Splitter(sizable_from = 'bottom')
            ug01 = BuilderUG01(name='ug01')()
            ug02 = BuilderUG02(name='ug02')()
            #----------------------------
            splitter.add_widget(ug02)
            main.add_widget(splitter)
            main.add_widget(ug01)
            self.add_widget(main)
            
            # s1.instance_time('18-Principal')
            return self
            
        except Exception as e:
            print('Erro View Principal: ',e)
            
        return self
    def on_size(self, *args):
        print('screen : ',args)
