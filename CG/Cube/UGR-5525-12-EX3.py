import pygame as pg
from OpenGL.GL import *
import numpy as np
from OpenGL.GL.shaders import compileProgram, compileShader
import os


class Triangle:
    def __init__(self) -> None:
        self.position = [0.0, 0.0, 0.0]

        self.velocity = np.array([0.0, 0.0, 0.0], dtype=np.float32)
        self.acceleration = np.array([0.0, -0.001, 0.0], dtype=np.float32)

        self.vertices = [-0.5 + self.position[0], -0.5 + self.position[1], 0.0 + self.position[2], 1.0, 0.0, 0.0,
                         0.5 +
                         self.position[0], -0.5 + self.position[1], 0.0 +
                         self.position[2], 0.0, 1.0, 0.0,
                         0.0 + self.position[0], 0.5 + self.position[1], 0.0 + self.position[2], 0.0, 0.0, 1.0]

        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER,
                     self.vertices.nbytes,
                     self.vertices,
                     GL_STATIC_DRAW)

        glEnableVertexArrayAttrib(self.vao, 0)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))

        glEnableVertexArrayAttrib(self.vao, 1)

        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE,
                              24, ctypes.c_void_p(12))

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo, ))

    def draw(self):
        glBindVertexArray(self.vao)

        self.velocity += self.acceleration
        self.position += self.velocity

        if self.position[1] < -0.5:
            self.velocity[1] = - self.velocity[1]

        self.vertices = [-0.5 + self.position[0], -0.5 + self.position[1], 0.0 + self.position[2], 1.0, 0.0, 0.0,
                         0.5 +
                         self.position[0], -0.5 + self.position[1], 0.0 +
                         self.position[2], 0.0, 1.0, 0.0,
                         0.0 + self.position[0], 0.5 + self.position[1], 0.0 + self.position[2], 0.0, 0.0, 1.0]

        self.vertices = np.array(self.vertices, dtype=np.float32)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes,
                     self.vertices, GL_STATIC_DRAW)
        glDrawArrays(GL_TRIANGLES, 0, 3)


class APP:

    def __init__(self) -> None:
        pg.init()
        # select resoulution
        self.screen = pg.display.set_mode((640, 400), pg.OPENGL | pg.DOUBLEBUF)

        self.clock = pg.time.Clock()
        # color of window
        glClearColor(0.1, 0.2, 0.2, 1)

        vertex_path = os.path.join(
            os.path.dirname(__file__), "shader/vertex.txt")

        fragment_path = os.path.join(
            os.path.dirname(__file__), "shader/fragment.txt")

        self.shader = self.createShader(vertex_path, fragment_path)

        glUseProgram(self.shader)

        self.mainLoop()

    def mainLoop(self):
        running = True
        triangle = Triangle()
        while running:
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    running = False

            # clear the screen
            glClear(GL_COLOR_BUFFER_BIT)

            triangle.draw()

            pg.display.flip()

            self.clock.tick(60)

    def createShader(self, vertexFilePath, fragmentFilePath):
        print(vertexFilePath)
        with open(vertexFilePath, mode='r') as f:
            vertex_src = f.readlines()

        with open(fragmentFilePath, mode='r') as f:
            fragment_src = f.readlines()

        shader = compileProgram(compileShader(
            vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )

        return shader


if __name__ == "__main__":
    # Initialize window
    app = APP()
