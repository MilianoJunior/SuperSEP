from libs.baseclass.view.factory.builder_widget import BuilderWidgets
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.state_variable import StateVariable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.graphics import Color
from kivy.graphics import Line,Ellipse
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from libs.baseclass.assets.color import cores
from kivymd.uix.textfield import MDTextField
from kivy.animation import Animation
from kivy.properties import ListProperty
# from kivy.uix.image import Image
# from os import getpid
from os.path import join, abspath
# from desempenho import Desempenho--
from libs.baseclass.view.widgets.gauge import WGauge
from libs.baseclass.view.widgets.input_text import InputText
from libs.baseclass.view.widgets.button_emergency import ButtonEmergency
from libs.baseclass.view.widgets.tables import Tables
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.stacklayout import MDStackLayout

# s1 = Desempenho()

var =  StateVariable()

# Total picle Gauge-UG01:  326888
# Total picle Gauge-UG01:  93648

#local = join(PATH[0],'libs\\baseclass\\assets\\imagens\\emergecy.jpg')
# gauge = join(PATH[0],'libs\\baseclass\\assets\\imagens\\gauge.png')


class Gauge(MDFloatLayout):

    gauge = ListProperty([120, 810, 70, 0, 360])


    def __init__(self,name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = False
        self.name = name
        self.md_bg_color = cores['primary']
        self.radius = [15,15,15,15]



    def __call__(self):
        try:
            # layouts
            box_gauge = MDBoxLayout(orientation='vertical',
                                    md_bg_color = cores['widget'],
                                    size_hint=(1,.5),
                                    radius = [15,15,0,0],
                                    pos_hint={'x':0,'y':.5})
            box_input = MDBoxLayout(orientation='horizontal',
                                    md_bg_color = cores['widget'],
                                    size_hint=(1,.15),
                                    pos_hint={'x':0,'y':.35},
                                    padding=[20,0,20,0])
            box_emergency = MDBoxLayout(orientation='horizontal',
                                        md_bg_color = cores['background_widget'],
                                        size_hint=(1,.35),
                                        radius = [0,0,15,15],
                                        pos_hint={'x':0,'y': 0})
            # componentes
            gauge = WGauge(name='gauge_ug01')()

            input_power = InputText(name='potencia')()
            button = ButtonEmergency(name='button_emergency')()
            # composicao
            box_gauge.add_widget(gauge)
            box_input.add_widget(input_power)
            box_emergency.add_widget(button)

            self.add_widget(box_gauge)
            self.add_widget(box_input)
            self.add_widget(box_emergency)
            # bind
            # box_gauge.bind(pos=gauge.update_size)

            return self

        except Exception as e:
            raise NotImplementedError(self.__class__.__name__ + str(e))

        return self


dados_ug01_a = {

                'Fase R'          : [100,20],
                'Fase S'          : [300,30],
                'Fase T'          : [100,40],
                'Campo/Excitação' : [100,20],

    }

dados_ug01_b = {

                'Frequência'          : ['100','Hz'],
                'Potência ativa'      : ['300','kW'],
                'Potência reativa'    : ['100','kvar'],
                'Potência aparente'   : ['100','kva'],
                'Fator de potência'   : ['.9',''],
                'Destribuidor'        : ['80','%'],
                'Velocidade'          : ['100','RPM'],
      }
final = {
            'Acumulador': ['48','MW']

    }

data_cols = ['UG-01','Tensão','Corrente']
data_rows = {

                'Fase R'          : [100,20],
                'Fase S'          : [300,30],
                'Fase T'          : [100,40],
                'Campo/Excitação' : [100,20],

    }
class Power(BuilderWidgets):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        try:
            box = MDStackLayout(md_bg_color = cores['background'])
            table_power = Tables('power_a',data_cols=data_cols,data_rows=data_rows, height_custon=30)()
            # table_power.bind(pos=table_power.responsivo)
            # print('tabela power: ',table_power.size)

            table_info = Tables('power_b',data_rows=dados_ug01_b, height_custon=35)()
            # table_info.bind(pos=table_info.responsivo)
            table_grave = Tables('final',data_rows=final, height_custon=40)()

            box.add_widget(table_power)
            box.add_widget(table_info)
            box.add_widget(table_grave)

            return box

        except Exception as e:
            print(e)

        return self

temperature_ug01_a = {
                        'Enrol. fase A'  :['10 °C'],
                        'Enrol. fase B'  :['10 °C'],
                        'Enrol. fase C'  :['10 °C'],
                        'N. estator'     :['10 °C'],
                        'Excitatriz'     :['10 °C'],
                        'Cub. CS-U1'     :['10 °C'],
                    }

temperature_ug01_b = {
                        'Gula casquilo'  :['10 °C'],
                        'C. casquilo'    :['10 °C'],
                        'Comb. escora'   :['10 °C'],
                        'Contra escora'  :['10 °C'],
                        'UHRV óleo'      :['10 °C'],
                        'UHLM óleo'      :['10 °C'],

                    }
class Temperatures(BuilderWidgets):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __call__(self):
        try:
            # layouts
            box = MDStackLayout(md_bg_color = cores['background'])

            # widgets
            table_power = Tables('power_a',data_cols=['Temperaturas'],data_rows=temperature_ug01_a, height_custon=35)()
            table_info = Tables('power_b',data_rows=temperature_ug01_b, height_custon=35)()

            # composicao
            box.add_widget(table_power)
            box.add_widget(table_info)

            return box

        except Exception as e:
            print(e)

        return self


lubrification_a = {
                    'Unid. hid. oper.'   : ['circle-outline', True],
                    'Bomba 01 - Ligada'  : ['circle-outline', True],
                    'Bomba 02 - Ligada'  : ['circle-outline', True],
                    'Pressostato linha'  : ['circle-outline', True],
                    'Água tc. de calor'  : ['circle-outline', True],

    }

lubrification_b = {
                    'Unid. hid. oper.'  : ['circle-outline', True],
                    'Bomba 01 - Ligada' : ['circle-outline', True],
                    'Bomba 02 - Ligada' : ['circle-outline', True],
    }

class Lubrification(MDFloatLayout):

    def __init__(self,name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __call__(self):
        try:
            # layouts
            box_tabelas = MDBoxLayout(orientation='vertical',
                                    md_bg_color = cores['background'],
                                    size_hint=(1,.75),
                                    pos_hint={'x':0,'y':.25})
            box_gauge = MDBoxLayout(orientation='vertical',
                                    md_bg_color = cores['background'],
                                    size_hint=(1,.35),
                                    pos_hint={'x':0,'y':.0})
            box = MDStackLayout(md_bg_color = cores['background'])
            # widgets
            table_power = Tables('power_a',data_cols=['Lubrificação'],data_rows=lubrification_a, height_custon=30)()
            table_info = Tables('power_b',data_rows=lubrification_b, height_custon=30)()
            gauge = WGauge(name='gauge_ug03')()
            # composicao
            box.add_widget(table_power)
            box.add_widget(table_info)
            box_tabelas.add_widget(box)
            box_gauge.add_widget(gauge)

            self.add_widget(box_tabelas)
            self.add_widget(box_gauge)

            # # s1.instance_time('23-Lubrification')
            # # s1.memory_size(getpid(),'Lubrification')
            return self

        except Exception as e:
            print(e)

        return self