import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Coordinates of the clicked point
clicked_point = None

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
    print(colors)
    if colors is not None:
        glBegin(GL_TRIANGLES)
        for i in range(3):
            if fill:
                glColor3f(*colors[i])
            else:
                glColor3f(0.0, 0.0, 0.0)
            glVertex2f(*vertices[i])
        glEnd()
    else:
        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glLineWidth(2.0)
        for i in range(3):
            glVertex2f(*vertices[i])
        glEnd()
# Function to interpolate color based on barycentric coordinates
def interpolate_color(alpha, beta, gamma):
    global color_picker_colors
    R = alpha * color_picker_colors[0][2] + beta * color_picker_colors[1][2] + gamma * color_picker_colors[2][2]
    G = alpha * color_picker_colors[0][0] + beta * color_picker_colors[1][0] + gamma * color_picker_colors[2][0]
    B = alpha * color_picker_colors[0][1] + beta * color_picker_colors[1][1] + gamma * color_picker_colors[2][1]
    return [R, G, B]

# Function to calculate barycentric coordinates
def barycentric_coordinates(x, y, vertices):
    A, B, C = vertices
    denominator = abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])) * 0.5
    alpha = abs(A[0] * (y - C[1]) + x * (C[1] - A[1]) + C[0] * (A[1] - y)) * 0.5 / denominator
    beta = abs(A[0] * (B[1] - y) + B[0] * (y - A[1]) + x * (A[1] - B[1])) * 0.5 / denominator
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
    if clicked_point:
        draw_triangle(outline_vertices)
    else:
        draw_triangle(outline_vertices, fill=True, colors=np.array([selected_color, selected_color, selected_color]))
    
    glFlush()

# OpenGL initialization function
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
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

        if alpha >= 0 and beta >= 0 and gamma >= 0:
            selected_color = interpolate_color(alpha, beta, gamma)
        else:
            clicked_point = None

        glutPostRedisplay() # Recall Display Function

# Main function
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    
    glutInitWindowSize(1200, 500)
    glutCreateWindow("Color Picker")
    init()
    
    glutDisplayFunc(display)
    glutMouseFunc(mouse_click)
    
    glutMainLoop()

if __name__ == "__main__":
    main()
