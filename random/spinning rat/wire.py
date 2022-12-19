#---------------------------------------------------libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront

#---------------------------------------------------scene
#---------------------------------------------------replace '' with your obj
scene = pywavefront.Wavefront('.obj', collect_faces=True) 


#---------------------------------------------------initialize
pygame.init()
display = (1280,720)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0] / display[1]), 1, 500.0)
glTranslatef(0.0, 0.0, -40)
glRotatef(0, 0, 0, 0)
glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) #---------replace LINE with FILL to remove wireframe

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

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 5, 1, 1)

        for mesh in scene.mesh_list:
                glBegin(GL_TRIANGLES)
                for face in mesh.faces:
                    for vertex_i in face:
                        glVertex3f(*scene.vertices[vertex_i])
        glEnd()
        pygame.display.flip()
        pygame.time.wait(10)
main()