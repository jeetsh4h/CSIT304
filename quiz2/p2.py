## Question 2 ##
# There is a clipping window with the following specifications: 
# x_max = 2.0, y_max = 6.0, x_min = -3.0, y_min = 1.0. 
# Render the clipping window on the coordinate system of Q1


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# q1
x_left = -10; x_right = 10; y_bottom = -10; y_top = 10
# q2
x_max = 2.0; y_max = 6.0; x_min = -3.0; y_min = 1.0


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

    glFlush()


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



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(1000, 0)

    glutCreateWindow("Viewport")
    initialize()

    glutDisplayFunc(clipping_window)

    glutMainLoop()



if __name__ == "__main__":
    main()