from tupy import *
from gameconstants import *
from buttons import MenuBackground, Resume, Restart

class Pause(Image):
    _isPaused = False

    @property
    def isPaused(self):
        return Pause._isPaused
    
    @isPaused.setter
    def isPaused(self, p):
        Pause._isPaused = p

    def __init__(self):
        self.x = RIGHT_BOUNDARY - BUTTON_OFFSET
        self.y = UPPER_BOUNDARY + BUTTON_OFFSET
        self.file = "pause.png"
        self.gameRestart = False
        self.menuBackground = MenuBackground()
        self.resumeButton = Resume()
        self.restartButton = Restart()
        self.resume()
    
    def _destroy(self) -> None:
        self.menuBackground._destroy()
        self.resumeButton._destroy()
        self.restartButton._destroy()
        super()._destroy()

    def kick_off(self):
        self.resume()
        self.gameRestart = False

    def pause(self):
        self.resumeButton._show()
        self.restartButton._show()
        self.menuBackground._show()
        Pause.isPaused = True
    
    def resume(self):
        self.resumeButton._hide()
        self.restartButton._hide()
        self.menuBackground._hide()
        Pause.isPaused = False
    
    def restart(self):
        self.gameRestart = True
        self.resume()

    def detectClick(self):
        if Pause.isPaused:
            if (self.resumeButton._contains_point(mouse.x, mouse.y) or self._contains_point(mouse.x, mouse.y)) \
                and mouse.is_button_just_down():
                self.resume()

            elif self.restartButton._contains_point(mouse.x, mouse.y) and mouse.is_button_just_down():
                self.restart()

        else:
            if self._contains_point(mouse.x, mouse.y) and mouse.is_button_just_down():
                self.pause()

    def update(self):
        self.detectClick()
        
                
