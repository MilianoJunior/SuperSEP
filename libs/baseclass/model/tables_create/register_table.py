from libs.baseclass.model.connection.connection_db import DataBase


class RegisterTable(DataBase):
    '''
    Description
    -----------
        Tabela para registrar as interfaces.
    '''
    
    name = 'main_logic'
    
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
        -----------
            Método que cria a query para nova tabela com colunas, tipos e nome da tabela.
        Returns
        -------
            query_table : str
        '''
        
        register: str = '(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,main text,screen text,name text,struct text,content text,properties text,actions text,widgets text)'
        query_table = f"CREATE TABLE IF NOT EXISTS {self.name} {register}"

        return query_table


