from tupy import *
from gameconstants import *
from random import choice

class Background(BaseImage):
    
    def __init__(self) -> None:
        self._x: int = X_CENTER
        self._y: int = Y_CENTER
        self.kick_off()
    
    def kick_off(self) -> None:
        '''
        reset, set random background
        '''
        backgrounds: list[str] = ["CampJapan.png", 
                      "CampBrasil.png", 
                      "CampEgypt.png", 
                      "CampItaly.png", 
                      "CampParis.png", 
                      "CampUS.png"]
        
        self._file: str = choice(backgrounds)
