from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.view.widgets import *
from libs.baseclass.observer.property.properties import Properties

import asyncio

''' Classe abstrata  factory'''
class Struct(MDBoxLayout):

    def __init__(self,register: list,name_screen: str,sm: object, **kwargs):
        
        super().__init__(**kwargs)
        self.rules_properties = Properties()
        print(f' id propriedades: {id(self.rules_properties)}')
        self.name = name_screen
        self.orientation = 'vertical'
        self.padding = [0,0,0,0]
        self.spacing = 1
        self.register = register
        self.sm = sm
        
    async def set_camada(self,widget):
        # Instância do Objeto--
        print(widget['struct'])
        objeto = eval(widget['struct'])() 
        
        # Atribuição de nome
        objeto.name = widget['name']
        # Define o conteudo do objeto-
        if widget['content']:
            objeto.content = widget['content']
            # criar o objeto
            objeto.create()
        # Define as propriedades
        for propert in widget['properties'].keys():
            setattr(objeto, propert, widget['properties'][propert])
        # Define as ações do objeto
        for action in widget['actions']:
            pass
        # Registrando os objetos na classe ObserverProprety-
        self.rules_properties.addObjeto(objeto,widget['name'])
        
        return objeto
    
    async def proxy(self):
        
        for widgets in self.register['widgets']:
            print(widgets['name'])
            task = asyncio.create_task(self.set_camada(widgets))
            objeto = await task
            
            for widget in widgets['widgets']:
                task1 = asyncio.create_task(self.set_camada(widget))
                objeto1 = await task1
                objeto.add_widget(objeto1)
                print('    ',widget['name'])
                for widge in widget['widgets']:
                    print('            ',widge['name'])
                    task2 = asyncio.create_task(self.set_camada(widge))
                    objeto2 = await task2
                    objeto1.add_widget(objeto2)
            self.add_widget(objeto)

    def __call__(self): 
        
        el = asyncio.get_event_loop()
        el.run_until_complete(self.proxy())
        
        return self
    def on_size(self, *args):
        print('-----')
        print(self.x,self.y)
        print(self.size)
        print(self.top)
        print(self.height)
        print(self.center)
    def on_press(self, *args):
        print('on_press struct')
    def callback(self, instance):
        print('struct',instance.icon)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    