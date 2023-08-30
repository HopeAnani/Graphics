import pygame as pg #provide us window for us to draw using opengl
from OpenGL.GL import * #draw



class APP:
    
    def __init__(self) -> None: #constructor
        pg.init()
        pg.display.set_mode((640,400), pg.OPENGL | pg.DOUBLEBUF) #set_mode - tell the pygame to set the resoulution
                                                                 #DOUBLEBUF = buffer to store our content
        self.clock = pg.time.Clock()
        glClearColor(0.1, 0.2, 0.2, 1) #set rgb
        self.mainLoop() #initiate main loop


    def mainLoop(self):
        running = True
        while running:
            for event in pg.event.get(): #brings events that are in pygame
                if(event.type == pg.QUIT):
                    running = False

            glClear(GL_COLOR_BUFFER_BIT) #clear the screen
            pg.display.flip() #display content   
            self.clock.tick(60) #60 FPS as long as there is enough source


if __name__ == "__main__":
    #Initialize window
    app = APP()
   