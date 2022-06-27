import numpy as np
import colorsys

class Polygon:
    def __init__(self, vertecies):
        self.vertecies = vertecies 

    #Find the normal of the polygon plane
    def getNormal(self):
        A = self.vertecies[1].coord[:3] - self.vertecies[0].coord[:3]
        B = self.vertecies[2].coord[:3] - self.vertecies[1].coord[:3]
        normal = np.cross(A, B)
        return normal/np.linalg.norm(normal)
    
    #Check if the polygon should be visible to the camera
    def isVisible(self, camera_pos):
        normal = self.getNormal()
        similarity = np.dot(normal, self.vertecies[0].coord[:3] - camera_pos)
        if similarity < 0:
            return True
        return False

    # Temporary shader function
    def shader(self, color, light):
        normal = self.getNormal()
        dp = np.dot(normal, self.vertecies[0].coord[:3]/np.linalg.norm(self.vertecies[0].coord[:3]) - light)
        HSV = colorsys.rgb_to_hsv(*color)
        HSV = (HSV[0], HSV[1], HSV[2] - dp*10)
        color_sh = colorsys.hsv_to_rgb(*HSV)
        return color_sh

    def toString(self):
        print('Polygon: \n')
        for v in self.vertecies:
            print(v.coord)