from typing import NoReturn
import pandas as pd


class Verification():
    '''
    Description
    -----------
        Métodos auxiliares para tratamento de erros e geração de notificações
    '''
    def instancie_is(self,data: list, types: list)->NoReturn:
        '''
        Description
        -----------
            Verifica se os dados são de acordo com os types, senão gera um erro personalizado           
        '''
        for s in range(0,len(data)):
            if not isinstance(data[s], types[0]):
                raise RuntimeError(f'O argumento {str(data[s])} não é do tipo {str(types[s])} requisitado.')
        
        
class Convert():
    '''
    Description
    -----------
        convert dados para pandas Dataframe
    '''
    def convert_data_pd(self,data: list, columns: list)->pd:
        '''
        Parameters
        ----------
            data : list
                list com os dados da consulta.
            columns : list
                descrição dos nomes das colunas.

        Returns
        -------
            pd : pandas Dataframe
                Pandas dataframe.
        '''
        df = pd.DataFrame(data=data,columns=columns)
        
        return df