"""
rotate the cube about the local x-axis by +30 degrees
the origin of the local axes is the centroid of the cube

This means we have to 
- find the centroid of the cube (because rotating about this point,,, essentially)
- translate the cube to the origin
    - translate all the points of the cube by the negative of the centroid
- rotate the cube +30 degrees about the x-axis
- translate the cube back to its original position
"""

from pprint import pprint
import numpy as np

# cube vertices
cube = [[1, 1, 2, 1], 
        [2, 1, 2, 1], 
        [2, 2, 2, 1], 
        [1, 2, 2, 1], 
        [1, 1, 1, 1], 
        [2, 1, 1, 1], 
        [2, 2, 1, 1], 
        [1, 2, 1, 1]]
cube = np.array(cube)

theta = 30 # degrees
theta_r = np.radians(theta)


# finding centroid
centroid = np.mean(cube, axis=0)
# print('centroid:', centroid)    # [1.5 1.5 1.5 1. ]

# translation matrix
tx  =  [[1, 0, 0, -centroid[0]],
        [0, 1, 0, -centroid[1]],
        [0, 0, 1, -centroid[2]],
        [0, 0, 0, 1            ]]
tx = np.array(tx)

# rotation matrix
rx  =  [[1, 0,               0,                0],
        [0, np.cos(theta_r), -np.sin(theta_r), 0],
        [0, np.sin(theta_r), np.cos(theta_r),  0],
        [0, 0,               0,                1]]
rx = np.array(rx)

# reverse translation matrix
ti  =  [[1, 0, 0, centroid[0]],
        [0, 1, 0, centroid[1]],
        [0, 0, 1, centroid[2]],
        [0, 0, 0, 1          ]]
ti = np.array(ti)



rotated_cube = []
for point in cube:
    point = np.array(point).T

    transform_point = ti @ rx @ tx @ point
    rotated_cube.append(transform_point)


print('rotated_cube:')
pprint(rotated_cube)