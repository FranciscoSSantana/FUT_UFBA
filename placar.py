from tupy import *
from gameconstants import *
from pause import Pause

class Placar(Image):
    def __init__(self):
        self.x = X_CENTER
        self.y = PLACAR_Y
        self.t1 = Image(self.get_number_image(0), TIME_TENS_X, TIME_Y)
        self.t2 = Image(self.get_number_image(0), TIME_UNITS_X, TIME_Y)
        self.blueScore_image_tens = Image(self.get_number_image(0), BLUE_SCORE_TENS_X, SCORE_Y)
        self.blueScore_image_units = Image(self.get_number_image(0), BLUE_SCORE_UNITS_X, SCORE_Y)
        self.redScore_image_tens = Image(self.get_number_image(0), RED_SCORE_TENS_X, SCORE_Y)
        self.redScore_image_units = Image(self.get_number_image(0), RED_SCORE_UNITS_X, SCORE_Y)
        self.kick_off()

    def _destroy(self) -> None:
        self.t1._destroy()
        self.t2._destroy()
        self.blueScore_image_tens._destroy()
        self.blueScore_image_units._destroy()
        self.redScore_image_tens._destroy()
        self.redScore_image_units._destroy()
        super()._destroy()
    
    def update(self):
        if not Pause.isPaused:
            self.counter += 1
            if self.counter == 21:
                self.counter = 0
                self.tempo -= 1
                self.update_number_images()
            if self.tempo == 0:
                 self.get_winner()
    
    def kick_off(self):
        self.ganhador = 0
        self.counter = 0
        self.blueScore = BLUE_INITIAL_SCORE
        self.redScore = RED_INITIAL_SCORE
        self.tempo = TIME
        self.update_number_images()

    def update_number_images(self):
        t1_digit = self.tempo // 10
        t2_digit = self.tempo % 10

        self.t1.file = self.get_number_image(t1_digit)
        self.t2.file = self.get_number_image(t2_digit)

        blueScore_tens_digit = self.blueScore // 10
        blueScore_units_digit = self.blueScore % 10

        self.blueScore_image_tens.file = self.get_number_image(blueScore_tens_digit)
        self.blueScore_image_units.file = self.get_number_image(blueScore_units_digit)

        redScore_tens_digit = self.redScore // 10
        redScore_units_digit = self.redScore % 10

        self.redScore_image_tens.file = self.get_number_image(redScore_tens_digit)
        self.redScore_image_units.file = self.get_number_image(redScore_units_digit)

    def get_number_image(self, digit):
         return f'{digit}.png'

    def addRedGoal(self):
        self.redScore += 1
        self.update_number_images()

    def addBlueGoal(self):
        self.blueScore += 1
        self.update_number_images()

    def get_winner(self):
        if self.redScore > self.blueScore:
            self.ganhador = 2
        if self.blueScore > self.redScore:
            self.ganhador = 1
        Pause.isPaused = True
