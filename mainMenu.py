from tupy import *
from gameconstants import *
from player import Player
from ball import Ball
from goal import Goal
from background import Background
from pause import Pause
from placar import Placar

class MainMenu(Image):
    def __init__(self) -> None:
        self.x = X_CENTER
        self.y = Y_CENTER
        self.file = "Home.png"
        self.message = Image("PRESS “Enter” TO PLAY.png", X_CENTER, MESSAGE_Y)
        self.counter = MESSAGE_FLICK_SPEED
        self.started = False
    
    def messageFlick(self, message):
        self.counter -= 1
        if self.counter == MESSAGE_FLICK_SPEED/2:
            message._show()
        if self.counter == 0:
            message._hide()
            self.counter = MESSAGE_FLICK_SPEED
    
    def start(self):
        if keyboard.is_key_just_down('space'):
            if self.file == "P1 WINS!.png" or self.file == "P2 WINS!.png":
                self.started = True
                self.winscreen._hide()
                self.winmessage._hide()
                self.pause.gameRestart = True
                self.checkRestart()

            if self.file == "Commands.png":
                self.started = True
                self.message._hide()
                self._hide()
                self.counter = MESSAGE_FLICK_SPEED
                self.startNewGame()

            if self.file == "Home.png":
                self.file = "Commands.png"
                self.message.file = "PRESS “Enter” TO CONTINUE.png"

    def startNewGame(self):
        self.background = Background()
        self.playerBlue = Player(True)
        self.playerRed = Player(False)
        self.placar = Placar()
        self.bola = Ball(self.placar)
        self.pause = Pause()
        self.leftgoal = Goal(True)
        self.rightgoal = Goal(False)

        self.winscreen = Image(f"P{self.placar.ganhador} WINS!.png", X_CENTER, Y_CENTER)
        self.winscreen._hide()
        self.winmessage = Image("PRESS “Enter” TO PLAY.png", X_CENTER, MESSAGE_Y)
        self.winmessage._hide()
    
    def checkRestart(self):
        if self.pause.gameRestart:
            self.background.kick_off()
            self.playerBlue.kick_off()
            self.playerRed.kick_off()
            self.placar.kick_off()
            self.bola.kick_off()
            self.pause.kick_off()
    
    def checkEnd(self):
        self.file = f"P{self.placar.ganhador} WINS!.png"
        self.started = False
        self.winscreen.file = f"P{self.placar.ganhador} WINS!.png"
        self.winscreen._show()
        self.winmessage._show()

    def update(self) -> None:
        if not self.started:
            self.start()
            if self.file == "Home.png" or self.file == "Commands.png":
                self.messageFlick(self.message)
            else:
                self.messageFlick(self.winmessage)
        else:
            self.checkRestart()
            if self.placar.ganhador != 0:
                self.checkEnd()
