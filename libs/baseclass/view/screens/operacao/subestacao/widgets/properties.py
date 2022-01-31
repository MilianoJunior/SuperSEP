from libs.baseclass.assets.color import *


width_all = 860
height_all = 610

widget_screens = 550
height_screens = 535

x = [widget_screens/width_all,1]
y = [height_screens/height_all,.54]

pos_x = 72/width_all
pos_y = 0


print('proporção da largura principal: ', round(x,2))

sidebar_properties = [
                        {  
                            'name'      : 'builder_ug01',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'md_bg_color',
                            'values'    : [cores['widget'],cores['widget']],
                        },
                      ]

card_properties = [

                      {  
                          'name'      : 'card_UG01_gauge',
                          'condition' : 1200,
                          'methods'   : 'methods_orientation',
                          'property'  : 'md_bg_color',
                          'values'    : [cores['widget'],cores['widget']],
                      },
                      {  
                          'name'      : 'card_UG01_gauge',
                          'condition' : 1200,
                          'methods'   : 'methods_orientation',
                          'property'  : 'size_hint',
                          'values'    : [[x[0],y[1]],[.98,y[1]]],
                      },
                      {  
                          'name'      : 'card_UG01_gauge',
                          'condition' : 1200,
                          'methods'   : 'methods_orientation',
                          'property'  : 'pos_hint',
                          'values'    : [{'center_x': .5, 'center_y':.5},{'x': 0, 'center_y':.5}],
                      },
                      {  
                          'name'      : 'card_UG01_gauge',
                          'condition' : 1200,
                          'methods'   : 'methods_orientation',
                          'property'  : 'radius',
                          'values'    : [[15,15,15,15],[15,15,15,15]],
                      },

                    ]