from typing import NoReturn
from libs.baseclass.exception_error import Error

class BuilderWidgets:
    '''
    Description
    -----------
        SuperClasse Widget
    '''
    
    def __init__(self, name: str)->NoReturn:
        self.name = name
                    
    def builder_properties(self, widget: object, properties: list=None)->NoReturn:
        try:
            for name,value in properties.items():
                setattr(widget, name, value)
                
        except Exception as e:
            Error(self).msg(e)
            
    def builder_methods(self,widget: object, methods: dict=None)->NoReturn:
        try:
            for name,value in methods.items():
                setattr(widget, name, value)
                
        except Exception as e:
            Error(self).msg(e)
            
    def change_screen(self, *args):
        print(args)