from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

### global variables
# viewport coordinates
xmin = -300; xmax = 100; ymin = -100; ymax = 300


# outcode constants
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

def encode_point(x, y):
    outcode = INSIDE

    if x < xmin:        # to the left of clip window
        outcode |= LEFT
    elif x > xmax:      # to the right of clip window
        outcode |= RIGHT

    if y < ymin:        # below the clip window
        outcode |= BOTTOM
    elif y > ymax:      # above the clip window
        outcode |= TOP
    
    return outcode

def cohen_sutherland_line_clip(x1, y1, x2, y2):
    outcode1 = encode_point(x1, y1)
    outcode2 = encode_point(x2, y2)

    while True:
        if not (outcode1 | outcode2):
            # bitwise OR is 0 therefore, both points inside window
            # trivially accept and return original points
            return (x1, y1), (x2, y2)

        elif outcode1 & outcode2:
            # bitwise AND is not 0 therefore, both points share an outside area
            # trivially reject and return Nones
            return None, None
        
        else:
            # failed both tests, so calculate the line segment to clip
            # from an outside point to an intersection with clip edge
            
            # pick outside point, pick non-zero outcode
            outcodeOut = outcode1 if outcode1 else outcode2
            curr_x = 0; curr_y = 0

        # bitwise ANDing resulting in non-zero value
        # means that the point is outside the viewport
        # so we need to clip it, based on that viewport edge
            # the formula below is calculating intersection point
            # between the line and the viewport edge
            if outcodeOut & TOP:
                # point is above the clip window
                curr_x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                curr_y = ymax

            elif outcodeOut & BOTTOM:
                # point is below the clip window
                curr_x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                curr_y = ymin
            
            elif outcodeOut & RIGHT:
                # point is to the right of clip window
                curr_x = xmax
                curr_y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
            
            elif outcodeOut & LEFT:
                # point is to the left of clip window
                curr_x = xmin
                curr_y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)

            if outcodeOut == outcode1:  # pointOut == (x1, y1)
                x1, y1 = curr_x, curr_y
                outcode1 = encode_point(x1, y1)
            else: # pointOut == (x2, y2) 
                x2, y2 = curr_x, curr_y
                outcode2 = encode_point(x2, y2)


def clip_polygon():
    NotImplemented

def draw_clipped_polygon():
    NotImplemented


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
    
    
    
    glutDisplayFunc(draw_clipped_polygon)
    glutMainLoop()


if __name__ == "__main__":
    main()