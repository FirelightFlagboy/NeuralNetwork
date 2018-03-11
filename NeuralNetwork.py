# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NeuralNetwork.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: fbenneto <f.benneto@student.42.fr>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/06 21:49:25 by fbenneto          #+#    #+#              #
#    Updated: 2018/03/06 21:49:25 by fbenneto         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# coding:utf-8


class NeuralNetwork():
    """
    create a multi-leyar neural network
    """

    def __init__(self, numInput, numHidden, numOutput):
        """
        constructor of the class
        """
        self.input_nodes = numInput
        self.hidden_nodes = numHidden
        self.output_nodes = numOutput
