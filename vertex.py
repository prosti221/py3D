import numpy as np

class Vertex:
    def __init__(self, x, y, z):
        self.coord = np.array([ x, y, z, 1]) 
    
    def __str__(self):
        return f"Vertex: {self.coord}"
    
    def update_coord(self, coords):
        self.coord = coords

    def normalize(self):
        return self.coord[:3]/self.coord[3] 