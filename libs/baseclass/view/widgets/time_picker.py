from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.picker import MDTimePicker
from libs.baseclass.observer.interfaces.observer import Observador


class TimePicker(MDBoxLayout):
    
    __metaclass__ = Observador
    content: list = []
    name: str = None
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
    
    def create(self):
        
        time_dialog = MDTimePicker()
        self.add_widget(time_dialog)
        
        return self
    
    def update(self):
        print('Classe não instanciada: TimePicker')