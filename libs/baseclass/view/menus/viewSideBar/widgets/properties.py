'''
    Description
    ----------
        propriedades dos widgets do SideBar
'''

from libs.baseclass.assets.color import *
from libs.baseclass.utils.layout_supersep import *
from libs.baseclass.utils.methods import *
import random
widht_all = 855
height_all = 610
#----------------------

# table1_properties = [
#                         {  
#                             'name'      : 'sidebar_main',
#                             'condition' : 0,
#                             'methods'   : 'methods_ajust_percentual',
#                             'property'  : 'size',
#                             'values'    : [[.5,.6],[1,.03]],
#                         },

#                       ]


avatar_properties = [
    
                    {  
                        'name'      : 'sidebar_main',
                        'condition' : 1200,
                        'methods'   : 'methods_orientation',
                        'property'  : 'font_style',
                        'values'    : ['Subtitle1','Subtitle2'],
                    },
                    
    ]
card_properties = [
                    {  
                        'name'      : 'sidebar_main',
                        'condition' : 1200,
                        'methods'   : 'methods_orientation',
                        'property'  : 'size_hint',
                        'values'    : [(.8,.6),(.94,.5)],
                    },
    
    
    ]

remove_user = [
                {  
                    'name'      : 'sidebar_remove_user',
                    'condition' : 1200,
                },
    
    ]

remove_table = [
                {  
                    'name'      : 'sidebar_remove_table',
                    'condition' : 1200,
                },
    
    ]

remove_search = [
                {  
                    'name'      : 'sidebar_remove_search',
                    'condition' : 1200,
                },
    
    ]
remove_graph = [
                {  
                    'name'      : 'sidebar_remove_graph',
                    'condition' : 1200,
                },
    
    ]

remove_table1 = [
                {  
                    'name'      : 'sidebar_remove_table',
                    'condition' : 1200,
                },
    
    ]

icons_aviso = {'alarm-light-outline':cores['danger'],
               'alert-plus':cores['alert'],
               'adjust': cores['adjust'],
               'check-outline': cores['check']}




lista_data = {
                'UG01' : { 
                            'state'  : list(icons_aviso.items())[random.choice([i for i in range(4)])],
                            'values' : {
                                            'tensao'         : ['000 V','tensão'],
                                            'potencia_ativa' : ['000 KW','potência ativa'],
                                            'fp'             : ['1 FP','fator de potência'],
                                            'vex'            : ['000 Vex','tensão de exicitação'],
                                            'corrente'       : ['00 A','corrente'],
                                            'pa'             : ['00 kvar','potência reativa'],
                                            'p_a'            : ['00 %','porcentagem do distribuidor em aberto'],
                                            'aex'            : ['00 Aex','corrente de excitação']
                                        }
                          },
                          
                'UG02' : { 
                            'state'  : list(icons_aviso.items())[random.choice([i for i in range(4)])],
                            'values' : {
                                            'tensao'         : ['000 V','tensão'],
                                            'potencia_ativa' : ['000 KW','potência ativa'],
                                            'fp'             : ['1 FP','fator de potência'],
                                            'vex'            : ['000 Vex','tensão de exicitação'],
                                            'corrente'       : ['00 A','corrente'],
                                            'pa'             : ['00 kvar','potência reativa'],
                                            'p_a'            : ['00 %','porcentagem do distribuidor em aberto'],
                                            'aex'            : ['00 Aex','corrente de excitação']
                                        }
                    
                          },
                'Usina/Linha' : { 
                                  'state'  : list(icons_aviso.items())[random.choice([i for i in range(4)])],
                                  'values' : {
                                                'tensao'         : ['000 V','tensão'],
                                                'potencia_ativa' : ['000 KW','potência ativa'],
                                                'fp'             : ['1 FP','fator de potência'],
                                                'corrente'       : ['00 A','corrente'],
                                                'pa'             : ['00 kvar','potência reativa'],
                                              }
                    
                              },
                'Nível' : { 
                                  'state'  : list(icons_aviso.items())[random.choice([i for i in range(4)])],
                                  'values' : {
                                                'tensao'         : ['000 V','tensão'],
                                                'potencia_ativa' : ['000 KW','potência ativa'],
                                                'fp'             : ['1 FP','fator de potência'],
                                                'corrente'       : ['00 A','corrente'],
                                                'pa'             : ['00 kvar','potência reativa'],
                                              }
                    
                              },
                'Temperaturas' : { 
                                  'state'  : list(icons_aviso.items())[random.choice([i for i in range(4)])],
                                  'values' : {
                                                'tensao'         : ['000 V','tensão'],
                                                'potencia_ativa' : ['000 KW','potência ativa'],
                                                'fp'             : ['1 FP','fator de potência'],
                                                'corrente'       : ['00 A','corrente'],
                                                'pa'             : ['00 kvar','potência reativa'],
                                              }
                    
                              }
            
            }