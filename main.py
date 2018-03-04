# coding:utf-8

import os

from Perceptron import *
from Window import *
from Training import *
import time

win = Window()
points = []


def after(t, fun, *tab, **dic):
    time.sleep(t)
    fun(*tab, *dic)


def show():

    for i in range(0, len(points)):
        points[i].show()
    win.update()
    after(1, show)


def main():
    n = Perceptron()
    ipt = [1, 1, 1, 1]

    print(n.weights, end="\n\n")
    print(n.guess(ipt))
    win.createCanvas(500, 500)
    win.fill("black")
    win.background("white")
    win.line(0, 0, win.width, win.height)

    for i in range(0, 100):
        points.append(Point(win))

    show()
    os.system("pause")


if __name__ == '__main__':
    main()
