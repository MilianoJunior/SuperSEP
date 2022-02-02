from kivy.uix.widget import Widget
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import (Color, Line, Ellipse)
from libs.baseclass.assets.color import cores
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivy.properties import ListProperty,NumericProperty
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from kivy.clock import Clock
#from os.path import join, abspath
import os
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.animation import Animation
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

local = os.path.join(os.environ.get('ENGESEP_IMG'),'emergecy.jpg')
#local = join(os.eviroment.get('ENGESEP_IMG'),'emergecy.jpg')

class ImageButton(ButtonBehavior, Image):
    pass

class ButtonEmergency(MDBoxLayout):

    font = NumericProperty(0.41)

    def __init__(self,name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.orientation = 'vertical'
        self.name = name
        self.md_bg_color = cores['widget']
        self.padding=[0,0,0,10]
        self.size_hint=(1,1)
        self.pos_hint={'x':0,'y': 0}
        self.radius = [0,0,15,15]
        self.state = False
    def __call__(self):

        label_aviso = MDLabel(text='Botão de emergência',
                                halign = "center",
                                theme_text_color = "Custom",
                                text_color=cores['background_widget'],
                                pos_hint={'center_x':.5,'center_y':.5})
        # self.img = MDIconButton(icon=local,user_font_size= "39sp",pos_hint={'center_x':.5,'center_y':.5})
        self.img = ImageButton(source=local,size_hint=(None,None), size=[0,0],pos_hint={'center_x':.5,'center_y':.5})
        self.img.fbind('on_press',self.emergency_state,label_aviso)
        self.add_widget(label_aviso)
        self.add_widget(self.img)

        return self
    def emergency_state(self,*args):
        a = Animation(md_bg_color=cores['background_widget'])
        a += Animation(md_bg_color=cores['danger'])
        a.repeat = True
        if self.state:
            self.state = False
            args[0].text = 'Botão de emergência'
            args[0].text_color=cores['background_widget']
            self.md_bg_color=cores['widget']
            Animation.cancel_all(self,'md_bg_color')
        else:
            self.state = True
            args[0].text = 'Emergência acionada!'
            args[0].text_color=cores['widget']
            a.start(self)
    def on_size(self, *args):
        tamanho = int(0.51*((self.size[0]+self.size[1])/2))
        self.img.size = [tamanho, tamanho]
