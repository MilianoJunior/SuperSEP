from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDSeparator
from kivymd.uix.list import OneLineIconListItem, IconRightWidget,MDList,OneLineListItem
from kivy.metrics import dp

from libs.baseclass.observer.interfaces.observer import Observador


class Card(MDBoxLayout):
    
    __metaclass__ = Observador
    content = []
    name = None
    
    def __init__(self, **kwargs)->None:
        
        super().__init__(**kwargs)
        
    def create(self):
        theme = self.content['objetos']['Theme']
        print(theme.__dict__)
        card = MDCard(orientation='vertical',
                      padding=theme.padding,
                      size_hint=(1,1),
                      pos_hint={'center_x':.5,'center_y':.5})
        card.add_widget(MDLabel(text=theme.tema_escolhido,
                                adaptive_height= True,
                                halign = theme.text_align,
                                font_size=16,
                                center = self.center,
                                theme_text_color = "Custom",
                                text_color=(0,0,0)))
        card.add_widget(MDSeparator(height=1))
        lis = MDList()
        self.ids['container'] = lis
        for i in range(2):
            self.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
            )
        card.add_widget(lis)
        self.add_widget(card)
        
        return self
    
    def update(self):
        
        print('atualização registrada: ',self.name)