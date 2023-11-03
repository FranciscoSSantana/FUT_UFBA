from tupy import *
from player import Player
import numpy as np

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
        self.frictionCoefficient = 0.09
        self.stopMovement = 0.1

        self.x_speed = 0
        self.y_speed = 0
        self.gravity = 0.5
        self.mass = 0
    
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
        normal_vector = [self.x - player.x, self.y - player.y]
        normal_vector = np.array(normal_vector)
        normal_vector = normal_vector / np.linalg.norm(normal_vector)
        tangent_vector = np.array([-1 * normal_vector[1], normal_vector[0]])

        ball_speed_vector = np.array([self.x_speed, self.y_speed])
        player_speed_vector = np.array([player.x_speed, player.y_speed])

        ball_normal_speed = np.dot(normal_vector, ball_speed_vector)
        ball_tangent_speed = np.dot(tangent_vector, ball_speed_vector)

        player_normal_speed = np.dot(normal_vector, player_speed_vector)

        ball_new_normal_speed = (ball_normal_speed * (self.mass - player.mass) + (2 * player.mass * player_normal_speed)) / (self.mass + player.mass)
        ball_speed_vector = (ball_new_normal_speed * normal_vector) + (ball_tangent_speed * tangent_vector)

        self.x_speed = ball_speed_vector[0] * self.elasticity
        self.y_speed = ball_speed_vector[1] * self.elasticity


    def collision_wall(self):
        if ((self.x < LEFT_BOUNDARY + self.radius) and (self.x_speed < 0)) or \
           ((self.x > RIGHT_BOUNDARY - self.radius) and (self.x_speed > 0)):
            
            self.x_speed = self.x_speed * (-1) * self.elasticity
        
        if ((self.y < UPPER_BOUNDARY + self.radius) and (self.y_speed < 0)):
            self.y_speed = self.y_speed * (-1) * self.elasticity
    
    def frictionCheck(self):
        if self.y_speed == 0 and self.x_speed != 0.0:
            if self.x_speed > 0:
                self.x_speed -= self.frictionCoefficient
            elif self.x_speed < 0:
                self.x_speed += self.frictionCoefficient
        if abs(self.x_speed) <= self.stopMovement:
            self.x_speed = 0

    def update(self):
        self.gravityCheck()
        self.collision_wall()
        self.frictionCheck()

        if self.x_speed > 0:
            self.angle -= 20

        if self.x_speed < 0:
            self.angle += 20

        if len(Player.PLAYERS) > 0:
            for player in Player.PLAYERS:

                if player.ballCollisionCooldown > 0:
                    player.ballCollisionCooldown -= 1

                distance = ((self.x - player.x)**2 + (self.y - player.y)**2)**0.5
                if (distance <= self.radius + player.radius) and (player.ballCollisionCooldown == 0):
                    player.ballCollisionCooldown = 15
                    self.collision_response(player)

        self.y += self.y_speed
        self.x += self.x_speed
