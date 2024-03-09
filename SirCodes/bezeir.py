# Bezier Curve (d=3)

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Control points
P = np.array([[100.0, 100.0], [150.0, 200.0], [250.0, 200.0], [300.0, 100.0]])
# P = np.array([[150.0, 100.0], [150.0, 200.0], [250.0, 200.0], [250.0, 100.0]])

# Function to calculate Bezier curve point at t
def bezier(t):
    B = (1 - t)**3 * P[0] + 3 * (1 - t)**2 * t * P[1] + 3 * (1 - t) * t**2 * P[2] + t**3 * P[3]
    print(B)
    return B

# OpenGL display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(2.0)
    glBegin(GL_LINE_STRIP)
    for t in np.linspace(0, 1, 100):
        B = bezier(t)
        glVertex2f(B[0], B[1])
    glEnd()
    
    # Draw Control Polygon Lines
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(3.0)
    
    glBegin(GL_LINE_STRIP)
    for i in range(len(P)):
        glVertex2f(P[i][0],P[i][1])
    glEnd()
    
    # Draw control Points
    glColor3f(1.0, 1.0, 0.0)
    glPointSize(5.0)
    
    glBegin(GL_POINTS)
    for i in range(len(P)):
        glVertex2f(P[i][0],P[i][1])
    glEnd()
    
    glFlush()

# OpenGL initialization function
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 400.0, 0.0, 300.0)

# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(400, 300)
    glutCreateWindow("Bezier Curve")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()