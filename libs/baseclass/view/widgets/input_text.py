from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import (Color, Line, Ellipse)
from libs.baseclass.assets.color import cores
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivy.properties import ListProperty,NumericProperty
from kivymd.uix.textfield import MDTextField
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation

class InputText(MDTextField):
    
    def __init__(self,name: str, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.name = name

            
    def __call__(self):
        self.text = '48 W'
        self.hint_text= 'potência ativa'
        self.halign = 'center'
        self._hint_y = 58
        self.padding = [30,30,30,30]
        # for name, value in self.__dict__.items():
        #     print(name, '   ', value)
        #     print('---')
        # self.set_pos_hint_text(100.0,100.0)
        # input_text = MDTextField(
                                  
        #                           mode='fill',
        #                           active_line = True,
        #                           halign = "center",
        #                           current_hint_text_color=cores['background_widget'])
        # input_text.set_pos_hint_text(input_text,100,100)
        # self.add_widget(input_text)
        
        return self
    def on_size(self, *args):
        
        
        print('*************************')
        print('InputText: ',args)
        print(self.size)
        print(self.pos)
        # print(self.properties())
        # for name,value in self.properties().items():
        #     print(name,value)
        #     print(getattr(self, name))
        #     print('---')
        # print(args[0].pos)
        # print(args[0].size)
        # self.size = args[1]
        # self.pos = [0,0]
        print('*************************')