import numpy as np

def addition(*args):
    v = 0
    for arg in args:
        v +=  arg
    return np.sin(v)
