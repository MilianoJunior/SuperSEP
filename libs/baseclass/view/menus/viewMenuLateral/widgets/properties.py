from libs.baseclass.assets.color import *
from libs.baseclass.utils.layout_supersep import *

# configurações do layout geral
widht_all = 855
height_all = 610
# ----------------------
# configurações de size do menu
height_menu = 70
#---------------------
y1 = height_menu/height_all
# configurações de size do menu lateral e posicao
# height_menu_lateral = 70
widht_menu_lateral = 76
#-----------------------
width_nav = 62
height_nav = 150
#--------------
y = [(width_nav/widht_menu_lateral),(width_nav/widht_menu_lateral)]
x = [height_nav/(height_all-height_menu),height_nav/(height_all-height_menu)]
#------------------------
pos_x = [0,0]
pos_y = [0,0]

icon = [30,30]

condicao =1200

icons = {  
             'UG'           : ['UG01 e UG021','car-cruise-control'],
             'subestacao'   : ['subestação','transmission-tower'],
             'temperaturas' : ['temperaturas UG01 e UG02','coolant-temperature'],
             'comportas'    : ['controle das comportas','gate'],
             'historico'    : ['histórico de eventos e alarmes','history'],
             'graficos'     : ['gráficos de temperatura','chart-areaspline'],
             'controle'     : ['controle de potência','hydro-power'],
             'matriz'       : ['matriz de sinais','arrange-send-to-back'],
             'relatorios'   : ['relatórios de energia','ballot-outline'],
             'sintonizador' : ['sintonizador PID','tune-vertical'],
             'construtor'   : ['informações sobre o SuperSEP','devices'],
             'banco'        : ['banco de dados','database-outline'],
             'cameras'      : ['monitoramento por cameras','cctv'],
        }


navigation_properties = [

                            {  
                                'name'      : 'navegation_main',
                                'condition' : condicao,
                                'methods'   : 'methods_orientation',
                                'property'  : 'md_bg_color',
                                'values'    : [cores['background'],cores['background']],
                            },
                            {  
                                'name'      : 'navigation_main',
                                'condition' : condicao,
                                'methods'   : 'methods_orientation',
                                'property'  : 'size_hint',
                                'values'    : [[1,1],[1,1]],
                            },

                          ]

card_properties = [

                      {  
                          'name'      : 'navegation_card',
                          'condition' : condicao,
                          'methods'   : 'methods_orientation',
                          'property'  : 'md_bg_color',
                          'values'    : [cores['widget'],cores['widget']],
                      },
                      # {  
                      #     'name'      : 'navegation_card',
                      #     'condition' : condicao,
                      #     'methods'   : 'methods_orientation',
                      #     'property'  : 'size_hint',
                      #     'values'    : [[None,y[0]],[.98,y[1]]],
                      # },
                       {  
                           'name'      : 'navegation_card',
                           'condition' : condicao,
                           'methods'   : 'methods_orientation',
                           'property'  : 'size_hint',
                           'values'    : size_nav_lateral,
                       },
                                         
                        # {  
                        #     'name'      : 'navegation_card',
                        #     'condition' : condicao,
                        #     'methods'   : 'methods_orientation',
                        #     'property'  : 'height',
                        #     'values'    : [13*30,1],
                        # },
                                                     
                      # {  
                      #     'name'      : 'navegation_card',
                      #     'condition' : condicao,
                      #     'methods'   : 'methods_orientation',
                      #     'property'  : 'pos_hint',
                      #     'values'    : [{'center_x': .5, 'center_y':.5},{'x': 0, 'center_y':.5}],
                      # },
                       {  
                           'name'      : 'navegation_card',
                           'condition' : condicao,
                           'methods'   : 'methods_orientation',
                           'property'  : 'pos_hint',
                           'values'    : pos_nav_lateral,
                       },
                      {  
                          'name'      : 'navegation_card',
                          'condition' : condicao,
                          'methods'   : 'methods_orientation',
                          'property'  : 'radius',
                          'values'    : [[15,15,15,15],[15,15,15,15]],
                      },

                    ]

box_properties = [
                        {  
                            'name'      : 'box_icon',
                            'condition' : condicao,
                            'methods'   : 'methods_orientation',
                            'property'  : 'orientation',
                            'values'    : ['vertical','horizontal'],
                        },
                        {  
                            'name'      : 'box_icon',
                            'condition' : condicao,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : [(1,None),(None,1)],
                        },
                        {  
                            'name'      : 'box_icon',
                            'condition' : condicao,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : [(1,None),(None,1)],
                        },
            
                    ]

grid_properties = [
                        {  
                            'name'      : 'box_icon',
                            'condition' : condicao,
                            'methods'   : 'methods_orientation',
                            'property'  : 'cols',
                            'values'    : [1,None],
                        },
                        {  
                            'name'      : 'box_icon',
                            'condition' : condicao,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : [(1,None),(None,1)],
                        },
                        {  
                            'name'      : 'box_icon',
                            'condition' : condicao,
                            'methods'   : 'methods_orientation',
                            'property'  : 'cols',
                            'values'    : [1,None],
                        },
                        {  
                            'name'      : 'box_icon',
                            'condition' : condicao,
                            'methods'   : 'methods_orientation',
                            'property'  : 'rows',
                            'values'    : [None,1],
                        },
            
                    ]

scrool_view_properties = [
                            {  
                                'name'      : 'scrool_view',
                                'condition' : condicao,
                                'methods'   : 'methods_orientation',
                                'property'  : 'size_hint',
                                'values'    : [(1,.9),(.6,1)],
                            },
                            {  
                                'name'      : 'scrool_view',
                                'condition' : condicao,
                                'methods'   : 'methods_orientation',
                                'property'  : 'pos_hint',
                                'values'    : [{'center_x':.5,'center_y':.5},{'center_x':.5,'center_y':.5}],
                            },
 
    
    
    ]

icon_properties = [

                       {  
                           'name'      : 'navegation_icon',
                           'condition' : condicao,
                           'methods'   : 'methods_orientation',
                           'property'  : 'theme_text_color',
                           'values'    : ['Custom','Custom'],
                       },
                       {  
                           'name'      : 'navegation_card',
                           'condition' : condicao,
                           'methods'   : 'methods_orientation',
                           'property'  : 'text_color',
                           'values'    : [cores['background_widget'],cores['background_widget']],
                       },
                       {  
                           'name'      : 'navegation_card',
                           'condition' : 1600,
                           'methods'   : 'methods_orientation',
                           'property'  : 'user_font_size',
                           'values'    : ['24sp','18sp'],
                       },
 
                    ]