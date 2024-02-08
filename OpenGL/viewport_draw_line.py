from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

viewport_coordinates = (-300, 200, 100, 600)
line_start = (0.0, 0.0)
line_end = (0.0, 0.0)

def encode_point(x, y):
    global viewport_coordinates
    xmin, xmax, ymin, ymax = viewport_coordinates

    code = 0                                # 0 is 0000
    if x < xmin:
        # set last bit to 1
        code |= 1                           # 1 is 0001
    
    elif x > xmax:
        # set second last bit to 1
        code |= 2                           # 2 is 0010

    if y < ymin:
        # set second bit to 1
        code |= 4                           # 4 is 0100
    
    elif y > ymax:
        # set first bit to 1
        code |= 8                           # 8 is 1000
    
    return code


def kohen_sutherland(point_a, point_b):
    x1, y1 = point_a
    x2, y2 = point_b

    code_a = encode_point(x1, y1)
    code_b = encode_point(x2, y2)

    while True:
        if code_a == 0 and code_b == 0:
            # trivially accepted
            return point_a, point_b

        if code_a & code_b != 0:
            # trivially rejected
            return None, None

        code_out = code_a if code_a else code_b

        if code_out & 1:  # left
            x = viewport_coordinates[0]
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        
        elif code_out & 2:  # right
            x = viewport_coordinates[1]
            y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
        
        elif code_out & 4:  # bottom
            y = viewport_coordinates[2]
            x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
        
        elif code_out & 8:  # top
            y = viewport_coordinates[3]
            x = x1 + (x2 - x1) * (y - y1) / (y2 - y1)

        if code_out == code_a:
            point_a = (x, y)
            code_a = encode_point(x, y)
        else:
            point_b = (x, y)
            code_b = encode_point(x, y)

def viewport():
    global line_start, line_end
    clip_line_start, clip_line_end = kohen_sutherland(line_start, line_end)

    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

    glLineWidth(5.0)  # Set line width to 5 pixels
    glBegin(GL_LINES)

    if clip_line_start is None or clip_line_end is None:
        print("Line is completely outside the viewport")
    
    else:
        print(f"Point A: {clip_line_start}, Point B: {clip_line_end}")

        glColor3f(0.0, 0.0, 0.0)    # Set color to black
        
        glVertex2f(*clip_line_start)   # Starting point of the line
        glVertex2f(*clip_line_end)     # Ending point of the line

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


    global line_start, line_end
    line_start = (-300, 100)
    line_end = (100, 700)

    glutDisplayFunc(viewport)

    glutMainLoop()


if __name__ == "__main__":
    main()