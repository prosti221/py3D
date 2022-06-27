import numpy as np

Rx = lambda theta_x: np.array([[1, 0, 0, 0],
                                [0, np.cos(np.deg2rad(theta_x)), -np.sin(np.deg2rad(theta_x)), 0],
                                [0, np.sin(np.deg2rad(theta_x)), np.cos(np.deg2rad(theta_x)), 0],
                                [0, 0, 0, 1]])

Ry = lambda theta_y: np.array([[np.cos(np.deg2rad(theta_y)), 0, np.sin(np.deg2rad(theta_y)), 0],
                               [0, 1, 0, 0],
                               [-np.sin(np.deg2rad(theta_y)), 0, np.cos(np.deg2rad(theta_y)), 0],
                               [0, 0, 0, 1]])

Rz = lambda theta_z: np.array([[np.cos(np.deg2rad(theta_z)), -np.sin(np.deg2rad(theta_z)), 0, 0],
                               [np.sin(np.deg2rad(theta_z)), np.cos(np.deg2rad(theta_z)), 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])

T = lambda d_x, d_y, d_z: np.array([[1, 0, 0, d_x],
                                    [0, 1, 0, d_y],
                                    [0, 0, 1, d_z],
                                    [0, 0, 0, 1]])

# If no arguments are passed, the identity matrix is returned
def get_camera_axis_transformation(theta_x=0, theta_y=0, theta_z=0, d_x=0, d_y=0, d_z=0):
    M = np.eye(4)
    if theta_z:
        M = np.matmul(M, Rz(theta_z))
    if theta_y:
        M = np.matmul(M, Ry(theta_y))
    if theta_x:
        M = np.matmul(M, Rx(theta_x))
    
    if d_x or d_y or d_z:
        M = np.matmul(T(d_x, d_y, d_z), M)

    return M

# If no arguments are passed, the identity matrix is returned
def get_obj_axis_transformation(object_position, theta_x=0, theta_y=0, theta_z=0, d_x=0, d_y=0, d_z=0):
    x, y, z = object_position
    M = np.eye(4)
    if theta_z:
        M = np.matmul(M, Rz(theta_z))
    if theta_y:
        M = np.matmul(M, Ry(theta_y))
    if theta_x:
        M = np.matmul(M, Rx(theta_x))
    
    if d_x or d_y or d_z:
        M = T(d_x, d_y, d_z) @ T(x, y, z) @ M @ T(-x, -y, -z)
    else:
        M = T(x, y, z) @ M @ T(-x, -y, -z)

    return M
