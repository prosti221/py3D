import numpy as np
from vertex import *
from polygon import *
from mesh import *

#This represents scene objects
class Object:
    def __init__(self, file):
        self.file = file
        self.mesh = None 
    
    def load_mesh(self):
        vertecies = []
        polygons = []
        with open(self.file) as file:
            for line in file:
                elements = line.split(' ')
                if "v" in elements:
                    elements = [float(e) for e in elements if e != "v"]
                    vertecies.append(Vertex(*elements))
                elif "f" in elements:
                    elements = [int(e.split('/')[0]) for e in elements if e != "f" and e != '\n']
                    index = (elements[0], elements[1], elements[2])
                    params = [vertecies[index[0] - 1], vertecies[index[1] - 1], vertecies[index[2] - 1]]
                    polygons.append(Polygon(params))
        self.mesh = Mesh(polygons)

    def print(self):
        for polygon in self.mesh.m:
            polygon.toString() 

