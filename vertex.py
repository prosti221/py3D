import numpy as np

class Vertex:
    def __init__(self, x, y, z):
        #Contains an extra dimension for the matrix multiplication
        self.coord = np.array([ x, y, z, 1], dtype=np.float64) 
