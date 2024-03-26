from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import time



def render_mandlebrot_set():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # bg color white

    start_time = time.time()

    ### rendering the mandelbrot set ###

    end_time = time.time()

    print(f"Frame Time: {(end_time - start_time) / 1000} ms")