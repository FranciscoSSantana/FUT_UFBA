from tupy import *

class Player(Image):

    def __init__(self, x = 100, y = 400, file = "player.jpg", wasd_scheme = True):
        self.x = x
        self.y = y
        self.jumping = False
        self.file = file

        self.x_speed = 5
        self.jump_height = 20
        self.y_speed = self.jump_height
        self.y_gravity = 2

        if wasd_scheme:
            self.left = 'a'
            self.right = 'd'
            self.jump_key = 'w'
            self.power_key = 'space'
        else:
            self.left = 'Left'
            self.right = 'Right'
            self.jump_key = 'Up'
            self.power_key = 'enter'

    def kick(self):
        pass

    def update(self):
        if keyboard.is_key_down(self.left):
            self.x -= self.x_speed
        if keyboard.is_key_down(self.right):
            self.x += self.x_speed
        if keyboard.is_key_just_down(self.jump_key):
            self.jumping = True
        if keyboard.is_key_down(self.power_key):
            pass

        if self.jumping:
            self.y -= self.y_speed
            self.y_speed -= self.y_gravity
            if self.y_speed < -self.jump_height:
                self.jumping = False
                self.y_speed = self.jump_height
