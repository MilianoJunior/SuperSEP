import os

class Fonts():
    def __init__(self):
        pass
    def __call__(self,font):
        
        print('Executando as fonts')
        FONT_PATH = f"{os.environ['ENGESEP_ROOT']}\\libs\\baseclass\\assets\\fonts\\"
        print('----------------------')
        print(FONT_PATH,font)
        print('---------------------')
        return {
             "H1": [FONT_PATH + font, 96, False, -1.5],
             "H2": [FONT_PATH + font, 60, False, -0.5],
             "H3": [FONT_PATH + font, 48, False, 0],
             "H4": [FONT_PATH + font, 34, False, 0.25],
             "H5": [FONT_PATH + font, 24, False, 0],
             "H6": [FONT_PATH + font, 20, False, 0.15],
             "Subtitle1": [
                 FONT_PATH + font,
                 16,
                 False,
                 0.15,
             ],
             "Subtitle2": [
                 FONT_PATH + font,
                 16,
                 False,
                 0.1,
             ],
             "Body1": [FONT_PATH + font, 16, False, 0.5],
             "Body2": [FONT_PATH + font, 14, False, 0.25],
             "Button": [FONT_PATH + font, 14, True, 1.25],
             "Caption": [
                 FONT_PATH + font,
                 14,
                 False,
                 0.4,
             ],
             "Overline": [
                 FONT_PATH + font,
                 10,
                 True,
                 1.5,
             ],
             "Label": [FONT_PATH + font, 48, False, 0],
             "subtitulo": [FONT_PATH + font, 10, False, 0],
         }