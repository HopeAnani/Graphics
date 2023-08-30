import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#define the vertices of the cube
vertices = [
    (-1, -1, 1), #front bottom left (0)
    (1, -1, 1), #front bottom right (1)
    (1, 1, 1), #front top right (2)
    (-1, 1, 1), #front top left (3)

    (-1, -1, -1), #back bottom left  (4)
    (1, -1, -1), #back bottom right (5)
    (1, 1, -1), #back top right (6)
    (-1, 1, -1), #back top left (7)
]

faces = [
    (0, 1, 2, 3), #front face
    (3, 2, 6, 7), #Top face
    (7, 6, 5, 4), #Back face
    (4, 5, 1, 0), #Bottom face
    (1, 5, 6, 2), #Right face
    (4, 0, 3, 7), #Left face
]

colors = [
    (1, 0, 0), #Red front face
    (0, 1, 0), #Green top face
    (0, 0, 1), #blue back face
    (1, 1, 0), #yellow bottom face
    (1, 0, 1), #magenta right face
    (0, 1, 1), #Cyan left face
]

def draw_cube():

    glBegin(GL_QUADS)
    for  i, face in enumerate(faces):
        glColor4f(*colors[i], 0.5)
        for vertex in face:
            glVertex3fv(vertices[vertex])

    glEnd()





def main():
    pygame.init()
    display = (640, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    #3D
    gluPerspective (45, (display[0]/display[1]), 0.1, 50)
    glTranslate(0.0, 0.0, -5.0) #moving the camera around


    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        glRotate(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()