import pygame as pg #provide us window for us to draw using opengl
from OpenGL.GL import * #draw
import numpy as np
import ctypes

from OpenGL.GL.shaders import compileProgram, compileShader
import os


#Shader -> render model 

class Triangle:
    def __init__(self,vertices):

        #     
        #     (-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
        #     0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
        #     0.0, 0.5, 0.0, 0.0, 0.0, 1.0)
              
        # ]
        
        #opengl gives access to our graphics card

        vertices = np.array(vertices, dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo) 

        glBufferData(GL_ARRAY_BUFFER, 
                     vertices.nbytes,
                     vertices,
                     GL_STATIC_DRAW 
                     )
        
        #postion data
        glEnableVertexArrayAttrib(self.vao,0)

        glVertexAttribPointer(0, 3, 
                              GL_FLOAT, GL_FALSE, 24, 
                              ctypes.c_void_p(0)
                              )
        
        #color data
        glEnableVertexArrayAttrib(self.vao,1)

        glVertexAttribPointer(1, 3, 
                              GL_FLOAT, GL_FALSE, 24, 
                              ctypes.c_void_p(12)
                              )

    def draw(self):
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES,0, 3)

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo, ))


class APP:
    
    def __init__(self) -> None: #constructor
        pg.init()
        pg.display.set_mode((640,400), pg.OPENGL | pg.DOUBLEBUF) #set_mode - tell the pygame to set the resoulution
                                                                 #DOUBLEBUF = buffer to store our content
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1) #set rgb

        vertex_path = os.path.join(os.path.dirname(__file__),"shader/vertex.txt")

        fragment_path = os.path.join(os.path.dirname(__file__),"shader/fragment.txt")

        self.shader = self.createShader(vertex_path, fragment_path)

        glUseProgram(self.shader)
        self.vertices = [
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            0.0, 0.5, 0.0, 0.0, 0.0, 1.0]
        #(-0.1, -0.1, 0.0, 1.0, 0.0, 0.0,
        #     0.1, -0.1, 0.0, 0.0, 1.0, 0.0,
        #     0.0, 0.1, 0.0, 0.0, 0.0, 1.0),

        # self.triangle = Triangle()
        self.mainLoop() #initiate main loop


    def mainLoop(self):
        running = True
        change = 0.01
        change2 = 0.01
        while running:
            if self.vertices[0] >= -0.1:
                change = -0.01
            if self.vertices[0] <= -0.5:
                change = 0.01

            if self.vertices[6] <= 0.1:
                change2 = 0.01
            if self.vertices[6] >= 0.5:
                change2 = -0.01
            
            self.triangle = Triangle(self.vertices)
            for event in pg.event.get(): #brings events that are in pygame
                if(event.type == pg.QUIT):
                    running = False

            glClear(GL_COLOR_BUFFER_BIT) #clear the screen

            self.triangle.draw()

            pg.display.flip() #display content   
            self.clock.tick(60) #60 FPS as long as there is enough source
            self.vertices[0] += change
            self.vertices[1] += change
            self.vertices[7] += change
            self.vertices[6] += change2
            self.vertices[13] += change2
            

    def createShader(self, verteFilePath, fragmentFilePath):
        with open(verteFilePath, mode='r') as f:
            vertex_src = f.readlines()

        with open(fragmentFilePath, mode='r') as f:
            fragment_src = f.readlines()
        
        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )

        return shader

if __name__ == "__main__":
    #Initialize window
    app = APP()
   

