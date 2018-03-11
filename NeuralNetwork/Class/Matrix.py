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

    def __mulMatrix(self, mat):
        """
        multiply the two matrix and return sur result
        """
        if self.colums != mat.rows:
            raise TypeError("error the matrix's size don't match")

        res = Matrix(self.rows, mat.colums)

        for i in range(0, res.rows):
            for j in range(0, res.colums):
                for k in range(0, self.colums):
                    res.matrix[i][j] += self.matrix[i][k] * mat.matrix[k][j]
        return (res)

    def __addMatrix(self, mat):
        """
        simply add the two matrix and return a new matrix
        """
        if self.rows != mat.rows or self.colums != mat.colums:
            raise TypeError("error the matrix's size don't match")

        res = Matrix(self.rows, self.colums)
        for i in range(0, self.rows):
                for y in range(0, self.colums):
                    res.matrix[i][y] = self.matrix[i][y] + mat.matrix[i][y]
        return (res)

    def __init__(self, rows, colums):
        """
        The constructor of the matrix
        """
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
        """
        when the user want to add a matrix or a number
        """
        if type(n) is Matrix:
            return (self.__addMatrix(n))
        elif type(n) is int:
            res = Matrix(self.rows, self.colums)
            for i in range(0, self.rows):
                for y in range(0, self.colums):
                    res.matrix[i][y] = self.matrix[i][y] + n
        else:
            raise TypeError("error 'n' is not an int or a matrix")
        return (res)

    def __mul__(self, n):
        """
        when the user want to multiply a matrix or a scalar
        """
        if type(n) is Matrix:
            return (self.__mulMatrix(n))
        elif type(n) is int:
            res = Matrix(self.rows, self.colums)
            for i in range(0, self.rows):
                for y in range(0, self.colums):
                    res.matrix[i][y] = self.matrix[i][y] * n
        else:
            raise TypeError("error 'n' is not an int or a matrix")
        return (res)

    def randomize(self):
        """
        randomize each node of the matrix with random value between
        0 and 100
        """
        for x in range(0, self.rows):
            for y in range(0, self.colums):
                self.matrix[x][y] = randint(0, 100)

    def transpose(self):
        """
        Transpose the matrix and return a new one
        """
        res = Matrix(self.colums, self.rows)
        for r in range(0, res.rows):
            for c in range(0, res.colums):
                res.matrix[r][c] = self.matrix[c][r]
        return (res)
