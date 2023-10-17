class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    '''return the output'''
    def forward(self, input):
        pass

    '''update the parameters and return the input gradient'''
    def backward(self, output_gradient, learning_rate):
        pass
