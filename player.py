from tupy import *
from gameconstants import *
from pause import Pause

class Player(Image):
        
    PLAYERS = []
    

    def __init__(self, isBluePlayer: bool = True) -> None:
        
        self.isBluePlayer = isBluePlayer

        self.jump_height = PLAYER_JUMP_HEIGHT
        self.gravity = PLAYER_GRAVITY
        self.mass = PLAYER_MASS
        self.radius = PLAYER_RADIUS
        self.ballCollisionCooldown = PLAYER_BALL_COLLISION_COOLDOWN
        self.boost = False

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

        Player.PLAYERS.append(self)
    
    def _destroy(self) -> None:
        Player.PLAYERS.remove(self)
        super()._destroy()

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
            self.jump_height = PLAYER_JUMP_HEIGHT
            self.y_speed = self.jump_height
        if keyboard.is_key_down(self.power_key):
            pass

        if keyboard.is_key_up(self.left) and self.x_speed < 0:
            self.x_speed = 0
        if keyboard.is_key_up(self.right) and self.x_speed > 0:
            self.x_speed = 0
            
    
    def _Power_movementInput(self):
        if keyboard.is_key_down(self.left):
            self.x_speed = -PLAYER_X_POWER_MOVING_SPEED
        if keyboard.is_key_down(self.right):
            self.x_speed = PLAYER_X_POWER_MOVING_SPEED
        if keyboard.is_key_just_down(self.jump_key) and self.jumping is False:
            self.jumping = True
            self.jump_height = PLAYER_POWER_JUMP_HEIGHT
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
        if self.boost:
            self._Power_movementInput()
            self.handleJump()
        else:
            self.movementInput()
            self.handleJump()
        if self.x - PLAYER_WIDTH//2 >= LEFT_BOUNDARY and self.x + PLAYER_WIDTH//2 <= RIGHT_BOUNDARY:
            self.x += self.x_speed
        else:
            if self.x - PLAYER_WIDTH//2 < LEFT_BOUNDARY:
                self.x += PLAYER_WIDTH//8
            else:
                self.x -= PLAYER_WIDTH//8

    def update(self):
        if not Pause.isPaused:
            self.move()
