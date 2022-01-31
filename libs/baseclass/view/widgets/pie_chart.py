from kivy.properties import ListProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.graphics import Color, Ellipse,Rectangle,Line
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.observer.interfaces.observer import Observador

class PieChartLine(Widget):
    
    __metaclass__ = Observador
    text = StringProperty()
    line_color = ListProperty(
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
    )
    angle_start = ListProperty([0, 0, 0, 0])
    angle_end = ListProperty([0, 0, 0, 0])
    content: list = []
    name: str = None
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)
        
    def create(self):
        
        theme = self.content['objetos']['Theme']
        self.size = self.content['element']['size']
        self.pos = self.content['element']['pos']
        self.text = f"{self.content['element']['name']}"
        angle = [ (a + a) for a in range(-70,70)]
        
        with self.canvas:
            for s in angle:
                t = s if s> 0 else -s
                Color(30,self.content['element']['cor'],t/255)
                Line(width = dp(5),
                     circle=(self.center_x,
                             self.center_y,
                             min(self.width,self.height)/2,
                             s,s+1))
            label = MDLabel(text=self.text,
                            halign = "center",
                            font_size= dp(20),
                            center = self.center,
                            theme_text_color = "Custom",
                            text_color=theme.text_color)
            self.add_widget(label)
            
        return self
    
    def on_touch_down(self, touch):
        # self.content[0]['size']
        print(touch.x,touch.y)
        # self.size = [touch.x,touch.y]

    def on_touch_move(self, touch):
        print('test')
        
    def update(self):
        print('atualização registrada: ',self.name)

