from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
# from kivymd.floatlayout import MDFloatLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from libs.baseclass.assets.color import cores
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton


class Tables(MDBoxLayout):
    
    def __init__(self,name: str, data_rows: list, height_custon: int, data_cols: list = None , *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_cols = data_cols
        self.data_rows = data_rows
        self.name = name
        self.height_custon = height_custon
        self.icons_ = False
        # self.radius = [15,15,15,15]
        # self.line_color = cores['linecard']
        self.orientation = 'vertical'
        self.md_bg_color= cores['background']
        self.padding = [0,0,0,0]
        # self.size_hint=(1, None)
        self.size_hint = (1,None)
        # self.pos_hint = {'center_x':.5, 'center_y':.5}
        
    def __call__(self):
        try:
            self.main_layout = MDBoxLayout(orientation = 'vertical', 
                                          size_hint_y = None, 
                                          padding=[0,],
                                          spacing=1,
                                          radius = [5,5,5,5],
                                          md_bg_color= cores['background'])
            self.main_layout.bind(minimum_height=self.main_layout.setter('height'))
            if not self.data_cols is None:
                titulo = MDBoxLayout(orientation = 'horizontal',size_hint_y = None,height=35,radius = [5,5,0,0], padding=[0],md_bg_color= cores['widget'])
                for col in self.data_cols:
                    btn = MDLabel(text=col,
                                  halign= "center",
                                  theme_text_color= "Custom",
                                  text_color=cores['background_widget'])
                    titulo.add_widget(btn)
                self.main_layout.add_widget(titulo)
            cont = 0
            for name,row in self.data_rows.items():
                cont += 1
                if cont%2 == 0:
                    linha = MDBoxLayout(orientation = 'horizontal',md_bg_color= cores['linha1'],size_hint_y = None,height=self.height_custon)
                else:
                    linha = MDBoxLayout(orientation = 'horizontal',md_bg_color= cores['linha2'],radius = [5,5,5,5], size_hint_y = None,height=self.height_custon)

                btn = MDLabel(text=name,
                              halign= "center",
                              theme_text_color= "Custom",
                              text_color=cores['background_widget'])
                linha.add_widget(btn)
                if self.icons_:
                    icon_lub = MDIconButton(icon="circle-outline",
                                            theme_text_color = "Custom",
                                            user_font_size = 15,
                                            pos_hint={'x': 0,'y':0},
                                            text_color = cores['check'])
                    linha.add_widget(btn)
                    
                for s in row:
                    btn = MDLabel(text=str(s),
                                  halign= "center",
                                  theme_text_color= "Custom",
                                  text_color=cores['background_widget'])
                    linha.add_widget(btn)
                self.main_layout.add_widget(linha)
            self.root = ScrollView(size_hint=(1, None), height=100, bar_width= 0)
            self.root.add_widget(self.main_layout) 
            self.add_widget(self.root)
            return self
            
        except Exception as e:
            
            raise RuntimeError('Erro table', e)
        
        return self
    def on_size(self,*args):
        self.height = self.main_layout.size[1]
        self.root.height = self.height -.5
        
        # print('*************************')
        # print(self.name)
        # print(args[0].size)
        # print('position: ',self.pos, self.pos_hint)
        # print('on_size: ',self.height)
        # print('on_size: ',self.main_layout.size)
        # print('*************************')
        # self.pos_hint = {'x':0,'y':0}
        
    # def responsivo(self, *args):
    #     # self.root.height = args[1][1]-40
    #     print('------------------------')
    #     print(self.name)
    #     print(args)
    #     print('scrooll: ',self.root.size)
    #     print('responsivo: ', args[1])
    #     print('responsivo: ',args[0].size)
    #     print('----------------------')
# x /2 + y =10
# 0.75
# x + y = 10
# 2 + y = 10

# 4854.6440.8021.3709
# 02/2022
# 405
# t = 15
# print(cores['primary'])
# data_tables = MDDataTable(
#     background_color = cores['primary'],
#     size_hint=(1, 1),
#     use_pagination=False,
#     column_data=[
#         ("[size=12][color=#C042B8]Column 4[/color][/size]", dp(t)),
#         ("[size=12][color=#C042B8]Column 4[/color][/size]", dp(t)),
#         ("[size=12][color=#C042B8]Column 4[/color][/size]", dp(t)),
#         ("[size=12][color=#C042B8]Column 4[/color][/size]", dp(t)),
#         ("[size=12][color=#C042B8]Column 4[/color][/size]", dp(t)),
#         ("[size=12][color=#C042B8]Column 4[/color][/size]", dp(t)),
#     ],
#     row_data=[
#         (
#             f"{i + 1}",
#             "[color=#297B50]1[/color]",
#             "[color=#C552A1]2[/color]",
#             "[color=#6C9331]3[/color]",
#             "4",
#             "5",
#         )
#         for i in range(50)
#     ],
    
# )
# layout.add_widget(data_tables)

# card_layout = MDCard()
# # layouts
# box_float = MDFloatLayout()
# box_titulo = MDBoxLayout(orientation='horizontal',
#                          md_bg_color = cores['widget'],
#                          size_hint=(1,.08),
#                          pos_hint={'x':0,'y':.92})
# box_tabela = MDBoxLayout(orientation='horizontal',
#                          md_bg_color = cores['background'],
#                          size_hint=(1,.92),
#                          pos_hint={'x':0,'y': 0})
# box_grid = GridLayout(cols=1)
# box_grid_titulo = GridLayout(cols=3)
# # componentes
# s = 0
# for index in ['UG-01','Tensão','Corrente']:
#     label = MDLabel(text=index,
#                     halign = "center",
#                     theme_text_color = "Custom",
#                     text_color=cores['background_widget'],
#                     pos_hint={'center_x':.5,'center_y':.5})
#     box_grid_titulo.add_widget(label)
    
# for name,value in dados_ug01_a.items():
#     label_a = MDLabel(text=name,
#                     halign = "left",
#                     theme_text_color = "Custom",
#                     font_style = 'Caption',
#                     text_color=cores['background_widget'],
#                     pos_hint={'center_x':.5,'center_y':.5})
#     label_b = MDLabel(text=str(value[0]) + ' V',
#                     halign = "center",
#                     theme_text_color = "Custom",
#                     font_style = 'Caption',
#                     text_color=cores['background_widget'],
#                     pos_hint={'center_x':.5,'center_y':.5})
#     label_c = MDLabel(text=str(value[1]) + ' A',
#                     halign = "center",
#                     theme_text_color = "Custom",
#                     font_style = 'Caption',
#                     text_color=cores['background_widget'],
#                     pos_hint={'center_x':.5,'center_y':.5})
#     if s%2 == 0:
#         linha = MDBoxLayout(orientation='horizontal',
#                             md_bg_color = cores['linha2'],
#                             padding = [10,10,10,10],
#                             radius=[5,])
#     else:
#         linha = MDBoxLayout(orientation='horizontal',
#                             md_bg_color = cores['linha1'],
#                             padding = [10,10,10,10],
#                             radius=[5,])
#     linha.add_widget(label_a)
#     linha.add_widget(label_b)
#     linha.add_widget(label_c)
#     s+=1
#     box_grid.add_widget(linha)
    
# label_subtitulo = MDLabel(text='',
#                         halign = "center",
#                         theme_text_color = "Custom",
#                         font_style = 'Caption',
#                         text_color=cores['background_widget'],
#                         pos_hint={'center_x':.1,'center_y':.5})
# linha = MDBoxLayout(orientation='horizontal',
#                     md_bg_color = cores['widget'],
#                     padding = [0,0,0,0],
#                     radius=[5,])
# box_grid.add_widget(linha)  
# for name,value in dados_ug01_b.items():
    
#     label_a = MDLabel(text=name,
#                     halign = "left",
#                     theme_text_color = "Custom",
#                     font_style = 'Caption',
#                     text_color=cores['background_widget'],
#                     pos_hint={'center_x':.1,'center_y':.5})
#     label_b = MDLabel(text= value[0] +' '+value[1],
#                     halign = "center",
#                     theme_text_color = "Custom",
#                     font_style = 'Caption',
#                     text_color=cores['background_widget'],
#                     pos_hint={'center_x':.5,'center_y':.5})
#     if s%2 == 0:
#         linha = MDBoxLayout(orientation='horizontal',
#                             md_bg_color = cores['linha2'],
#                             padding = [10,10,10,10],
#                             radius=[5,])
#     else:
#         linha = MDBoxLayout(orientation='horizontal',
#                             md_bg_color = cores['linha1'],
#                             padding = [10,10,10,10],
#                             radius=[5,])
    
#     linha.add_widget(label_a)
#     linha.add_widget(label_b)
#     s+=1
#     box_grid.add_widget(linha)
 
# box_titulo.add_widget(box_grid_titulo)
# box_tabela.add_widget(box_grid)
#     # nivel 1
# box_float.add_widget(box_titulo)
# box_float.add_widget(box_tabela)
#     # nivel 3
# card_layout.add_widget(box_float)
# #---- Animação
# # s1.instance_time('21-Power')
# # s1.memory_size(getpid(),'Power')
# return card_layout



