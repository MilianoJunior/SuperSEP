from libs.baseclass.view.factory.builder_widget import BuilderWidgets
from libs.baseclass.exception_error import Error
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.state_variable import StateVariable
from libs.baseclass.view.menus.viewMenuLateral.widgets import *
from libs.baseclass.view.menus.viewMenuLateral.widgets.properties import *
from kivy.uix.button import Button
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

var =  StateVariable()


widgets = ['gauge','button-emergency','card-power','card-temperature','card-lubrication']

class Gauge(BuilderWidgets):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error = Error(self,'NavegationMenu')
        self.name = widgets[0]
        
    def __call__(self):
        try:
            # criar o layout main
            main = MDFloatLayout()
            var.register_change(main,navigation_properties)
            # Create Card
            card = MDCard(elevation=20)
            var.register_change(card,card_properties)
            
            main.add_widget(card)
            
            return main
            
        except Exception as e:
            self.error.msg(e)
            
        return self