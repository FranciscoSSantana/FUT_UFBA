from tupy import *
from background import *
from player import *
from ball import *
from goal import *

bg = Background()
bola = Ball()
gl = Goal()
gl2 = Goal(x=830, file= "Goal Front Dir.png")
playerBlue = Player(x = 450)
playerRed = Player(750, 428, "Player Red.png", False)

run(globals())
