from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import copy

viewport_coordinates = (-300, 200, 100, 600)
full_polygon = []

def clip_against_edge(edge, polygon):
    # edges will be l, t, r, b,,, thats how they are encoded
    
    global full_polygon, viewport_coordinates
    xmin, xmax, ymin, ymax = viewport_coordinates


def kohen_sutherland():
    global full_polygon, viewport_coordinates
    xmin, xmax, ymin, ymax = viewport_coordinates

    clip_polygon = copy.deepcopy(full_polygon)

    clip_polygon_l = clip_against_edge('l', clip_polygon)
    



def viewport():
    global line_start, line_end
    clip_polygon = kohen_sutherland()

    glClear(GL_COLOR_BUFFER_BIT)

    glBegin(GL_POLYGON)

    # add vertices to draw a polygon
    # use glvertex2f to add vertices
    # for loop use karo
    
    glEnd()
    glFlush()


def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)    # bg color white
    gluOrtho2D(*viewport_coordinates)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(
        abs(viewport_coordinates[1] - viewport_coordinates[0]), 
        abs(viewport_coordinates[3] - viewport_coordinates[2])
    )
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Viewport Drawing")
    initialize()


    global full_polygon
    full_polygon = []

    glutDisplayFunc(viewport)

    glutMainLoop()


if __name__ == "__main__":
    main()