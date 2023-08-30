import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class OBJ:
    def __init__(self, filename):
        self.vertices = []
        self.normals = []
        self.faces = []
        self.load(filename)

    def load(self, filename):
        with open(filename, "r") as file:
            for line in file:
                if line.startswith("#"):
                    continue
                values = line.split()

                if not values:
                    continue

                if values[0] == "v":
                    self.vertices.append(list(map(float, values[1:4])))
                elif values[0] == "vn":
                    self.normals.append(list(map(float, values[1:4])))
                elif values[0] == "f":
                    face = []
                    for face_str in values[1:]:
                        vertex_data = face_str.split('/')
                        vertex_index = int(vertex_data[0]) - 1
                        if vertex_index >= 0 and vertex_index < len(self.vertices):
                            face.append(vertex_index)
      
                    if len(face) >= 3:
                        self.faces.append(face)

    def render(self):
        for face in self.faces:
            if all (vertex_id < len(self.vertices) for vertex_id in face):
                glBegin(GL_POLYGON)
                for vertex_id in face:
                    vertex = self.vertices[vertex_id]
                    if vertex_id < len(self.normals):
                        normal = self.normals[vertex_id]
                        glNormal3fv(normal)
                    glVertex3fv(vertex)
                glEnd()

pygame.init()
width, height = 800, 600
pygame.display.set_mode((width,height), DOUBLEBUF | OPENGL)

# model = OBJ ("model.obj")

model = OBJ ("C:/Users\Hope\Desktop\CG\Model\model.obj")

glClearColor(0.8, 0.8, 0.8, 1.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)

glLightfv(GL_LIGHT0, GL_POSITION, (0.5, 1.0, 1.0, 0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 0.0, 0.0, 1.0))
glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 0.0, 0.0, 1.0))

# set up material properties

glMaterialfv(GL_FRONT, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glMaterialfv(GL_FRONT, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
glMaterialfv(GL_FRONT, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))
glMaterialfv(GL_FRONT, GL_SHININESS, 32.0) #set the shine

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslate(0.0, 0.0, -5)

rotation_x = 0
rotation_y = 0

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rotation_y += 1
    if keys[pygame.K_RIGHT]:
        rotation_y -= 1
    if keys[pygame.K_UP]:
        rotation_x += 1
    if keys[pygame.K_DOWN]:
        rotation_x -= 1


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(rotation_x, 1, 0, 0)
    glRotatef(rotation_y, 0, 1, 0)
    model.render()

    pygame.display.flip()
    pygame.time.wait(5)
