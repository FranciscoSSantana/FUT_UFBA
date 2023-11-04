from tupy import *
from gameconstants import *

class Background(Image):
    def __init__(self, file = "CampJapan.png"):
        self.x = X_CENTER
        self.y = Y_CENTER
        self.file = file
