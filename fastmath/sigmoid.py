import numpy as np

def sigmoid(value):
    return 1 / (1 + np.exp(-value))