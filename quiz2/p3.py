## Question 3 ##
# Consider a triangle with the vertices located at (-2,3), (1,2), (-1,7).
#    Calculate the centroid of the triangle [Pen and Paper]
#    Plot the triangle and the centroid in the coordinate system of Q1 and render them.

from OpenGL.GL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# q1
x_left = -10; x_right = 10; y_bottom = -10; y_top = 10
# q2
x_max = 2.0; y_max = 6.0; x_min = -3.0; y_min = 1.0
# q3
#   a)
triangle_a = (-2, 3); triangle_b = (1, 2); triangle_c = (-1, 7)
#   b)
triangle_centroid = ((-2/3), 4.)


def draw_triangle():
# draw triangle
    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)

    glColor3f(1.0, 0.0, 0.0)    # red
    glVertex2f(*triangle_a)

    glColor3f(0.0, 1.0, 0.0)    # green
    glVertex2f(*triangle_b)

    glColor3f(1.0, 1.0, 0.0)    # yellow
    glVertex2f(*triangle_c)

    glEnd()

# draw centroid
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 1.0)    # blues

    glVertex2f(*triangle_centroid)

    glEnd()

    glFlush()

def clipping_window():
# draw window
    glLineWidth(0.8)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.7, 0.7, 0.7)    # gray

    glVertex2f(x_min, y_min)
    glVertex2f(x_max, y_min)
    glVertex2f(x_max, y_max)
    glVertex2f(x_min, y_max)

    glEnd()

def axes():
# clear screen
    glClear(GL_COLOR_BUFFER_BIT)

# draw axes
    glLineWidth(2.0)
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
    clipping_window()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(1000, 0)

    glutCreateWindow("Draw Triangle and Centroid")
    initialize()

    glutDisplayFunc(draw_triangle)

    glutMainLoop()



if __name__ == "__main__":
    main()