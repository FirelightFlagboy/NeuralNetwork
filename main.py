#coding:utf-8

from Perceptron import *

def main():
	n = Perceptron()
	print(n.weights)
	print(n.guess([1,1,1,1]))

if __name__ == '__main__':
	main()
