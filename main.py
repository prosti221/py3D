import time
import pygame as pg
from object import Object
from render import Render
from transform import get_camera_axis_transformation, get_obj_axis_transformation
from globals import *

if __name__ == '__main__': # Testing the rendering
    renderer = Render()
    #initializing the screen
    display, pg = renderer.create()
    #creating a Mesh object for testing
    test_object = Object("objects/rifle.obj")
    test_object.load_mesh()
    test_object.apply_transform(get_camera_axis_transformation(d_z=4, d_x=-1))
    
    run = True
    amplitude = 0.07
    frequency = 1.3
    frame_count = 0
    sTime = time.time()
    while(run):
        renderer.clear()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        d_y = amplitude * np.sin(2 * np.pi * frequency * (time.time() - sTime))
        test_object.apply_transform(get_obj_axis_transformation(test_object.position, theta_x=5, d_y=d_y))
        renderer.draw(test_object, wire_frame=True)
        renderer.update()
        frame_count += 1
        print("FPS: %d" % (frame_count / (time.time() - sTime)))
