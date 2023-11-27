from tupy import *
from gameconstants import *
from buttons import MenuBackground, Resume, Restart

class Pause(BaseImage):
    _isPaused: bool = False

    @classmethod
    def isGamePaused(cls) -> bool:
        return Pause._isPaused

    @classmethod
    def freeze(cls) -> None:
        Pause._isPaused = True

    @classmethod
    def unfreeze(cls) -> None:
        Pause._isPaused = False

    def __init__(self) -> None:
        self._x: int = RIGHT_BOUNDARY - BUTTON_OFFSET
        self._y: int = UPPER_BOUNDARY + BUTTON_OFFSET
        self._file: str = "pause.png"
        self._gameRestart: bool = False
        self._menuBackground: MenuBackground = MenuBackground()
        self._resumeButton: Resume = Resume()
        self._restartButton: Restart = Restart()
        self._resume()
    
    def _destroy(self) -> None:
        self._menuBackground._destroy()
        self._resumeButton._destroy()
        self._restartButton._destroy()
        super()._destroy()

    def kick_off(self) -> None:
        '''
        Standard start/restart function.
        '''
        self._resume()
        self._gameRestart = False

    def _pause(self) -> None:
        self._resumeButton._show()
        self._restartButton._show()
        self._menuBackground._show()
        Pause.freeze()
    
    def _resume(self) -> None:
        self._resumeButton._hide()
        self._restartButton._hide()
        self._menuBackground._hide()
        Pause.unfreeze()
    
    def _restart(self) -> None:
        self._gameRestart = True
        self._resume()

    def _detectPauseCommand(self) -> None:
        '''
        Handles pause buttons and actions.
        '''
        if Pause.isGamePaused():
            if ((self._resumeButton._contains_point(mouse.x, mouse.y) or self._contains_point(mouse.x, mouse.y)) \
                and mouse.is_button_just_down()) \
                or keyboard.is_key_just_down('p'):
                self._resume()

            elif self._restartButton._contains_point(mouse.x, mouse.y) and mouse.is_button_just_down():
                self._restart()

        else:
            if (self._contains_point(mouse.x, mouse.y) and mouse.is_button_just_down()) \
                or keyboard.is_key_just_down('p'):

                self._pause()

    def update(self) -> None:
        self._detectPauseCommand()
    
    @property
    def gameRestart(self) -> bool:
        return self._gameRestart
                
