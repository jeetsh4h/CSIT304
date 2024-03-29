import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_sector():
    glBegin(GL_LINE_STRIP)

    for x in np.arange(0., 1.1, 0.1):
        y = (1 - x * x)**0.5
        print(x, y)
        glVertex2f(x, y)

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

    glutDisplayFunc(draw_sector)
    glutMainLoop()


if __name__ == "__main__":
    main()