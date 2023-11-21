from tupy import *
from gameconstants import *

class Player(Image):

    PLAYERS = []

    def __init__(self, isBluePlayer: bool = True) -> None:
        
        self.isBluePlayer = isBluePlayer

        self.game_is_on = True
        self.jump_height = PLAYER_JUMP_HEIGHT
        self.gravity = PLAYER_GRAVITY
        self.mass = PLAYER_MASS
        self.radius = PLAYER_RADIUS
        self.ballCollisionCooldown = PLAYER_BALL_COLLISION_COOLDOWN

        if self.isBluePlayer:
            self.file = "Player Blue.png"
            self.left = 'a'
            self.right = 'd'
            self.jump_key = 'w'
            self.power_key = 'space'
        else:
            self.file = "Player Red.png"
            self.left = 'Left'
            self.right = 'Right'
            self.jump_key = 'Up'
            self.power_key = 'enter'
        
        self.kick_off()

        self.PLAYERS.append(self)

    def kick(self):
        pass

    def kick_off(self):
        self.y = PLAYER_Y_SPAWN
        self.jumping = False
        self.x_speed = 0
        self.y_speed = 0

        if self.isBluePlayer:
            self.x = BLUE_PLAYER_X_SPAWN
        else:
            self.x = RED_PLAYER_X_SPAWN
    
    def movementInput(self):
        if keyboard.is_key_down(self.left):
            self.x_speed = -PLAYER_X_MOVING_SPEED
        if keyboard.is_key_down(self.right):
            self.x_speed = PLAYER_X_MOVING_SPEED
        if keyboard.is_key_just_down(self.jump_key) and self.jumping is False:
            self.jumping = True
            self.y_speed = self.jump_height
        if keyboard.is_key_down(self.power_key):
            pass

        if keyboard.is_key_up(self.left) and self.x_speed < 0:
            self.x_speed = 0
        if keyboard.is_key_up(self.right) and self.x_speed > 0:
            self.x_speed = 0

    def handleJump(self):
        if self.jumping:
            self.y += self.y_speed
            self.y_speed += self.gravity
            if self.y_speed > -self.jump_height:
                self.jumping = False
                self.y_speed = 0
    
    def move(self):
        self.movementInput()
        self.handleJump()
        self.x += self.x_speed

    def update(self):
        if self.game_is_on:
            self.move()
