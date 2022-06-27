import numpy as np

#window size
WIDTH = 854
HEIGHT = 480

#Perspective projection parameters
NEAR = 0.1
FAR = 100.0
FOV = 90
ASPECT = float(WIDTH / HEIGHT)
E = 1.0/np.tan(np.deg2rad(FOV)/2)

#Colors
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
GREEN = (1, 180, 30)