import os

class Fonts():
    def __init__(self):
        pass
    def __call__(self,font):

        FONT_PATH = os.path.join(os.environ['ENGESEP_ROOT'],f"libs{os.sep}baseclass{os.sep}assets{os.sep}fonts{os.sep}",font)
        return {
             "H1": [FONT_PATH, 96, False, -1.5],
             "H2": [FONT_PATH, 60, False, -0.5],
             "H3": [FONT_PATH, 48, False, 0],
             "H4": [FONT_PATH, 34, False, 0.25],
             "H5": [FONT_PATH, 24, False, 0],
             "H6": [FONT_PATH, 20, False, 0.15],
             "Subtitle1": [
                 FONT_PATH,
                 16,
                 False,
                 0.15,
             ],
             "Subtitle2": [
                 FONT_PATH,
                 16,
                 False,
                 0.1,
             ],
             "Body1": [FONT_PATH, 16, False, 0.5],
             "Body2": [FONT_PATH, 14, False, 0.25],
             "Button": [FONT_PATH, 14, True, 1.25],
             "Caption": [
                 FONT_PATH,
                 14,
                 False,
                 0.4,
             ],
             "Overline": [
                 FONT_PATH,
                 10,
                 True,
                 1.5,
             ],
             "Label": [FONT_PATH, 48, False, 0],
             "subtitulo": [FONT_PATH, 10, False, 0],
         }