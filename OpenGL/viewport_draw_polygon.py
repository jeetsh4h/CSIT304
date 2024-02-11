from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from copy import deepcopy

### global variables
# viewport coordinates
xmin = -300; xmax = 100; ymin = -100; ymax = 300

# intializing input polygon, to feed into clipping algorithm
# this is for convenience, easily updatable
polygon = []

def compute_intersection(p1, p2, edge):
    match edge:
        case 'l':
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
            
            int_x = xmin
            int_y = m * xmin + p1[1] - m * p1[0]
        
        case 'r':
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
            
            int_x = xmax
            int_y = m * xmax + p1[1] - m * p1[0]

        case 'b':
            mi = (p2[0] - p1[0]) / (p2[1] - p1[1])

            int_x = mi * ymin + p1[0] - mi * p1[1]
            int_y = ymin
        
        case 't':
            mi = (p2[0] - p1[0]) / (p2[1] - p1[1])
            
            int_x = mi * ymax + p1[0] - mi * p1[1]
            int_y = ymax

    # print(p1, p2, ":", (int_x, int_y))
    return (int_x, int_y)

def clip_againt_edge(curr_polygon, edge):
    clipped_polygon = []
    
    for p1, p2 in zip(curr_polygon, curr_polygon[1:] + [curr_polygon[0]]):
        # print(p1, p2, edge)
        match edge:
            case 'l':
                if p1[0] > xmin:
                    # first point inside
                    if p2[0] > xmin:
                        # second point inside
                        clipped_polygon.append(p2)
                    else:
                        # second point outside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                else:
                    # first point outside
                    if p2[0] > xmin:
                        # second point inside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                        clipped_polygon.append(p2)
            
            case 'r':
                if p1[0] < xmax:
                    # first point inside
                    if p2[0] < xmax:
                        # second point inside
                        clipped_polygon.append(p2)
                    else:
                        # second point outside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                else:
                    # first point outside
                    if p2[0] < xmax:
                        # second point inside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                        clipped_polygon.append(p2)
            
            case 'b':
                if p1[1] > ymin:
                    # first point inside
                    if p2[1] > ymin:
                        # second point inside
                        clipped_polygon.append(p2)
                    else:
                        # second point outside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                else:
                    # first point outside
                    if p2[1] > ymin:
                        # second point inside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                        clipped_polygon.append(p2)

            case 't':
                if p1[1] < ymax:
                    # first point inside
                    if p2[1] < ymax:
                        # second point inside
                        clipped_polygon.append(p2)
                    else:
                        # second point outside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                else:
                    # first point outside
                    if p2[1] < ymax:
                        # second point inside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                        clipped_polygon.append(p2)

    return clipped_polygon

def sutherland_hodgman_polygon_clip(polygon):
    clip_polygon = deepcopy(polygon)

    # codes for each edge
    for edge in ['l', 'r', 'b', 't']:
        clip_polygon = clip_againt_edge(clip_polygon, edge)
        # print(edge, clip_polygon)
    
    return clip_polygon

def draw_clipped_polygon():
    clip_polygon = sutherland_hodgman_polygon_clip(polygon)
    print(clip_polygon)
    
    glBegin(GL_POLYGON)
    # draw the original polygon
    glColor3f(1.0, 0.0, 0.0)
    for vertex in polygon:
        glVertex2f(*vertex)
    glEnd()

    glBegin(GL_POLYGON)
    # draw the clipped polygon
    glColor3f(0.0, 1.0, 0.0)
    for vertex in clip_polygon:
        glVertex2f(*vertex)
    glEnd()

    glFlush()


def viewport():
# clear screen
    glClear(GL_COLOR_BUFFER_BIT)
    
# draw viewport
    glLineWidth(5.0)
    glBegin(GL_LINES)
# viewport lines
    glColor3f(0.0, 0.0, 0.0)
    # bottom
    glVertex2f(xmin, ymin)
    glVertex2f(xmax, ymin)
    # right
    glVertex2f(xmax, ymin)
    glVertex2f(xmax, ymax)
    # top
    glVertex2f(xmax, ymax)
    glVertex2f(xmin, ymax)
    # left
    glVertex2f(xmin, ymax)
    glVertex2f(xmin, ymin)

    glEnd()

def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)    # bg color white
    gluOrtho2D(-500, 500, -500, 500)    # full screen

    viewport()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(900, 900)
    glutInitWindowPosition(1000, 0)

    glutCreateWindow("Clipping Lines")
    initialize()
    
    # viewport_coordinates = (-300, 100, -100, 300)
    global polygon
    # polygon = [(165, 20), (25, 20), (25, 200), (150, 200)]
    # polygon = [(165, 20), (25, 20), (25, 400), (450, 400)]
    polygon = [(165, 20), (25, 20), (25, -200)]
    
    glutDisplayFunc(draw_clipped_polygon)
    glutMainLoop()


if __name__ == "__main__":
    main()