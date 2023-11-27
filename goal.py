from tupy import *
from gameconstants import *

class Goal(BaseImage):
    def __init__(self, leftSide: bool = True) -> None:
        self._y: int = GOAL_Y
        
        self._x: int = LEFT_GOAL_X if leftSide else RIGHT_GOAL_X
        self._file: str = "GoalFrontEsq.png" if leftSide else "GoalFrontDir.png"
