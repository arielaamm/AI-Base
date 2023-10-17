import numpy as np


class Activation(): 
    def ReLU(num):
        return np.max(0,num)
    
    def tanh(num):
        if -1<num<1:
            return None
        return np.tanh(num)
    
    def sigmoid(num):
        if 0<num<1:
            return None
        e = np.e
        return 1/(1+e**-num)