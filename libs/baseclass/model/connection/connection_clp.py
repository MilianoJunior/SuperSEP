import sqlite3
from singleton import Singleton

class CLP(metaclass=Singleton):
    
    connection = None
    
    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('superseg')
            self.cursor = self.connection.cursor()
        return self.cursor


# teste1 = CLP()
# print(f'Teste 1 id: {id(teste1)}')

# teste2 = CLP()
# print(f'Teste 2 id: {id(teste2)}')