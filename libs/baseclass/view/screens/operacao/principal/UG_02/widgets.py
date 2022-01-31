from libs.baseclass.view.factory.builder_widget import BuilderWidgets
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.state_variable import StateVariable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.graphics import Color
from kivy.graphics import Line
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from libs.baseclass.assets.color import cores
from kivymd.uix.textfield import MDTextField
from kivy.animation import Animation
# from os import getpid 
from os.path import join, abspath
# from desempenho import Desempenho
from libs.baseclass.view.widgets.gauge import WGauge
from libs.baseclass.view.widgets.input_text import InputText
from libs.baseclass.view.widgets.button_emergency import ButtonEmergency
from kivy.properties import ListProperty

# s1 = Desempenho()

var =  StateVariable()


class Gauge(MDFloatLayout):
    
    gauge = ListProperty([120, 810, 70, 0, 360])
    
    
    def __init__(self,name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = False
        self.name = name
        self.md_bg_color = cores['background']
        
    def __call__(self):
        try:
            # layouts
            box_gauge = MDBoxLayout(orientation='horizontal',
                                    md_bg_color = cores['widget'],
                                    size_hint=(1,.5),
                                    pos_hint={'x':0,'y':.5})
            box_input = MDBoxLayout(orientation='horizontal',
                                    md_bg_color = cores['widget'],
                                    size_hint=(1,.15),
                                    pos_hint={'x':0,'y':.35},
                                    padding=[0,])
            box_emergency = MDBoxLayout(orientation='horizontal',
                                        md_bg_color = cores['background_widget'],
                                        size_hint=(1,.35),
                                        pos_hint={'x':0,'y': 0})
            # componentes
            gauge = WGauge(name='gauge_ug02')()
            
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
            box_gauge.bind(pos=gauge.update_size)
            
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
                'Acumulador de energia': ['48','MW']
    
      }   
