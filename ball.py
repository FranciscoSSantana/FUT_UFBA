from tupy import *
from gameconstants import *
from player import Player
from pause import Pause
import numpy as np

class Ball(Image):
    def __init__(self, placar):
        self.radius = BALL_RADIUS
        self.stopBounce = BALL_BOUNCE_STOP_COEFFICIENT
        self.elasticity = BALL_ELASTICITY
        self.frictionCoefficient = BALL_FRICTION_COEFFICIENT
        self.stopMovement = BALL_STOP_MOVEMENT_COEFFICIENT
        self.placar = placar

        self.gravity = BALL_GRAVITY
        self.mass = BALL_MASS

        self.kick_off()
    
    def kick_off(self):
        self.x = BALL_KICK_OFF_X
        self.y = BALL_KICK_OFF_Y
        self.x_speed = BALL_KICK_OFF_X_SPEED
        self.y_speed = BALL_KICK_OFF_Y_SPEED
        for player in Player.PLAYERS:
            player.kick_off()
    
    def blue_kick_off(self):
        self.kick_off()
        self.x_speed = BALL_BLUE_KICK_OFF_X_SPEED
    
    def red_kick_off(self):
        self.kick_off()
        self.x_speed = BALL_RED_KICK_OFF_X_SPEED
    
    def handleGravity_and_FloorCollision(self):
        #Apply gravity
        if self.y < (GROUND_BOUNDARY - self.radius):
            self.y_speed += self.gravity
        else:
            #Floor collision
            if self.y_speed > self.stopBounce:
                self.y_speed = self.y_speed * (-1) * self.elasticity
            else:
                if abs(self.y_speed) <= self.stopBounce:
                    self.y_speed = 0
    
    def checkPlayerCollision(self):
        if len(Player.PLAYERS) > 0:
            for player in Player.PLAYERS:

                if player.ballCollisionCooldown < PLAYER_BALL_COLLISION_COOLDOWN:
                    player.ballCollisionCooldown += 1

                distance = ((self.x - player.x)**2 + (self.y - player.y)**2)**0.5
                if (distance <= self.radius + player.radius) and (player.ballCollisionCooldown == PLAYER_BALL_COLLISION_COOLDOWN):
                    player.ballCollisionCooldown = 0
                    self.handlePlayerCollision(player)

    def handlePlayerCollision(self, player):
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

    def handleRoofCollision(self):
        if ((self.y < UPPER_BOUNDARY + self.radius) and (self.y_speed < 0)):
            self.y_speed = self.y_speed * (-1) * self.elasticity

    def handleLeftWallCollision_and_GoalDetection(self):
        #Side-wall collisions
        if ((self.x < LEFT_BOUNDARY + self.radius) and (self.x_speed < 0)):
            
            self.x_speed = self.x_speed * (-1) * self.elasticity

            #Goal detection
            if ((self.y < GROUND_BOUNDARY) and (self.y > GROUND_BOUNDARY - GOAL_SIZE)):
                self.blue_kick_off()
                self.placar.addRedGoal()
        

    def handleRightWallCollision_and_GoalDetection(self):
            #Side-wall collisions
            if ((self.x > RIGHT_BOUNDARY - self.radius) and (self.x_speed > 0)):
                
                self.x_speed = self.x_speed * (-1) * self.elasticity

                #Goal detection
                if ((self.y < GROUND_BOUNDARY) and (self.y > GROUND_BOUNDARY - GOAL_SIZE)):
                    self.red_kick_off()
                    self.placar.addBlueGoal()
    
    def handleWallCollision_and_GoalDetection(self):
        self.handleLeftWallCollision_and_GoalDetection()
        self.handleRightWallCollision_and_GoalDetection()
        self.handleRoofCollision()

    def handleGoalpostCollision(self):

        #top-side post collision
        if (self.y + self.radius > GOALPOST_TOP) and \
           (self.y < GOALPOST_TOP) and \
           ((self.x + self.radius >= GOALPOST_RIGHT_WALL) or (self.x - self.radius <= GOALPOST_LEFT_WALL)):
            
            self.y_speed *= (-1) * self.elasticity

            #avoid cases of stuck ball
            if (self.x >= RIGHT_BOUNDARY - GOALPOST_WIDTH):
                self.x_speed -= 1
            elif(self.x <= LEFT_BOUNDARY + GOALPOST_WIDTH):
                self.x_speed += 1

    def handleFriction(self):
        if self.y_speed == 0 and self.x_speed != 0.0:
            if self.x_speed > 0:
                self.x_speed -= self.frictionCoefficient
            elif self.x_speed < 0:
                self.x_speed += self.frictionCoefficient
        if abs(self.x_speed) <= self.stopMovement:
            self.x_speed = 0
    
    def handleSpin(self):
        if self.x_speed > 0:
            self.angle -= BALL_SPIN
        if self.x_speed < 0:
            self.angle += BALL_SPIN

    def handlePhysics(self):
        self.handleGravity_and_FloorCollision()
        self.handleWallCollision_and_GoalDetection()
        self.handleFriction()
        self.checkPlayerCollision()
        self.handleSpin()
        self.handleGoalpostCollision()
        self.y += self.y_speed
        self.x += self.x_speed

    def update(self):
        if not Pause.isPaused:
            self.handlePhysics()
