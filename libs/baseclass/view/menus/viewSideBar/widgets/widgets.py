import os
from libs.baseclass.view.factory.builder_widget import BuilderWidgets
from libs.baseclass.exception_error import Error
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.state_variable import StateVariable
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from libs.baseclass.assets.color import *
from libs.baseclass.view.menus.viewSideBar.widgets.properties import *
from libs.baseclass.utils.methods import *
from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget
from kivymd.uix.list import IconRightWidget
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.list import MDList
from kivymd.uix.textfield import MDTextField
from kivymd.uix.tab import MDTabsBase,MDTabs

# from desempenho import Desempenho

# s1 = Desempenho()

var =  StateVariable()

local = os.path.join(os.environ.get('ENGESEP_IMG'),'12.png')

class UserCard(BuilderWidgets):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = Error(self,'UserCard')

    def __call__(self):
        try:
            float_aux = MDFloatLayout()
            card_layout = MDCard(orientation='horizontal',
                                 elevation=20,
                                 radius=[5,],
                                 padding=[1,1,1,1],
                                 md_bg_color = cores['sidebar'],
                                 pos_hint={'center_x':.5,'center_y':.5},
                                 line_color= cores['linecard'])
            avatar_layout = TwoLineAvatarIconListItem(text= "Olá, Usuário",
                                                      theme_text_color = 'Custom',
                                                      font_style = 'Subtitle1',
                                                      secondary_theme_text_color = 'Custom',
                                                      secondary_text_color = cores['background_widget'],
                                                      text_color=cores['background_widget'],
                                                      secondary_text= "engesep@gmail.com",
                                                      secondary_font_style='Caption')
            img = ImageLeftWidget(source= local)
            icon = IconRightWidget(icon='dots-vertical',
                                   theme_text_color = "Custom",
                                   text_color = cores['background_widget'])
            var.register_change(avatar_layout, avatar_properties)
            var.register_change(card_layout, card_properties)
            avatar_layout.add_widget(img)
            avatar_layout.add_widget(icon)
            card_layout.add_widget(avatar_layout)
            float_aux.add_widget(card_layout)

            # s1.instance_time('12-UserCard')
            # s1.memory_size(os.getpid(),'UserCard')
            return float_aux

        except Exception as e:
            self.error.msg(e)



class Search(BuilderWidgets):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = Error(self,'Search menu lateral')

    def __call__(self):
        try:
#            FONT_PATH = f"{os.environ['ENGESEP_ROOT']}\\libs\\baseclass\\assets\\fonts\\BERNIERRegular-Regular"
            float_aux = MDFloatLayout()
            search_button = MDTextField(hint_text='Search',
                                        mode = 'rectangle',
                                        _current_line_color = cores['widget'],
#                                        font_name_hint_text = FONT_PATH,
                                        size_hint=[.76,.3],
                                        pos_hint={'center_x':.5,'center_y':.5})
            search_button.current_hint_text_color = cores['secundary']
            float_aux.add_widget(search_button)
            var.register_remove(float_aux,search_button,remove_search)

            # s1.instance_time('13-Search')
            # s1.memory_size(os.getpid(),'Search')
            return float_aux

        except Exception as e:
            self.error.msg(e)

