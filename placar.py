from tupy import *
from gameconstants import *

class Placar(Image):

    NUM = [
        "0.png", "1.png", "2.png", "3.png", "4.png",
        "5.png", "6.png", "7.png", "8.png", "9.png"
    ]

    def __init__(self):
        self.x = X_CENTER
        self.y = PLACAR_Y
        self.counter = 0
        self.scoreR = 0
        self.scoreL = 0
        self.game_is_on = True
        self.tempo = 90
        self.t1 = Números(TIME_TENS_X, TIME_Y, self.get_number_image(9))
        self.t2 = Números(TIME_UNITS_X, TIME_Y, self.get_number_image(0))
        self.scoreR_image_tens = Números(SCORE_R_TENS_X, SCORE_Y, self.get_number_image(0))
        self.scoreR_image_units = Números(SCORE_R_UNITS_X, SCORE_Y, self.get_number_image(0))
        self.scoreL_image_tens = Números(SCORE_L_TENS_X, SCORE_Y, self.get_number_image(0))
        self.scoreL_image_units = Números(SCORE_L_UNITS_X, SCORE_Y, self.get_number_image(0))

    def update(self):
        if self.game_is_on:
            self.counter += 1
            if self.counter == 21:
                self.counter = 0
                self.tempo -= 1
                self.update_number_images()
            if self.tempo == 0:
                 self.get_winner()

    def update_number_images(self):
        t1_digit = self.tempo // 10
        t2_digit = self.tempo % 10

        self.t1.file = self.get_number_image(t1_digit)
        self.t2.file = self.get_number_image(t2_digit)

        scoreR_tens_digit = self.scoreR // 10
        scoreR_units_digit = self.scoreR % 10

        self.scoreR_image_tens.file = self.get_number_image(scoreR_tens_digit)
        self.scoreR_image_units.file = self.get_number_image(scoreR_units_digit)

        scoreL_tens_digit = self.scoreL // 10
        scoreL_units_digit = self.scoreL % 10

        self.scoreL_image_tens.file = self.get_number_image(scoreL_tens_digit)
        self.scoreL_image_units.file = self.get_number_image(scoreL_units_digit)

    def get_number_image(self, digit):
         return self.NUM[digit]

    def addgoalL(self):
        self.scoreL += 1
        self.update_number_images()

    def addgoalR(self):
        self.scoreR += 1
        self.update_number_images()

    def get_winner(self):
        from game import playerBlue
        from game import playerRed
        from game import bola
        playerBlue.game_is_on = False
        playerRed.game_is_on = False
        bola.game_is_on = False
        self.game_is_on = False
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
        self.y = Y_CENTER

class Números(Image):
    def __init__(self, x, y, file):
        self.x = x
        self.y = y
        self.file = file





