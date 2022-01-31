from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
# from assets.themes import Themes
from libs.baseclass.observer.interfaces.observer import Observador
from libs.baseclass.observer.property.properties import Properties


class OptionMenu(MDBoxLayout):
    
    __metaclass__ = Observador
    content: list = []
    name: str = None

    def __init__(self, **kwargs):
        
        super().__init__(**kwargs)

    def create(self):
        
        self.theme = self.content['objetos']['Theme']

        for element in self.content['element'].keys():
            for elemen in self.content['element'][element].keys():
                print('Option Menu:------------------ ',element)
                if elemen == 'struct':
                    obj = eval(self.content['element'][element]['struct'])()
                else:
                    print(self.content['element'][element])
                    setattr(obj,elemen,self.content['element'][element][elemen])
        # for add_icon in self.content['element']:
        
            self.add_widget(obj)
        icon = MDIconButton(icon = 'android',
                            user_font_size = "25sp", 
                            pos_hint = {"center_x": .5, "center_y": .5},
                            theme_text_color= "Custom",
                            text_color = self.theme.icon_color,
                            on_release = self.callback)
        self.add_widget(icon)
        return self
    
    def callback(self,dt):
        self.theme.escolha += 1
        if self.theme.escolha > 4:
            self.theme.escolha = 0
        print(self.theme.escolha)
        # self.rules_properties = Properties()
        # print(f' id propriedades: {id(self.rules_properties)}')
        # self.rules_properties.msg()
        
    def option(self):
        
        FULL_MONTHS = {'janeiro': 1,  'fevereiro': 2, u'março': 3,    'abril': 4,
                       'maio': 5,     'junho': 6,     'julho': 7,     'agosto': 8,
                       'setembro': 9, 'outubro': 10,  'novembro': 11, 'dezembro': 12}
        menu_items = []
        for i in FULL_MONTHS.items():
            menu_items.append({"viewclass": "OneLineListItem","text": i[0],"height": dp(56),"on_release":lambda x=i: self.set_item(x)})
        self.menu = MDDropdownMenu(caller=self.id_option,items=menu_items,width_mult=4)
        self.menu.bind()
        
    def set_item(self, text__item):
        
        self.callback(text__item)
        self.menu.dismiss()
    
    def update(self):
        print('atualização registrada: ',self.name)