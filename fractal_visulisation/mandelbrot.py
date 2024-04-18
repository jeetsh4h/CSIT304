import time
import colorsys
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window_width = None
window_height = None

ortho_proj = (-1.0, 1.0, -1.0, 1.0)
MOUSE_DOWN = False
MOUSE_DOWN_COORDS = (None, None)

MAX_ITER = 100


def mandlebrot(x, y):
    ortho_x = ortho_proj[0] + x / window_width * (ortho_proj[1] - ortho_proj[0])
    ortho_y = ortho_proj[2] + (window_height - y) / window_height * (ortho_proj[3] - ortho_proj[2])
    
    c = complex(ortho_x, ortho_y)
    z = complex(0, 0)
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1

    if n == MAX_ITER:
        return MAX_ITER
    
    # for smoother colors
    return n + 1 - np.log(np.log2(abs(z)))


def display():
    if MOUSE_DOWN:
        pass

    glClear(GL_COLOR_BUFFER_BIT)

    # Get the window width and height
    global window_width, window_height
    window_width = glutGet(GLUT_WINDOW_WIDTH)
    window_height = glutGet(GLUT_WINDOW_HEIGHT)

    # start_time = time.time()
    # # Calculate the color of each pixel
    # pixels = np.zeros((window_height, window_width, 3), dtype=np.uint8)

    # for y in range(window_height):
    #     for x in range(window_width):
    #         m_c = mandlebrot(x, y)
    #         pixels[y, x] = [255, 255, 255] if m_c == MAX_ITER else [0, 0, 0]

    #         # The color depends on the number of iterations
    #         hue = int(255 * m_c / MAX_ITER)
    #         saturation = 255
    #         value = 255 if m_c < MAX_ITER else 0

    #         rgb = colorsys.hsv_to_rgb(hue / 255, saturation / 255, value / 255)
    #         pixels[y, x] = [int(255 * c) for c in rgb]
    
    # print("Time taken: ", time.time() - start_time)

    start_time = time.time()
## Trying to vectorize the calculations
    pixels = np.zeros((window_height, window_width, 3), dtype=np.uint8)

    y = np.arange(0, window_height)
    x = np.arange(0, window_width)
    
    xv, yv = np.meshgrid(x, y)
    
    mandlebrot_vec = np.vectorize(mandlebrot)
    mandelbrot_val = mandlebrot_vec(xv, yv)

    hue = (255 * mandelbrot_val / MAX_ITER).astype(np.uint8)
    saturation = 255
    value = 255 * (mandelbrot_val < MAX_ITER).astype(np.uint8)

    for i in range(3):
        pixels[:, :, i] = (255 * np.vectorize(colorsys.hsv_to_rgb)(hue / 255, saturation / 255, value / 255)[i]).astype(np.uint8)

    print("Time taken: ", time.time() - start_time)

    # Render the pixels on the screen
    glDrawPixels(window_width, window_height, GL_RGB, GL_UNSIGNED_BYTE, pixels)

    # Swap the buffers to display the rendered image
    glutSwapBuffers()



def zoom(button, state, x, y):    
    global MOUSE_DOWN, MOUSE_DOWN_COORDS, ortho_proj, window_height, window_width
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if not MOUSE_DOWN:
            MOUSE_DOWN = True
            MOUSE_DOWN_COORDS = (x, y)
    
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        if MOUSE_DOWN:
            MOUSE_DOWN = False

            scale_factor = (MOUSE_DOWN_COORDS[1] - y) / 15
            scale_factor = 1.05 if 0 < scale_factor < 1 else scale_factor
            scale_factor = -1.05 if -1 < scale_factor < 0 else scale_factor
            
            if scale_factor < 0:
                print("Zooming in by a factor of:", abs(scale_factor))
                scale_factor = 1 / abs(scale_factor)
            else:
                print("Zooming out by a factor of:", scale_factor)

            mouse_down_ortho = (
                ortho_proj[0] + MOUSE_DOWN_COORDS[0] / window_width * (ortho_proj[1] - ortho_proj[0]),
                ortho_proj[2] + (window_height - MOUSE_DOWN_COORDS[1]) / window_height * (ortho_proj[3] - ortho_proj[2])
            )

            ortho_proj = (
                ((ortho_proj[0] - (mouse_down_ortho[0] / 2)) * scale_factor) + (mouse_down_ortho[0] / 2),
                ((ortho_proj[1] - (mouse_down_ortho[0] / 2)) * scale_factor) + (mouse_down_ortho[0] / 2),
                ((ortho_proj[2] - (mouse_down_ortho[1] / 2)) * scale_factor) + (mouse_down_ortho[1] / 2),
                ((ortho_proj[3] - (mouse_down_ortho[1] / 2)) * scale_factor) + (mouse_down_ortho[1] / 2)
            )


            print(ortho_proj)
            gluOrtho2D(*ortho_proj)
            
            glutPostRedisplay()


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(*ortho_proj)
    glClear(GL_COLOR_BUFFER_BIT)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    glutInitWindowSize(600, 600)
    glutInitWindowPosition(900, 0)

    glutCreateWindow(b"Mandelbrot Set")
    init()

    glutMouseFunc(zoom)
    glutDisplayFunc(display)

    glutMainLoop()


if __name__ == "__main__":
    main()