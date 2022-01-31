from math import sin
from kivy_garden.graph import Graph, MeshLinePlot
from kivymd.uix.tab import MDTabsBase,MDTabs
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.graphics import *
import os
from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
        BooleanProperty

    
class Graph:
    
    size = ListProperty([])
    size_all = ListProperty([])
    pos_graph = ListProperty([])
    
    def __init__(self):
        pass
        
    def create(self):
        print('----------------------')
        print(self.size_all)
        print(self.size)
        print(self.pos_graph)
        print('---------------------')
        # super().__init__(*args, **kwargs)
            
    # def __call__(self):
    #     print('----------------------')
    #     print(self.size_all)
    #     print(self.size)
    #     print('---------------------')
        
    #     return

    # def update_points_animation(self, *args):
    #     cy = self.height * 0.6
    #     cx = self.width * 0.1
    #     w = self.width * 0.8
    #     dt = 0
    #     print('Largura------------')
    #     print(self.width)
    #     step = 20
    #     points = []
    #     points2 = []
    #     import time
    #     dt += dt
    #     for i in range(int(w / step)):
    #         x = i * step
    #         a = cx + x
    #         b = cy + cos(x / w * 8. + dt) * self.height * 0.2
    #         points.append(a)
    #         points.append(b)
    #         # points.append(cy + self.sigmoid(x))
    #         time.sleep(0.03)
    #         points2.append(cx + x)
    #         points2.append(cy + sin(x / w * 8. + dt) * self.height * 0.2)
    #     print(points)
    #     print('-----')