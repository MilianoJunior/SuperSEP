from libs.baseclass.assets.color import cores
from libs.baseclass.exception_error import Error
from libs.baseclass.utils.posicoes import *

try:
    '''
    Layout SuperSEP
    '''
    
    '''
            Componentes do Menu: l1_logo l2_links, l3_icon_config
    '''
    size_menu      = [[x1,y1],[x2,y2]]
    pos_menu       = [{'x':posx1,'y':posy1},{'x':posx2,'y':posy2}]
    color_menu     = cores['background']
    # composição l1_logo: Image
    size_logo      = [[x11,y11],[x22,y22]]
    pos_logo       = [{'x':posx11,'y':posy11},{'x':posx22,'y':posy22}]
    color_logo     = cores['background']
    # composição l2_links: MDLabels
    size_links      = [[x33,y33],[x44,y44]]
    pos_links       = [{'x':posx33,'y':posy33},{'x':posx44,'y':posy44}]
    color_links     = cores['background']
    # composição l2_icons: Icons
    size_icons      = [[x55,y55],[x66,y66]]
    pos_icons       = [{'x':posx55,'y':posy55},{'x':posx66,'y':posy66}]
    color_icons     = cores['background']
    
    '''
            Componentes do Menu lateral: l1_icons,
    '''
    size_menu_lateral      = [[x5,y5],[x6,y6]]
    pos_menu_lateral       = [{'x':posx5,'y':posy5},{'x':posx6,'y':posy6}]
    color_menu_lateral     = cores['background_widget']
    
    # composição l1_icons: icons is 12, igual para todos
    size_nav_lateral =[[x77,y77],[x88,y88]]
    pos_nav_lateral = [{'center_x':posx77,'y':posy77},{'center_x':posx88,'y':posy88}]
    cores_menu_lateral = cores['secundary']
        
    '''
            Componentes do sidebar: l1_search, l2_user, l3_card_public, l4_card_level
    '''
    size_sidebar      = [[x3,y3],[x4,y4]]
    pos_sidebar       = [{'x': posx3,'y':posy3},{'x':posx4,'y':posy4}]
    color_sidebar     = cores['sidebar']
    
    # composição l1_search: Button
    size_sidebar_search      = [[x330,y330],[x440,y440]]
    pos_sidebar_search       = [{'x': posx330,'y':posy330},{'x':posx440,'y':posy440}]
    color_sidebar_search     = cores['sidebar']

    # composição l2_user: card, image, label, icon
    size_sidebar_user      = [[x331,y331],[x441,y441]]
    pos_sidebar_user       = [{'x': posx331,'y':posy331},{'x':posx441,'y':posy441}]
    color_sidebar_user     = cores['sidebar']
    
    # composição l3_card_public
    size_sidebar_table      = [[x332,y332],[x442,y442]]
    pos_sidebar_table       = [{'x': posx332,'y':posy332},{'x':posx442,'y':posy442}]
    color_sidebar_table     = cores['sidebar']
    # composição l4_graph
    size_sidebar_graph      = [[x333,y333],[x443,y443]]
    pos_sidebar_graph       = [{'x': posx333,'y':posy333},{'x':posx443,'y':posy443}]
    color_sidebar_graph     = cores['sidebar']
    
    '''
        Screens Main
    '''
    size_screens = [[xc1,yc1],[xc2,yc2]]
    pos_screens  =  [{'x':posxc1,'y':posyc1},{'x':posxc2,'y':posyc2}]
    
    # def imprime_layout(tipo,size,pos):
    #     print('*********************')
    #     print(f'{tipo} size: ',size)
    #     print(f'{tipo} pos: ',pos)
    #     print('*********************')
        
    # imprime_layout('Menu', size_menu, pos_menu)
    # imprime_layout('Menu logo', size_logo, pos_logo)
    # imprime_layout('Menu links', size_links, pos_links)
    # imprime_layout('Menu icons', size_icons, pos_icons)
    # imprime_layout('Menu Lateral', size_menu_lateral, pos_menu_lateral)
    # imprime_layout('Menu Lateral nav', size_nav_lateral, pos_nav_lateral)
    # imprime_layout('Sidebar', size_sidebar, pos_sidebar)
    # imprime_layout('Sidebar user', size_sidebar_user, pos_sidebar_user)
    # imprime_layout('Sidebar search', size_sidebar_search, pos_sidebar_search)
    # imprime_layout('Sidebar table', size_sidebar_table, pos_sidebar_table)
    # imprime_layout('Sidebar graph', size_sidebar_graph, pos_sidebar_graph)
    # print('#############################################################')
    # imprime_layout('Screens', size_screens, pos_screens)


    
                
    
    
        
    # composição l2_user: card, image, label, icon
    
        # card
        # image
        # label
        # icon
    
    # composição l3_card_public: table
        # table:


    '''
                Componentes do Menu lateral: l1_icons,
    '''
    
    '''
            Componentes do body: screens
    '''
    
except Exception as e:
    print('--------------')
    print(' Error: ',e)
    print('--------------')
    Error('layout_size').msg(e)


















# #----------------------
# # configurações de size do menu
# widht_menu = 624
# height_menu = 70
# #-----------------------
# # proporções em percentual
# x = widht_menu/widht_all
# y = height_menu/height_all

# pos_y = 1-y
# pos_x = 0
# # proporções dos elementos internos do menu