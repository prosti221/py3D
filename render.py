import numpy as np
import pygame as pg

from utils import get_projection_matrix
from globals import *

from camera import Camera
from light import Light


class Render():
    def __init__(self):
        self.matProj = get_projection_matrix()

    def create(self):
        pg.init()
        self.display = pg.display
        self.display.set_caption("3D Renderer")
        self.display.set_mode((WIDTH, HEIGHT))

        self.camera = Camera(0, 0, 0)
        self.light = Light(0, 0, -1)

        return (self.display, pg)

    def clear(self):
        self.display.get_surface().fill(BLACK)
    
    def update(self):
        self.display.flip()
    
    def destroy(self):
        pg.quit()

    def draw(self, object, wire_frame=False):
        cur_polygon = np.zeros((3, 3))
        for poly in object.mesh.polygons:
            #Project from 3D space to 2D space
            if poly.isVisible(self.camera.pos):
                #shader = poly.shader(BLACK, self.light.direction)
                for i, vertex in enumerate(poly.vertecies):
                    point4d = np.dot(self.matProj, vertex.coord)
                    point4d /= (point4d[3] if point4d[3] != 0 else 1)

                    point4d[0] = (point4d[0] + 1) * 0.5 * WIDTH 
                    point4d[1] = (1 - (point4d[1] + 1) * 0.5) * HEIGHT

                    cur_polygon[i] = point4d[:3]

                #Draw the polygon
                if wire_frame:
                    pg.draw.line(self.display.get_surface(), CYAN, (cur_polygon[0][0], cur_polygon[0][1]), (cur_polygon[1][0], cur_polygon[1][1]))
                    pg.draw.line(self.display.get_surface(), CYAN, (cur_polygon[1][0], cur_polygon[1][1]), (cur_polygon[2][0], cur_polygon[2][1]))
                    pg.draw.line(self.display.get_surface(), CYAN, (cur_polygon[2][0], cur_polygon[2][1]), (cur_polygon[0][0], cur_polygon[0][1]))
                else: 
                    pg.draw.polygon(surface=self.display.get_surface(), color=CYAN, points=[(int(cur_polygon[0][0]), int(cur_polygon[0][1])), 
                                                                          (int(cur_polygon[1][0]), int(cur_polygon[1][1])), 
                                                                          (int(cur_polygon[2][0]), int(cur_polygon[2][1]))])
