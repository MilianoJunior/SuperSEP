from typing import Type
from libs.baseclass.observer.interfaces.observer import Observador

class SingletonMeta(type):
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            
        return cls._instances[cls]


class Properties(metaclass=SingletonMeta):

    objetos: list = []
    
    def addObjeto(self, objeto: Type[Observador], name: str):
        
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨**')
        print('Registrando o objeto com nome: ',name)
        print('Objeto: ', objeto)
        print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        self.objetos.append({'name': name ,'objeto':objeto})
        
    def get_registers(self):
        
        for objeto in self.objetos:
            print(objeto.name)
            print('----')
        return self.objetos
    
    def msg(self):
        
        for objeto in self.objetos:
            print('update:   ')
            print(objeto['name'])
            objeto['objeto'].update()
            print(objeto['objeto'].__dict__)
    

    