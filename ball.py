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
    
    def gravityCheck(self):
        if self.y < (460 - self.radius):
            self.y_speed += self.gravity
        else:
            if self.y_speed > self.stopBounce:
                self.y_speed = self.y_speed * -1 * self.elasticity
            else:
                if abs(self.y_speed) <= self.stopBounce:
                    self.y_speed = 0

    def update(self):

        self.gravityCheck()
        self.y += self.y_speed
