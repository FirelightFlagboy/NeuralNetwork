# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbenneto <f.benneto@student.42.fr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/06 21:49:53 by fbenneto          #+#    #+#              #
#    Updated: 2018/03/06 21:49:54 by fbenneto         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# coding:utf-8

import os

from Perceptron import Perceptron
from Window import Window
from Training import Point
import time

win = Window()
points = []
brain = Perceptron()


def show():
    err = 0

    for pts in points:
        x = pts.x
        y = pts.y
        tg = pts.label
        brain.train([x, y, 1], tg)
        res = brain.guess([x, y])
        if res == tg:
            win.fill("green")
        else:
            err = 1
            win.fill("red")
        win.ellipse(x, y, 2, 2)
    win.update()
    if err == 0:
        print("done total node:{}".format(len(points)))
        return
    print("err: {} brain:".format(err), brain.weights)
    time.sleep(0.5)
    show()


def main():
    print(brain.weights, end="\n")
    win.createCanvas(500, 500)
    win.fill("black")
    win.background("white")
    win.line(0, 0, win.width, win.height)

    for i in range(0, 10000):
        points.append(Point(win))

    for pts in points:
        x = pts.x
        y = pts.y
        tg = pts.label
        res = brain.guess([x, y, 1])
        if res == tg:
            win.fill("green")
        else:
            win.fill("red")
        win.ellipse(x, y, 2, 2)
    win.update()
    time.sleep(1)
    show()
    print("we learn")
    print(brain.weights)
    os.system("pause")


if __name__ == '__main__':
    main()
