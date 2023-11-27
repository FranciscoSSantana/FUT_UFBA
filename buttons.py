from tupy import *
from gameconstants import *

class MenuBackground(BaseImage):
    def __init__(self) -> None:
        self._file: str = "Backmenu.png"
        self._x: int = X_CENTER
        self._y: int = Y_CENTER
            
class Resume(BaseImage):
    def __init__(self) -> None:
        self._file: str = "resume.png"
        self._x: int = X_CENTER 
        self._y: int = Y_CENTER - BUTTON_OFFSET
            
class Restart(BaseImage):            
    def __init__(self) -> None:
        self._file: str = "restart.png"
        self._x: int = X_CENTER 
        self._y: int = Y_CENTER + BUTTON_OFFSET
