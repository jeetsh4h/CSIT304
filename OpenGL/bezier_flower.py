import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x_left = -300; x_right = 300; y_bottom = -300; y_top = 300

P = np.array([[0.0, 0.0], [0.0, 200.0], [150.0, 100.0], [200.0, 0.0]])

def bezier(t):
    B = (1 - t)**3 * P[0] + 3 * (1 - t)**2 * t * P[1] + 3 * (1 - t) * t**2 * P[2] + t**3 * P[3]
    return B

def draw_flower():
    half_petal = []
    for t in np.linspace(0, 1, 100):
        B = bezier(t)
        half_petal.append((B[0], B[1]))

    full_petal = half_petal + [(x, -y) for x, y in half_petal[::-1]]


    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    for vertex in full_petal:   # right
        glVertex2f(*vertex)
    glEnd()
    
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    for vertex in [(-x, y) for x, y in full_petal]:   # left
        glVertex2f(*vertex)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    for vertex in [(y, x) for x, y in full_petal]:   # top
        glVertex2f(*vertex)
    glEnd()

    glColor3f(1.0, 0.0, 1.0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    for vertex in [(-y, -x) for x, y in full_petal]:   # bottom
        glVertex2f(*vertex)
    glEnd()

    glFlush()


def axes():
# clear screen
    glClear(GL_COLOR_BUFFER_BIT)

# draw axes
    glLineWidth(1.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 0.0)    # black

    # x-axis
    glVertex2f(x_left, 0)
    glVertex2f(x_right, 0)

    # y-axis
    glVertex2f(0, y_bottom)
    glVertex2f(0, y_top)

    glEnd()

def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)    # bg color white

    # screen size, in terms of co-ordinates
    gluOrtho2D(x_left, x_right, y_bottom, y_top)
    axes()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(600, 600)
    glutInitWindowPosition(1000, 0)

    glutCreateWindow("Bezier Flower")
    initialize()

    glutDisplayFunc(draw_flower)

    glutMainLoop()


if __name__ == "__main__":
    main()