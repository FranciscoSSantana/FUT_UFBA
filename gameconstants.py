# *** WALLS, BOUNDARY AND DIMENSION CONSTANTS ***
RIGHT_BOUNDARY: int = 850
LEFT_BOUNDARY: int = 50
UPPER_BOUNDARY: int = 0
LOWER_BOUNDARY: int = 500
GROUND_BOUNDARY: int = 460
X_CENTER: int = 450
Y_CENTER: int = 250


# *** BALL CONSTANTS ***
BALL_KICK_OFF_X: int = X_CENTER
BALL_KICK_OFF_Y: int = Y_CENTER
BALL_KICK_OFF_X_SPEED: float = 0
BALL_KICK_OFF_Y_SPEED: float = -5

BALL_BLUE_KICK_OFF_X_SPEED: float = -5
BALL_RED_KICK_OFF_X_SPEED: float = 5

BALL_RADIUS: int = 18 #DONT change unless changing image file as well

BALL_GRAVITY: float = 0.75
BALL_MASS: float = 0
BALL_ELASTICITY: float = 0.7
BALL_BOUNCE_STOP_COEFFICIENT: float = 3

BALL_FRICTION_COEFFICIENT: float = 0.09
BALL_STOP_MOVEMENT_COEFFICIENT: float = 0.1

BALL_SPIN: float = 20


# *** PLAYER CONSTANTS ***
PLAYER_HEIGHT:int = 64 #DONT change unless changing image file as well
PLAYER_WIDTH: int = 45 #DONT change unless changing image file as well

PLAYER_SPAWN_OFFSET: int = 200
BLUE_PLAYER_X_SPAWN: int = X_CENTER - PLAYER_SPAWN_OFFSET
RED_PLAYER_X_SPAWN: int = X_CENTER + PLAYER_SPAWN_OFFSET
PLAYER_Y_SPAWN: int = GROUND_BOUNDARY - PLAYER_HEIGHT//2

PLAYER_X_MOVING_SPEED: float = 8
PLAYER_X_POWER_MOVING_SPEED: float = 14

PLAYER_RADIUS: int = 32 #DONT change unless changing image file as well

PLAYER_JUMP_HEIGHT: int = -14
PLAYER_POWER_JUMP_HEIGHT: int = -20
PLAYER_GRAVITY: float = 2 #its important that the PLAYER_JUMP_HEIGHT is a multiple of PLAYER_GRAVITY, otherwise jump WILL break
PLAYER_MASS: float = 50

PLAYER_BALL_COLLISION_COOLDOWN: int = 10


# *** GOAL CONSTANTS ***
GOAL_SPAWN_OFFSET: int = 20 #DONT change unless changing image file as well
LEFT_GOAL_X: int = LEFT_BOUNDARY + GOAL_SPAWN_OFFSET
RIGHT_GOAL_X: int = RIGHT_BOUNDARY - GOAL_SPAWN_OFFSET
GOAL_Y: int = 385 #DONT change unless changing image file as well

GOAL_SIZE: int = 135 #DONT change unless changing image file as well

GOALPOST_WIDTH: int = 36 #DONT change unless changing image file as well
GOALPOST_HEIGHT: int = 12 #DONT change unless changing image file as well

GOALPOST_BOTTOM: int = GROUND_BOUNDARY - GOAL_SIZE
GOALPOST_TOP: int = GROUND_BOUNDARY - GOAL_SIZE - GOALPOST_HEIGHT
GOALPOST_LEFT_WALL: int = LEFT_BOUNDARY + GOALPOST_WIDTH
GOALPOST_RIGHT_WALL: int = RIGHT_BOUNDARY - GOALPOST_WIDTH


# *** PLACAR CONSTANTS ***
TIME: int = 90
BLUE_INITIAL_SCORE: int = 0
RED_INITIAL_SCORE: int = 0

PLACAR_Y: int = 49

TIME_TENS_X: int = 435
TIME_UNITS_X: int = 465
TIME_Y: int = 52

BLUE_SCORE_TENS_X: int = 342
BLUE_SCORE_UNITS_X: int = 372
RED_SCORE_TENS_X: int = 528
RED_SCORE_UNITS_X: int = 558
SCORE_Y: int = 65


# *** BUTTON CONSTANTS ***
BUTTON_OFFSET: int = 50

MESSAGE_Y: int = Y_CENTER + 175
MESSAGE_FLICK_SPEED: int = 20    #HAS TO BE EVEN

# *** POWER BOX CONSTANTS ***
POWER_BOX_X_KICK_OFF: int = X_CENTER
POWER_BOX_Y_KICK_OFF: int = GROUND_BOUNDARY - 120
POWER_BOX_Y_SPEED: int = 3
POWER_BOX_SPAWN_TIME: int = 420
POWER_TIME: int = 168
