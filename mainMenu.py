from typing import Optional
from tupy import *
from gameconstants import *
from player import Player
from ball import Ball
from goal import Goal
from background import Background
from pause import Pause
from placar import Placar
from powerbox import PowerBox

class _Message(BaseImage):
    def __init__(self, file: Optional[str] = None) -> None:
        super().__init__(file, X_CENTER, MESSAGE_Y)
    
    def toggleEnter_or_Continue(self) -> None:
        if self._file == "PressToPlay.png":
            self._file = "PressToContinue.png"
        else:
            self._file = "PressToPlay.png"

class _Winscreen(BaseImage):
    def __init__(self, file: Optional[str] = None) -> None:
        super().__init__(file, X_CENTER, Y_CENTER)
    
    def chooseFile(self, winner: int) -> None:
        '''
        Changes file based on game winner (1, 2 or 3) (number 3 represents a tie.).
        '''
        #data treatment
        if winner < 0 or winner > 3:
            self._file = "P3WINS.png"
        else:
            self._file = f"P{winner}WINS.png"

class MainMenu(BaseImage):
    def __init__(self) -> None:
        self._x: int = X_CENTER
        self._y: int = Y_CENTER
        self._file: str = "Home.png"
        self._message: _Message = _Message("PressToPlay.png")
        self._counter: int = MESSAGE_FLICK_SPEED
        self._started: bool = False
    
    def _messageFlick(self, message: _Message) -> None:
        self._counter -= 1
        if self._counter == MESSAGE_FLICK_SPEED/2:
            message._show()
        if self._counter == 0:
            message._hide()
            self._counter = MESSAGE_FLICK_SPEED
    
    def _start(self) -> None:
        '''
        Handles start and restart of the game upon pressing "Enter".
        '''
        if keyboard.is_key_just_down('Return'):
            if self._file == "P1WINS.png" or self._file == "P2WINS.png" or self._file == "P3WINS.png":
                self._started = True
                self._winscreen._hide()
                self._winmessage._hide()
                self._doRestart()

            if self._file == "Commands.png":
                self._started = True
                self._message._hide()
                self._hide()
                self._counter = MESSAGE_FLICK_SPEED
                self._startNewGame()

            if self._file == "Home.png":
                self._file = "Commands.png"
                self._message.toggleEnter_or_Continue()

    def _startNewGame(self) -> None:
        self._background: Background = Background()
        self._playerBlue: Player = Player(True)
        self._playerRed: Player = Player(False)
        self._bola: Ball = Ball()
        self._placar: Placar = Placar(self._bola)
        self._powerbox: PowerBox = PowerBox()
        self._pause: Pause = Pause()
        self._leftgoal: Goal = Goal(True)
        self._rightgoal: Goal = Goal(False)

        self._winscreen: _Winscreen = _Winscreen()
        self._winscreen._hide()
        self._winmessage: _Message = _Message("PressToPlay.png")
        self._winmessage._hide()
    
    def _checkRestart(self) -> None:
        if self._pause.gameRestart:
            self._doRestart()
    
    def _doRestart(self) -> None:
        self._background.kick_off()
        self._playerBlue.kick_off()
        self._playerRed.kick_off()
        self._placar.kick_off()
        self._bola.kick_off()
        self._pause.kick_off()
        self._powerbox.kick_off()
    
    def _endGame(self) -> None:
        self._file = f"P{self._placar.winner}WINS.png"
        self._started = False
        self._winscreen.chooseFile(self._placar.winner)
        self._winscreen._show()
        self._winmessage._show()

    def update(self) -> None:
        if not self._started:
            self._start()
            if self._file == "Home.png" or self._file == "Commands.png":
                self._messageFlick(self._message)
            else:
                self._messageFlick(self._winmessage)
        else:
            self._checkRestart()
            if self._placar.winner != 0:
                Pause.freeze()
                self._endGame()
