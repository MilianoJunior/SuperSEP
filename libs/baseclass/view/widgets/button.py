from libs.baseclass.observer.interfaces.observer import Observador
from kivymd.uix.textfield import MDTextField
from libs.baseclass.exception_error import Error

class MyButton():
    '''
    Description
    -----------
        Cria um buttom com propriedades e métodos
    '''
    __metaclass__ = Observador
    name: str = None
    content: list = []
    action: list = []
    
    def __init__(self,button_name: str)->None:

        self.button_name = button_name
        
    def create(self):
        try:
            button = eval(self.button_name)()
            for x in self.content:
                setattr(button, x['name'], x['value'])
                
            return button
        
        except Exception as e:
            Error(self,'MyButton').msg(e)

    def update(self):
        
        print(f'{self.name} - está recebendo uma mensagem')