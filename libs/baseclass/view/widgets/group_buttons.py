from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.observer.interfaces.observer import Observador
from kivy.utils import get_color_from_hex


class MyToggleButton(MDRaisedButton, MDToggleButton):
    
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        

class GroupButtons(MDBoxLayout):
    
    __metaclass__ = Observador
    content = []
    actions = None
    name = 'groupbuttons'
    
    def __init__(self, **kwargs)->None:
        
        super().__init__(**kwargs)
        self.spacing = 1
        self.md_bg_color = get_color_from_hex('#0097a7')
        
    def create(self):   
        num = len(self.content)
        for i in range(0,num):
            btn = MyToggleButton(text=self.content[i],
                                  group = 'x')
            btn.bind(on_press= self.construir)
            btn.background_normal = get_color_from_hex('#0069c0')
            self.add_widget(btn)

        return self
    
    def update(self):
        print('atualização registrada-: ',self.name)
        
    def construir(self,obj):
        self.actions.current = obj.text
        obj.background_normal = get_color_from_hex('#0069c0')
        obj.background_down =  get_color_from_hex('#6ec6ff')
  

