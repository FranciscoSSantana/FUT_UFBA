from tupy import *
from gameconstants import *

class Goal(Image):
    def __init__(self, leftSide: bool = True):
        self.y = GOAL_Y
        if leftSide:
            self.x = LEFT_GOAL_X
            self.file = "Goal Front Esq.png"
        else:
            self.x = RIGHT_GOAL_X
            self.file = "Goal Front Dir.png"
