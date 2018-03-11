# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Window.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbenneto <f.benneto@student.42.fr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/06 21:49:38 by fbenneto          #+#    #+#              #
#    Updated: 2018/03/06 21:49:38 by fbenneto         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# coding:utf-8

import tkinter


class Window():
    def __init__(self):
        self.window = tkinter.Tk()
        self.__background = "white"
        self.__fill = ""
        self.canvas = "init"
        self.__weigth = 1

    def update(self):
        self.canvas.update()

    def show(self):
        self.canvas.pack()
        self.window.mainloop()

    def fill(self, color=""):
        self.__fill = color

    def strokeWeigth(self, weigth):
        self.__weigth = weigth

    def ellipse(self, x, y, width, height):
        x1 = x - width
        y1 = y - height
        x2 = x + width
        y2 = y + height
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.__fill, width=self.__weigth)
        self.canvas.pack()

    def line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill=self.__fill, width=self.__weigth)
        self.canvas.pack()

    def background(self, color="white"):
        self.__background = color
        if type(self.canvas) != str:
            self.canvas.pack_forget()
        self.canvas = tkinter.Canvas(
            self.window, width=self.width,
            height=self.height, bg=self.__background)
        self.canvas.pack()

    def createCanvas(self, width, height):
        self.width = width
        self.height = height
        self.canvas = tkinter.Canvas(
            self.window, width=self.width,
            height=self.height, bg=self.__background)
        self.canvas.pack()
