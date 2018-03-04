# coding:utf-8

import random


class Point():

    def __init__(self, window):
        self.win = window
        self.x = random.randint(0, window.width)
        self.y = random.randint(0, window.height)
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1

    def show(self):
        if self.label == 1:
            self.win.fill("white")
        else:
            self.win.fill("black")
        self.win.ellipse(self.x, self.y, 3, 3)
