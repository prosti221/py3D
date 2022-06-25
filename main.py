import colorsys
import random
import multiprocessing
import time
import numpy as np
import pygame as pg

from render import *

if __name__ == '__main__': # Testing the rendering
    renderer = Render()
    #initializing the screen
    screen, pg = renderer.init()
    #creating a Mesh object for testing
    test_object = Object("objects/rifle.obj")
    test_object.load_mesh()
    test_object.mesh = renderer.transform(test_object.mesh, d_x = 0, d_y = 0, d_z = 0)
    #setting a temporary camera and lighting direction
    
    c = 0.1
    run = True
    while(run):
        sTime = time.time()
        screen.fill(WHITE)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        renderer.rotate_cube(test_object.mesh, c)
        pg.display.flip()
        c += 3 
        eTime = time.time()
        print("FPS: %d" %(1/(eTime - sTime)))
