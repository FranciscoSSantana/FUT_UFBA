from tupy import *
from gameconstants import *

class Placar(Image):
    def __init__(self):
        self.x = X_CENTER
        self.y = 49
        self.counter = 0
        self.scoreR = 0
        self.scoreL = 0
        self.game_is_on = True
        self.tempo = 90
        self.label = Label("", self.x - 50, self.y + 50)
        self.atualiza_label()
     

    def update(self):
        if self.game_is_on:
            self.counter += 1
            self.atualiza_label()
            if self.counter == 21:
                self.counter = 0
                self.tempo -= 1
            if self.tempo == 0:
                self.get_winner()

    def atualiza_label(self):
        self.label.text = f"Tempo: {self.tempo}, P1:{self.scoreR}, P2:{self.scoreL}"

    def addgoalL(self):
        self.scoreL +=1

    def addgoalR(self):
        self.scoreR +=1

    def get_winner(self):
        from game import playerBlue
        from game import playerRed
        from game import bola
        playerBlue.game_is_on = False
        playerRed.game_is_on = False
        bola.game_is_on = False
        self.game_is_on == False
        if self.scoreL > self.scoreR:
            ganhador = Ganhador(2)
        if self.scoreR > self.scoreL:
            ganhador = Ganhador(1)

class Ganhador(Image):
    def __init__(self, ganhou):
        if ganhou == 1:
            self.file = "P1 WINS!.png"
        if ganhou == 2:
            self.file = "P2 WINS!.png"
        self.x = X_CENTER
        self. y = Y_CENTER




