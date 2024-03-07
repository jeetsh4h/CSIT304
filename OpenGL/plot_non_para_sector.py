import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def draw_sector():
    glBegin(GL_POINTS)

    for x in np.arange(0., 1.1, 0.1):
        y = (1 - x * x)**0.5
        print(x, y)
        glVertex2f(x, y)

    glEnd()
    glFlush()


def initialize():
    glClearColor(1.0, 1.0, 1.0, 0.0)  # Set the window color to white

    gluOrtho2D(-5, 5, -5, 5)

# # draw axes
#     glLineWidth(2.0)
#     glBegin(GL_LINES)
#     glColor3f(0.0, 0.0, 0.0)    # black

#     # x-axis
#     glVertex2f(-5, 0)
#     glVertex2f(5, 0)

#     # y-axis
#     glVertex2f(0, -5)
#     glVertex2f(0, 5)

#     glEnd()


def main():
    glutInit()  # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Set the display mode to be single buffer and RGB color
    
    glutInitWindowSize(500, 500)  # Set the window size
    glutInitWindowPosition(500, 500)  # Set the window position
    
    glutCreateWindow(b"Sector")  # Set the window title

    initialize()  # Call the initialize function

    glutDisplayFunc(draw_sector)  # Set the display function
    glutMainLoop()  # Run the infinite loop to keep the window open


if __name__ == "__main__":
    main()