from typing import Optional
from tupy import *
from gameconstants import *
from ball import Ball
from pause import Pause

class Placar(BaseImage):
    def __init__(self, ball: Ball) -> None:
        self._x: int = X_CENTER
        self._y: int = PLACAR_Y
        self._ball: Ball = ball
        self._t1: _Numero = _Numero('0.png', TIME_TENS_X, TIME_Y)
        self._t2: _Numero = _Numero('0.png', TIME_UNITS_X, TIME_Y)
        self._blueScore_image_tens: _Numero = _Numero('0.png', BLUE_SCORE_TENS_X, SCORE_Y)
        self._blueScore_image_units: _Numero = _Numero('0.png', BLUE_SCORE_UNITS_X, SCORE_Y)
        self._redScore_image_tens: _Numero = _Numero('0.png', RED_SCORE_TENS_X, SCORE_Y)
        self._redScore_image_units: _Numero = _Numero('0.png', RED_SCORE_UNITS_X, SCORE_Y)
        self.kick_off()

    def _destroy(self) -> None:
        self._t1._destroy()
        self._t2._destroy()
        self._blueScore_image_tens._destroy()
        self._blueScore_image_units._destroy()
        self._redScore_image_tens._destroy()
        self._redScore_image_units._destroy()
        super()._destroy()
    
    def kick_off(self) -> None:
        '''
        Standard start/restart function.
        '''
        self._winner: int = 0
        self._counter: int = 0
        self._blueScore: int = BLUE_INITIAL_SCORE
        self._redScore: int = RED_INITIAL_SCORE
        self._tempo: int = TIME
        self._update_number_images()

    def _update_number_images(self) -> None:
        t1_digit = self._tempo // 10
        t2_digit = self._tempo % 10

        self._t1.setNewNumber(t1_digit)
        self._t2.setNewNumber(t2_digit)

        blueScore_tens_digit = self._blueScore // 10
        blueScore_units_digit = self._blueScore % 10

        self._blueScore_image_tens.setNewNumber(blueScore_tens_digit)
        self._blueScore_image_units.setNewNumber(blueScore_units_digit)

        redScore_tens_digit = self._redScore // 10
        redScore_units_digit = self._redScore % 10

        self._redScore_image_tens.setNewNumber(redScore_tens_digit)
        self._redScore_image_units.setNewNumber(redScore_units_digit)

    def _addRedGoal(self) -> None:
        self._redScore += 1
        self._update_number_images()

    def _addBlueGoal(self) -> None:
        self._blueScore += 1
        self._update_number_images()

    def _set_winner(self) -> None:
        '''
        Sets the winner based on result. 1 = P1, 2 = P2, 3 = Tie.
        '''
        if self._redScore > self._blueScore:
            self._winner = 2
        if self._blueScore > self._redScore:
            self._winner = 1
        if self._blueScore == self._redScore:
            self._winner = 3

    def update(self) -> None:
        if not Pause.isGamePaused():
            self._counter += 1
            if self._counter == 21:
                self._counter = 0
                self._tempo -= 1
                self._update_number_images()
            if self._tempo == 0:
                 self._set_winner()

            #receives feedback from the ball if goal was detected and adds if it was
            if self._ball._handleLeftWallCollision_and_GoalDetection():
                self._addRedGoal()
            if self._ball._handleRightWallCollision_and_GoalDetection():
                self._addBlueGoal()
    
    @property
    def winner(self) -> int:
        return self._winner

class _Numero(BaseImage):
    def __init__(self, file: Optional[str] = None, x: Optional[int] = None, y: Optional[int] = None) -> None:
        super().__init__(file, x, y)
    
    @property
    def file(self) -> str:
        return self._file
    
    def setNewNumber(self, digit: int) -> None:
        digit = digit % 10
        self._file = f'{digit}.png'
