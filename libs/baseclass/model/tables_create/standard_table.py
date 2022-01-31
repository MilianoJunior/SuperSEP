from libs.baseclass.model.connection.connection_db import DataBase

class StandardTable(DataBase):
    '''
    Description
    -----------
        Tabela padrão, serve com base para criação de novas tabelas.
    '''
    
    name = 'standard_table'
    
    def __call__(self)->bool:
        '''
        Description
        -----------
            Cria uma nova tabela.
        Returns
        -------
            True se a tabela for criada, senão False

        '''
        
        try:
            query = self.table_register()
            if self.table_create(query):
                return True
            else:
                return False
        except Exception as e:
            return e
        
    def table_register(self)->str:
        '''
        Description
        ----------
            Método que gera uma query 

        Returns
        -------
        str
            query para criar colunas e tipos para o banco de dados.

        '''
        
        register: str = '(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,name text,struct text,content text,properties text,actions text,widgets text)'
        query_table = f"CREATE TABLE IF NOT EXISTS {self.name} {register}"

        return query_table
