from tupy import *
from gameconstants import *

class Menu(Image):
    def __init__(self, file = "Backmenu.png", is_menu_on: bool = False) -> None:
        self.is_menu_on = is_menu_on
        self.file = file
        self.x = X_CENTER
        self.y = Y_CENTER
            
class Resume(Image):
    def __init__(self, file = "resume.png"):
        self.file = file
        self.x = X_CENTER 
        self.y = Y_CENTER - 50
            
class Restart(Image):            
    def __init__(self, file = "restart.png"):
        self.file = file
        self.x = X_CENTER 
        self.y = Y_CENTER + 50

