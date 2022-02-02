clear#from desempenho import Desempenho
#s2 = Desempenho()
from kivy import Config
# import importlib
import multiprocessing
DEVELOPMENT_VERSION = False
KIVY_LOG_LEVEL = "info" if not DEVELOPMENT_VERSION else "debug"
# Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
# Config.set('kivy', 'exit_on_escape', '0')
Config.set('kivy', 'log_level', KIVY_LOG_LEVEL)
Config.set('graphics','borderless',[0,1][0])
Config.set('graphics', 'window_state', ['visible','hidden','maximized'][2])
Config.set('graphics', 'fbo',['hardware','software','force-hardware'][2])
Config.set('graphics', 'fullscreen', [0,1,'fake','auto'][0])
# Config.set('graphics', 'height', 0)
# Config.set('graphics', 'left', 0)
Config.set('graphics','maxfps',[0,60,120][2])
Config.set('graphics', 'multisamples',[0,1,2,3,4,1000][5])
Config.set('graphics','position',['auto','custom'][1])
Config.set('graphics', 'show_cursor',[0,1][1])
# Config.set('graphics','top',10)
Config.set('graphics', 'resizable',[0,1][1])
Config.set('graphics','rotation',[0,90,180,270][0])
# Config.set('graphics','width',1)
Config.set('graphics','minimum_width',300)
Config.set('graphics','minimum_height',600)

'''
hardware: 17.2-cpu, 338.4 ram, 1.6 GPU
software: 17.0-cpu, 343.4 ram, 1.6 GPU
force-hardware: 17.3-cpu,342.2 ram, 1.6 GPU

[force-hardware: 2, maxfps: 1]: 0.8-cpu,347.2 ram, 1.7 GPU
[force-hardware: 2, maxfps: 2]: 0.8-cpu,343.2 ram, 1.7 GPU

[force-hardware: 2, maxfps: 2, multisamples: 1]: 1.5-cpu,339.7 ram, 2.9 GPU

[force-hardware: 2, maxfps: 2, multisamples: 2]: 1.0-cpu,339.7 ram, 2.2 GPU

[force-hardware: 2, maxfps: 2, multisamples: 3]: 4.0-cpu,343.7 ram, 2.8 GPU

[force-hardware: 2, maxfps: 2, multisamples: 5]: 0.6-cpu,343.7 ram, 2.8 GPU
'''
import os,sys
from pathlib import Path
os.environ["ENGESEP_LANG"] = "1"
if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["ENGESEP_ROOT"] = sys._MEIPASS
else:
    os.environ["ENGESEP_ROOT"] = str(Path(__file__).parent)
os.environ["ENGESEP_ASSETS"] = os.path.join(os.environ["ENGESEP_ROOT"], f"assets{os.sep}")
os.environ["ENGESEP_IMG"] = os.path.join(os.environ["ENGESEP_ROOT"], f"libs{os.sep}baseclass{os.sep}assets{os.sep}imagens{os.sep}")
from kivy.clock import mainthread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from libs.baseclass.assets.fonts import Fonts
from kivy.factory import Factory  # NOQA: F401
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.base import ExceptionManager
import ctypes
from libs.baseclass.composite import Composite
from screeninfo import get_monitors
from libs.baseclass.exception_error import E

screensize = [get_monitors()[0].width, get_monitors()[0].height]
registrar_componentes = ['construtor.py','main.py','interfaces.py','homescreen.py','header.py',
                          'footer.py','struct.py','sidebar.py','register_interfaces.py',
                          'group_buttons.py','option_menu.py','timer_picker.py','tabs.py',
                          'pie_chart.py','velocimetro.py','terminal.py','hour.py','card.py',
                          'logo.py','title.py','themes.py','controller_construtor.py','construtor_model.py',
                          'construtor_view.py','delete_view.py','update_view.py','visualizador_view.py',
                          'template_construtor.py','body.py','view_builder.py','metodos.py','composite.py',
                          'widgets.py','button.py','widgets.py','state_variable.py','exception_error.py',
                          'methods.py','properties.py','view_menus.py','menu.py','view_footer.py','view_sidebar.py',
                          'sidebar.py','__init__.py','menu_lateral.py','view_principal.py','layout_supersep.py',
                          'posicoes.py','graph.py','builder_ug1.py','builder_ug2.py','menu_lateral.py','gauge.py','input_text.py',
                          'button_emergency.py','tables.py']

def abrir():
    os.system("clear")
    os.system("python3 main.py")

class KvHandler(FileSystemEventHandler):
    def __init__(self, callback, target, **kwargs):
        super(KvHandler, self).__init__(**kwargs)
        self.callback = callback
        self.target = target

    def on_modified(self, event):
        for s in registrar_componentes:
            if os.path.basename(event.src_path) == s:
                self.callback(os.path.basename(event.src_path))

class EngeSEPApp(MDApp):
    cont = 0

    def __init__(self: object,**kwargs)->None:
        super().__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
#        ExceptionManager.add_handler(E(self))
        # fonts_ = ['Blacker-Display-Bold-trial',
        #           'ZenOldMincho-Black',
        #           'Nunito-Black',
        #           'ZenKakuGothicAntique-Bold',
        #           'ZillaSlab-Bold',
        #           'BERNIERShade-Regular',
        #           'BERNIERRegular-Regular',
        #           'Evogria.otf',
        #           'Eczar-Regular',
        #           'Eczar-Bold']

        font = Fonts()('Eczar-Regular')
        self.theme_cls.font_styles.update(font)
        Window.system_size = screensize
        self.titulo = 'SuperSEP'

    def build(self: object)->object:
        try:
            TARGET = [ files for files in os.listdir(f"{os.environ['ENGESEP_ROOT']}")]
            PATH = os.environ["ENGESEP_ROOT"]
            o = Observer()
            o.schedule(KvHandler(self.update, TARGET), PATH,recursive=True)
            o.start()
            return Composite()()

        except Exception as e:
            print(e)
    def on_stop(self, *args):
        print('Fechando o app')

    def on_start(self):
        print('On_start')

    @mainthread
    def update(self,target,*args):
        pc2 = multiprocessing.Process(target=abrir)
        pc2.start()
        pc2.join()
        self.get_running_app().stop()

if __name__ == "__main__":
    try:
        app = EngeSEPApp()
        app.run()
    except Exception as inst:
        print(inst)

