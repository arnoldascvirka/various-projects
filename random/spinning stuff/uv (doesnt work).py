#---------------------------------------------------libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront

#---------------------------------------------------initialize
pygame.init()
display = (1280, 720)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

#---------------------------------------------------scene and textures
scene = pywavefront.Wavefront('rat_licht.obj', collect_faces=True)
image = pygame.image.load('texture.png')
image_data = pygame.image.tostring(image, 'RGB', 1)
texture_id = glGenTextures(1)

#---------------------------------------------------set up parameters
glBindTexture(GL_TEXTURE_2D, texture_id)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.get_width(), image.get_height(), 0, GL_RGB, GL_UNSIGNED_BYTE, image_data)


#---------------------------------------------------opengl setup
gluPerspective(45, (display[0] / display[1]), 1, 500.0)
glTranslatef(0.0, 0.0, -40)
glRotatef(0, 0, 0, 0)
# glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

#---------------------------------------------------start loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                glTranslatef(-0.5,0,0)
            if event.key == pygame.K_RIGHT: 
                glTranslatef(0.5,0,0)
            if event.key == pygame.K_UP:
                glTranslatef(0,1,0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0,-1,0)

        # Clear the color and depth buffers
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        # Rotate the object
        glRotatef(1, 5, 1, 1)

        # Bind the texture to the object
        glBindTexture(GL_TEXTURE_2D, texture_id)

        # Enable texture mapping
        glEnable(GL_TEXTURE_2D)

        # Render the mesh list
        for mesh in scene.mesh_list:
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                for vertex_index in face:
                    # Get the texture coordinates for this vertex
                    u, v = scene.uv[vertex_index]

                    # Specify the texture coordinates for this vertex
                    glTexCoord2f(u, v)

                    # Render the vertex
                    glVertex3f(*scene.vertices[vertex_index])
            glEnd()

        # Update the display
        pygame.display.flip()
        pygame.time.wait(10)

# Run the main function
main()