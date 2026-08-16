import sys,pygame ,random#importing pygame modules
from pygame.locals import *
pygame.init() #initializes pygame modules
pygame.mixer.init() #initializes the mixer module for playing sounds

pygame.display.set_caption("Bouncing Ball Animation") #sets the title of the display window
size = width, height = 800, 600  #this is the size of the display window
speed = [2, 2]
background_color = 0, 0, 0
screen = pygame.display.set_mode(size,RESIZABLE) #creates the display window with the specified size and allows it to be resized
ball = pygame.image.load("intro_ball.gif").convert_alpha() #loads the image of the ball from the specified file path
ballrect = ball.get_rect(center=(width//2, height//2)) #gets the rectangular area of the ball image and sets its center to the middle of the display window
sound = pygame.mixer.Sound("bounce_sound.mp3") #loads the sound effect for the ball bouncing from the specified file path

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    ballrect = ballrect.move(speed) #moves the ball by the current speed in both x and y directions
    #reverses the speed if the ball has moved outside the display window boundaries, creating a bouncing effect
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        #fills the screen with a new random background color when the ball hits the left or right edge of the window
        background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #changes the background color to a random color when the ball hits the left or right edge of the window
        sound.play() #plays the bounce sound effect when the ball hits the left or right edge of the window
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #changes the background color to a random color when the ball hits the top or bottom edge of the window
        sound.play() 
    screen.fill(background_color)
    #drawing of images is hanlded by the surface.blit() method, which takes two arguments: the source surface (the image to be drawn) and the destination rectangle (the position and size of the area where the image will be drawn).
    screen.blit(ball, ballrect) #draws the ball image onto the display window at the position specified by ballrect
    pygame.display.flip() #makes everything drawn on the display window visible by updating the entire display
    pygame.time.delay(10) #takes in milliseconds as an argument and pauses the execution of the program for that amount of time, creating a delay between each frame of the animation.