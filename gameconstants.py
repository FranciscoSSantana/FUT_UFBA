# *** WALLS, BOUNDARY AND DIMENSION CONSTANTS ***
RIGHT_BOUNDARY = 850
LEFT_BOUNDARY = 50
UPPER_BOUNDARY = 0
LOWER_BOUNDARY = 500
GROUND_BOUNDARY = 460
X_CENTER = 450
Y_CENTER = 250


# *** BALL CONSTANTS ***
BALL_KICK_OFF_X = X_CENTER
BALL_KICK_OFF_Y = Y_CENTER
BALL_KICK_OFF_X_SPEED = 0
BALL_KICK_OFF_Y_SPEED = -5

BALL_BLUE_KICK_OFF_X_SPEED = -5
BALL_RED_KICK_OFF_X_SPEED = 5

BALL_RADIUS = 18 #DONT change unless changing image file as well

BALL_GRAVITY = 0.75
BALL_MASS = 0
BALL_ELASTICITY = 0.7
BALL_BOUNCE_STOP_COEFFICIENT = 3

BALL_FRICTION_COEFFICIENT = 0.09
BALL_STOP_MOVEMENT_COEFFICIENT = 0.1

BALL_SPIN = 20


# *** PLAYER CONSTANTS ***
PLAYER_HEIGHT = 64 #DONT change unless changing image file as well
PLAYER_WIDTH = 45 #DONT change unless changing image file as well

PLAYER_SPAWN_OFFSET = 200
BLUE_PLAYER_X_SPAWN = X_CENTER - PLAYER_SPAWN_OFFSET
RED_PLAYER_X_SPAWN = X_CENTER + PLAYER_SPAWN_OFFSET
PLAYER_Y_SPAWN = GROUND_BOUNDARY - PLAYER_HEIGHT/2

PLAYER_X_MOVING_SPEED = 8

PLAYER_RADIUS = 32 #DONT change unless changing image file as well

PLAYER_JUMP_HEIGHT = -14
PLAYER_GRAVITY = 2 #its important that the PLAYER_JUMP_HEIGHT is a multiple of PLAYER_GRAVITY, otherwise jump WILL break
PLAYER_MASS = 50

PLAYER_BALL_COLLISION_COOLDOWN = 10


# *** GOAL CONSTANTS ***
GOAL_SPAWN_OFFSET = 20 #DONT change unless changing image file as well
LEFT_GOAL_X = LEFT_BOUNDARY + GOAL_SPAWN_OFFSET
RIGHT_GOAL_X = RIGHT_BOUNDARY - GOAL_SPAWN_OFFSET
GOAL_Y = 385 #DONT change unless changing image file as well

GOAL_SIZE = 135 #DONT change unless changing image file as well

GOALPOST_WIDTH = 36 #DONT change unless changing image file as well
GOALPOST_HEIGHT = 12 #DONT change unless changing image file as well

GOALPOST_BOTTOM = GROUND_BOUNDARY - GOAL_SIZE
GOALPOST_TOP = GROUND_BOUNDARY - GOAL_SIZE - GOALPOST_HEIGHT
GOALPOST_LEFT_WALL = LEFT_BOUNDARY + GOALPOST_WIDTH
GOALPOST_RIGHT_WALL = RIGHT_BOUNDARY - GOALPOST_WIDTH


# *** PLACAR CONSTANTS ***
TIME = 10
BLUE_INITIAL_SCORE = 0
RED_INITIAL_SCORE = 0

PLACAR_Y = 49

TIME_TENS_X = 435
TIME_UNITS_X = 465
TIME_Y = 52

BLUE_SCORE_TENS_X = 342
BLUE_SCORE_UNITS_X = 372
RED_SCORE_TENS_X = 528
RED_SCORE_UNITS_X = 558
SCORE_Y = 65


# *** BUTTON CONSTANTS ***
BUTTON_OFFSET = 50

MESSAGE_Y = Y_CENTER + 175
MESSAGE_FLICK_SPEED = 20    #HAS TO BE EVEN
