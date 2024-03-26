from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from render import render_mandlebrot_set




def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)

    glutCreateWindow(b"Mandelbrot Set")

# Setting the display calback function
    glutDisplayFunc(render_mandlebrot_set)

# setting the idle callabck function
    glutIdleFunc(render_mandlebrot_set)

    glutMainLoop()


if __name__ == "main":
    main()