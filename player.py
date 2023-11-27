from tupy import *
from gameconstants import *
from pause import Pause

class Player(BaseImage):
        
    _PLAYERS: list["Player"] = []

    @classmethod
    def playerList(cls) -> list["Player"]:
        return Player._PLAYERS.copy()

    def __init__(self, isBluePlayer: bool = True) -> None:
        
        self._isBluePlayer: bool = isBluePlayer

        self._jump_height: int = PLAYER_JUMP_HEIGHT
        self._gravity: float = PLAYER_GRAVITY
        self._mass: float = PLAYER_MASS
        self._radius: int = PLAYER_RADIUS
        self._ballCollisionCooldown: int = PLAYER_BALL_COLLISION_COOLDOWN
        self._boost: bool = False

        self._file: str = "PlayerBlue.png" if isBluePlayer else "PlayerRed.png"
        self._left: str = 'a' if isBluePlayer else 'Left'
        self._right: str = 'd' if isBluePlayer else 'Right'
        self._jump_key: str = 'w' if isBluePlayer else 'Up'
        
        self.kick_off()

        Player._PLAYERS.append(self)
    
    def _destroy(self) -> None:
        Player._PLAYERS.remove(self)
        super()._destroy()

    def kick_off(self) -> None:
        '''
        Standard start/restart function.
        '''
        self._y: int = PLAYER_Y_SPAWN
        self._jumping: bool = False
        self._x_speed: float = 0
        self._y_speed: float = 0

        self._x: int = BLUE_PLAYER_X_SPAWN if self._isBluePlayer else RED_PLAYER_X_SPAWN
    
    def _movementInput(self) -> None:
        if keyboard.is_key_down(self._left):
            self._x_speed = -PLAYER_X_MOVING_SPEED
        if keyboard.is_key_down(self._right):
            self._x_speed = PLAYER_X_MOVING_SPEED
        if keyboard.is_key_just_down(self._jump_key) and self._jumping is False:
            self._jumping = True
            self._jump_height = PLAYER_JUMP_HEIGHT
            self._y_speed = self._jump_height

        if keyboard.is_key_up(self._left) and self._x_speed < 0:
            self._x_speed = 0
        if keyboard.is_key_up(self._right) and self._x_speed > 0:
            self._x_speed = 0
            
    
    def _Power_movementInput(self) -> None:
        '''
        Movement if powerbox was collected.
        '''
        if keyboard.is_key_down(self._left):
            self._x_speed = -PLAYER_X_POWER_MOVING_SPEED
        if keyboard.is_key_down(self._right):
            self._x_speed = PLAYER_X_POWER_MOVING_SPEED
        if keyboard.is_key_just_down(self._jump_key) and self._jumping is False:
            self._jumping = True
            self._jump_height = PLAYER_POWER_JUMP_HEIGHT
            self._y_speed = self._jump_height

        if keyboard.is_key_up(self._left) and self._x_speed < 0:
            self._x_speed = 0
        if keyboard.is_key_up(self._right) and self._x_speed > 0:
            self._x_speed = 0

    def _handleJump(self) -> None:
        if self._jumping:
            self._y += round(self._y_speed)
            self._y_speed += self._gravity
            if self._y_speed > -self._jump_height:
                self._jumping = False
                self._y_speed = 0
    
    def _move(self) -> None:
        '''
        Executes Player Movement and bounds it to the field.
        '''
        if self._boost:
            self._Power_movementInput()
            self._handleJump()
        else:
            self._movementInput()
            self._handleJump()
        if self._x - PLAYER_WIDTH//2 >= LEFT_BOUNDARY and self._x + PLAYER_WIDTH//2 <= RIGHT_BOUNDARY:
            self._x += round(self._x_speed)
        else:
            if self._x - PLAYER_WIDTH//2 < LEFT_BOUNDARY:
                self._x += PLAYER_WIDTH//8
            else:
                self._x -= PLAYER_WIDTH//8

    def update(self) -> None:
        if not Pause.isGamePaused():
            self._move()
    
    @property
    def x(self) -> int:
        return self._x
    
    @property
    def y(self) -> int:
        return self._y
    
    @property
    def x_speed(self) -> float:
        return self._x_speed
    
    @property
    def y_speed(self) -> float:
        return self._y_speed
    
    @property
    def radius(self) -> int:
        return self._radius
    
    @property
    def mass(self) -> float:
        return self._mass
    
    @property
    def ballCollisionCooldown(self) -> int:
        return self._ballCollisionCooldown
    
    def resetBallCollisionCooldown(self) -> None:
        self._ballCollisionCooldown = 0
    
    def tickBallCollisionCooldown(self) -> None:
        if self.ballCollisionCooldown < PLAYER_BALL_COLLISION_COOLDOWN:
            self._ballCollisionCooldown += 1
    
    @property
    def boost(self) -> bool:
        return self._boost
    
    def toggleBoost(self) -> None:
        self._boost = True if self._boost == False else False
