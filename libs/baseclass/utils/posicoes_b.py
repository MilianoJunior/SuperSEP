# from libs.baseclass.assets.color import cores
# from libs.baseclass.utils.methods import metodo_percentage_size
# from libs.baseclass.exception_error import Error

# try:
#     # configurações do layout geral-
#     width_all  = 1920
#     height_all = 1080
#     '''
#         Componentes do layout: Menu, sidebar, menu lateral, body
#     '''
#     #--- Menu ----
#     width_menu  = 1400
#     height_menu = 124
#     x1          = metodo_percentage_size(width_all, width_menu)
#     x2          = 1
#     y1          = metodo_percentage_size(height_all, height_menu)
#     y2          = y1
#     posx1       = 0
#     posx2       = 0
#     posy1       = 1-y1
#     posy2       = 1-y1
#     #---sidebar----
#     width_sidebar  = 520
#     height_sidebar = 1080
#     x3             = metodo_percentage_size(width_all, width_sidebar)
#     x4             = 1
#     y3             = 1
#     y4             = x3
#     posx3          = 1-x3
#     posx4          = 0
#     posy3          = 0
#     posy4          = 0
    
#     #--- Menu Lateral ---
#     width_menu_lateral  = 124
#     height_menu_lateral = 956
#     x5                  = metodo_percentage_size(width_all, width_menu_lateral)
#     x6                  = 1
#     y5                  = metodo_percentage_size(height_all, height_menu_lateral)
#     y6                  = x5
#     posx5               = 0
#     posx6               = 0
#     posy5               = 0
#     posy6               = 1-(x5+y1)
    
#     #--- body -----------
#     width_screens   = 1243
#     height_screens  = 956
#     xc1             = metodo_percentage_size(width_all,width_screens)
#     xc2             = 1
#     yc1             = metodo_percentage_size(height_all,height_screens)
#     yc2             = 1-(y2+y6+x3)
#     posxc1          = x5
#     posxc2          = 0
#     posyc1          = 0
#     posyc2          = x3
    
    
#     # menu
#     size_menu      = [[x1,y1],[x2,y2]]
#     pos_menu       = [{'x':posx1,'y':posy1},{'x':posx2,'y':posy2}]
#     color_menu     = cores['background']
    
#     # sidebar
#     size_sidebar      = [[x3,y3],[x4,y4]]
#     pos_sidebar       = [{'x': posx3,'y':posy3},{'x':posx4,'y':posy4}]
#     color_sidebar     = cores['sidebar']
    
#     # menu lateral
#     size_menu_lateral      = [[x5,y5],[x6,y6]]
#     pos_menu_lateral       = [{'x':posx5,'y':posy5},{'x':posx6,'y':posy6}]
#     color_menu_lateral     = cores['background_widget']
    
#     # screens
#     size_screens  = [[xc1,yc1],[xc2,yc2]]
#     pos_screens   = [{'x':posxc1,'y':posyc1},{'x':posxc2,'y':posyc2}]
#     color_screens = cores['background_widget']

#     def imprime_layout(tipo,size,pos):
#         print('*********************')
#         print(f'{tipo} size: ',size)
#         print(f'{tipo} pos: ',pos)
#         print('*********************')
        
#     imprime_layout('menu principal',size_menu,pos_menu )
#     imprime_layout('menu sidebar',size_sidebar,pos_sidebar)
#     imprime_layout('menu lateral',size_menu_lateral,pos_menu_lateral)
#     imprime_layout('screen',size_screens,pos_screens)

# except Exception as e:
#     print('--------------')
#     print(' Error: ',e)
#     print('--------------')
#     Error('layout_size').msg(e)