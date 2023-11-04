from tupy import *
from background import Background
from player import Player
from ball import Ball
from goal import Goal

bg = Background()
playerBlue = Player(True)
playerRed = Player(False)
bola = Ball()
gl = Goal(True)
gl2 = Goal(False)

run(globals())
