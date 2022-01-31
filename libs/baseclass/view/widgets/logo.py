from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.observer.interfaces.observer import Observador
from kivy.uix.image import Image

class Logo(MDBoxLayout):
    
    __metaclass__ = Observador
    name: str = None
    content: list = []
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
    def create(self):
        theme = self.content['objetos']['Theme']
        for element in self.content['element'].keys():
            if element == 'struct':
                obj = eval(self.content['element']['struct'])()
            else:
                print(self.content['element'][element])
                setattr(obj,element,self.content['element'][element])
        
        return self.add_widget(obj)
    
    def update(self):

        print(f'{self.name} - está recebendo uma mensagem')