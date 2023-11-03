from tupy import *
from player import Player
from background import background

RIGHT_BOUNDARY = 850
LEFT_BOUNDARY = 50
UPPER_BOUNDARY = 0
LOWER_BOUNDARY = 500
GROUND_BOUNDARY = 460

class Ball(Image):
    def __init__(self, x = 450, y = 250):
        self.x = x
        self.y = y
        self.file = 'ball.png'

        self.radius = 18
        self.stopBounce = 3
        self.elasticity = 0.7
        self.frictionCoefficient = 0.03

        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 1.5
        self.mass = 1
    
    def gravityCheck(self):
        if self.y < (GROUND_BOUNDARY - self.radius):
            self.y_speed += self.gravity
        else:
            if self.y_speed > self.stopBounce:
                self.y_speed = self.y_speed * (-1) * self.elasticity
            else:
                if abs(self.y_speed) <= self.stopBounce:
                    self.y_speed = 0

    def collision_response(self, player):
        relative_velocity_y = self.y_speed - player.y_speed
        impulse = -(1 + self.elasticity) * relative_velocity_y / (1 / self.mass + 1 / player.mass)
        self.y_speed += impulse / self.mass

        if self.x > player.x:
            self.x_speed += impulse / self.mass
        else:
            self.x_speed -= impulse / self.mass

        self.y_speed = -self.y_speed

    def collision_wall(self):
        if ((self.x < LEFT_BOUNDARY + self.radius) and (self.x_speed < 0)) or \
           ((self.x > RIGHT_BOUNDARY - self.radius) and (self.x_speed > 0)):
            
            self.x_speed = self.x_speed * (-1) * self.elasticity
        
        if ((self.y < UPPER_BOUNDARY + self.radius) and (self.y_speed < 0)):
            self.y_speed = self.y_speed * (-1) * self.elasticity
    
    def frictionCheck(self):
        if self.y_speed == 0 and self.x_speed != 0:
            if self.x_speed > 0:
                self.x_speed -= self.frictionCoefficient
            elif self.x_speed < 0:
                self.x_speed += self.frictionCoefficient

    def update(self):
        self.gravityCheck()
        self.collision_wall()
        self.frictionCheck()
        self.y += self.y_speed
        self.x += self.x_speed
        
        if len(Player.PLAYERS) > 0:
            for player in Player.PLAYERS:
                if self._collides_with(player):
                    self.collision_response(player)
                
                if self._collides_with(player):
                    self.collision_response(player)
