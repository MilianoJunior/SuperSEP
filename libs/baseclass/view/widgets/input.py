from libs.baseclass.observer.interfaces.observer import Observador
from kivymd.uix.textfield import *

class Button():
    '''
    Description
    -----------
        Cria um buttom com propriedades e métodos
    '''
    __metaclass__ = Observador
    name: str = None
    content: list = []
    action: list = []
    
    def __init__(self,textfield_name: str, **kwargs)->None:
        
        super().__init__(**kwargs)
        self.textfield_name = textfield_name
        
    def create(self):
        button = eval(button_name)
        add_property = map(lambda x: setattr(button, x['name'], x['value']),content)
        return button
    
    def update(self):
        print(f'{self.name} - está recebendo uma mensagem')