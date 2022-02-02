from kivy.graphics import (Color, Ellipse, Rectangle)
from libs.baseclass.assets.color import cores
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivy.properties import ListProperty,NumericProperty
from kivy.clock import Clock
import ctypes
from screeninfo import get_monitors

#raise 'error'
#user32 = ctypes.windll.user32
#screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)*.96
screensize = [get_monitors()[0].width, get_monitors()[0].height]
#user32 = ctypes.windll.user32
#screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)*.95

# csoperacao123!@
# Clau654123
class WGauge(Widget):

    rpm: int = NumericProperty(0)
    position_gauge: list = ListProperty([.5,.5,.8,.8,0,360,0])
    spacy = 20
    pr: int = 0

    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __call__(self):

        with self.canvas:
            # Color(1., 0, 0)
            # self.rec = Rectangle(pos=(10, 10), size=(500, 500))
            self.color = Color(rgba=cores['adjust'])
            self.ellipse1 = Ellipse(pos=self.position_gauge[0:2],
                                    size=[(self.position_gauge[2]*self.size[self.position_gauge[6]]),(self.position_gauge[3]*self.size[self.position_gauge[6]])],
                                    angle_start=self.position_gauge[4],
                                    angle_end=self.position_gauge[4])
            self.color = Color(rgba=cores['widget'])
            self.ellipse2 = Ellipse(pos=(self.position_gauge[0]+self.spacy,self.position_gauge[1]+self.spacy),
                                    size=[(self.position_gauge[2]*self.size[self.position_gauge[6]])-self.spacy,
                                          (self.position_gauge[3]*self.size[self.position_gauge[6]])-self.spacy],
                                    angle_start=0,
                                    angle_end=360)
        self.label_aviso = MDLabel( text='0 \n rpm',
                                    halign = "center",
                                    font_style= 'Body1',
                                    theme_text_color = "Custom",
                                    text_color=cores['background_widget'])
        self.add_widget(self.label_aviso,1)
        Clock.schedule_interval(self.animation, 1)

        return self
    def on_size(self, *args):

        diametro = (self.position_gauge[2]*self.size[1])
        raio = diametro/2
        centro_x = (self.size[0]/2 + self.pos[0])
        centro_y = (self.size[1]/2 + self.pos[1])

        self.ellipse1.size = [diametro,
                              diametro]
        self.ellipse2.size = [diametro-self.spacy,
                              diametro-self.spacy]
        self.ellipse1.pos = [centro_x - raio, centro_y - raio]
        self.ellipse2.pos = [centro_x - raio + (self.spacy/2), centro_y- raio + (self.spacy/2) ]
        self.label_aviso.pos  = [centro_x - (self.label_aviso.texture_size[0]/2) , centro_y - (self.label_aviso.texture_size[1]/2)]
        # # self.rec.pos = [ self.pos[0]+ 50, self.pos[1] + 50]
        # self.rec.pos = self.pos
        # self.rec.size = self.size
        # self.label_aviso.texture_size[1] = ((self.size[0] + self.size[1])/2) * 0.75
        # self.label_aviso.texture_size[0] = 150
        # self.label_aviso.texture_size[1] = 150
        # self.label_aviso = font_style
        # print('   ')
        # print('-----------------------')
        # # print('proporção do texto em relação ao size: ', (self.label_aviso.text_size[1]/(self.size[0] + self.size[1])/2))
        # # print('proporção do texto em relação ao size: ', (self.label_aviso.texture_size[1]/(self.size[0] + self.size[1])/2))
        # print('text: ',self.label_aviso.text_size)
        # print(self.label_aviso.texture_size)
        # print(f'on_size {self.name}: ')
        # print('Diametro: ', diametro)
        # print('size: ',self.size)
        # print('pos: ',self.pos)
        # print('posicao elipse 1: ',self.ellipse1.pos)
        # print('posicao elipse 2: ',self.ellipse2.pos)
        # print('Size Elipse 1: ',self.ellipse1.size)
        # print('Size Elipse 2: ',self.ellipse2.size)
        # print('pos label: ',self.label_aviso.pos)
        # print('----------------------')
        # print('   ')
    def update_size(self, *args):

        try:
            pass
            # print('gauge:   ',self.name)
            # print('size widget: ',self.size)
            # print('widget pos: ', self.pos)
            # print('args size: ',args[0].size)
            # print('args 1: ',args[1])
            # print('args pos: ',args[0].pos)
            # self.size = args[0].size
            # self.pos = args[0].pos
            # self.ellipse1.size = [(self.position_gauge[2]*self.size[self.position_gauge[6]]),
            #                       (self.position_gauge[3]*self.size[self.position_gauge[6]])]
            # self.ellipse2.size = [(self.position_gauge[2]*self.size[self.position_gauge[6]])-self.spacy,
            #                       (self.position_gauge[3]*self.size[self.position_gauge[6]])-self.spacy]
            # self.ellipse1.pos = args[0].pos
            # self.ellipse2.pos = [args[0].pos[0] +self.spacy,args[0].pos[1] +self.spacy]
            # self.label_aviso = args[0].pos
            # self.ellipse1.pos = [(self.position_gauge[0] * self.size[0])- (self.ellipse1.size[1]/2),
            #                       (self.position_gauge[1] * self.size[1])+self.pos[1] -  (self.ellipse1.size[1]/2)]
            # self.ellipse2.pos = [(self.position_gauge[0] * self.size[0])- (self.ellipse2.size[1]/2),
            #                       (self.position_gauge[1] * self.size[1])+self.pos[1] +(self.spacy/2)- (self.ellipse1.size[1]/2)]
            # self.label_aviso.pos = [(self.size[0]/2)-(self.spacy*2 +10), (self.size[1]/2 + self.pos[1])-(self.spacy*2 + 10)]
            # print('posicao elipse 1: ',self.ellipse1.pos)
            # print('posicao elipse 2: ',self.ellipse2.pos)
            # print('label pos',self.label_aviso)
            # print('Ideal: ',[(self.size[0]/2)-(self.spacy*2 +10), (self.size[1]/2 + self.pos[1])-(self.spacy*2 + 10)] )
            # print('Size Elipse 1: ',self.ellipse1.size)
            # print('Size Elipse 2: ',self.ellipse2.size)
            # print('-------------------')

        except Exception as e:
            raise NotImplementedError(self.__class__.__name__ + str(e))

    def animation(self, *args):
        if self.rpm > 360:
            self.rpm = 0
        self.ellipse1.angle_start = self.rpm
        self.rpm = self.rpm + 2
        self.label_aviso.text = str(self.rpm)+ '\n rpm'
        # print('executando: ',self.ellipse1.angle_start,self.pos)

    # def on_touch_down(self, touch):
    #     print('#################')
    #     print(touch.x, touch.y,self.ellipse1.angle_start)
    #     print('#################')