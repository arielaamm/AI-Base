from ML_objects.Layer import Layer


class ConvolutionLayer(Layer):
    # most of the time KernelHeight = KernelWight
    def __init__(self, KernelHeight, KernelWight):
        self.KernelHeight = KernelHeight
        self.KernelWight = KernelWight
        