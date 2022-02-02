from libs.baseclass.view.factory.builder_widget import BuilderWidgets
from libs.baseclass.exception_error import Error
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.state_variable import StateVariable
from libs.baseclass.view.menus.viewMenuLateral.widgets import *
from libs.baseclass.view.menus.viewMenuLateral.widgets.properties import *
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivy.uix.image import Image
from kivymd.uix.label import MDLabel
from libs.baseclass.assets.color import *
from libs.baseclass.view.menus.viewMenu.widgets.properties import *
from libs.baseclass.utils.methods import *
from kivy.core.window import Window
import os
# from desempenho import Desempenho

# s1 = Desempenho()

var =  StateVariable()
local = os.path.join(os.environ.get('ENGESEP_IMG'),'11.png')

class MenuMobile(BuilderWidgets):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = Error(self,'Menu Mobile')

    def __call__(self):
        try:
            img = Image(source=local,size_hint=[.6,.6],
                        pos_hint={'center_x':.5,'center_y':.5},
                        color=cores['background_widget'])

            menu_mobile = MDCard(elevation=20,
                          md_bg_color = cores['background'],
                          radius = [5,5,5,5],
                          pos_hint={'center_x':.5,'center_y':.5})
            menu_mobile.add_widget(img)
            # s1.instance_time('10-MenuMobile')
            # s1.memory_size(os.getpid(),'MenuMobile')
            return menu_mobile

        except Exception as e:
            self.error.msg(e)

class Logo(MDBoxLayout):

    def __init__(self,name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        # self.error = Error(self,'NavegationMenu')

    def __call__(self):
        try:
            img = Image(source=local,size_hint=[1,1],
                        pos_hint={'center_x':.5,'center_y':.5},
                        color=cores['background_widget'])
            # s1.instance_time('7-Logo')
            # s1.memory_size(os.getpid(),'Logo')
            return img

        except Exception as e:
            print('erro logo',e)


labels = ['SuperSEP','Principal']

class MenuPrincipal(BuilderWidgets):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = Error(self,'NavegationMenu')

    def __call__(self):
        try:
            box = MDBoxLayout()
            var.register_change(box,box_links)
            for label in labels:
                la = MDLabel(text=label,
                             halign="center",
                             theme_text_color= "Custom",
                             text_color=cores['background_widget'])
                var.register_change(la,labels_menu)

                box.add_widget(la)
            # s1.instance_time('8-MenuPrincipal')
            # s1.memory_size(os.getpid(),'MenuPrincipal')
            return box

        except Exception as e:
            self.error.msg(e)

        return self

class TooltipIcon(MDTooltip,MDIconButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_text_color = "Custom"
        self.text_color = cores['background_widget']
        self.md_bg_color = cores['widget']
        self.elevation_normal = 12
        self.pos_hint = {"center_x": .5, "center_y": .5}


icons = {
            'account'    : 'account-box',
            'config'       : 'cog-outline',
            'sair'         : 'exit-to-app',
        }

class CardMenu(BuilderWidgets):
    # screen_card = ObjectProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = Error(self,'NavegationMenu')

    def __call__(self):
        try:
            float_card = MDFloatLayout()
            box_card = MDBoxLayout(spacing=1)
            var.register_change(box_card, box_card_properties)
            b=.5
            for name,icon in icons.items():
                b+=.1
                card = MDCard(elevation=20,
                              md_bg_color = cores['widget'],
                              radius=[5,5,5,5],
                              pos_hint={'x':b,'center_y':.5})
                icon_add = TooltipIcon()
                icon_add.icon =icon
                icon_add.tooltip_text = name
                var.register_change(card,card_icons)
                var.register_change(icon_add,icons_toltip)
                icon_add.fbind('on_press',self.change_screen,name)
                card.add_widget(icon_add)
                box_card.add_widget(card)
            float_card.add_widget(box_card)
            # s1.instance_time('9-CardMenu')
            # s1.memory_size(os.getpid(),'CardMenu')
            return float_card

        except Exception as e:
            self.error.msg(e)

        return self

    def change_screen(self, *args):
        Window.system_size = [290,620]