import time
from memory_profiler import memory_usage
# from libs.baseclass.utils.verification import Convert
import seaborn as sns
import pandas as pd
import os,psutil
from sys import getsizeof
import matplotlib.pyplot as plt

# pandas = Convert()
df = pd.DataFrame(data=[],columns=['name','tempo','desempenho','memoria','custo'])
# pd = pandas.convert_data_pd([],['name','desempenho','memoria'])
class SingletonMeta(type):
    _instances = {}
    inicio = 0
    point = 0
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            cls.inicio = time.time()
            cls.point = 0
        return cls._instances[cls]
   
class Desempenho(metaclass=SingletonMeta):

    def instance_time(self,instance):
        termino = time.time() - self.inicio
        
        if self.point == 0:
            df.loc[self.point,'name'] = instance
            df.loc[self.point,'tempo'] = termino
            df.loc[self.point,'desempenho'] = termino
        else:
            df.loc[self.point,'name'] = instance
            df.loc[self.point,'tempo'] = termino
            df.loc[self.point,'desempenho'] = termino - df['tempo'][self.point-1]
        
    def memory_size(self,pid,name):
        mem_usage = memory_usage(pid, interval=.2, timeout=1, max_usage=True)
        if self.point == 0:
            df.loc[self.point,'memoria'] = mem_usage
            df.loc[self.point,'custo'] = mem_usage
        else:
            df.loc[self.point,'memoria'] = mem_usage
            df.loc[self.point,'custo'] = mem_usage-df['memoria'][self.point-1]
        self.point += 1
    def grafico(self):
        print('**********************************************')
        for t in range(len(df)):
            print('   ')
            for p in df.columns:
                print(t,p,':',df[p][t])
        print('**********************************************')

# Total picle Gauge-UG01:  326888
# Total picle Gauge-UG01:  93648

# # Total picle UG-01:  213296
# a = globals().copy()
# s3 = 0
# # Total picle View Menus:  201104

# from pympler import asizeof
# # maior = 0
# # name_maior = ''
# for name,value in a.items():
#     print(name)
#     print(value)
#     try:
#         ta = asizeof.asizeof(value)
#         print('pympler size: ',ta)
#         s3 += ta
#     except:
#         print('pympler size: error')
#     # print('----')
# print('Total picle UG-02 gauge: ',s3)
# # print('Name: ',name,' tamanho: ',maior)

        
# '''
# 04/11/2021 - 1.71 segundos 1-main
# 05/11/2021 - 1.96 segundos 1-main [ menus, principal]
# 05/11/2021 - 7.78 segundo 00-ultima chamada [ menus, principal]

# '''

# Modelo de conexão = M.2
# protocolo de comunicação = NVMe