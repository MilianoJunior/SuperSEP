from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDSeparator
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivymd.uix.button import MDRectangleFlatButton,MDRaisedButton,MDFlatButton,MDRaisedButton,MDTextButton
from kivymd.toast import toast
from libs.baseclass.observer.interfaces.observer import Observador


class Objeto:
    
    def __init__(self):
        self.__observadores = []
        
    def __repr__(self):
        return '::Objeto::'
    
    def registrar(self, observador):
        self.__observadores.append(observador)
        
    def notificar_all(self, *args, **kwargs):
        for observador in self.__observadores:
            observador.notificar(self, *args, **kwargs)
            
class ObservadorA:
    
    def __init__(self,objeto):
        objeto.registrar(self)
        
    def notificar(self, objeto, *args):
        print(f'0 {type(self).__name__} recebeu uma {args[0]} de {objeto}')
        toast(f'0 {type(self).__name__} recebeu uma {args[0]} de {objeto}',duration=4)

        
class ObservadorB:
    
    def __init__(self,objeto):
        objeto.registrar(self)
        
    def notificar(self, objeto, *args):
        print(f'0 {type(self).__name__} recebeu uma {args[0]} de {objeto}')
        toast(f'0 {type(self).__name__} recebeu uma {args[0]} de {objeto}',duration=7)
#
class Terminal(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        __metaclass__ = Observador
        self.__observadores = []
        
    def create(self):
        
        button = MDRaisedButton(text='notificação',on_press=self.notificar)
        # obj.notificar_all('notificação')
        card = MDCard(orientation='vertical',
                      padding=8,
                      size_hint=(1,1),
                      pos_hint={'center_x':.5,'center_y':.5})
        card.add_widget(button)
        card.add_widget(MDLabel(text='titulo'))
        card.add_widget(MDSeparator(height=1))
        card.add_widget(MDLabel(text='titulo'))
        self.add_widget(card)
        return self
    def on_press(self,*args):
        print('teste onpresse')
    def notificar(self,dt):
        obj = Objeto()
        obs_a = ObservadorA(obj)
        obs_b = ObservadorB(obj)
        obj.notificar_all('notificar')
        
    def update(self):
        print('atualização registrada: ',self.name)
        
    
