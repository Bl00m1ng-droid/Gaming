import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# CUBE
Cube_Vertices = (
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
    (0,1),(0,3),(0,4),
    (2,1),(2,3),(2,7),
    (6,3),(6,4),(6,7),
    (5,1),(5,4),(5,7)
)
Cube_Faces = (
    (0,1,2,3),
    (4,5,7,6),
    (0,4,5,1),
    (3,2,7,6),
    (1,5,7,2),
    (0,3,6,4)
)
Cube_Colours = (
    (1,0,0),(0,1,0),(0,0,1),
    (1,1,0),(0,1,1),(1,0,1)
)
#-----------------------------------------
# PYRAMID (triangular base)
Pyramid_Vertices = (
    (1, -1, 1),
    (-1, -1, 1),
    (0, -1, -1),
    (1, 1, 0.5)
)
Pyramid_Edges = (
    (0,1),(0,2),(0,3),
    (2,1),(2,3),(3,1)
)
Pyramid_Faces = (
    (0,1,2),
    (0,2,3),
    (0,3,1),
    (1,2,3)
)
Pyramid_Colours = (
    (1,0,0),(0,1,0),(0,0,1),(1,1,0)
)
#----------------------------------------------
# PRISM (triangular prism)
Prism_Vertices = (
    (-1, -1, 1),
    (1, -1, 1),
    (0, 1, 1),
    (-1, -1, -1),
    (1, -1, -1),
    (0, 1, -1)
)
Prism_Edges = (
    (0,1),(0,2),(1,2),
    (3,4),(3,5),(4,5),
    (0,3),(1,4),(2,5)
)
Prism_Faces = (
    (0,1,2),   # front triangle
    (3,4,5),   # back triangle
    (0,1,4,3), # bottom quad
    (1,2,5,4), # right quad
    (2,0,3,5)  # left quad
)
Prism_Colours = (
    (1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1)
)

# Toggle flag
colour_mode = False
texture_mode = False
autorotate = False

models = [ 
    (Cube_Vertices, Cube_Edges), 
    (Pyramid_Vertices, Pyramid_Edges), 
    (Prism_Vertices, Prism_Edges) 
] 

# Drawing function
def draw_model(vertices, edges): 
    glColor3fv((1,1,1))
    glBegin(GL_LINES) 
    for edge in edges: 
        for vertex in edge: 
            glVertex3fv(vertices[vertex]) 
    glEnd()

#Cube function
def Cube(textureID=None):
    #Texture
    if texture_mode and not colour_mode:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)
       
        glBegin(GL_QUADS)
        for face in Cube_Faces:
            texCoords = [(0,0),(1,0),(1,1),(0,1)] #texturre coordinates to fit shape
            for i, vertex in enumerate(face):
                glTexCoord2f(*texCoords[i])
                glVertex3fv(Cube_Vertices[vertex])
        glEnd()
        glDisable(GL_TEXTURE_2D)
    
    #Colour
    elif colour_mode and not texture_mode:
        glBegin(GL_QUADS)
        for i, face in enumerate(Cube_Faces):
            glColor3fv(Cube_Colours[i])
            for vertex in face:
                glVertex3fv(Cube_Vertices[vertex])
        glEnd()
        draw_model(Cube_Vertices, Cube_Edges) #makes sure the edges are white

    #tinting (texture + color)
    elif colour_mode and texture_mode:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)

        glBegin(GL_QUADS)
        for i, face in enumerate(Cube_Faces):
            glColor3fv(Cube_Colours[i])  # face tint
            texCoords = [(0,0),(1,0),(1,1),(0,1)]
            for j, vertex in enumerate(face):
                glTexCoord2f(*texCoords[j])
                glVertex3fv(Cube_Vertices[vertex])
        glEnd()
        glDisable(GL_TEXTURE_2D)

    else:
         #default shape with only white edges
         draw_model(Cube_Vertices, Cube_Edges)

#Pyramid Function         
def Pyramid(textureID = None):
    #adding Texture
    if texture_mode and not colour_mode:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D,textureID)

        glBegin(GL_TRIANGLES)
        for face in Pyramid_Faces:
            texcoords = [(0,0),(1,0),(0.5,1)]
            for i, vertex in enumerate(face):
                glTexCoord2f(*texcoords[i])
                glVertex3fv(Pyramid_Vertices[vertex])
        glEnd()
        glDisable(GL_TEXTURE_2D)
    
    #Colour
    elif colour_mode and not texture_mode:
        glBegin(GL_TRIANGLES)
        for i, face in enumerate(Pyramid_Faces):
            glColor3fv(Pyramid_Colours[i])
            for vertex in face:
                glVertex3fv(Pyramid_Vertices[vertex])
        glEnd()
        draw_model(Pyramid_Vertices, Pyramid_Edges) #makes sure edges are white
    
    #Tinting (combination of colour and texture)
    elif colour_mode and texture_mode:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)
        
        glBegin(GL_TRIANGLES)
        texcoords = [(0,0),(1,0),(0.5,1)] #texture coordinates for triangle faces
        for i, face in enumerate(Pyramid_Faces):
            #adding colour to each face
            glColor3fv(Pyramid_Colours[i])
            for j, vertex in enumerate(face):
                glTexCoord2f(*texcoords[j]) #adding texture to each face
                glVertex3fv(Pyramid_Vertices[vertex])
        glEnd()
        glDisable(GL_TEXTURE_2D)

    else:
         #default shape with only white edges
         draw_model(Pyramid_Vertices, Pyramid_Edges)

