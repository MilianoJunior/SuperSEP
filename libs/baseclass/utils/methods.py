from typing import NoReturn
import inspect



def metodo_comparar_instance(value_a: object, value_b: object)->bool:
    '''
        compara dois objetos e retorna True se são da mesma instancia, ou False se não..
    '''
    try:
        return type(value_a).__name__ == type(value_b).__name__
    except Exception as e:
        raise RuntimeError(f'Erro função metodo_comparar_instance, linha 28: {str(e)}')

def metodo_qual_type(value: object)->type:
    '''
        returna o type do objeto.
    '''
    try:
        return type(value).__name__
    except Exception as e:
        raise RuntimeError(f'Erro função metodo_qual_type, linha 46: {str(e)}')

def metodo_dir(value: object, nivel: int = 0)->NoReturn:
    '''
        Imprime os objetos, type, e valor.
    '''
    try:
        
        for s in dir(value):
            print('nivel',nivel,'NAME: ',s,
                  '\nTYPE: ',type(getattr(value,s)).__name__,
                  '\nVALUE: ',getattr(value,s),
                  '\nCALLABLE: ',callable(getattr(value,s)))
            try:
                print('Fuction value: ',getattr(value,s)())
                print('Atributos: ',inspect.getfullargspec(getattr(value,s)),'\n')
                if inspect.ismetodo(getattr(value,s)) or inspect.isfunction(getattr(value,s)):
                    print('Fuction value: ',getattr(value,s)())
                print('\n')
            except:
                print('\n')
        print(value)
        for s,v in inspect.getmembers(value):
            print('Info: ',s)
            print('Value: ',v)
        print('-----')
        
    except Exception as e:
        
        raise RuntimeError(f'Erro método dir, linha 84: {str(e)}')

def methods_fbind(size:list, reference:int, values:list)-> str:
    '''
        orientação conformado com o tamanho da janela.
    '''
    try: 
        if size[0] > reference:
            
            return values[0]
        
        return values[1]
    
    except Exception as e:
        
        raise RuntimeError(f'Erro método metodo_resp_oreintation, linha 113: {str(e)}')
        
def methods_ajust_percentual(size:list, reference:list, values:list)-> list:
    '''
        orientação conformado com o tamanho da janela.
    '''
    try: 

        return [int(size[0]*values[0][0]),int(size[1]*values[0][1])]
    
    except Exception as e:
        
        raise RuntimeError(f'Erro método metodo_resp_oreintation, linha 113: {str(e)}')
     
def methods_orientation(size:list, reference:int, values:list)-> str:
    '''
        orientação conformado com o tamanho da janela.
    '''
    try: 
        if size[0] > reference:
            
            return values[0]
        
        return values[1]
    
    except Exception as e:
        
        raise RuntimeError(f'Erro método metodo_resp_oreintation, linha 113: {str(e)}')
        
def methods_single(value: list)-> str:
    '''
        orientação conformado com o tamanho da janela.
    '''
    try: 

        return value
    
    except Exception as e:
        
        raise RuntimeError(f'Erro método methods_single, linha 93: {str(e)}')
        
def metodo_resp_size(width:int, height:int, reference:int, list_layouts: list)->list:
    '''
        lista com tamanhos conformados de acordo com o tamanho da janela.
    '''
    try:
        
        if width < reference:
            list_layouts = [(s[0],s[1]) if s[0]>s[1] else (s[1],s[0]) for s in list_layouts]
            print('lista 2',list_layouts)
            return list_layouts 
        else:
            list_layouts = [(s[0],s[1]) if s[0]<s[1] else (s[1],s[0]) for s in list_layouts]
            print('lista 1',list_layouts)
            return list_layouts 
    
    except Exception as e:
        
        raise RuntimeError(f'Erro método metodo_resp_size, linha 146: {str(e)}')
    
def metodo_generic_caller(objeto: object, function_name, *args):
      if hasattr(objeto, function_name):
        function = getattr(objeto, function_name)
        function(*args)
      else:
        pass # Some error handling here
    
    
def metodo_percentage_size(reference: float, size: float):
    '''
    Description
    ----------
        Retorna o valor percentual do layout de referência em relação a composição apontada como argumento
    '''
    try:
        
        return round(size/reference,4)
                     
    except Exception as e:
        
        raise RuntimeError(f'Erro método metodo_percentage_size, linha 121: {str(e)}')
    
    
