from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from libs.baseclass.observer.interfaces.observer import Observador


class MyToggleButton(MDRaisedButton, MDToggleButton):
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        self.font_size = 11
        self.background_down = theme.backgroundcolor
        self.background_normal =  theme.text_color_down
        self.font_color_normal = theme.text_color_normal
        self.font_color_down = theme.text_color_down

    
class Tabs(MDBoxLayout):
    
    __metaclass__ = Observador
    content: list = []
    name: str = None
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
    
    def create(self):
        
        for name_tab in self.content:
            btn = MyToggleButton(text = name_tab,group = 'x')
            self.add_widget(btn)
            
        return self
    
    def update(self):
        print('atualização registrada: ',self.name)
    
    