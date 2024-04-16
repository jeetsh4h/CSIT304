import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

ortho_proj = (-300.0, 300.0, -300.0, 300.0)


def display():
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)
    glEnd()
    glFlush()


def zoom(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        window_width = glutGet(GLUT_WINDOW_WIDTH)
        window_height = glutGet(GLUT_WINDOW_HEIGHT)

        ortho_x_start = ortho_proj[0] + x / window_width * (ortho_proj[1] - ortho_proj[0])
        ortho_y_start = ortho_proj[2] + (window_height - y) / window_height * (ortho_proj[3] - ortho_proj[2])
        
        print(ortho_x_start, ortho_y_start)

    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        window_width = glutGet(GLUT_WINDOW_WIDTH)
        window_height = glutGet(GLUT_WINDOW_HEIGHT)

        ortho_x_end = ortho_proj[0] + x / window_width * (ortho_proj[1] - ortho_proj[0])
        ortho_y_end = ortho_proj[2] + (window_height - y) / window_height * (ortho_proj[3] - ortho_proj[2])

        print(ortho_x_end, ortho_y_end)

    print()



def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(*ortho_proj)
    glClear(GL_COLOR_BUFFER_BIT)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(600, 600)
    glutInitWindowPosition(960, 0)

    glutCreateWindow(b"Mandelbrot Set")
    init()

    glutMouseFunc(zoom)
    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()