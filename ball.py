from tupy import *
from gameconstants import *
from player import Player
from pause import Pause
import numpy as np

class Ball(BaseImage):
    def __init__(self) -> None:
        self._radius: int = BALL_RADIUS
        self._stopBounce: float = BALL_BOUNCE_STOP_COEFFICIENT
        self._elasticity: float = BALL_ELASTICITY
        self._frictionCoefficient: float = BALL_FRICTION_COEFFICIENT
        self._stopMovement: float = BALL_STOP_MOVEMENT_COEFFICIENT

        self._gravity: float = BALL_GRAVITY
        self._mass: float = BALL_MASS

        self.kick_off()
    
    def kick_off(self) -> None:
        '''
        Standard start/restart function. Also used upon goal detection
        '''
        self._x: int = BALL_KICK_OFF_X
        self._y: int = BALL_KICK_OFF_Y
        self._x_speed: float = BALL_KICK_OFF_X_SPEED
        self._y_speed: float = BALL_KICK_OFF_Y_SPEED

        playerList: list[Player] = Player.playerList()
        for player in playerList:
            player.kick_off()
    
    def _blue_kick_off(self) -> None:
        '''
        kick-off after Blue Player received a goal
        '''
        self.kick_off()
        self._x_speed = BALL_BLUE_KICK_OFF_X_SPEED
    
    def _red_kick_off(self) -> None:
        '''
        kick-off after Red Player received a goal
        '''
        self.kick_off()
        self._x_speed = BALL_RED_KICK_OFF_X_SPEED
    
    def _handleGravity_and_FloorCollision(self) -> None:
        #Apply gravity
        if self._y < (GROUND_BOUNDARY - self._radius):
            self._y_speed += self._gravity
        else:
            #Floor collision
            if self._y_speed > self._stopBounce:
                self._y_speed = self._y_speed * (-1) * self._elasticity
            else:
                if abs(self._y_speed) <= self._stopBounce:
                    self._y_speed = 0
    
    def _checkPlayerCollision(self) -> None:
        '''
        Checks if a player and the ball have collided. Upon collision,
        applies cooldown for colliding again.
        '''
        playerList: list[Player] = Player.playerList()
        if len(playerList) > 0:
            for player in playerList:

                player.tickBallCollisionCooldown()

                distance = ((self._x - player.x)**2 + (self._y - player.y)**2)**0.5
                if (distance <= self._radius + player.radius) and (player.ballCollisionCooldown == PLAYER_BALL_COLLISION_COOLDOWN):
                    player.resetBallCollisionCooldown()
                    self._handlePlayerCollision(player)

    def _handlePlayerCollision(self, player: Player) -> None:
        '''
        Calculates new velocities for the ball after collision
        with player. Calculations made based on post by Chad Berchek, 2009
        https://www.vobarian.com/collisions/2dcollisions2.pdf
        '''
        normal_vector = np.array([self._x - player.x, self._y - player.y])
        normal_vector = normal_vector / np.linalg.norm(normal_vector)
        tangent_vector = np.array([-1 * normal_vector[1], normal_vector[0]])

        ball_speed_vector = np.array([self._x_speed, self._y_speed])
        player_speed_vector = np.array([player.x_speed, player.y_speed])

        ball_normal_speed = np.dot(normal_vector, ball_speed_vector)
        ball_tangent_speed = np.dot(tangent_vector, ball_speed_vector)

        player_normal_speed = np.dot(normal_vector, player_speed_vector)

        ball_new_normal_speed = (ball_normal_speed * (self._mass - player.mass) + (2 * player.mass * player_normal_speed)) / (self._mass + player.mass)
        ball_speed_vector = (ball_new_normal_speed * normal_vector) + (ball_tangent_speed * tangent_vector)

        self._x_speed = ball_speed_vector[0] * self._elasticity
        self._y_speed = ball_speed_vector[1] * self._elasticity

    def _handleRoofCollision(self) -> None:
        if ((self._y < UPPER_BOUNDARY + self._radius) and (self._y_speed < 0)):
            self._y_speed = self._y_speed * (-1) * self._elasticity

    def _handleLeftWallCollision_and_GoalDetection(self) -> bool:
        '''
        Returns True if goal was detected, False if not.
        '''
        #Side-wall collisions
        if ((self._x < LEFT_BOUNDARY + self._radius) and (self._x_speed < 0)):
            
            self._x_speed = self._x_speed * (-1) * self._elasticity

            #Goal detection
            if ((self._y < GROUND_BOUNDARY) and (self._y > GROUND_BOUNDARY - GOAL_SIZE)):
                self._blue_kick_off()
                return True
        return False

    def _handleRightWallCollision_and_GoalDetection(self) -> bool:
        '''
        Returns True if goal was detected, False if not.
        '''
        #Side-wall collisions
        if ((self._x > RIGHT_BOUNDARY - self._radius) and (self._x_speed > 0)):
            
            self._x_speed = self._x_speed * (-1) * self._elasticity

            #Goal detection
            if ((self._y < GROUND_BOUNDARY) and (self._y > GROUND_BOUNDARY - GOAL_SIZE)):
                self._red_kick_off()
                return True
        return False
    
    def _handleWallCollision_and_GoalDetection(self) -> None:
        self._handleLeftWallCollision_and_GoalDetection()
        self._handleRightWallCollision_and_GoalDetection()
        self._handleRoofCollision()

    def _handleGoalpostCollision(self) -> None:

        #top-side post collision
        if (self._y + self._radius > GOALPOST_TOP) and \
           (self._y < GOALPOST_TOP) and \
           ((self._x + self._radius >= GOALPOST_RIGHT_WALL) or (self._x - self._radius <= GOALPOST_LEFT_WALL)):
            
            self._y_speed *= (-1) * self._elasticity

            #avoid cases of stuck ball
            if (self._x >= RIGHT_BOUNDARY - GOALPOST_WIDTH):
                self._x_speed -= 1
            elif(self._x <= LEFT_BOUNDARY + GOALPOST_WIDTH):
                self._x_speed += 1

    def _handleFriction(self) -> None:
        if self._y_speed == 0 and self._x_speed != 0.0:
            if self._x_speed > 0:
                self._x_speed -= self._frictionCoefficient
            elif self._x_speed < 0:
                self._x_speed += self._frictionCoefficient
        if abs(self._x_speed) <= self._stopMovement:
            self._x_speed = 0
    
    def _handleSpin(self) -> None:
        if self._x_speed > 0:
            self._angle -= BALL_SPIN
        if self._x_speed < 0:
            self._angle += BALL_SPIN

    def _handlePhysics(self) -> None:
        self._handleGravity_and_FloorCollision()
        self._handleWallCollision_and_GoalDetection()
        self._handleFriction()
        self._checkPlayerCollision()
        self._handleSpin()
        self._handleGoalpostCollision()
        self._y += round(self._y_speed)
        self._x += round(self._x_speed)

    def update(self) -> None:
        if not Pause.isGamePaused():
            self._handlePhysics()
