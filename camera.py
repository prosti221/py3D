import numpy as np

class Camera:
    def __init__(self, x=0, y=0, z=0):
        self.pos = np.array([x, y, z])

