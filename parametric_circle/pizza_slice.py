import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_circle_with_pizza_slice():
    radius = 2
    num_segments = 32
    center = [2, 2]

    # pizza_slice_angle = (0, (3 * np.pi) / 8)
    # pizza_slice_angle = ((3 * np.pi) / 8, (5 * np.pi) / 8)
    pizza_slice_angle = ((-1 * np.pi) / 8, (1 * np.pi) / 8)
    slice_offset = 0.5

    if pizza_slice_angle[0] > pizza_slice_angle[1]:
        pizza_slice_angle = tuple(reversed(pizza_slice_angle))

# calculating points of the rest of the pizza
    pizza_points = [[0, 0, 1]]  # adding the center of the origin circle
    for angle in np.arange(
        pizza_slice_angle[1],
        (2 * np.pi) + pizza_slice_angle[0] + 0.01,
        (2 * np.pi) / num_segments,
    ):
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        pizza_points.append([x, y, 1])

# calculating points of the pizza slice
    slice_points = [[0, 0, 1]]  # adding the center of the origin circle
    for angle in np.arange(
        pizza_slice_angle[0], 
        pizza_slice_angle[1] + 0.1, 
        (2 * np.pi) / num_segments
    ):
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        slice_points.append([x, y, 1])

# translating along the line drawn from the origin and the center of the pizza slice arc
    grad = np.tan(sum(pizza_slice_angle) / 2)
    tx = slice_offset
    ty = slice_offset * grad 
    if (np.abs(sum(pizza_slice_angle) / 2) == np.pi / 2) or (np.abs(sum(pizza_slice_angle) / 2) == (3 * np.pi) / 2): 
        tx = 0
        ty = slice_offset

    translate_slice = np.array(
            [[1, 0, tx],
             [0, 1, ty],
             [0, 0, 1 ]]
        )

# translating all the points to the appropriate pizza center
    translate_all = np.array(
        [[1, 0, center[0]], 
         [0, 1, center[1]], 
         [0, 0, 1        ]]
    )

# rendering pizza
    glBegin(GL_LINE_LOOP)
    for point in np.array(pizza_points):
        translated_point = translate_all @ point.T

        print(translated_point[:-1])
        glVertex2f(*translated_point[:-1])

    glEnd()

# rendering pizza slice
    glBegin(GL_LINE_LOOP)
    for point in np.array(slice_points):
        translated_point = translate_all @ translate_slice @ point.T
        
        print(translated_point[:-1])
        glVertex2f(*translated_point[:-1])

    glEnd()

    glFlush()


def axes():
    glClear(GL_COLOR_BUFFER_BIT)

    # draw axes
    glLineWidth(1.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)  # black

    # x-axis
    glVertex2f(10, 0)
    glVertex2f(-10, 0)

    # y-axis
    glVertex2f(0, 10)
    glVertex2f(0, -10)

    glEnd()

def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white

    gluOrtho2D(-10, 10, -10, 10)
    axes()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(1000, 0)

    glutCreateWindow("Parametric Circle")
    initialize()

    glutDisplayFunc(draw_circle_with_pizza_slice)

    glutMainLoop()

if __name__ == "__main__":
    main()
