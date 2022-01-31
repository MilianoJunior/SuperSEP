from libs.baseclass.model.connection.connection_db import DataBase 
import libs.baseclass.model.tables_create as in_tables
from typing import NoReturn
import pandas as pd
import inspect
import os



class ModelConstrutor():
    '''
    Description
    -----------
        Estabelece conexão com o banco de dados. Cria tabelas. Persiste, altera, deleta e lê dados nas tabelas.
        
    '''
    register: list = []
    if inspect.ismodule(in_tables):
        for name, obj in inspect.getmembers(in_tables):
                if inspect.isclass(obj) and name != 'DataBase':
                    globals()[name] = obj
                    register.append(eval(name))
    conn = None
                    
    def __init__(self,**kwargs)->NoReturn:
        
        super().__init__(**kwargs)
        
    def model_connect(self)->object:
        '''
        Description
        -----------
            Faz a conexão com o banco de dados.
            
        Returns
        -------
            object, senão False

        '''
        db = DataBase()
        db.connect()
        self.conn = db.conn
        cursor = db.conn.cursor()
        return cursor
        
    def list_tables(self)->list:
        '''
        Description
        -----------
            Verifica se existem tabelas a ser registradas. Se houver, registra as tabelas.

        Returns
        -------
            list com as tabelas registradas

        '''
        try:
            cursor = self.model_connect()
            query_list = "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"
            cursor.execute(query_list)
            registered_tables = [t[0] for t in cursor.fetchall()]
            for table in self.register:
                chave = True
                for table_existing in registered_tables:
                    if table_existing == table.name:
                        chave = False
                if chave:
                    if table()():
                        registered_tables.append(table.name)
            self.conn.close()
            
            return registered_tables
        
        except Exception as e:
            print('Erro: ',e)
            return e
        
    def update(self,main: str, row: int, values: dict)->bool:
        '''
        Description
        -----------
            Atualiza dados de uma tabela a partir de uma linha e valores repassados como argumento, retornando o resultado do pedido.
            
        Parameters
        ----------
        main : str
            Nome da tabela
        row : int
            id chave da tabela
        values : dict
            valores de atualização

        Returns
        -------
        True se os dados forem atualizados, senão False

        '''
        try:
            cursor = self.model_connect()
            query_list = "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"
            cursor.execute(query_list)
            registered_tables = [t[0] for t in cursor.fetchall()]
            for table in self.register:
                chave = True
                for table_existing in registered_tables:
                    if table_existing == table.name:
                        chave = False
                if chave:
                    if table()():
                        registered_tables.append(table.name)
            self.conn.close()
        except Exception as e:
            
            return e
        
        
    def delete(self, name: str, row: int)->bool:
        '''
        Description
        -----------
            Apaga os dados de uma determina tabela e linha conforme os argumentos, retornando o resultado do pedido.
            
        Parameters
        ----------
        main : str
            Nome da tabela
        row : int
            id chave da tabela

        Returns
        -------
        True se os dados forem apagados, senão False

        '''
        try:
            pass
        
        except Exception as e:
            return e
        
    def rows(self,main: str)->list:
        '''
        Description
        -----------
            Utilizado para saber os nomes da colunas para determina tabela, conforme argumentos, retornando o resultado do pedido.
            
        Parameters
        ----------
        main : str
            Nome da tabela

        Returns
        -------
        List como os nomes das colunas, senão False

        '''
        cursor = self.model_connect()
        query_list = query = f'SELECT * FROM {main}'
        cursor.execute(query_list)
        names = list(map(lambda x: x[0], cursor.description))
        
        return names
        
    def write(self,widget: dict)->bool:
        '''
        Description
        -----------
            Persiste os dados, retornando o resultado do pedido.
            
        Parameters
        ----------
        widget : dict
            variável que compoem os dados da interface

        Returns
        -------
        True se os dados forem persistidos, senão False

        '''
        try:
            cursor = self.model_connect()
            tabela = 'main_logic'
            tuple_query: list = []
            for s in widget.keys():
                tuple_query.append(str(widget[s]))
            rows: str = '(main,screen,name,struct,content,properties,actions,widgets)'
            query = f"insert into {tabela} {rows} values (?,?,?,?,?,?,?,?)"
            cursor.execute(query,tuple(tuple_query)) 
            self.conn.commit()
            self.conn.close()
            print('Salvo com sucesso')
            return True
        
        except Exception as e:
            print('Erro na escrita: ', e)
            return e
        
    def read_select(self, column: str, valor: str)->list:
        '''
        Description
        -----------
            Consulta o banco de dados, retornando alguns dados da tabela, conforme argumentos, retornando o resultado do pedido.
            
        Parameters
        ----------
        column : str
            Nome da coluna
        valor: str
            Valor de busca
        Returns
        --------
        List com os dados, senão False

        '''
        try:
            self.model_connect()
            tabela = 'main_logic'
            cursor = self.conn.cursor()
            query = f'SELECT * FROM {tabela} WHERE {column} = ?'
            cursor.execute(query,(valor,))
            dados = []
            for linha in cursor.fetchall():
                dados.append(list(linha))
            self.conn.close()
            return dados, self.rows(tabela)
        
        except Exception as e:
            
            return e
        
    def read(self,name: str)->list:
        '''
        Description
        -----------
            Consulta o banco de dados, retornando todos os dados da tabela, conforme argumentos, retornando o resultado do pedido.
            
        Parameters
        ----------
        main : str
            Nome da tabela

        Returns
        --------
        List com os dados, senão False

        '''
        try:
            self.model_connect()
            cursor = self.conn.cursor()
            query = f'SELECT * FROM {name}'
            cursor.execute(query)
            dados = []
            for linha in cursor.fetchall():
                dados.append(list(linha))
            self.conn.close()
            return dados, self.rows(name)
        
        except Exception as e:
            
            return e
        
    
        
    
