from __future__ import annotations
from abc import ABC, abstractmethod

class Observador(ABC):
    
    @abstractmethod 
    def update(self):
        pass














# class Subject(ABC):
#     '''
#     Essa interface declara um conjunto de metodos para gerenciar os inscritos
#     '''
#     @abstractmethod 
#     def attach(self,observer: Observer)-> None:
#         '''
#         Parameters
#         ----------
#         observer : Observer
#             Anexar um observador ao assunto
#         Returns
#         -------
#         None
#         '''
#         pass
    
#     @abstractmethod 
#     def detach(self,observer: Observer)-> None:
#         '''
#         Parameters
#         ----------
#         observer : Observer
#             Desanexar um observador ao assunto
#         Returns
#         -------
#         None
#         '''
#         pass
#     @abstractmethod 
#     def notify(self)->None:
#         '''
#         Notificar todos os observadores do assunto
#         Returns
#         -------
#         None
#         '''
#         pass
    
    
# class ConcreteSubject(Subject):
#         '''
#         O assunto possui algum estado importante e notifica os observadores quando há alteração.
#         '''
#         _state: int = None
#         '''
#         O estado dos inscritos é armazenado nessa variável.
#         '''
#         _observers: List[Observer] = []
        
#         def attach(self, observer: Observer)-> None:
#             print('Subject: Attached an observer')
#             self._observers
        
        