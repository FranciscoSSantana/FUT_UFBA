from tupy import *

RIGHT_GOAL_X = 830
LEFT_GOAL_X = 70
GOAL_Y = 385

class Goal(Image):
    def __init__(self, x = LEFT_GOAL_X, file = "Goal Front Esq.png"):
        self.x = x
        self.y = GOAL_Y
        self.file = file
