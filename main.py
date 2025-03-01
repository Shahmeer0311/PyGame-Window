#import library
import pygame 
#initialise required modules
pygame.init()
#setUp Window Geometry
screen = pygame.display.set_mode((400,500))
#create a loop to run till the game is quit by the user 
while True:
#clear the evnt queue 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    #make the changes visable
    pygame.display.flip()