import numpy as np
from Layer import Layer


class Dense(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size, input_size)
        self.bios = np.random.randn(output_size, 1)

    '''return the output'''
    def forward(self, input):
        self.input = input
        return np.dot(self.weights, self.input) + self.bios

    '''update the parameters and return the input gradient''' 
    def backward(self, output_gradient, learning_rate):
        weights_gradient = np.dot(output_gradient,self.input.T)
        self.weights -= learning_rate * weights_gradient
        self.bios -= learning_rate * output_gradient
        return np.dot(self.weights.T,output_gradient)
