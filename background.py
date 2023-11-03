from tupy import *

CENTER_X = 450
CENTER_Y = 250

class Background(Image):
    def __init__(self, file = "CampJapan.png"):
        self.x = CENTER_X
        self.y = CENTER_Y
        self.file = file
