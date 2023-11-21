from tupy import *
from player import Player
from ball import Ball
from goal import Goal
from background import Background
from pause import Pause
from placar import Placar

bg = Background()
pause = Pause()
playerBlue = Player(True)
playerRed = Player(False)
placar = Placar()
bola = Ball(placar)
gl = Goal(True)
gl2 = Goal(False)

run(globals())

