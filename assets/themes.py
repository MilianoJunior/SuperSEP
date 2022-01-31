from kivy.utils import get_color_from_hex

class SingletonMeta(type):
    
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
            
        return cls._instances[cls]

    
class Themes(metaclass=SingletonMeta):
    
    def __init__(self,escolha=0):
        
        # Configurações de escolha e themas
        
        self.escolha =  escolha
        self.option_theme = ["Dark","Light", "Normal","Green", "Azul"]
        self.tema_escolhido  = self.option_theme[self.escolha]
        
        self.escolha = self.escolha if self.escolha < 4 else 0
        # self.background_color = get_color_from_hex('#121212')
        self.background_color_opacity = get_color_from_hex('#FAFAFA')
        
        '''Option Dark Template'''
        if self.option_theme[self.escolha] == 'Dark':
            
            ''' Configurações de fonte '''

            self.font_size = 11
            self.font_size_title = 'H6'
            self.font_size_subtitle = 14
            
            ''' Configurações spacing, padding, line e halign'''
            
            self.padding = [0,0,0,0]
            self.spacing = 0
            self.line_color = get_color_from_hex('#3C3C3C')
            self.text_align = 'center'
            self.radius = [0,0,0,0]
            
            ''' Configurações de color text '''
            
            self.text_color = get_color_from_hex('#000000')
            self.text_color_normal = get_color_from_hex('#FFFFFF')
            self.text_color_down = get_color_from_hex('#FFFFFF')
            self.text_color_title = get_color_from_hex('#FFFFFF')
            
            ''' Configurações de elevação '''
            
            self.background_color_elevation = get_color_from_hex('#1F1B24')
            
            ''' Configurações de buttons text '''
            
            self.button_text_color = get_color_from_hex('#FFFFFF')
            
            '''Configurações de buttons background'''
            
            self.icon_color = get_color_from_hex('#FFFFFF')
            self.button_normal_color = get_color_from_hex('#3700B3')    #informações
            self.button_active_color = get_color_from_hex('#3C3C3D')
            self.button_emergency = get_color_from_hex('#FF0266')
            
            '''Configurações de background'''
            
            self.background_color = get_color_from_hex('#263238')
            self.background_color_elevation = get_color_from_hex('#37474F')
            
            
            ''' Configurações de mensagem '''
            
            self.sucess = get_color_from_hex('#03DAC6') #sucesso
            self.alert = get_color_from_hex('#FFDE03')  #alerta
            self.warning = get_color_from_hex('#BB86FC') #atenção
            self.danger = get_color_from_hex('#512DA8')   #perigo
            self.info = get_color_from_hex('#78909C')    #informações

                    
        '''Option Light Template'''
        if self.option_theme[self.escolha] == 'Light':
            ''' Configurações de fonte '''

            self.font_size = 11
            self.font_size_title = 'H6'
            self.font_size_subtitle = 14
            
            ''' Configurações spacing, padding, line e halign'''
            
            self.padding = [0,0,0,0]
            self.spacing = 0
            self.line_color = get_color_from_hex('#3C3C3C')
            self.text_align = 'center'
            self.radius = [0,0,0,0]
            
            ''' Configurações de color text '''
            
            self.text_color = get_color_from_hex('#FFFFFF')
            self.text_color_normal = get_color_from_hex('#FFFFFF')
            self.text_color_down = get_color_from_hex('#FFFFFF')
            self.text_color_title = get_color_from_hex('#FFFFFF')
            
            ''' Configurações de elevação '''
            
            self.background_color_elevation = get_color_from_hex('#1F1B24')
            
            ''' Configurações de buttons text '''
            
            self.button_text_color = get_color_from_hex('#FFFFFF')
            
            '''Configurações de buttons background'''
            
            self.icon_color = get_color_from_hex('#FFFFFF')
            self.button_normal_color = get_color_from_hex('#3700B3')    #informações
            self.button_active_color = get_color_from_hex('#3C3C3D')
            self.button_emergency = get_color_from_hex('#FF0266')
            
            '''Configurações de background'''
            
            self.background_color = get_color_from_hex('#0D47A1')
            self.background_color_elevation = get_color_from_hex('#1565C0')
            
            
            ''' Configurações de mensagem '''
            
            self.sucess = get_color_from_hex('#03DAC6') #sucesso
            self.alert = get_color_from_hex('#FFDE03')  #alerta
            self.warning = get_color_from_hex('#BB86FC') #atenção
            self.danger = get_color_from_hex('#512DA8')   #perigo
            self.info = get_color_from_hex('#78909C')    #informações

            
            
        '''Option Green Template'''
        if self.option_theme[self.escolha] == 'Green':
            
            ''' Configurações de fonte '''

            self.font_size = 11
            self.font_size_title = 'H6'
            self.font_size_subtitle = 14
            
            ''' Configurações spacing, padding, line e halign'''
            
            self.padding = [0,0,0,0]
            self.spacing = 0
            self.line_color = get_color_from_hex('#3C3C3C')
            self.text_align = 'center'
            self.radius = [0,0,0,0]
            
            ''' Configurações de color text '''
            
            self.text_color = get_color_from_hex('#FFFFFF')
            self.text_color_normal = get_color_from_hex('#FFFFFF')
            self.text_color_down = get_color_from_hex('#FFFFFF')
            self.text_color_title = get_color_from_hex('#FFFFFF')
            
            ''' Configurações de elevação '''
            
            self.background_color_elevation = get_color_from_hex('#1F1B24')
            
            ''' Configurações de buttons text '''
            
            self.button_text_color = get_color_from_hex('#FFFFFF')
            
            '''Configurações de buttons background'''
            
            self.icon_color = get_color_from_hex('#FFFFFF')
            self.button_normal_color = get_color_from_hex('#3700B3')    #informações
            self.button_active_color = get_color_from_hex('#3C3C3D')
            self.button_emergency = get_color_from_hex('#FF0266')
            
            '''Configurações de background'''
            
            self.background_color = get_color_from_hex('#EEEEEE')
            
            
            ''' Configurações de mensagem '''
            
            self.sucess = get_color_from_hex('#03DAC6') #sucesso
            self.alert = get_color_from_hex('#FFDE03')  #alerta
            self.warning = get_color_from_hex('#BB86FC') #atenção
            self.danger = get_color_from_hex('#512DA8')   #perigo
            self.info = get_color_from_hex('#78909C')    #informações

            
        '''Option Blue Template'''
        if self.option_theme[self.escolha] == 'Normal':
            ''' Configurações de fonte '''

            self.font_size = 11
            self.font_size_title = 'H6'
            self.font_size_subtitle = 14
            
            ''' Configurações spacing, padding, line e halign'''
            
            self.padding = [0,0,0,0]
            self.spacing = 0
            self.line_color = get_color_from_hex('#3C3C3C')
            self.text_align = 'center'
            self.radius = [0,0,0,0]
            
            ''' Configurações de color text '''
            
            self.text_color = get_color_from_hex('#FFFFFF')
            self.text_color_normal = get_color_from_hex('#FFFFFF')
            self.text_color_down = get_color_from_hex('#FFFFFF')
            self.text_color_title = get_color_from_hex('#FFFFFF')
            
            ''' Configurações de elevação '''
            
            self.background_color_elevation = get_color_from_hex('#1F1B24')
            
            ''' Configurações de buttons text '''
            
            self.button_text_color = get_color_from_hex('#FFFFFF')
            
            '''Configurações de buttons background'''
            
            self.icon_color = get_color_from_hex('#FFFFFF')
            self.button_normal_color = get_color_from_hex('#3700B3')    #informações
            self.button_active_color = get_color_from_hex('#3C3C3D')
            self.button_emergency = get_color_from_hex('#FF0266')
            
            '''Configurações de background'''
            
            self.background_color = get_color_from_hex('#EEEEEE')
            self.background_color_elevation = get_color_from_hex('#FAFAFA')
            self.background_color_opacity = get_color_from_hex('#FAFAFA')
            
            
            ''' Configurações de mensagem '''
            
            self.sucess = get_color_from_hex('#03DAC6') #sucesso
            self.alert = get_color_from_hex('#FFDE03')  #alerta
            self.warning = get_color_from_hex('#BB86FC') #atenção
            self.danger = get_color_from_hex('#512DA8')   #perigo
            self.info = get_color_from_hex('#78909C')    #informações

            
        def on_size(self,x,y):
            pass





