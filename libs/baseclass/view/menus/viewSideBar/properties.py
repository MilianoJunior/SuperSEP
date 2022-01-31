'''
    Description
    ----------
        propriedades do layout SideBar
'''

from libs.baseclass.assets.color import *
from libs.baseclass.utils.layout_supersep import *

# proporções em percentual

sidebar_properties = [
                        {  
                            'name'      : 'sidebar_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'md_bg_color',
                            'values'    : [cores['widget'],cores['widget']],
                        },
                        {  
                            'name'      : 'sidebar_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : size_sidebar,
                        },
                        {  
                            'name'      : 'sidebar_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'pos_hint',
                            'values'    : pos_sidebar,
                        },
                      ]
search_properties = [
                        {  
                            'name'      : 'sidebar_search',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'md_bg_color',
                            'values'    : [color_sidebar_search,color_sidebar_search],
                        },
                        {  
                            'name'      : 'sidebar_search',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : size_sidebar_search,
                        },
                        {  
                            'name'      : 'sidebar_search',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'pos_hint',
                            'values'    : pos_sidebar_search,
                        },
                      ]

user_properties = [
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'md_bg_color',
                            'values'    : [color_sidebar_user,color_sidebar_user],
                        },
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : size_sidebar_user,
                        },
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'pos_hint',
                            'values'    : pos_sidebar_user,
                        },
                      ]

table_properties = [
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'md_bg_color',
                            'values'    : [color_sidebar_table,color_sidebar_table],
                        },
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : size_sidebar_table,
                        },
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'pos_hint',
                            'values'    : pos_sidebar_table,
                        },
                      ]

graph_properties = [
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'md_bg_color',
                            'values'    : [color_sidebar_graph,color_sidebar_graph],
                        },
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : size_sidebar_graph,
                        },
                        {  
                            'name'      : 'sidebar_user',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'pos_hint',
                            'values'    : pos_sidebar_graph,
                        },
                      ]