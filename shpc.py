#Sutherland-Hodgeman Polygon clipping algorithm

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Input polygon vertices
input_polygon = [(165, 20), (25, 20), (25, 200), (150, 200)]

# Clipping window coordinates
xmin, ymin, xmax, ymax = 75, 75, 175, 175

def sutherland_hodgman(input_polygon, xmin, ymin, xmax, ymax):
    output_polygon = input_polygon
    #print(output_polygon)

    # Clip against left edge
    print('Left Clip')
    output_polygon = clip_against_edge(output_polygon, xmin, ymin, xmin, ymax,'l')

    # Clip against right edge
    print('Right Clip')
    output_polygon = clip_against_edge(output_polygon, xmax, ymin, xmax, ymax,'r')

    # Clip against bottom edge
    print('Bottom Clip')
    output_polygon = clip_against_edge(output_polygon, xmin, ymin, xmax, ymin,'b')

    # Clip against top edge
    print('Top Clip')
    output_polygon = clip_against_edge(output_polygon, xmin, ymax, xmax, ymax,'t')

    return output_polygon

def clip_against_edge(polygon, x1, y1, x2, y2,code):
    clipped_polygon = []

    # Handle wraparound
    v1 = polygon[-1]
    print('V1: ', v1)

    for v2 in polygon:
        print('V2: ', v2)
        if inside(v2, x1, y1, x2, y2,code):
            print('v2 inside')
            if inside(v1, x1, y1, x2, y2,code):
                print('v1 inside')
                # Both vertices inside, add v2
                print('Add V2')
                clipped_polygon.append(v2)
            else:
                # v1 outside, v2 inside, add intersection point
                print('v1 outside, v2 inside')
                intersection_point = compute_intersection(v1, v2, x1, y1, x2, y2)
                clipped_polygon.append(intersection_point)
                clipped_polygon.append(v2)
                print('Intersection Point ', intersection_point)
        elif inside(v1, x1, y1, x2, y2,code):
            # v1 inside, v2 outside, add intersection point
            print('v1 inside, v2 outside')
            intersection_point = compute_intersection(v1, v2, x1, y1, x2, y2)
            clipped_polygon.append(intersection_point)
            print('Intersection Point ', intersection_point)
        else:
            print('V1 and V2 Outside')
            print('Do not store vertices')

        v1 = v2
    print(clipped_polygon)
    return clipped_polygon

def inside(vertex, x1, y1, x2, y2,code):
    # Check if a vertex is inside the specified edge
    x, y = vertex
    if code=='l':
        if x>x1:
            return 1
        else:
            return 0
    if code=='r':
        if x<x1:
            return 1
        else:
            return 0
    if code == 't':
        if y<y1:
            return 1
        else:
            return 0
    if code == 'b':
        if y>y1:
            return 1
        else:
            return 0
        
def compute_intersection(v1, v2, x1, y1, x2, y2):
    # Compute the intersection point of the line segment (v1, v2) and the edge (x1, y1) to (x2, y2)
    x3, y3 = v1
    x4, y4 = v2

    intersection_x = 0
    intersection_y = 0

    # Compute the intersection point using parametric representation
    t = ((x2 - x1) * (y1 - y3) + (y2 - y1) * (x3 - x1)) / ((x2 - x1) * (y4 - y3) - (y2 - y1) * (x4 - x3))
    intersection_x = x3 + t * (x4 - x3)
    intersection_y = y3 + t * (y4 - y3)

    return (intersection_x, intersection_y)

def draw_polygon(polygon):
    glBegin(GL_POLYGON)
    for vertex in polygon:
        glVertex2f(*vertex)
    glEnd()

def draw_clipping_window(xmin, ymin, xmax, ymax):
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(xmin, ymin)
    glVertex2f(xmin, ymax)
    glVertex2f(xmax, ymax)
    glVertex2f(xmax, ymin)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Original polygon
    glColor3f(0.0, 1.0, 1.0)
    draw_polygon(input_polygon)

    # Clipping window
    draw_clipping_window(xmin, ymin, xmax, ymax)

    # Clipped polygon
    glColor3f(1.0, 0.0, 1.0)
    clipped_polygon = sutherland_hodgman(input_polygon, xmin, ymin, xmax, ymax)
    print(clipped_polygon)
    draw_polygon(clipped_polygon)

    glFlush()

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Sutherland-Hodgman Polygon Clipping")
    gluOrtho2D(0, 300, 0, 300)
    glutDisplayFunc(display)
    glutMainLoop()