import numpy as np

class Light:
    def __init__(self, x=0, y=0, z=0):
        self.direction = np.array([x, y, z], dtype=np.float64)/np.linalg.norm(np.array([x, y, z], dtype=np.float64))
