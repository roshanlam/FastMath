import numpy as np

def gaussain(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-np.power((x - mu)/sigma, 2) / 2)

