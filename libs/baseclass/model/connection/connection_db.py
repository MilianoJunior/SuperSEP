import sqlite3
import os
from typing import NoReturn

class Singleton(type):
    '''
    Description
    -----------
        Metaclasse singleton, com objetivo de criar uma única instância do banco de dados, para gerar sincronismo.
    '''
    
    __instances ={}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class DataBase(metaclass=Singleton):
    '''
    Description
    -----------
        Classe para conexão do banco de dados
    '''

    connection = None
    conn = None
    name = 'database'
    
    def connect(self)->NoReturn:
        '''
        Description
        -----------
            Metodo que conecta o banco de dados na pasta assets.
        '''
        
        if self.connection is None:
            path = os.path.join(os.environ["ENGESEP_ASSETS"],'DB','supersep.db')
            self.conn = sqlite3.connect(path)
            print('Objeto criado')
        else:
            print('Objeto já esta criado')
            
    def table_create(self,query: str)->bool:
        '''
        Description
        -----------
            Método que recebe uma query (tipe str), chama o método connect e cria uma tabela
            
        Parameters
        ----------
        query : str
            variável em format sql

        Returns
        -------
        True se a tabela for criada, senão False

        '''
        try:
            if self.conn is None:
                self.connect()
            cursor = self.conn.cursor()
            cursor.execute(query)
            return True
        except Exception as e:
            raise RuntimeError('Não foi possivel cria a tabela: {str(e)}')
        


            
            
            