class Power(BuilderWidgets):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def __call__(self):
        try:
            card_layout = MDCard()
            # layouts
            box_float = MDFloatLayout()
            box_titulo = MDBoxLayout(orientation='horizontal',
                                     md_bg_color = cores['widget'],
                                     size_hint=(1,.08),
                                     pos_hint={'x':0,'y':.92})
            box_tabela = MDBoxLayout(orientation='horizontal',
                                     md_bg_color = cores['background'],
                                     size_hint=(1,.92),
                                     pos_hint={'x':0,'y': 0})
            box_grid = GridLayout(cols=1)
            box_grid_titulo = GridLayout(cols=3)
            # componentes
            s = 0
            for index in ['UG-01','Tensão','Corrente']:
                label = MDLabel(text=index,
                                halign = "center",
                                theme_text_color = "Custom",
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                box_grid_titulo.add_widget(label)
                
            for name,value in dados_ug01_a.items():
                label_a = MDLabel(text=name,
                                halign = "left",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                label_b = MDLabel(text=str(value[0]) + ' V',
                                halign = "center",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                label_c = MDLabel(text=str(value[1]) + ' A',
                                halign = "center",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                if s%2 == 0:
                    linha = MDBoxLayout(orientation='horizontal',
                                        md_bg_color = cores['linha2'],
                                        padding = [10,10,10,10],
                                        radius=[5,])
                else:
                    linha = MDBoxLayout(orientation='horizontal',
                                        md_bg_color = cores['linha1'],
                                        padding = [10,10,10,10],
                                        radius=[5,])
                linha.add_widget(label_a)
                linha.add_widget(label_b)
                linha.add_widget(label_c)
                s+=1
                box_grid.add_widget(linha)
                
            label_subtitulo = MDLabel(text='',
                                    halign = "center",
                                    theme_text_color = "Custom",
                                    font_style = 'Caption',
                                    text_color=cores['background_widget'],
                                    pos_hint={'center_x':.1,'center_y':.5})
            linha = MDBoxLayout(orientation='horizontal',
                                md_bg_color = cores['widget'],
                                padding = [0,0,0,0],
                                radius=[5,])
            box_grid.add_widget(linha)  
            for name,value in dados_ug01_b.items():
                
                label_a = MDLabel(text=name,
                                halign = "left",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.1,'center_y':.5})
                label_b = MDLabel(text= value[0] +' '+value[1],
                                halign = "center",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                if s%2 == 0:
                    linha = MDBoxLayout(orientation='horizontal',
                                        md_bg_color = cores['linha2'],
                                        padding = [10,10,10,10],
                                        radius=[5,])
                else:
                    linha = MDBoxLayout(orientation='horizontal',
                                        md_bg_color = cores['linha1'],
                                        padding = [10,10,10,10],
                                        radius=[5,])
                
                linha.add_widget(label_a)
                linha.add_widget(label_b)
                s+=1
                box_grid.add_widget(linha)
             
            box_titulo.add_widget(box_grid_titulo)
            box_tabela.add_widget(box_grid)
                # nivel 1
            box_float.add_widget(box_titulo)
            box_float.add_widget(box_tabela)
                # nivel 3
            card_layout.add_widget(box_float)
            #---- Animação
            # s1.instance_time('B-Power')
            # s1.memory_size(getpid(),'Power')
            return card_layout
            
        except Exception as e:
            print('Power: ',e)
            
        return self

temperature_ug01_a = {
                        'Enrol. fase A'  :[10],
                        'Enrol. fase B'  :[10],
                        'Enrol. fase C'  :[10],
                        'Núcleo estator' :[10],
                        'Excitatriz'     :[10],
                        'Cubículo CS-U1' :[10],    
                    }

temperature_ug01_b = {
                        'Gula casquilo'  :[10],
                        'Comb. casquilo' :[10],
                        'Comb. escora'   :[10],
                        'Contra escora'  :[10],
                        'UHRV óleo'      :[10],
                        'UHLM óleo'      :[10],
    
                    }
class Temperatures(BuilderWidgets):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def __call__(self):
        try:
            card_layout = MDCard()
            # layouts
            box_float = MDFloatLayout()
            box_titulo = MDBoxLayout(orientation='horizontal',md_bg_color = cores['widget'],size_hint=(1,.08),pos_hint={'x':0,'y':.92})
            box_tabela = MDBoxLayout(orientation='horizontal',md_bg_color = cores['background'],size_hint=(1,.92),pos_hint={'x':0,'y': 0})
            box_grid = GridLayout(cols=1)
            # componentes
            label_titulo = MDLabel(text='Temperaturas UG-01',
                                    halign = "center",
                                    theme_text_color = "Custom",
                                    text_color=cores['background_widget'],
                                    pos_hint={'center_x':.5,'center_y':.5})
            label_subtitle = MDLabel(text= 'Gerador',
                                    halign = "center",
                                    theme_text_color = "Custom",
                                    font_style = 'Caption',
                                    text_color=cores['background_widget'],
                                    pos_hint={'center_x':.5,'center_y':.5})
            linha = MDBoxLayout(orientation='horizontal',
                                md_bg_color = cores['widget'],
                                padding = [10,10,10,10],
                                radius=[5,])
            linha.add_widget(label_subtitle)
            box_grid.add_widget(linha) 
            s = 0
            for name,value in temperature_ug01_a.items():
                label_a = MDLabel(text= name,
                                halign = "left",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                label_b = MDLabel(text= str(value[0]) + 'ºC',
                                halign = "center",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                if s%2 == 0:
                    linha = MDBoxLayout(orientation='horizontal',md_bg_color = cores['linha2'],radius=[5,],padding=[10,10,10,10])
                else:
                    linha = MDBoxLayout(orientation='horizontal',md_bg_color = cores['linha1'],radius=[5,],padding=[10,10,10,10])
                
                linha.add_widget(label_a)
                linha.add_widget(label_b)
                box_grid.add_widget(linha)
                s+=1
            linha = MDBoxLayout(orientation='horizontal',
                                md_bg_color = cores['widget'],
                                padding = [0,0,0,0],
                                radius=[5,])
            label_subtitle = MDLabel(text= 'Turbina',
                                    halign = "center",
                                    theme_text_color = "Custom",
                                    font_style = 'Caption',
                                    text_color=cores['background_widget'],
                                    pos_hint={'center_x':.5,'center_y':.5})
            linha.add_widget(label_subtitle)
            box_grid.add_widget(linha)  
            #---------------------------------------------------------
            s = 0
            for name,value in temperature_ug01_b.items():
                label_a = MDLabel(text= name,
                                halign = "left",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                label_b = MDLabel(text= str(value[0]) + 'ºC',
                                halign = "center",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                if s%2 == 0:
                    linha = MDBoxLayout(orientation='horizontal',md_bg_color = cores['linha2'],radius=[5,],padding=[10,10,10,10])
                else:
                    linha = MDBoxLayout(orientation='horizontal',md_bg_color = cores['linha1'],radius=[5,],padding=[10,10,10,10])
                
                linha.add_widget(label_a)
                linha.add_widget(label_b)
                box_grid.add_widget(linha)
                s+=1
            # composicao
                # nivel 1
            box_titulo.add_widget(label_titulo)
            box_tabela.add_widget(box_grid)
                # nivel 1
            box_float.add_widget(box_titulo)
            box_float.add_widget(box_tabela)
                # nivel 3
            card_layout.add_widget(box_float)
            
            # s1.instance_time('B-Temperatures')
            # s1.memory_size(getpid(),'Temperatures')
            return card_layout
            
        except Exception as e:
            print('Temperatures : ',e)
            
        return self


lubrification_a = {
                    'unidade hidráulica operacional': True,
                    'Bomba 01 - Ligada': True,
                    'Bomba 02 - Ligada': True,
                    'Pressostato linha': True,
                    'Água trocador de calor' : True,
    
    }

lubrification_b = {
                    'unidade hidráulica operacional': True,
                    'Bomba 01 - Ligada': True,
                    'Bomba 02 - Ligada': True,    
    }

class Lubrification(BuilderWidgets):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def __call__(self):
        try:
            card_layout = MDCard(md_bg_color = cores['alert'])
            # layouts
            box_float = MDFloatLayout()
            box_titulo = MDBoxLayout(orientation='horizontal',md_bg_color = cores['widget'],size_hint=(1,.08),pos_hint={'x':0,'y':.92})
            box_tabela = MDBoxLayout(orientation='horizontal',md_bg_color = cores['background'],size_hint=(1,.69),pos_hint={'x':0,'y':.23})
            box_gauge  = MDBoxLayout(orientation='horizontal',md_bg_color = cores['background'],size_hint=(1,.23),pos_hint={'x':0,'y': 0})
            box_grid = GridLayout(cols=1)
            # componentes
            label_titulo = MDLabel(text='Lubrificação',
                                    halign = "center",
                                    font_size= 90,
                                    theme_text_color = "Custom",
                                    text_color=cores['background_widget'],
                                    pos_hint={'center_x':.5,'center_y':.5})
            label_subtitle = MDLabel(text= 'UH Lubrificação do mancal (UHLM)',
                                    halign = "center",
                                    theme_text_color = "Custom",
                                    font_style = 'Caption',
                                    text_color=cores['background_widget'],
                                    pos_hint={'center_x':.1,'center_y':.5})
            linha = MDBoxLayout(orientation='horizontal',
                                md_bg_color = cores['widget'],
                                padding = [10,10,10,10],
                                radius=[5,])
            linha.add_widget(label_subtitle)
            box_grid.add_widget(linha) 
            s = 0
            for name,value in lubrification_a.items():
                icon_lub = MDIconButton(icon="circle-outline",
                                        theme_text_color = "Custom",
                                        user_font_size = 15,
                                        pos_hint={'x': 0,'y':0},
                                        text_color = cores['check']) 
                label_a = MDLabel(text= name,
                                halign = "left",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                if s%2 == 0:
                    linha = MDBoxLayout(orientation='horizontal',md_bg_color = cores['linha2'],radius=[5,],padding=[0,0,0,0])
                else:
                    linha = MDBoxLayout(orientation='horizontal',md_bg_color = cores['linha1'],radius=[5,],padding=[0,0,0,0])
                linha.add_widget(icon_lub)
                linha.add_widget(label_a)
                box_grid.add_widget(linha)
                s+=1
            label_subtitle = MDLabel(text= 'UH Regulador de velocidade (UHRV)',
                                    halign = "left",
                                    theme_text_color = "Custom",
                                    font_style = 'Caption',
                                    text_color=cores['background_widget'],
                                    pos_hint={'center_x': 0,'center_y':.5})
            linha = MDBoxLayout(orientation='horizontal',
                                md_bg_color = cores['widget'],
                                padding = [10,10,10,10],
                                radius=[5,])
            linha.add_widget(label_subtitle)
            box_grid.add_widget(linha) 
            s = 0
            for name,value in lubrification_b.items():
                
                icon_lub = MDIconButton(icon="circle-outline",
                                        theme_text_color = "Custom",
                                        user_font_size = 15,
                                        pos_hint={'x': 0,'y':.1},
                                        text_color = cores['check']) 
                label_a = MDLabel(text= name,
                                halign = "left",
                                theme_text_color = "Custom",
                                font_style = 'Caption',
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
                if s%2 == 0:
                    linha = MDBoxLayout(orientation='horizontal',md_bg_color = cores['linha2'],radius=[5,],padding=[0,0,0,0])
                else:
                    linha = MDBoxLayout(orientation='horizontal',md_bg_color = cores['linha1'],radius=[5,],padding=[0,0,0,0])
                linha.add_widget(icon_lub)
                linha.add_widget(label_a)
                box_grid.add_widget(linha)
                s+=1
                
            # with card_layout.canvas.after:
            #     Color(rgba=(.4, .4, 1, .6))
            #     Line(width = dp(4),
            #           circle=(1080, 510, 38, 0, 360))   
            #     Color(rgba=get_color_from_hex('#2bebc8'))
            #     Line(width = dp(4),
            #           circle=(1080, 510, 25, -90, 180)) 
            #     Color(rgba=(.4, .4, 1, .1))
            #     Line(width = dp(4),
            #           circle=(1082, 510, 38, 0, 360))
                
            label_bar = MDLabel(text='100 \n bar',
                                halign = "center",
                                font_style= 'Overline',
                                theme_text_color = "Custom",
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
            # # composicao
            #     # nivel 1
            box_titulo.add_widget(label_titulo)
            box_tabela.add_widget(box_grid)
            box_gauge.add_widget(label_bar)
                # nivel 1
            box_float.add_widget(box_titulo)
            box_float.add_widget(box_tabela)
            box_float.add_widget(box_gauge)
                # nivel 3
            card_layout.add_widget(box_float)
            
            # s1.instance_time('23-Lubrification')
            # s1.memory_size(getpid(),'Lubrification')
            return card_layout
            
        except Exception as e:
            print('Lubrification: ',e)
            
        return self




