from kivymd.uix.label import MDLabel
from typing import NoReturn
from kivymd.uix.boxlayout import MDBoxLayout
import sys,os
# from desempenho import Desempenho

# s2 = Desempenho()

class Singleton(type):
    
    __instances ={}
    contador = 0
        
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
            cls.contador = 0
        return cls.__instances[cls]

class Error(metaclass=Singleton):
    
    error_msg = None
    
    def __init__(self, name: str, obj)->NoReturn:
        self.obj = obj
        # s2.instance_time('4-Error')
        # s2.memory_size(os.getpid(),'Error')
        

    def msg(self, e: str)->NoReturn: 
        print('##################')
        print('Classe error: ',self.contador)
        print('##################')
        exc_type, exc_value, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        details = {
                      'arquivo': fname,
                      'linha'  : exc_tb.tb_lineno,
                      'type'    : exc_type.__name__,
                      'message' : e,
                      'path'    : os.path.abspath(__file__),
                    }

        self.data = details
        print(details)
        if self.error_msg is None:
            self.error_msg = True
            texto = ''
            for name,value in self.data.items():
                texto += f'\n{str(name)} : {value}'
            layout_error = MDBoxLayout()
            layout_error.add_widget(MDLabel(text=str(texto),
                                            halign="center"))
            self.obj.add_widget(layout_error)
            
            
            
            
            
            
            
            