class TableSidebar(BuilderWidgets):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = Error(self,'Search menu lateral')
    def __call__(self):
        try:
            float_aux = MDFloatLayout()
            box_menu = MDBoxLayout(md_bg_color=cores['background'],
                                   size_hint=[.8,.095],
                                   pos_hint={'center_x':.5,'center_y': .955},
                                   padding=[20,20,1,20],
                                   radius=[5,5,5,5])
            titulo = MDLabel(text='últimas informações',
                             theme_text_color= "Custom",
                             text_color= cores['background_widget'])
            box_menu.add_widget(titulo)
            box_table = MDBoxLayout(md_bg_color=cores['widget'],
                                    size_hint=[.8,.865],
                                    radius=[5,5,5,5],
                                    pos_hint={'center_x':.5,'center_y': .460})
            main_table = MDBoxLayout(size_hint_y=None)
            main_table.bind(minimum_height=main_table.setter('height'))
            lista = MDList()

            for names,values in lista_data.items():
                text_linha = ''
                for n,v in values['values'].items():
                    text_linha += v[1].upper() +'  : ' + v[0] + '\n'
                texto = MDLabel(text=text_linha,halign="left",
                                font_style='Caption',
                                valign= 'middle',
                                theme_text_color= "Custom",
                                text_color= cores['background_widget'])
                card_eventos = MDCard(orientation="vertical",
                                      size_hint= (.8,None),
                                      height=300,
                                      padding=[10,10,10,10],
                                      md_bg_color = cores['sidebar'],
                                      pos_hint={'center_x':.5,'center_y':.5},
                                      line_color= cores['linecard'])
                card_eventos.add_widget(texto)
                box = MDBoxLayout(orientation='vertical',adaptive_height=True)
                avatar_layout = TwoLineAvatarIconListItem(text= names,
                                                          pos_hint={'center_x':.5,'center_y':.1},
                                                          theme_text_color = 'Custom',
                                                          secondary_theme_text_color = 'Custom',
                                                          secondary_text_color = cores['background_widget'],
                                                          text_color=cores['background_widget'],
                                                          secondary_text= "Aviso: 25/10/2021 às 12:11",
                                                          secondary_font_style='Overline')
                icon = IconRightWidget(icon='dots-vertical',
                                        theme_text_color = "Custom",
                                        text_color = cores['background_widget'])
                icon.fbind('on_press', self.expand_info,names,box,card_eventos)
                icon_alerta = IconLeftWidget(icon=values['state'][0],
                                             theme_text_color = "Custom",
                                             user_font_size = 15,
                                             text_color = values['state'][1])

                avatar_layout.add_widget(icon)
                avatar_layout.add_widget(icon_alerta)
                box.add_widget(avatar_layout)
                lista.add_widget(box)
            root = ScrollView(size_hint=(1, 1))
            main_table.add_widget(lista)
            root.add_widget(main_table)
            box_table.add_widget(root)
            float_aux.add_widget(box_menu)
            float_aux.add_widget(box_table)

            # s1.instance_time('14-TableSidebar')-
            # s1.memory_size(os.getpid(),'TableSidebar')-----
            return float_aux

        except Exception as e:
            self.error.msg(e)

    def expand_info(self,*args):
        if args[2] in args[1].children:
            args[1].remove_widget(args[2])
        else:
            args[1].add_widget(args[2])



class TabSidebar(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class GraphSidebar(MDFloatLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = Error(self,'Search menu lateral')

    def __call__(self):
        try:
#            FONT_PATH = f"{os.environ['ENGESEP_ROOT']}\\libs\\baseclass\\assets\\fonts\\BERNIERRegular-Regular"
            card_layout = MDCard(orientation='vertical',
                                  elevation=20,
                                  size_hint = (.8,.9),
                                  radius=[5,],
                                  padding=[1,1,1,1],
                                  md_bg_color = cores['sidebar'],
                                  pos_hint={'center_x':.5,'center_y':.5},
                                  line_color= cores['linecard'])
            tab = MDTabs(tab_bar_height="30dp",
                         background_color=cores['background'],
                         tab_indicator_height="1dp",
#                         font_name= FONT_PATH,
                         )
            for s in ['diário','semanal','mensal']:
                title = TabSidebar(title=f'[size=12]{s}[/size]')
                tab.add_widget(title)
            card_layout.name = 'card_graph'
            card_layout.add_widget(tab)
            self.add_widget(card_layout)
            # s1.instance_time('15-GraphSidebar')
            # s1.memory_size(os.getpid(),'GraphSidebar')
            return self

        except Exception as e:
            self.error.msg(e)




