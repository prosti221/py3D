import numpy as np
from globals import *
from utils import parse_obj
from vertex import Vertex 
from mesh import Mesh

class Object:
    def __init__(self, file=None):
        self.file = file
        self.mesh = None
        self.position = (0, 0, 0) # center point of the object

    def load_mesh(self):
        polygons = parse_obj(self.file)
        self.mesh = Mesh(polygons)
        self.position = self.get_center_point()

    def print(self):
        for polygon in self.mesh.polygons:
            polygon.toString() 
    
    def get_center_point(self):
        x, y, z = 0, 0, 0
        for poly in self.mesh.polygons:
            for vert in poly.vertecies:
                x += vert.coord[0]
                y += vert.coord[1]
                z += vert.coord[2]
        x /= len(self.mesh.polygons) * 3
        y /= len(self.mesh.polygons) * 3
        z /= len(self.mesh.polygons) * 3
        return (x, y, z)

    def apply_transform(self, transform):
        x, y, z = 0, 0, 0
        #Transform all the vertecies
        for i, poly in enumerate(self.mesh.polygons):
            for j, vertex in enumerate(poly.vertecies):
                x += vertex.coord[0]; y += vertex.coord[1]; z += vertex.coord[2]
                new_vert = np.dot(transform, vertex.coord)
                # Creating a new vertex object, modyfing in place leads to weird behavior
                self.mesh.polygons[i].vertecies[j] = Vertex(new_vert[0], new_vert[1], new_vert[2])

        self.position = (x/(len(self.mesh.polygons) * 3), y/(len(self.mesh.polygons) * 3), z/(len(self.mesh.polygons) * 3))

    def apply_scale(self, scale_factor):
        for poly in self.mesh.polygons:
            for vert in poly.vertecies:
                new_vert = np.array(vert.coord[:3]) * scale_factor
                vert.coord = np.append(new_vert, 1)
    