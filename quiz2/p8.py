## Question 8 ##
# In the class we discussed the Sutherland-Hodgeman Polygon clipping code.
# Demonstrate how the polygons (Triangles (before and after transformation) in this case)
# will be clipped.

import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from copy import deepcopy

# q1
x_left = -10; x_right = 10; y_bottom = -10; y_top = 10

# q2
x_max = 2.0; y_max = 6.0; x_min = -3.0; y_min = 1.0

# q3
#   a)
triangle_a = (-2, 3); triangle_b = (1, 2); triangle_c = (-1, 7)
#   b)
triangle_centroid = ((-2/3), 4.)

# q5
theta = np.radians(-75); a = 3; b = 1.2

# q4
x_c, y_c = triangle_centroid
T = np.array(
    [[a*np.cos(theta), -a*np.sin(theta), -x_c*a*np.cos(theta) + -y_c*(-a)*np.sin(theta) + x_c],
     [b*np.sin(theta), b*np.cos(theta),  -x_c*b*np.sin(theta) + -y_c*b*np.cos(theta) + y_c   ],
     [0,               0,                1                                                   ]]
)

# q6
t_a = 0; t_b = 0; t_c = 8
tt_a = 1; tt_b = 1; tt_c = 2

# q7
#   cohen sutherland algorithm
#       outcode constants
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def encode_point(x, y):
    outcode = INSIDE

    if x < x_min:        # to the left of clip window
        outcode |= LEFT
    elif x > x_max:      # to the right of clip window
        outcode |= RIGHT

    if y < y_min:        # below the clip window
        outcode |= BOTTOM
    elif y > y_max:      # above the clip window
        outcode |= TOP
    
    return outcode

def cohen_sutherland_line_clip(x1, y1, x2, y2, outcode1, outcode2):
    assert outcode1 == encode_point(x1, y1)
    assert outcode2 == encode_point(x2, y2)

    while True:
        if not (outcode1 | outcode2):
            return (x1, y1), (x2, y2)

        elif outcode1 & outcode2:
            return None, None
        
        else:            
            # pick outside point, pick non-zero outcode
            outcodeOut = outcode1 if outcode1 else outcode2
            curr_x = 0; curr_y = 0

            if outcodeOut & TOP:
                # point is above the clip window
                curr_x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                curr_y = y_max

            elif outcodeOut & BOTTOM:
                # point is below the clip window
                curr_x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                curr_y = y_min
            
            elif outcodeOut & RIGHT:
                # point is to the right of clip window
                curr_x = x_max
                curr_y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
            
            elif outcodeOut & LEFT:
                # point is to the left of clip window
                curr_x = x_min
                curr_y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)

            # updating x1, x2, y1, y2
            if outcodeOut == outcode1:  # pointOut == (x1, y1)
                x1, y1 = curr_x, curr_y
                outcode1 = encode_point(x1, y1)
            else: # pointOut == (x2, y2) 
                x2, y2 = curr_x, curr_y
                outcode2 = encode_point(x2, y2)

# q8
def compute_intersection(p1, p2, edge):
    match edge:
        case 'l':
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
            
            int_x = x_min
            int_y = m * x_min + p1[1] - m * p1[0]
        
        case 'r':
            m = (p2[1] - p1[1]) / (p2[0] - p1[0])
            
            int_x = x_max
            int_y = m * x_max + p1[1] - m * p1[0]

        case 'b':
            mi = (p2[0] - p1[0]) / (p2[1] - p1[1])

            int_x = mi * y_min + p1[0] - mi * p1[1]
            int_y = y_min
        
        case 't':
            mi = (p2[0] - p1[0]) / (p2[1] - p1[1])
            
            int_x = mi * y_max + p1[0] - mi * p1[1]
            int_y = y_max

    # print(p1, p2, ":", (int_x, int_y))
    return (int_x, int_y)

def clip_againt_edge(curr_polygon, edge):
    clipped_polygon = []
    
    for p1, p2 in zip(curr_polygon, curr_polygon[1:] + [curr_polygon[0]]):
        # print(p1, p2, edge)
        match edge:
            case 'l':
                if p1[0] > x_min:
                    # first point inside
                    if p2[0] > x_min:
                        # second point inside
                        clipped_polygon.append(p2)
                    else:
                        # second point outside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                else:
                    # first point outside
                    if p2[0] > x_min:
                        # second point inside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                        clipped_polygon.append(p2)
            
            case 'r':
                if p1[0] < x_max:
                    # first point inside
                    if p2[0] < x_max:
                        # second point inside
                        clipped_polygon.append(p2)
                    else:
                        # second point outside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                else:
                    # first point outside
                    if p2[0] < x_max:
                        # second point inside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                        clipped_polygon.append(p2)
            
            case 'b':
                if p1[1] > y_min:
                    # first point inside
                    if p2[1] > y_min:
                        # second point inside
                        clipped_polygon.append(p2)
                    else:
                        # second point outside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                else:
                    # first point outside
                    if p2[1] > y_min:
                        # second point inside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                        clipped_polygon.append(p2)

            case 't':
                if p1[1] < y_max:
                    # first point inside
                    if p2[1] < y_max:
                        # second point inside
                        clipped_polygon.append(p2)
                    else:
                        # second point outside
                        clipped_polygon.append(
                            compute_intersection(p1, p2, edge)
                        )
                else:
                    # first point outside
                    if p2[1] < y_max:
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

