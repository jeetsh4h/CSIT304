from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def draw_point():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer
    
    glPointSize(10.0)  # Set point size to 10 pixels
    
    glBegin(GL_POINTS)
    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    glVertex2f(0.0, 0.0)  # Coordinates of the point

    glColor3f(1.0, 1.0, 0.0)  # Set color to yellow
    glVertex2f(10.0, -10.0)  # Coordinates of the point
    glEnd()

    glFlush()  # Flush the OpenGL pipeline to display the point

def draw_line():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

    glLineWidth(5.0)  # Set line width to 5 pixels

    glBegin(GL_LINES)
    glColor3f(0.0, 1.0, 0.0)  # Set color to green
    glVertex2f(-50.0, -50.0)  # Starting point of the line
    glVertex2f(50.0, 50.0)    # Ending point of the line

    glColor3f(0.0, 1.0, 1.0)   # Set color to cyan
    glVertex2f(50.0, 50.0)     # Starting point of the line
    glVertex2f(50.0, -50.0)    # Ending point of the line
    
    glColor3f(1.0, 0.0, 1.0)   # Set color to magenta
    glVertex2f(50.0, -50.0)     # Starting point of the line
    glVertex2f(-50.0, 50.0)    # Ending point of the line
    glEnd()

    glFlush()  # Flush the OpenGL pipeline to display the line

def draw_triangle():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

    glLineWidth(5.0)  # Set line width to 5 pixels
    glColor3f(0.0, 0.0, 1.0)  # Set color to blue

    glBegin(GL_TRIANGLES)
    glVertex2f(-50.0, -50.0)  # Vertex 1
    glVertex2f(50.0, -50.0)   # Vertex 2
    glVertex2f(0.0, 50.0)     # Vertex 3
    glEnd()

    glFlush()  # Flush the OpenGL pipeline to display the transformed triangle


def draw_transformed_triangle(sx=2, sy=3, t=(100, 100)):
    x1, y1 = (-50.0, -50.0)
    x2, y2 = (50.0, -50.0)
    x3, y3 = (0.0, 0.0)

    # transformation matrix calculation
    tx, ty = t
    
    translate = np.array([[1, 0, -tx],[0, 1, -ty],[0, 0, 1]])
    scale = np.array([[sx, 0, 0],[0, sy, 0],[0, 0, 1]])
    translate_back = np.array([[1, 0, tx],[0, 1, ty],[0, 0, 1]])
    
    transform = translate @ scale @ translate_back

    # applying transformation matrix
    p1 = np.array([x1, y1, 1])
    p2 = np.array([x2, y2, 1])
    p3 = np.array([x3, y3, 1])

    p1_t = transform @ p1; x1_t, y1_t = p1_t[:2]
    p2_t = transform @ p2; x2_t, y2_t = p2_t[:2]
    p3_t = transform @ p3; x3_t, y3_t = p3_t[:2]

    # drawing triangles
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the color buffer

    glLineWidth(5.0)  # Set line width to 5 pixels
    glPointSize(10.0)  # Set point size to 10 pixels

    glBegin(GL_TRIANGLES)
    # original triangle
    glColor3f(0.0, 0.0, 1.0)  # Set color to blue
    glVertex2f(x1, y1)   # Vertex 1
    glVertex2f(x2, y2)   # Vertex 2
    glVertex2f(x3, y3)   # Vertex 3
    
    # transformed matrix
    glColor3f(1.0, 0.0, 0.0)  # Set color to red
    glVertex2f(x1_t, y1_t)   # Vertex 1
    glVertex2f(x2_t, y2_t)   # Vertex 2
    glVertex2f(x3_t, y3_t)   # Vertex 3
    glEnd()

    glBegin(GL_POINTS)
    glColor3f(0.0, 1.0, 0.0)  # Set color to green
    glVertex2f(0.0, 0.0)
    glEnd()

    glFlush()  # Flush the OpenGL pipeline to display the transformed triangle


def initialize():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white

    # gluOrtho2D(-250, 250, -250, 250)  # Set the orthographic projection
    gluOrtho2D(-100, 400, -100, 400)  # Set the orthographic projection

def main():
    glutInit(sys.argv)  # Initialize GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Set display mode

    glutInitWindowSize(500, 500)  # Set window size
    glutInitWindowPosition(100, 100)  # Set window position

    glutCreateWindow("OpenGL Drawing")  # Create the window with the given title

    initialize()  # Call the initialization function

    # glutDisplayFunc(draw_point)  # Register the display function
    # glutDisplayFunc(draw_line)  # Register the display function
    # glutDisplayFunc(draw_triangle)  # Register the display function
    glutDisplayFunc(draw_transformed_triangle)  # Register the display function


    glutMainLoop()  # Enter the GLUT main event loop

if __name__ == "__main__":
    main()