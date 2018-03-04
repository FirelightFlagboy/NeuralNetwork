#codind: utf-8

import random


class Perceptron():
    """
    a class for neural network it represent each
    neuron
    """

    def __init__(self):
        """ the constructor,
        it initialize the the weights of axon randomly
        """
        self.len = 3
        self.lr = 0.05
        self.weights = []
        for i in range(0, self.len):
            self.weights.append(random.uniform(-1, 1))

    def __sign(self, sumOpt):
        """ to know if the neuron is activated or not"""
        if sumOpt >= 0:
            return (1)
        else:
            return (-1)

    def guess(self, ipt):
        sumOpt = 0
        for i in range(0, len(ipt)):
            sumOpt += ipt[i] * self.weights[i]
        return (self.__sign(sumOpt))

    def train(self, ipt, target):
        guess = self.guess(ipt)
        error = target - guess

        for i in range(0, len(self.weights)):
            self.weights[i] += error * ipt[i] * self.lr
