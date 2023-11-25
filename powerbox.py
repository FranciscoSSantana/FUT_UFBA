from tupy import*
from gameconstants import *
from player import Player
from ball import Ball
from pause import Pause

class PowerBox(Image):
    _IsPowerBox_on = False
    
    @property
    def isPowerBox_on(self):
        return PowerBox._IsPowerBox_on
    
    @isPowerBox_on.setter
    def isPowerBox_on(self, p):
        PowerBox._IsPowerBox_on = p

    
    def __init__(self):
        self.file = "PowerBox.png"
        self.x = POWER_BOX_X_KICK_OFF
        self.y = POWER_BOX_y_KICK_OFF
        self.y_speed = POWER_BOX_Y_SPEED
        self.direction = 1
        
        self.kick_off()
        
    def _destroy(self) -> None:
        super()._destroy()
      
    def kick_off(self) -> None:
        PowerBox.isPowerBox_on = False
        self._hide()
        self.counter = 0
        self.power_counter = 0
        
    def spawn_timer(self) -> None:
        self.counter += 1
        if self.counter == POWER_BOX_SPAWN_TIME:
            self.spawn()
        
    def movement(self) -> None:
        self.y += self.y_speed * self.direction
        if self.y > POWER_BOX_y_KICK_OFF or self.y < POWER_BOX_y_KICK_OFF - 50:
            self.direction *= -1
        
    
    def spawn(self):
        self._show()
        PowerBox.isPowerBox_on = True
        
    def detect_collision(self) -> None:
        if PowerBox.isPowerBox_on:
            for player in Player.PLAYERS:
                if self._collides_with(player):
                    player.boost = True
                    PowerBox.isPowerBox_on = False
                    self._hide()
                    self.counter = 0
    
    def handlePower(self, p):
        self.power_counter += 1
        if self.power_counter == POWER_TIME:
            p.boost = False
            self.power_counter = 0
            
        
    def update(self):
        if not Pause.isPaused:
            if PowerBox.isPowerBox_on:
                self._show()
            self.movement()
            self.spawn_timer()
            self.detect_collision()
            for player in Player.PLAYERS:
                if player.boost:
                    self.handlePower(player)
        else:
            if PowerBox.isPowerBox_on:
                self._hide()
            