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

    def _mulMatrix(self, mat):
        if self.colums != mat.rows:
            raise ValueError("error matrix size")

        res = Matrix(self.rows, mat.colums)

        for i in range(0, res.rows):
            for j in range(0, res.colums):
                for k in range(0, self.colums):
                    res.matrix[i][j] += self.matrix[i][k] * mat.matrix[k][j]
        return (res)

    def __init__(self, rows, colums):
        self.rows = rows
        self.colums = colums
        self.matrix = []

        for i in range(0, rows):
            self.matrix.append([])
            for y in range(0, colums):
                self.matrix[i].append(0)

    def __str__(self):
        s = ""
        for i in range(0, self.rows):
            s += str(self.matrix[i]) + "\n"
        return (s)

    def __add__(self, n):
        res = Matrix(self.rows, self.colums)
        if type(n) is Matrix:
            for i in range(0, self.rows):
                for y in range(0, self.colums):
                    res.matrix[i][y] = self.matrix[i][y] + n.matrix[i][y]
        elif type(n) is int:
            for i in range(0, self.rows):
                for y in range(0, self.colums):
                    res.matrix[i][y] = self.matrix[i][y] + n
        else:
            raise ValueError("error 'n' is not an int or a matrix")
        return (res)

    def __mul__(self, n):
        if type(n) is Matrix:
            return (self._mulMatrix(n))
        elif type(n) is int:
            res = Matrix(self.rows, self.colums)
            for i in range(0, self.rows):
                for y in range(0, self.colums):
                    res.matrix[i][y] = self.matrix[i][y] * n
        else:
            raise ValueError("error 'n' is not an int or a matrix")
        return (res)

    def randomize(self):
        for x in range(0, self.rows):
            for y in range(0, self.colums):
                self.matrix[x][y] = randint(0, 100)

    def transpose(self):
        res = Matrix(self.colums, self.rows)
        for r in range(0, res.rows):
            for c in range(0, res.colums):
                res.matrix[r][c] = self.matrix[c][r]
        return (res)
