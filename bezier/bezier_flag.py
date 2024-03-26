import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Function to calculate Bezier curve point at t for a given set of control points
def bezier(t, P):
    n = len(P) - 1      # Degree of the Bezier curve
    B = np.zeros(2)     # Initialize the point on the curve
    for i in range(n + 1):
        B += np.array(P[i]) * nCr(n, i) * (1 - t)**(n - i) * t**i
    return B

# Binomial coefficient function
def nCr(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def draw_circle(radius, center, num_segments):
    angle = 2 * np.pi / num_segments

    circle_points = []
    for i in range(num_segments + 1):
        x = radius * np.cos(i * angle)
        y = radius * np.sin(i * angle)
        circle_points.append([x, y])

    translate = np.array(
        [[1, 0, center[0]],
         [0, 1, center[1]],
         [0, 0, 1        ]]
    )

    glLineWidth(2.0)
    glColor3f(0.0, 0.0, 0.0)    # Black color
    glBegin(GL_LINE_STRIP)
    for point in np.array(circle_points):
        translated_point = translate @ np.array([point[0], point[1], 1]).T
        glVertex2f(*translated_point[:-1])
    glEnd()


def draw_flag():
    diff_layer_flag = 50

    glClear(GL_COLOR_BUFFER_BIT)

    # Control points for the flag,,, top layer
    ogP = np.array([[-100.0, 200.0], [-25.0, 125.0], [25.0, 275.0], [100.0, 200.0]])
    P = ogP.copy()

# Drawing the flag
    glColor3f(1.0, 0.0, 0.0)    # Red color
    glLineWidth(2.0)
    
    glBegin(GL_LINE_STRIP)
    for t in np.linspace(0, 1, 1000):
        B = bezier(t, P)
        glVertex2f(B[0], B[1])
    glEnd()


    P[:, 1] = P[:, 1] - diff_layer_flag     # translating the control points down by 50 units
    
    glColor3f(0.0, 0.0, 1.0)    # Blue color
    glLineWidth(2.0)
    
    glBegin(GL_LINE_STRIP)
    for t in np.linspace(0, 1, 1000):
        B = bezier(t, P)
        glVertex2f(B[0], B[1])
    glEnd()

    # drawing circle
    draw_circle((diff_layer_flag // 2) - 5, [(P[0, 0] + P[-1, 0]) // 2, abs(P[1, 1] - P[2, 1]) - (diff_layer_flag // 2)], 1000)

    P[:, 1] = P[:, 1] - diff_layer_flag     # translating the control points down by 50 units
    glColor3f(0.0, 1.0, 0.0)    # Green color
    glLineWidth(2.0)
    
    glBegin(GL_LINE_STRIP)
    for t in np.linspace(0, 1, 1000):
        B = bezier(t, P)
        glVertex2f(B[0], B[1])
    glEnd()


    P[:, 1] = P[:, 1] - diff_layer_flag     # translating the control points down by 50 units
    glColor3f(1.0, 0.0, 0.0)    # Green color
    glLineWidth(2.0)
    
    glBegin(GL_LINE_STRIP)
    for t in np.linspace(0, 1, 1000):
        B = bezier(t, P)
        glVertex2f(B[0], B[1])
    glEnd()


    # drawing the two lines
    glColor3f(0.0, 0.0, 0.0)    # Black color
    glLineWidth(2.0)

    glBegin(GL_LINES)
    glVertex2f(*ogP[0])
    glVertex2f(*P[0])

    glVertex2f(*ogP[-1])
    glVertex2f(*P[-1])
    glEnd()



# #to print the control points 
#     glPointSize(5.0)
#     glBegin(GL_POINTS)
#     for p in P:
#         glVertex2f(p[0], p[1])
#     glEnd()

    glFlush()



def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)    # bg color white

    # screen size, in terms of co-ordinates
    gluOrtho2D(-300, 300, -300, 300)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(600, 600)
    glutInitWindowPosition(1000, 0)

    glutCreateWindow("Bezier Flag")
    initialize()

    glutDisplayFunc(draw_flag)

    glutMainLoop()


if __name__ == "__main__":
    main()