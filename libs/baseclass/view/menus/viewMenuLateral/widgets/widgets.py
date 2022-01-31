# from libs.baseclass.exception_error import Error
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.state_variable import StateVariable
from libs.baseclass.view.menus.viewMenuLateral.widgets.properties import ( navigation_properties,card_properties,
                                                                          box_properties,
                                                                          icon_properties,scrool_view_properties,
                                                                          icons,cores)
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.tooltip import MDTooltip
# from desempenho import Desempenho
# from os import getpid

# Total picle:  688368
#               108544

# s1 = Desempenho()

var = StateVariable()



class TooltipIcon(MDTooltip,MDIconButton):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.theme_text_color = "Custom"
        self.text_color = cores['background_widget']
        self.md_bg_color = cores['widget']
        self.font_size = "10sp"
        self.elevation_normal = 12
        self.pos_hint = {"center_x": .5, "center_y": .5}


class NavegationMenu(MDFloatLayout):
    
    memory = None
    def __init__(self,name, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __call__(self):
        try:
            var.register_change(self,navigation_properties)
            # Create Card
            card = MDCard(elevation=20)
            var.register_change(card,card_properties)
            # add icons
            layout = MDBoxLayout(spacing=5)
            var.register_change(layout,box_properties)
            layout.bind(minimum_height=layout.setter('height'))
            layout.bind(minimum_width=layout.setter('width'))
            for name,icon in icons.items():
                icon_add = TooltipIcon(icon=icon[1])
                icon_add.tooltip_text = icon[0]
                if self.memory is None:
                    self.memory = icon_add
                    icon_add.md_bg_color = cores['icon_select']
                icon_add.fbind('on_press',self.change_screen,name)
                var.register_change(icon_add,icon_properties)
                if name == 'UG':
                    self.ids['UG'] = icon_add
                layout.add_widget(icon_add)
            root = ScrollView()
            var.register_change(root,scrool_view_properties)
            root.add_widget(layout)
            card.add_widget(root)
            self.add_widget(card)
            # s1.instance_time('17-NavegationMenu')
            # s1.memory_size(getpid(),'NavegationMenu')
            return self
            
        except Exception as e:
            print('menu lateral: ',e)
            
        return self

    def change_screen(self,*args):
        args[1].md_bg_color = cores['icon_select']
        self.memory.md_bg_color = cores['widget']
        self.memory = args[1]
