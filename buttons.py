from tupy import *
from gameconstants import *

class MenuBackground(Image):
    def __init__(self) -> None:
        self.file = "Backmenu.png"
        self.x = X_CENTER
        self.y = Y_CENTER
            
class Resume(Image):
    def __init__(self):
        self.file = "resume.png"
        self.x = X_CENTER 
        self.y = Y_CENTER - BUTTON_OFFSET
            
class Restart(Image):            
    def __init__(self):
        self.file = "restart.png"
        self.x = X_CENTER 
        self.y = Y_CENTER + BUTTON_OFFSET
