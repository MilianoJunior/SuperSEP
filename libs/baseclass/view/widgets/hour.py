from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDSeparator
from libs.baseclass.observer.interfaces.observer import Observador



class Hour(MDBoxLayout):
    
    __metaclass__ = Observador
    content = []
    
    def __init__(self, **kwargs)->None:
        
        super().__init__(**kwargs)
        self.spacing = 1
        
    def create(self):
        theme = self.content['objetos']['Theme']
        card = MDCard(orientation='vertical',
                      padding=theme.padding,
                      size_hint=(1,1),
                      pos_hint={'center_x':.5,'center_y':.5})
        card.add_widget(MDLabel(text='Data: 20/09/2021'))
        card.add_widget(MDSeparator(height=1))
        card.add_widget(MDLabel(text='Hora: 15:23'))
        self.add_widget(card)
        
        return self
    
    def update(self):
        print('atualização registrada: ',self.name)