#coding:utf-8

from Perceptron import *

def main():
	n = Perceptron()
	ipt = [1,1,1,1]
	
	print(n.weights, end="\n\n")
	print(n.guess(ipt))

if __name__ == '__main__':
	main()
