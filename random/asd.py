import glfw
from OpenGL.GL import *
import numpy as np

def render():
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Create a new perspective projection matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = glfw.get_window_size(window)
    gluPerspective(45.0, width / float(height), 0.1, 100.0)

    # Set the viewport
    glViewport(0, 0, width, height)

    # Create a new model-view matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set the camera position and orientation
    glTranslatef(0.0, 0.0, -10.0)
    glRotatef(angle, 1.0, 1.0, 1.0)

    # Draw the cube
    draw_cube()

    # Swap the buffers
    glfw.swap_buffers(window)

def draw_cube():
    vertices = [
        #front face
        -1.0, -1.0,  1.0,
        1.0, -1.0,  1.0,
        1.0,  1.0,  1.0,
        -1.0,  1.0,  1.0,

        #back face
        -1.0, -1.0, -1.0,
        -1.0,  1.0, -1.0,
        1.0,  1.0, -1.0,
        1.0, -1.0, -1.0,
        #topp face
        -1.0,  1.0, -1.0,
        -1.0,  1.0,  1.0,
        1.0,  1.0,  1.0,
        1.0,  1.0, -1.0,

        #bottom face
        -1.0, -1.0, -1.0,
        1.0, -1.0, -1.0,
        1.0, -1.0,  1.0,
        -1.0, -1.0,  1.0,

        #right face
        1.0, -1.0 , -1.0,
        1.0, 1.0, -1.0,
        1.0, 1.0, 1.0,
        1.0, -1.0, 1.0,

        #lft face
        -1.0, -1.0, -1.0,
        -1.0, -1.0,  1.0,
        -1.0,  1.0,  1.0,
        -1.0,  1.0, -1.0,
    ]

    # Define the edges connecting the vertices
    edges = [
        # Front face
        0, 1,
        1, 2,
        2, 3,
        3, 0,

        # Back face
        4, 5,
        5, 6,
        6, 7,
        7, 4,

        # Top face
        8, 9,
        9, 10,
        10, 11,
        11, 8,

        # Bottom face
        12, 13,
        13, 14,
        14, 15,
        15, 12,

        # Right face
        16, 17,
        17, 18,
        18, 19,
        19, 16,

        # Left face
        20, 21,
        21, 22,
        22, 23,
        23, 20
    ]
    # Convert the vertices and edges to NumPy arrays for faster rendering
    vertices = np.array(vertices, dtype=np.float32)
    edges = np.array(edges, dtype=np.uint32)

    # Draw the edges of the cube
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glDrawElements(GL_LINES, len(edges), GL_UNSIGNED_INT, edges)
    glDisableClientState(GL_VERTEX_ARRAY)


render()