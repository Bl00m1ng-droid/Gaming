import pygame
import OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#CUBE
Cube_Vertices =( 

   (1, -1, -1), 

   (1, 1, -1), 

   (-1, 1, -1), 

   (-1, -1, -1), 

   (1, -1, 1), 

   (1, 1, 1), 

   (-1, -1, 1), 

   (-1, 1, 1) 

) 

Cube_Edges = ( 

   (0,1), 

   (0,3), 

   (0,4), 

   (2,1), 

   (2,3), 

   (2,7), 

   (6,3), 

   (6,4), 

   (6,7), 

   (5,1), 

   (5,4), 

   (5,7) 

) 

#PYRAMID
Pyramid_Vertices =( 

   (1, -1, 1), 

   (-1, -1, 1), 

   (0, -1, -1), 

   (1, 1, 0.5), 

) 

Pyramid_Edges =( 

   (0,1), 

   (0,2), 

   (0,3), 

   (2,1), 

   (2,3), 

   (3,1), 

) 

#PRISM
Prism_Vertices =( 

   (-1, -1, 1), 

   (1, -1, 1), 

   (0, 1, 1), 

   (-1, -1, -1), 

   (1, -1, -1), 

   (0, 1, -1), 

) 

Prism_Edges =( 

   (0,1), 

   (0,2), 

   (1,2), 

   (3,4), 

   (3,5), 

   (4,5), 

   (0,3), 

   (1,4), 

   (2,5), 

)

models = [ 
    (Cube_Vertices, Cube_Edges), 
    (Pyramid_Vertices, Pyramid_Edges), 
    (Prism_Vertices, Prism_Edges) 
] 

def draw_model(vertices, edges): 
    glBegin(GL_LINES) 
    for edge in edges: 
        for vertex in edge: 
            glVertex3fv(vertices[vertex]) 
    glEnd()

def main():
    pygame.init() 
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF| OPENGL|RESIZABLE)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5.0) 
    glEnable(GL_DEPTH_TEST)

    currentModel = 0 # 0=cube 1=pyramid 2=prism
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:  #user presses space bar to cycle through the models
                     # cycle models
                    currentModel += 1
                    if currentModel >= len(models):
                        currentModel = 0
                   
                #X-translation
                #positive direction right 
                if event.key == K_RIGHT:
                    glTranslatef(1,0,0)
                #negative direction left 
                if event.key == K_LEFT:
                    glTranslatef(-1,0,0)

                #Y-translation
                #positive direction up 
                if event.key == K_UP:
                    glTranslatef(0,1,0)
                #negative direction down
                if event.key == K_DOWN:
                    glTranslatef(0,-1,0)

                #Z-translation
                     #positive direction /zoom in z
                if event.key == K_z:
                        glTranslatef(0,0,1.0)
                     #negative direction /zoom out capslock
                if event.key == K_CAPSLOCK:
                        glTranslatef(0,0,-1.0)
                
    
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) 
        draw_model(models[currentModel][0], models[currentModel][1]) 

        pygame.display.flip() 
        pygame.time.wait(10) 

main()




