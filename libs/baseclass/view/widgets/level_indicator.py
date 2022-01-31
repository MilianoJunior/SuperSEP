from kivymd.uix.boxlayout import MDBoxLayout

from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDSeparator
from libs.baseclass.observer.interfaces.observer import Observador

class LevelIndicator(MDBoxLayout):
    
    __metaclass__ = Observador
    content = []
    
    def __init__(self, **kwargs)->None:
        
        super().__init__(**kwargs)
        self.spacing = 1
        self.md_bg_color = theme.button_normal_color
        
    def create(self):
        theme = self.content[0]['Theme']
        card = MDCard(orientation='vertical',
                      padding=theme.padding,
                      size_hint=(1,1),
                      pos_hint={'center_x':.5,'center_y':.5})
        card.add_widget(MDLabel(text='Indicador de nível'))
        self.add_widget(card)
        
        return self
    
    def update(self):
        print('atualização registrada: ',self.name)