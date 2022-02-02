from libs.baseclass.assets.color import *
#from libs.baseclass.assets.imagens import *

remove_logo = [
                {
                    'name'      : 'menu_remove',
                    'condition' : 1200,
                },

    ]

img_properties = [
                    {
                        'name'      : 'menu_main',
                        'condition' : 1200,
                        'methods'   : 'methods_orientation',
                        'property'  : 'color',
                        'values'    : [cores['primary'],cores['primary']],
                    },

            ]
box_links = [

                       {
                           'name'      : 'menu_main',
                           'condition' : 1200,
                           'methods'   : 'methods_orientation',
                           'property'  : 'orientation',
                           'values'    : ['horizontal','vertical'],
                       },
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : [[None,1],[.2,.9]],
                        },
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'width',
                            'values'    : [300,200],
                        },
                       {
                           'name'      : 'menu_main',
                           'condition' : 1200,
                           'methods'   : 'methods_orientation',
                           'property'  : 'padding',
                           'values'    : [[50,50,0,50],[1,1,1,1]],
                       },
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'pos_hint',
                            'values'    : [{'center_x': .3, 'center_y':.5},{'center_x': .1, 'center_y':.5}],
                        },
                   ]
labels_menu  = [
                       {
                           'name'      : 'menu_main',
                           'condition' : 1200,
                           'methods'   : 'methods_orientation',
                           'property'  : 'font_style',
                           'values'    : ['Subtitle1','Overline'],
                       },

                ]

box_card_properties = [
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'orientation',
                            'values'    : ['horizontal','horizontal'],
                        },
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint_x',
                            'values'    : [None,1],
                        },
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'width',
                            'values'    : [150,1],
                        },
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'pos_hint',
                            'values'    : [{"center_x": .8, "center_y": .5},{"center_x": .4, "center_y": .5}],
                        },
                   ]

card_icons = [
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'orientation',
                            'values'    : ['horizontal','horizontal'],
                        },
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : [(None,None),(None,None)],
                        },
                        {
                            'name'      : 'menu_main',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size',
                            'values'    : [[50,50],[30,30]],
                        },
                        # {
                        #     'name'      : 'menu_main',
                        #     'condition' : 1200,
                        #     'methods'   : 'methods_orientation',
                        #     'property'  : 'pos_hint',
                        #     'values'    : [{'x': .5, 'y': .5},{"x": .5, "y": .5}],
                        # },

                   ]
icons_toltip = [

                {
                    'name'      : 'menu_main',
                    'condition' : 1200,
                    'methods'   : 'methods_orientation',
                    'property'  : 'user_font_size',
                    'values'    : ['24sp','14sp'],
                },
    ]