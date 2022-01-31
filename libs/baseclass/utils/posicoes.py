from libs.baseclass.assets.color import cores
from libs.baseclass.utils.methods import metodo_percentage_size
from libs.baseclass.exception_error import Error

try:
    # configurações do layout geral-
    width_all  = 855
    height_all = 610
    '''
        Componentes do layout: Menu, sidebar, menu lateral, body
    '''
    #--- Menu ----
    width_menu  = 625
    height_menu = 70
    x1          = metodo_percentage_size(width_all, width_menu)
    x2          = 1
    y1          = metodo_percentage_size(height_all, height_menu)
    y2          = y1
    posx1       = 0
    posx2       = 0
    posy1       = 1-y1
    posy2       = 1-y1
    #---sidebar----
    width_sidebar  = 200
    height_sidebar = 610
    x3             = metodo_percentage_size(width_all, width_sidebar)
    x4             = 1
    y3             = 1
    y4             = x3
    posx3          = 1-x3
    posx4          = 0
    posy3          = 0
    posy4          = 0
    #--- Menu Lateral ---
    width_menu_lateral  = 70
    height_menu_lateral = 535
    x5                  = metodo_percentage_size(width_all, width_menu_lateral)
    x6                  = 1
    y5                  = metodo_percentage_size(height_all, height_menu_lateral)
    y6                  = x5
    posx5               = 0
    posx6               = 0
    posy5               = 0
    posy6               = 1-(x5+y1)
    #---- Logo -----
    width_menu_logo  = 78
    height_menu_logo = 75
    x11              = metodo_percentage_size(width_menu, width_menu_logo)
    x22              = metodo_percentage_size(width_menu, width_menu_logo)
    y11              = 1
    y22              = 1
    posx11           = 0 
    posx22           = 0 
    posy11           = 0
    posy22           = 0
    #---- links -----
    x33              = (1-x11)/2
    x44              = x33
    y33              = 1
    y44              = 1
    posx33           = 0 + x11
    posx44           = 0 + x22
    posy33           = 0
    posy44           = 0
    #--icons---
    x55             = (1-x11)/2
    x66             = x55
    y55             = 1
    y66             = 1
    posx55          = posx33 + x55
    posx66          = posx44 + x66
    posy55          = 0
    posy66          = 0
    #-- navigation menu ---
    width_nav       = 33
    height_nav      = 30
    x77             = metodo_percentage_size(width_menu_lateral, width_nav)
    x88             = .9
    y77             = .9
    y88             = 1
    posx77          = .5
    posx88          = .5
    posy77          = metodo_percentage_size(height_menu_lateral, 30)
    posy88          = 0
    #-- sidebar search ---
    width_search    = 230
    height_search   = 60
    x330            =  1
    x440            =  1
    y330            =  metodo_percentage_size(height_all,height_search)
    y440            =  0
    posx330         =  0
    posx440         =  0 
    posy330         =  1-y330
    posy440         =  0#1-y440
    #----sidebar user---
    width_user      = 230
    height_user     = 80
    x331            = 1
    x441            = 1
    y331            = metodo_percentage_size(height_all,height_user)
    y441            = .8
    posx331         = 0
    posx441         = 0
    posy331         = 1-(y331 + y330)
    posy441         = .1
    #----sidebar tables---
    width_table     = 230
    height_table    = 300
    x332            = 1
    x442            = 1
    y332            = metodo_percentage_size(height_all,height_table)
    y442            = 0
    posx332         = 0
    posx442         = 0
    posy332         = 1-(y331+y330 + metodo_percentage_size(height_all,height_table))
    posy442         = 0
    #----sidebar graph---
    width_graph     = 230
    height_graph    = 170
    x333            = 1
    x443            = 1
    y333            = metodo_percentage_size(height_all,height_graph)
    y443            = 0
    posx333         = 0
    posx443         = 0
    posy333         = 0
    posy443         = 0
    #----- body ----
    width_screens   = 580
    height_screens  = 550
    xc1             = metodo_percentage_size(width_all,width_screens)
    xc2             = 1
    yc1             = metodo_percentage_size(height_all,height_screens)
    yc2             = 1-(y2+y6+x3)
    posxc1          = x5
    posxc2          = 0
    posyc1          = 0
    posyc2          = x3
    

    # x = [widget_screens/width_all,1]
    # y = [height_screens/height_all,.54]

    # pos_x = 72/width_all
    # pos_y = 0

    

except Exception as e:
    print('--------------')
    print(' Error: ',e)
    print('--------------')
    Error('layout_size').msg(e)