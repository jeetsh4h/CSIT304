## Question 1 ##
# Write a code to generate a 2D coordinate system, and draw the axis. 
# The specifications are as follows: 
# x-left = -10, x-right = 10, y-bottom = -10, y-top = 10.


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# q1
x_left = -10; x_right = 10; y_bottom = -10; y_top = 10


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

    glFlush()


def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)    # bg color white

    # screen size, in terms of co-ordinates
    gluOrtho2D(x_left, x_right, y_bottom, y_top)



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(1000, 0)

    glutCreateWindow("Co-ordinate axes")
    initialize()

    glutDisplayFunc(axes)

    glutMainLoop()



if __name__ == "__main__":
    main()