#Prism Function
def Prism(textureID=None):
    #adding texture
    if texture_mode and not colour_mode:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)

        for j,face in enumerate(Prism_Faces):
            if len(face) == 3:
                glBegin(GL_TRIANGLES)
                texCoords = [(0,0), (1,0), (0.5,1)] #texture coordinates for triangles
            else:
                glBegin(GL_QUADS)
                texCoords = [(0,0), (1,0), (1,1), (0,1)] #texture coordinates for squares
            for i, vertex in enumerate(face):
                glTexCoord2f(*texCoords[i]) #add texture to each face
                glVertex3fv(Prism_Vertices[vertex])
            glEnd()
        glDisable(GL_TEXTURE_2D)

    #Adding colour 
    elif colour_mode and not texture_mode:
        for i, face in enumerate(Prism_Faces):
            if len(face) == 3:
                glBegin(GL_TRIANGLES)
            else:
                glBegin(GL_QUADS)
            glColor3fv(Prism_Colours[i]) #adding colour to each face
            for vertex in face:
                glVertex3fv(Prism_Vertices[vertex])
            glEnd()
            draw_model(Prism_Vertices, Prism_Edges) #makes sure the edges are white

    #Tinting (combination of colour and texture)
    elif colour_mode and texture_mode:
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, textureID)

        for i, face in enumerate(Prism_Faces):
            #for each face apply a colour
            glColor3fv(Prism_Colours[i])
            if len(face) == 3:
               #apply texture to triangle faces
               glBegin(GL_TRIANGLES)
               texCoords = [(0,0),(1,0),(0.5,1)]
            else:
               glBegin(GL_QUADS)
               #apply texture to square faces
               texCoords = [(0,0),(1,0),(1,1),(0,1)]
            for j, vertex in enumerate(face):
                #for each face apply the texture
                glTexCoord2f(*texCoords[j])
                glVertex3fv(Prism_Vertices[vertex])
            glEnd()
        glDisable(GL_TEXTURE_2D)
    
    else:
         #default shape with only white edges
         draw_model(Prism_Vertices, Prism_Edges)


#addding texture function
def add_texture(image):
    textureSurface = pygame.image.load(image) #loads the texture image 
    textureData = pygame.image.tobytes(textureSurface,"RGB",True) #transfer image to a byte buffer
    width,height = textureSurface.get_size()
    textureID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D,textureID)
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,width,height,0,GL_RGB,GL_UNSIGNED_BYTE,textureData)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)
    return textureID

# Main loop
def main():
    global colour_mode
    global texture_mode
    global autorotate

    pygame.init()
    display = (800,600)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL|RESIZABLE)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0,-5.0)
    glEnable(GL_TEXTURE_2D)
    glTexEnvf(GL_TEXTURE_ENV,GL_TEXTURE_ENV_MODE,GL_MODULATE)
    glEnable(GL_DEPTH_TEST)

    #textures
    grateTexID = add_texture("grate.jpg")
    mudTexID = add_texture("mud.jpg")
    stoneWallID = add_texture("stonewall.jpg")

    currentModel = 0 # 0=cube 1=pyramid 2=prism
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                #change models
                if event.key == K_SPACE:
                    currentModel = (currentModel + 1) % 3

                    #change color
                if event.key == K_c:
                    # Toggle colour mode
                    colour_mode = not colour_mode
                    texture_mode = False

                    #add texture
                if event.key == K_t:
                    texture_mode = not texture_mode
                    colour_mode = False
                
                #tinting
                if event.key == K_b:
                    colour_mode = True
                    texture_mode = True

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
            
                #rotation
                if event.key == K_r:
                        autorotate = not autorotate
        
        if autorotate:
                glRotatef(1,3,1,0)
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if currentModel == 0: 
            #apply the texture to the model
            Cube(grateTexID)
        elif currentModel == 1:
             #apply the texture to the model
            Pyramid(mudTexID)
        elif currentModel == 2: 
             #apply the texture to the model
            Prism(stoneWallID)
      
        pygame.display.flip()
        pygame.time.wait(10)

main()
