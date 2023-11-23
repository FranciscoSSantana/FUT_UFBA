from tupy import *
from gameconstants import *

class Background(Image):

    backgrounds = ["CampJapan.png", 
                   "CampBrasil.png", 
                   "CampEgypt.png", 
                   "CampItaly.png", 
                   "CampParis.png", 
                   "CampUS.png"]
    
    def __init__(self) -> None:
        self._x = X_CENTER
        self._y = Y_CENTER
        self.kick_off()
    
    def kick_off(self):
        self.file = random.choice(Background.backgrounds)
