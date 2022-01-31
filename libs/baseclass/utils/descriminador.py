import time
import inspect
from collections.abc import Iterable


class Teste():
    
    idade = 3
    
    def __init__(self, name: str = 'Miliano')->None:
        self.name = name
    
    def leonardo(self, passeando: bool=False)->bool:
        
        if passeando:
            return True
        else: 
            return False
        
'''Verificação recursiva'''
class Descriminador():
    
    armazena_valores = []
    
    def varedura(self, classe)->list:
        
        descriminado: dict = {
                                'name': '',
                                'var_class':[],
                                'metodos':[],
                                'atributos':[],
                                'return_metodos':[]
                            }
        loop = 0
        loop2 = 0
        caixa = dir(classe)[0:5]           
        caixa = [{'obj':classe, 'element': dir(classe)[0:5]}]
        while True:
            
            print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
            for sp in caixa:
                print('Caixa inicial: ',sp, len(caixa))
            try:
                if isinstance(getattr(caixa[loop]['obj'], caixa[loop]['element'][loop]), Iterable):
                    print('1 : indice: ', loop,' valor: ',caixa[loop],' Interavel')
                    base = getattr(caixa[loop]['obj'], caixa[loop]['element'][loop])
                    del caixa[loop]
                    armazen = []
                    for t in dir(base):
                        armazen.append(t)
                    caixa.append({'obj':base['obj'],'element':armazen})
                else:
                    # print('2 : indice: ', loop,' valor: ',caixa[loop], ' Não interavel')
                    self.armazena_valores.append({'obj':caixa[loop]['obj'],'element':caixa[loop]['element'][loop]})
                    del caixa[loop]['element'][loop]
            except Exception as e:
                print(e)
            loop2 += 1
            print('          ')
            # print(loop,'caixa final: ',caixa, len(caixa))
            for ap in self.armazena_valores:
                print('Armazena valores: ',ap)
            print('--------------------------------------------')
            if len(caixa) == 0:
                break
            if loop2 > 10:
                break
        # box31 = [6,7]
        # box21 = [5]
        # box3 = [4]
        # box22 = [box3]
        # box2 = [3, box21,box22]
        # box1 =[1,box2,2, box31]
        # loop = 0
        # loop2 = 0
        # while True:
        #     caixa = box1
        #     print('   ')
        #     print('Caixa inicial: ',caixa, len(caixa))
        #     try:
                
        #         # for s in range(0,st):
        #         if isinstance(caixa[loop], Iterable):
        #             # caixa.append(s)
        #             # print('caixas a verificar: ',caixa[loop])
        #             print('indice: ', loop,' valor: ',caixa[loop],' Interavel')
        #             # loop += 1
        #             base = caixa[loop].copy()
        #             del caixa[loop]
        #             for t in base:
        #                 caixa.append(t)
        #             # del caixa[loop]
        #         else:
        #             # print('valores: ',caixa[loop])
        #             print('indice: ', loop,' valor: ',caixa[loop], ' Não interavel')
        #             self.armazena_valores.append(caixa[loop])
        #             del caixa[loop]
        #     except Exception as e:
        #         print(e)
        #     loop2 += 1
        #     print(loop,'caixa final: ',caixa, len(caixa))
        #     print('Armazena valores: ',sorted(self.armazena_valores))
        #     print('--------------------------------------------')
        #     if len(caixa) == 0:
        #         break
            
        # for s in dir(classe):
        #     print(s)
        #     print(getattr(classe, s))
        #     op1 = getattr(classe, s)
        #     for t in dir(op1):
        #         try:
        #             op2 = getattr(op1,t)
        #             print('            ',t)
        #             print('            ',op2)
        #             print('¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨')
        #         except Exception as e:
        #             pass
        #         for p in dir(op2):
        #             op3 = getattr(op2, p)
        #             print('                  ',p)
        #             print('                  ',op3)
        #     print('---')
        # while True:
        #     descriminado['name'] = str(classe)
        #     for s in dir(classe):
        #         if inspect.ismethod(getattr(classe, s)):
        #             descriminado['metodos'].append(s)
        #             for s, name in inspect.getmembers(getattr(classe, s)):
        #                 print(s,name)
                    # for p in getattr(classe, s): 
                    #     print(p)
                        # print(getattr(getattr(classe, s), p))
                        # print('---')
                # print(s, ':      ',type(s))
                # print(getattr(classe, s))
                # print(type(getattr(classe, s)))
                # print('---------')
            # descriminado['name'] = inspect.getmodule(classe)
            # menbres = inspect.getmembers(classe)
            # for k in menbres:
            #     print(k)
            #     for s in k:
            #         print('       ',s)
                # for p in dir(inspect):
                    
                #     try:
                #         obj = getattr(inspect,p)(k)
                #         if obj:
                #             print(p, k)
                #             print('--')
                #         # print(p,': ',obj)
                #         # for s in obj:
                #         #     print('       ',s)
                #         # print('     ')
                #         # if obj == 'idade' or obj == 3 or obj == 'leonardo' or obj == 'Miliano' or obj == 'name' or obj == 'Teste' or obj == 'passeando':
                #         #     print('1 Elemento da classe: ', 'inspect: ',p,' valor obj : ',obj)
                #         # for r in dir(obj):
                #         #     if r == True or r == 'idade' or r == 3 or r == 'leonardo' or r == 'Miliano' or r == 'name' or r == 'Teste' or r == 'passeando':
                #         #         print('   2 Elemento da classe: ',s, 'inspect: ',p,' valor: ',r)
                #     except Exception as e:
                #         pass
                        # print('------',e,'  :  ',s)
                # time.sleep(0.01)
            # for s in dir(classe):
            #     try:
            #         if inspect.isclass(getattr(classe, s)):
            #             print(getattr(classe, s).__dict__)
            #         if inspect.ismethod(getattr(classe, s)):
            #             descriminado['metodos'].append(s)

            #     except:
            #         pass
                # for p in dir(inspect):
                #     try:
                #         obj = getattr(inspect,p)(getattr(classe, s))
                #         if obj == 'idade' or obj == 3 or obj == 'leonardo' or obj == 'Miliano' or obj == 'name' or obj == 'Teste' or obj == 'passeando':
                #             print('1 Elemento da classe: ',s, 'inspect: ',p,' valor obj : ',obj)
                #         # for r in dir(obj):
                #         #     if r == True or r == 'idade' or r == 3 or r == 'leonardo' or r == 'Miliano' or r == 'name' or r == 'Teste' or r == 'passeando':
                #         #         print('   2 Elemento da classe: ',s, 'inspect: ',p,' valor: ',r)
                #     except Exception as e:
                #         pass
                #             # print('------',e,'  :  ',s)
                #     # time.sleep(0.01)

            # print('-----')
            # print('FIM')
            # print('---')
            # break
        return descriminado
                # if inspect.ismethod(s):
                #     descriminado['metodos'].append(s)
                # print(s)
                # print(type(s))
                # print(getattr(classe, s))
                # print('     ')
                
                
# d = Descriminador()
# op = Teste()

# descri = d.varedura(op) 
# print(descri)              


