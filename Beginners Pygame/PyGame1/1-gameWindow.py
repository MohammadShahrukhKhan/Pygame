'''creating game window'''
import pygame

pygame.init() #to initialize the pygame

screen = pygame.display.set_mode((800, 600)) #width and height

# Game Loop 
running = True
while running:
    #this makes sure all the events happening in the pygame gets into this 
    # and check one by one if the cross button has been pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
