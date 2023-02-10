import pygame
from Utilities import WIDTH, HEIGHT, BACKGROUND_COLOUR, WINDOW_NAME

pygame.init()
#Window size
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#Caption of window
pygame.display.set_caption(WINDOW_NAME)
#Fill window background with the chosen colour
screen.fill(BACKGROUND_COLOUR)
#Font

myfont = pygame.font.SysFont("achelas.tff",72) # use default system font, size 10
mytext = myfont.render('HEX', True, (255, 100, 100))
screen.blit(mytext, (WIDTH*0.45,0)) # put the text in top left corner of screen

#Update window
pygame.display.flip()
#Keep window running
running = True

while running:
    # for loop through the event queue
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            running = False