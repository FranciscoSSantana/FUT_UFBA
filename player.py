from tupy import *

class Player(Image):
    def __init__(self, x = 100, y = 100):
        self.x = x
        self.y = y

    def kick(self):
        pass

    def update(self):
        if keyboard.is_key_just_down('a'):