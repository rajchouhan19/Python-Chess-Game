from src.constants import *

class Theme:

    def __init__(self):

        self.current = "classic"

    def get_colors(self):

        if self.current == "classic":

            return CLASSIC_LIGHT, CLASSIC_DARK

        return DARK_LIGHT, DARK_DARK

    def toggle(self):

        if self.current == "classic":

            self.current = "dark"

        else:

            self.current = "classic"