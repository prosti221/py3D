from globals import *
from vertex import Vertex
from polygon import Polygon

def get_projection_matrix():
    return np.array([[(1/ASPECT) * E, 0, 0, 0],
                    [0, E, 0 ,0],
                    [0, 0, -((FAR + NEAR)/(FAR - NEAR)), (-2 * FAR * NEAR)/(FAR - NEAR)],
                    [0, 0, -1.0, 0]])

def parse_obj(file):
    vertecies = []
    polygons = []
    with open(file) as file:
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
    
    return polygons