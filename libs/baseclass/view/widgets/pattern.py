from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.observer.interfaces.observer import Observador

class Pattern(MDBoxLayout):
    
    __metaclass__ = Observador
    name: str = None
    content: list = []
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
    def create(self):
        # theme = self.content
        print(self.name, 'ok')
        pass
    
    def update(self):
        print(f'{self.name} - está recebendo uma mensagem')
        