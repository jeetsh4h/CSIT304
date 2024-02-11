# this checks whether OpenGL is working or not

from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glutWireTeapot(0.5)
    # glutWireSphere(0.75, 10, 10)
    # glutWireCube(1.0)
    # glutWireTetrahedron()
    # glutSolidTeapot(0.5)
    # glutSolidSphere(0.75, 10, 10)
    # glutSolidCube(1.0)
    # glutSolidTetrahedron()
    glFlush()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(250, 250)
glutInitWindowPosition(100, 100)
glutCreateWindow("My FIRST OGL Program")
glutDisplayFunc(draw)
glutMainLoop()
