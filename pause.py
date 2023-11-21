from tupy import *
from gameconstants import *
from menu import Menu
from menu import Resume
from menu import Restart


class Pause(Image):
    def __init__(self, file = "pause.png"):
        self.x = RIGHT_BOUNDARY - 50
        self.y = UPPER_BOUNDARY + 50
        self.file = file
        self.menu = False
        self.resume = None
        self.restart = None
        self.back = None
        
    def pause(self):
        if self.menu:
            if mouse.x > self.resume.x - 100 and mouse.x < self.resume.x + 100 and \
                mouse.y > self.resume.y - 40 and mouse.y < self.resume.y + 40 and mouse.is_button_just_down():
                        from game import playerBlue
                        from game import playerRed
                        from game import bola
                        from game import placar
                        self.resume._hide()
                        self.restart._hide()
                        self.back._hide()
                        playerBlue.game_is_on = True
                        playerRed.game_is_on = True
                        bola.game_is_on = True
                        placar.game_is_on = True
                        self.menu = False        
        
        if mouse.x > self.x - 20 and mouse.x < self.x + 20 and \
            mouse.y > self.y - 24 and mouse.y < self.y + 24 and mouse.is_button_just_down():
                from game import playerBlue
                from game import playerRed
                from game import bola
                from game import placar
                playerBlue.game_is_on = False
                playerRed.game_is_on = False
                bola.game_is_on = False
                placar.game_is_on = True
                self.back = Menu()
                self.resume = Resume()
                self.restart = Restart()
                self.menu = True
                
    def update(self):
        self.pause()
        
                
