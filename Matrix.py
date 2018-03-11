# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbenneto <f.benneto@student.42.fr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/11 18:12:07 by fbenneto          #+#    #+#              #
#    Updated: 2018/03/11 18:12:07 by fbenneto         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint


class Matrix():

    def __init__(self, row, colums):
        self.row = row
        self.colums = colums
        self.matrix = []

        for i in range(0, row):
            self.matrix.append([])
            for y in range(0, colums):
                self.matrix[i].append(0)

    def __str__(self):
        s = ""
        for i in range(0, self.row):
            s += str(self.matrix[i]) + "\n"
        return (s)

    def __add__(self, n):
        if type(n) is Matrix:
            for i in range(0, self.row):
                for y in range(0, self.colums):
                    self.matrix[i][y] += n.matrix[i][y]
        elif type(n) is int:
            for i in range(0, self.row):
                for y in range(0, self.colums):
                    self.matrix[i][y] += n
        else:
            raise ValueError("error 'n' is not an int or a matrix")
        return (self)

    def __mul__(self, n):
        if type(n) is Matrix:
            for i in range(0, self.row):
                for y in range(0, self.colums):
                    self.matrix[i][y] *= n.matrix[i][y]
        elif type(n) is int:
            for i in range(0, self.row):
                for y in range(0, self.colums):
                    self.matrix[i][y] *= n
        else:
            raise ValueError("error 'n' is not an int or a matrix")
        return (self)

    def randomize(self):
        for x in range(0, self.row):
            for y in range(0, self.colums):
                self.matrix[x][y] = randint(0, 100)
