from libs.baseclass.exception_error import Error
from libs.baseclass.view.factory.builder_layout import BuilderLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.state_variable import StateVariable
from libs.baseclass.assets.color import *
from libs.baseclass.view.screens.operacao.principal.UG_02.widgets import Gauge,Power,Temperatures,Lubrification
# from desempenho import Desempenho
# from os import getpid
# s1 = Desempenho()
var =  StateVariable()

widgets_ug01 = ['gauge','button-emergency','card-power','card-temperature','card-lubrication']

class BuilderUG02(BuilderLayout):
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
            box1_gauge = MDBoxLayout(orientation='vertical',md_bg_color=cores['background'],
                                     size_hint=(.2,1),pos_hint={'x':0,'y':0},padding=[0,0,10,10])
            # box2_card_inputs = MDBoxLayout(orientation='vertical',md_bg_color=cores['background_widget'],
            #                                size_hint=(.2,1),pos_hint={'x':.2,'y':0},padding=[0,0,10,10])
            box2_card_power = MDBoxLayout(orientation='vertical',md_bg_color=cores['background'],
                                          size_hint=(.35,1),pos_hint={'x':.2,'y':0},padding=[0,0,10,10])
            box3_card_temperature = MDBoxLayout(orientation='vertical',md_bg_color=cores['background'],
                                                size_hint=(.225,1),pos_hint={'x':.55,'y':0},padding=[0,0,10,10])
            box4_card_lubrification = MDBoxLayout(orientation='vertical',md_bg_color=cores['background'],
                                                  size_hint=(.225,1),pos_hint={'x':.775,'y':0},padding=[0,0,10,10])
            # Componentes
            gauge = Gauge(name='gauge')()
            power = Power(name='power')()
            temperatures = Temperatures(name='temperatures')()
            lubrification = Lubrification(name='lubrification')()
            
            box1_gauge.add_widget(gauge)
            box2_card_power.add_widget(power)
            box3_card_temperature.add_widget(temperatures)
            box4_card_lubrification.add_widget(lubrification)
            
            main.add_widget(box1_gauge)
            main.add_widget(box2_card_power)
            main.add_widget(box3_card_temperature)
            main.add_widget(box4_card_lubrification)
            
            # s1.instance_time('24-UG-02')
            # s1.memory_size(getpid(),'UG-02')
            return main
            
        except Exception as e:
            self.error.msg(e)
            
        return self


