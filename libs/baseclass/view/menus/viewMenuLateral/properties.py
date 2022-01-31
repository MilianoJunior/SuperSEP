from libs.baseclass.assets.color import *
from libs.baseclass.utils.layout_supersep import *

menu_lateral_properties = [
                            {  
                                'name'      : 'menu_lateral_main',
                                'condition' : 1200,
                                'methods'   : 'methods_orientation',
                                'property'  : 'orientation',
                                'values'    : ['vertical','horizontal'],
                            },
                            {  
                                'name'      : 'menu_lateral_main',
                                'condition' : 1200,
                                'methods'   : 'methods_orientation',
                                'property'  : 'md_bg_color',
                                'values'    : [cores['secundary'],cores['secundary']],
                            },
                            {  
                                'name'      : 'menu_lateral_main',
                                'condition' : 1200,
                                'methods'   : 'methods_orientation',
                                'property'  : 'size_hint',
                                'values'    : size_menu_lateral,
                            },
                            {  
                                'name'      : 'menu_lateral_main',
                                'condition' : 1200,
                                'methods'   : 'methods_orientation',
                                'property'  : 'pos_hint',
                                'values'    : pos_menu_lateral,
                            }
                          ]