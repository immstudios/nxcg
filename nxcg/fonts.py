__all__ = ["fonts"]

from .common import *

class Fonts():
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        if not key in self.data:
            font = self.get_font(key)
            self.data[key] = font
        return self.data[key]

    def get_font(self, font_description):
        return Pango.FontDescription(font_description)

fonts = Fonts()