def draw_clipped_polygon_triangle():
    triangle = [triangle_a, triangle_b, triangle_c]
    clip_triangle = sutherland_hodgman_polygon_clip(triangle)

    glBegin(GL_POLYGON)
    # draw the original polygon
    glColor3f(1.0, 0.0, 1.0)
    for vertex in clip_triangle:
        glVertex2f(*vertex)
    
    glEnd()

    glFlush()

def draw_clipped_polygon_transform_triangle():
    transform_a = T @ np.array([*triangle_a, 1]).T
    transform_b = T @ np.array([*triangle_b, 1]).T
    transform_c = T @ np.array([*triangle_c, 1]).T

    transform_triangle = [transform_a[:2], transform_b[:2], transform_c[:2]]
    clip_triangle = sutherland_hodgman_polygon_clip(transform_triangle)

    glBegin(GL_POLYGON)
    # draw the original polygon
    glColor3f(1.0, 0.0, 1.0)
    for vertex in clip_triangle:
        glVertex2f(*vertex)
    
    glEnd()

    glFlush()


def draw_clip_triangle():
    # clipping triangle
    clip_points = []
    # using pre-calculated outcodes
    clip_points.append([cohen_sutherland_line_clip(*triangle_a, *triangle_b, t_a, t_b)])
    clip_points.append([cohen_sutherland_line_clip(*triangle_b, *triangle_c, t_b, t_c)])
    clip_points.append([cohen_sutherland_line_clip(*triangle_c, *triangle_a, t_c, t_a)])


    # transformed triangle points
    transform_a = T @ np.array([*triangle_a, 1]).T
    transform_b = T @ np.array([*triangle_b, 1]).T
    transform_c = T @ np.array([*triangle_c, 1]).T

    # clipping transformed traingle
    transform_clip_points = []
    # using pre-calculated outcodes
    transform_clip_points.append([cohen_sutherland_line_clip(*transform_a[:2], *transform_b[:2], tt_a, tt_b)])
    transform_clip_points.append([cohen_sutherland_line_clip(*transform_b[:2], *transform_c[:2], tt_b, tt_c)])
    transform_clip_points.append([cohen_sutherland_line_clip(*transform_c[:2], *transform_a[:2], tt_c, tt_a)])


    # draw clipped triangle
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)    # blue

    for clip_point in clip_points:
        for point in clip_point:
            if point != (None, None):
                glVertex2f(*point[0])
                glVertex2f(*point[1])
    
    glEnd()
    # highlight intersection points
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)    # black
    
    for clip_point in clip_points:
        for point in clip_point:
            if point != (None, None):
                glVertex2f(*point[0])
                glVertex2f(*point[1])

    glEnd()

    # draw transformed clipped triangle
    glBegin(GL_LINES)
    glColor3f(0.0, 0.0, 1.0)    # blue

    for clip_point in transform_clip_points:
        for point in clip_point:
            if point != (None, None):
                glVertex2f(*point[0])
                glVertex2f(*point[1])

    glEnd()
    # highlight intersection points
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 0.0)    # black
    
    for clip_point in transform_clip_points:
        for point in clip_point:
            if point != (None, None):
                glVertex2f(*point[0])
                glVertex2f(*point[1])

    glEnd()

def draw_transformed_triangle():
    transform_a = T @ np.array([*triangle_a, 1]).T
    transform_b = T @ np.array([*triangle_b, 1]).T
    transform_c = T @ np.array([*triangle_c, 1]).T

    glLineWidth(3.0)
    glBegin(GL_LINE_LOOP)

    glColor3f(1.0, 0.0, 0.0)    # red
    glVertex2f(*transform_a[:2])

    glColor3f(0.0, 1.0, 0.0)    # green
    glVertex2f(*transform_b[:2])

    glColor3f(1.0, 1.0, 0.0)    # yellow
    glVertex2f(*transform_c[:2])

    glEnd()

    # draw centroid
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glColor3f(0.0, 0.0, 1.0)    # blues

    glVertex2f(*triangle_centroid)

    glEnd()

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

def until_p7_initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)    # bg color white

    # screen size, in terms of co-ordinates
    gluOrtho2D(x_left, x_right, y_bottom, y_top)
    axes()
    clipping_window()
    draw_triangle()
    draw_transformed_triangle()
    draw_clip_triangle()

def triangle_initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)    # bg color white

    # screen size, in terms of co-ordinates
    gluOrtho2D(x_left, x_right, y_bottom, y_top)
    axes()
    clipping_window()
    draw_triangle()

def transform_triangle_initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)    # bg color white

    # screen size, in terms of co-ordinates
    gluOrtho2D(x_left, x_right, y_bottom, y_top)
    axes()
    clipping_window()
    draw_transformed_triangle()

def main():
    glutInit(sys.argv)

    # window 1
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(1000, 0)
    win1 = glutCreateWindow("Clipped Triangle Cohen-Sutherland Algorithm")
    until_p7_initialize()
    glutDisplayFunc(lambda: glFlush())

    # window 2
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(500, 0)
    win2 = glutCreateWindow("Triangle Triangle Clip")
    triangle_initialize()
    glutDisplayFunc(draw_clipped_polygon_triangle)

    # window 3
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    win3 = glutCreateWindow("Transformed Triangle Clip")
    transform_triangle_initialize()
    glutDisplayFunc(draw_clipped_polygon_transform_triangle)

    glutMainLoop()



if __name__ == "__main__":
    main()