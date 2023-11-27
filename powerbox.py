from tupy import*
from gameconstants import *
from player import Player
from pause import Pause

class PowerBox(BaseImage):
    _isPowerBox_on: bool = False

    def __init__(self) -> None:
        self._file: str = "PowerBox.png"
        self._x: int = POWER_BOX_X_KICK_OFF
        self._y: int = POWER_BOX_Y_KICK_OFF
        self._y_speed: int = POWER_BOX_Y_SPEED
        self._direction: int = 1
        
        self.kick_off()
        
    def _destroy(self) -> None:
        super()._destroy()
      
    def kick_off(self) -> None:
        '''
        Standard start/restart function.
        '''
        PowerBox._isPowerBox_on = False
        self._hide()
        self._counter: int = 0
        self._power_counter: int = 0
        playerList: list[Player] = Player.playerList()
        for player in playerList:
            if player.boost:
                player.toggleBoost()
        
    def _spawn_timer(self) -> None:
        self._counter += 1
        if self._counter == POWER_BOX_SPAWN_TIME:
            self._spawn()
        
    def _movement(self) -> None:
        self._y += self._y_speed * self._direction
        if self._y > POWER_BOX_Y_KICK_OFF or self._y < POWER_BOX_Y_KICK_OFF - 50:
            self._direction *= -1
        
    def _spawn(self) -> None:
        self._show()
        PowerBox._isPowerBox_on = True
        
    def _detect_collision(self) -> None:
        if PowerBox._isPowerBox_on:
            playerList = Player.playerList()
            for player in playerList:
                if self._collides_with(player):
                    player.toggleBoost()
                    PowerBox._isPowerBox_on = False
                    self._hide()
                    self._counter = 0
    
    def _handlePower(self, player: Player) -> None:
        '''
        Removes power from the player after certain amount of time.
        '''
        self._power_counter += 1
        if self._power_counter == POWER_TIME:
            player.toggleBoost()
            self._power_counter = 0
            
        
    def update(self) -> None:
        if not Pause.isGamePaused():
            if PowerBox._isPowerBox_on:
                self._show()
            self._movement()
            self._spawn_timer()
            self._detect_collision()
            playerList = Player.playerList()
            for player in playerList:
                if player.boost:
                    self._handlePower(player)
        else:
            if PowerBox._isPowerBox_on:
                self._hide()
            
