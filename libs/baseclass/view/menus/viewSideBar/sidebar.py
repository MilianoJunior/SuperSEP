# from libs.baseclass.exception_error import Error
from libs.baseclass.view.factory.builder_layout import BuilderLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from libs.baseclass.view.menus.viewSideBar.properties import sidebar_properties,search_properties,user_properties,table_properties,graph_properties
from libs.baseclass.view.menus.viewSideBar.widgets.widgets import UserCard,Search,TableSidebar,GraphSidebar
from libs.baseclass.state_variable import StateVariable
# from desempenho import Desempenho
# from os import getpid
# s1 = Desempenho()

var =  StateVariable()


class SideBar(BuilderLayout):
    '''
    Description: Layout
    -----------
        Composto por widgets
    '''
    name = None

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

    def __call__(self):
        try:

            main = MDFloatLayout()
            search_layout = MDBoxLayout(orientation='horizontal')
            user_layout = MDBoxLayout(orientation='horizontal')
            table_layout = MDBoxLayout(orientation='horizontal')
            graph_layout = MDBoxLayout(orientation='horizontal')

#
            search = Search(name='search')()
            user = UserCard(name='user')()
            table = TableSidebar(name='table')()
            graph = GraphSidebar()()

            var.register_change(main,sidebar_properties)
            var.register_change(search_layout,search_properties)
            var.register_change(user_layout,user_properties)
            var.register_change(table_layout,table_properties)
            var.register_change(graph_layout,graph_properties)
            var.register_graphs(graph,[1,2])

            search_layout.add_widget(search)
            user_layout.add_widget(user)
            table_layout.add_widget(table)
            graph_layout.add_widget(graph)

            main.add_widget(search_layout)
            main.add_widget(user_layout)
            main.add_widget(table_layout)
            main.add_widget(graph_layout)

            # s1.instance_time('11-SideBar')
            # s1.memory_size(getpid(),'SideBar')
            return main

        except Exception as e:
            raise NotImplementedError(self.__class__.__name__ + str(e))

        return self

