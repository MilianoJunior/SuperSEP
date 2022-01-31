from libs.baseclass.model.construtor.construtor_model import ModelConstrutor
from libs.baseclass.utils.verification import Verification, Convert
from typing import NoReturn
import pandas as pd


class ControllerConstrutor(ModelConstrutor):
    '''
    Target
        É um proxy, sendo assim, relaciona as requisições de interfaces para o model, filtrando e compondo dados no formato Dataframe.
        
    '''
    
    def __init__(self)->NoReturn:
        
        r = self.list_tables()
        self.util = Verification()

    def add_data(self,widget: dict)->bool:
        '''
        Description
        -----------
            Avalia os dados e faz o pedido a classe ModelConstrutor para persistir os dados, retornando o resultado do pedido.
            
        Parameters
        ----------
        widget : dict
            variável que compoem os dados da interface

        '''
        self.util.instancie_is([widget],[dict])
        return self.write(widget)
    
    def select_data(self,column: str, value: str):
        '''
        Description
        -----------
            Avalia os dados e faz o pedido para ler os dados, retornando o resultado do pedido.
            
        Parameters
        ----------
        Name : str
            Nome da tabela.

        Returns
        -------
        True se os dados forem persistidos, senão False
        '''
        self.util.instancie_is([column,value],[str,str])
        data,columns = self.read_select(column,value)
        print('select data: ', data,columns)
        pd_query = Convert().convert_data_pd(data,columns)
        
        return pd_query
                    
    def get_data(self,name: str)->pd:
        '''
        Description
        -----------
            Avalia os dados e faz o pedido para ler os dados, retornando o resultado do pedido.
            
        Parameters
        ----------
        Name : str
            Nome da tabela.

        Returns
        -------
        True se os dados forem persistidos, senão False
        '''
        self.util.instancie_is([name],[str])
        data,columns = self.read(name)
        pd_query = Convert().convert_data_pd(data,columns)
            
        return pd_query
    
    def del_data(self,name: str, row: int)->bool:
        '''
        Description
        -----------
            Avalia os dados e faz o pedido para deletar a linha, retornando o resultado do pedido.
            
        Parameters
        ----------
        name : str
            Nome da tabela.
        row : int
            Id da linha a ser deletada.
        '''
        
        self.util.instancie_is([name,row],[str,int])
        self.delete(name, row)
            
            
    def update_data(self,name: str, row: int)->bool:
        '''
        Description
        -----------
            Avalia os dados e faz o pedido para atualizar determinada linha, retornando o resultado do pedido.
            
        Parameters
        ----------
        name : str
            Nome da tabela.
        row : int
            Id da linha a ser alterada.

        Returns
        -------
        True se os dados forem alterados, senão False
        '''
        self.util.instancie_is([name,row],[str,int])
        self.update(name, row)
        
        
        

        