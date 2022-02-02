from kivy.uix.screenmanager import ScreenManager
from libs.baseclass.view.menus import ViewMenus
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from libs.baseclass.exception_error import Error
from libs.baseclass.state_variable import StateVariable
from kivy.utils import get_color_from_hex
from libs.baseclass.assets.color import cores
from libs.baseclass.view.screens.operacao import ViewPrincipal
from libs.baseclass.utils.layout_supersep import size_screens,pos_screens
# from libs.baseclass.utils.posicoes_b import *
# from desempenho import Desempenho

# s2 = Desempenho()

var =  StateVariable()

screens_properties = [
                        {
                            'name'      : 'screens',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'orientation',
                            'values'    : ['vertical','horizontal'],
                        },
                        {
                            'name'      : 'screens',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'md_bg_color',
                            'values'    : [cores['background'],cores['background']],
                        },
                        {
                            'name'      : 'screens',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'size_hint',
                            'values'    : size_screens,
                        },
                        {
                            'name'      : 'screens',
                            'condition' : 1200,
                            'methods'   : 'methods_orientation',
                            'property'  : 'pos_hint',
                            'values'    : pos_screens,
                        },

                    ]



class Singleton(type):

    __instances ={}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Composite(metaclass=Singleton):
    '''
    Description
    -----------
        Instância do ScreenManager, para comport os screens do construtor
    '''
    screens = ['principal','UG01','UG02','subestacao']

    def __init__(self,**kwargs):

        super().__init__(**kwargs)
        self.name = 'composite'
        # self.central = MDFloatLayout(md_bg_color=get_color_from_hex('#1E1F23'))

    def __call__(self):
        try:
            #----------------------------------------
            # configurações iniciais do layout central
            sm = ScreenManager()
            central = MDFloatLayout(md_bg_color=get_color_from_hex('#1E1F23'))
            # central.name = 'composite'
            # configurações iniciais das classes observers-
            error = Error('Composite',central)
            #--------------------------------------
            # configurações do screen box, para construção corpo da aplicação
            screens_box = MDBoxLayout()
            # observador responsável por monitorar o estado da variáveis, com o
            # propósito de alterar a posição e tamnho dos layouts e widgets, tornando o layout responsivo
            var.register_change(screens_box,screens_properties)
            #-----------------------------------
            menus = ViewMenus(name='menus')()
            central.add_widget(menus)
            #------------------------------------------
            sc_a = ViewPrincipal(name=self.screens[0])
            sm.add_widget(sc_a())
            #------------------------------------------
            '''
            # sc_b = ViewUG01(name=self.screens[1])
            # sm.add_widget(sc_b())
            # # #------------------------------------------
            # sc_c = ViewUG02(name=self.screens[2])
            # sm.add_widget(sc_c())
            # # #------------------------------------------
            # sc_d = ViewSubestacao(name=self.screens[3])
            # sm.add_widget(sc_d())

            # menu = template.create(sm)
            # central.add_widget(menu)
            central.add_widget(menus)

            central.add_widget(screens_box)
             menus.set_screen(sm)
            # print('###################')
            # print('MRO: ',sm.mro())
            # print('###################')
            '''
            screens_box.add_widget(sm)
            central.add_widget(screens_box)
            central.fbind('size',var.update)



        except Exception as e:
            error.msg(e)
        # s2.instance_time('2-composite')
        # s2.memory_size(os.getpid(),'composite')
        return central

