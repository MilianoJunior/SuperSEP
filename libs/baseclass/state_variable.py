from kivy.event import EventDispatcher
from libs.baseclass.utils.methods import *
from libs.baseclass.exception_error import Error
from desempenho import Desempenho
import os

s1 = Desempenho()

class Singleton(type):
    
    __instances ={}
    contador = 0
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
            cls.contador = 0
        return cls.__instances[cls]


class StateVariable(EventDispatcher,metaclass=Singleton):
    '''
    Description
    -----------
        monitora e altera os estados das variáveis se necessário
    '''
    register: list = []
    register_remover: list = []
    register_remover_add: list = []
    register_graph: list = []
    aux = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # s1.instance_time('3-StateVariable')
        # s1.memory_size(os.getpid(),'StateVariable')
        
          
    def register_change(self,widget: object, variable: dict)->NoReturn:
        try:
            # self.contador += 1
            # print('Acessado - registro_change',self.contador,' : ',variable[0]['name'])
            # print(os.getcwd())
            self.register.append([widget,variable])
        except Exception as e:
            Error(self).msg(e)
    def register_remove_add(self,pai: object,remove_widget: list[object], add_widget: list[object], variable: list)->NoReturn:
        try:
            # self.contador += 1
            # print('Acessado - register_remove_add',self.contador)
            self.register_remover_add.append([pai,remove_widget,add_widget,variable])
        except Exception as e:
            Error(self).msg(e)
        
    def register_remove(self,pai: object,filho: object, variable: list)->NoReturn:
        try:
            # self.contador += 1
            # print('Acessado - register_remove',self.contador)
            self.register_remover.append([pai,filho,variable])
        except Exception as e:
            Error(self).msg(e)
            
    def register_graphs(self,graph: object,formula: list)->NoReturn:
        try:
            # self.contador += 1
            # print('Acessado - register_graphs',self.contador)
            self.register_graph.append([graph,formula])
        except Exception as e:
            Error(self).msg(e)
            
    def change_graphics(self,*args):
        pass
        # self.contador += 1
        # print('Acessado - Change grap',self.contador)
        # s1.instance_time('00-ultima chamada')
        # s1.memory_size(os.getpid(),'00-ultima chamada')
        # s1.grafico()
        
    def update_condition(self,size):
        contador = 0
        for values in self.register_remover_add:
            for condition in values[3]:
                contador += 1
                if condition['condition'] > size[0] and any([s== p for s in values[1] for p in values[0].children]):
                    [values[0].remove_widget(s) for s in values[1]]

                if condition['condition'] < size[0] and not any([s== p for s in values[1] for p in values[0].children]):
                    [values[0].add_widget(s) for s in values[1]]
                    
                if condition['condition'] > size[0] and not any([s== p for s in values[2] for p in values[0].children]):
                    [values[0].add_widget(s) for s in values[2]]
                    
                if condition['condition'] < size[0] and any([s== p for s in values[2] for p in values[0].children]):
                    [values[0].remove_widget(s) for s in values[2]]
                
        for values in self.register_remover:
            for condition in values[2]:
                contador += 1
                if condition['condition'] > size[0] and values[1] in values[0].children:
                    values[0].remove_widget(values[1])
                elif condition['condition'] < size[0] and not values[1] in values[0].children:
                    values[0].add_widget(values[1])
                    
        for values in self.register:
            for condition in values[1]:
                contador += 1
                value_atual = eval(condition['methods'])(size,condition['condition'],condition['values'])
                if value_atual != getattr(values[0], condition['property']):
                    setattr(values[0],condition['property'], value_atual)
        # print(' Contador: ',contador)

    def update(self, *args):
        # self.contador += 1-
        # print('Acessado - update',self.contador)
        # s1.instance_time('001- antes update StateVariable')
        # s1.memory_size(os.getpid(),'001- antes update StateVariable')
        size = args[1]
        try:
            if size[0] > 1200 and self.aux:
                self.aux = False
                self.update_condition(size)
 
            if size[0] < 1200 and not self.aux:
                self.aux = True
                self.update_condition(size)

            # print('numero de interações: ',contador)
            # self.change_graphics(size)
            # s1.instance_time('002- depois update StateVariable')
            # s1.memory_size(os.getpid(),'002- antes update StateVariable')
        except Exception as e:
            Error(self,'StateVariable').msg(e)
            




    