import pygame
import OpenGL

from pygame.locals import * 
from OpenGL.GL import *   #typical OpenGl functions
from OpenGL.GLU import *   # fancy OpenGL functions

#Cube
#cube vertices
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
#cube edges
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

   (5,7) )

#Pyramid
#pyramid vertices
Pyramid_Vertices =( 

   (1, -1, 1), 

   (-1, -1, 1), 

   (0, -1, -1), 

   (1, 1, 0.5)
) 

#Pyramid_Edges: 
Pyramid_Edges =( 

   (0,1), 

   (0,2), 

   (0,3), 

   (2,1), 

   (2,3), 

   (3,1), 

) 

#Prism_Vertices: 
Prism_Vertices =( 

   (-1, -1, 1), 

   (1, -1, 1), 

   (0, 1, 1), 

   (-1, -1, -1), 

   (1, -1, -1), 

   (0, 1, -1)
) 

#Prism_Edges: 
Prism_Edges =( 

   (0,1), 

   (0,2), 

   (1,2), 

   (3,4), 

   (3,5), 

   (4,5), 

   (0,3), 

   (1,4), 

   (2,5)
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
    pygame.init() #initialising
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF| OPENGL|RESIZABLE) #doublebuf = double buffer
    #this notifies that there are two buffers to comply with monitor refresh rates
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    #the first value is the degree value of the field of view
    #2nd value is the aspect ratio - display width/display height
    # the next two values are the znear and zfar, which are the near and far clipping planes

    # a clipping plane is what distance does the object appear / disappear -both values are to be positive
    #in other words it makes sure we are not inside the model
    glTranslatef(0.0,0.0,-5) #glTranslatef multiplies the current matrix by a translation matrix
    # the parameters ar x,y and z

    currentModel = 0 # 0=cube 1=pyramid 2=prism

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:  #user presses space bar to cycle through the models
                    currentModel = (currentModel + 1) % 3 # cycle models
    
       
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT) #glClear is a clearing function,the constants specify exactly what we are clearing
        draw_model(models[currentModel][0], models[currentModel][1])

        pygame.display.flip() #updates the display
        pygame.time.wait(10) #short wait

main()

