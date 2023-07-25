import numpy as np
import matplotlib.pyplot as plt

def show(img):
    if isinstance(img,str):
        img = plt.imread(img)
    plt.imshow(img,cmap='gray')
    plt.colorbar()
    plt.show()