import numpy as np
import pygame as pg

from vertex import *
from polygon import *
from mesh import *
from object import *
from camera import *
from light import *


#window size
WIDTH = 900
HEIGHT = 800

#Colors
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
GREEN = (1, 180, 30)

#Perspective projection parameters
near = 0.1
far = 1000.0
fov = 90.0
aspect = float(WIDTH / HEIGHT)
e = 1.0/np.tan(fov/2)

#Camera border
top = np.tan(fov/2) * near
bottom = -top * aspect
right = top * aspect
left = bottom

#Projection matrix
matProj = np.array([[aspect * e, 0, 0, 0],
                    [0, e, 0 ,0],
                    [0, 0, far/(far - near), 1.0],
                    [0, 0, (-far * near)/(far -near), 0]], dtype=np.float64)

class Render():

    def init(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill(WHITE)
        pg.display.flip()    
        self.camera = Camera(0, 0, 0)
        self.light = Light(0, 0, -1)
        return (self.screen, pg)

    def transform(self, mesh, theta_x=0, theta_y=0, theta_z=0, d_x=0, d_y=0, d_z=0):
        #Homogeneous transformation along the x-axis
        Rx = np.array([[1, 0, 0, d_x], 
                        [0, np.cos(np.deg2rad(theta_x)), -np.sin(np.deg2rad(theta_x)), 0], 
                        [0, np.sin(np.deg2rad(theta_x)), np.cos(np.deg2rad(theta_x)), 0],
                        [0, 0, 0, 1]], dtype=np.float64)
       
        #Homogeneous transformation along the y-axis
        Ry = np.array([[np.cos(np.deg2rad(theta_y)), 0, np.sin(np.deg2rad(theta_y)), 0], 
                        [0, 1, 0, d_y], 
                        [-np.sin(np.deg2rad(theta_y)), 0, np.cos(np.deg2rad(theta_y)), 0],
                        [0, 0, 0, 1]], dtype=np.float64)

        #Homogeneous transformation along the z-axis
        Rz = np.array(  [[np.cos(np.deg2rad(theta_z)), -np.sin(np.deg2rad(theta_z)), 0, 0], 
                        [np.sin(np.deg2rad(theta_z)), np.cos(np.deg2rad(theta_z)), 0, 0], 
                        [0, 0, 1, d_z],
                        [0, 0, 0, 1]], dtype=np.float64)
        
        R = np.matmul(Rz, Ry)
        R = np.matmul(R, Rx)

        transformed_mesh = []
        #Transform all the vertecies
        for poly in mesh.m:
            transformed_verts = []
            for vertex in poly.vertecies:
                new_vert = np.dot(R, vertex.coord)
                transformed_verts.append(Vertex(new_vert[0], new_vert[1], new_vert[2]))
            transformed_mesh.append(Polygon(transformed_verts))
        return Mesh(transformed_mesh)

    def scale(self, mesh, x, y):
        for poly in mesh.m:
            for vert in poly.vertecies:
                vert.coord[1] *= x
                vert.coord[0] *= y

    def draw(self, mesh, screen, pg, wire_frame=False):
        for poly in mesh.m:
            #Project from 3D space to 2D space
            if poly.isVisible(self.camera.pos): #Supposed to check if poly.isVisible(camera.pos) but has a big performance hit
                #shader = poly.shader(BLACK, self.light.direction)
                for vertex in poly.vertecies:
                    vertex.coord = np.dot(vertex.coord, matProj)
                    w = vertex.coord[-1]
                    vertex.coord = np.divide(vertex.coord, w)
                #Draw the polygon
                if wire_frame:
                    pg.draw.line(screen,BLACK, (poly.vertecies[0].coord[0], poly.vertecies[0].coord[1]), (poly.vertecies[1].coord[0], poly.vertecies[1].coord[1]))
                    pg.draw.line(screen,BLACK, (poly.vertecies[1].coord[0], poly.vertecies[1].coord[1]), (poly.vertecies[2].coord[0], poly.vertecies[2].coord[1]))
                    pg.draw.line(screen,BLACK, (poly.vertecies[2].coord[0], poly.vertecies[2].coord[1]), (poly.vertecies[0].coord[0], poly.vertecies[0].coord[1]))
                else: 
                    pg.draw.polygon(surface=screen, color=BLACK, points=[(poly.vertecies[0].coord[0], poly.vertecies[0].coord[1]), (poly.vertecies[1].coord[0], poly.vertecies[1].coord[1]), (poly.vertecies[2].coord[0], poly.vertecies[2].coord[1])])

    def rotate_cube(self, cube, theta):
        #Do the rotations and translations
        mesh_transformed = self.transform(cube, theta_x=theta*0.5, theta_y=0, theta_z=0, d_x=3, d_y=2, d_z=6)
        #Scale the mesh
        self.scale(mesh_transformed, WIDTH, HEIGHT)
        self.draw(mesh_transformed, self.screen, pg, wire_frame=True)

