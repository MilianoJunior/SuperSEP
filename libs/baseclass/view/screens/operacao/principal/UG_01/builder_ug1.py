# from libs.baseclass.view.factory.builder_layout import BuilderLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.state_variable import StateVariable
from libs.baseclass.assets.color import cores
from libs.baseclass.view.screens.operacao.principal.UG_01.widgets import Power,Temperatures,Lubrification,Gauge
# from libs.baseclass.view.widgets.gauge import Gauge
from desempenho import Desempenho
from os import getpid

s1 = Desempenho()
var =  StateVariable()


class BuilderUG01(MDFloatLayout):
    '''
    Description: Layout
    -----------
        Composto por widgets da interface principal
    '''

    def __init__(self,name,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.name = name

    def __call__(self):
        try:
            # criar o layout main
            # main = MDFloatLayout()
            box1_gauge = MDBoxLayout(orientation='vertical',md_bg_color=cores['background'],
                                     size_hint=(.2,1),pos_hint={'x':0,'y':0},padding=[0,0,10,0])
            box2_card_power = MDBoxLayout(orientation='vertical',md_bg_color=cores['background'],
                                          size_hint=(.35,1),pos_hint={'x':.2,'y':0},padding=[0,0,10,0])
            box3_card_temperature = MDBoxLayout(orientation='vertical',md_bg_color=cores['background'],
                                                size_hint=(.225,1),pos_hint={'x':.55,'y':0},padding=[0,0,10,10])
            box4_card_lubrification = MDBoxLayout(orientation='vertical',md_bg_color=cores['background'],
                                                  size_hint=(.225,1),pos_hint={'x':.775,'y':0},padding=[0,0,10,10])
            # Componentes
            gauge = Gauge(name='gauge')()
            #-----------------------
            s1.instance_time('power')
            s1.memory_size(getpid(),'power')
            power = Power(name='power')()
            s1.instance_time('power')
            s1.memory_size(getpid(),'power')
            s1.grafico()
            # 1 name : power
            # 1 tempo : 2.058992385864258
            # 1 desempenho : 1.1424250602722168
            # 1 memoria : 220.23828125
            # 1 custo : 7.109375
            #-----------------------------
            # 0 name : power
            # 0 tempo : 0.902742862701416
            # 0 desempenho : 0.902742862701416
            # 0 memoria : 213.01953125
            # 0 custo : 213.01953125

            # 1 name : power
            # 1 tempo : 2.132324457168579
            # 1 desempenho : 1.229581594467163
            # 1 memoria : 226.875
            # 1 custo : 13.85546875
            #-------------------------------
            temperatures = Temperatures(name='temperatures')()
            lubrification = Lubrification(name='lubrification')()

            box1_gauge.add_widget(gauge)
            box2_card_power.add_widget(power)
            box3_card_temperature.add_widget(temperatures)
            box4_card_lubrification.add_widget(lubrification)

            self.add_widget(box1_gauge)
            self.add_widget(box2_card_power)
            self.add_widget(box3_card_temperature)
            self.add_widget(box4_card_lubrification)
            # s1.instance_time('19-UG-01')
            # s1.memory_size(getpid(),'UG-01')
            return self

        except Exception as e:
            raise NotImplementedError(self.__class__.__name__ + str(e))

        return self
    def on_size(self, *args):
        print('-----------------')
        print('Builder UG01', args)
        print('----------------')