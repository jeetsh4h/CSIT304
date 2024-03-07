import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x_left = -10; x_right = 10; y_bottom = -10; y_top = 10

radius = 3; n_points = 1024

end_angle = np.pi / 4; start_angle = 0

def draw_para_circle():
    dtheta = (2 * np.pi) / n_points
    
    glPointSize(2.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)    # black
    for theta in np.arange(0, 2*np.pi + 0.001, dtheta):
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        
        glVertex2f(x, y)
    glEnd()

def pizza_slice():
    draw_para_circle()

    assert start_angle < end_angle, "start_angle must be less than end_angle"
    
    grad = np.tan((start_angle + end_angle) / 2)

    glPointSize(2.0)
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.5, 0.0)    # orange
    for theta in np.arange(start_angle, end_angle + 0.001, 0.001):
        x = radius * np.cos(theta)
        y = radius * np.sin(theta)
        
        glVertex2f(x + 0.5, y + (0.5 * grad))    # translating

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

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(1000, 0)

    glutCreateWindow("Clipped Triangles")
    initialize()

    glutDisplayFunc(pizza_slice)

    glutMainLoop()


if __name__ == "__main__":
    main()