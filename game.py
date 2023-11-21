from tupy import *
from player import Player
from ball import Ball
from goal import Goal
from background import Background
from pause import Pause

bg = Background()
pause = Pause()
playerBlue = Player(True)
playerRed = Player(False)
bola = Ball()
gl = Goal(True)
gl2 = Goal(False)

run(globals())
