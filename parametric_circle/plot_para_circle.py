import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_circle_parametrically():
    radius = 2
    num_segments = 8
    angle = 2 * np.pi / num_segments
    center = [2, 2]


    circle_points = []
    for i in range(num_segments + 1):
        x = radius * np.cos(i * angle)
        y = radius * np.sin(i * angle)
        circle_points.append([x, y, 1])

    translate = np.array(
        [[1, 0, center[0]],
         [0, 1, center[1]],
         [0, 0, 1        ]]
    )


    glBegin(GL_LINE_STRIP)
    for point in np.array(circle_points):
        translated_point = translate @ point.T

        print(translated_point[:-1])
        glVertex2f(*translated_point[:-1])

    glEnd()

    glFlush()


def axes():
    glClear(GL_COLOR_BUFFER_BIT)

    # draw axes
    glLineWidth(1.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)    # black

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

    glutDisplayFunc(draw_circle_parametrically)

    glutMainLoop()


if __name__ == "__main__":
    main()