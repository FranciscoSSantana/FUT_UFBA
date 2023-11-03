from tupy import *

RIGHT_BOUNDARY = 850
LEFT_BOUNDARY = 50
TOP_BOUNDARY = 0
BOTTOM_BOUNDARY = 500
GROUND_BOUNDARY = 460
PLAYER_HEIGHT = 64
PLAYER_SPAWN = 150

class Player(Image):
    PLAYERS = []

    def __init__(self, x: int = PLAYER_SPAWN, y : int = GROUND_BOUNDARY - PLAYER_HEIGHT/2, file: str = 'Player Blue.png', wasd_scheme: bool = True) -> None:
        self.x = x
        self.y = y
        self.jumping = False
        self.file = file

        self.x_speed = 5
        self.jump_height = 20
        self.y_speed = self.jump_height
        self.gravity = 2
        self.mass = 2

        if wasd_scheme:
            self.left = 'a'
            self.right = 'd'
            self.jump_key = 'w'
            self.power_key = 'space'
        else:
            self.left = 'Left'
            self.right = 'Right'
            self.jump_key = 'Up'
            self.power_key = 'enter'
        
        self.PLAYERS.append(self)

    def kick(self):
        pass

    def update(self):
        if keyboard.is_key_down(self.left) and self.x > LEFT_BOUNDARY:
            self.x -= self.x_speed
        if keyboard.is_key_down(self.right) and self.x < RIGHT_BOUNDARY:
            self.x += self.x_speed
        if keyboard.is_key_just_down(self.jump_key):
            self.jumping = True
        if keyboard.is_key_down(self.power_key):
            pass

        if self.jumping:
            self.y -= self.y_speed
            self.y_speed -= self.gravity
            if self.y_speed < -self.jump_height:
                self.jumping = False
                self.y_speed = self.jump_height
