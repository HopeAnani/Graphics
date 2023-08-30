from cmath import inf
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from OpenGL.GLUT import *

MAX_PARTICLES = 1000
PARTICLE_SIZE = 0.2
WIND_FORCE = (0.01, 0, 0)


class Particle: 
    def __init__(self, pos, vel, color):
        self.pos = pos
        self.vel = vel
        self.color = color

    def draw(self):
        glPushMatrix()
        glColor3f(*self.color)
        glTranslatef(*self.pos)
        quad = gluNewQuadric()
        gluSphere(quad, PARTICLE_SIZE, 10, 10)
        gluDeleteQuadric(quad)
        glPopMatrix()

    def update(self):
        self.vel = tuple(sum(x) for x in zip(self.vel, WIND_FORCE))
        self.pos = tuple(sum(x) for x in zip(self.pos, self.vel))


class ParticleSystem: 
    def __init__(self):
        self.particles = []

    def add_particles(self, particle):
        if len(self.particles) < MAX_PARTICLES:
            self.particles.append(particle)
    
    def update(self):
        for particle in self.particles:
            particle.update()

    def draw(self):
        for particle in self.particles:
            particle.draw()


def main():
    pygame.init()
    display = (640, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslate(0.0, 0.0, -10.0)

    clock = pygame.time.Clock()

    particle_system = ParticleSystem()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pos = (0, 0, 0)
        vel = (random.uniform(0.2, 0.3),
               random.uniform(-0.1, 0.1),
               random.uniform(-0.1, 0.1)
               )
        Color = (random.uniform(0.0, 1.0),
                 random.uniform(0.0, 1.0),
                 random.uniform(0.0, 1.0)
                 )
        
        particle_system.add_particles(Particle(pos, vel, Color))

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        particle_system.update()
        particle_system.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()