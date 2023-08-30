# import pygame as pg  #provide us window for us to draw using opengl
# from OpenGL.GL import * #draw - give as access to communicate with our graphics card
# import numpy as np
# import ctypes 
# from OpenGL.GL.shaders import compileProgram, compileShader #compile shaders
# import os 

# #Shader -> render model

# #triangle 
# class Triangle:
#     def __init__(self):
#         self.vertices = (
#             #points = x, y, z, r, g, b
#             -0.5, -0.5, 0.0,  1.0, 0.0, 0.0,
#             0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
#             0.0, 0.5, 0.0, 0.0, 0.0, 1.0

#             # -0.5, -1, 0.0, 1.0, 0.0, 0.0,
#             # 0.5, -1, 0.0, 0.0, 1.0, 0.0,
#             # 0.0, 0.5, 0.0, 0.0, 0.0, 1.0

#         )

#         #convert to numpy array
#         self.vertices = np.array(self.vertices, dtype=np.float32)

#         #vertex array object
#         #vertex buffer object
#         self.vao = glGenVertexArrays(1)
#         glBindVertexArray(self.vao)

#         self.vbo = glGenBuffers(1)
#         glBindBuffer(GL_ARRAY_BUFFER, self.vao)
        
#         #pass it to openGL as gl Buffer 
#         glBufferData(
#                     GL_ARRAY_BUFFER, 
#                      self.vertices.nbytes,
#                      self.vertices,
#                      GL_STATIC_DRAW
#                      )
        
#         #distinguish data (differentiate pos and color data)
#         glEnableVertexArrayAttrib(self.vao ,0)
        
#         #pos data
#         glVertexAttribPointer(
#                             0, 3, 
#                               GL_FLOAT, 
#                               GL_FALSE, 24, 
#                               ctypes.c_void_p(0)
#                               )
        
#         #color data
#         glEnableVertexArrayAttrib(self.vao, 1)

#         glVertexAttribPointer(
#                             1, 3, 
#                               GL_FLOAT, 
#                               GL_FALSE, 24, 
#                               ctypes.c_void_p(12)
#                               )

#     def draw(self):

#         #draw the triangle
#         glBindVertexArray(self.vao)
#         glDrawArrays(GL_TRIANGLES, 0, 3)
        
        

#     def destroy(self):
#         glDeleteVertexArrays(1, (self.vao, ))
#         glDeleteBuffers(1, (self.vbo, ))


# class APP:

#     def __init__(self) -> None:
        
#         #initialize pygame
#         pg.init()

#         #tell the pygame to set the resolution and tell it what the contents are in the window (which is opengl)
#         #DOUBLEBUF = buffer to store our content drawn in window
#         self.screen = pg.display.set_mode((640, 800), pg.OPENGL | pg.DOUBLEBUF)

#         #set clock for the pygame to process as the performance of our GPU
#         self.clock = pg.time.Clock()

#         #set rgb background
#         glClearColor(0.1, 0.1, 0.1, 1)


#         #get the file name of the shaders
#         vertex_path = os.path.join(os.path.dirname(__file__), "shader/vertex.txt")
#         fragment_path = os.path.join(os.path.dirname(__file__), "shader/fragment.txt")



#         self.shader = self.createShader(vertex_path, fragment_path)

#         #use the shader program
#         glUseProgram(self.shader)


#         self.triangle = Triangle()

        
#         #initiate main Loop
#         self.mainLoop()

#     def mainLoop(self):

#         running = True
#         while running:
#             #check event type from list of events in pygame 
#             for event in pg.event.get():
#                 #if event type is quit then break the loop
#                 if event.type == pg.QUIT:
#                     running = False
            
#             #clear the screen
#             glClear(GL_COLOR_BUFFER_BIT)

#             #
#             self.triangle.draw()

#             #display content
#             pg.display.flip()
            
#             #60 FPS as long there is enough resources
#             self.clock.tick(60)

#     def createShader(self, vertexFilePath, fragmentFilePath):
#         #read the txt files (shaders)
#         with open(vertexFilePath, 'r') as f:
#             vertex_src = f.readlines()

#         with open(fragmentFilePath, 'r') as f:
#             fragment_src = f.readlines() 
        
#         shader = compileProgram(
#             compileShader(vertex_src, GL_VERTEX_SHADER),
#             compileShader(fragment_src, GL_FRAGMENT_SHADER)
#         )

#         return shader

# if __name__ == '__main__':
#     #intialize window
#     app = APP() 







