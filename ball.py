from tupy import *

class Ball(Image):
    def __init__(self, x = 400, y = 250):
        self.x = x
        self.y = y
        self.file = 'ball.png'

        self.radius = 10
        self.stopBounce = 2.5
        self.elasticity = 0.7

        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 2
        self.mass = 1
    
    def gravityCheck(self):
        if self.y < (460 - self.radius):
            self.y_speed += self.gravity
        else:
            if self.y_speed > self.stopBounce:
                self.y_speed = self.y_speed * -1 * self.elasticity
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

    def update(self):
        self.gravityCheck()
        self.y += self.y_speed
        self.x += self.x_speed

        if self._collides_with(player1):
            self.collision_response(player1)
        
        if self._collides_with(player2):
            self.collision_response(player2)
