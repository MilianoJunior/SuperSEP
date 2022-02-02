from kivymd.uix.label import MDLabel
from typing import NoReturn
from kivymd.uix.boxlayout import MDBoxLayout
from sys import exc_info
from os import path
from kivy.base import ExceptionHandler, EventLoopBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.base import ExceptionManager

class Singleton(type):

    __instances ={}
    contador = 0

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
            cls.contador = 0
        return cls.__instances[cls]

class E(ExceptionHandler):
    dialog = None

    def __init__(self, obj):
        self.obj = obj

    def callback_not(self, dt):
        self.stopTouchApp()
        self.dialog.dismiss()

    def msg(self, texto, callback):
        if not self.dialog:
            self.dialog = MDDialog(
                text=texto,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        text_color=get_color_from_hex("#27979d"),
                        on_release=callback,
                    ),
                ],
            )
        self.dialog.open()
        Clock.schedule_once(callback, 20)

    def stopTouchApp(self):
        EventLoop = EventLoopBase()
        print('EventLoop.status: ',EventLoop.status)
        '''Stop the current application by leaving the main loop'''
        if EventLoop is None:
            return
        if EventLoop.status in ('stopped', 'closed'):
            return
        if EventLoop.status != 'started':
            if not EventLoop.stopping:
                EventLoop.stopping = True
                Clock.schedule_once(lambda dt: self.obj.stopTouchApp(), 0)
            return
        EventLoop.close()

    def handle_exception(self, inst):
        self.msg(str(inst), self.callback_not)
        return ExceptionManager.PASS

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




#from kivymd.uix.label import MDLabel
#from typing import NoReturn
#from kivymd.uix.boxlayout import MDBoxLayout
#import sys,os
## from desempenho import Desempenho
#
## s2 = Desempenho()
#
#class Singleton(type):
#
#    __instances ={}
#    contador = 0
#
#    def __call__(cls, *args, **kwargs):
#        if cls not in cls.__instances:
#            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
#            cls.contador = 0
#        return cls.__instances[cls]
#
#class Error(metaclass=Singleton):
#
#    error_msg = None
#
#    def __init__(self, name: str, obj)->NoReturn:
#        self.obj = obj
#        # s2.instance_time('4-Error')
#        # s2.memory_size(os.getpid(),'Error')
#
#
#    def msg(self, e: str)->NoReturn:
#        print('##################')
#        print('Classe error: ',self.contador)
#        print('##################')
#        exc_type, exc_value, exc_tb = sys.exc_info()
#        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#        details = {
#                      'arquivo': fname,
#                      'linha'  : exc_tb.tb_lineno,
#                      'type'    : exc_type.__name__,
#                      'message' : e,
#                      'path'    : os.path.abspath(__file__),
#                    }
#
#        self.data = details
#        print(details)
#        if self.error_msg is None:
#            self.error_msg = True
#            texto = ''
#            for name,value in self.data.items():
#                texto += f'\n{str(name)} : {value}'
#            layout_error = MDBoxLayout()
#            layout_error.add_widget(MDLabel(text=str(texto),
#                                            halign="center"))
#            self.obj.add_widget(layout_error)