import pygame as pg  #provide us window for us to draw using opengl
from OpenGL.GL import * #draw - give as access to communicate with our graphics card
import numpy as np
import ctypes 
from OpenGL.GL.shaders import compileProgram, compileShader #compile shaders
import os 

#Shader -> render model

#triangle 
class Triangle:
    
    # vertices = (
    #     #points = x, y, z, r, g, b
    #     -0.5, -0.5, 0.0,  1.0, 0.0, 0.0,
    #     0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
    #     0.0, 0.5, 0.0, 0.0, 0.0, 1.0

    #     # -0.5, -1, 0.0, 1.0, 0.0, 0.0,
    #     # 0.5, -1, 0.0, 0.0, 1.0, 0.0,
    #     # 0.0, 0.5, 0.0, 0.0, 0.0, 1.0

    # )
            
    def __init__(self, vertices):
        
        self.vertices = vertices
        
        #convert to numpy array
        self.vertices = np.array(self.vertices, dtype=np.float32)

        #vertex array object
        #vertex buffer object
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vao)
        
        #pass it to openGL as gl Buffer 
        glBufferData(
                    GL_ARRAY_BUFFER, 
                     self.vertices.nbytes,
                     self.vertices,
                     GL_STATIC_DRAW
                     )
        
        #distinguish data (differentiate pos and color data)
        glEnableVertexArrayAttrib(self.vao ,0)
        
        #pos data
        glVertexAttribPointer(
                            0, 3, 
                              GL_FLOAT, 
                              GL_FALSE, 24, 
                              ctypes.c_void_p(0)
                              )
        
        #color data
        glEnableVertexArrayAttrib(self.vao, 1)

        glVertexAttribPointer(
                            1, 3, 
                              GL_FLOAT, 
                              GL_FALSE, 24, 
                              ctypes.c_void_p(12)
                              )

    def draw(self):
        
        '''This method draws the triangle and move it to the left'''

        #define the amount of change of the vertices
        change = 0.008
        
        #if the triangle is out of bound restart it  
        if self.vertices[0] <= -1:
            change = -1

        #change the value vertices to move the traingle
        updated_vertices = list(self.vertices)
        updated_vertices[0] -= change
        updated_vertices[6] -= change
        updated_vertices[12] -= change

        #change it to tuple
        vertices = tuple(updated_vertices)

        #call the constructor to reinitiaize the whole triangle
        self.__init__(vertices) 

        #draw the triangle
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        
        

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao, ))
        glDeleteBuffers(1, (self.vbo, ))


class APP:

    def __init__(self) -> None:
        
        #initialize pygame
        pg.init()

        #tell the pygame to set the resolution and tell it what the contents are in the window (which is opengl)
        #DOUBLEBUF = buffer to store our content drawn in window
        self.screen = pg.display.set_mode((640, 800), pg.OPENGL | pg.DOUBLEBUF)

        #set clock for the pygame to process as the performance of our GPU
        self.clock = pg.time.Clock()

        #set rgb background
        glClearColor(0.1, 0.1, 0.1, 1)


        #get the file name of the shaders
        vertex_path = os.path.join(os.path.dirname(__file__), "shader/vertex.txt")
        fragment_path = os.path.join(os.path.dirname(__file__), "shader/fragment.txt")

        #call the shader method
        self.shader = self.createShader(vertex_path, fragment_path)

        #use the shader program
        glUseProgram(self.shader)


        self.triangle = Triangle(vertices=(
        #points = x, y, z, r, g, b
        -0.5, -0.5, 0.0,  1.0, 0.0, 0.0,
        0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
        0.0, 0.5, 0.0, 0.0, 0.0, 1.0))

        
        #initiate main Loop
        self.mainLoop()

    def mainLoop(self):

        running = True
        while running:
            #check event type from list of events in pygame 
            for event in pg.event.get():
                #if event type is quit then break the loop
                if event.type == pg.QUIT:
                    running = False
            
            #clear the screen
            glClear(GL_COLOR_BUFFER_BIT)

            #draw the traingle
            self.triangle.draw()

            #display content
            pg.display.flip()
            
            #60 FPS as long there is enough resources
            self.clock.tick(60)

    def createShader(self, vertexFilePath, fragmentFilePath):
        #read the txt files (shaders)
        with open(vertexFilePath, 'r') as f:
            vertex_src = f.readlines()

        with open(fragmentFilePath, 'r') as f:
            fragment_src = f.readlines() 
        
        shader = compileProgram(
            compileShader(vertex_src, GL_VERTEX_SHADER),
            compileShader(fragment_src, GL_FRAGMENT_SHADER)
        )

        return shader

if __name__ == '__main__':
    #intialize window
    app = APP() 