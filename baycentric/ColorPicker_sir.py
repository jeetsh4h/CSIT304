# Color Picker Appliation

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

# Coordinates of the clicked point
clicked_point = False

# Define vertices of the color picker triangle
color_picker_vertices = np.array([
    [100.0, 100.0],
    [300.0, 400.0],
    [500.0, 200.0]
])

# Define colors at each vertex of the color picker triangle
color_picker_colors = np.array([
    [1.0, 0.0, 0.0],  # Red
    [0.0, 1.0, 0.0],  # Green
    [0.0, 0.0, 1.0]   # Blue
])

# Define vertices of the outline triangle
outline_vertices = np.array([
    [700.0, 100.0],
    [900.0, 400.0],
    [1100.0, 100.0]
])

# Initialize the selected color to white
selected_color = [1.0, 1.0, 1.0]

# Function to draw a triangle
def draw_triangle(vertices, colors=None, fill=False):
    # Implement the draw Triangle function

# Function to interpolate color based on barycentric coordinates
def interpolate_color(alpha, beta, gamma):
    global color_picker_colors
    # Calculate InterpolatedR, G, B
	
    return [R, G, B]

# Function to calculate barycentric coordinates
def barycentric_coordinates(x, y, vertices):
    A, B, C = vertices
    denominator = 
    alpha = / denominator
    beta =  / denominator
    gamma = 1 - alpha - beta
    return alpha, beta, gamma

# OpenGL display function
def display():
    global clicked_point
    global selected_color
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw the color picker triangle
    draw_triangle(color_picker_vertices, color_picker_colors, fill=True)

    # Draw the Target triangle
    # When no color picked draw outline triangle
    # When color picked draw the solid filled triangle
    
    glFlush()

# OpenGL initialization function
def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 1200.0, 0.0, 500.0)

# Mouse click event handler
def mouse_click(button, state, x, y):
    global selected_color
    global clicked_point
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # Calculate barycentric coordinates for the color picker triangle
        alpha, beta, gamma = barycentric_coordinates(x, 500 - y, color_picker_vertices)
        
	# Check whether the click is inside the Color Picker Triangle or Not
	# If yes then pickup the color by interpolating using the Barycentric coordinates
        # Else don't do anything

        glutPostRedisplay() # Recall Display Function

# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1200, 500)
    glutCreateWindow("Color Picker")
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()