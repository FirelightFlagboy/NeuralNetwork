# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tests.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbenneto <f.benneto@student.42.fr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/11 20:10:50 by fbenneto          #+#    #+#              #
#    Updated: 2018/03/11 20:45:12 by fbenneto         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.test import TestCase
from NeuralNetwork.Class.Matrix import Matrix

# Create your tests here.
class MatrixTest(TestCase):
	def setUp(self):
		self.matrix_a = Matrix(3, 3)
		self.matrix_b = Matrix(3, 3)
		self.matrix_c = Matrix(2, 3)
		self.matrix_d = Matrix(3, 2)

		self.matrix_a.matrix = [
			[5, 8, 4],
			[9, 5, 6],
			[7, 6, 8]
		]
		self.matrix_b.matrix = [
			[2, 6, 7],
			[16, 4, 3],
			[1, 8, 9]
		]
		self.matrix_c.matrix = [
			[1, 2, 3],
			[4, 5, 6]
		]
		self.matrix_d.matrix = [
			[1, 2],
			[3, 4],
			[5, 6]
		]

	def test_matrix_show(self):
		self.assertEqual(self.matrix_a.__str__(), "[5, 8, 4]\n[9, 5, 6]\n[7, 6, 8]\n")
		self.assertEqual(self.matrix_b.__str__(), "[2, 6, 7]\n[16, 4, 3]\n[1, 8, 9]\n")
		self.assertEqual(self.matrix_c.__str__(), "[1, 2, 3]\n[4, 5, 6]\n")
		self.assertEqual(self.matrix_d.__str__(), "[1, 2]\n[3, 4]\n[5, 6]\n")

	def test_matrix_add(self):
		self.assertEqual(self.matrix_a.__add__(5), "[5, 8, 4]\n[9, 5, 6]\n[7, 6, 8]\n")
		pass
